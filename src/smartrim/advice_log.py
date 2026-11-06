"""Advice log: append-only JSONL of every piece of advice given, with outcome tracking.

This module is the single owner of ``runtime/<run>/advice.jsonl``: every read and every
rewrite (update_outcome, set_event_cause, outcomes.close_outcomes, expire_stale) goes
through ``read_advice`` / ``_read_all`` / ``save_atomic`` here, so there is exactly one
atomic-write implementation to keep correct.
"""

import json
import os
import uuid
from datetime import datetime, timedelta

from smartrim import config

# Optional overrides for tests/tooling. None means "the active run's ledger":
# runtime/<run_id>/advice.jsonl
ADVICE_DIR: str | None = None
ADVICE_FILE: str | None = None


def _advice_path(create: bool = False) -> str | None:
    if ADVICE_FILE:
        return ADVICE_FILE
    if ADVICE_DIR:
        return os.path.join(ADVICE_DIR, "advice.jsonl")
    return config.advice_file(create=create)


def _ensure_dir():
    path = _advice_path(create=True)
    if path:
        os.makedirs(os.path.dirname(path), exist_ok=True)


def new_advice_id():
    return "adv-" + datetime.now().strftime("%Y%m%d-%H%M%S") + "-" + uuid.uuid4().hex[:6]


def log_advice(run_id, snapshot_day, trigger, severity, situation, actions,
               risks=None, watch_next=None, linked_lessons=None, reflex_name=None,
               auto_paused=False, llm_model=None, context_tokens=None, event_cause=None,
               days_passed=None):
    """Append one advice record. Returns the advice_id.

    event_cause is auto-tagged at log time from the game's own alerts (see
    smartrim.event_cause); a human may override it later with set_event_cause
    / set_cause_matching ("raider arson", "quest target extraction"). Auto-tags
    are never overwritten by re-tagging. The bundle cannot infer causes, only
    symptoms — this field is the bridge.
    """
    _ensure_dir()
    advice_id = new_advice_id()
    record = {
        "advice_id": advice_id,
        "run_id": run_id,
        "timestamp": datetime.now().isoformat(),
        "snapshot_day": snapshot_day,
        "trigger": trigger,
        "reflex_name": reflex_name,
        "severity": severity,
        "status": "open",
        "outcome_note": None,
        "situation": situation,
        "risks": risks or [],
        "actions": actions,
        "watch_next": watch_next or [],
        "linked_lessons": linked_lessons or [],
        "auto_paused": auto_paused,
        "llm_model": llm_model,
        "context_tokens": context_tokens,
        "event_cause": event_cause,
        "days_passed": days_passed,
    }
    with open(_advice_path(create=True), "a", encoding="utf-8") as f:
        f.write(json.dumps(record, default=str) + "\n")
    return advice_id


def _read_all():
    """Read every advice record (no filtering)."""
    path = _advice_path()
    if not path or not os.path.exists(path):
        return []
    out = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                out.append(json.loads(line))
    return out


def read_advice(run_id=None, status=None):
    """Read advice records, optionally filtered by run_id or status."""
    return [
        rec for rec in _read_all()
        if (not run_id or rec.get("run_id") == run_id)
        and (not status or rec.get("status") == status)
    ]


def save_atomic_at(path, records):
    """Atomically replace an arbitrary advice file (tmp write + os.replace)."""
    tmp_path = path + ".tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        for rec in records:
            f.write(json.dumps(rec, default=str) + "\n")
    os.replace(tmp_path, path)


def save_atomic(records):
    """Atomically replace the advice file with the given records (tmp write + os.replace)."""
    path = _advice_path(create=True)
    if not path:
        return
    save_atomic_at(path, records)


def _mutate(predicate, mutator):
    """Change matching records in place, then atomically rewrite the file if any changed.

    Returns the list of changed records.
    """
    records = _read_all()
    changed = []
    for rec in records:
        if predicate(rec):
            mutator(rec)
            changed.append(rec)
    if changed:
        save_atomic(records)
    return changed


def update_outcome(advice_id, status, outcome_note=None):
    """Update the status/outcome of an existing advice record. Returns True if found.

    Rewrites the file atomically.
    """

    def _set(rec):
        rec["status"] = status
        if outcome_note is not None:
            rec["outcome_note"] = outcome_note

    return bool(_mutate(lambda rec: rec.get("advice_id") == advice_id, _set))


def set_event_cause(advice_id, cause):
    """Record what actually caused an event. Used after a run, by the player or the agent.

    The bundle can see symptoms (Fire!, DOWNED) but not causes (raider arson, quest target
    extraction). Without this field the reviewer has to guess, and the guesses were wrong.
    Returns True if the record was found.
    """

    def _set(rec):
        rec["event_cause"] = cause
        rec["event_cause_source"] = "human"

    return bool(_mutate(lambda rec: rec.get("advice_id") == advice_id, _set))


def set_cause_matching(run_id, needle, cause):
    """Set event_cause on every record of run_id whose situation contains needle.

    Returns the number of records changed. Convenience for tagging a burst of identical
    alerts (eight "Fire!" records from one incident) without pasting ids one at a time.
    """
    needle_low = str(needle).lower()

    def _matches(rec):
        return rec.get("run_id") == run_id and needle_low in str(rec.get("situation", "")).lower()

    def _set(rec):
        rec["event_cause"] = cause
        rec["event_cause_source"] = "human"

    return len(_mutate(_matches, _set))


def _parse_ts(value):
    """Parse an ISO timestamp from a record; None if missing/unparseable."""
    try:
        return datetime.fromisoformat(str(value))
    except (TypeError, ValueError):
        return None


def _record_days_passed(rec):
    try:
        return int(rec["days_passed"])
    except (KeyError, TypeError, ValueError):
        return None


def expiry_matches(rec, *, now, wall_days, game_days, current_days_passed):
    """True when an open record is too old to ever be judged decidable.

    Aging prefers in-game days when both the current ``days_passed`` and the
    record's own ``days_passed`` are known; otherwise wall-clock aging applies.
    """
    if rec.get("status") != "open":
        return False
    if current_days_passed is not None:
        rec_days = _record_days_passed(rec)
        if rec_days is not None:
            return (current_days_passed - rec_days) > game_days
    ts = _parse_ts(rec.get("timestamp"))
    return ts is not None and ts < now - timedelta(days=wall_days)


def expiry_thresholds(max_age_days=None):
    """(wall_days, game_days) thresholds from args/env. See expire_stale."""
    wall = max_age_days if max_age_days is not None else float(os.getenv("ADVICE_EXPIRE_DAYS", "7.0"))
    game = float(os.getenv("ADVICE_EXPIRE_IN_GAME_DAYS", "3.0"))
    return wall, game


def expire_stale(max_age_days: float | None = None, now: datetime | None = None,
                 current_days_passed: int | None = None) -> int:
    """Expire undecidable open records so stale advice stops polluting debrief bundles.

    Judging happens before expiry (outcomes.close_outcomes decides helped/failed
    first); this only sweeps records that could not be resolved. Aging prefers
    in-game days: when both the current ``days_passed`` and the record's own
    ``days_passed`` are known, a record older than ADVICE_EXPIRE_IN_GAME_DAYS
    (default 3) expires. Otherwise it falls back to wall-clock aging at
    ADVICE_EXPIRE_DAYS (default 7). Records with neither are left alone.

    Passing ``max_age_days`` explicitly overrides the wall-clock threshold
    (kept for CLI/tests; predates in-game aging). Idempotent; returns how many
    records were expired.
    """
    now = now or datetime.now()
    wall, game = expiry_thresholds(max_age_days)

    def _matches(rec):
        return expiry_matches(rec, now=now, wall_days=wall, game_days=game,
                              current_days_passed=current_days_passed)

    def _expire(rec):
        rec["status"] = "expired"
        if current_days_passed is not None and _record_days_passed(rec) is not None:
            rec["outcome_note"] = f"auto-expired: no outcome recorded within {game:g} in-game day(s)"
        else:
            rec["outcome_note"] = f"auto-expired: no outcome recorded within {wall:g} day(s)"

    return len(_mutate(_matches, _expire))


def find_open_duplicate(run_id, situation):
    """Return the advice_id of an already-open record with the same situation, if any.

    Used to stop monitor restarts (or repeated polls after a restart) from writing the
    same urgent advice again and again.
    """
    for rec in read_advice(run_id=run_id, status="open"):
        if rec.get("situation") == situation:
            return rec.get("advice_id")
    return None


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: advice_log.py list [run_id] | update <advice_id> <status> [note] "
              "| cause <advice_id> <text> | cause-match <run_id> <substring> <text> "
              "| expire [days]")
        sys.exit(0)
    cmd = sys.argv[1]
    if cmd == "list":
        rid = sys.argv[2] if len(sys.argv) > 2 else None
        for r in read_advice(run_id=rid):
            print(r["advice_id"], r["trigger"], r["severity"], r["status"], "-", r["situation"][:60])
    elif cmd == "update":
        aid = sys.argv[2]
        st = sys.argv[3]
        note = " ".join(sys.argv[4:]) if len(sys.argv) > 4 else None
        print("updated:", update_outcome(aid, st, note))
    elif cmd == "cause":
        aid = sys.argv[2]
        cause = " ".join(sys.argv[3:])
        print("cause set:", set_event_cause(aid, cause))
    elif cmd == "cause-match":
        rid, needle = sys.argv[2], sys.argv[3]
        cause = " ".join(sys.argv[4:])
        print("records changed:", set_cause_matching(rid, needle, cause))
    elif cmd == "expire":
        days = float(sys.argv[2]) if len(sys.argv) > 2 else 3.0
        print("records expired:", expire_stale(days))
