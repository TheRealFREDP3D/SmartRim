import time
import json
import os
import sys
from datetime import datetime
from mcp_client import McpClient
from config import *

try:
    import situation as _situation
    import lessons as _lessons
except Exception:
    _situation = None
    _lessons = None


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

        colonist_count = status.get("colonistCount", 0)
        days_now = status.get("daysPassed", 0)
        if colonist_count == 0 and days_now and days_now > 0:
            alerts.append({"type": "urgent", "category": "colony_death", "message": "All colonists dead — debrief recommended", "timestamp": timestamp})

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

        food_items = 0
        for k, v in res_map.items():
            kl = str(k).lower()
            if "meal" in kl or "rice" in kl or "corn" in kl or "potato" in kl or "berry" in kl or "meat" in kl or "bread" in kl or "kibble" in kl:
                food_items += v
        colonist_count = status.get("colonistCount") or len(colonists)
        if colonist_count and colonist_count > 0:
            food_days = round(food_items / (colonist_count * 2), 1)
        else:
            food_days = None

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
            "food_days": food_days,
            "medicine_count": sum(v for k, v in res_map.items() if "medicine" in str(k).lower()),
            "wealth": status.get("wealthTotal") or (resources_wrap.get("wealthTotal") if isinstance(resources_wrap, dict) else None),
            "difficulty": status.get("difficulty"),
            "storyteller": status.get("storyteller"),
            "biome": None,
        }
    except Exception:
        snapshot["summary"] = {"error": "normalization failed"}
    return snapshot


def snapshot_dir_for(run_id, root=None):
    """Per-run snapshot directory. Empty run_id stays on the shared root (legacy)."""
    root = root or SNAPSHOTS_DIR
    if not run_id:
        return root
    return os.path.join(root, str(run_id))


def write_snapshot(client, day_label, run_id=None):
    run_id = RUN_ID if run_id is None else run_id
    snapshot = {
        "run_id": run_id,
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
    dest = snapshot_dir_for(run_id)
    os.makedirs(dest, exist_ok=True)
    path = os.path.join(dest, f"day-{safe}.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(snapshot, f, indent=2, default=str)
    return path


def adviser_acts(observe_only):
    """Adviser-off runs observe and snapshot, but do not pause or write advice."""
    return not observe_only


def configure_observe_only(argv=None):
    """CLI --observe-only overrides the OBSERVE_ONLY env var. Returns the flag."""
    argv = sys.argv[1:] if argv is None else argv
    if "--observe-only" in argv:
        return True
    if "--advise" in argv:
        return False
    return os.getenv("OBSERVE_ONLY", "0") == "1"


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


def write_run_end(client, run_id, days_passed, observe_only=False, urgent_alerts=0,
                  auto_pauses=0, stop_reason="run_length"):
    # Protocol stop, not an adviser pause. Both arms pause here so the window closes.
    try:
        client.call_tool("set_speed", {"action": "pause"})
    except Exception:
        pass
    final_day = f"end-day-{days_passed}"
    path = write_snapshot(client, final_day, run_id=run_id)
    status = {}
    try:
        with open(path, encoding="utf-8") as fh:
            status = (json.load(fh).get("status") or {})
    except (OSError, json.JSONDecodeError):
        status = {}
    runs_dir = os.path.join(os.path.dirname(ALERTS_DIR), "runs")
    os.makedirs(runs_dir, exist_ok=True)
    marker = os.path.join(runs_dir, f"{run_id}.end.json")
    with open(marker, "w", encoding="utf-8") as f:
        json.dump({
            "run_id": run_id,
            "arm": "off" if observe_only else "on",
            "observe_only": bool(observe_only),
            "run_days": RUN_DAYS,
            "days_passed": days_passed,
            "stop_reason": stop_reason,
            "urgent_alerts": urgent_alerts,
            "auto_pauses": auto_pauses,
            "difficulty": status.get("difficulty"),
            "storyteller": status.get("storyteller"),
            "ended_at": datetime.now().isoformat(),
            "snapshots_dir": snapshot_dir_for(run_id),
            "final_snapshot": path,
        }, f, indent=2)
    return marker


def _advice_context(client, status_now, conditions, alerts):
    """Build a situation and ranked actions. Never references loop-local names."""
    snap_summary = {}
    situation = {}
    actions = []
    linked = []
    try:
        snap_summary = normalize_snapshot({
            "status": status_now,
            "conditions": conditions,
            "colonists": client.call_tool("list_colonists"),
            "resources": client.call_tool("get_resources"),
            "alerts": client.call_tool("get_alerts"),
        }).get("summary") or {}
    except Exception:
        snap_summary = {}
    if _situation is not None:
        try:
            situation = _situation.build_situation(snap_summary, alerts)
            lessons_list = _lessons.load_lessons() if _lessons else []
            retrieved = _situation.retrieve(situation, lessons_list, limit=5)
            linked = [lesson.get("id") for lesson in retrieved]
            actions, _ = _situation.rank_actions(alerts, situation, retrieved, limit=5)
        except Exception as e:
            print(f"situation/lessons error: {e}")
    return snap_summary, situation, actions, linked


OBSERVE_ONLY = os.getenv("OBSERVE_ONLY", "0") == "1"


def _log_scheduled(client, status_now, conditions, alerts, day_label):
    import advice_log
    _, _, actions, linked = _advice_context(client, status_now, conditions, alerts)
    advice_log.log_advice(
        run_id=RUN_ID,
        snapshot_day=day_label or "unknown",
        trigger="scheduled",
        severity="info",
        situation=f"Daily assessment for {day_label}",
        actions=actions,
        linked_lessons=linked,
        auto_paused=False,
    )


def _log_urgent(client, status_now, conditions, alerts, urgent, day_label):
    import advice_log
    _, _, actions, linked = _advice_context(client, status_now, conditions, alerts)
    advice_log.log_advice(
        run_id=RUN_ID,
        snapshot_day=day_label or "unknown",
        trigger="reflex",
        severity="urgent",
        situation="; ".join(a.get("message", "") for a in urgent),
        actions=actions if actions else [{
            "rank": 1,
            "action": "Pause game and assess",
            "rationale": "Reflex check triggered urgent alert",
        }],
        risks=[{"label": a.get("message", ""), "severity": "urgent"} for a in urgent],
        linked_lessons=linked,
        reflex_name=",".join(sorted(set(a.get("category", "") for a in urgent))),
        auto_paused=True,
    )


def main():
    global OBSERVE_ONLY
    OBSERVE_ONLY = configure_observe_only()
    ensure_dirs()
    if not _acquire_lock():
        return
    client = McpClient(MCP_URL, delay=MCP_DELAY)
    last_day = None
    snapshotted_day = None
    consecutive_errors = 0
    run_ended = False
    poll_count = 0
    urgent_alerts = 0
    auto_pauses = 0

    print(f"Reflex monitor started. Polling every {POLL_INTERVAL}s (PID {os.getpid()}) "
          f"run={RUN_ID} observe_only={OBSERVE_ONLY}")
    print(f"Alerts: {ALERTS_DIR}")
    print(f"Snapshots: {snapshot_dir_for(RUN_ID)}")

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
                    marker = write_run_end(
                        client, RUN_ID, days_now, observe_only=OBSERVE_ONLY,
                        urgent_alerts=urgent_alerts, auto_pauses=auto_pauses,
                        stop_reason="run_length",
                    )
                    print(f"RUN COMPLETE at {days_now} days (limit {RUN_DAYS}). Marker: {marker}")
                    run_ended = True
                    break

                current_day = conditions.get("date")
                day_rolled = False

                if current_day is not None and current_day != last_day:
                    if last_day is not None and snapshotted_day != last_day:
                        path = write_snapshot(client, last_day)
                        print(f"Snapshot written: {path}")
                        snapshotted_day = last_day
                        day_rolled = True
                        if adviser_acts(OBSERVE_ONLY):
                            try:
                                import outcomes
                                with open(path, encoding="utf-8") as fh:
                                    closed = json.load(fh)
                                outcomes.close_outcomes(closed.get("summary") or {}, run_id=RUN_ID)
                            except Exception as e:
                                print(f"outcome close error: {e}")
                    last_day = current_day

                poll_count += 1
                deep = (poll_count % 3 == 0)
                alerts = run_reflex_checks(client, deep=deep)
                alert_path = os.path.join(ALERTS_DIR, "current.json")
                with open(alert_path, "w") as f:
                    json.dump(alerts, f, indent=2)

                if day_rolled and adviser_acts(OBSERVE_ONLY):
                    try:
                        _log_scheduled(client, status_now, conditions, alerts, current_day)
                    except Exception as e:
                        print(f"scheduled advice error: {e}")

                urgent = [a for a in alerts if a.get("type") == "urgent"]
                _sig = tuple(sorted((a.get("type"), a.get("category"), a.get("message")) for a in alerts))
                if _sig != getattr(main, "_last_sig", None):
                    main._last_sig = _sig
                    if urgent:
                        urgent_alerts += 1
                        print(f"{len(alerts)} alert(s) ({len(urgent)} urgent)")
                        if adviser_acts(OBSERVE_ONLY):
                            try:
                                _log_urgent(client, status_now, conditions, alerts, urgent, current_day)
                            except Exception as e:
                                print(f"advice log error: {e}")
                            try:
                                client.call_tool("set_speed", {"action": "pause"})
                                auto_pauses += 1
                            except Exception:
                                pass
                        if any(a.get("category") == "colony_death" for a in alerts) and not run_ended:
                            marker = write_run_end(
                                client, RUN_ID, days_now, observe_only=OBSERVE_ONLY,
                                urgent_alerts=urgent_alerts, auto_pauses=auto_pauses,
                                stop_reason="colony_death",
                            )
                            print(f"COLONY DEATH. Marker: {marker}")
                            run_ended = True
                            break
                    elif alerts:
                        print(f"{len(alerts)} alert(s): " + ", ".join(a.get("message", "") for a in alerts))
                    else:
                        print("No alerts.")

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
