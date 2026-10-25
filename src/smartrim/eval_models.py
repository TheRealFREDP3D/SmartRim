"""Evaluate models on the same debrief bundle (A/B style), and score them with the rubric.

Writes response files to:
  memory/debriefs/<run>.<provider>.<model>.response.md

Then prints a comparison table with criterion scores.

Usage:
  python -m smartrim.eval_models --run run-006-obs-cassandra \
    --models ollama:gemma4-e2b-rimworld ollama:qwen3-rimworld
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from dataclasses import dataclass
from typing import Any

from smartrim.config import DEBRIEFS_DIR
from smartrim.debrief_llm import BUNDLE_SYSTEM, analyze_debrief, find_bundle

FENCE_RE = re.compile(r"```json\s*(.*?)```", re.DOTALL | re.IGNORECASE)


def _repo_root() -> str:
    # src/smartrim/eval_models.py -> src/smartrim -> src -> repo root
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))


def _load_rubric_labels() -> dict[int, str]:
    """Extract rubric criterion labels from memory/debrief-rubric.md."""
    rubric_path = os.path.join(_repo_root(), "memory", "debrief-rubric.md")
    try:
        with open(rubric_path, encoding="utf-8") as f:
            text = f.read()
    except OSError:
        return {}

    labels: dict[int, str] = {}
    # Example row: | 1 | Format | Not the two sections ... |
    for m in re.finditer(r"\|\s*(\d+)\s*\|\s*([^|]+?)\s*\|", text):
        idx = int(m.group(1))
        name = m.group(2).strip()
        if name and name.lower() not in {"criterion"}:
            labels[idx] = name
    return labels

REQUIRED_LESSON_KEYS = {
    "title",
    "cause_chain",
    "trigger",
    "recommendation",
    "rationale",
    "source",
    "wiki_pages_used",
    "unverified_claims",
    "confidence",
}

ACTION_VERBS = {
    "build",
    "research",
    "plant",
    "assign",
    "enclose",
    "replace",
    "stockpile",
    "draft",
    "tend",
    "grow",
    "freeze",
    "set up",
    "prepare",
    "repair",
    "buy",
}

DAY_EVIDENCE_RE = re.compile(r"day\s*\d+|\d+(?:th|st|nd|rd)\s+of\s+\w+\b", re.IGNORECASE)
WIKI_EVIDENCE_RE = re.compile(r"^wiki:")

UNKNOWN_TOKEN_RE = re.compile(r"days\s+\d+-\d+|day\s+\d+-\d+", re.IGNORECASE)


@dataclass
class ScoreRow:
    provider: str
    model: str
    total: int
    criteria: list[int]
    weakest: str


def _safe_load_json(s: str) -> Any:
    return json.loads(s)


def _extract_fenced_json(raw: str) -> Any:
    m = FENCE_RE.search(raw or "")
    if not m:
        raise json.JSONDecodeError("no fenced ```json block found", raw, 0)
    return _safe_load_json(m.group(1))


def _criterion_name(i: int) -> str:
    return str(i)


def score_debrief_answer(bundle_text: str, raw_answer: str) -> tuple[list[int], int]:
    """Heuristic rubric scorer.

    Returns (criteria[1..10], total[0..20]).
    """
    # Parse JSON candidates.
    raw_answer = raw_answer or ""
    has_section_a = "Section A" in raw_answer
    has_section_b = "Section B" in raw_answer
    criteria = [0] * 11  # 1-indexed

    parsed = None
    json_ok = False
    lesson_list: list[dict[str, Any]] = []
    try:
        parsed = _extract_fenced_json(raw_answer)
        if isinstance(parsed, list):
            lesson_list = parsed
            json_ok = True
        elif isinstance(parsed, dict) and isinstance(parsed.get("candidate_lessons"), list):
            lesson_list = parsed["candidate_lessons"]
            json_ok = True
    except Exception:
        parsed = None
        lesson_list = []
        json_ok = False

    # Criterion 1: Format
    # Rubric expects both sections present; if either is missing, score 0.
    if has_section_a and has_section_b and json_ok:
        # Validate candidate objects minimally.
        ok = True
        for item in lesson_list:
            if not isinstance(item, dict):
                ok = False
                break
            if set(item.keys()) != REQUIRED_LESSON_KEYS:
                ok = False
                break

        # Section B max 10 bullets (simple heuristic).
        section_b_text = raw_answer.split("Section B", 1)[1] if "Section B" in raw_answer else ""
        bullet_lines = [ln for ln in section_b_text.splitlines() if ln.strip().startswith("-")]
        section_b_ok = len(bullet_lines) <= 10

        criteria[1] = 2 if ok and section_b_ok else 1
    elif (has_section_a and (not has_section_b)) or ((not has_section_a) and has_section_b):
        criteria[1] = 0
    else:
        criteria[1] = 0

    # If we can't parse lessons, score the rest as best-effort.
    if not json_ok:
        return criteria, sum(criteria)
    # Criterion 6 needs trigger structure.
    trigger_ok = []
    evidence_counts = []
    for lesson in lesson_list:
        trig = lesson.get("trigger") if isinstance(lesson, dict) else None
        trig_ok = isinstance(trig, dict) and all(k in trig for k in ("phases", "threats", "resources"))
        trigger_ok.append(trig_ok)
        src = lesson.get("source")
        if isinstance(src, list):
            evidence = [s for s in src if isinstance(s, str) and (DAY_EVIDENCE_RE.search(s) or WIKI_EVIDENCE_RE.search(s))]
            evidence_counts.append(len(evidence))
        else:
            evidence_counts.append(0)

    # Criterion 2: Grounding in the timeline
    if lesson_list:
        grounded = sum(1 for c in evidence_counts if c >= 1)
        if grounded == len(lesson_list):
            criteria[2] = 2
        elif grounded > 0:
            criteria[2] = 1

    # Criterion 6: Scope fields
    if lesson_list:
        if all(trigger_ok):
            criteria[6] = 2
        elif any(trigger_ok):
            criteria[6] = 1

    # Criterion 4: Handling unverified claims
    unverified_flags = []
    for lesson in lesson_list:
        uc = lesson.get("unverified_claims")
        unverified_flags.append(isinstance(uc, list) and len(uc) > 0)

    if any(unverified_flags):
        criteria[4] = 2
    else:
        # If model asserts known unverified token patterns, penalize.
        if UNKNOWN_TOKEN_RE.search(raw_answer):
            criteria[4] = 0
        elif any("unverified" in str(lesson) for lesson in lesson_list):
            criteria[4] = 1
        else:
            criteria[4] = 1

    # Criterion 3: Wiki accuracy
    wiki_used = [bool(lesson.get("wiki_pages_used")) for lesson in lesson_list]
    if any(wiki_used):
        criteria[3] = 2 if all(wiki_used) else 1

    # Criterion 9: Failure analysis
    chain_lens = []
    for lesson in lesson_list:
        cc = lesson.get("cause_chain")
        if isinstance(cc, list):
            chain_lens.append(len(cc))
        else:
            chain_lens.append(0)
    if chain_lens:
        if min(chain_lens) >= 2:
            criteria[9] = 2
        elif any(chain_len >= 1 for chain_len in chain_lens):
            criteria[9] = 1

    # Criterion 7: Actionability
    action_scores = []
    for lesson in lesson_list:
        rec = str(lesson.get("recommendation") or "").lower()
        has_action = any(v in rec for v in ACTION_VERBS)
        action_scores.append(has_action)
    if action_scores:
        if all(action_scores):
            criteria[7] = 2
        elif any(action_scores):
            criteria[7] = 1

    # Criterion 5: Invention
    # Heuristic: if model supplies unverified_claims frequently, treat as restrained.
    inv_base = sum(1 for f in unverified_flags if f)
    if inv_base == len(lesson_list) and len(lesson_list) > 0:
        criteria[5] = 2
    elif inv_base > 0:
        criteria[5] = 1

    # Criterion 8: Restraint
    n = len(lesson_list)
    if 3 <= n <= 6:
        criteria[8] = 2
    elif 1 <= n <= 10:
        criteria[8] = 1

    # Criterion 10: Calibration
    if evidence_counts:
        good = 0
        for lesson, ev in zip(lesson_list, evidence_counts, strict=False):
            conf = lesson.get("confidence")
            try:
                conf = float(conf)
            except Exception:
                conf = 0.0
            if (ev <= 1 and conf <= 0.4) or (ev >= 2 and conf >= 0.5):
                good += 1
        criteria[10] = 2 if good == len(lesson_list) else 1 if good > 0 else 0

    total = sum(criteria[1:])
    return criteria, total


def _safe_model_suffix(s: str) -> str:
    return s.replace(":", "_").replace("/", "_").replace("\\", "_")


def eval_one(
    run_id: str,
    bundle_text: str,
    provider: str,
    model: str,
    *,
    reuse_existing: bool,
    rubric_labels: dict[int, str],
    system: str | None,
) -> tuple[ScoreRow, str]:
    out_path = os.path.join(DEBRIEFS_DIR, f"{run_id}.{provider}.{_safe_model_suffix(model)}.response.md")
    os.makedirs(DEBRIEFS_DIR, exist_ok=True)

    if reuse_existing and os.path.exists(out_path):
        with open(out_path, encoding="utf-8") as f:
            raw_answer = f.read()
        criteria, total = score_debrief_answer(bundle_text, raw_answer)
        weakest_i = min(range(1, 11), key=lambda i: criteria[i])
        weakest = rubric_labels.get(weakest_i, str(weakest_i))
        return (
            ScoreRow(provider=provider, model=model, total=total, criteria=criteria[1:], weakest=weakest),
            out_path,
        )

    analysis = None
    try:
        analysis = analyze_debrief(
            bundle_text,
            model=model,
            provider=provider,
            task="debrief",
            system=system,
        )
    except Exception as e:
        raw_answer = f"(error: {e})"
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(raw_answer)
        criteria = [0] * 11
        total = 0
        return (
            ScoreRow(provider=provider, model=model, total=total, criteria=criteria[1:], weakest="1"),
            out_path,
        )

    raw_answer = analysis.get("raw") if isinstance(analysis, dict) else None
    if not raw_answer:
        # Fallback: write whatever analysis returned.
        raw_answer = json.dumps(analysis, default=str, indent=2)

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(raw_answer)

    criteria, total = score_debrief_answer(bundle_text, raw_answer)
    weakest_i = min(range(1, 11), key=lambda i: criteria[i])
    weakest = rubric_labels.get(weakest_i, str(weakest_i))
    return (
        ScoreRow(provider=provider, model=model, total=total, criteria=criteria[1:], weakest=weakest),
        out_path,
    )


def main():
    ap = argparse.ArgumentParser(description="Evaluate models on the same debrief bundle and score with the rubric")
    ap.add_argument("--run", required=True, help="Run ID (e.g. run-006-obs-cassandra)")
    ap.add_argument(
        "--models",
        nargs="+",
        required=True,
        help="Pairs like provider:model (e.g. ollama:gemma4-e2b-rimworld)",
    )
    ap.add_argument("--temperature", type=float, default=0.3)
    ap.add_argument("--no-reuse", action="store_true", help="Re-run models even if response files exist")
    args = ap.parse_args()

    reuse_existing = not args.no_reuse

    rubric_labels = _load_rubric_labels()

    bundle_path = find_bundle(args.run)
    if not bundle_path or not os.path.exists(bundle_path):
        print(f"Bundle not found: {bundle_path}")
        sys.exit(1)

    with open(bundle_path, encoding="utf-8") as f:
        bundle_text = f.read()

    is_bundle = ("Section A" in bundle_text) and ("## 8. Task" in bundle_text or "## 8." in bundle_text)
    system = BUNDLE_SYSTEM if is_bundle else None

    rows: list[ScoreRow] = []
    for pair in args.models:
        if ":" not in pair:
            raise SystemExit(f"Invalid --models entry '{pair}', expected provider:model")
        provider, model = pair.split(":", 1)
        provider = provider.strip()
        model = model.strip()
        row, _path = eval_one(
            args.run,
            bundle_text,
            provider,
            model,
            reuse_existing=reuse_existing,
            rubric_labels=rubric_labels,
            system=system,
        )
        rows.append(row)

    # Print comparison table.
    rows.sort(key=lambda r: (r.total, -int(r.criteria and max(r.criteria)) ), reverse=True)
    print("Model comparison")
    print("Run:", args.run)
    print("\n| Provider | Model | Total | Weakest |")
    print("|---|---|---:|---:|")
    for r in rows:
        print(f"| {r.provider} | {r.model} | {r.total} | {r.weakest} |")


if __name__ == "__main__":
    main()
