"""AI-ready debrief bundle (template-only, no API calls).

Writes one self-contained markdown file per run that can be pasted into any chat model:
  memory/debriefs/<run>.bundle.md          the prompt + data
  memory/debriefs/<run>.response.md        empty template for the model's answer
The wiki facts block is copied from memory/wiki-audit-20261018.md (verified entries only).
"""

import json
import os
import glob
import re
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Verified wiki facts (memory/wiki-audit-20261018.md, section D). Keep this list short and cited.
WIKI_FACTS = [
    "Mental break base thresholds for a normal colonist: minor 35%, major 20%, extreme 5% (wiki:Mental_break). Traits shift them (wiki:Mental_break).",
    "Base mood by difficulty: Peaceful 42, Community builder 42, Adventure story 37, Strive to survive 32, Blood and dust 27, Losing is Fun 22 (wiki:Mood).",
    "Mood bar moves toward its target at most +12/hour up and -8/hour down (wiki:Mood).",
    "Raid points cap at 10,000; wealth points use storyteller wealth up to 1,000,000 (wiki:Raid_points, wiki:Wealth).",
    "Shared barracks: Dull barracks -5 and Awful barracks -7 mood versus a private bedroom (wiki:Thoughts, wiki:Bedroom).",
    "Raw food: flat 2% food poisoning; cooked meals depend on cook skill and kitchen cleanliness (wiki:Rice, wiki:Blood_loss).",
    "Freezing point 0 C prevents spoilage; coolers can make freezers (wiki:Cooler).",
    "Rice matures in about 5.54 days and yields 6 units per plant (wiki:Rice).",
    "Herbal medicine is extracted from healroot. Industrial medicine needs cloth 3 + herbal 1 + neutroamine 1 and Medicine production research (wiki:Herbal_medicine, wiki:Research).",
    "Drug production (drug lab) and Medicine production are separate research projects; Medicine production requires Drug production (wiki:Research).",
    "Predators hunt colonists when hungry and keep attacking downed prey (wiki:Animals). Guinea pigs are herbivores (wiki:Guinea_pig).",
    "Sandbags: 55% cover, built from Fabric or Leathery material, 5 units (wiki:Sandbags).",
    "Incapable of Violent: cannot equip weapons or hunt (wiki:Incapable).",
    "Unburied colonist corpse triggers a 'left unburied' thought after 4 game days (wiki:Thoughts).",
    "Difficulty: Community builder research speed 120%, threat scale 30%; Adventure story research 100%, threat scale 60% (wiki:Difficulty, wiki:AI_Storytellers).",
]

UNVERIFIED = [
    "First raid day window (e.g. 'Days 8-15'): NOT in the wiki. Session 5 had a raid on Day 5 under Phoebe.",
    "Corpse -10 mood per corpse: NOT confirmed in the wiki text.",
    "Community Builder pre-researched projects: NOT in the wiki.",
    "Healroot 60% potency, packaged meal duration (~8 days for 3 pawns), ate-without-table -3: NOT confirmed.",
    "Sandbag material 'cloth only' (MCP tool observation): conflicts with the wiki (Fabric or Leathery).",
]

OUTPUT_FIELDS = [
    "title", "cause_chain", "trigger", "recommendation", "rationale",
    "source", "wiki_pages_used", "unverified_claims", "confidence",
]

PROMPT_RULES = """You are reviewing one RimWorld colony run to extract candidate lessons for a knowledge base.

Rules:
1. The wiki facts below are the source of truth. If a claim contradicts them, say so.
2. Cite evidence by in-game day (for example "Day 6, 12th of Septober") and by advice id.
3. Do not invent game mechanics. If you are unsure, list the claim under unverified_claims.
4. Do not repeat the timeline. Analyse it.
5. Propose at most 6 candidate lessons. Prefer fewer, better-supported ones.
6. Each candidate needs a trigger (phases, threats, resources, difficulty, storyteller, biome). Use "any" for unscoped fields.
7. Output exactly the two sections below, in this order, and nothing else.

Section A: a JSON array of candidate lessons. Each object has exactly these keys:
  title, cause_chain (array of short strings), trigger (object with phases, threats, resources, difficulty, storyteller, biome), recommendation, rationale, source (array of day strings or wiki page names), wiki_pages_used (array), unverified_claims (array), confidence (number 0.3 to 0.7).

Section B: a short markdown summary (max 10 bullet points): primary cause of failure or current risk, what worked, and what the next colony should do differently.
"""

PHASE_NOTE = (
    "Phases (our own labels, not wiki terms): early_survival (day 0-7), stabilization (day 8-20), "
    "raid_prep, expansion, crisis."
)


def _parse_day(day_str):
    day = str(day_str or "")
    m = re.search(r"(\d+)", day)
    num = int(m.group(1)) if m else 0
    mm = re.search(r"of\s+(\w+)", day)
    month = mm.group(1) if mm else ""
    ym = re.search(r",\s*(\d+)", day)
    year = int(ym.group(1)) if ym else 0
    order = {"Jugust": 0, "Septober": 1, "Decembary": 2, "Aprimay": 3, "Jumay": 4}
    return (year, order.get(month, 99), num)


def _colonists(snap):
    cwrap = snap.get("colonists") or {}
    if isinstance(cwrap, dict):
        return cwrap.get("colonists") or []
    return []


def _is_valid(snap):
    return bool(_colonists(snap)) or bool((snap.get("status") or {}).get("colonistCount"))


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
            f"- {rec.get('advice_id')} | {rec.get('timestamp')} | trigger={rec.get('trigger')} "
            f"| severity={rec.get('severity')} | status={rec.get('status')} | auto_paused={rec.get('auto_paused')}"
        )
        out.append(f"  situation: {rec.get('situation', '')}")
    out.append("")
    return out


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
    snapshots.sort(key=lambda s: _parse_day(_day_label(s)))

    meta = meta or {}
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
    lines.append(f"- difficulty: {meta.get('difficulty', 'Adventure story (baseline)')}")
    lines.append(f"- storyteller: {meta.get('storyteller', 'Cassandra Classic (baseline)')}")
    lines.append(f"- biome: {meta.get('biome', 'unknown')}")
    lines.append(f"- outcome: {meta.get('outcome', 'not stated by the user')}")
    lines.append(f"- snapshots used: {len(snapshots) - len(skipped)}")
    if skipped:
        lines.append(f"- snapshots skipped (no colony data): {', '.join(skipped)}")
    lines.append("")
    lines.append("## 3. Wiki facts (source of truth, verified)")
    lines.append("")
    for f in WIKI_FACTS:
        lines.append(f"- {f}")
    lines.append("")
    lines.append("## 4. Claims that are NOT verified (do not treat as facts)")
    lines.append("")
    for u in UNVERIFIED:
        lines.append(f"- {u}")
    lines.append("")
    lines.append("## 5. Colony timeline")
    lines.append("")
    lines.extend(timeline if timeline else ["(no valid snapshots)", ""])
    lines.append("## 6. Advice log")
    lines.append("")
    lines.extend(_advice_section(advice_records or []))
    lines.append("## 7. Task")
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
    from config import SNAPSHOTS_DIR, DEBRIEFS_DIR
    from advice_log import read_advice

    run = sys.argv[1] if len(sys.argv) > 1 else "current-run"
    snap_dir = SNAPSHOTS_DIR
    nested = os.path.join(SNAPSHOTS_DIR, run)
    if glob.glob(os.path.join(nested, "day-*.json")):
        snap_dir = nested
    b, r = build_bundle(snap_dir, DEBRIEFS_DIR, run, read_advice(run_id=run))
    print("bundle:", b)
    print("response template:", r)
