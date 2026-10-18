import time
import json
import os
from datetime import datetime
from mcp_client import McpClient
from config import *


def ensure_dirs():
    os.makedirs(ALERTS_DIR, exist_ok=True)
    os.makedirs(SNAPSHOTS_DIR, exist_ok=True)


def run_reflex_checks(client):
    alerts = []
    timestamp = datetime.now().isoformat()

    try:
        status = client.call_tool("get_status")
        if not status or not isinstance(status, dict):
            return alerts

        colonists = (
            status.get("bundled", {})
            .get("list_colonists", {})
            .get("colonists", [])
        )
        for colonist in colonists:
            name = colonist.get("name", "Unknown")
            mood = colonist.get("mood")
            health = colonist.get("health")

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

        game_alerts = (
            status.get("bundled", {}).get("get_alerts", {}).get("activeAlerts", [])
        )
        for alert in game_alerts:
            label = alert.get("label", "")
            alert_type = (
                "urgent"
                if any(kw in label.lower() for kw in URGENT_KEYWORDS)
                else "warning"
            )
            alerts.append(
                {
                    "type": alert_type,
                    "category": "game_alert",
                    "message": label,
                    "timestamp": timestamp,
                }
            )

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


def write_snapshot(client, day):
    snapshot = {
        "day": day,
        "timestamp": datetime.now().isoformat(),
        "status": client.call_tool("get_status"),
        "conditions": client.call_tool("get_conditions"),
        "colonists": client.call_tool("list_colonists"),
        "resources": client.call_tool("get_resources"),
        "research": client.call_tool("get_research"),
        "alerts": client.call_tool("get_alerts"),
    }

    path = os.path.join(SNAPSHOTS_DIR, f"day-{day}.json")
    with open(path, "w") as f:
        json.dump(snapshot, f, indent=2, default=str)
    return path


def main():
    ensure_dirs()
    client = McpClient(MCP_URL)
    last_hour = None
    last_day = None

    print(f"Reflex monitor started. Polling every {POLL_INTERVAL}s")
    print(f"Alerts: {ALERTS_DIR}")
    print(f"Snapshots: {SNAPSHOTS_DIR}")

    while True:
        try:
            conditions = client.call_tool("get_conditions")
            if not conditions or not isinstance(conditions, dict):
                time.sleep(POLL_INTERVAL)
                continue

            current_hour = conditions.get("hour")
            current_day = conditions.get("date")

            # Day rollover -> snapshot
            if current_day != last_day and current_day is not None:
                if last_day is not None:
                    path = write_snapshot(client, last_day)
                    print(f"Snapshot written: {path}")
                last_day = current_day

            # Hour change -> reflex checks
            if current_hour != last_hour and current_hour is not None:
                alerts = run_reflex_checks(client)
                alert_path = os.path.join(ALERTS_DIR, "current.json")
                with open(alert_path, "w") as f:
                    json.dump(alerts, f, indent=2)
                if alerts:
                    urgent = [a for a in alerts if a["type"] == "urgent"]
                    print(f"{len(alerts)} alert(s) ({len(urgent)} urgent)")
                last_hour = current_hour

        except Exception as e:
            print(f"Error: {e}")

        time.sleep(POLL_INTERVAL)


if __name__ == "__main__":
    main()
