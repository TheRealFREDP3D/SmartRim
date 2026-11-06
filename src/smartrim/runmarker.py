"""Run-end markers: the single owner of ``runtime/<run-id>/end.json``.

Three ways a run can end in code:

- monitor detects ``daysPassed >= RUN_DAYS`` -> ``stop_reason="run_length"`` (definitive)
- monitor loses the whole colony            -> ``stop_reason="colony_death"`` (definitive)
- anything else (game closed, save
  abandoned, monitor stopped, power loss)   -> ``stop_reason="manual_close"`` or
                                               ``"monitor_abort"`` (**inconclusive**)

Inconclusive markers are legitimate history, not valid comparison datapoints:
the run happened and its artifacts are real, but it must not be scored against
protocol-conformant runs. ``evaluate`` skips inconclusive markers by default
(``--include-inconclusive`` opts back in).

Definitive markers written by the monitor (``monitor.write_run_end``) keep
working unchanged. This module mirrors their field shape and derives what it
can from the run's own snapshots and advice log.
"""

from __future__ import annotations

import argparse
import contextlib
import glob
import json
import os
import re
from datetime import datetime

from smartrim import config

STOP_REASONS = ("run_length", "colony_death", "manual_close", "monitor_abort")
DEFINITIVE_STOP_REASONS = frozenset({"run_length", "colony_death"})
INCONCLUSIVE_STOP_REASONS = frozenset({"manual_close", "monitor_abort"})


def is_inconclusive(marker) -> bool:
    """True when a marker (or the absence of one) is not a valid datapoint."""
    if not isinstance(marker, dict):
        return True
    if marker.get("inconclusive") is True:
        return True
    reason = str(marker.get("stop_reason") or "").strip()
    if not reason:
        return True
    if reason in INCONCLUSIVE_STOP_REASONS:
        return True
    # Unknown/garbage stop reasons fail safe: never silently treated as valid.
    return reason not in DEFINITIVE_STOP_REASONS


def validate_marker(marker) -> list[str]:
    """Structural checks for a run-end marker; returns a list of errors."""
    errors: list[str] = []
    if not isinstance(marker, dict):
        return ["marker is not an object"]
    if not marker.get("run_id"):
        errors.append("missing run_id")
    reason = str(marker.get("stop_reason") or "").strip()
    if reason not in STOP_REASONS:
        errors.append(f"stop_reason not one of {STOP_REASONS}: {reason!r}")
    dp = marker.get("days_passed")
    if dp is not None:
        try:
            if int(dp) < 0:
                errors.append(f"days_passed negative: {dp}")
        except (TypeError, ValueError):
            errors.append(f"days_passed not an integer: {dp!r}")
    created_by = marker.get("created_by")
    if created_by is not None and not isinstance(created_by, str):
        errors.append("created_by must be a string")
    return errors


def _load_json(path):
    try:
        with open(path, encoding="utf-8") as fh:
            return json.load(fh)
    except (OSError, json.JSONDecodeError):
        return None


def _snapshot_day_key(path):
    data = _load_json(path) or {}
    status = data.get("status") if isinstance(data.get("status"), dict) else {}
    dp = status.get("daysPassed")
    if dp is None:
        summary = data.get("summary") if isinstance(data.get("summary"), dict) else {}
        dp = summary.get("days_passed")
    try:
        return int(dp)
    except (TypeError, ValueError):
        m = re.search(r"(\d+)", os.path.basename(path))
        return int(m.group(1)) if m else -1


def _latest_day_snapshot(snapshots_dir):
    files = glob.glob(os.path.join(snapshots_dir, "day-*.json"))
    if not files:
        return None, None
    files.sort(key=_snapshot_day_key)
    latest = files[-1]
    dp = _snapshot_day_key(latest)
    return _load_json(latest), (dp if dp >= 0 else None), latest


def _count_jsonl_matching(path, predicate):
    n = 0
    try:
        with open(path, encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if not line:
                    continue
                rec = _load_json_line(line)
                if rec and predicate(rec):
                    n += 1
    except OSError:
        return 0
    return n


def _load_json_line(line):
    try:
        data = json.loads(line)
        return data if isinstance(data, dict) else None
    except json.JSONDecodeError:
        return None


def derive_end_state(run_dir) -> dict:
    """Derive days/mood/colonists/counters from a run's own artifacts."""
    out: dict = {
        "days_passed": None,
        "difficulty": None,
        "storyteller": None,
        "final_snapshot": None,
        "reflex_snapshots": 0,
        "urgent_alerts": 0,
        "auto_pauses": 0,
    }
    snaps_dir = os.path.join(run_dir, "snapshots")
    if os.path.isdir(snaps_dir):
        latest, dp, latest_path = _latest_day_snapshot(snaps_dir)
        out["days_passed"] = dp
        if isinstance(latest, dict):
            status = latest.get("status") if isinstance(latest.get("status"), dict) else {}
            out["difficulty"] = status.get("difficulty")
            out["storyteller"] = status.get("storyteller")
        # Point at the real last daily snapshot; evaluators read it read-only.
        if latest_path:
            out["final_snapshot"] = os.path.abspath(latest_path)
        with contextlib.suppress(OSError):
            out["reflex_snapshots"] = len(glob.glob(os.path.join(snaps_dir, "reflex-*.json")))

    advice_file = os.path.join(run_dir, "advice.jsonl")
    if os.path.isfile(advice_file):
        out["urgent_alerts"] = _count_jsonl_matching(advice_file, lambda r: r.get("severity") == "urgent")
        out["auto_pauses"] = _count_jsonl_matching(advice_file, lambda r: r.get("auto_paused") is True)
    return out


def _run_meta(run_dir) -> dict:
    meta = _load_json(os.path.join(run_dir, "meta.json"))
    return meta if isinstance(meta, dict) else {}


def has_run_data(run_dir) -> bool:
    """A directory counts as a run only if it produced real artifacts."""
    if not os.path.isdir(run_dir):
        return False
    snaps = os.path.join(run_dir, "snapshots")
    if glob.glob(os.path.join(snaps, "day-*.json")) or glob.glob(os.path.join(snaps, "reflex-*.json")):
        return True
    for name in ("advice.jsonl", "actions.jsonl", "end.json"):
        if os.path.isfile(os.path.join(run_dir, name)):
            return True
    return False


def find_unfinished_runs(exclude=None) -> list[str]:
    """Run ids with artifacts but no end.json, newest allocation last."""
    exclude = str(exclude) if exclude else None
    try:
        names = os.listdir(config.RUNTIME_DIR)
    except OSError:
        return []
    out = []
    for name in names:
        if not re.match(r"^run-\d+", name):
            continue
        if name == exclude:
            continue
        run_dir = os.path.join(config.RUNTIME_DIR, name)
        if os.path.isfile(os.path.join(run_dir, "end.json")):
            continue
        if has_run_data(run_dir):
            out.append(name)
    return sorted(out)


def close_run(run_id, *, stop_reason, note=None, overwrite=False) -> str:
    """Write an inconclusive end.json for a run that ended outside the monitor.

    Returns the marker path. Raises FileNotFoundError for unknown runs and
    FileExistsError when the run already has a marker (unless overwrite=True).
    Never captures a live snapshot: the game may be closed, or may hold a
    *different* colony than the one being closed.
    """
    if stop_reason not in INCONCLUSIVE_STOP_REASONS:
        raise ValueError(
            f"close_run is for inconclusive closes only; got {stop_reason!r}. "
            f"Definitive endings ({sorted(DEFINITIVE_STOP_REASONS)}) are written by the monitor."
        )
    run_dir = config.run_dir(run_id)
    if not has_run_data(run_dir):
        raise FileNotFoundError(f"no run artifacts found for {run_id!r} at {run_dir}")
    marker_path = os.path.join(run_dir, "end.json")
    if os.path.isfile(marker_path) and not overwrite:
        raise FileExistsError(f"{run_id!r} already has an end.json; use --force to overwrite")

    derived = derive_end_state(run_dir)
    meta = _run_meta(run_dir)
    marker = {
        "run_id": run_id,
        "arm": meta.get("arm"),
        "observe_only": meta.get("observe_only"),
        "stop_reason": stop_reason,
        "stop_reason_detail": note,
        "inconclusive": True,
        "created_by": "smartrim.runmarker",
        "days_passed": derived["days_passed"],
        "difficulty": derived["difficulty"],
        "storyteller": derived["storyteller"],
        "urgent_alerts": derived["urgent_alerts"],
        "auto_pauses": derived["auto_pauses"],
        "reflex_snapshots": derived["reflex_snapshots"],
        "ended_at": datetime.now().isoformat(),
        "snapshots_dir": os.path.abspath(os.path.join(run_dir, "snapshots")),
        "final_snapshot": derived["final_snapshot"],
    }
    from smartrim import protocol

    marker = protocol.stamp(marker,
                            storyteller=derived["storyteller"],
                            difficulty=derived["difficulty"],
                            run_days=config.RUN_DAYS)
    errors = validate_marker(marker)
    if errors:  # defensive: never write a marker the evaluator cannot parse
        raise ValueError(f"refusing to write invalid marker for {run_id!r}: {errors}")
    with open(marker_path, "w", encoding="utf-8") as fh:
        json.dump(marker, fh, indent=2)
    return marker_path


def close_abandoned_runs(exclude=None, *, stop_reason="monitor_abort", note=None,
                         log=None) -> list[str]:
    """Sweep every unfinished run (except ``exclude``) into an inconclusive marker."""
    closed = []
    for run_id in find_unfinished_runs(exclude=exclude):
        try:
            close_run(
                run_id,
                stop_reason=stop_reason,
                note=note or "auto-closed at next monitor start; never reached a definitive ending",
            )
        except (OSError, ValueError) as exc:
            if log:
                log(f"could not auto-close {run_id}: {exc}")
            continue
        closed.append(run_id)
        if log:
            log(f"auto-closed abandoned run {run_id} (stop_reason={stop_reason}, inconclusive)")
    return closed


def _print_marker_status(run_id):
    path = os.path.join(config.run_dir(run_id), "end.json")
    marker = _load_json(path)
    if marker is None:
        print(f"{run_id}: no end.json (unfinished)")
        return 1
    flag = "inconclusive" if is_inconclusive(marker) else "definitive"
    print(f"{run_id}: {marker.get('stop_reason')} ({flag}), days_passed={marker.get('days_passed')}, "
          f"created_by={marker.get('created_by', 'monitor')}")
    return 0


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_list = sub.add_parser("list", help="List runs with artifacts but no end.json")
    p_list.add_argument("--all", action="store_true", help="Include runs that already have a marker")

    p_close = sub.add_parser("close", help="Close an abandoned run (inconclusive marker)")
    p_close.add_argument("run_id")
    p_close.add_argument("--reason", default="manual_close",
                         choices=sorted(INCONCLUSIVE_STOP_REASONS))
    p_close.add_argument("--note", default=None, help="Free-text provenance note for the marker")
    p_close.add_argument("--force", action="store_true", help="Overwrite an existing end.json")

    p_status = sub.add_parser("status", help="Show a run's end.json status")
    p_status.add_argument("run_id")

    p_sweep = sub.add_parser("sweep", help="Close every unfinished run (like the monitor does at startup)")
    p_sweep.add_argument("--reason", default="monitor_abort",
                         choices=sorted(INCONCLUSIVE_STOP_REASONS))
    p_sweep.add_argument("--note", default=None)

    args = parser.parse_args(argv)
    if args.cmd == "list":
        unfinished = find_unfinished_runs()
        if not unfinished:
            print("No unfinished runs.")
            return 0
        for rid in unfinished:
            print(rid)
        return 0
    if args.cmd == "close":
        path = close_run(args.run_id, stop_reason=args.reason, note=args.note,
                         overwrite=args.force)
        print(f"closed {args.run_id}: {path}")
        return 0
    if args.cmd == "status":
        return _print_marker_status(args.run_id)
    if args.cmd == "sweep":
        closed = close_abandoned_runs(stop_reason=args.reason, note=args.note,
                                      log=print)
        print(f"closed {len(closed)} run(s)")
        return 0
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
