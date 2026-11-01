# debrief.py — Debrief Generation

Generate markdown debrief from snapshots and advice logs.

## Function
```python
def generate_debrief(run_id: str, snapshots_dir: str, advice_log_path: str, output_path: str) -> str:
    # Returns path to generated debrief markdown
```

## Process
1. Load all daily snapshots for run
2. Load advice log entries
3. Build timeline with day-by-day summary
4. Include: alerts, resources, colonists, advice given
5. Write markdown to `memory/debriefs/{run_id}.md`

## Output Sections
- Run metadata (difficulty, storyteller, days)
- Day-by-day timeline
- Alert summary
- Advice log
- Resource trends

## CLI
```bash
python -m smartrim.debrief --run run-005
```

## Notes
- 201 lines
- Template-based, no LLM
- Used by `debrief_llm.py` as input