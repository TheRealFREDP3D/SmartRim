import glob
import json
import logging
import os
import sys
import time
from dataclasses import dataclass
from datetime import datetime
from typing import Any

from smartrim.config import (
    ALERTS_DIR,
    HEALTH_THRESHOLD,
    MCP_DELAY,
    MCP_URL,
    MOOD_EXTREME_THRESHOLD,
    MOOD_MAJOR_THRESHOLD,
    MOOD_MINOR_THRESHOLD,
    POLL_INTERVAL,
    RUN_DAYS,
    RUN_ID,
    SAY_DAILY_HOURS,
    SNAPSHOTS_DIR,
    URGENT_KEYWORDS,
)
from smartrim.logging_config import get_logger, setup_logging
from smartrim.mcp_client import McpClient, McpError

logger = get_logger(__name__)

try:
    from smartrim import situation as _lessons
    from smartrim import situation as _situation
except ImportError:
    _situation = None
    _lessons = None

try:
    from smartrim import quests as _quests
except ImportError:
    _quests = None

try:
    from smartrim import say_daily as _say_daily
except ImportError:
    _say_daily = None

# A reflex snapshot is taken when a new urgent alert appears, so incidents that start and
# end between two daily snapshots (a raid, a fire) still leave evidence for the debrief.
REFLEX_SNAPSHOT_LIMIT = 40


def ensure_dirs() -> None:
    os.makedirs(ALERTS_DIR, exist_ok=True)
    os.makedirs(SNAPSHOTS_DIR, exist_ok=True)


SIG_FILE = os.path.join(ALERTS_DIR, "last_signature.json")


def _load_last_sig() -> dict[str, Any] | None:
    """Load the last alert signature so a monitor restart does not re-log the same urgent set."""
    try:
        with open(SIG_FILE, encoding="utf-8") as f:
            data = json.load(f)
        if data.get("run_id") == RUN_ID and isinstance(data.get("sig"), list):
            return tuple(tuple(x) for x in data["sig"])
    except (OSError, json.JSONDecodeError, TypeError, KeyError):
        pass
    return None


def _save_last_sig(sig: dict[str, Any]) -> None:
    try:
        os.makedirs(ALERTS_DIR, exist_ok=True)
        with open(SIG_FILE, "w", encoding="utf-8") as f:
            json.dump({"run_id": RUN_ID, "sig": [list(x) for x in (sig or ())]}, f, indent=2)
    except (OSError, TypeError, ValueError) as e:
        logger.debug("sig save failed: %s", e)


def _is_urgent_label(label):
    low = (label or "").lower()
    return any(kw in low for kw in URGENT_KEYWORDS)




def run_reflex_checks(client: McpClient) -> list[dict[str, Any]]:
    alerts: list[dict[str, Any]] = []
    timestamp = datetime.now().isoformat()

    try:
        status = client.call_tool("get_status")
        if not status or not isinstance(status, dict) or status.get("error"):
            alerts.append({"type": "error", "category": "system", "message": f"get_status failed: {status}", "timestamp": timestamp})
            return alerts

        if status.get("loaded") is False or status.get("programState") in ("Entry", "Menu"):
            return []

        _bundled = status.get("bundled")
        if not isinstance(_bundled, dict):
            _bundled = {}
        colonists = (
            (_bundled.get("list_colonists") or {}).get("colonists", [])
            if isinstance(_bundled.get("list_colonists"), dict)
            else []
        )
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

        _bundled_alerts = (_bundled.get("get_alerts") if isinstance(_bundled, dict) else None)
        bundled_alerts = _bundled_alerts if isinstance(_bundled_alerts, dict) else {}
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

        # Predator proximity and hostile-near-colonist checks removed: these duplicate
        # in-game alerts (the game already warns about nearby hostiles and predators).
        # The game's own alert system (get_alerts) covers these cases.

        try:
            res = client.call_tool("get_resources")
            if isinstance(res, dict) and not res.get("error"):
                res_list = res.get("resources", [])
                # An empty readout means the game is still loading (or the readout failed);
                # it must not be reported as "medicine 0 / food 0".
                if res_list:
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
        except (McpError, OSError, ValueError, TypeError, KeyError, AttributeError):
            pass

        colonist_count = status.get("colonistCount", 0)
        days_now = status.get("daysPassed", 0)
        # Only call colony death once this process has actually seen the colony alive;
        # during a save load the status briefly reports zero colonists.
        if colonists:
            run_reflex_checks._seen_colonists = True
        if colonist_count == 0 and days_now and days_now > 0 and getattr(run_reflex_checks, "_seen_colonists", False):
            alerts.append({"type": "urgent", "category": "colony_death", "message": "All colonists dead — debrief recommended", "timestamp": timestamp})

        try:
            if isinstance(bundled_alerts, dict):
                threat_labels = [a.get("label", "") for a in bundled_alerts.get("activeAlerts", [])]
                if any("raid" in lbl.lower() or "attack" in lbl.lower() or "enemy" in lbl.lower() for lbl in threat_labels):
                    for colonist in colonists:
                        job = str(colonist.get("job", "")).lower()
                        if "sleep" in job or "rest" in job:
                            alerts.append({"type": "urgent", "category": "sleeping_during_threat", "message": f"{colonist.get('name')} is sleeping during a threat", "timestamp": timestamp})
        except (McpError, OSError, ValueError, TypeError, KeyError, AttributeError):
            pass

    except (McpError, OSError, ValueError, TypeError, KeyError, AttributeError, json.JSONDecodeError) as e:
        alerts.append({"type": "error", "category": "system", "message": f"Reflex check failed: {e!s}", "timestamp": timestamp})

    return alerts


def normalize_snapshot(snapshot: dict[str, Any]) -> dict[str, Any]:
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

        # Count ready-to-eat meals only. Raw ingredients (rice, corn, potatoes,
        # berries, meat, ...) are measured in harvest units, not meals, and must
        # not be mixed into the meal count (see run-005 starvation-with-full-pantry).
        food_items = 0
        for k, v in res_map.items():
            kl = str(k).lower()
            if ("meal" in kl) or ("pemmican" in kl) or ("kibble" in kl) or ("survival" in kl and "pack" in kl) or ("paste" in kl and "nutrient" in kl):
                food_items += v
        colonist_count = status.get("colonistCount") or len(colonists)
        if colonist_count and colonist_count > 0:
            food_days = round(food_items / (colonist_count * 2), 1)
        else:
            food_days = None

        snapshot["summary"] = {
            "day": conditions.get("date") or snapshot.get("day"),
            "days_passed": status.get("daysPassed") if isinstance(status, dict) else None,
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
    except (OSError, ValueError, TypeError, KeyError, AttributeError, json.JSONDecodeError) as e:
        logger.debug("snapshot normalization failed: %s", e)
        snapshot["summary"] = {"error": "normalization failed"}
    # Populate biome from run metadata when available, so biome-scoped lessons can match.
    try:
        if isinstance(snapshot.get("summary"), dict) and "error" not in snapshot["summary"]:
            rid = snapshot.get("run_id")
            if rid:
                meta_path = os.path.join(os.path.dirname(ALERTS_DIR), "runs", f"{rid}.meta.json")
                if os.path.exists(meta_path):
                    with open(meta_path, encoding="utf-8") as _f:
                        _meta = json.load(_f)
                    if isinstance(_meta, dict) and _meta.get("biome"):
                        snapshot["summary"]["biome"] = _meta.get("biome")
                else:
                    end_path = os.path.join(os.path.dirname(ALERTS_DIR), "runs", f"{rid}.end.json")
                    if os.path.exists(end_path):
                        with open(end_path, encoding="utf-8") as _f:
                            _end = json.load(_f)
                        if isinstance(_end, dict) and _end.get("biome"):
                            snapshot["summary"]["biome"] = _end.get("biome")
    except (OSError, ValueError, TypeError, KeyError, json.JSONDecodeError) as e:
        logger.debug("biome population failed: %s", e)
    return snapshot


def snapshot_dir_for(run_id, root=None):
    """Per-run snapshot directory. Empty run_id stays on the shared root (legacy)."""
    root = root or SNAPSHOTS_DIR
    if not run_id:
        return root
    return os.path.join(root, str(run_id))


def write_snapshot(client: McpClient, day_label: str, run_id: str | None = None, prefix: str = "day", quest_registry_path: str | None = None,
                   filename_stem=None):
    run_id = RUN_ID if run_id is None else run_id
    status = client.call_tool("get_status")
    conditions = client.call_tool("get_conditions")
    colonists = client.call_tool("list_colonists")
    resources = client.call_tool("get_resources")
    research = client.call_tool("get_research")
    alerts = client.call_tool("get_alerts")

    effective_day = day_label
    if prefix == "day" and not filename_stem and isinstance(conditions, dict):
        cond_date = conditions.get("date")
        if cond_date:
            effective_day = cond_date

    snapshot = {
        "run_id": run_id,
        "day": effective_day,
        "timestamp": datetime.now().isoformat(),
        "status": status,
        "conditions": conditions,
        "colonists": colonists,
        "resources": resources,
        "research": research,
        "alerts": alerts,
    }
    # Quest context. Optional: an older game build without get_quest must not break snapshots.
    if _quests is not None:
        try:
            snapshot["quests"] = _quests.update(client, day_label=str(effective_day), path=quest_registry_path)
        except (McpError, OSError, ValueError, TypeError, KeyError, AttributeError, json.JSONDecodeError) as e:
            logger.debug("quest update failed: %s", e)
            snapshot["quests"] = []
    normalize_snapshot(snapshot)

    safe = str(effective_day).replace("/", "-").replace("\\", "-")
    dest = snapshot_dir_for(run_id)
    os.makedirs(dest, exist_ok=True)
    stem = filename_stem or f"{prefix}-{safe}"
    path = os.path.join(dest, f"{stem}.json")
    if filename_stem:
        # Incident snapshots must each keep their own file, even if two fire in one second.
        suffix = 2
        while os.path.exists(path):
            path = os.path.join(dest, f"{stem}-{suffix}.json")
            suffix += 1
    with open(path, "w", encoding="utf-8") as f:
        json.dump(snapshot, f, indent=2, default=str)
    return path


def reflex_snapshot_name(now=None):
    """Filename stem for an incident snapshot. Sortable, filesystem-safe, no spaces."""
    now = now or datetime.now()
    return f"reflex-{now.strftime('%Y%m%d-%H%M%S')}"


def write_reflex_snapshot(client: McpClient, run_id: str | None = None, limit: int = REFLEX_SNAPSHOT_LIMIT, quest_registry_path: str | None = None) -> str | None:
    """Snapshot at the moment an urgent alert fires. Returns the path, or None when capped."""
    run_id = RUN_ID if run_id is None else run_id
    dest = snapshot_dir_for(run_id)
    if os.path.isdir(dest) and len(glob.glob(os.path.join(dest, "reflex-*.json"))) >= limit:
        return None
    return write_snapshot(client, reflex_snapshot_name(), run_id=run_id, prefix="reflex",
                         quest_registry_path=quest_registry_path,
                         filename_stem=reflex_snapshot_name())



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


PID_FILE = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "memory", "monitor.pid")


def _pid_alive(pid):
    """Check if a process with the given PID is alive. Windows-safe."""
    try:
        pid = int(pid)
    except (TypeError, ValueError):
        return False
    if pid <= 0:
        return False
    if os.name == "nt":
        try:
            import ctypes
            PROCESS_QUERY_LIMITED_INFORMATION = 0x1000
            STILL_ACTIVE = 259
            handle = ctypes.windll.kernel32.OpenProcess(PROCESS_QUERY_LIMITED_INFORMATION, False, pid)
            if not handle:
                return False
            try:
                code = ctypes.c_ulong()
                if not ctypes.windll.kernel32.GetExitCodeProcess(handle, ctypes.byref(code)):
                    return False
                return code.value == STILL_ACTIVE
            finally:
                ctypes.windll.kernel32.CloseHandle(handle)
        except (OSError, AttributeError, ValueError, TypeError):
            # If we cannot safely query, assume not alive to avoid blocking
            return False
    try:
        os.kill(pid, 0)
        return True
    except OSError:
        return False


def _acquire_lock() -> bool:
    if os.path.exists(PID_FILE):
        try:
            with open(PID_FILE) as f:
                old_pid = int(f.read().strip())
            if _pid_alive(old_pid):
                logger.warning(f"Monitor already running (PID {old_pid}). Exiting.")
                return False
        except (ValueError, OSError):
            pass
    import contextlib
    with contextlib.suppress(Exception):
        os.makedirs(os.path.dirname(PID_FILE), exist_ok=True)
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


def run_length_reached(days_passed: int, run_days: int | None = None) -> bool:
    run_days = RUN_DAYS if run_days is None else run_days
    return days_passed is not None and days_passed >= run_days


def write_run_end(client: McpClient, run_id: str, days_passed: int, observe_only: bool = False, urgent_alerts: int = 0,
                  auto_pauses=0, stop_reason="run_length", reflex_snapshots=0):
    # Protocol stop. Adviser-on runs pause so the window closes; observe-only runs
    # never pause (observe only, no intervention), even at the end of the run.
    if not observe_only:
        import contextlib
        with contextlib.suppress(Exception):
            client.call_tool("set_speed", {"action": "pause"})
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
            "reflex_snapshots": reflex_snapshots,
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
    except (McpError, OSError, ValueError, TypeError, KeyError, AttributeError, json.JSONDecodeError) as e:
        logger.debug("advice context snapshot failed: %s", e)
        snap_summary = {}
    if _situation is not None:
        try:
            situation = _situation.build_situation(snap_summary, alerts)
            lessons_list = _lessons.load_lessons() if _lessons else []
            retrieved = _situation.retrieve(situation, lessons_list, limit=5)
            linked = [lesson.get("id") for lesson in retrieved]
            actions, _ = _situation.rank_actions(alerts, situation, retrieved, limit=5)
        except (OSError, ValueError, TypeError, KeyError, AttributeError, json.JSONDecodeError) as e:
            logger.error(f"situation/lessons error: {e}")
    return snap_summary, situation, actions, linked


OBSERVE_ONLY = os.getenv("OBSERVE_ONLY", "0") == "1"


def _say_daily_message(client: McpClient, conditions: dict[str, Any], slot: str | None = None) -> bool:
    """Display a daily status + advice message via the in-game say command."""
    if _say_daily is None:
        return False
    try:
        hour = conditions.get("hour", 0) if isinstance(conditions, dict) else 0
        if slot is None:
            slot = "morning" if (isinstance(hour, int) and hour < 12) else "evening"
        use_llm = globals().get("SAY_DAILY_USE_LLM", False)
        message, _ = _say_daily.build_message(slot, use_llm=use_llm)
        result = client.call_tool("say", {"text": message})
        if isinstance(result, dict) and result.get("shown"):
            logger.info(f"Daily say ({slot}, hour {hour}): displayed {result.get('chars', 0)} chars")
            return True
        else:
            logger.warning(f"Daily say ({slot}): not shown: {result}")
            return False
    except (McpError, OSError, ValueError, TypeError, KeyError, AttributeError, json.JSONDecodeError, RuntimeError) as e:
        logger.error(f"Daily say error: {e}")
        return False


def _log_scheduled(client, status_now, conditions, alerts, day_label):
    from smartrim import advice_log
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
    from smartrim import advice_log
    situation = "; ".join(a.get("message", "") for a in urgent)
    # Do not re-log an identical urgent situation that is still open for this run
    # (monitor restarts used to duplicate advice records and auto-pause counts).
    try:
        if advice_log.find_open_duplicate(RUN_ID, situation):
            return None
    except (OSError, json.JSONDecodeError, ValueError, TypeError, KeyError) as e:
        logger.debug("find_open_duplicate failed: %s", e)
    _, _, actions, linked = _advice_context(client, status_now, conditions, alerts)
    advice_log.log_advice(
        run_id=RUN_ID,
        snapshot_day=day_label or "unknown",
        trigger="reflex",
        severity="urgent",
        situation=situation,
        actions=actions if actions else [{
            "rank": 1,
            "action": "Pause game and assess",
            "rationale": "Reflex check triggered urgent alert",
        }],
        risks=[{"label": a.get("message", ""), "severity": "urgent"} for a in urgent],
        linked_lessons=linked,
        reflex_name=",".join(sorted({a.get("category", "") for a in urgent})),
        auto_paused=True,
    )
    return situation


@dataclass
class PollResult:
    """Mutable state carried across poll iterations."""
    last_day: str | None = None
    snapshotted_day: str | None = None
    last_say_day: str | None = None
    last_say_hour: int | None = None
    consecutive_errors: int = 0
    poll_count: int = 0
    urgent_alerts: int = 0
    auto_pauses: int = 0
    reflex_snapshots: int = 0
    run_ended: bool = False
    last_sig: Any | None = None


def poll_once(client: McpClient, state: PollResult) -> PollResult:
    """Perform one monitoring iteration. Mutates and returns ``state``."""
    try:
        conditions = client.call_tool("get_conditions")
        if not conditions or not isinstance(conditions, dict) or conditions.get("error"):
            state.consecutive_errors += 1
            if state.consecutive_errors >= 5:
                alert_path = os.path.join(ALERTS_DIR, "current.json")
                with open(alert_path, "w") as f:
                    json.dump([{"type": "urgent", "category": "system", "message": f"MCP unreachable for {state.consecutive_errors} polls", "timestamp": datetime.now().isoformat()}], f, indent=2)
            return state

        state.consecutive_errors = 0
        status_now = client.call_tool("get_status")
        days_now = status_now.get("daysPassed") if isinstance(status_now, dict) else None
        if run_length_reached(days_now) and not state.run_ended:
            marker = write_run_end(
                client, RUN_ID, days_now, observe_only=OBSERVE_ONLY,
                urgent_alerts=state.urgent_alerts, auto_pauses=state.auto_pauses,
                stop_reason="run_length", reflex_snapshots=state.reflex_snapshots,
            )
            logger.info(f"RUN COMPLETE at {days_now} days (limit {RUN_DAYS}). Marker: {marker}")
            state.run_ended = True
            return state

        current_day = conditions.get("date")
        current_hour = conditions.get("hour", 0) if isinstance(conditions, dict) else 0
        day_rolled = False

        # Daily say: display status + advice at configured hours (default 6am and 6pm).
        # Display is observational (not an intervention), so it runs in every mode.
        try:
            if isinstance(current_hour, int) and current_hour in SAY_DAILY_HOURS:
                say_key = (current_day, current_hour)
                if say_key != (state.last_say_day, state.last_say_hour):
                    slot = "morning" if current_hour < 12 else "evening"
                    _say_daily_message(client, conditions, slot=slot)
                    state.last_say_day = current_day
                    state.last_say_hour = current_hour
        except (McpError, OSError, ValueError, TypeError, KeyError, AttributeError, json.JSONDecodeError, RuntimeError) as e:
            logger.error(f"Daily say check error: {e}")

        if current_day is not None and (state.last_day is None or current_day != state.last_day) and state.snapshotted_day != current_day:
            path = write_snapshot(client, current_day)
            logger.info(f"Snapshot written: {path}")
            state.snapshotted_day = current_day
            day_rolled = True
            if adviser_acts(OBSERVE_ONLY):
                try:
                    from smartrim import outcomes
                    with open(path, encoding="utf-8") as fh:
                        closed = json.load(fh)
                    outcomes.close_outcomes(closed.get("summary") or {}, run_id=RUN_ID)
                except (OSError, json.JSONDecodeError, ValueError, TypeError, KeyError) as e:
                    logger.error(f"outcome close error: {e}")
        if current_day is not None:
            state.last_day = current_day

        state.poll_count += 1
        alerts = run_reflex_checks(client)
        alert_path = os.path.join(ALERTS_DIR, "current.json")
        with open(alert_path, "w") as f:
            json.dump(alerts, f, indent=2)

        if day_rolled and adviser_acts(OBSERVE_ONLY):
            try:
                _log_scheduled(client, status_now, conditions, alerts, current_day)
            except (McpError, OSError, ValueError, TypeError, KeyError, AttributeError, json.JSONDecodeError, RuntimeError) as e:
                logger.error(f"scheduled advice error: {e}")

        urgent = [a for a in alerts if a.get("type") == "urgent"]
        _sig = tuple(sorted((a.get("type"), a.get("category"), a.get("message")) for a in alerts))
        if _sig != state.last_sig:
            state.last_sig = _sig
            _save_last_sig(_sig)
            if urgent:
                state.urgent_alerts += 1
                logger.warning(f"{len(alerts)} alert(s) ({len(urgent)} urgent)")
                # Display the urgent situation in-game via say (all modes).
                try:
                    msg = "URGENT: " + "; ".join(a.get("message", "") for a in urgent)
                    if adviser_acts(OBSERVE_ONLY):
                        try:
                            _, _, actions, _ = _advice_context(client, status_now, conditions, alerts)
                            if actions:
                                msg += " | Advice: " + "; ".join(ac.get("action", "") for ac in actions)
                        except (OSError, ValueError, TypeError, KeyError, AttributeError, json.JSONDecodeError):
                            pass
                    client.call_tool("say", {"text": msg})
                except (McpError, OSError, ValueError, TypeError, KeyError, AttributeError, json.JSONDecodeError, RuntimeError) as e:
                    logger.error(f"say urgent error: {e}")
                if adviser_acts(OBSERVE_ONLY):
                    logged = True
                    try:
                        logged = _log_urgent(client, status_now, conditions, alerts, urgent, current_day) is not None
                    except (McpError, OSError, ValueError, TypeError, KeyError, AttributeError, json.JSONDecodeError, RuntimeError) as e:
                        logger.error(f"advice log error: {e}")
                    try:
                        client.call_tool("set_speed", {"action": "pause"})
                        if logged:
                            state.auto_pauses += 1
                    except McpError as e:
                        logger.debug("set_speed pause failed: %s", e)
                try:
                    rpath = write_reflex_snapshot(client)
                    if rpath:
                        state.reflex_snapshots += 1
                        logger.info(f"Reflex snapshot: {rpath}")
                except (McpError, OSError, ValueError, TypeError, KeyError, AttributeError, json.JSONDecodeError) as e:
                    logger.error(f"reflex snapshot error: {e}")
                if any(a.get("category") == "colony_death" for a in alerts) and not state.run_ended:
                    marker = write_run_end(
                        client, RUN_ID, days_now, observe_only=OBSERVE_ONLY,
                        urgent_alerts=state.urgent_alerts, auto_pauses=state.auto_pauses,
                        stop_reason="colony_death", reflex_snapshots=state.reflex_snapshots,
                    )
                    logger.critical(f"COLONY DEATH. Marker: {marker}")
                    state.run_ended = True
            elif alerts:
                logger.info(f"{len(alerts)} alert(s): " + ", ".join(a.get("message", "") for a in alerts))
            else:
                logger.debug("No alerts.")

    except (McpError, OSError, ValueError, TypeError, KeyError, AttributeError, json.JSONDecodeError, RuntimeError, ImportError) as e:
        state.consecutive_errors += 1
        logger.error(f"Error: {e}")
        if state.consecutive_errors >= 5:
            alert_path = os.path.join(ALERTS_DIR, "current.json")
            with open(alert_path, "w") as f:
                json.dump([{"type": "urgent", "category": "system", "message": f"Monitor error: {e}", "timestamp": datetime.now().isoformat()}], f, indent=2)

    return state


def main() -> None:
    global OBSERVE_ONLY
    # Configure the root logger before anything else, otherwise every logger.info()
    # below is discarded (no handlers) and the monitor appears silent.
    setup_logging(logging.INFO)
    OBSERVE_ONLY = configure_observe_only()
    ensure_dirs()
    if not _acquire_lock():
        return
    client = McpClient(MCP_URL, delay=MCP_DELAY)

    logger.info(f"Reflex monitor started. Polling every {POLL_INTERVAL}s (PID {os.getpid()}) "
                f"run={RUN_ID} observe_only={OBSERVE_ONLY}")
    logger.info(f"Alerts: {ALERTS_DIR}")
    logger.info(f"Snapshots: {snapshot_dir_for(RUN_ID)}")

    state = PollResult(last_sig=_load_last_sig())
    try:
        while not state.run_ended:
            state = poll_once(client, state)
            time.sleep(POLL_INTERVAL)
    finally:
        _release_lock()


if __name__ == "__main__":
    main()
