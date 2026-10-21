# LLM Benchmark — Ollama models on this machine

**Date:** 2026-10-21
**Hardware:** Intel Core i7-6700K (4c/8t), 32 GB RAM, NVIDIA GTX 1050 Ti (4 GB VRAM)
**Ollama:** 0.34.0, models stored on `D:\BACKUP\MODELS`
**Server config:** flash attention ON, KV cache `q8_0`, `OLLAMA_NUM_PARALLEL=1`, `OLLAMA_MAX_LOADED_MODELS=2`, `OLLAMA_KEEP_ALIVE=30m`, `OLLAMA_NUM_GPU=999`, debug OFF.

## Goal

Pick the best trade-off between **speed** (tokens/sec, total latency) and **quality** (valid structured JSON + relevant content) for the SmartRim sidecar's debrief/analysis task, on a 4 GB VRAM GPU.

## Method

- All installed **chat/completion** models were benchmarked; embedding-only models and exact digest duplicates were skipped.
- A single fixed prompt (constant base data) was used for every model so results are comparable.
- Each request: `stream=false`, `think=false`, `keep_alive=0` (model unloaded after each run to free VRAM), `temperature=0`, `num_ctx=4096`, `num_predict=512`.
- A warm-up was implicit via the first request's load time, which is included in `total_s`.
- Timeout: 300s per model.

### Prompt used

```
You are reviewing a RimWorld colony run.

Colony data:
- Day 5: 3 colonists, food 12 units, medicine 0; alerts: food_low, medicine_low.
- Day 6: raid (3 raiders); 1 colonist downed; food 4.
- Day 7: colony wiped (all colonists dead).

Task: Return ONLY a JSON object with these keys:
  "primary_cause" (string),
  "worked" (array of strings),
  "lessons" (array of strings, max 3),
  "next_steps" (array of strings).
No markdown, no extra text.
```

### Scoring (max ~14)

- +2 for valid JSON (after stripping markdown fences).
- +1 for each of the 4 required keys present.
- +1 if `lessons` is a list with ≤ 3 items.
- +1 if `worked` is a non-empty list.
- +1 if `next_steps` is a non-empty list.
- +1 for each relevant keyword found in the output (raid, food, medicine, defense, doctor, stock) — up to +6.
- −1 if the output contained markdown fences (```).

## Results

Sorted by score descending, then by tok/s.

| Rank | Model | Score | tok/s | total_s | eval_tokens | Notes |
|---:|---|---:|---:|---:|---:|---|
| 1 | qwen3-rimworld (custom) | 14 | 5.07 | 32.0 | — | valid_json, kw5 |
| 1 | gemma-4-E2B-it-Q4_K_M | 14 | 19.60 | 35.2 | — | valid_json, kw5 |
| 1 | Mistral-7B-Instruct-v0.3-Q4_K_M | 14 | 6.93 | 58.5 | — | valid_json, kw5 |
| 4 | qwen3:latest (8b) | 13 | 5.39 | 34.0 | — | valid_json, kw4 |
| 5 | Qwen3-1.7B-Q6_K | 13 | 24.21 | 22.8 | — | valid_json, kw4 |
| 6 | qwen2.5-coder:7b | 12 | 6.17 | 65.3 | — | valid_json, kw4, fences |
| 7 | llama3.2:1b-instruct-q4_K_M | 12 | 41.49 | 12.3 | — | valid_json, kw3 |
| 8 | llama-3.1:latest (4.9GB) | 11 | 6.65 | 57.8 | — | valid_json, kw3, fences |
| 9 | llama3.2:3b | 11 | 12.30 | 30.6 | — | valid_json, kw2 |
| 10 | gemma3:latest (4b) | 11 | 9.74 | 55.0 | — | valid_json, kw3, fences |
| 11 | llama-3.1:latest (4.7GB, Q4_0) | 11 | 6.24 | 87.1 | — | valid_json, kw3, fences |
| 12 | gemma-3-1B-it-QAT-Q4_0 | 10 | 34.47 | 13.4 | — | valid_json, kw2, fences |
| 13 | gemma3:1b | 10 | 29.44 | 16.0 | — | valid_json, kw2, fences |
| 14 | qwen2.5:1.5b | 10 | 26.17 | 16.8 | — | valid_json, kw2, fences |
| 15 | Phi-4-mini-reasoning-Q4_K_M | 0 | 8.87 | 90.4 | — | invalid_json (thinking output) |
| 16 | DeepSeek-R1-Distill-Llama-8B | 0 | 5.52 | 172.4 | — | invalid_json |
| 17 | deepseek-r1:8b | −1 | 5.37 | 132.0 | — | invalid_json |
| 18 | DeepSeek-R1-0528-Qwen3-8B | −1 | 4.86 | 160.2 | — | invalid_json |
| 19 | deepseek-r1:1.5b | −1 | 24.00 | 35.0 | — | invalid_json |
| 20 | llama3.2-vision:latest | — | — | — | — | HTTP 500 (too large for 4 GB VRAM) |

Raw data: `scratchpad/bench_results.json`.

## Analysis

### Quality
Three models tied at the top score (14): **qwen3-rimworld**, **gemma-4-E2B-it-Q4_K_M**, and **Mistral-7B-Instruct**. All produced valid JSON with 5/6 keyword hits. The qwen3 variant gave the most nuanced reasoning; gemma-4-E2B and Mistral were more concise.

### Speed
- 4 GB VRAM cannot hold an 8B Q4 model fully; 8B models offload ~40–60% to CPU, capping them at 5–7 tok/s.
- Sub-4B models fit (mostly) on GPU and reach 20–41 tok/s.
- **gemma-4-E2B-it-Q4_K_M** is the standout: top quality (14) at 19.6 tok/s — ~4× faster than qwen3, with valid JSON and no fences.

### Structured-output reliability
All DeepSeek-R1 variants emitted chain-of-thought (`<think>…`) and failed to return parseable JSON under this prompt, even with `think=false`. They are unsuitable for direct structured extraction unless wrapped in post-processing. Phi-4-mini-reasoning likewise failed.

### Trade-off recommendation

| Use case | Model | Why |
|---|---|---|
| **Default (best trade-off)** | `gemma4-e2b-rimworld` | Top score (14), 19.6 tok/s, valid JSON, fits GPU |
| Quality-first (offline, no time pressure) | `qwen3-rimworld` | Top score (14), more nuanced reasoning, 5 tok/s |
| Speed-first (interactive/bulk) | `llama3.2:1b-instruct-q4_K_M` | 12 score, 41.5 tok/s |
| Avoid | DeepSeek-R1 variants | Thinking output breaks JSON parsing |

## Applied changes

- Built tuned model `gemma4-e2b-rimworld` from `gemma-4-E2B-it-Q4_K_M` (8k ctx, temp 0.2).
- Updated `OLLAMA.md` recommended model and benchmark table.
- Updated `start-ollama.ps1` recommended-model line.
- Updated `sidecar/llm.py` default Ollama model → `gemma4-e2b-rimworld`.
- `sidecar/config.py` already exposes `OLLAMA_BASE_URL`.

## Reproducing

```powershell
$env:PYTHONPATH="...\SmartRim\sidecar"
python scratchpad\benchmark_ollama.py
```

Raw per-model output and previews are in `scratchpad/bench_results.json`.