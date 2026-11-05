# Ollama model benchmark — 2026-11-05

Goal: find the fastest model and the best-quality model for SmartRim's debrief
task on the actual hardware, then decide which one to use.

## Setup

| Item | Value |
|---|---|
| Hardware | GTX 1050 Ti, 4 GB VRAM; 32 GB RAM; Windows |
| Ollama | 0.40.11, `flash_attn=on`, `kv_cache=q8_0`, `num_parallel=1` |
| Bundle | `run-009-adv.bundle.md` (28,014 chars, v3, Section 8 task) |
| Settings | `num_ctx=16384`, `temperature=0.3`, `num_predict=4096` |
| Protocol | one run per model, cold load, model unloaded between runs |
| Quality | `memory/debrief-rubric.md`, 10 criteria × 0–2 = 20 |
| Speed | decode tok/s reported by Ollama |

Models are the ones in `ollama_models.md`; `qwen3:latest` and `qwen3:8b` share a
digest, so 17 unique digests were run. Digests are recorded in the tables.

## Zero-shot results

| Model | Digest | GB | Rubric | Decode tok/s | Wall | Schema |
|---|---|---:|---:|---:|---:|:--:|
| gemma-4-E2B-it-Q4_K_M | `ebb4e91482e6` | 3.1 | **19/20** | 16.7 | 196 s | fail |
| Qwen3-1.7B-Q6_K | `ad47863af7c1` | 1.7 | 17/20 | 15.4 | 167 s | fail |
| llama3.2:3b | `a80c4f17acd5` | 2.0 | 15/20 | 5.5 | 291 s | fail |
| gemma4-e2b-rimworld | `c95ec9b9354f` | 3.1 | 14/20 | 16.0 | 234 s | fail |
| gemma3:1b | `8648f39daa8f` | 0.8 | 9/20 | **29.4** | 154 s | fail |
| gemma-3-1B-it-QAT-Q4_0 | `02f708abca79` | 0.7 | 0/20 | **32.7** | 47 s | fail |
| llama3.2:1b-instruct-q4_K_M | `22bc6b92eb01` | 0.8 | 0/20 | 31.8 | 149 s | fail |
| deepseek-r1:1.5b | `a42b25d8c10a` | 1.1 | 0/20 | 23.2 | 209 s | fail |

Timed out at 300 s: Phi-4-mini-reasoning (3.8B), Mistral-7B, llama3.1,
qwen3-rimworld, qwen3, deepseek-r1:8b, DeepSeek-R1-0528-Qwen3-8B,
DeepSeek-R1-Distill-Llama-8B. `llama3.2-vision` returned HTTP 500 on load.

## Retry results (the app's repair loop, 3 attempts)

Before scalar coercion (2026-11-05):

| Model | Attempts | Total wall | Rubric | Schema |
|---|---:|---:|---:|:--:|
| gemma-4-E2B-it-Q4_K_M | 3 | 598 s | **20/20** | fail |
| gemma4-e2b-rimworld | 3 | 600 s | 20/20 | fail |
| Qwen3-1.7B-Q6_K | 3 | 463 s | 17/20 | fail |
| llama3.2:3b | 3 | 435 s | 16/20 | fail |

After scalar→list coercion in `TriggerCandidate` (verified by re-running the
same two models through the real loop):

| Model | Attempts | Total wall | Rubric | Schema |
|---|---:|---:|---:|:--:|
| gemma-4-E2B-it-Q4_K_M | **2** | 433 s | 19/20 | **ok** |
| Qwen3-1.7B-Q6_K | **2** | 417 s | 17/20 | **ok** |

The first attempt still fails on vocabulary (`"injury"` vs `colonist_injured`),
the retry fixes the vocabulary, and the coercion accepts the scalar form it
returns. That is the difference between "no model is usable" and "usable in two
attempts".

## Findings

1. **Best quality:** `gemma-4-E2B-it-Q4_K_M` — 19/20 zero-shot, 20/20 after retry,
   16.7 tok/s, 196 s per answer. It is the only model that reaches a perfect
   rubric score.
2. **Best speed/quality tradeoff:** `Qwen3-1.7B-Q6_K` — 17/20 at 15.4 tok/s,
   167 s. Faster and smaller, one rubric point behind.
3. **Fastest overall is unusable:** `gemma-3-1B-it-QAT` at 32.7 tok/s scores 0/20
   and returns an object instead of an array. `llama3.2:1b` degenerates into a
   repeated `Day 0-7…` loop. `deepseek-r1:1.5b` never emits fenced JSON.
4. **4 GB ceiling:** every model above 4.7 GB exceeded 300 s. The 7–11B group is
   not viable for interactive advice on this machine, regardless of quality.
5. **The schema gate, not the model, was the bottleneck.** All zero-shot failures
   are vocabulary/type errors (`"injury"` vs `colonist_injured`, `"low food"` vs
   `low_food`). After retries the vocabulary is correct but the model emits
   scalars where lists were required (`phases='stabilization'`).
   `TriggerCandidate` accepted scalars only for `difficulty`/`storyteller`/`biome`,
   so semantically correct answers were rejected on shape alone. **Fixed:** scalar
   values are now wrapped for `phases`/`threats`/`resources` (invalid vocabulary
   still fails). Both test models then validate on attempt 2 instead of 3.
6. **The tuned Modelfile did not help.** `gemma4-e2b-rimworld` scored 14/20
   zero-shot and 20/20 after retry, but took 600 s over 3 attempts versus 598 s
   for the stock `gemma-4-E2B-it`; on this test the stock model is equal or better.

## Recommendation

| Use case | Model | Why |
|---|---|---|
| Debrief quality (batch, once per run) | `gemma-4-E2B-it-Q4_K_M:latest` | 19/20, schema-valid on attempt 2, 433 s total |
| Cheapest coherent model | `Qwen3-1.7B-Q6_K:latest` | 17/20, schema-valid on attempt 2, 417 s total |
| Do not use | `gemma-3-1B-QAT`, `llama3.2:1b`, `deepseek-r1:1.5b` | 0/20 — loops, wrong shape, or no JSON |
| Do not use on this GPU | anything ≥4.7 GB | exceeds 300 s per answer |

**Resolved during this benchmark:** scalar→list coercion for
`trigger.phases`/`threats`/`resources` in `debrief_llm.TriggerCandidate`, with
tests. Both surviving models now validate on attempt 2. The remaining cost is
vocabulary repair (one extra ~200 s pass), not format rejection.

Note on latency: ~7 minutes end-to-end is acceptable for a once-per-run debrief,
but not for interactive advice. If in-game advice needs to be fast, it must not
use the 16k-context debrief prompt on this hardware.

## Cloud alternative: NVIDIA NIM (tested 2026-11-05)

The same bundle against `nvidia/nemotron-3.5-super-vl-120b-a12b` through
`LLM_PROVIDER=nvidia` (OpenAI-compatible endpoint, `NVIDIA_API_KEY`):

| Path | Result |
|---|---|
| Small prompt via `smartrim.llm.generate` | 2.8 s, exact answer |
| Full debrief via `debrief_llm.analyze_debrief` | **141 s, 4–5 schema-valid lessons, 16/20, no retries** |
| Local best for comparison | gemma-4-E2B-it: 19/20, 433 s and 2 attempts |

Trade-off: NIM is ~3× faster than the local best and needs no VRAM, but scored
3 points lower on this run (weakest: unverified claims 0/2, invention 1/2).
Rubric variance between runs is real; treat 16 vs 19 as close, not decisive.

Operational note: this is a thinking model. It returns `reasoning_content`
alongside `content`, and a small `max_tokens` can be consumed entirely by
reasoning, leaving `content=None`. `smartrim.llm.generate` does not set
`max_tokens` by default, so the app path is fine; callers that cap tokens must
budget for thinking.

`LLM_PROVIDER=nvidia` overrides the task registry for every task, and the model
comes from `NVIDIA_MODEL`, not `LLM_MODEL` (registry names are local Ollama tags).

Model card archived at
`docs/models/nvidia-nemotron-3.5-super-vl-120b-a12b.md` (source links in the
file header).



```powershell
.\start-ollama.ps1
python scripts\bench_ollama.py --resume --timeout 300
python scripts\report_bench.py
python scripts\bench_retry.py
```

Raw answers: `runtime/bench/answers/` and `runtime/bench/retry-*.txt`.
Results: `runtime/bench/results.jsonl`, `retry.jsonl`, `report.md`.
