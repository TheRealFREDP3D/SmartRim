# Ollama server — optimal setup for this machine

Hardware: Intel i7-6700K (4c/8t), 32 GB RAM, NVIDIA GTX 1050 Ti (4 GB VRAM).
Ollama 0.34.0, models stored on `D:\BACKUP\MODELS`.

## Recommended model (best speed/quality trade-off)

Benchmarked all installed chat models on a fixed RimWorld colony-review prompt (JSON output, 4k ctx, temp 0). Results: `scratchpad/bench_results.json`.

- **`gemma4-e2b-rimworld`** (custom, based on `gemma-4-E2B-it-Q4_K_M`) — **recommended default**.
  - Score 14/14 (valid JSON, 5/6 keyword hits), 19.6 tok/s, 35s total. ~4x faster than 8B models, fits GPU well.
  - Tuned: `num_ctx=8192`, `temperature=0.2`, `top_p=0.9`.
- Quality option: `qwen3-rimworld` (score 14, 5.1 tok/s) — more nuanced reasoning, slower.
- Speed option: `llama3.2:1b-instruct-q4_K_M` (score 12, 41.5 tok/s) — fastest usable.
- Avoid for structured JSON: all DeepSeek-R1 variants (thinking output, invalid JSON under this prompt).

### Benchmark results (sorted by score desc)

| Model | Score | tok/s | total_s | Notes |
|---|---|---|---|---|
| qwen3-rimworld | 14 | 5.1 | 32.0 | valid_json, kw5 |
| gemma-4-E2B-it-Q4_K_M | 14 | 19.6 | 35.2 | valid_json, kw5 |
| Mistral-7B-Instruct-v0.3 | 14 | 6.9 | 58.5 | valid_json, kw5 |
| qwen3:latest | 13 | 5.4 | 34.0 | valid_json, kw4 |
| Qwen3-1.7B-Q6_K | 13 | 24.2 | 22.8 | valid_json, kw4 |
| qwen2.5-coder:7b | 12 | 6.2 | 65.3 | valid_json, kw4, fences |
| llama3.2:1b-instruct-q4_K_M | 12 | 41.5 | 12.3 | valid_json, kw3 |
| llama-3.1:latest (4.9GB) | 11 | 6.7 | 57.8 | valid_json, kw3, fences |
| llama3.2:3b | 11 | 12.3 | 30.6 | valid_json, kw2 |
| gemma3:latest | 11 | 9.7 | 55.0 | valid_json, kw3, fences |
| gemma-3-1B-it-QAT | 10 | 34.5 | 13.4 | valid_json, kw2, fences |
| gemma3:1b | 10 | 29.4 | 16.0 | valid_json, kw2, fences |
| qwen2.5:1.5b | 10 | 26.2 | 16.8 | valid_json, kw2, fences |
| Phi-4-mini-reasoning | 0 | 8.9 | 90.4 | invalid_json (thinking) |
| DeepSeek-R1-Distill-Llama-8B | 0 | 5.5 | 172.4 | invalid_json |
| deepseek-r1:8b | -1 | 5.4 | 132.0 | invalid_json |
| DeepSeek-R1-0528-Qwen3-8B | -1 | 4.9 | 160.2 | invalid_json |
| deepseek-r1:1.5b | -1 | 24.0 | 35.0 | invalid_json |
| llama3.2-vision:latest | — | — | — | HTTP 500 (OOM/too large)

## Tuned environment variables (persisted at user level)

| Var | Value | Why |
|---|---|---|
| `OLLAMA_FLASH_ATTENTION` | 1 | Faster attention, enables q8_0 KV cache |
| `OLLAMA_KV_CACHE_TYPE` | q8_0 | ~2x KV memory savings vs f16 |
| `OLLAMA_NUM_PARALLEL` | 1 | Single user; avoids splitting VRAM |
| `OLLAMA_MAX_LOADED_MODELS` | 2 | Chat + embedder kept hot |
| `OLLAMA_KEEP_ALIVE` | 30m | Avoid reload latency |
| `OLLAMA_NUM_GPU` | 999 | Offload as many layers as VRAM allows |
| `OLLAMA_DEBUG` | 0 | Reduce overhead |
| `OLLAMA_ORIGINS` | * | Allow local clients |
| `OLLAMA_HOST` | 127.0.0.1:11434 | Local only |
| `OLLAMA_MODELS` | D:\BACKUP\MODELS | Model storage |

## Usage

```powershell
.\start-ollama.ps1     # apply env + start server
.\stop-ollama.ps1      # stop server
```

From Python sidecar:
```python
from llm import generate
text = generate("your prompt", provider="ollama", model="qwen3-rimworld", think=False)
```

## Notes

- 8B models only partially fit in 4 GB VRAM; expect ~40-60% GPU offload. For fully-GPU speed use 3B/1B models.
- `think=False` disables qwen3 chain-of-thought for faster structured output.
- Context beyond 8k requires more VRAM; raise `num_ctx` only if you switch to a smaller model or quant.