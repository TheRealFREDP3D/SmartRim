import glob
import json
import os
import re
import sys
from datetime import datetime

try:
    import requests as _requests
except Exception:
    _requests = None

try:
    from advice_log import read_advice
except Exception:
    def read_advice(run_id=None, status=None):
        return []

try:
    from config import CANDIDATES_DIR, DEBRIEFS_DIR, SNAPSHOTS_DIR
except Exception:
    CANDIDATES_DIR = None
    DEBRIEFS_DIR = None
    SNAPSHOTS_DIR = None


MONTH_ORDER = {
    "Aprimay": 0, "Jugust": 1, "Septober": 2, "Decembary": 3,
    "Jumay": 4,
}


def _day_key(snap):
    day = str(snap.get("day", ""))
    m = re.search(r"(\d+)", day)
    num = int(m.group(1)) if m else 0
    mm = re.search(r"of\s+(\w+)", day)
    month = mm.group(1) if mm else ""
    ym = re.search(r",\s*(\d+)", day)
    year = int(ym.group(1)) if ym else 0
    month_idx = MONTH_ORDER.get(month, 99)
    return (year, month_idx, num)


def generate_debrief(snapshots_dir, debriefs_dir, run_name=None):
    pattern = os.path.join(snapshots_dir, "day-*.json")
    files = sorted(glob.glob(pattern))

    if not files:
        print("No snapshots found")
        return None

    snapshots = []
    for f in files:
        try:
            with open(f, encoding="utf-8") as fh:
                snapshots.append(json.load(fh))
        except (json.JSONDecodeError, OSError) as e:
            print(f"Skipping {f}: {e}")

    if not snapshots:
        print("No valid snapshots found")
        return None

    snapshots.sort(key=_day_key)

    run_name = run_name or f"run-{datetime.now().strftime('%Y%m%d-%H%M%S')}"

    # Read advice records for this run
    advice_records = read_advice(run_id=run_name) if run_name else []

    lines = []
    lines.append(f"# Debrief: {run_name}")
    lines.append("")
    lines.append(f"Generated: {datetime.now().isoformat()}")
    lines.append(f"Snapshots: {len(snapshots)}")
    lines.append("")
    lines.append("## Colony Timeline")
    lines.append("")

    for snap in snapshots:
        day = snap.get("day", "?")
        conditions = snap.get("conditions", {}) or {}
        colonists = []
        cwrap = snap.get("colonists", {})
        if isinstance(cwrap, dict):
            colonists = cwrap.get("colonists", []) or []
        alerts = snap.get("alerts", {}) or {}
        resources = snap.get("resources", {}) or {}
        research = snap.get("research", {}) or {}

        lines.append(f"### Day {day}")
        lines.append(f"- Date (conditions): {conditions.get('date')} Hour {conditions.get('hour')}")
        lines.append(f"- Season: {conditions.get('seasonLabel')} | Weather: {conditions.get('weather', {}).get('current') if isinstance(conditions.get('weather'), dict) else conditions.get('weather')}")
        lines.append(f"- Colonists: {len(colonists)}")
        for c in colonists:
            lines.append(
                f"  - {c.get('name', 'Unknown')}: HP {c.get('health', '?')}%, Mood {c.get('mood', '?')}%"
                + (" [DOWNED]" if c.get("downed") else "")
            )
        active_alerts = alerts.get("activeAlerts", []) if isinstance(alerts, dict) else []
        if active_alerts:
            lines.append(f"- Alerts: {', '.join(a.get('label', '') for a in active_alerts)}")
        danger = alerts.get("dangerByMap", []) if isinstance(alerts, dict) else []
        if danger:
            lines.append(f"- Danger ratings: {', '.join(str(d.get('dangerRating')) for d in danger)}")
        res_list = resources.get("resources", []) if isinstance(resources, dict) else []
        if res_list:
            lines.append("- Resources: " + ", ".join(f"{r.get('label')}:{r.get('count')}" for r in res_list))
        if isinstance(research, dict) and research.get("current"):
            cur = research["current"]
            lines.append(f"- Research: {cur.get('label')} ({cur.get('progressPercent', '?')}%)")
        lines.append("")

    # Advice log section
    if advice_records:
        lines.append("## Advice log")
        lines.append("")
        lines.append(f"{len(advice_records)} advice records for this run.")
        lines.append("")
        for rec in advice_records:
            lines.append(f"- [{rec.get('advice_id')}] ({rec.get('trigger')}, {rec.get('severity')}) status={rec.get('status')}: {rec.get('situation', '')[:120]}")
        lines.append("")

    lines.append("## Analysis Request")
    lines.append("")
    lines.append("Based on the timeline above:")
    lines.append("1. What was the primary cause of colony failure (or current risk)?")
    lines.append("2. What worked well?")
    lines.append("3. What lessons should be added to lessons-learned.md? (include trigger condition + recommended action)")
    lines.append("4. What should the next colony do differently?")
    lines.append("")

    os.makedirs(debriefs_dir, exist_ok=True)
    path = os.path.join(debriefs_dir, f"{run_name}.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    # Candidate lessons file (human-reviewed before merging)
    cand_dir = CANDIDATES_DIR
    if cand_dir:
        os.makedirs(cand_dir, exist_ok=True)
        cand_path = os.path.join(cand_dir, f"{run_name}.md")
        cand_lines = [
            f"# Candidate lessons: {run_name}",
            "",
            "Generated by debrief.py. Review each candidate before merging into lessons-learned.md.",
            "A candidate is mergeable only if it has a source (snapshot day or wiki page).",
            "",
            "## Template",
            "",
            "### <title>",
            "- Trigger: <phase/threat/resource condition>",
            "- Recommendation: <action>",
            "- Rationale: <failure mode prevented>",
            "- Source: <snapshot day or wiki page>",
            "- Confidence: 0.3 (initial)",
            "",
            "## Candidates",
            "",
            "(Fill in from the debrief above.)",
            "",
        ]
        with open(cand_path, "w", encoding="utf-8") as f:
            f.write("\n".join(cand_lines))
        print(f"Candidate lessons template written: {cand_path}")

    print(f"Debrief prompt written: {path}")
    return path


if __name__ == "__main__":
    from config import DEBRIEFS_DIR, SNAPSHOTS_DIR

    run_name = sys.argv[1] if len(sys.argv) > 1 else None
    snap_dir = SNAPSHOTS_DIR
    if run_name:
        nested = os.path.join(SNAPSHOTS_DIR, run_name)
        if glob.glob(os.path.join(nested, "day-*.json")):
            snap_dir = nested
    generate_debrief(snap_dir, DEBRIEFS_DIR, run_name)
    from advice_log import read_advice
    from debrief_bundle import build_bundle
    rid = run_name or "current-run"
    print("bundle:", build_bundle(snap_dir, DEBRIEFS_DIR, rid, read_advice(run_id=rid)))
