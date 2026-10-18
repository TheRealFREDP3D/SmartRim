import os
import sys
import json
import glob
import re
from datetime import datetime

try:
    import requests as _requests
except Exception:
    _requests = None

MONTH_ORDER = {
    "Jugust": 0, "Septober": 1, "Decembary": 2, "Aprimay": 3,
    "Jumay": 4, "Aug (summer?)": 5,
}


def _day_key(snap):
    day = str(snap.get("day", ""))
    m = re.search(r"(\d+)", day)
    num = int(m.group(1)) if m else 0
    # month name is the word after "of"
    mm = re.search(r"of\s+(\w+)", day)
    month = mm.group(1) if mm else ""
    # year
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
            with open(f) as fh:
                snapshots.append(json.load(fh))
        except (json.JSONDecodeError, OSError) as e:
            print(f"Skipping {f}: {e}")

    if not snapshots:
        print("No valid snapshots found")
        return None

    snapshots.sort(key=_day_key)

    run_name = run_name or f"run-{datetime.now().strftime('%Y%m%d-%H%M%S')}"

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
    with open(path, "w") as f:
        f.write("\n".join(lines))

    print(f"Debrief prompt written: {path}")

    # Optional LLM-backed analysis
    try:
        from config import LLM_API_KEY, LLM_PROVIDER, LLM_MODEL
    except Exception:
        LLM_API_KEY = None
    if LLM_API_KEY and _requests is not None:
        try:
            with open(path) as fh:
                prompt_text = fh.read()
            if LLM_PROVIDER == "anthropic":
                resp = _requests.post(
                    "https://api.anthropic.com/v1/messages",
                    headers={
                        "x-api-key": LLM_API_KEY,
                        "anthropic-version": "2023-06-01",
                        "content-type": "application/json",
                    },
                    json={
                        "model": LLM_MODEL,
                        "max_tokens": 1200,
                        "messages": [{"role": "user", "content": prompt_text}],
                    },
                    timeout=60,
                )
                resp.raise_for_status()
                data = resp.json()
                analysis = data.get("content", [{}])[0].get("text", "")
            else:
                resp = _requests.post(
                    "https://api.openai.com/v1/chat/completions",
                    headers={"Authorization": f"Bearer {LLM_API_KEY}", "Content-Type": "application/json"},
                    json={
                        "model": LLM_MODEL,
                        "messages": [{"role": "user", "content": prompt_text}],
                        "max_tokens": 1200,
                    },
                    timeout=60,
                )
                resp.raise_for_status()
                data = resp.json()
                analysis = data["choices"][0]["message"]["content"]
            analysis_path = os.path.join(debriefs_dir, f"{run_name}.analysis.md")
            with open(analysis_path, "w") as f:
                f.write("# LLM Analysis\n\n")
                f.write(analysis)
            print(f"LLM analysis written: {analysis_path}")
        except Exception as e:
            print(f"LLM analysis skipped: {e}")

    return path


if __name__ == "__main__":
    from config import SNAPSHOTS_DIR, DEBRIEFS_DIR

    run_name = sys.argv[1] if len(sys.argv) > 1 else None
    generate_debrief(SNAPSHOTS_DIR, DEBRIEFS_DIR, run_name)
