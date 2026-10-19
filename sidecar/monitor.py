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


def _predator_kinds():
    return {
        "cougar", "panther", "lynx", "cobra", "grizzly bear", "polar bear",
        "arctic fox", "arctic wolf", "fennec fox", "red fox", "timber wolf",
        "warg", "alligator", "greatwolf", "scimitar cat", "tiger",
        "wolverine",
    }


def run_reflex_checks(client, deep=False):
    alerts = []
    timestamp = datetime.now().isoformat()

    try:
        status = client.call_tool("get_status")
        if not status or not isinstance(status, dict) or status.get("error"):
            alerts.append({"type": "error", "category": "system", "message": f"get_status failed: {status}", "timestamp": timestamp})
            return alerts

        if status.get("loaded") is False or status.get("programState") in ("Entry", "Menu"):
            return []

        colonists = (
            status.get("bundled", {}).get("list_colonists", {}).get("colonists", [])
        )
        if not colonists:
            cr = client.call_tool("list_colonists")
            if isinstance(cr, dict):
                colonists = cr.get("colonists", [])

        colonist_positions = []
        for colonist in colonists:
            name = colonist.get("name", "Unknown")
            mood = colonist.get("mood")
            health = colonist.get("health")
            downed = colonist.get("downed")
            cid = colonist.get("id")

            if downed:
                alerts.append({"type": "urgent", "category": "downed", "message": f"{name} is DOWNED", "timestamp": timestamp})

            if mood is not None:
                if mood < MOOD_EXTREME_THRESHOLD:
                    alerts.append({"type": "urgent", "category": "mood_extreme", "message": f"{name} mood at {mood}% (extreme break risk)", "timestamp": timestamp})
                elif mood < MOOD_MAJOR_THRESHOLD:
                    alerts.append({"type": "urgent", "category": "mood_major", "message": f"{name} mood at {mood}% (major break risk)", "timestamp": timestamp})
                elif mood < MOOD_MINOR_THRESHOLD:
                    alerts.append({"type": "warning", "category": "mood_minor", "message": f"{name} mood at {mood}% (minor break risk)", "timestamp": timestamp})

            if health is not None and health < HEALTH_THRESHOLD:
                alerts.append({"type": "urgent", "category": "health", "message": f"{name} health at {health}%", "timestamp": timestamp})

            if cid:
                try:
                    p = client.call_tool("get_pawn", {"id": cid})
                    if isinstance(p, dict) and p.get("x") is not None:
                        colonist_positions.append((name, p.get("x"), p.get("z")))
                except Exception:
                    pass

        bundled_alerts = status.get("bundled", {}).get("get_alerts", {})
        if not bundled_alerts:
            bundled_alerts = client.call_tool("get_alerts") or {}

        for d in (bundled_alerts.get("dangerByMap", []) if isinstance(bundled_alerts, dict) else []):
            rating = d.get("dangerRating", "None")
            if rating and str(rating).lower() not in ("none", "null"):
                urgent = str(rating).lower() in ("high", "extreme", "danger")
                alerts.append({"type": "urgent" if urgent else "warning", "category": "danger_rating", "message": f"Map {d.get('mapIndex')} danger rating: {rating}", "timestamp": timestamp})

        for alert in (bundled_alerts.get("activeAlerts", []) if isinstance(bundled_alerts, dict) else []):
            label = alert.get("label", "")
            low = label.lower()
            if "idle" in low:
                alerts.append({"type": "warning", "category": "idle_colonist", "message": label, "timestamp": timestamp})
                continue
            if "medical treatment" in low:
                alerts.append({"type": "warning", "category": "medical_treatment_needed", "message": label, "timestamp": timestamp})
                continue
            if "low food" in low:
                alerts.append({"type": "warning", "category": "food_low", "message": label, "timestamp": timestamp})
                continue
            alert_type = "urgent" if _is_urgent_label(label) else "warning"
            alerts.append({"type": alert_type, "category": "game_alert", "message": label, "timestamp": timestamp})

        # Hostile and predator proximity (deep check only, every 3rd poll)
        if deep:
            try:
                pawns_resp = client.call_tool("list_things", {"category": "pawn"})
                things = pawns_resp.get("things", []) if isinstance(pawns_resp, dict) else []
                for t in things:
                    hostile = t.get("hostile") or t.get("isHostile") or (str(t.get("faction", "")).lower() in ("hostile", "enemy", "raider"))
                    if hostile:
                        hx, hz = t.get("x"), t.get("z")
                        near = False
                        if hx is not None and hz is not None:
                            for (_, cx, cz) in colonist_positions:
                                if cx is not None and cz is not None and abs(hx - cx) + abs(hz - cz) <= 15:
                                    near = True
                        alerts.append({"type": "urgent" if near else "warning", "category": "hostile", "message": f"Hostile pawn nearby: {t.get('label') or t.get('name') or t.get('def')} at ({hx},{hz}){' (near colonist)' if near else ''}", "timestamp": timestamp})
            except Exception:
                pass

            try:
                wl = client.call_tool("list_wildlife")
                animals = wl.get("animals", []) if isinstance(wl, dict) else []
                predators = _predator_kinds()
                for a in animals:
                    kind = str(a.get("kind", "")).lower()
                    if any(p in kind for p in predators):
                        ax, az = a.get("x"), a.get("z")
                        if ax is not None and az is not None:
                            for (_, cx, cz) in colonist_positions:
                                if cx is not None and cz is not None and abs(ax - cx) + abs(az - cz) <= 15:
                                    alerts.append({"type": "urgent", "category": "predator_near", "message": f"Predator ({a.get('kind')}) near colonist at ({ax},{az})", "timestamp": timestamp})
                                    break
            except Exception:
                pass

        # Resource checks (food, medicine) - advisory only
        try:
            res = client.call_tool("get_resources")
            if isinstance(res, dict) and not res.get("error"):
                res_list = res.get("resources", [])
                res_map = {(r.get("defName") or r.get("label")): r.get("count", 0) for r in res_list if isinstance(r, dict)}
                med = sum(v for k, v in res_map.items() if "medicine" in str(k).lower())
                if med < 5:
                    alerts.append({"type": "warning", "category": "medicine_low", "message": f"Medicine stock low ({med})", "timestamp": timestamp})
                food = 0
                for k, v in res_map.items():
                    kl = str(k).lower()
                    if "meal" in kl or "rice" in kl or "corn" in kl or "potato" in kl or "berry" in kl or "meat" in kl or "bread" in kl:
                        food += v
                if food < 20:
                    alerts.append({"type": "warning", "category": "food_low", "message": f"Food stock low ({food} units)", "timestamp": timestamp})
        except Exception:
            pass

        # Colony death detection
        colonist_count = status.get("colonistCount", 0)
        days_now = status.get("daysPassed", 0)
        if colonist_count == 0 and days_now and days_now > 0:
            alerts.append({"type": "urgent", "category": "colony_death", "message": "All colonists dead — debrief recommended", "timestamp": timestamp})

        # Sleeping during a threat
        try:
            if isinstance(bundled_alerts, dict):
                threat_labels = [a.get("label", "") for a in bundled_alerts.get("activeAlerts", [])]
                if any("raid" in l.lower() or "attack" in l.lower() or "enemy" in l.lower() for l in threat_labels):
                    for colonist in colonists:
                        job = str(colonist.get("job", "")).lower()
                        if "sleep" in job or "rest" in job:
                            alerts.append({"type": "urgent", "category": "sleeping_during_threat", "message": f"{colonist.get('name')} is sleeping during a threat", "timestamp": timestamp})
        except Exception:
            pass

    except Exception as e:
        alerts.append({"type": "error", "category": "system", "message": f"Reflex check failed: {str(e)}", "timestamp": timestamp})

    return alerts


def normalize_snapshot(snapshot):
    try:
        status = snapshot.get("status", {}) or {}
        conditions = snapshot.get("conditions", {}) or {}
        colonists_wrap = snapshot.get("colonists", {}) or {}
        colonists = colonists_wrap.get("colonists", []) if isinstance(colonists_wrap, dict) else []
        resources_wrap = snapshot.get("resources", {}) or {}
        res_list = resources_wrap.get("resources", []) if isinstance(resources_wrap, dict) else []
        alerts_wrap = snapshot.get("alerts", {}) or {}
        active_alerts = alerts_wrap.get("activeAlerts", []) if isinstance(alerts_wrap, dict) else []

        moods = [c.get("mood") for c in colonists if isinstance(c, dict) and c.get("mood") is not None]
        healths = [c.get("health") for c in colonists if isinstance(c, dict) and c.get("health") is not None]
        downed = [c.get("name") for c in colonists if isinstance(c, dict) and c.get("downed")]

        res_map = {}
        for r in res_list:
            if isinstance(r, dict):
                res_map[r.get("defName") or r.get("label")] = r.get("count", 0)

        snapshot["summary"] = {
            "day": conditions.get("date") or snapshot.get("day"),
            "hour": conditions.get("hour"),
            "season": conditions.get("seasonLabel"),
            "temp": (conditions.get("temperature", {}) or {}).get("outdoorC") if isinstance(conditions.get("temperature"), dict) else None,
            "colonist_count": status.get("colonistCount"),
            "min_mood": min(moods) if moods else None,
            "min_health": min(healths) if healths else None,
            "downed": downed,
            "alerts": [a.get("label") for a in active_alerts if isinstance(a, dict)],
            "resources": res_map,
            "wealth": status.get("wealthTotal") or (resources_wrap.get("wealthTotal") if isinstance(resources_wrap, dict) else None),
            "difficulty": status.get("difficulty"),
            "storyteller": status.get("storyteller"),
            "biome": None,
        }
    except Exception:
        snapshot["summary"] = {"error": "normalization failed"}
    return snapshot


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
    normalize_snapshot(snapshot)

    safe = str(day_label).replace("/", "-").replace("\\", "-")
    path = os.path.join(SNAPSHOTS_DIR, f"day-{safe}.json")
    with open(path, "w") as f:
        json.dump(snapshot, f, indent=2, default=str)
    return path


PID_FILE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "memory", "monitor.pid")


def _acquire_lock():
    if os.path.exists(PID_FILE):
        try:
            with open(PID_FILE) as f:
                old_pid = int(f.read().strip())
            try:
                os.kill(old_pid, 0)
                print(f"Monitor already running (PID {old_pid}). Exiting.")
                return False
            except OSError:
                pass
        except (ValueError, OSError):
            pass
    with open(PID_FILE, "w") as f:
        f.write(str(os.getpid()))
    return True


def _release_lock():
    try:
        if os.path.exists(PID_FILE):
            with open(PID_FILE) as f:
                pid = int(f.read().strip())
            if pid == os.getpid():
                os.remove(PID_FILE)
    except (ValueError, OSError):
        pass


def run_length_reached(days_passed, run_days=None):
    run_days = RUN_DAYS if run_days is None else run_days
    return days_passed is not None and days_passed >= run_days


def write_run_end(client, run_id, days_passed):
    try:
        client.call_tool("set_speed", {"action": "pause"})
    except Exception:
        pass
    final_day = f"end-day-{days_passed}"
    path = write_snapshot(client, final_day)
    runs_dir = os.path.join(os.path.dirname(ALERTS_DIR), "runs")
    os.makedirs(runs_dir, exist_ok=True)
    marker = os.path.join(runs_dir, f"{run_id}.end.json")
    with open(marker, "w", encoding="utf-8") as f:
        json.dump({
            "run_id": run_id,
            "run_days": RUN_DAYS,
            "days_passed": days_passed,
            "ended_at": datetime.now().isoformat(),
            "final_snapshot": path,
        }, f, indent=2)
    return marker


def main():
    ensure_dirs()
    if not _acquire_lock():
        return
    client = McpClient(MCP_URL, delay=MCP_DELAY)
    last_day = None
    snapshotted_day = None
    consecutive_errors = 0
    run_ended = False
    poll_count = 0

    print(f"Reflex monitor started. Polling every {POLL_INTERVAL}s (PID {os.getpid()})")
    print(f"Alerts: {ALERTS_DIR}")
    print(f"Snapshots: {SNAPSHOTS_DIR}")

    try:
        while True:
            try:
                conditions = client.call_tool("get_conditions")
                if not conditions or not isinstance(conditions, dict) or conditions.get("error"):
                    consecutive_errors += 1
                    if consecutive_errors >= 5:
                        alert_path = os.path.join(ALERTS_DIR, "current.json")
                        with open(alert_path, "w") as f:
                            json.dump([{"type": "urgent", "category": "system", "message": f"MCP unreachable for {consecutive_errors} polls", "timestamp": datetime.now().isoformat()}], f, indent=2)
                    time.sleep(POLL_INTERVAL)
                    continue

                consecutive_errors = 0
                status_now = client.call_tool("get_status")
                days_now = status_now.get("daysPassed") if isinstance(status_now, dict) else None
                if run_length_reached(days_now) and not run_ended:
                    marker = write_run_end(client, RUN_ID, days_now)
                    print(f"RUN COMPLETE at {days_now} days (limit {RUN_DAYS}). Marker: {marker}")
                    run_ended = True
                    break

                current_day = conditions.get("date")

                if current_day is not None and current_day != last_day:
                    if last_day is not None and snapshotted_day != last_day:
                        path = write_snapshot(client, last_day)
                        print(f"Snapshot written: {path}")
                        snapshotted_day = last_day
                    last_day = current_day

                poll_count += 1
                deep = (poll_count % 3 == 0)
                alerts = run_reflex_checks(client, deep=deep)
                alert_path = os.path.join(ALERTS_DIR, "current.json")
                with open(alert_path, "w") as f:
                    json.dump(alerts, f, indent=2)

                urgent = [a for a in alerts if a.get("type") == "urgent"]
                if urgent:
                    print(f"{len(alerts)} alert(s) ({len(urgent)} urgent) - pausing game")
                    try:
                        import advice_log
                        advice_log.log_advice(
                            run_id=RUN_ID,
                            snapshot_day=current_day or "unknown",
                            trigger="reflex",
                            severity="urgent",
                            situation="; ".join(a.get("message", "") for a in urgent),
                            actions=[{"rank": 1, "action": "Pause game and assess", "rationale": "Reflex check triggered urgent alert"}],
                            risks=[{"label": a.get("message", ""), "severity": "urgent"} for a in urgent],
                            reflex_name=",".join(sorted(set(a.get("category", "") for a in urgent))),
                            auto_paused=True,
                        )
                    except Exception as e:
                        print(f"advice log error: {e}")
                    try:
                        client.call_tool("set_speed", {"action": "pause"})
                    except Exception:
                        pass
                    if any(a.get("category") == "colony_death" for a in alerts):
                        if snapshotted_day != current_day:
                            path = write_snapshot(client, current_day)
                            print(f"Death snapshot written: {path}")
                            snapshotted_day = current_day
                elif alerts:
                    print(f"{len(alerts)} alert(s)")

            except Exception as e:
                consecutive_errors += 1
                print(f"Error: {e}")
                if consecutive_errors >= 5:
                    alert_path = os.path.join(ALERTS_DIR, "current.json")
                    with open(alert_path, "w") as f:
                        json.dump([{"type": "urgent", "category": "system", "message": f"Monitor error: {e}", "timestamp": datetime.now().isoformat()}], f, indent=2)

            time.sleep(POLL_INTERVAL)
    finally:
        _release_lock()


if __name__ == "__main__":
    main()
