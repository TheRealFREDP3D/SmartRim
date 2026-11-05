"""Turn runtime/bench/results.jsonl into a speed/quality report.

Usage: python scratchpad/report_bench.py
Writes runtime/bench/report.md and prints the tables.
"""

from __future__ import annotations

import json
import os
import sys
from datetime import datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "src"))

from smartrim.debrief_llm import (
    _extract_first_json_fence,
    _validate_lesson_candidates,
)

RESULTS = os.path.join(ROOT, "runtime", "bench", "results.jsonl")
ANSWERS = os.path.join(ROOT, "runtime", "bench", "answers")
REPORT = os.path.join(ROOT, "runtime", "bench", "report.md")


def answer_path(model):
    safe = model.replace(":", "_").replace("/", "_").replace("\\", "_")
    return os.path.join(ANSWERS, safe + ".txt")


def schema_error(model):
    """Exact reason a model's Section A fails the app contract."""
    path = answer_path(model)
    if not os.path.exists(path):
        return "no answer file"
    text = open(path, encoding="utf-8").read()
    try:
        parsed = _extract_first_json_fence(text)
    except Exception:
        return "no fenced JSON array"
    try:
        _validate_lesson_candidates(parsed)
        return ""
    except Exception as e:
        return " ".join(str(e).split())[:110]


def load():
    seen = {}
    with open(RESULTS, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            row = json.loads(line)
            seen[row["model"]] = row  # last run wins
    return list(seen.values())


def fmt_size(n):
    return f"{n / 1e9:.1f}" if n else "?"


def sort_rows(rows):
    ok = [r for r in rows if r["status"] == "ok"]
    bad = [r for r in rows if r["status"] != "ok"]
    ok.sort(key=lambda r: (-r["quality_total"], -(r.get("out_tok_s") or 0)))
    bad.sort(key=lambda r: r["model"])
    return ok, bad


def pareto(ok):
    """Models not beaten on both speed and quality by another model."""
    front = []
    for r in ok:
        speed = r.get("out_tok_s") or 0
        q = r["quality_total"]
        dominated = any(
            (o.get("out_tok_s") or 0) >= speed and o["quality_total"] >= q
            and ((o.get("out_tok_s") or 0) > speed or o["quality_total"] > q)
            for o in ok
            if o is not r
        )
        if not dominated:
            front.append(r)
    front.sort(key=lambda r: (r.get("out_tok_s") or 0), reverse=True)
    return front


def recommend(ok):
    usable = [r for r in ok if r.get("schema_ok") and r["quality_total"] >= 10]
    best_quality = max(ok, key=lambda r: (r["quality_total"], r.get("out_tok_s") or 0), default=None)
    fastest = max(ok, key=lambda r: (r.get("out_tok_s") or 0), default=None)
    fastest_usable = max(usable, key=lambda r: (r.get("out_tok_s") or 0), default=None)

    max_speed = max((r.get("out_tok_s") or 0) for r in ok) if ok else 1
    balance = max(
        ok,
        key=lambda r: (r["quality_total"] / 20) * ((r.get("out_tok_s") or 0) / max_speed) ** 0.5,
        default=None,
    )
    return {
        "fastest": fastest,
        "fastest_usable": fastest_usable,
        "best_quality": best_quality,
        "balance": balance,
    }


def markdown(rows):
    ok, bad = sort_rows(rows)
    rec = recommend(ok)
    front = pareto(ok)
    lines = [
        "# Ollama model benchmark — speed vs quality",
        "",
        f"Generated: {datetime.now().isoformat(timespec='seconds')}",
        "Bundle: `run-009-adv.bundle.md` (28,014 chars, v3)",
        "Settings: `num_ctx=16384`, `temperature=0.3`, `num_predict=4096`, one run per model, cold load.",
        "Quality: rubric from `memory/debrief-rubric.md` (0-20). Speed: decode tokens/s from Ollama.",
        "Zero-shot: the app retries schema failures up to 3 times with the validation error, so a failure",
        "here is a robustness/latency signal, not an automatic rejection.",
        "",
        "## Ranked by quality",
        "",
        "| Model | Digest | GB | Quality | Decode tok/s | Wall s | Schema | Lessons | Out tok |",
        "|---|---|---:|---:|---:|---:|:--:|---:|---:|",
    ]
    for r in ok:
        lines.append(
            f"| {r['model']} | `{r['digest'][:12]}` | {fmt_size(r['size_bytes'])} | "
            f"{r['quality_total']}/20 | {r.get('out_tok_s')} | {r['wall_s']} | "
            f"{'yes' if r['schema_ok'] else 'no'} | {r['lessons']} | {r['out_tokens']} |"
        )
    if bad:
        lines += ["", "## Failed or timed out", "", "| Model | Status | Wall s | Error |", "|---|---|---:|---|"]
        for r in bad:
            lines.append(f"| {r['model']} | {r['status']} | {r['wall_s']} | {r.get('error','')} |")

    invalid = [r for r in ok if not r.get("schema_ok")]
    if invalid:
        lines += ["", "## Why schema validation fails (app contract)", "",
                  ("The rubric is lenient; the app needs the exact Section A contract. "
                  "These answers score points but could not be promoted automatically."),
                  "", "| Model | Reason |", "|---|---|"]
        for r in invalid:
            lines.append(f"| {r['model']} | {schema_error(r['model'])} |")

    lines += ["", "## Pareto frontier (no model is both faster and better)", ""]
    for r in front:
        lines.append(f"- **{r['model']}** — {r.get('out_tok_s')} tok/s, {r['quality_total']}/20")

    lines += ["", "## Recommendation", ""]
    for key, label in (
        ("fastest", "Fastest overall"),
        ("fastest_usable", "Fastest that still produces schema-valid lessons"),
        ("best_quality", "Best quality"),
        ("balance", "Best balance (quality weighted by speed)"),
    ):
        r = rec.get(key)
        if r:
            lines.append(
                f"- **{label}:** `{r['model']}` — {r.get('out_tok_s')} tok/s, "
                f"{r['quality_total']}/20, schema {'ok' if r['schema_ok'] else 'fail'}"
            )
    lines.append("")
    return "\n".join(lines)


def main():
    rows = load()
    text = markdown(rows)
    os.makedirs(os.path.dirname(REPORT), exist_ok=True)
    with open(REPORT, "w", encoding="utf-8") as f:
        f.write(text)
    print(text)
    print(f"\nWrote {REPORT}")


if __name__ == "__main__":
    main()
