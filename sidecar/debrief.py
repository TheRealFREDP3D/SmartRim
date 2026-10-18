import os
import sys
import json
import glob
from datetime import datetime


def generate_debrief(snapshots_dir, debriefs_dir, run_name=None):
    pattern = os.path.join(snapshots_dir, "day-*.json")
    files = sorted(glob.glob(pattern))

    if not files:
        print("No snapshots found")
        return None

    snapshots = []
    for f in files:
        with open(f) as fh:
            snapshots.append(json.load(fh))

    run_name = run_name or f"run-{datetime.now().strftime('%Y%m%d-%H%M%S')}"

    prompt = f"""# Debrief: {run_name}

## Colony Timeline
"""
    for snap in snapshots:
        day = snap.get("day", "?")
        colonists = snap.get("colonists", {}).get("colonists", [])
        alerts = snap.get("alerts", {})

        prompt += f"\n### Day {day}\n"
        prompt += f"- Colonists: {len(colonists)}\n"
        for c in colonists:
            prompt += f"  - {c.get('name', 'Unknown')}: HP {c.get('health', '?')}%, Mood {c.get('mood', '?')}%\n"

        active_alerts = alerts.get("activeAlerts", [])
        if active_alerts:
            prompt += f"- Alerts: {', '.join(a.get('label', '') for a in active_alerts)}\n"

    prompt += """
## Analysis Request

Based on the timeline above:
1. What was the primary cause of colony failure?
2. What worked well?
3. What lessons should be added to lessons-learned.md?
4. What should the next colony do differently?
"""

    os.makedirs(debriefs_dir, exist_ok=True)
    path = os.path.join(debriefs_dir, f"{run_name}.md")
    with open(path, "w") as f:
        f.write(prompt)

    print(f"Debrief prompt written: {path}")
    return path


if __name__ == "__main__":
    from config import SNAPSHOTS_DIR, DEBRIEFS_DIR

    run_name = sys.argv[1] if len(sys.argv) > 1 else None
    generate_debrief(SNAPSHOTS_DIR, DEBRIEFS_DIR, run_name)
