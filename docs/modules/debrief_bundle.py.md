# debrief_bundle.py — AI-Ready Debrief Bundle (v3)

Builds structured markdown bundle for LLM analysis. Template-only, no API calls.

## Function
```python
def build_bundle(run_id: str, snapshots_dir: str, advice_log_path: str, wiki_dir: str) -> str:
    # Returns bundle markdown text
```

## Bundle Structure (v3)
```
# Section 1: Run Metadata
# Section 2: Day-by-Day Timeline
# Section 3: Resource Trends
# Section 4: Colonist Roster
# Section 5: Alert Summary
# Section 6: Advice Log with Causes
# Section 7: Advice Causes (detailed)
# Section 8: Task & Output Contract
```

## Key Helpers
| Function | Purpose |
|----------|---------|
| `_load_wiki_facts()` | Load relevant wiki markdown |
| `_parse_day(snapshot)` | Extract day number from snapshot |
| `_timeline(snapshots)` | Build chronological summary |
| `_advice_section(advice)` | Format advice with outcomes |
| `_food_units(resources)` | Normalize food to meal units |
| `_quest_records(snapshots)` | Extract quest progress |
| `_event_digest(snapshots)` | Summarize incidents |
| `_derive_outcome(run_marker)` | Determine win/loss/abandoned |

## Section 8: Task Contract
Tells LLM exactly what to output:
- PRIMARY CAUSE (1-2 sentences)
- WHAT WORKED (bullets)
- LESSONS (3-5 objects with trigger, recommendation, rationale, confidence 0.3-0.8)
- NEXT COLONY (2-3 sentences)
- Output as JSON with keys: `cause`, `worked`, `lessons`, `next_colony`

## Constants
- `BUNDLE_MAX_CHARS = 65000` (fits num_ctx=16384)

## Notes
- 564 lines
- Used by `debrief_llm.py` as input
- Bundle includes wiki facts for grounding