"""Outcome tracking: close open advice records at each daily snapshot and update lesson confidence."""

import json
import os
from datetime import datetime

try:
    from smartrim.config import BASE_DIR
except ImportError:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LESSONS_FILE = os.path.join(BASE_DIR, "memory", "lessons.jsonl")


def _read_advice():
    """Read advice records via the single owner of the advice file (advice_log)."""
    from smartrim.advice_log import _read_all
    return _read_all()


def _write_advice(records):
    """Rewrite the advice file atomically via the single owner (advice_log)."""
    from smartrim.advice_log import save_atomic
    save_atomic(records)


def _read_lessons():
    if not os.path.exists(LESSONS_FILE):
        return []
    out = []
    with open(LESSONS_FILE, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            out.append(json.loads(line))
    return out


def _write_lessons(lessons):
    try:
        from smartrim.lesson_store import DEFAULT_SQLITE_PATH, SqliteLessonStore

        db_path = (
            os.path.splitext(LESSONS_FILE)[0] + ".sqlite"
            if os.path.join(BASE_DIR, "memory", "lessons.jsonl") != LESSONS_FILE
            else DEFAULT_SQLITE_PATH
        )
        store = SqliteLessonStore(db_path=db_path, jsonl_path=LESSONS_FILE)
        try:
            store.save_all(lessons)
        finally:
            store.close()
    except Exception:
        with open(LESSONS_FILE, "w", encoding="utf-8") as f:
            f.writelines(json.dumps(lesson, default=str) + "\n" for lesson in lessons)


def _close_advice(advice, snapshot_summary):
    """Return (new_status, outcome_note) for an open advice record."""
    # Determine if the risk cleared or worsened
    threats = set()
    alerts = snapshot_summary.get("alerts", [])
    if isinstance(alerts, list):
        for a in alerts:
            threats.add(a.get("label", "").lower() if isinstance(a, dict) else str(a).lower())

    situation = (advice.get("situation") or "").lower()
    trigger_text = situation

    # Food risk (only if this advice is about food)
    if "food" in trigger_text or "meal" in trigger_text:
        food_days = snapshot_summary.get("food_days")
        if food_days is not None:
            if food_days >= 5:
                return "helped", f"food days now {food_days} (>=5)"
            if food_days < 2:
                return "failed", f"food days fell to {food_days} (<2)"
            return None, None  # still at risk

    # Medical risk (only if this advice is about medicine/health)
    if "medicine" in trigger_text or "health" in trigger_text or "injur" in trigger_text:
        med = snapshot_summary.get("medicine_count")
        if med is not None:
            min_health = snapshot_summary.get("min_health")
            injured = min_health is not None and min_health < 90
            if med == 0 and injured:
                return "failed", "medicine 0 and colonist injured"
            if med >= 5 and not injured:
                return "helped", f"medicine stock {med}, no injured colonists"
        return None, None

    # Mood risk (only if this advice is about mood)
    if "mood" in trigger_text:
        min_mood = snapshot_summary.get("min_mood")
        if min_mood is not None:
            if min_mood < 20:
                return "failed", f"min mood fell to {min_mood} (<20)"
            if min_mood >= 35:
                return "helped", f"min mood now {min_mood} (>=35)"
            return None, None  # still at risk

    # If no risk signal matches, the advice may be expired
    still_relevant = False
    for t in threats:
        if t and t in trigger_text:
            still_relevant = True
            break
    if not still_relevant:
        food_days = snapshot_summary.get("food_days")
        min_mood = snapshot_summary.get("min_mood")
        if (food_days is None or food_days >= 5) and (min_mood is None or min_mood >= 35):
            return "expired", "risk cleared, trigger no longer applies"

    return None, None  # stays open


def _days_passed(snapshot_summary) -> int | None:
    """Current in-game day from a snapshot summary, or None when unknown."""
    try:
        return int(snapshot_summary.get("days_passed"))
    except (TypeError, ValueError, AttributeError):
        return None


def close_outcomes(snapshot_summary, run_id=None):
    """Close open advice records and update lesson confidence. Idempotent.

    Order matters: records are judged (helped/failed/expired) *first* at each
    day roll, and only then are still-undecidable records aged out. Expiry
    prefers in-game days when the record and the snapshot both carry
    ``days_passed``. Only helped/failed verdicts touch lesson counters —
    expiry and other inconclusive closures update the advice record alone,
    so ``times_applied`` counts judged advice, not retrieval frequency.
    """
    days_passed = _days_passed(snapshot_summary)

    records = _read_advice()
    lessons = _read_lessons()
    lesson_map = {lesson["id"]: lesson for lesson in lessons}

    changed = False
    lessons_changed = False
    for rec in records:
        if rec.get("status") not in ("open", "applied"):
            continue
        if run_id and rec.get("run_id") != run_id:
            continue
        new_status, note = _close_advice(rec, snapshot_summary)
        if new_status is None:
            continue
        rec["status"] = new_status
        if note:
            rec["outcome_note"] = note
        changed = True

        # A verdict is required to learn anything. Inconclusive closures
        # (e.g. "expired" = risk cleared before a decision could be made)
        # are recorded on the advice record and never touch lessons.
        if new_status not in ("helped", "failed"):
            continue

        # A lesson is applied as soon as a verdict is recorded. Record that
        # touch so lineage is complete.
        effective_run_id = run_id or rec.get("run_id")
        for lid in rec.get("linked_lessons") or []:
            lesson = lesson_map.get(lid)
            if not lesson:
                continue
            source_runs = lesson.get("source_runs") or []
            if effective_run_id and effective_run_id not in source_runs:
                source_runs.append(effective_run_id)
                lesson["source_runs"] = source_runs
                lessons_changed = True

        # Update linked lessons
        for lid in rec.get("linked_lessons") or []:
            lesson = lesson_map.get(lid)
            if not lesson:
                continue
            if new_status == "helped":
                lesson["times_helped"] = lesson.get("times_helped", 0) + 1
                lesson["confidence"] = round(min(1.0, lesson.get("confidence", 0.3) + 0.1), 2)
            elif new_status == "failed":
                lesson["times_failed"] = lesson.get("times_failed", 0) + 1
                lesson["confidence"] = round(max(0.0, lesson.get("confidence", 0.3) - 0.15), 2)
                if lesson.get("times_failed", 0) >= 3 and lesson.get(
                    "times_failed", 0
                ) > lesson.get("times_helped", 0):
                    lesson["status"] = "needs_review"
            lesson["times_applied"] = lesson.get("times_applied", 0) + 1
            lesson["last_updated"] = datetime.now().strftime("%Y-%m-%d")
            lessons_changed = True

    # Judge everything decidable first; only then age out the undecidable —
    # inline, on the same in-memory records, so the single atomic write below
    # carries both the verdicts and the expiries.
    from smartrim.advice_log import expiry_matches, expiry_thresholds

    now = datetime.now()
    wall, game = expiry_thresholds()
    for rec in records:
        if not expiry_matches(rec, now=now, wall_days=wall, game_days=game,
                              current_days_passed=days_passed):
            continue
        rec["status"] = "expired"
        if days_passed is not None and rec.get("days_passed") is not None:
            rec["outcome_note"] = f"auto-expired: no outcome recorded within {game:g} in-game day(s)"
        else:
            rec["outcome_note"] = f"auto-expired: no outcome recorded within {wall:g} day(s)"
        changed = True

    if changed:
        _write_advice(records)
    if lessons_changed:
        _write_lessons(list(lesson_map.values()))

    return changed


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: outcomes.py <snapshot.json> [run_id]")
        sys.exit(0)
    snap = json.load(open(sys.argv[1]))
    summary = snap.get("summary", snap)
    rid = sys.argv[2] if len(sys.argv) > 2 else None
    changed = close_outcomes(summary, run_id=rid)
    print("changed:", changed)
