"""Situation classifier and lesson retrieval for Phase 2.

Pure functions. No LLM. No MCP. Testable with fixtures.
"""

import json
import os
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LESSONS_FILE = os.path.join(BASE_DIR, "memory", "lessons.jsonl")

# Threat vocabulary (monitor alert category -> threat tag). Single source of truth.
ALERT_TO_THREAT = {
    "downed": "colonist_downed",
    "mood_extreme": "mood_break_risk",
    "mood_major": "mood_break_risk",
    "mood_minor": "mood_break_risk",
    "health": "colonist_injured",
    "danger_rating": "danger_high",
    "hostile": "raid_incoming",
    "predator_near": "predator_near_worker",
    "food_low": "low_food",
    "medicine_low": "medical_untreated",
    "medical_treatment_needed": "medical_untreated",
    "idle_colonist": "idle_colonists",
    "sleeping_during_threat": "threat_response",
    "colony_death": "colony_death",
    "game_alert": "other_game_alert",
}

GAME_ALERT_KEYWORDS = {
    "raid": "raid_incoming",
    "enemy": "raid_incoming",
    "attack": "raid_incoming",
    "predator": "predator_near_worker",
    "fire": "threat_response",
}


def classify_phase(snapshot_summary, alerts):
    """Return one of: early_survival, stabilization, raid_prep, expansion, crisis."""
    day = snapshot_summary.get("day") or snapshot_summary.get("colonist_count") or 0
    # day may be a date string; try to extract a number
    if isinstance(day, str):
        m = re.search(r"(\d+)", day)
        day = int(m.group(1)) if m else 0
    try:
        day = int(day)
    except (ValueError, TypeError):
        day = 0

    # Crisis overrides everything
    is_crisis = False
    for a in alerts:
        cat = a.get("category", "")
        tag = ALERT_TO_THREAT.get(cat, "")
        if tag in ("colonist_downed", "danger_high", "raid_incoming", "predator_near_worker", "colony_death", "threat_response"):
            is_crisis = True
        if cat == "game_alert":
            label = a.get("label", "").lower() if "label" in a else a.get("message", "").lower()
            if any(k in label for k in ("raid", "attack", "enemy", "predator", "fire")):
                is_crisis = True
    if is_crisis:
        return "crisis"

    # Raid prep: raid-related alert or letter
    for a in alerts:
        cat = a.get("category", "")
        label = (a.get("label", "") or a.get("message", "")).lower()
        if cat == "hostile" or cat == "predator_near":
            return "raid_prep"
        if cat == "game_alert" and any(k in label for k in ("raid", "enemy", "attack")):
            return "raid_prep"

    if day <= 7:
        return "early_survival"
    if day <= 20:
        return "stabilization"
    return "expansion"


def build_threats(alerts):
    """Convert alert list to a set of threat tags."""
    threats = set()
    for a in alerts:
        cat = a.get("category", "")
        tag = ALERT_TO_THREAT.get(cat)
        if tag:
            threats.add(tag)
        if cat == "game_alert":
            label = (a.get("label", "") or a.get("message", "")).lower()
            for kw, t in GAME_ALERT_KEYWORDS.items():
                if kw in label:
                    threats.add(t)
    return threats


def build_resources(snapshot_summary):
    """Convert a snapshot summary into resource tags."""
    resources = set()
    food_days = snapshot_summary.get("food_days")
    if food_days is not None:
        if food_days < 2:
            resources.add("food_under_2_days")
        elif food_days < 5:
            resources.add("food_under_5_days")
    med = snapshot_summary.get("medicine_count")
    if med is not None:
        if med == 0:
            resources.add("no_medicine")
        elif med < 5:
            resources.add("medicine_under_5")
    res_map = snapshot_summary.get("resources") or {}
    if isinstance(res_map, dict):
        wood = res_map.get("WoodLog") or res_map.get("wood") or 0
        steel = res_map.get("Steel") or res_map.get("steel") or 0
        if wood < 50:
            resources.add("low_wood")
        if steel < 50:
            resources.add("low_steel")
    return resources


def build_situation(snapshot_summary, alerts):
    """Build a Situation dict from a snapshot summary and alert list."""
    threats = build_threats(alerts)
    resources = build_resources(snapshot_summary)
    phase = classify_phase(snapshot_summary, alerts)
    return {
        "phase": phase,
        "difficulty": snapshot_summary.get("difficulty") or "any",
        "storyteller": snapshot_summary.get("storyteller") or "any",
        "biome": snapshot_summary.get("biome") or "any",
        "food_days": snapshot_summary.get("food_days"),
        "medicine_count": snapshot_summary.get("medicine_count"),
        "colonist_count": snapshot_summary.get("colonist_count"),
        "threats": sorted(threats),
        "resources": sorted(resources),
    }


def load_lessons(path=None):
    path = path or LESSONS_FILE
    lessons = []
    if not os.path.exists(path):
        return lessons
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            lessons.append(json.loads(line))
    return lessons


def retrieve(situation, lessons=None, limit=5):
    """Return up to `limit` lessons matching the situation. Deterministic."""
    if lessons is None:
        lessons = load_lessons()

    phase = situation.get("phase")
    threats = set(situation.get("threats") or [])
    resources = set(situation.get("resources") or [])
    difficulty = situation.get("difficulty")
    storyteller = situation.get("storyteller")
    biome = situation.get("biome")

    candidates = []
    for lesson in lessons:
        if lesson.get("status") != "active":
            continue
        trigger = lesson.get("trigger") or {}
        phases = trigger.get("phases") or []
        l_threats = set(trigger.get("threats") or [])
        l_resources = set(trigger.get("resources") or [])
        l_diff = trigger.get("difficulty") or []
        l_st = trigger.get("storyteller") or []
        l_biome = trigger.get("biome") or []

        # phase overlap
        if phases and phase not in phases:
            continue
        # threat or resource must match
        threat_match = bool(threats & l_threats)
        resource_match = bool(resources & l_resources)
        if l_threats or l_resources:
            if not (threat_match or resource_match):
                continue
        else:
            # no trigger threats/resources -> eligible only if phase matched
            pass
        # scope match (strict)
        if l_diff and difficulty not in l_diff:
            continue
        if l_st and storyteller not in l_st:
            continue
        if l_biome and biome not in l_biome:
            continue

        # ranking key
        conf = lesson.get("confidence", 0.0)
        helped = lesson.get("times_helped", 0)
        failed = lesson.get("times_failed", 0)
        last_updated = lesson.get("last_updated") or ""
        key = (-conf, -(helped - failed), last_updated, lesson.get("id", ""))
        candidates.append((key, lesson))

    candidates.sort(key=lambda x: x[0])
    return [c[1] for c in candidates[:limit]]


def validate_lesson(lesson):
    """Return list of validation errors (empty = valid)."""
    errors = []
    lid = lesson.get("id", "")
    if not re.match(r"^L-\d{4}$", lid):
        errors.append(f"bad id: {lid}")
    if not lesson.get("title"):
        errors.append("missing title")
    trigger = lesson.get("trigger") or {}
    if not isinstance(trigger, dict):
        errors.append("trigger must be object")
    else:
        for f in ("phases", "threats", "resources"):
            if f not in trigger:
                errors.append(f"trigger missing {f}")
    conf = lesson.get("confidence")
    if conf is None or not (0 <= conf <= 1):
        errors.append(f"bad confidence: {conf}")
    if not lesson.get("source") and (conf is None or conf > 0.3):
        errors.append("lesson with no source must have confidence <= 0.3")
    status = lesson.get("status")
    if status not in ("active", "needs_review", "retired"):
        errors.append(f"bad status: {status}")
    for f in ("times_applied", "times_helped", "times_failed"):
        v = lesson.get(f, 0)
        if not isinstance(v, int) or v < 0:
            errors.append(f"bad {f}: {v}")
    return errors


def validate_all(path=None):
    path = path or LESSONS_FILE
    if not os.path.exists(path):
        return []
    errors = []
    with open(path, encoding="utf-8") as f:
        for i, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                lesson = json.loads(line)
            except json.JSONDecodeError as e:
                errors.append(f"line {i}: json error: {e}")
                continue
            for e in validate_lesson(lesson):
                errors.append(f"line {i} ({lesson.get('id', '?')}): {e}")
    return errors


def render_markdown(path=None):
    """Render lessons.jsonl as human-readable markdown."""
    lessons = load_lessons(path)
    lines = ["# Lessons Learned (generated from lessons.jsonl)", "",
             "Do not edit this file by hand. Edit memory/lessons.jsonl, then run:",
             "  python sidecar/lessons.py render > memory/lessons-learned.md", ""]
    # Group by status
    for status in ("active", "needs_review", "retired"):
        group = [l for l in lessons if l.get("status") == status]
        if not group:
            continue
        lines.append(f"## {status.title()} lessons")
        lines.append("")
        for l in group:
            lines.append(f"### {l.get('id')} {l.get('title')}")
            lines.append(f"- Confidence: {l.get('confidence')} | applied {l.get('times_applied',0)} | helped {l.get('times_helped',0)} | failed {l.get('times_failed',0)}")
            lines.append(f"- Trigger: phases={l.get('trigger',{}).get('phases')} threats={l.get('trigger',{}).get('threats')} resources={l.get('trigger',{}).get('resources')}")
            scope = []
            if l.get('trigger',{}).get('difficulty'):
                scope.append("difficulty=" + ",".join(l['trigger']['difficulty']))
            if l.get('trigger',{}).get('storyteller'):
                scope.append("storyteller=" + ",".join(l['trigger']['storyteller']))
            if l.get('trigger',{}).get('biome'):
                scope.append("biome=" + ",".join(l['trigger']['biome']))
            if scope:
                lines.append("- Scope: " + "; ".join(scope))
            lines.append(f"- Recommendation: {l.get('recommendation')}")
            lines.append(f"- Rationale: {l.get('rationale')}")
            lines.append(f"- Source: {', '.join(l.get('source', []))}")
            lines.append(f"- Tags: {', '.join(l.get('tags', []))}")
            lines.append("")
    return "\n".join(lines)


if __name__ == "__main__":
    import sys
    cmd = sys.argv[1] if len(sys.argv) > 1 else "help"
    if cmd == "validate":
        errs = validate_all()
        if errs:
            for e in errs:
                print(e)
            sys.exit(1)
        print("all lessons valid")
    elif cmd == "render":
        print(render_markdown())
    elif cmd == "retrieve":
        # usage: retrieve <json situation file>
        path = sys.argv[2] if len(sys.argv) > 2 else None
        if path:
            sit = json.load(open(path))
        else:
            sit = json.load(sys.stdin)
        for l in retrieve(sit):
            print(l.get("id"), l.get("title"), f"(conf {l.get('confidence')})")
    elif cmd == "build-situation":
        # read snapshot summary + alerts from stdin or files
        snap = json.load(open(sys.argv[2])) if len(sys.argv) > 2 else {}
        alerts = json.load(open(sys.argv[3])) if len(sys.argv) > 3 else []
        sit = build_situation(snap.get("summary", snap), alerts)
        print(json.dumps(sit, indent=2))
    else:
        print("usage: lessons.py validate | render | retrieve <sit.json> | build-situation <snap.json> <alerts.json>")
