# monitor.py — Colony Monitoring Loop (Heart of Sidecar)

**860 lines — the main polling loop. Does too many things (god module).**

## Main Entry
```python
def main() -> None:
    # 1. Setup logging
    # 2. Parse --observe-only / OBSERVE_ONLY env
    # 3. Acquire PID lock (memory/monitor.pid)
    # 4. Create McpClient
    # 5. Loop: poll_once() every POLL_INTERVAL seconds
```

## State: `PollResult` (dataclass)
Mutated and returned each poll iteration:
```python
last_day: str | None
snapshotted_day: str | None
last_say_day: str | None
last_say_hour: int | None
consecutive_errors: int
poll_count: int
urgent_alerts: int
auto_pauses: int
reflex_snapshots: int
run_ended: bool
last_sig: Any | None  # alert signature for dedup
```

## `poll_once(client, state) → PollResult`

### Flow
1. **Ensure dirs** → `ensure_dirs()`
2. **Get conditions** → if MCP unreachable, increment errors, write alert after 5 failures
3. **Check run end** → if `daysPassed >= RUN_DAYS`, write run-end marker, pause (if not observe-only), stop
4. **Daily say** → at `SAY_DAILY_HOURS`, call `_say_daily_message()` (briefly unpauses to render)
5. **Day roll** → new day → write snapshot, close outcomes (advice + reflex), log scheduled advice
6. **Reflex checks** → `run_reflex_checks(client)` → writes `memory/alerts/current.json`
7. **Alert signature dedup** → compare to `last_sig`, save new
8. **Urgent alerts** → if any:
   - Display via `_say_visible()` (unpauses briefly)
   - Log urgent advice (`_log_urgent()`)
   - Auto-pause game (`set_speed pause`)
   - Write reflex snapshot (`write_reflex_snapshot()`)
   - Invoke reflex actor (`_REFLEX_ACTOR.evaluate()`)
   - Check for colony death → write run-end marker

## Key Functions

| Function | Purpose |
|----------|---------|
| `run_reflex_checks(client)` | Health/mood/downed/alerts/resources checks → list of alert dicts |
| `normalize_snapshot(snapshot)` | Add computed `summary` dict (food_days, min_mood, etc.) |
| `write_snapshot(client, day_label, ...)` | Full MCP snapshot to JSON |
| `write_reflex_snapshot(client, ...)` | Incident snapshot (capped at 40/run) |
| `_say_visible(client, text)` | Unpause → say → restore pause |
| `_say_daily_message(client, conditions, slot)` | Build + display daily status+advice |
| `_log_scheduled / _log_urgent` | Write to advice_log |
| `_advice_context(client, ...)` | Build situation + ranked actions + linked lessons |
| `write_run_end(client, ...)` | Final snapshot + run marker |
| `run_length_reached(days_passed)` | Check if RUN_DAYS reached |
| `adviser_acts(observe_only)` | True if adviser mode (not observe-only) |
| `configure_observe_only(argv)` | Parse CLI --observe-only / --advise |

## Locking
- PID file: `memory/monitor.pid`
- Stale PID detection (Windows via `ctypes`, Unix via `os.kill(pid, 0)`)

## Alert Categories (from `run_reflex_checks`)
- `downed`, `mood_extreme`, `mood_major`, `mood_minor`, `health`
- `danger_rating`, `idle_colonist`, `medical_treatment_needed`, `food_low`
- `game_alert` (with urgent keyword check), `medicine_low`, `sleeping_during_threat`, `colony_death`

## Notes
- **Too large** — split into: `monitor_loop.py`, `snapshotter.py`, `alert_analyzer.py`, `daily_say.py`, `reflex_coordinator.py`
- `SAY_DAILY_USE_LLM` accessed via `globals().get()` hack (not imported)
- Dual alert processing: here + `situation.build_threats()`