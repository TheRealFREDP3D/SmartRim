import time
import json
import os
from datetime import datetime
from mcp_client import McpClient
from config import *


def ensure_dirs():
    os.makedirs(ALERTS_DIR, exist_ok=True)
    os.makedirs(SNAPSHOTS_DIR, exist_ok=True)


def _is_urgent_label(label):
    low = (label or "").lower()
    return any(kw in low for kw in URGENT_KEYWORDS)


def run_reflex_checks(client):
    alerts = []
    timestamp = datetime.now().isoformat()

    try:
        status = client.call_tool("get_status")
        if not status or not isinstance(status, dict) or status.get("error"):
            alerts.append(
                {
                    "type": "error",
                    "category": "system",
                    "message": f"get_status failed: {status}",
                    "timestamp": timestamp,
                }
            )
            return alerts

        colonists = (
            status.get("bundled", {})
            .get("list_colonists", {})
            .get("colonists", [])
        )
        # Fallback if not bundled
        if not colonists:
            cr = client.call_tool("list_colonists")
            if isinstance(cr, dict):
                colonists = cr.get("colonists", [])

        for colonist in colonists:
            name = colonist.get("name", "Unknown")
            mood = colonist.get("mood")
            health = colonist.get("health")
            downed = colonist.get("downed")

            if downed:
                alerts.append(
                    {
                        "type": "urgent",
                        "category": "downed",
                        "message": f"{name} is DOWNED",
                        "timestamp": timestamp,
                    }
                )

            if mood is not None and mood < MOOD_THRESHOLD:
                alerts.append(
                    {
                        "type": "warning",
                        "category": "mood",
                        "message": f"{name} mood at {mood}% (below {MOOD_THRESHOLD}%)",
                        "timestamp": timestamp,
                    }
                )

            if health is not None and health < HEALTH_THRESHOLD:
                alerts.append(
                    {
                        "type": "urgent",
                        "category": "health",
                        "message": f"{name} health at {health}%",
                        "timestamp": timestamp,
                    }
                )

        # Game alerts (danger rating, active alerts)
        bundled_alerts = (
            status.get("bundled", {}).get("get_alerts", {})
        )
        if not bundled_alerts:
            bundled_alerts = client.call_tool("get_alerts") or {}

        danger_by_map = bundled_alerts.get("dangerByMap", [])
        for d in danger_by_map:
            rating = d.get("dangerRating", "None")
            if rating and rating.lower() not in ("none", "null"):
                urgent = rating.lower() in ("high", "extreme", "danger")
                alerts.append(
                    {
                        "type": "urgent" if urgent else "warning",
                        "category": "danger_rating",
                        "message": f"Map {d.get('mapIndex')} danger rating: {rating}",
                        "timestamp": timestamp,
                    }
                )

        for alert in bundled_alerts.get("activeAlerts", []):
            label = alert.get("label", "")
            alert_type = "urgent" if _is_urgent_label(label) else "warning"
            alerts.append(
                {
                    "type": alert_type,
                    "category": "game_alert",
                    "message": label,
                    "timestamp": timestamp,
                }
            )

        # Hostile proximity: any pawn reported as hostile near the base.
        try:
            pawns_resp = client.call_tool("list_things", {"category": "pawn"})
            things = []
            if isinstance(pawns_resp, dict):
                things = pawns_resp.get("things", []) or pawns_resp.get("pawns", [])
            for t in things:
                hostile = (
                    t.get("hostile")
                    or t.get("isHostile")
                    or (str(t.get("faction", "")).lower() in ("hostile", "enemy", "raider"))
                )
                if hostile:
                    alerts.append(
                        {
                            "type": "urgent",
                            "category": "hostile",
                            "message": f"Hostile pawn nearby: {t.get('label') or t.get('name') or t.get('def')}",
                            "timestamp": timestamp,
                        }
                    )
        except Exception:
            pass

        # Colony death detection
        colonist_count = status.get("colonistCount", 0)
        if colonist_count == 0:
            alerts.append(
                {
                    "type": "urgent",
                    "category": "colony_death",
                    "message": "All colonists dead — debrief recommended",
                    "timestamp": timestamp,
                }
            )

    except Exception as e:
        alerts.append(
            {
                "type": "error",
                "category": "system",
                "message": f"Reflex check failed: {str(e)}",
                "timestamp": timestamp,
            }
        )

    return alerts


def write_snapshot(client, day_label):
    snapshot = {
        "day": day_label,
        "timestamp": datetime.now().isoformat(),
        "status": client.call_tool("get_status"),
        "conditions": client.call_tool("get_conditions"),
        "colonists": client.call_tool("list_colonists"),
        "resources": client.call_tool("get_resources"),
        "research": client.call_tool("get_research"),
        "alerts": client.call_tool("get_alerts"),
    }

    safe = str(day_label).replace("/", "-").replace("\\", "-")
    path = os.path.join(SNAPSHOTS_DIR, f"day-{safe}.json")
    with open(path, "w") as f:
        json.dump(snapshot, f, indent=2, default=str)
    return path


def main():
    ensure_dirs()
    client = McpClient(MCP_URL)
    last_day = None
    snapshotted_day = None

    print(f"Reflex monitor started. Polling every {POLL_INTERVAL}s")
    print(f"Alerts: {ALERTS_DIR}")
    print(f"Snapshots: {SNAPSHOTS_DIR}")

    while True:
        try:
            conditions = client.call_tool("get_conditions")
            if not conditions or not isinstance(conditions, dict) or conditions.get("error"):
                time.sleep(POLL_INTERVAL)
                continue

            current_day = conditions.get("date")
            current_hour = conditions.get("hour")

            # Day rollover -> snapshot the day that just ended (label = previous day).
            # Contents still carry conditions.date, so the exact timestamp is preserved.
            if current_day is not None and current_day != last_day:
                if last_day is not None and snapshotted_day != last_day:
                    path = write_snapshot(client, last_day)
                    print(f"Snapshot written: {path}")
                    snapshotted_day = last_day
                last_day = current_day

            # Hour change -> reflex checks
            # Run every poll? Keep hourly trigger but also run on first poll.
            alerts = run_reflex_checks(client)
            alert_path = os.path.join(ALERTS_DIR, "current.json")
            with open(alert_path, "w") as f:
                json.dump(alerts, f, indent=2)

            urgent = [a for a in alerts if a.get("type") == "urgent"]
            if urgent:
                print(f"{len(alerts)} alert(s) ({len(urgent)} urgent) - pausing game")
                try:
                    client.call_tool("set_speed", {"action": "pause"})
                except Exception:
                    pass
                # Colony death -> snapshot current day
                if any(a.get("category") == "colony_death" for a in alerts):
                    if snapshotted_day != current_day:
                        path = write_snapshot(client, current_day)
                        print(f"Death snapshot written: {path}")
                        snapshotted_day = current_day
            elif alerts:
                print(f"{len(alerts)} alert(s) ({len(urgent)} urgent)")

        except Exception as e:
            print(f"Error: {e}")

        time.sleep(POLL_INTERVAL)


if __name__ == "__main__":
    main()
