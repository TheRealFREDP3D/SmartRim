"""Outcome tracking: close open advice records at each daily snapshot and update lesson confidence."""

import json
import os
from datetime import datetime

try:
    from smartrim.config import BASE_DIR
except ImportError:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ADVICE_FILE = os.path.join(BASE_DIR, "memory", "advice", "advice.jsonl")
LESSONS_FILE = os.path.join(BASE_DIR, "memory", "lessons.jsonl")


def _read_advice():
    if not os.path.exists(ADVICE_FILE):
        return []
    out = []
    with open(ADVICE_FILE, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            out.append(json.loads(line))
    return out


def _write_advice(records):
    os.makedirs(os.path.dirname(ADVICE_FILE), exist_ok=True)
    with open(ADVICE_FILE, "w", encoding="utf-8") as f:
        f.writelines(json.dumps(rec, default=str) + "\n" for rec in records)


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


def close_outcomes(snapshot_summary, run_id=None):
    """Close open advice records and update lesson confidence. Idempotent."""
    records = _read_advice()
    lessons = _read_lessons()
    lesson_map = {lesson["id"]: lesson for lesson in lessons}

    changed = False
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

        # A lesson is applied as soon as linked advice is issued, even if its
        # outcome remains open. Record that touch now so lineage is complete.
        effective_run_id = run_id or rec.get("run_id")
        for lid in rec.get("linked_lessons") or []:
            lesson = lesson_map.get(lid)
            if not lesson:
                continue
            source_runs = lesson.get("source_runs") or []
            if effective_run_id and effective_run_id not in source_runs:
                source_runs.append(effective_run_id)
                lesson["source_runs"] = source_runs
                changed = True

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

    if changed:
        _write_advice(records)
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
