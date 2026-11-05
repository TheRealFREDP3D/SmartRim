import glob
import json
import os
import re
import shutil
import sys
from datetime import datetime

try:
    import requests as _requests
except ImportError:
    _requests = None

try:
    from smartrim.advice_log import read_advice
except ImportError:
    def read_advice(run_id=None, status=None):
        return []

try:
    from smartrim import config
except ImportError:
    config = None


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
    cand_dir = config.candidates_dir(run_name, create=True) if config else None
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


def archive_runtime_artifacts(run_name):
    """Move one run's runtime directory into runtime/archive/<run>-<stamp>/."""
    if config is None:
        return None
    src = config.run_dir(run_name)
    if not os.path.isdir(src):
        print(f"No runtime data for run {run_name}")
        return None
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    dest = os.path.join(config.RUNTIME_DIR, "archive", f"{run_name}-{stamp}")
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    shutil.move(src, dest)
    print(f"Archived runtime artifacts to {dest}")
    return dest


if __name__ == "__main__":
    _usage = (
        "Usage: python -m smartrim.debrief [run_id]\n"
        "       python -m smartrim.debrief add-lessons [run_id]\n"
        "\n"
        "Generates the debrief prompt, candidate-lessons template and v3 bundle for a run.\n"
        "add-lessons archives that run's runtime directory.\n"
        "Omit run_id to use the active run."
    )

    _args = sys.argv[1:]
    if _args and _args[0] in ("-h", "--help"):
        print(_usage)
        raise SystemExit(0)

    if _args and _args[0] == "add-lessons":
        run_name = _args[1] if len(_args) > 1 else config.resolve_run_id()
        if not run_name:
            print("No active run. Pass a run id: python -m smartrim.debrief add-lessons <run-id>")
            raise SystemExit(1)
        archive_runtime_artifacts(run_name)
        raise SystemExit(0)

    run_name = _args[0] if _args else config.resolve_run_id()
    if run_name and (run_name.startswith("-") or "/" in run_name or "\\" in run_name):
        print(f"Invalid run id: {run_name!r}\n\n{_usage}")
        raise SystemExit(2)
    if not run_name:
        print("No active run. Pass a run id: python -m smartrim.debrief <run-id>")
        raise SystemExit(1)

    snap_dir = config.snapshots_dir(run_name)
    if not snap_dir or not glob.glob(os.path.join(snap_dir, "day-*.json")):
        print(f"No snapshots for run {run_name}")
        raise SystemExit(1)
    debrief_dir = config.debriefs_dir(run_name, create=True)
    generate_debrief(snap_dir, debrief_dir, run_name)
    from smartrim.advice_log import read_advice
    from smartrim.debrief_bundle import build_bundle
    rid = run_name
    print("bundle:", build_bundle(snap_dir, debrief_dir, rid, read_advice(run_id=rid)))
