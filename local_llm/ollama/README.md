# Custom Ollama Models

Modelfiles for the RimWorld Counselor sidecar's tuned models. Both wrap an existing base model with optimized parameters for structured JSON debrief/analysis output. Created 2026-10-21.

## Tuned parameters (both models)

| Parameter | Value | Purpose |
|---|---|---|
| `num_ctx` | 8192 | Enough context for a full debrief bundle |
| `temperature` | 0.2 | Deterministic-ish, focused output |
| `top_p` | 0.9 | Nucleus sampling |
| `repeat_penalty` | 1.05 | Reduce repetition |
| `num_predict` | 2048 | Cap response length |

## Models

### `qwen3-rimworld` (quality-first)
- **Base:** `qwen3:8b` (8.2B params, Q4_K_M)
- **Benchmark:** score 14/14, 5.07 tok/s, 32.0s total
- **Notes:** Most nuanced reasoning of the top scorers. ~5 tok/s because the 8B model only partially fits in 4 GB VRAM (CPU/GPU split). Use when quality matters more than speed.

### `gemma4-e2b-rimworld` (recommended default — best speed/quality trade-off)
- **Base:** `gemma-4-E2B-it-Q4_K_M` (4.6B params, Q4_K_M)
- **Benchmark:** score 14/14, 19.60 tok/s, 35.2s total
- **Notes:** Tied top score at ~4x the speed of qwen3. Fits GPU well. Recommended default for the sidecar.

## Build

```powershell
# From this directory:
ollama create qwen3-rimworld -f Modelfile.qwen3-rimworld
ollama create gemma4-e2b-rimworld -f Modelfile.gemma4-e2b-rimworld
```

## Remove

```powershell
ollama rm qwen3-rimworld
ollama rm gemma4-e2b-rimworld
```

Base models (`qwen3:8b`, `gemma-4-E2B-it-Q4_K_M`) are not affected by removing these.

## Related

- `RimAutonomous/OLLAMA.md` — server config and usage
- `RimAutonomous/LLM_BENCHMARK.md` — full benchmark results and methodology
- `RimAutonomous/ollama/` — original Modelfile copies
- `RimAutonomous/sidecar/llm.py` — Python helper using these models