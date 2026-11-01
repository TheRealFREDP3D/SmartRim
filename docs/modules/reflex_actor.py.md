# reflex_actor.py — Layer 2 Reflex Actor

**Whitelisted, guarded, audited in-game actions. Defaults to dry-run.**

## Safety Order (per action)
1. `REFLEX_KILL` env (master kill switch)
2. `REFLEX_PAUSE` (one in-game day pause via CLI)
3. `REFLEX_LOCK` (PID file prevents concurrent execution)
4. Human action window (60s after `cli.py` human action)
5. Preconditions (from YAML)
6. Dry-run (global `REFLEX_DRY_RUN` or per-action YAML)
7. Say intent (in-game message)
8. Execute MCP write
9. Audit record → `memory/actions.jsonl`

## Configuration
- `memory/reflex_actions.yaml` — whitelist (see below)
- Env vars: `REFLEX_KILL=1` (disable), `REFLEX_DRY_RUN=1` (default), `REFLEX_PAUSE=1`

## ReflexAction (dataclass)
```python
id: str                    # "draft-and-focus-fire"
action_type: str           # "draft_and_focus_fire"
label_contains: list[str]  # alert keywords to match
category: str | None       # alert category to match
dry_run: bool              # per-action override (currently IGNORED - BUG)
kill_switch_env: str       # "REFLEX_KILL"
preconditions: list[str]   # names from reflex_preconditions.PRECONDITIONS
```

## YAML Whitelist (`memory/reflex_actions.yaml`)
| Action ID | Type | Trigger | Preconditions | Dry-run |
|-----------|------|---------|---------------|---------|
| `draft-and-focus-fire` | `draft_and_focus_fire` | raid/enemy/attack | `has_raid_alert`, `has_shooter_above_5`, `none_drafted` | false |
| `designate-firefighting` | `designate_firefighting` | fire | `has_fire_alert` | true |
| `assign-beds-to-unassigned` | `assign_beds` | idle_colonist | `has_unassigned_colonist` | true |
| `rescue-downed` | `rescue_downed` | downed/incapacitated | `has_downed_colonist` ❌ MISSING | true |
| `prioritize-treatment` | `prioritize_treatment` | wounded/bleeding | `has_wounded_colonist` ❌ MISSING | true |

## ReflexActor Class

### Guards
| Method | Check |
|--------|-------|
| `_paused(current_day)` | Read `memory/reflex_pause.json`, clear on day roll |
| `_acquire_lock()` | PID lock `memory/reflex.lock` |
| `_human_recent()` | Check `memory/last_human_action.json` < 60s |
| `_dry_run(action)` | **BUG**: ignores `action.dry_run`, only reads `REFLEX_DRY_RUN` env |
| `_preconditions_pass(action, game_state)` | All precondition functions return True |
| `_already_acted(alert_id, action_type)` | Check `memory/actions.jsonl` for duplicate |

### Execution
| Action Type | Executor | Status |
|-------------|----------|--------|
| `draft_and_focus_fire` | `_exec_draft()` | ✅ Works |
| `designate_firefighting` | `_exec_firefighting()` | ❌ Returns False (no fire cell in alert) |
| `assign_beds` | `_exec_assign_beds()` | ❌ Returns False (no bed IDs in alert) |
| `rescue_downed` | **Not wired** | ❌ Missing in `_execute()` |
| `prioritize_treatment` | **Not wired** | ❌ Missing in `_execute()` |

### Entry Point
```python
def evaluate(alerts, situation, game_state, current_day=None) -> list[dict]:
    # For each action in whitelist:
    #   1. Match alerts
    #   2. Run all guards
    #   3. Check preconditions
    #   4. Say intent
    #   5. Dry-run or execute
    #   6. Write audit record
```

## Audit Record (`memory/actions.jsonl`)
```json
{
  "timestamp": "...",
  "run_id": "...",
  "alert_id": "category|message",
  "action": "draft_and_focus_fire",
  "action_id": "draft-and-focus-fire",
  "precondition_result": true,
  "dry_run": true,
  "executed": false,
  "outcome_check_at": null,
  "outcome_status": null,
  "say": "SmartRim: drafting John, Jane to focus fire (Raid incoming)"
}
```

## Outcome Closing
```python
close_action_outcomes(snapshot_summary, run_id)
# Reuses outcomes._close_advice() on executed actions
```

## Known Bugs (from TODO.md)
1. `_dry_run()` ignores per-action YAML config
2. Unknown preconditions (`has_downed_colonist`, `has_wounded_colonist`) silently pass
3. Two actions lack executors (`designate_firefighting`, `assign_beds`)
4. Two actions not wired in `_execute()` (`rescue_downed`, `prioritize_treatment`)

## Notes
- 575 lines
- `EXECUTE_ACTIONS = ("draft_and_focus_fire", "designate_firefighting", "assign_beds")` but only first works
- Uses `counselor` module for MCP writes