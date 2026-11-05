"""AI-ready debrief bundle (template-only, no API calls).

Writes one self-contained markdown file per run that can be pasted into any chat model:
  runtime/<run>/debriefs/<run>.bundle.md          the prompt + data
  runtime/<run>/debriefs/<run>.response.md        empty template for the model's answer
The wiki facts block is loaded from memory/wiki_facts.yaml (single source of truth).
"""

import contextlib
import glob
import json
import logging
import os
import re
from datetime import datetime

logger = logging.getLogger(__name__)

try:
    from smartrim import config
except ImportError:
    config = None
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

WIKI_FACTS_PATH = (
    config.WIKI_FACTS_FILE if config else os.path.join(BASE_DIR, "memory", "wiki_facts.yaml")
)
WIKI_DIR = config.WIKI_DIR if config else os.path.join(BASE_DIR, "memory", "wiki")


def _load_wiki_facts():
    """Load wiki facts from YAML file. Returns (verified_facts, unverified_facts)."""
    try:
        import yaml
    except ImportError:
        logger.warning("PyYAML not installed; using fallback empty facts")
        return [], []

    if not os.path.exists(WIKI_FACTS_PATH):
        logger.warning(f"Wiki facts file not found: {WIKI_FACTS_PATH}")
        return [], []

    try:
        with open(WIKI_FACTS_PATH, encoding="utf-8") as f:
            data = yaml.safe_load(f) or []
    except (OSError, yaml.YAMLError) as e:
        logger.error(f"Failed to load wiki facts: {e}")
        return [], []

    verified = []
    unverified = []

    for entry in data:
        if not isinstance(entry, dict):
            continue
        text = entry.get("text", "")
        source_pages = entry.get("source_page")
        status = entry.get("status", "unverified")

        # Format source pages as wiki:citation
        if source_pages:
            if isinstance(source_pages, str):
                citations = f" (wiki:{source_pages})"
            elif isinstance(source_pages, list):
                citations = " (wiki:" + ", wiki:".join(source_pages) + ")"
            else:
                citations = ""
        else:
            citations = ""

        fact_with_citation = text + citations

        if status == "verified":
            verified.append(fact_with_citation)
        else:
            unverified.append(text)  # Unverified facts don't get citations

    return verified, unverified


# Load facts at module init (cached for performance)
WIKI_FACTS, UNVERIFIED = _load_wiki_facts()

OUTPUT_FIELDS = [
    "title", "cause_chain", "trigger", "recommendation", "rationale",
    "source", "wiki_pages_used", "unverified_claims", "confidence",
]

PROMPT_RULES = """You are reviewing one RimWorld colony run to extract candidate lessons for a knowledge base.

Rules:
1. The wiki facts below are the source of truth. If a claim contradicts them, say so.
2. Cite evidence by in-game day (for example "Day 6, 12th of Septober") and by advice id.
3. Do not invent game mechanics. If you are unsure, list the claim under unverified_claims.
4. Read the quest context before calling a pawn a colonist. A quest target has an objective and a leaving condition, and treating them as a settler produces the wrong lesson.
5. Where a record carries "cause (recorded after the run)", that is ground truth from the player. Do not re-diagnose against it; build the lesson on it.
6. Do not repeat the timeline. Analyse it.
7. Propose at most 6 candidate lessons. Prefer fewer, better-supported ones.
8. Each candidate needs a trigger (phases, threats, resources, difficulty, storyteller, biome). Use "any" for unscoped fields.
9. Output exactly the two sections below, in this order, and nothing else.

Section A: a JSON array of candidate lessons. Each object has exactly these keys:
  title, cause_chain (array of short strings), trigger (object with phases, threats, resources, difficulty, storyteller, biome), recommendation, rationale, source (array of day strings or wiki page names), wiki_pages_used (array), unverified_claims (array), confidence (number 0.3 to 0.7).

Section B: a short markdown summary (max 10 bullet points): primary cause of failure or current risk, what worked, and what the next colony should do differently.
"""

PHASE_NOTE = (
    "Phases (our own labels, not wiki terms): early_survival (day 0-7), stabilization (day 8-20), "
    "raid_prep, expansion, crisis."
)

# Bump when the bundle's shape changes: scores are only comparable within one version.
BUNDLE_VERSION = "v3.1 (wiki excerpts, quests, event causes, incident snapshots)"

# Wiki pages that tend to matter for each phase and threat. Used to pick the
# 3-5 excerpts pasted into section 3, so the model gets grounded facts instead
# of an empty "source of truth" block.
PHASE_PAGES = {
    "early_survival": ["Basics", "Quickstart_Guides", "Food", "Temperature", "Growing", "Raid", "Medicine"],
    "stabilization": ["Base", "Room_roles", "Mood", "Recreation", "Research", "Defense"],
    "raid_prep": ["Raid", "Defense", "Cover", "Turret", "Sandbags", "Shooting"],
    "expansion": ["Wealth", "Research", "Power", "Trade", "Base"],
    "crisis": ["Mental_break", "Raid", "Firefighting", "Injury", "Medicine"],
}

THREAT_PAGES = {
    "low_food": ["Food", "Meals", "Farming", "Growing", "Cooking", "Cooler", "Stockpile"],
    "medical_untreated": ["Medicine", "Injury", "Infection", "Doctoring", "Hospital"],
    "colonist_injured": ["Injury", "Medicine", "Doctoring", "Pain"],
    "mood_break_risk": ["Mood", "Mental_break", "Recreation", "Thoughts", "Joy"],
    "raid_incoming": ["Raid", "Defense", "Cover", "Sandbags", "Turret"],
    "predator_near_worker": ["Animals", "Taming", "Shooting", "Melee"],
    "danger_high": ["Defense", "Raid", "Cover", "Turret"],
    "threat_response": ["Firefighting", "Raid", "Defense"],
    "idle_colonists": ["Schedule", "Skills", "Work"],
    "colonist_downed": ["Injury", "Medicine", "Hospital"],
    "colony_death": ["Mental_break", "Injury", "Raid"],
}

FALLBACK_PAGES = ["Basics", "Food", "Mood"]

# Lines that are navigation chrome or maintenance banners rather than wiki prose.
_NAV_PREFIXES = (
    "jump to",
    "contents",
    "from rimworld wiki",
    "see also",
    "navigation",
    "retrieved from",
    "categories:",
)

_BOILERPLATE_MARKERS = (
    "suggested to be rewritten",
    "you can help the rimworld wiki",
    "this article is a stub",
    "candidate for deletion",
    "needs citation",
)

# Snapshot alerts are raw game alerts and carry no monitor category, so map
# their labels to the threat vocabulary used by lessons and page selection.
LABEL_THREATS = (
    ("combatant unarmed", "danger_high"),
    ("need defenses", "danger_high"),
    ("low medicine", "medical_untreated"),
    ("medicine stock low", "medical_untreated"),
    ("medical treatment", "medical_untreated"),
    ("injur", "colonist_injured"),
    ("break risk", "mood_break_risk"),
    ("low food", "low_food"),
    ("food stock low", "low_food"),
    ("meal source", "low_food"),
    ("starv", "low_food"),
    ("predator", "predator_near_worker"),
    ("raid", "raid_incoming"),
    ("hostile", "raid_incoming"),
    ("fire", "threat_response"),
)


def _wiki_dir():
    return globals().get("WIKI_DIR") or (config.WIKI_DIR if config else "")


def _clean_wiki_text(text):
    text = re.sub(r"&#\d+;", " ", str(text or ""))
    text = re.sub(r"<[^>]+>", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def _is_prose(paragraph):
    low = paragraph.lower()
    if len(paragraph) < 80:
        return False
    if any(low.startswith(prefix) for prefix in _NAV_PREFIXES):
        return False
    if any(marker in low for marker in _BOILERPLATE_MARKERS):
        return False
    return "." in paragraph


def _wiki_excerpt(page, keywords, max_chars=420):
    """Best short paragraph from a wiki page for the run's keywords."""
    path = os.path.join(_wiki_dir(), f"{page}.md")
    try:
        with open(path, encoding="utf-8") as f:
            raw = f.read()
    except OSError:
        return None
    paragraphs = []
    for block in re.split(r"\n\s*\n", raw):
        cleaned = _clean_wiki_text(block)
        if _is_prose(cleaned):
            paragraphs.append(cleaned)
    if not paragraphs:
        return None
    low_keywords = [k.lower() for k in keywords if k and len(k) > 3]

    def score(paragraph):
        low = paragraph.lower()
        return sum(low.count(k) for k in low_keywords)

    best = max(paragraphs, key=score)
    if score(best) == 0:
        best = paragraphs[0]
    if len(best) > max_chars:
        cut = best[:max_chars]
        dot = cut.rfind(". ")
        best = cut[: dot + 1] if dot > max_chars // 2 else cut.rstrip() + "..."
    return best


def _select_wiki_pages(phase, threats, keywords, limit=5):
    """Rank cached wiki pages for this run and return at most ``limit`` names.

    One page per threat first, so a medical-heavy run does not return five
    medicine pages and nothing about mood or defense.
    """
    available = set()
    with contextlib.suppress(OSError):
        available = {name[:-3] for name in os.listdir(_wiki_dir()) if name.endswith(".md")}
    scores = {}
    for page in PHASE_PAGES.get(phase, []):
        scores[page] = scores.get(page, 0) + 3
    for threat in threats or ():
        for page in THREAT_PAGES.get(threat, []):
            scores[page] = scores.get(page, 0) + 4
    text = " ".join(keywords or ()).lower()
    for page in list(scores):
        if page.replace("_", " ").lower() in text:
            scores[page] += 2

    def usable(page):
        return not available or page in available

    picked = []
    for threat in sorted(threats or ()):
        candidates = [p for p in THREAT_PAGES.get(threat, []) if p in scores and usable(p)]
        if candidates:
            best = max(candidates, key=lambda p: (scores[p], p))
            if best not in picked:
                picked.append(best)
        if len(picked) >= limit:
            return picked[:limit]

    for page in PHASE_PAGES.get(phase, []):
        if len(picked) >= limit:
            return picked[:limit]
        if page not in picked and usable(page):
            picked.append(page)

    ranked = sorted(scores, key=lambda p: (-scores[p], p))
    for page in ranked:
        if len(picked) >= limit:
            return picked[:limit]
        if page not in picked and usable(page):
            picked.append(page)

    if len(picked) < 3:
        for page in FALLBACK_PAGES:
            if page not in picked and usable(page):
                picked.append(page)
            if len(picked) >= 3:
                break
    return picked[:limit]


def _threats_from_labels(alerts):
    """Map raw game-alert labels to the threat vocabulary."""
    found = set()
    for alert in alerts or ():
        label = str(alert.get("label") or alert.get("message") or "").lower()
        for needle, threat in LABEL_THREATS:
            if needle in label:
                found.add(threat)
    return found


def _run_wiki_context(snapshots, advice_records, meta):
    """Phase, threats and keyword text for choosing wiki excerpts.

    Threats are unioned across every snapshot (and the advice log), not just the
    last one: a food crisis or an unarmed-colonist warning that resolved before
    the final day still shaped the run and should inform the excerpts.
    """
    phase = "early_survival"
    threats = set()
    keywords = []
    try:
        from smartrim import situation as _situation
    except ImportError:
        _situation = None

    for snap in snapshots or ():
        alerts = (snap.get("alerts") or {}).get("activeAlerts") or []
        if _situation is not None:
            with contextlib.suppress(KeyError, TypeError, ValueError):
                threats |= _situation.build_threats(alerts)
        threats |= _threats_from_labels(alerts)
        for alert in alerts:
            label = alert.get("label") or alert.get("message")
            if label:
                keywords.append(str(label))

    last = snapshots[-1] if snapshots else {}
    summary = last.get("summary") or {}
    last_alerts = (last.get("alerts") or {}).get("activeAlerts") or []
    if _situation is not None:
        with contextlib.suppress(KeyError, TypeError, ValueError):
            phase = _situation.classify_phase(summary, last_alerts)

    for rec in advice_records or []:
        text = rec.get("situation")
        if text:
            keywords.append(str(text))
        for risk in rec.get("risks") or []:
            if isinstance(risk, dict) and risk.get("label"):
                label = str(risk["label"])
                keywords.append(label)
                threats |= _threats_from_labels([{"label": label}])
    keywords.append(str((meta or {}).get("biome") or ""))
    keywords.append(str((meta or {}).get("storyteller") or ""))
    return phase, threats, keywords


def _wiki_section_lines(snapshots, advice_records, meta):
    """Section 3 body: curated facts when present, else selected wiki excerpts."""
    if WIKI_FACTS:
        return [f"- {fact}" for fact in WIKI_FACTS]
    phase, threats, keywords = _run_wiki_context(snapshots, advice_records, meta)
    selected = _select_wiki_pages(phase, threats, keywords)

    # Some pages are stubs with no prose (Defense is one), so fall back to the
    # next page for the same threat rather than leaving a slot empty.
    alternates = []
    for threat in sorted(threats or ()):
        alternates.extend(THREAT_PAGES.get(threat, []))
    alternates.extend(PHASE_PAGES.get(phase, []))
    alternates.extend(FALLBACK_PAGES)

    lines = []
    seen = set()
    for page in list(selected) + alternates:
        if page in seen or len(lines) >= 5:
            continue
        seen.add(page)
        excerpt = _wiki_excerpt(page, keywords)
        if excerpt:
            lines.append(f"- **{page.replace('_', ' ')}** (wiki:{page}): {excerpt}")
    if not lines:
        lines.append("- (no wiki pages matched this run; do not assume wiki facts)")
    return lines



def _parse_day(day_str):
    day = str(day_str or "")
    m = re.search(r"(\d+)", day)
    num = int(m.group(1)) if m else 0
    mm = re.search(r"of\s+(\w+)", day)
    month = mm.group(1) if mm else ""
    ym = re.search(r",\s*(\d+)", day)
    year = int(ym.group(1)) if ym else 0
    # RimWorld quadrum order: Aprimay (spring) -> Jugust (summer) -> Septober (autumn) -> Decembary (winter).
    order = {"Aprimay": 0, "Jugust": 1, "Septober": 2, "Decembary": 3}
    return (year, order.get(month, 99), num)


def _make_sort_key(snap):
    cond = snap.get("conditions") or {}
    hour = cond.get("hour")
    return (*_parse_day(_day_label(snap)), hour if isinstance(hour, int) else 0)


def _colonists(snap):
    cwrap = snap.get("colonists") or {}
    if isinstance(cwrap, dict):
        return cwrap.get("colonists") or []
    return []


def _is_valid(snap):
    colonists = _colonists(snap)
    if colonists:
        return True
    status = snap.get("status") or {}
    cc = status.get("colonistCount")
    if cc and cc > 0:
        return True
    day_label = str(_day_label(snap) or "").lower()
    if day_label.startswith(("end", "reflex", "day")):
        if cc == 0 or cc is None:
            return False
        return bool(cc)
    return bool(cc)


def _day_label(snap):
    cond = snap.get("conditions") or {}
    return cond.get("date") or snap.get("day") or "unknown day"


def _timeline(snapshots):
    lines = []
    skipped = []
    for snap in snapshots:
        if not _is_valid(snap):
            skipped.append(str(snap.get("_file")))
            continue
        cond = snap.get("conditions") or {}
        lines.append(f"### {_day_label(snap)} (hour {cond.get('hour')})")
        for c in _colonists(snap):
            flags = []
            if c.get("downed"):
                flags.append("DOWNED")
            if c.get("dead"):
                flags.append("DEAD")
            lines.append(
                f"- {c.get('name')}: HP {c.get('health')}%, mood {c.get('mood')}%, job: {c.get('job')}"
                + (f" [{', '.join(flags)}]" if flags else "")
            )
        alerts = (snap.get("alerts") or {}).get("activeAlerts") or []
        if alerts:
            lines.append("- Alerts: " + "; ".join(a.get("label", "") for a in alerts))
        res = (snap.get("resources") or {}).get("resources") or []
        if res:
            lines.append("- Resources: " + ", ".join(f"{r.get('label')} {r.get('count')}" for r in res))
        lines.append("")
    return lines, skipped


def _advice_section(advice_records):
    if not advice_records:
        return ["(no advice records for this run)", ""]
    out = []
    for rec in advice_records:
        out.append(
            f"- {rec.get('advice_id')} | day={rec.get('snapshot_day')} | {rec.get('timestamp')} | trigger={rec.get('trigger')} "
            f"| severity={rec.get('severity')} | status={rec.get('status')} | auto_paused={rec.get('auto_paused')}"
        )
        out.append(f"  situation: {rec.get('situation', '')}")
        if rec.get("event_cause"):
            out.append(f"  cause (recorded after the run): {rec.get('event_cause')}")
    out.append("")
    return out


FOOD_KEYS = ("meal", "rice", "corn", "potato", "berry", "meat", "bread", "kibble")


def _food_units(snap):
    total = 0
    for r in (snap.get("resources") or {}).get("resources") or []:
        label = str(r.get("label") or r.get("defName") or "").lower()
        if any(k in label for k in FOOD_KEYS):
            total += r.get("count") or 0
    return total


def _quest_records(snapshots):
    """Quest context embedded in snapshots, merged by id. Missing module is not fatal."""
    try:
        from smartrim import quests as quests_mod
    except ImportError as e:
        logger.debug("quests module unavailable: %s", e)
        return []
    try:
        return quests_mod.quests_from_snapshots(snapshots)
    except (OSError, ValueError, TypeError, KeyError) as e:
        logger.debug("quest records failed: %s", e)
        return []


def _incident_lines(reflex_snapshots):
    """One block per incident snapshot: what the colony looked like when an urgent alert fired."""
    out = []
    for snap in reflex_snapshots or []:
        if not _is_valid(snap):
            continue
        cond = snap.get("conditions") or {}
        stamp = str(snap.get("timestamp") or "")
        clock = stamp[11:16] if len(stamp) >= 16 else ""
        when = _day_label(snap)
        if cond.get("hour") is not None:
            when += f", hour {cond.get('hour')}"
        if clock:
            when += f" ({clock})"
        alerts = [a.get("label") for a in (snap.get("alerts") or {}).get("activeAlerts") or [] if a.get("label")]
        out.append(f"- {when}: " + ("alerts: " + "; ".join(alerts) if alerts else "no active alerts"))
        for c in _colonists(snap):
            flags = []
            if c.get("downed"):
                flags.append("DOWNED")
            if c.get("dead"):
                flags.append("DEAD")
            out.append(
                f"  - {c.get('name')}: HP {c.get('health')}%, mood {c.get('mood')}%, job: {c.get('job')}"
                + (f" [{', '.join(flags)}]" if flags else "")
            )
        quests_now = snap.get("quests") or []
        if quests_now:
            out.append("  - quests: " + "; ".join(
                f"[{q.get('id')}] {q.get('name')} ({q.get('last_state') or q.get('state') or '?'})"
                for q in quests_now if isinstance(q, dict)
            ))
    if out:
        out.append("")
    return out


def _event_digest(snapshots, advice_records, reflex_snapshots=None):
    """Transitions between daily snapshots: what changed, not what the day looked like.

    The timeline shows daily stills; this section names the changes (new alerts, injuries,
    downed pawns, food swings), the incident snapshots taken when an urgent alert fired, and
    the urgent advice that fired between snapshots.
    """
    events = []
    prev_alerts = set()
    prev_hp = {}
    prev_food = None
    for snap in snapshots:
        label = _day_label(snap)
        cond = snap.get("conditions") or {}
        hour = cond.get("hour")
        alerts = {a.get("label") for a in (snap.get("alerts") or {}).get("activeAlerts") or [] if a.get("label")}
        new = sorted(alerts - prev_alerts)
        if new:
            events.append((label, hour, "new alerts: " + "; ".join(new)))
        for c in _colonists(snap):
            name = c.get("name")
            hp = c.get("health")
            old = prev_hp.get(name)
            if old is not None and hp is not None and old - hp >= 10:
                events.append((label, hour, f"{name} health {old}% -> {hp}% (injury)"))
            if c.get("downed"):
                events.append((label, hour, f"{name} DOWNED"))
            if hp is not None:
                prev_hp[name] = hp
        food = _food_units(snap)
        if prev_food is not None and food >= 0:
            if prev_food - food >= max(20, prev_food * 0.5):
                events.append((label, hour, f"food stock fell {prev_food} -> {food} units"))
            elif food - prev_food >= max(50, prev_food * 2):
                events.append((label, hour, f"food stock jumped {prev_food} -> {food} units"))
        prev_food = food
        prev_alerts = alerts

    urgent = [r for r in advice_records or [] if r.get("trigger") == "reflex" and r.get("severity") == "urgent"]
    out = []
    if events:
        out.append("Transitions between snapshots:")
        out.append("")
        for label, hour, text in events:
            when = label + (f", hour {hour}" if hour is not None else "")
            out.append(f"- {when}: {text}")
        out.append("")
    else:
        out.append("(no transitions detected between snapshots)")
        out.append("")

    incidents = _incident_lines(reflex_snapshots)
    if incidents:
        out.append("Incident snapshots (taken when an urgent alert fired, so short events survive):")
        out.append("")
        out.extend(incidents)
    elif reflex_snapshots is not None:
        out.append("(no incident snapshots for this run - they are captured only when an urgent alert fires)")
        out.append("")

    if urgent:
        out.append("Urgent advice recorded (in-game day from the monitor, real timestamp in section 7):")
        out.append("")
        grouped = []
        for rec in urgent:
            text = re.sub(r"<[^>]+>", "", str(rec.get("situation") or "")).strip()
            key = (rec.get("snapshot_day"), text)
            cause = rec.get("event_cause")
            if grouped and grouped[-1]["key"] == key:
                grouped[-1]["count"] += 1
                grouped[-1]["cause"] = cause or grouped[-1]["cause"]
            else:
                grouped.append({"key": key, "count": 1, "status": rec.get("status"), "cause": cause})
        for item in grouped:
            day, text = item["key"]
            suffix = f" ({item['count']}x)" if item["count"] > 1 else ""
            cause_txt = f" - cause: {item['cause']}" if item["cause"] else ""
            out.append(f"- {day}: {text}{suffix} [{item['status']}]{cause_txt}")
        out.append("")
    return out



def _load_run_marker(run_id):
    """Read runtime/<run_id>/end.json (monitor) and meta.json (human/agent notes)."""
    out = {}
    for name in ("meta.json", "end.json"):
        path = config.run_file(name, run_id) if config else None
        if not path:
            continue
        try:
            with open(path, encoding="utf-8") as f:
                data = json.load(f)
            if isinstance(data, dict):
                out.update(data)
        except (OSError, json.JSONDecodeError):
            continue
    return out


def _derive_outcome(marker, final_summary):
    if not marker and not final_summary:
        return None
    parts = []
    if marker.get("stop_reason") == "run_length":
        parts.append(f"survived the full run ({marker.get('days_passed')} days, run-limited)")
    elif marker.get("stop_reason"):
        parts.append(f"run ended early: {marker.get('stop_reason')}")
    if final_summary:
        cols = final_summary.get("colonist_count")
        if cols is not None:
            downed = final_summary.get("downed") or []
            parts.append(f"{cols} colonist(s) alive at the end" + (f", downed: {', '.join(downed)}" if downed else ", none downed"))
        if final_summary.get("min_mood") is not None:
            parts.append(f"lowest end-of-day mood {final_summary.get('min_mood')}%")
        if final_summary.get("food_days") is not None:
            parts.append(f"{final_summary.get('food_days')} days of food")
        if final_summary.get("medicine_count") is not None:
            parts.append(f"{final_summary.get('medicine_count')} medicine")
        if final_summary.get("wealth") is not None:
            parts.append(f"wealth {final_summary.get('wealth')}")
    if marker:
        parts.append(f"urgent alerts {marker.get('urgent_alerts')}, auto-pauses {marker.get('auto_pauses')}")
    return "; ".join(parts) if parts else None


def build_bundle(snapshots_dir, debriefs_dir, run_id, advice_records=None, meta=None):
    """Write the paste-ready bundle and the response template. Returns (bundle_path, response_path)."""
    files = sorted(glob.glob(os.path.join(snapshots_dir, "day-*.json")))
    snapshots = []
    for f in files:
        try:
            with open(f, encoding="utf-8") as fh:
                snap = json.load(fh)
        except (OSError, json.JSONDecodeError):
            continue
        snap["_file"] = os.path.basename(f)
        snapshots.append(snap)
    snapshots.sort(key=_make_sort_key)

    # Incident snapshots: taken by the monitor when a new urgent alert fires. They are kept
    # out of the timeline (which stays one still per day) and shown in the digest instead.
    reflex = []
    for f in sorted(glob.glob(os.path.join(snapshots_dir, "reflex-*.json"))):
        try:
            with open(f, encoding="utf-8") as fh:
                snap = json.load(fh)
        except (OSError, json.JSONDecodeError):
            continue
        snap["_file"] = os.path.basename(f)
        reflex.append(snap)
    reflex.sort(key=lambda s: (_make_sort_key(s), str(s.get("timestamp") or "")))

    meta = dict(meta or {})
    marker = _load_run_marker(run_id)
    final_summary = (snapshots[-1].get("summary") or {}) if snapshots else {}
    if not meta.get("outcome"):
        derived = _derive_outcome(marker, final_summary)
        if derived:
            meta["outcome"] = derived
    if not meta.get("biome"):
        meta["biome"] = marker.get("biome") or "unknown"
    if not meta.get("quests") and marker.get("quests"):
        meta["quests"] = marker.get("quests")
        if marker.get("quests_recorded_after_run"):
            meta["quests_recorded_after_run"] = True
    if not meta.get("causes") and marker.get("causes"):
        meta["causes"] = marker.get("causes")
    timeline, skipped = _timeline(snapshots)
    now = datetime.now().isoformat(timespec="seconds")

    lines = []
    lines.append(f"# Debrief bundle: {run_id}")
    lines.append("")
    lines.append(f"Generated: {now}. Paste this whole file into a chat model, then paste its answer into `{run_id}.response.md`.")
    lines.append("")
    lines.append("## 1. Instructions")
    lines.append("")
    lines.append(PROMPT_RULES.strip())
    lines.append("")
    lines.append(PHASE_NOTE)
    lines.append("")
    lines.append("## 2. Run metadata")
    lines.append("")
    lines.append(f"- run_id: {run_id}")
    lines.append(f"- bundle version: {BUNDLE_VERSION}")
    lines.append(f"- difficulty: {meta.get('difficulty', 'Adventure story (baseline)')}")
    lines.append(f"- storyteller: {meta.get('storyteller', 'Cassandra Classic (baseline)')}")
    lines.append(f"- biome: {meta.get('biome', 'unknown')}")
    lines.append(f"- outcome: {meta.get('outcome', 'not stated by the user')}")
    run_causes = meta.get("causes") or []
    if run_causes:
        lines.append("- event causes (recorded after the run, from the player):")
        for cause in run_causes:
            if isinstance(cause, dict):
                label = cause.get("event") or cause.get("name") or "event"
                text = cause.get("cause") or ""
                lines.append(f"  - {label}: {text}" if text else f"  - {label}")
            else:
                lines.append(f"  - {cause}")
    lines.append(f"- snapshots used: {len(snapshots) - len(skipped)}")
    if skipped:
        lines.append(f"- snapshots skipped (no colony data): {', '.join(skipped)}")
    if reflex:
        lines.append(f"- incident snapshots (urgent-alert moments): {len(reflex)}")
    quest_records = _quest_records(snapshots + reflex)
    quest_note = None
    if not quest_records and meta.get("quests"):
        quest_records = meta["quests"]
        if meta.get("quests_recorded_after_run"):
            quest_note = "recorded after the run; this run's snapshots predate quest capture"
    if quest_records:
        lines.append("")
        lines.append("Quest context from the game (colour tags removed; this is where quest objectives live):")
        if quest_note:
            lines.append(f"({quest_note})")
        lines.append("")
        try:
            from smartrim import quests as quests_mod
            lines.extend(quests_mod.summary_lines(quest_records))
        except ImportError as e:
            logger.debug("quests module unavailable: %s", e)
            for rec in quest_records:
                lines.append(f"- [{rec.get('id')}] {rec.get('name')}: {rec.get('description') or 'no description'}")
        except (TypeError, AttributeError, KeyError) as e:
            logger.debug("quest summary failed: %s", e)
            for rec in quest_records:
                lines.append(f"- [{rec.get('id')}] {rec.get('name')}: {rec.get('description') or 'no description'}")
    else:
        lines.append("- quests: none recorded")
    lines.append("")
    lines.append("## 3. Wiki facts (source of truth, verified)")
    lines.append("")
    lines.extend(_wiki_section_lines(snapshots, advice_records or [], meta))
    lines.append("")
    lines.append("## 4. Claims that are NOT verified (do not treat as facts)")
    lines.append("")
    if UNVERIFIED:
        for u in UNVERIFIED:
            lines.append(f"- {u}")
    else:
        lines.append("- (none recorded for this run)")
    lines.append("")
    lines.append("## 5. Colony timeline")
    lines.append("")
    lines.extend(timeline if timeline else ["(no valid snapshots)", ""])
    lines.append("## 6. Notable changes and incidents (event digest)")
    lines.append("")
    lines.extend(_event_digest(snapshots, advice_records or [], reflex_snapshots=reflex))
    lines.append("## 7. Advice log")
    lines.append("")
    lines.extend(_advice_section(advice_records or []))
    lines.append("## 8. Task")
    lines.append("")
    lines.append("Produce Section A (JSON array) and Section B (markdown summary) as described in the instructions.")
    lines.append("")

    os.makedirs(debriefs_dir, exist_ok=True)
    bundle_path = os.path.join(debriefs_dir, f"{run_id}.bundle.md")
    with open(bundle_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    resp_lines = [
        f"# Model response: {run_id}",
        "",
        "Provider / model: ",
        "Date: ",
        "Notes on the run (anything the model got wrong or missed): ",
        "",
        "## Section A (JSON)",
        "",
        "```json",
        "[]",
        "```",
        "",
        "## Section B (summary)",
        "",
        "- ",
        "",
    ]
    response_path = os.path.join(debriefs_dir, f"{run_id}.response.md")
    if not os.path.exists(response_path):
        with open(response_path, "w", encoding="utf-8") as f:
            f.write("\n".join(resp_lines))

    return bundle_path, response_path


if __name__ == "__main__":
    import sys

    from smartrim.advice_log import read_advice

    run = sys.argv[1] if len(sys.argv) > 1 else config.resolve_run_id()
    if not run:
        print("No active run. Pass a run id: python -m smartrim.debrief_bundle <run-id>")
        raise SystemExit(1)
    snap_dir = config.snapshots_dir(run)
    if not snap_dir:
        print(f"No snapshots for run {run}")
        raise SystemExit(1)
    debrief_dir = config.debriefs_dir(run, create=True)
    b, r = build_bundle(snap_dir, debrief_dir, run, read_advice(run_id=run))
    print("bundle:", b)
    print("response template:", r)
