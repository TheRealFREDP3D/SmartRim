"""Auto-tag urgent advice with a best-effort cause from the game's own alerts.

The debrief bundle can show *what happened* (alerts, moods, stockpiles) but not
*why* (fire vs. raider arson vs. construction accident). Instead of asking the
human to tag every incident by hand — which never happened (0 of 56 records) —
we derive a stable, greppable cause slug from the alerts the monitor itself
saw at the time the advice was logged.

The slug is deliberately coarse. It is a floor, not a ceiling: a human can
always override it with ``python -m smartrim.advice_log cause <id> "<cause>"``
or ``cause-match`` for a whole burst, and overrides are never overwritten by
re-tagging.

Usage:

    python -m smartrim.event_cause backfill [--run RUN_ID | --all] [--dry-run]
"""

from __future__ import annotations

import argparse
import glob
import json
import os

from smartrim import advice_log, config

_RAID_KWS = ("raid", "attack", "enem", "hostile")
_PREDATOR_KWS = ("predator", "beast")
_FIRE_KWS = ("fire", "burn")


def _haystack(alerts):
    parts = []
    cats = []
    for alert in alerts or []:
        if not isinstance(alert, dict):
            parts.append(str(alert))
            continue
        parts.append(str(alert.get("message") or alert.get("label") or ""))
        cats.append(str(alert.get("category") or ""))
    return " ".join(parts).lower(), cats


def derive_event_cause(alerts=None, *, text=None, categories=None) -> str | None:
    """Derive a cause slug from alert dicts, or from raw text + category list.

    Accepts either the monitor's alert dicts (``category`` + ``message``), or a
    pre-joined situation text with the comma-joined category list stored on the
    advice record as ``reflex_name``. Returns None when there is nothing
    derivable (empty input).
    """
    msgs, cats = _haystack(alerts)
    if text is not None:
        msgs = f"{msgs} {text}".lower()
    if categories is not None:
        cats = list(cats) + [c for c in str(categories).split(",") if c]

    if not msgs.strip() and not cats:
        return None

    def has_kw(words):
        return any(kw in msgs for kw in words)

    fire = has_kw(_FIRE_KWS)
    raid = has_kw(_RAID_KWS) or any(c in ("hostile", "raid_incoming") for c in cats)
    predator = has_kw(_PREDATOR_KWS) or any(c.startswith("predator") for c in cats)

    if "colony_death" in cats:
        return "colony_death"
    if fire and raid:
        return "fire_during_raid"
    if fire:
        return "fire_unknown"
    if raid:
        return "hostile_raid"
    if predator:
        return "predator_attack"
    if any(c.startswith("mood_") for c in cats) or "break risk" in msgs:
        return "mood_break_risk"
    if "downed" in cats or "downed" in msgs:
        return "colonist_downed"
    if "food_low" in cats:
        return "food_exhaustion"
    if "medicine_low" in cats:
        return "medicine_shortage"
    if "medical_treatment_needed" in cats or "medical treatment" in msgs:
        return "medical_emergency"
    if "sleeping_during_threat" in cats:
        return "threat_response_failure"
    if "danger_rating" in cats:
        return "high_danger"
    if "idle_colonist" in cats:
        return "idle_colonists"
    return "unclassified"


def _backfill_file(path, *, dry_run=False):
    """Fill event_cause on reflex records that lack it. Returns (changed, total)."""
    try:
        with open(path, encoding="utf-8") as fh:
            lines = fh.readlines()
    except OSError:
        return 0, 0
    records = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        try:
            records.append(json.loads(line))
        except json.JSONDecodeError:
            continue

    changed = 0
    for rec in records:
        if rec.get("event_cause"):
            continue  # human tags are never overwritten
        if rec.get("trigger") != "reflex" and rec.get("severity") not in ("urgent", "critical"):
            continue
        cause = derive_event_cause(None, text=rec.get("situation") or "",
                                   categories=rec.get("reflex_name"))
        if not cause:
            continue
        rec["event_cause"] = cause
        rec["event_cause_source"] = "auto:alerts"
        changed += 1

    if changed and not dry_run:
        advice_log.save_atomic_at(path, records)
    return changed, len(records)


def backfill(run_id=None, *, all_runs=False, dry_run=False):
    """Backfill event_cause across one run or every run under runtime/."""
    targets = []
    if all_runs:
        for path in glob.glob(os.path.join(config.RUNTIME_DIR, "run-*", "advice.jsonl")):
            targets.append(path)
    elif run_id:
        p = config.advice_file(run_id)
        if p:
            targets.append(p)
    else:
        p = config.advice_file()
        if p:
            targets.append(p)
    total_changed = 0
    for path in targets:
        changed, total = _backfill_file(path, dry_run=dry_run)
        run = os.path.basename(os.path.dirname(path))
        print(f"{run}: tagged {changed} of {total} record(s)"
              + (" (dry-run)" if dry_run else ""))
        total_changed += changed
    print(f"total: {total_changed} record(s) tagged")
    return total_changed


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("backfill", help="Fill event_cause on urgent advice from alert text")
    p.add_argument("--run", dest="run_id", default=None, help="One run id (default: active/sentinel resolution)")
    p.add_argument("--all", action="store_true", help="Every run under runtime/")
    p.add_argument("--dry-run", action="store_true", help="Report without writing")
    args = parser.parse_args(argv)
    if args.cmd == "backfill":
        backfill(args.run_id, all_runs=args.all, dry_run=args.dry_run)
        return 0
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
