# advice_log.py — Append-Only Advice Log with Outcome Tracking

JSONL file: `memory/advice/advice.jsonl` (tracked in git, 282KB).

## Record Schema

```json
{
  "id": "adv-<timestamp>-<random>",
  "run_id": "run-005",
  "snapshot_day": "day_10",
  "trigger": "scheduled" | "reflex",
  "severity": "info" | "warning" | "urgent",
  "situation": "Description...",
  "actions": [{"rank": 1, "action": "...", "rationale": "..."}],
  "risks": [{"label": "...", "severity": "urgent"}],
  "linked_lessons": ["lesson-id-1", "lesson-id-2"],
  "reflex_name": "draft-and-focus-fire",
  "auto_paused": false,
  "outcome": null,
  "outcome_note": null,
  "event_cause": null,
  "timestamp": "2026-10-30T12:00:00"
}
```

## Functions

| Function | Purpose |
| ---------- | --------- |
| `log_advice(...)` | Append new advice record |
| `update_outcome(advice_id, outcome, note)` | Close advice with outcome |
| `set_event_cause(advice_id, cause)` | Set root cause |
| `set_cause_matching(pattern, cause)` | Bulk set cause by regex |
| `find_open_duplicate(run_id, situation)` | Dedup: find open advice with same situation |
| `read_advice(run_id=None)` | Load all/filtered records |

## Outcome Values

- `helped` — advice resolved the issue
- `failed` — advice didn't help
- `obsolete` — situation resolved on its own
- `unknown` — insufficient data

## File Operations

**FIXED**: Atomic rewrites using `.tmp` + `os.replace` pattern (like `cli.py`).

- `update_outcome()` line ~80
- `set_event_cause()` line ~109
- `set_cause_matching()` line ~138

## Notes

- 199 lines
- Used by monitor (`_log_scheduled`, `_log_urgent`) and outcomes
- Deduplication prevents spam on monitor restart
