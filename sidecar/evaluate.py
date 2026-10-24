"""Evaluation harness for Phase 2.

Reads run-end markers, the advice log, and that run's snapshots. Prints one
summary row per run. Comparison is descriptive only (medians and ranges).
With n=3 per arm this is a first signal, not a significance test.

Usage:
    evaluate.py summarize [--runs-dir memory/runs] [--write memory/eval-YYYY-MM-DD.md]
    evaluate.py compare  --runs <id> <id> ... [--write memory/eval-YYYY-MM-DD.md]
"""

import argparse
import glob
import json
import os
import statistics
from datetime import date

try:
    from config import BASE_DIR
except Exception:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SUMMARY_KEYS = [
    "run_id",
    "arm",
    "days_survived",
    "colonists_alive_day10",
    "lowest_mood",
    "downed_events",
    "break_events",
    "first_low_food_day",
    "first_medicine_day",
    "urgent_alerts",
    "auto_pauses",
    "advice_helped",
    "advice_failed",
    "advice_ignored",
]

# Game-alert phrases. "medical treatment" is an injury alert, not a shortage.
_FOOD_PHRASES = ("low food", "food stock low", "need food", "starvation", "starving")
_MED_PHRASES = ("medicine stock low", "need medicine", "no medicine", "medicine low", "medicine shortage")
_BREAK_PHRASES = ("mental break", "berserk", "catatonic", "sad wander", "murderous rage", "gave up")


def _load_json(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def _load_end_marker(runs_dir, run_id):
    path = os.path.join(runs_dir, f"{run_id}.end.json")
    if not os.path.exists(path):
        return None
    return _load_json(path)


def _load_advice(advice_file, run_id):
    if not advice_file or not os.path.exists(advice_file):
        return []
    out = []
    with open(advice_file, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                rec = json.loads(line)
            except json.JSONDecodeError:
                continue
            if rec.get("run_id") == run_id:
                out.append(rec)
    return out


def resolve_snapshots_dir(run_id, marker=None, snapshots_root=None):
    """Prefer the directory recorded on the end marker, then the per-run folder."""
    if marker and marker.get("snapshots_dir") and os.path.isdir(marker["snapshots_dir"]):
        return marker["snapshots_dir"]
    root = snapshots_root or os.path.join(BASE_DIR, "memory", "snapshots")
    nested = os.path.join(root, str(run_id)) if run_id else root
    if os.path.isdir(nested) and glob.glob(os.path.join(nested, "day-*.json")):
        return nested
    final = (marker or {}).get("final_snapshot")
    if final:
        parent = os.path.dirname(final)
        if os.path.isdir(parent):
            return parent
    return nested


def _snapshot_sort_key(path):
    try:
        data = _load_json(path)
    except Exception:
        return (9999, path)
    status = data.get("status") or {}
    dp = status.get("daysPassed")
    if dp is not None:
        try:
            return (int(dp), path)
        except Exception:
            pass
    summary = data.get("summary") or {}
    day_label = summary.get("day") or data.get("day") or ""
    m = __import__("re").search(r"(\d+)", str(day_label))
    if m:
        try:
            return (int(m.group(1)), path)
        except Exception:
            pass
    return (9999, path)


def _load_snapshots(snapshots_dir):
    if not snapshots_dir or not os.path.isdir(snapshots_dir):
        return []
    snaps = []
    paths = glob.glob(os.path.join(snapshots_dir, "day-*.json"))
    for path in sorted(paths, key=_snapshot_sort_key):
        try:
            snaps.append(_load_json(path))
        except (json.JSONDecodeError, OSError):
            continue
    return snaps


def _summary(snap):
    summary = snap.get("summary")
    return summary if isinstance(summary, dict) else {}


def _days_passed(snap):
    status = snap.get("status")
    if isinstance(status, dict) and status.get("daysPassed") is not None:
        return status.get("daysPassed")
    return None


def _day_label(snap):
    summary = _summary(snap)
    return summary.get("day") or snap.get("day")


def _is_day10(snap):
    """Day 10 of the protocol window: daysPassed == 10, or a '10th' date label.

    daysPassed starts at 0 on Day 1, so 10 means ten days have elapsed and the
    Day-10 state is on disk. The end marker (daysPassed 11) is the window close,
    used only as a fallback.
    """
    passed = _days_passed(snap)
    if passed == 10:
        return True
    label = str(_day_label(snap) or "")
    return label.startswith(("10th", "10 "))


def _colonists_alive(snap):
    summary = _summary(snap)
    if summary.get("colonist_count") is not None:
        return summary.get("colonist_count")
    status = snap.get("status")
    if isinstance(status, dict):
        return status.get("colonistCount")
    return None


def _alert_texts(snap):
    texts = []
    summary = _summary(snap)
    for item in summary.get("alerts") or []:
        texts.append(str(item))
    alerts = snap.get("alerts")
    if isinstance(alerts, dict):
        for item in alerts.get("activeAlerts") or []:
            if isinstance(item, dict):
                texts.append(str(item.get("label") or ""))
            else:
                texts.append(str(item))
    elif isinstance(alerts, list):
        for item in alerts:
            if isinstance(item, dict):
                texts.append(str(item.get("label") or item.get("message") or ""))
    return texts


def _first_day(snaps, predicate):
    for snap in snaps:
        if any(predicate(text.lower()) for text in _alert_texts(snap)):
            return _day_label(snap)
    return None


def _is_food(text):
    return any(phrase in text for phrase in _FOOD_PHRASES)


def _is_medicine(text):
    return any(phrase in text for phrase in _MED_PHRASES)


def _is_break(text):
    return any(phrase in text for phrase in _BREAK_PHRASES)


def _arm(marker):
    if marker:
        arm = marker.get("arm")
        if arm in ("on", "off"):
            return arm
        if marker.get("observe_only") is True:
            return "off"
        if marker.get("observe_only") is False:
            return "on"
    return "unknown"


def summarize_run(run_id, runs_dir, advice_file, snapshots_root=None):
    marker = _load_end_marker(runs_dir, run_id)
    advice = _load_advice(advice_file, run_id)
    snaps = _load_snapshots(resolve_snapshots_dir(run_id, marker, snapshots_root))

    days_survived = marker.get("days_passed") if marker else None
    day10 = next((snap for snap in snaps if _is_day10(snap)), None)
    end_snap = None
    if marker and marker.get("final_snapshot") and os.path.exists(marker["final_snapshot"]):
        try:
            end_snap = _load_json(marker["final_snapshot"])
        except (json.JSONDecodeError, OSError):
            end_snap = None
    if end_snap is None and snaps:
        end_snap = snaps[-1]
    colonists = _colonists_alive(day10) if day10 is not None else _colonists_alive(end_snap or {})

    lowest_mood = None
    downed_names = set()
    break_events = 0
    for snap in snaps:
        summary = _summary(snap)
        mood = summary.get("min_mood")
        if mood is not None and (lowest_mood is None or mood < lowest_mood):
            lowest_mood = mood
        for name in summary.get("downed") or []:
            if name:
                downed_names.add(name)
        if any(_is_break(text.lower()) for text in _alert_texts(snap)):
            break_events += 1

    helped = sum(1 for rec in advice if rec.get("status") == "helped")
    failed = sum(1 for rec in advice if rec.get("status") == "failed")
    ignored = sum(1 for rec in advice if rec.get("status") in ("open", "dismissed", "expired"))
    auto_pauses = marker.get("auto_pauses") if marker and marker.get("auto_pauses") is not None else sum(
        1 for rec in advice if rec.get("auto_paused")
    )
    urgent = marker.get("urgent_alerts") if marker and marker.get("urgent_alerts") is not None else sum(
        1 for rec in advice if rec.get("severity") == "urgent"
    )

    return {
        "run_id": run_id,
        "arm": _arm(marker),
        "days_survived": days_survived,
        "colonists_alive_day10": colonists,
        "lowest_mood": lowest_mood,
        "downed_events": len(downed_names),
        "break_events": break_events,
        "first_low_food_day": _first_day(snaps, _is_food),
        "first_medicine_day": _first_day(snaps, _is_medicine),
        "urgent_alerts": urgent,
        "auto_pauses": auto_pauses,
        "advice_helped": helped,
        "advice_failed": failed,
        "advice_ignored": ignored,
        "advice_total": len(advice),
        "has_end_marker": marker is not None,
        "stop_reason": marker.get("stop_reason") if marker else None,
    }


def _numbers(rows, key):
    return [row[key] for row in rows if isinstance(row.get(key), (int, float))]


def _median_range(values):
    if not values:
        return None
    mid = statistics.median(values)
    if isinstance(mid, float) and mid.is_integer():
        mid = int(mid)
    return {"median": mid, "min": min(values), "max": max(values), "n": len(values)}


def arm_summary(rows):
    """Descriptive medians and ranges. No significance test."""
    out = {}
    for arm in ("on", "off"):
        group = [row for row in rows if row.get("arm") == arm]
        out[arm] = {
            "n": len(group),
            "days_survived": _median_range(_numbers(group, "days_survived")),
            "colonists_alive_day10": _median_range(_numbers(group, "colonists_alive_day10")),
            "lowest_mood": _median_range(_numbers(group, "lowest_mood")),
            "urgent_alerts": _median_range(_numbers(group, "urgent_alerts")),
            "auto_pauses": _median_range(_numbers(group, "auto_pauses")),
            "advice_helped": _median_range(_numbers(group, "advice_helped")),
            "advice_failed": _median_range(_numbers(group, "advice_failed")),
            "advice_ignored": _median_range(_numbers(group, "advice_ignored")),
        }
    return out


def format_table(rows):
    if not rows:
        return "No runs."
    keys = SUMMARY_KEYS
    widths = {key: max(len(key), max(len(_cell(row.get(key))) for row in rows)) for key in keys}
    header = " | ".join(key.ljust(widths[key]) for key in keys)
    lines = [header, "-" * len(header)]
    for row in rows:
        lines.append(" | ".join(_cell(row.get(key)).ljust(widths[key]) for key in keys))
    return "\n".join(lines)


def _cell(value):
    return "-" if value is None else str(value)


def _fmt_range(stat):
    if not stat:
        return "-"
    return f"{stat['median']} ({stat['min']}-{stat['max']}, n={stat['n']})"


def format_arm_summary(summary):
    lines = [
        "Arm comparison (median, min-max). Descriptive only; no significance test.",
    ]
    for arm in ("on", "off"):
        block = summary.get(arm) or {}
        n = block.get("n", 0)
        note = "" if n >= 3 else "  ** fewer than 3 runs — not enough for the planned comparison **"
        lines.append(f"arm={arm} n={n}{note}")
        if n == 0:
            continue
        lines.append(f"  days_survived: {_fmt_range(block.get('days_survived'))}")
        lines.append(f"  colonists_alive_day10: {_fmt_range(block.get('colonists_alive_day10'))}")
        lines.append(f"  lowest_mood: {_fmt_range(block.get('lowest_mood'))}")
        lines.append(f"  urgent_alerts: {_fmt_range(block.get('urgent_alerts'))}")
        lines.append(f"  auto_pauses: {_fmt_range(block.get('auto_pauses'))}")
        lines.append(f"  advice helped/failed/ignored: "
                     f"{_fmt_range(block.get('advice_helped'))} / "
                     f"{_fmt_range(block.get('advice_failed'))} / "
                     f"{_fmt_range(block.get('advice_ignored'))}")
    return "\n".join(lines)


def render_report(rows):
    summary = arm_summary(rows)
    unknown = [row["run_id"] for row in rows if row.get("arm") not in ("on", "off")]
    lines = [
        f"# Evaluation {date.today().isoformat()}",
        "",
        ("Protocol: Crashlanded, Cassandra Classic, Adventure story, flat temperate forest, "
         "no reload. Adviser-on pauses and logs advice. Adviser-off observes only."),
        ("Both arms pause once at the protocol stop (run length or colony death). "
         "That stop is not counted as an adviser auto-pause."),
        "",
        "This report is descriptive. Medians and ranges only. No significance claim.",
        "",
        "## Runs",
        "",
        format_table(rows),
        "",
        "## Arms",
        "",
        format_arm_summary(summary),
        "",
    ]
    if unknown:
        lines.append(f"Runs with no arm recorded (excluded from the arm summary): {', '.join(unknown)}")
        lines.append("")
    ready = all((summary[arm]["n"] >= 3) for arm in ("on", "off"))
    lines.append("Exit: both arms have at least 3 runs." if ready else
                 "Exit not met: both arms need at least 3 runs before this comparison means anything.")
    lines.append("")
    return "\n".join(lines)


def _print_rows(rows):
    print(format_table(rows))
    print()
    print(format_arm_summary(arm_summary(rows)))


def _maybe_write(rows, path):
    if not path:
        return
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    text = render_report(rows)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)
    print(f"\nWrote {path}")


def _rows_from_dir(runs_dir, advice_file, snapshots_root):
    if not os.path.isdir(runs_dir):
        return None
    run_ids = sorted(
        name[:-len(".end.json")] for name in os.listdir(runs_dir) if name.endswith(".end.json")
    )
    return [summarize_run(run_id, runs_dir, advice_file, snapshots_root) for run_id in run_ids]


def cmd_summarize(args):
    rows = _rows_from_dir(args.runs_dir, args.advice, args.snapshots_dir)
    if rows is None:
        print(f"Runs dir not found: {args.runs_dir}")
        return
    if not rows:
        print("No completed runs found.")
        return
    _print_rows(rows)
    _maybe_write(rows, args.write)


def cmd_compare(args):
    rows = [summarize_run(run_id, args.runs_dir, args.advice, args.snapshots_dir) for run_id in args.runs]
    _print_rows(rows)
    _maybe_write(rows, args.write)


def main():
    parser = argparse.ArgumentParser(description="Phase 2 evaluation harness")
    sub = parser.add_subparsers(dest="cmd", required=True)

    default_runs = os.path.join(BASE_DIR, "memory", "runs")
    default_advice = os.path.join(BASE_DIR, "memory", "advice", "advice.jsonl")
    default_snaps = os.path.join(BASE_DIR, "memory", "snapshots")

    summarize = sub.add_parser("summarize")
    summarize.add_argument("--runs-dir", default=default_runs)
    summarize.add_argument("--advice", default=default_advice)
    summarize.add_argument("--snapshots-dir", default=default_snaps)
    summarize.add_argument("--write", default=None, help="Write the markdown report to this path")
    summarize.set_defaults(func=cmd_summarize)

    compare = sub.add_parser("compare")
    compare.add_argument("--runs", nargs="+", required=True)
    compare.add_argument("--runs-dir", default=default_runs)
    compare.add_argument("--advice", default=default_advice)
    compare.add_argument("--snapshots-dir", default=default_snaps)
    compare.add_argument("--write", default=None, help="Write the markdown report to this path")
    compare.set_defaults(func=cmd_compare)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
