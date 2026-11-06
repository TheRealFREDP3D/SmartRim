"""One-command post-run pipeline.

    python -m smartrim.pipeline <run-id>

Steps (each idempotent, each skippable for testing):

1. Debrief  — regenerate the run's prose debrief (`runtime/<run>/debriefs/<run>.md`).
2. Bundle   — build the v3 LLM bundle (`<run>.bundle.md`).
3. LLM      — send the bundle to the configured debrief model; write the
              analysis (`<run>-llm.md`) and candidate lessons
              (`runtime/<run>/candidates/<run>-<timestamp>.jsonl`).
4. Promote  — rule-based auto-promotion of candidates (see `smartrim.promote`).
              Candidates that pass the rules become **needs_review** lessons —
              never auto-activated. Everything else is listed with its reason;
              nothing is silently dropped.
5. Render   — regenerate `memory/lessons-learned.md` when promotions happened.

The run must have snapshots. If `end.json` is missing (run abandoned before
the pipeline existed), a warning is printed but the pipeline still runs — the
data is real, just not a definitive evaluation datapoint.

The pipeline never edits game state and never activates a lesson. Flip
`needs_review` -> `active` with a human decision (`python -m smartrim.situation
promote` or by editing the JSONL) after reading the candidate.
"""

from __future__ import annotations

import argparse
import glob
import json
import os

from smartrim import config
from smartrim.advice_log import read_advice
from smartrim.debrief import generate_debrief
from smartrim.debrief_bundle import build_bundle
from smartrim.debrief_llm import analyze_debrief, write_analysis
from smartrim.llm import resolve_model
from smartrim.promote import (
    annotate_candidates_file,
    load_candidates,
    promote_rule_based,
)
from smartrim.situation import render_markdown

BUNDLE_SYSTEM = (
    "You are a RimWorld game analyst. You analyze colony debriefs and extract "
    "actionable lessons. Be specific, cite the days and events in the data, and "
    "never invent facts. Output exactly the sections the debrief asks for."
)


def _newest_candidates(candidates_dir, run_id):
    files = glob.glob(os.path.join(candidates_dir, f"{run_id}-*.jsonl"))
    files.sort(key=os.path.getmtime, reverse=True)
    return files[0] if files else None


def _warn_inconclusive(run_id):
    end_path = config.run_file("end.json", run_id)
    if end_path and os.path.isfile(end_path):
        try:
            with open(end_path, encoding="utf-8") as fh:
                marker = json.load(fh)
            reason = marker.get("stop_reason")
            if reason in ("manual_close", "monitor_abort"):
                print(f"warning: {run_id} ended early ({reason}); treating as inconclusive, "
                      f"not an evaluation datapoint.")
            return
        except (OSError, json.JSONDecodeError):
            pass
    print(f"warning: {run_id} has no end.json; treating as inconclusive, not an evaluation datapoint.")


def run_pipeline(run_id, *, use_llm=True, auto_promote=True, render=True,
                 dry_run=False, model=None, provider=None,
                 render_path=None, lessons_file=None):
    """Run the post-run pipeline. Returns a report dict."""
    snap_dir = config.snapshots_dir(run_id)
    if not snap_dir or not glob.glob(os.path.join(snap_dir, "day-*.json")):
        print(f"No snapshots for run {run_id}")
        return None
    _warn_inconclusive(run_id)

    debrief_dir = config.debriefs_dir(run_id, create=True)
    print(f"== pipeline: {run_id} ==")

    print("step 1/5  debrief")
    generate_debrief(snap_dir, debrief_dir, run_id)

    print("step 2/5  bundle")
    bundle_path, _response = build_bundle(snap_dir, debrief_dir, run_id,
                                          read_advice(run_id=run_id))
    print(f"bundle: {bundle_path}")

    print("step 3/5  llm analysis")
    cand_dir = config.candidates_dir(run_id, create=True)
    candidates_path = None
    if use_llm:
        with open(bundle_path, encoding="utf-8") as fh:
            bundle = fh.read()
        _provider, _model = resolve_model(task="debrief", model=model)
        _provider = provider or _provider
        analysis = analyze_debrief(bundle, model=_model, provider=_provider,
                                   system=BUNDLE_SYSTEM)
        if "schema_error" in analysis:
            print(f"warning: model failed schema validation after retries: {analysis['schema_error']}")
            print("no candidates written; fix the prompt or try another model, then re-run with --skip-llm")
            return {"run_id": run_id, "candidates_path": None, "promoted": [],
                    "skipped": [], "schema_error": analysis["schema_error"]}
        written = write_analysis(run_id, analysis, _model)
        print(f"analysis: {written}")
        candidates_path = _newest_candidates(cand_dir, run_id)
    else:
        candidates_path = _newest_candidates(cand_dir, run_id)
        if not candidates_path:
            print("error: --skip-llm given but no candidates file exists yet; run with LLM first")
            return {"run_id": run_id, "candidates_path": None, "promoted": [],
                    "skipped": [], "error": "no candidates"}
        print(f"using existing candidates: {candidates_path}")

    if not candidates_path:
        print("no candidates emitted (model proposed nothing or none validated)")
        return {"run_id": run_id, "candidates_path": None, "promoted": [], "skipped": []}

    if not auto_promote:
        print("step 4/5+5/5  skipped (--no-promote)")
        return {"run_id": run_id, "candidates_path": candidates_path,
                "promoted": [], "skipped": []}

    print("step 4/5  auto-promote (needs_review)")
    candidates = load_candidates(candidates_path)
    print(f"candidates: {len(candidates)}")
    from smartrim.promote import load_existing_lessons

    existing = load_existing_lessons(lessons_file)
    promoted, skipped, mapping = promote_rule_based(candidates, existing,
                                                    lessons_file=lessons_file,
                                                    dry_run=dry_run)
    for lesson in promoted:
        print(f"  PROMOTED {lesson['id']}  {lesson['title']}")
    for cid, reasons in skipped:
        print(f"  SKIPPED  {cid}  {'; '.join(reasons)}")
    if mapping and not dry_run:
        annotate_candidates_file(candidates_path, mapping)

    print("step 5/5  render")
    if not promoted:
        print("no promotions; lessons-learned.md left unchanged")
    elif dry_run:
        print("dry-run; lessons-learned.md not rewritten")
    elif not render:
        print("render skipped (--no-render)")
    else:
        target = render_path or os.path.join(config.BASE_DIR, "memory", "lessons-learned.md")
        with open(target, "w", encoding="utf-8") as fh:
            fh.write(render_markdown(lessons_file))
        print(f"rendered: {target}")

    return {"run_id": run_id, "candidates_path": candidates_path,
            "promoted": [lesson["id"] for lesson in promoted], "skipped": skipped}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("run_id")
    parser.add_argument("--skip-llm", action="store_true",
                        help="Reuse the newest existing candidates file instead of calling the model")
    parser.add_argument("--no-promote", action="store_true",
                        help="Stop after the LLM step (analysis + candidates, no promotion)")
    parser.add_argument("--no-render", action="store_true",
                        help="Do not regenerate lessons-learned.md")
    parser.add_argument("--dry-run", action="store_true",
                        help="Report what would be promoted; write nothing")
    parser.add_argument("--model", default=None, help="Override debrief model")
    parser.add_argument("--provider", default=None, help="Override debrief provider")
    args = parser.parse_args(argv)

    if "/" in args.run_id or "\\" in args.run_id or args.run_id.startswith("-"):
        print(f"Invalid run id: {args.run_id!r}")
        return 2

    report = run_pipeline(
        args.run_id,
        use_llm=not args.skip_llm,
        auto_promote=not args.no_promote,
        render=not args.no_render,
        dry_run=args.dry_run,
        model=args.model,
        provider=args.provider,
    )
    if report is None:
        return 1
    print(f"done: promoted={report['promoted']} skipped={len(report['skipped'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
