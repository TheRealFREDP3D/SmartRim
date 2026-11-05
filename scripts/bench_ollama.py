"""Benchmark every Ollama chat model listed in ollama_models.md on one debrief bundle.

Measures speed (load, prefill, decode, end-to-end) and quality (rubric score via
smartrim.eval_models.score_debrief_answer + Section A schema validity).

Usage:
    python scratchpad/bench_ollama.py --pilot
    python scratchpad/bench_ollama.py
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
from datetime import datetime

import requests

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "src"))

import contextlib

from smartrim.debrief_llm import (
    BUNDLE_SYSTEM,
    _extract_first_json_fence,
    _validate_lesson_candidates,
)
from smartrim.eval_models import score_debrief_answer

OLLAMA = os.getenv("OLLAMA_HOST", "127.0.0.1:11434")
if not OLLAMA.startswith("http"):
    OLLAMA = "http://" + OLLAMA
BUNDLE = os.path.join(
    ROOT, ".DEV", "ARCHIVE", "runtime", "memory", "debriefs", "run-009-adv.bundle.md"
)
OUT_DIR = os.path.join(ROOT, "runtime", "bench")
RESULTS = os.path.join(OUT_DIR, "results.jsonl")
MODELS_MD = os.path.join(ROOT, "ollama_models.md")

NUM_CTX = 16384
TEMPERATURE = 0.3
NUM_PREDICT = 4096
TIMEOUT_S = 900

def load_models():
    """Model list from ollama_models.md, or every chat model Ollama reports."""
    if not os.path.exists(MODELS_MD):
        return None
    names = []
    with open(MODELS_MD, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            name = line.split()[0].replace("\\", "")
            if ":" not in name:
                continue
            names.append(name)
    return names


def resolve_name(name, available):
    """Repair truncated entries like 'Model:lates4.9' from the markdown table."""
    if name in available:
        return name
    base = name.split(":", 1)[0].lower()
    for candidate in available:
        if candidate.lower().startswith(base + ":"):
            return candidate
    return None


def tags():
    data = requests.get(f"{OLLAMA}/api/tags", timeout=20).json()
    return {m["name"]: m for m in data.get("models", [])}


def unload(model):
    with contextlib.suppress(Exception):
        requests.post(
            f"{OLLAMA}/api/generate",
            json={"model": model, "prompt": "", "keep_alive": 0},
            timeout=30,
        )


def build_prompt(bundle_text):
    system = BUNDLE_SYSTEM + (
        "\n\nWhen outputting Section A, wrap the JSON array in a single fenced block: ```json ...```"
    )
    prompt = "Analyze this RimWorld colony debrief bundle:\n\n" + bundle_text
    return system, prompt


def run_model(name, digest, size, bundle_text):
    system, prompt = build_prompt(bundle_text)
    payload = {
        "model": name,
        "prompt": prompt,
        "system": system,
        "stream": False,
        "keep_alive": "10m",
        "options": {
            "num_ctx": NUM_CTX,
            "temperature": TEMPERATURE,
            "num_predict": NUM_PREDICT,
        },
    }
    started = time.time()
    try:
        r = requests.post(f"{OLLAMA}/api/generate", json=payload, timeout=(10, TIMEOUT_S))
        r.raise_for_status()
        data = r.json()
        error = None
    except requests.exceptions.ReadTimeout:
        return {
            "model": name,
            "digest": digest,
            "size_bytes": size,
            "status": "timeout",
            "wall_s": round(time.time() - started, 1),
            "error": f">{TIMEOUT_S}s",
        }
    except Exception as e:
        return {
            "model": name,
            "digest": digest,
            "size_bytes": size,
            "status": "error",
            "wall_s": round(time.time() - started, 1),
            "error": str(e)[:300],
        }

    wall = time.time() - started
    text = data.get("response") or ""
    eval_count = data.get("eval_count") or 0
    eval_dur = (data.get("eval_duration") or 0) / 1e9
    prompt_count = data.get("prompt_eval_count") or 0
    prompt_dur = (data.get("prompt_eval_duration") or 0) / 1e9
    load_dur = (data.get("load_duration") or 0) / 1e9

    criteria, total = score_debrief_answer(bundle_text, text)
    try:
        parsed = _extract_first_json_fence(text)
        lessons = _validate_lesson_candidates(parsed)
        schema_ok = True
        n_lessons = len(lessons)
    except Exception:
        schema_ok = False
        n_lessons = 0

    # Keep the raw answer: quality scores are meaningless without the text.
    ans_dir = os.path.join(OUT_DIR, "answers")
    os.makedirs(ans_dir, exist_ok=True)
    safe = name.replace(":", "_").replace("/", "_").replace("\\", "_")
    with open(os.path.join(ans_dir, safe + ".txt"), "w", encoding="utf-8") as f:
        f.write(text)

    return {
        "model": name,
        "digest": digest,
        "size_bytes": size,
        "status": "ok",
        "wall_s": round(wall, 2),
        "load_s": round(load_dur, 2),
        "prompt_tokens": prompt_count,
        "prompt_tok_s": round(prompt_count / prompt_dur, 1) if prompt_dur else None,
        "out_tokens": eval_count,
        "out_tok_s": round(eval_count / eval_dur, 2) if eval_dur else None,
        "end_to_end_tok_s": round(eval_count / wall, 2) if wall else None,
        "truncated": eval_count >= NUM_PREDICT,
        "quality_total": total,
        "criteria": criteria[1:],
        "schema_ok": schema_ok,
        "lessons": n_lessons,
        "answer_chars": len(text),
        "error": error,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pilot", action="store_true", help="only the two 1B models")
    ap.add_argument("--only", nargs="*", default=None)
    ap.add_argument("--resume", action="store_true", help="skip models already in results.jsonl")
    ap.add_argument("--timeout", type=int, default=None, help="per-model read timeout (s)")
    ap.add_argument("--max-predict", type=int, default=None, help="max generated tokens")
    args = ap.parse_args()

    global TIMEOUT_S, NUM_PREDICT
    if args.timeout:
        TIMEOUT_S = args.timeout
    if args.max_predict:
        NUM_PREDICT = args.max_predict

    os.makedirs(OUT_DIR, exist_ok=True)
    bundle_text = open(BUNDLE, encoding="utf-8").read()
    available = tags()
    names = load_models()
    if names is None:
        # No curated list: benchmark every chat model Ollama reports.
        embedding_hints = ("embed", "bge-", "mxbai", "arctic", "nomic")
        names = [
            n for n in available
            if not any(h in n.lower() for h in embedding_hints)
        ]
        print(f"No {os.path.basename(MODELS_MD)}; using {len(names)} locally installed models")

    # Dedupe by digest (qwen3:latest == qwen3:8b, etc.)
    seen = {}
    ordered = []
    for n in names:
        resolved = resolve_name(n, available)
        if not resolved:
            print(f"MISSING from ollama: {n}")
            continue
        meta = available[resolved]
        d = meta["digest"]
        if d in seen:
            print(f"SKIP duplicate digest: {resolved} == {seen[d]}")
            continue
        seen[d] = resolved
        ordered.append((resolved, d, meta.get("size") or 0))

    if args.only:
        wanted = set(args.only)
        ordered = [x for x in ordered if x[0] in wanted]
    if args.pilot:
        ordered = [x for x in ordered if x[0] in ("gemma3:1b", "llama3.2:1b-instruct-q4_K_M")]

    ordered.sort(key=lambda x: x[2])

    done = set()
    if args.resume and os.path.exists(RESULTS):
        for line in open(RESULTS, encoding="utf-8"):
            with contextlib.suppress(Exception):
                done.add(json.loads(line)["model"])

    print(f"Bundle: {os.path.basename(BUNDLE)} ({len(bundle_text)} chars)")
    print(f"Models: {len(ordered)} | num_ctx={NUM_CTX} num_predict={NUM_PREDICT} timeout={TIMEOUT_S}s")
    print(f"Started: {datetime.now().isoformat(timespec='seconds')}\n")

    with open(RESULTS, "a", encoding="utf-8") as out:
        for i, (name, digest, size) in enumerate(ordered, 1):
            if name in done:
                print(f"[{i}/{len(ordered)}] skip (done): {name}")
                continue
            print(f"[{i}/{len(ordered)}] {name} ({size/1e9:.1f} GB) ...", flush=True)
            row = run_model(name, digest, size, bundle_text)
            out.write(json.dumps(row) + "\n")
            out.flush()
            if row["status"] == "ok":
                print(
                    f"    wall {row['wall_s']}s | load {row['load_s']}s | "
                    f"out {row['out_tokens']} tok @ {row['out_tok_s']} tok/s | "
                    f"quality {row['quality_total']}/20 | schema {row['schema_ok']} | "
                    f"lessons {row['lessons']}"
                )
            else:
                print(f"    {row['status']}: {row.get('error')}")
            unload(name)

    print("\nDone:", datetime.now().isoformat(timespec="seconds"))
    print("Results:", RESULTS)


if __name__ == "__main__":
    main()
