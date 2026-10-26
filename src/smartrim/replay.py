"""Replay harness for Layer 2 reflex actions.

Usage: python sidecar/replay.py <run_id> [snapshots_root]

Loads snapshots/<run_id>/day-*.json and reflex-*.json sorted by day. For each
consecutive pair (N, N+1) it builds the situation from snapshot N and evaluates
the reflex actor against a mock counselor (no real MCP writes). It then asserts
that the counselor calls which *would* fire are consistent with the state delta
observed in snapshot N+1 (e.g. drafted colonists appear drafted).
"""

import glob
import json
import os
import re
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from smartrim import situation
from smartrim.config import BASE_DIR
from smartrim.reflex_actor import (
    ACTIONS_FILE,
    HUMAN_ACTION_FILE,
    REFLEX_LOCK_FILE,
    REFLEX_PAUSE_FILE,
    ReflexActor,
)


class MockCounselor:
    """Records counselor calls instead of making MCP writes."""

    def __init__(self):
        self.calls = []

    def say(self, message):
        self.calls.append(("say", message))
        return {"shown": True}

    def draft(self, colonists):
        names = colonists if isinstance(colonists, list) else [colonists]
        self.calls.append(("draft", list(names)))
        return {"drafted": True}

    def undraft(self, colonists):
        names = colonists if isinstance(colonists, list) else [colonists]
        self.calls.append(("undraft", list(names)))
        return {"undrafted": True}

    def designate(self, designator, x1=None, z1=None, x2=None, z2=None, x=None, z=None):
        self.calls.append(("designate", {
            "designator": designator, "x1": x1, "z1": z1, "x2": x2, "z2": z2,
            "x": x, "z": z,
        }))
        return {"designated": True}

    def assign(self, colonist, building_id):
        self.calls.append(("assign", {"colonist": colonist, "building": building_id}))
        return {"assigned": True}


def _snapshot_sort_key(path):
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
    except (json.JSONDecodeError, OSError):
        return (9999, path)
    status = data.get("status") or {}
    dp = status.get("daysPassed")
    if dp is not None:
        try:
            return (int(dp), path)
        except (ValueError, TypeError):
            pass
    summary = data.get("summary") or {}
    day_label = summary.get("day") or data.get("day") or ""
    m = re.search(r"(\d+)", str(day_label))
    if m:
        try:
            return (int(m.group(1)), path)
        except (ValueError, TypeError):
            pass
    return (9999, path)


def _load_snapshots(run_id, snapshots_root):
    root = snapshots_root or os.path.join(BASE_DIR, "memory", "snapshots")
    dest = os.path.join(root, str(run_id))
    if not os.path.isdir(dest):
        return []
    paths = []
    for pattern in ("day-*.json", "reflex-*.json"):
        paths.extend(glob.glob(os.path.join(dest, pattern)))
    snaps = []
    for path in sorted(paths, key=_snapshot_sort_key):
        try:
            with open(path, encoding="utf-8") as f:
                snaps.append(json.load(f))
        except (json.JSONDecodeError, OSError):
            continue
    return snaps


def _game_state_from_snapshot(snap):
    status = snap.get("status") or {}
    conditions = snap.get("conditions") or {}
    colonists = snap.get("colonists")
    if isinstance(colonists, dict):
        colonists = colonists.get("colonists", [])
    elif not isinstance(colonists, list):
        colonists = []
    alerts = snap.get("alerts")
    if isinstance(alerts, dict):
        alerts = alerts.get("activeAlerts", [])
    elif not isinstance(alerts, list):
        alerts = []
    resources = snap.get("resources")
    if isinstance(resources, dict):
        resources = resources.get("resources", [])
    elif not isinstance(resources, list):
        resources = []
    temp = None
    temp_raw = conditions.get("temperature")
    if isinstance(temp_raw, dict):
        temp = temp_raw.get("outdoorC")
    return {
        "colony": status.get("colonyName"),
        "day": conditions.get("date") or snap.get("day"),
        "hour": conditions.get("hour"),
        "season": conditions.get("seasonLabel"),
        "temp": temp,
        "colonists": colonists,
        "alerts": alerts,
        "resources": resources,
    }


def _drafted_names(colonists):
    return {c.get("name") for c in colonists
            if isinstance(c, dict) and c.get("drafted") is True}


def _has_drafted_status(colonists):
    return any(isinstance(c, dict) and "drafted" in c for c in colonists)


def run_replay(run_id, snapshots_root=None):
    snaps = _load_snapshots(run_id, snapshots_root)
    if len(snaps) < 2:
        print(f"Replay {run_id}: need at least 2 snapshots, found {len(snaps)}")
        return 1

    # Opt into reflex actions with dry-run off so the mock counselor sees the
    # calls that *would* fire, without any real MCP writes.
    os.environ.setdefault("REFLEX_KILL", "0")
    os.environ.setdefault("REFLEX_DRY_RUN", "0")

    actor = ReflexActor(
        run_id=run_id,
        actions_file=os.environ.get("REFLEX_ACTIONS_FILE", ACTIONS_FILE),
        human_action_file=os.environ.get("REFLEX_HUMAN_ACTION_FILE", HUMAN_ACTION_FILE),
        lock_file=os.environ.get("REFLEX_LOCK_FILE", REFLEX_LOCK_FILE),
        pause_file=os.environ.get("REFLEX_PAUSE_FILE", REFLEX_PAUSE_FILE),
    )
    failures = 0
    checks = 0

    for i in range(len(snaps) - 1):
        cur, nxt = snaps[i], snaps[i + 1]
        cur_gs = _game_state_from_snapshot(cur)
        cur_day = cur_gs["day"]
        alerts = cur_gs["alerts"]
        sit = situation.build_situation(cur.get("summary") or cur, alerts)

        mock = MockCounselor()
        pair_actor = ReflexActor(
            run_id=run_id,
            actions_file=os.environ.get("REFLEX_ACTIONS_FILE", ACTIONS_FILE),
            human_action_file=os.environ.get("REFLEX_HUMAN_ACTION_FILE", HUMAN_ACTION_FILE),
            lock_file=os.environ.get("REFLEX_LOCK_FILE", REFLEX_LOCK_FILE),
            pause_file=os.environ.get("REFLEX_PAUSE_FILE", REFLEX_PAUSE_FILE),
            counselor_mod=mock,
        )
        results = pair_actor.evaluate(alerts, sit, cur_gs, current_day=cur_day)

        nxt_gs = _game_state_from_snapshot(nxt)
        drafted_before = _drafted_names(cur_gs["colonists"])
        drafted_after = _drafted_names(nxt_gs["colonists"])
        draftable = {c.get("name") for c in actor._draftable_colonists(cur_gs)}

        for result in results:
            if result.get("skipped_reason"):
                continue
            checks += 1
            action = result.get("action")
            if action == "draft_and_focus_fire" and result.get("executed"):
                if _has_drafted_status(nxt_gs["colonists"]):
                    missing = draftable - drafted_after
                    if missing:
                        failures += 1
                        print(f"  day {cur_day}: CONTRADICTION draft {sorted(draftable)} "
                              f"not reflected in next snapshot (still undrafted: {sorted(missing)})")
                    else:
                        print(f"  day {cur_day}: draft {sorted(draftable)} "
                              f"reflected in next snapshot")
                else:
                    newly = drafted_after - drafted_before
                    if newly:
                        print(f"  day {cur_day}: draft would fire; {sorted(newly)} drafted in next snapshot")
                    else:
                        print(f"  day {cur_day}: draft {sorted(draftable)} would fire "
                              f"(next snapshot carries no drafted status)")
            elif action in ("designate_firefighting", "assign_beds"):
                print(f"  day {cur_day}: {action} intent logged; no verifiable state delta in snapshots")

    if failures:
        print(f"REPLAY FAIL: {failures} of {checks} checks failed for {run_id}")
        return 1
    print(f"Replay {run_id}: {len(snaps)} snapshots, {checks} reflex actions evaluated, no contradictions")
    return 0


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    if not argv:
        print("Usage: python sidecar/replay.py <run_id> [snapshots_root]")
        return 2
    return run_replay(argv[0], argv[1] if len(argv) > 1 else None)


if __name__ == "__main__":
    sys.exit(main())
