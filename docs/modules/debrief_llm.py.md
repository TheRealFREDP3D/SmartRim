# debrief_llm.py — LLM Debrief Analysis

Sends debrief bundle to LLM, validates structured output, writes candidate lessons.

## Main Function
```python
def analyze_debrief(bundle_text, model=None, temperature=0.3, system=None, task="debrief", provider=None):
    # Returns analysis dict or raw text on failure
```

## Flow
1. Send bundle to LLM with system prompt (v3 bundle includes its own contract)
2. Extract JSON from ```json fence
3. Validate Section A (lesson candidates) with Pydantic schema
4. On schema failure: retry once with error prompt (max 3 attempts)
5. Write analysis to `memory/debriefs/{run_id}-llm.md`
6. Write candidate lessons to `memory/candidates/{run_id}-lessons.jsonl`

## Schemas (Pydantic)

### `TriggerCandidate`
```python
phases: list[PHASES_T]
threats: list[THREATS_T]
resources: list[RESOURCES_T]
difficulty: "any" | DIFFICULTY_T | list[DIFFICULTY_T] = "any"
storyteller: "any" | STORYTELLER_T | list[STORYTELLER_T] = "any"
biome: "any" | str | list[str] = "any"
```

### `LessonCandidate`
```python
title: str
cause_chain: list[str]
trigger: TriggerCandidate
recommendation: str
rationale: str
source: list[str]
wiki_pages_used: list[str]
unverified_claims: list[str]
confidence: float  # 0.3-0.7
```

## Retry Logic
- `@retry` on transport errors (timeout, connection, JSON decode)
- Schema validation failure → rebuild prompt with `TRIGGER_VOCAB` (allowed enum values) + error message
- Max 3 schema retries

## CLI
```bash
python -m smartrim.debrief_llm --run run-005
python -m smartrim.debrief_llm path/to/bundle.md --model gemma4-e2b-rimworld
```

## Output Files
- `memory/debriefs/{run_id}-llm.md` — full analysis
- `memory/candidates/{run_id}-lessons.jsonl` — validated LessonCandidate objects

## Notes
- 435 lines
- Uses `smartrim.llm.generate()` with `num_ctx=16384`
- `BUNDLE_MAX_CHARS = 65000`
- `SCHEMA_RETRY_ATTEMPTS = 3`