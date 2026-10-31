# outcomes.py — Outcome Tracking & Lesson Confidence Updates

Closes open advice records at each daily snapshot and updates lesson confidence.

## Function
```python
def close_outcomes(snapshot_summary: dict, run_id: str) -> int:
    # Returns number of advice records closed
```

## Logic
1. Load all advice for `run_id` from `advice_log`
2. For each open record (no outcome):
   - Call `_close_advice(advice, snapshot_summary)`
   - Heuristic: check if situation risks resolved in snapshot
   - Update advice record with outcome + note
3. For each linked lesson in closed advice:
   - Update `times_applied`, `times_helped`, `times_failed`
   - Recalculate `confidence` (Wilson score interval)
   - Write back to `lessons.jsonl`

## `_close_advice(advice, snapshot_summary) → (outcome, note)`
| Condition | Outcome | Note |
|-----------|---------|------|
| Downed colonist now healthy | `helped` | "Colonist recovered" |
| Mood improved above threshold | `helped` | "Mood recovered" |
| Food days > 5 | `helped` | "Food secured" |
| Medicine > 5 | `helped` | "Medicine stocked" |
| Raid alert gone | `helped` | "Threat passed" |
| Fire alert gone | `helped` | "Fire extinguished" |
| Still critical | `failed` | "Situation unchanged" |
| No matching risk in snapshot | `obsolete` | "Situation resolved" |

## Lesson Confidence Update
```python
# Wilson score interval for binomial proportion
# times_helped / times_applied with 95% CI
# confidence = lower_bound * 0.7 + upper_bound * 0.3
```

## File Operations
**BUG**: Non-atomic rewrites (2 locations):
- `_write_advice()` line ~30
- `_write_lessons()` line ~48

## Notes
- 193 lines
- Called by `monitor.poll_once()` on day roll
- Also called by `reflex_actor.close_action_outcomes()` for reflex actions