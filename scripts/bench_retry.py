"""Re-run the top models with the app's schema-repair loop.

Measures the real cost of a usable answer: attempt 1 may fail the exact Section A
contract, but debrief_llm retries with the validation error and the allowed
trigger vocabulary. Records attempts and total wall time.

Usage: python scripts/bench_retry.py
"""

from __future__ import annotations

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
    _schema_retry_prompt,
    _validate_lesson_candidates,
)
from smartrim.eval_models import score_debrief_answer

OLLAMA = os.getenv("OLLAMA_HOST", "127.0.0.1:11434")
if not OLLAMA.startswith("http"):
    OLLAMA = "http://" + OLLAMA
BUNDLE = os.path.join(
    ROOT, ".DEV", "ARCHIVE", "runtime", "memory", "debriefs", "run-009-adv.bundle.md"
)
OUT = os.path.join(ROOT, "runtime", "bench")
RESULTS = os.path.join(OUT, "retry.jsonl")

MODELS = [
    "gemma-4-E2B-it-Q4_K_M:latest",
    "Qwen3-1.7B-Q6_K:latest",
    "llama3.2:3b",
    "gemma4-e2b-rimworld:latest",
]

FENCE = (
    "\n\nWhen outputting Section A, wrap the JSON array in a single fenced block: ```json ...```"
)
NUM_CTX = 16384
TEMPERATURE = 0.3
NUM_PREDICT = 4096
TIMEOUT_S = 300
MAX_ATTEMPTS = 3


def generate(model, system, prompt):
    payload = {
        "model": model,
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
    r = requests.post(f"{OLLAMA}/api/generate", json=payload, timeout=(10, TIMEOUT_S))
    r.raise_for_status()
    data = r.json()
    return data.get("response") or "", time.time() - started, data


def main():
    import argparse

    global MAX_ATTEMPTS
    ap = argparse.ArgumentParser()
    ap.add_argument("--models", nargs="*", default=None)
    ap.add_argument("--attempts", type=int, default=MAX_ATTEMPTS)
    ap.add_argument("--tag", default="retry")
    args = ap.parse_args()

    MAX_ATTEMPTS = args.attempts
    models = args.models or MODELS

    os.makedirs(OUT, exist_ok=True)
    bundle = open(BUNDLE, encoding="utf-8").read()
    prompt = "Analyze this RimWorld colony debrief bundle:\n\n" + bundle
    base_system = BUNDLE_SYSTEM + FENCE

    results_path = os.path.join(OUT, f"{args.tag}.jsonl")
    print(f"Models: {len(models)} | retries: {MAX_ATTEMPTS} | timeout/attempt: {TIMEOUT_S}s\n")

    with open(results_path, "w", encoding="utf-8") as out:
        for model in models:
            print(f"{model}", flush=True)
            system = base_system
            total_wall = 0.0
            answer = ""
            ok = False
            attempt = 0
            last_err = ""
            for attempt in range(1, MAX_ATTEMPTS + 1):
                try:
                    answer, wall, _meta = generate(model, system, prompt)
                except Exception as e:
                    last_err = f"request failed: {e}"
                    print(f"  attempt {attempt}: {last_err}")
                    break
                total_wall += wall
                try:
                    parsed = _extract_first_json_fence(answer)
                    _validate_lesson_candidates(parsed)
                    ok = True
                    print(f"  attempt {attempt}: schema OK ({wall:.0f}s)")
                    break
                except Exception as e:
                    last_err = " ".join(str(e).split())[:500]
                    print(f"  attempt {attempt}: {last_err[:90]}... ({wall:.0f}s)")
                    system = base_system + _schema_retry_prompt(last_err)

            criteria, total = score_debrief_answer(bundle, answer)
            row = {
                "model": model,
                "attempts": attempt,
                "schema_ok": ok,
                "total_wall_s": round(total_wall, 1),
                "quality_total": total,
                "criteria": criteria[1:],
                "last_error": "" if ok else last_err,
            }
            out.write(json.dumps(row) + "\n")
            out.flush()
            safe = model.replace(":", "_").replace("/", "_")
            with open(os.path.join(OUT, f"{args.tag}-{safe}.txt"), "w", encoding="utf-8") as f:
                f.write(answer)
            print(f"  => usable={ok} attempts={attempt} total={total_wall:.0f}s quality={total}/20\n", flush=True)
            with contextlib.suppress(Exception):
                requests.post(
                    f"{OLLAMA}/api/generate",
                    json={"model": model, "prompt": "", "keep_alive": 0},
                    timeout=30,
                )

    print("Done:", datetime.now().isoformat(timespec="seconds"))


if __name__ == "__main__":
    main()
