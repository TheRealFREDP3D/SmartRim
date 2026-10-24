# LLM Implementation Guide for SmartRim

## Overview

SmartRim uses a local LLM (Ollama) to enhance colony advisory capabilities. The
default model is `gemma4-e2b-rimworld` (3.1 GB, custom fine-tuned for RimWorld).
All LLM features degrade gracefully if Ollama is unavailable.

## Current LLM Infrastructure

| Component | File | Status |
|-----------|------|--------|
| LLM helper | `sidecar/llm.py` | Ollama support, default model `gemma4-e2b-rimworld` |
| Config | `sidecar/config.py` | `LLM_PROVIDER`, `LLM_MODEL`, `OLLAMA_BASE_URL`, `SAY_DAILY_USE_LLM` |
| Debrief | `sidecar/debrief.py` | Generates template only (no LLM call) |
| Situation | `sidecar/situation.py` | Pure rule-based (explicitly "No LLM") |
| Counselor | `sidecar/counselor.py` | Tool library only, no LLM interaction |
| Monitor | `sidecar/monitor.py` | `_advice_context` uses rules, not LLM |

## Files Created

### `sidecar/debrief_llm.py`
Auto-analyze debrief bundles via LLM. Replaces the manual paste-into-model step.

**Usage:**
```powershell
python sidecar/debrief_llm.py --run run-005-adv-cassandra
python sidecar/debrief_llm.py memory/debriefs/run-005-adv-cassandra.md
python sidecar/debrief_llm.py --run run-005-adv-cassandra --no-write  # stdout only
```

**Features:**
- Reads debrief bundle markdown
- Sends to Ollama with structured analysis prompt
- Outputs JSON: cause, worked (list), lessons (list of {trigger, recommendation, rationale, confidence}), next_colony
- Writes analysis to `memory/debriefs/<run>-llm.md`

### `sidecar/chat.py`
Interactive colony Q&A chat using local LLM.

**Usage:**
```powershell
python sidecar/chat.py
python sidecar/chat.py --model gemma4-e2b-rimworld
python sidecar/chat.py --say  # Display answers in-game
```

**Commands:** `quit`/`exit`, `status` (refresh colony state), `say` (display last answer in-game)

## Files Modified

### `sidecar/llm.py`
Already had Ollama support. Default model set to `gemma4-e2b-rimworld`.

### `sidecar/config.py`
Added:
- `SAY_DAILY_USE_LLM` env var (`SAY_DAILY_USE_LLM=1` to enable LLM advice)

### `sidecar/say_daily.py`
Added:
- `build_llm_advice()` function — generates advice via Ollama instead of rule-based heuristics
- `--llm` CLI flag — `python sidecar/say_daily.py --llm`
- Falls back to rule-based advice if LLM unavailable

### `sidecar/monitor.py`
- Imported `say_daily` module
- Added `_say_daily_message()` function
- Added tracking variables (`last_say_day`, `last_say_hour`)
- In main loop: checks if current hour is in `SAY_DAILY_HOURS` and triggers daily say
- Passes `use_llm` from config

### `README.md`
Documented the daily say feature and configuration.

## 5 Integration Points (Priority Order)

| # | Feature | File | Effort | Value | Latency |
|---|---------|------|--------|-------|---------|
| 1 | Auto-debrief analysis | `debrief_llm.py` | Low | High | None (offline) |
| 2 | Interactive chat | `chat.py` | Low | Medium | On-demand |
| 3 | LLM daily advice | `say_daily.py --llm` | Medium | Medium | ~3-8s/day |
| 4 | Auto-lesson generation | (add to monitor on run end) | Medium | High | None (offline) |
| 5 | Threat narrative on urgent alerts | (add to `_log_urgent`) | Medium | Medium | ~2-5s/alert |

## Configuration

Update `.env`:
```env
LLM_PROVIDER=ollama
LLM_MODEL=gemma4-e2b-rimworld
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=gemma4-e2b-rimworld

# Daily say (optional LLM advice)
SAY_DAILY_HOURS=6,18
SAY_DAILY_USE_LLM=1
```

## Quick Start

```powershell
# 1. Ensure Ollama is running
ollama serve

# 2. Test the LLM
python sidecar/llm.py "Summarize: colony on day 5, 3 colonists, low food"

# 3. Auto-debrief (after a run completes)
python sidecar/debrief.py run-005-adv-cassandra
python sidecar/debrief_llm.py --run run-005-adv-cassandra

# 4. Interactive chat
python sidecar/chat.py

# 5. Daily status with LLM advice
python sidecar/say_daily.py --llm

# 6. Enable LLM advice in monitor (restart required)
$env:SAY_DAILY_USE_LLM = "1"
$env:RUN_ID = "run-005-adv-cassandra"
.\start-monitor.ps1
```

## Key Design Principles

1. **Keep the reflex layer deterministic** — The monitor's fast polling (mood, health, alerts) must NOT call the LLM. LLM calls are too slow (2-10s) for 30-second polling.
2. **LLM is advisory, not authoritative** — Rule-based alerts still fire. LLM adds context and narrative on top.
3. **Offline-friendly** — All features degrade gracefully if Ollama is down. Use try/except everywhere.
4. **Use `num_ctx` wisely** — The e2b model has limited context. Keep prompts under 4K tokens for daily advice, 16K for debriefs.
5. **Temperature** — Use 0.2-0.3 for factual analysis (debriefs), 0.4-0.5 for creative advice.

## Recommended Next Steps

1. **Test `debrief_llm.py`** on an existing debrief bundle to validate output quality
2. **Test `chat.py`** for interactive colony Q&A
3. **Enable `SAY_DAILY_USE_LLM=1`** in monitor for richer daily advice
4. **Implement auto-lesson generation** (add LLM call to monitor's run-end handler)
5. **Fine-tune the model** if advice quality needs improvement (add more RimWorld-specific training data)

## Model Details

- **Model**: `gemma4-e2b-rimworld` (3.1 GB)
- **Base**: Gemma 4 E2B (quantized Q4_K_M)
- **Fine-tuned for**: RimWorld colony management, threat assessment, survival advice
- **Context window**: 8192 tokens (configurable up to 16384)
- **Temperature range**: 0.2 (factual) to 0.5 (creative)
- **Inference time**: ~2-5s for short prompts, ~10-30s for long analysis

## Auto-Lesson Generation (Not Yet Implemented)

When a run completes, the LLM can analyze the debrief and propose candidate lessons.
These go into `memory/candidates/` for human review before merging into `lessons.jsonl`.

To implement, add to `monitor.py` after `write_run_end()`:

```python
try:
    import debrief_llm
    from debrief import generate_debrief
    generate_debrief(snapshot_dir_for(run_id), DEBRIEFS_DIR, run_id)
    bundle_path = os.path.join(DEBRIEFS_DIR, f"{run_id}.md")
    with open(bundle_path) as f:
        bundle = f.read()
    analysis = debrief_llm.analyze_debrief(bundle)
    cand_path = os.path.join(CANDIDATES_DIR, f"{run_id}-llm.md")
    with open(cand_path, "w") as f:
        f.write(f"# LLM Candidate Lessons: {run_id}\\n\\n{json.dumps(analysis, indent=2)}\\n")
    print(f"LLM candidate lessons: {cand_path}")
except Exception as e:
    print(f"LLM lesson generation failed: {e}")
```

## Threat Narrative (Not Yet Implemented)

In `monitor.py`, in the `_log_urgent` function, add:

```python
try:
    from llm import generate
    situation_text = "; ".join(a.get("message", "") for a in urgent)
    narrative = generate(
        f"Colony threat: {situation_text}. Write a 1-2 sentence urgent alert for the player.",
        provider="ollama", model="gemma4-e2b-rimworld",
        system="You are a RimWorld threat announcer. Be urgent but calm. Max 2 sentences.",
        temperature=0.3, num_ctx=2048
    )
    client.call_tool("say", {"text": f"Threat: {narrative}"})
except Exception:
    pass
```
