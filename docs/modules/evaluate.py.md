# evaluate.py — Phase 2 Evaluation Harness

Summarize and compare runs for evaluation protocol.

## Commands
```bash
python -m smartrim.evaluate summarize --run run-005
python -m smartrim.evaluate compare --runs run-001 run-002 run-003
```

## Functions

| Function | Purpose |
|----------|---------|
| `summarize_run(run_dir)` | Single run summary |
| `arm_summary(runs, arm)` | Aggregate stats per arm (on/off/reflex) |
| `format_table(rows)` | Render comparison table |
| `render_report(runs)` | Full evaluation report |
| `cmd_summarize(args)` | CLI summarize |
| `cmd_compare(args)` | CLI compare |

## Summary Metrics
- Days survived
- Final colonist count
- Food days remaining
- Medicine count
- Wealth
- Urgent alerts count
- Auto-pauses
- Reflex snapshots
- Stop reason (run_length / colony_death)
- First break day
- First food crisis day

## Data Sources
- `memory/runs/{run_id}.end.json` — run marker
- `memory/snapshots/{run_id}/day-*.json` — daily snapshots
- `memory/advice/advice.jsonl` — advice log (filtered by run_id)

## Notes
- 462 lines
- Used by `RUN-PROTOCOL.md` evaluation
- Outputs markdown tables for comparison