"""Situation classifier and lesson retrieval for Phase 2.

Pure functions. No LLM. No MCP. Testable with fixtures.
"""

import json
import os
import re


def _ci_contains(allowed, value) -> bool:
    """Case-insensitive membership test for scoped trigger fields.

    The situation carries values as the game reports them ("adventure story")
    while lessons store the canonical label ("Adventure story"), so an exact
    comparison silently rejects every difficulty/storyteller-scoped lesson.
    """
    if value is None:
        return False
    target = str(value).strip().lower()
    if not target or target == "any":
        return True
    return any(str(a).strip().lower() == target for a in allowed)

try:
    from smartrim.config import BASE_DIR
except ImportError:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LESSONS_FILE = os.path.join(BASE_DIR, "memory", "lessons.jsonl")

# Allowed enum values for lesson trigger fields (must stay in sync with schemas/lesson.schema.json).
_PHASES_ENUM = {"early_survival", "stabilization", "raid_prep", "expansion", "crisis", "any"}
_THREATS_ENUM = {"colonist_downed", "mood_break_risk", "colonist_injured", "danger_high",
                 "raid_incoming", "predator_near_worker", "low_food", "medical_untreated",
                 "idle_colonists", "threat_response", "colony_death", "other_game_alert", "any"}
_RESOURCES_ENUM = {"food_under_5_days", "food_under_2_days", "no_medicine", "medicine_under_5",
                   "low_wood", "low_steel", "any"}
_DIFFICULTY_ENUM = {"Peaceful", "Community builder", "Adventure story", "Strive to survive",
                    "Blood and dust", "Losing is fun", "any"}
_STORYTELLER_ENUM = {"Cassandra Classic", "Phoebe Chillax", "Randy Random", "any"}

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
    # Food and medicine alerts reach here when they arrive as generic game alerts
    # instead of the monitor's own food_low / medicine_low categories. Without
    # these they fall through to other_game_alert and never match the food
    # lessons (this is what let run-007 starve while the food lesson was active).
    "starv": "low_food",
    "food stock": "low_food",
    "low food": "low_food",
    "medicine stock": "medical_untreated",
    "medical treatment": "medical_untreated",
    "no medicine": "medical_untreated",
    "break risk": "mood_break_risk",
    "recreation": "mood_break_risk",
    "colonist beds": "mood_break_risk",
}


def classify_phase(snapshot_summary, alerts):
    day = snapshot_summary.get("days_passed")
    if day is None:
        day = snapshot_summary.get("day")
    if day is None:
        day = 0
    if isinstance(day, str):
        m = re.search(r"(\d+)", day)
        day = int(m.group(1)) if m else 0
    try:
        day = int(day)
    except (ValueError, TypeError):
        day = 0

    is_crisis = False
    for a in alerts:
        cat = a.get("category", "")
        tag = ALERT_TO_THREAT.get(cat, "")
        if tag in ("colonist_downed", "danger_high", "raid_incoming", "predator_near_worker", "colony_death", "threat_response"):
            is_crisis = True
        if cat == "game_alert":
            label = a.get("label", "").lower() if "label" in a else a.get("message", "").lower()
            if any(k in label for k in ("attack", "enemy", "predator", "fire")):
                is_crisis = True
    if is_crisis:
        return "crisis"

    for a in alerts:
        cat = a.get("category", "")
        label = (a.get("label", "") or a.get("message", "")).lower()
        if cat in ("hostile", "predator_near"):
            return "raid_prep"
        if cat == "game_alert" and "raid" in label:
            return "raid_prep"
        if cat == "game_alert" and "defenses" in label:
            return "raid_prep"

    if day <= 7:
        return "early_survival"
    if day <= 20:
        return "stabilization"
    return "expansion"


def build_threats(alerts):
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


SEVERITY_ORDER = {"critical": 0, "urgent": 1, "warning": 2, "info": 3}


def rank_actions(alerts, situation, lessons_list, limit=5, store=None, use_semantic_search=True):
    """Rank actions from alerts + retrieved lessons. Deterministic.

    Returns list of action dicts: {rank, action, rationale, estimated_time, auto_paused}.
    Also returns the list of linked lesson ids.

    Args:
        alerts: List of alert dicts
        situation: Situation dict from build_situation()
        lessons_list: Optional list of lesson dicts (for backward compatibility)
        limit: Maximum number of actions to return
        store: Optional LessonStore instance (uses SqliteLessonStore by default if None)
        use_semantic_search: If True, use SQLite+FTS5 store; if False, use legacy JSONL scan
    """
    # Map alert severity to risk severity
    risks = []
    for a in alerts:
        sev = a.get("type", "warning")
        risk_sev = "critical" if sev == "urgent" else sev
        risks.append((risk_sev, a))

    # For each risk, retrieve matching lessons and produce candidate actions
    candidates = []
    linked = set()
    for risk_sev, alert in risks:
        # Build a mini-situation for this risk's threat
        cat = alert.get("category", "")
        threat_tag = ALERT_TO_THREAT.get(cat, "other_game_alert")
        mini_sit = dict(situation)
        mini_sit["threats"] = [threat_tag]
        # Retrieve lessons for this specific threat
        matched = retrieve(mini_sit, lessons_list, limit=3, store=store, use_semantic_search=use_semantic_search)
        for lesson in matched:
            linked.add(lesson.get("id"))
            action_text = lesson.get("recommendation", "")
            rationale = lesson.get("rationale", "")
            tags = lesson.get("tags", [])
            est_time = None
            if "early_game" in tags:
                est_time = "immediate"
            elif "early" in str(tags):
                est_time = "soon"
            candidates.append({
                "risk_severity": risk_sev,
                "confidence": lesson.get("confidence", 0.0),
                "action": action_text,
                "rationale": rationale,
                "estimated_time": est_time,
                "lesson_id": lesson.get("id"),
            })

    # If no lessons matched, produce a generic action from the alert itself
    if not candidates:
        for risk_sev, alert in risks:
            candidates.append({
                "risk_severity": risk_sev,
                "confidence": 0.3,
                "action": f"Address: {alert.get('message', '')}",
                "rationale": "Reflex alert fired",
                "estimated_time": "immediate",
                "lesson_id": None,
            })

    # Sort: risk severity first, then confidence desc
    candidates.sort(key=lambda c: (SEVERITY_ORDER.get(c["risk_severity"], 9), -c["confidence"]))

    # Deduplicate by action text
    seen = set()
    unique = []
    for c in candidates:
        if c["action"] in seen:
            continue
        seen.add(c["action"])
        unique.append(c)

    # Cap at limit
    unique = unique[:limit]

    # Assign ranks
    actions = []
    for i, c in enumerate(unique, 1):
        actions.append({
            "rank": i,
            "action": c["action"],
            "rationale": c["rationale"],
            "estimated_time": c["estimated_time"],
            "auto_paused": False,
        })

    return actions, sorted(linked)


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


def _normalize_list(val):
    if val is None:
        return []
    if isinstance(val, str):
        v = val.strip().lower()
        if v == "any" or v == "":
            return []
        return [val]
    if isinstance(val, (list, set, tuple)):
        out = []
        for item in val:
            if item is None:
                continue
            if isinstance(item, str) and item.strip().lower() == "any":
                continue
            out.append(item)
        return out
    return [val]


def retrieve(situation, lessons=None, limit=5, store=None, use_semantic_search=True):
    """Retrieve lessons matching the situation.

    Args:
        situation: Dict with phase, threats, resources, difficulty, storyteller, biome
        lessons: Optional list of lesson dicts (for backward compatibility)
        limit: Maximum number of lessons to return
        store: Optional LessonStore instance (uses SqliteLessonStore by default if None)
        use_semantic_search: If True, use SQLite+FTS5 store; if False, use legacy JSONL scan

    Returns:
        List of lesson dicts (not Lesson objects, for backward compatibility)
    """
    # If lessons list is explicitly provided, use legacy path (backward compatibility)
    if lessons is not None:
        use_semantic_search = False

    # Use SqliteLessonStore by default for semantic search
    if store is None and use_semantic_search:
        try:
            from smartrim.lesson_store import get_store
            store = get_store(use_sqlite=True)
        except ImportError:
            use_semantic_search = False

    if store:
        # Build query text from situation for semantic search
        query_parts = []
        if situation.get("phase"):
            query_parts.append(situation["phase"])
        for threat in situation.get("threats", []):
            query_parts.append(threat)
        for resource in situation.get("resources", []):
            query_parts.append(resource)
        query_text = " ".join(query_parts) if query_parts else None

        lessons_objs = store.retrieve(situation, limit=limit, query_text=query_text)
        return [lesson.to_dict() for lesson in lessons_objs]

    # Legacy path: scan lessons list
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
        phases = _normalize_list(trigger.get("phases"))
        l_threats = set(_normalize_list(trigger.get("threats")))
        l_resources = set(_normalize_list(trigger.get("resources")))
        l_diff = _normalize_list(trigger.get("difficulty"))
        l_st = _normalize_list(trigger.get("storyteller"))
        l_biome = _normalize_list(trigger.get("biome"))

        if phases and phase not in phases:
            continue
        # A lesson with no scoping criteria at all is too broad to ever retrieve.
        if not phases and not l_threats and not l_resources and not l_diff and not l_st and not l_biome:
            continue
        # If the lesson declares threats or resources, at least one must match.
        # Lessons that declare neither (general-practice lessons) match on phase/other scope.
        if l_threats or l_resources:
            threat_match = bool(threats & l_threats)
            resource_match = bool(resources & l_resources)
            if not (threat_match or resource_match):
                continue
        if l_diff and not _ci_contains(l_diff, difficulty):
            continue
        if l_st and not _ci_contains(l_st, storyteller):
            continue
        if l_biome and not _ci_contains(l_biome, biome):
            continue

        conf = lesson.get("confidence", 0.0)
        helped = lesson.get("times_helped", 0)
        failed = lesson.get("times_failed", 0)
        last_updated = lesson.get("last_updated") or ""
        key = (-conf, -(helped - failed), last_updated, lesson.get("id", ""))
        candidates.append((key, lesson))

    candidates.sort(key=lambda x: x[0])
    return [c[1] for c in candidates[:limit]]


def validate_lesson(lesson):
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
        # Validate enum membership for scoped trigger fields.
        enum_map = {
            "phases": _PHASES_ENUM,
            "threats": _THREATS_ENUM,
            "resources": _RESOURCES_ENUM,
            "difficulty": _DIFFICULTY_ENUM,
            "storyteller": _STORYTELLER_ENUM,
        }
        for field, allowed in enum_map.items():
            raw = trigger.get(field)
            if raw is None:
                raw = []
            if isinstance(raw, str):
                raw = [raw]
            if not isinstance(raw, (list, tuple, set)):
                errors.append(f"trigger.{field} must be a list")
                continue
            for v in raw:
                if v is None:
                    continue
                s = str(v).strip()
                if s == "" or s.lower() == "any":
                    continue
                if s not in allowed:
                    errors.append(f"trigger.{field} bad value: {v}")
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


def load_run_lineage(run_id, lessons=None, advice_records=None):
    """Return lessons touched by ``run_id`` and their run-specific outcomes.

    A run touches a lesson when the lesson's ``source_runs`` contains the run
    id, or when advice issued by that run links to the lesson. Relationship is
    derived from the run's own outcome records rather than lifetime counters.
    """
    if lessons is None:
        lessons = load_lessons()
    if advice_records is None:
        try:
            from smartrim.advice_log import read_advice
            advice_records = read_advice(run_id=run_id)
        except (ImportError, OSError, json.JSONDecodeError):
            advice_records = []

    records_by_lesson = {}
    for rec in advice_records:
        for lesson_id in rec.get("linked_lessons") or []:
            records_by_lesson.setdefault(lesson_id, []).append(rec)

    lineage = []
    for lesson in lessons:
        lesson_id = lesson.get("id")
        source_runs = lesson.get("source_runs") or []
        records = records_by_lesson.get(lesson_id, [])
        if run_id not in source_runs and not records:
            continue

        outcomes = []
        for rec in records:
            status = rec.get("status")
            if status not in ("helped", "failed"):
                continue
            outcomes.append({
                "advice_id": rec.get("advice_id"),
                "status": status,
                "note": rec.get("outcome_note") or "",
            })

        if any(outcome["status"] == "failed" for outcome in outcomes):
            relationship = "CONTRADICTED"
        elif any(outcome["status"] == "helped" for outcome in outcomes):
            relationship = "HELPED"
        elif records:
            relationship = "APPLIED"
        else:
            relationship = "SOURCE"

        lineage.append({
            "lesson": lesson,
            "outcomes": outcomes,
            "relationship": relationship,
        })
    return lineage


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
    lessons = load_lessons(path)
    lines = ["# Lessons Learned (generated from lessons.jsonl)", "",
             "Do not edit this file by hand. Edit memory/lessons.jsonl, then run:",
             "  python sidecar/lessons.py render > memory/lessons-learned.md", ""]
    for status in ("active", "needs_review", "retired"):
        group = [lesson for lesson in lessons if lesson.get("status") == status]
        if not group:
            continue
        lines.append(f"## {status.title()} lessons")
        lines.append("")
        for lesson in group:
            lines.append(f"### {lesson.get('id')} {lesson.get('title')}")
            lines.append(f"- Confidence: {lesson.get('confidence')} | applied {lesson.get('times_applied',0)} | helped {lesson.get('times_helped',0)} | failed {lesson.get('times_failed',0)}")
            lines.append(f"- Trigger: phases={lesson.get('trigger',{}).get('phases')} threats={lesson.get('trigger',{}).get('threats')} resources={lesson.get('trigger',{}).get('resources')}")
            scope = []
            if lesson.get('trigger',{}).get('difficulty'):
                scope.append("difficulty=" + ",".join(lesson['trigger']['difficulty']))
            if lesson.get('trigger',{}).get('storyteller'):
                scope.append("storyteller=" + ",".join(lesson['trigger']['storyteller']))
            if lesson.get('trigger',{}).get('biome'):
                scope.append("biome=" + ",".join(lesson['trigger']['biome']))
            if scope:
                lines.append("- Scope: " + "; ".join(scope))
            lines.append(f"- Recommendation: {lesson.get('recommendation')}")
            lines.append(f"- Rationale: {lesson.get('rationale')}")
            lines.append(f"- Source: {', '.join(lesson.get('source', []))}")
            lines.append(f"- Tags: {', '.join(lesson.get('tags', []))}")
            lines.append("")
    return "\n".join(lines)


def main(argv=None):
    import sys
    argv = argv if argv is not None else sys.argv
    cmd = argv[1] if len(argv) > 1 else "help"
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
        path = argv[2] if len(argv) > 2 else None
        if path:
            with open(path, encoding="utf-8") as fh:
                sit = json.load(fh)
        else:
            sit = json.load(sys.stdin)
        for lesson in retrieve(sit):
            print(lesson.get("id"), lesson.get("title"), f"(conf {lesson.get('confidence')})")
    elif cmd == "build-situation":
        snap = {}
        if len(argv) > 2:
            with open(argv[2], encoding="utf-8") as fh:
                snap = json.load(fh)
        alerts = []
        if len(argv) > 3:
            with open(argv[3], encoding="utf-8") as fh:
                alerts = json.load(fh)
        sit = build_situation(snap.get("summary", snap), alerts)
        print(json.dumps(sit, indent=2))
    elif cmd == "reindex":
        from smartrim.lesson_store import SqliteLessonStore
        store = SqliteLessonStore()
        store.reindex()
        store.close()
    elif cmd == "verify-facts":
        import yaml

        from smartrim.debrief_bundle import BASE_DIR, WIKI_FACTS_PATH

        # Load wiki facts
        if not os.path.exists(WIKI_FACTS_PATH):
            print(f"Error: Wiki facts file not found: {WIKI_FACTS_PATH}")
            sys.exit(1)

        with open(WIKI_FACTS_PATH, encoding="utf-8") as f:
            facts_data = yaml.safe_load(f) or []

        wiki_dir = os.path.join(BASE_DIR, "memory", "wiki")
        if not os.path.exists(wiki_dir):
            print(f"Error: Wiki directory not found: {wiki_dir}")
            sys.exit(1)

        errors = []
        for entry in facts_data:
            if not isinstance(entry, dict):
                continue
            text = entry.get("text", "")
            source_pages = entry.get("source_page")
            status = entry.get("status", "unverified")

            if status != "verified":
                continue  # Skip unverified entries

            if not source_pages:
                errors.append(f"Missing source_page for: {text[:50]}...")
                continue

            # Check each source page
            pages = [source_pages] if isinstance(source_pages, str) else source_pages
            for page in pages:
                page_path = os.path.join(wiki_dir, f"{page}.md")
                if not os.path.exists(page_path):
                    errors.append(f"Source page not found: {page}.md for: {text[:50]}...")
                    continue

                # Read page and check if text is present (simple substring check)
                try:
                    with open(page_path, encoding="utf-8") as f:
                        page_content = f.read()
                    # Extract key terms from the fact to search for
                    # This is a heuristic - not perfect but good for CI
                    key_terms = text.split()[:5]  # First 5 words
                    found = any(term.lower() in page_content.lower() for term in key_terms)
                    if not found:
                        errors.append(f"Key terms not found in {page}.md for: {text[:50]}...")
                except OSError as e:
                    errors.append(f"Failed to read {page}.md: {e}")

        if errors:
            print("Wiki facts verification failed:")
            for err in errors:
                print(f"  - {err}")
            sys.exit(1)
        else:
            print(f"All {len(facts_data)} wiki facts verified successfully.")
    elif cmd == "promote":

        if len(argv) < 3:
            print("usage: lessons.py promote <candidate-file>")
            print("  candidate-file: path to JSONL file in memory/candidates/")
            sys.exit(1)

        candidate_path = argv[2]
        if not os.path.exists(candidate_path):
            print(f"Error: Candidate file not found: {candidate_path}")
            sys.exit(1)

        # Load candidates
        candidates = []
        with open(candidate_path, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                try:
                    candidates.append(json.loads(line))
                except json.JSONDecodeError as e:
                    print(f"Error parsing line: {e}")
                    sys.exit(1)

        if not candidates:
            print("No candidates found in file.")
            sys.exit(1)

        print(f"Found {len(candidates)} candidate lesson(s):")
        for i, c in enumerate(candidates):
            print(f"  {i}. {c.get('id')}: {c.get('title')} (status: {c.get('status')})")

        # Prompt for which to promote
        print("\nEnter lesson numbers to promote (comma-separated, or 'all'):")
        choice = input("> ").strip()

        if choice.lower() == "all":
            indices = list(range(len(candidates)))
        else:
            try:
                indices = [int(x.strip()) for x in choice.split(",")]
            except ValueError:
                print("Invalid input. Use comma-separated numbers or 'all'.")
                sys.exit(1)

        # Load existing lessons
        existing_lessons = load_lessons()

        # Generate new IDs for promoted lessons
        next_num = max([int(lesson.get("id", "L-0000")[2:]) for lesson in existing_lessons] + [0]) + 1

        promoted = []
        for idx in indices:
            if idx < 0 or idx >= len(candidates):
                print(f"Skipping invalid index: {idx}")
                continue

            candidate = candidates[idx]

            # Prompt for editing
            print(f"\n--- Editing lesson {idx}: {candidate.get('title')} ---")
            print("Current status:", candidate.get("status"))
            print("Current confidence:", candidate.get("confidence"))
            print("Leave blank to keep current value.")

            new_status = input(f"Status [{candidate.get('status')}]: ").strip()
            if new_status:
                candidate["status"] = new_status

            new_conf = input(f"Confidence [{candidate.get('confidence')}]: ").strip()
            if new_conf:
                try:
                    candidate["confidence"] = float(new_conf)
                except ValueError:
                    print("Invalid confidence, keeping current value.")

            # Assign new L-XXXX ID
            new_id = f"L-{next_num:04d}"
            candidate["id"] = new_id
            next_num += 1

            # Validate
            errors = validate_lesson(candidate)
            if errors:
                print(f"Validation errors: {errors}")
                confirm = input("Promote anyway? (y/n): ").strip().lower()
                if confirm != "y":
                    print("Skipping this lesson.")
                    continue

            promoted.append(candidate)
            print(f"Promoted as {new_id}")

        # Append to lessons.jsonl
        if promoted:
            with open(LESSONS_FILE, "a", encoding="utf-8") as f:
                for lesson in promoted:
                    f.write(json.dumps(lesson) + "\n")
            print(f"\nPromoted {len(promoted)} lesson(s) to {LESSONS_FILE}")
            print("Run 'lessons.py validate' to verify.")
        else:
            print("No lessons promoted.")
    elif cmd == "lineage":
        if len(argv) < 3:
            print("usage: lessons.py lineage <run_id>")
            print("  run_id: the run identifier to trace lineage for")
            sys.exit(1)

        run_id = argv[2]
        lineage_lessons = load_run_lineage(run_id)

        if not lineage_lessons:
            print(f"No lessons found with source_runs containing '{run_id}'")
            sys.exit(0)

        print(f"Lessons touched by run '{run_id}':")
        print()

        for item in lineage_lessons:
            lesson = item["lesson"]
            outcomes = item["outcomes"]
            print(f"{lesson.get('id')}: {lesson.get('title')}")
            print(f"  Status: {lesson.get('status')}")
            print(f"  Confidence: {lesson.get('confidence')}")
            print(f"  Times applied: {lesson.get('times_applied', 0)}")
            print(f"  Times helped: {lesson.get('times_helped', 0)}")
            print(f"  Times failed: {lesson.get('times_failed', 0)}")
            print(f"  Relationship: {item['relationship']}")
            if outcomes:
                print("  Outcomes:")
                for outcome in outcomes:
                    print(f"    {outcome['status']}: {outcome['note']}")
            print()
    else:
        print("usage: lessons.py validate | render | retrieve <sit.json> | build-situation <snap.json> <alerts.json> | reindex | verify-facts | promote <candidate-file> | lineage <run_id>")


if __name__ == "__main__":
    main()
