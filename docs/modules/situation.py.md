# situation.py — Situation Classifier + Lesson Retrieval

**Pure Python, no MCP/LLM dependencies — fully testable.**

## Core Functions

### Classification
| Function | Input | Output |
|----------|-------|--------|
| `classify_phase(snapshot_summary, alerts)` | snapshot, alerts | `phase: str` |
| `build_threats(alerts)` | alerts list | `set[str]` threat tags |
| `build_resources(snapshot_summary)` | snapshot | `set[str]` resource tags |
| `build_situation(snapshot_summary, alerts)` | snapshot, alerts | `dict` full situation |

### Situation Dict Schema
```python
{
    "phase": "early_survival" | "stabilization" | "raid_prep" | "expansion" | "crisis" | "any",
    "difficulty": "Peaceful" | "Community builder" | "Adventure story" | ... | "any",
    "storyteller": "Cassandra Classic" | "Phoebe Chillax" | "Randy Random" | "any",
    "biome": str | "any",
    "food_days": float | None,
    "medicine_count": int | None,
    "colonist_count": int | None,
    "threats": list[str],  # sorted
    "resources": list[str],  # sorted
}
```

### Enums (must sync with `schemas/lesson.schema.json`)
- `_PHASES_ENUM`: `early_survival`, `stabilization`, `raid_prep`, `expansion`, `crisis`, `any`
- `_THREATS_ENUM`: `colonist_downed`, `mood_break_risk`, `colonist_injured`, `danger_high`, `raid_incoming`, `predator_near_worker`, `low_food`, `medical_untreated`, `idle_colonists`, `threat_response`, `colony_death`, `other_game_alert`, `any`
- `_RESOURCES_ENUM`: `food_under_5_days`, `food_under_2_days`, `no_medicine`, `medicine_under_5`, `low_wood`, `low_steel`, `any`
- `_DIFFICULTY_ENUM`: `Peaceful`, `Community builder`, `Adventure story`, `Strive to survive`, `Blood and dust`, `Losing is fun`, `any`
- `_STORYTELLER_ENUM`: `Cassandra Classic`, `Phoebe Chillax`, `Randy Random`, `any`

### Lesson Retrieval
| Function | Description |
|----------|-------------|
| `load_lessons()` | Load all lessons from JSONL |
| `validate_lesson(lesson)` | Validate single lesson dict |
| `validate_all()` | Validate all lessons (CLI `validate`) |
| `retrieve(situation, lessons_list, limit=5)` | Match lessons to situation |
| `rank_actions(alerts, situation, lessons_list, limit=5)` | Rank actions from alerts + lessons |

### Retrieval Logic
1. For each alert → threat tag via `ALERT_TO_THREAT` + `GAME_ALERT_KEYWORDS`
2. Build mini-situation per threat
3. Query lesson store (SQLite FTS5 or JSONL fallback)
4. Score by: threat match > resource match > phase match > confidence
5. Return top N lessons

### CLI
```bash
python -m smartrim.situation validate    # Validate all lessons
python -m smartrim.situation reindex     # Rebuild SQLite FTS index
```

## Data Flow
```
MCP snapshots → normalize_snapshot() → build_situation() → retrieve() → rank_actions() → advice
```

## Notes
- 890 lines — consider splitting: `classifier.py`, `lesson_retrieval.py`, `action_ranker.py`, `validator.py`
- `ALERT_TO_THREAT` and `GAME_ALERT_KEYWORDS` map monitor alert categories to lesson threat tags
- Duplicate alert parsing logic exists in `monitor.run_reflex_checks()`