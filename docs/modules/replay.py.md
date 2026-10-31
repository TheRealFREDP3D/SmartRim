# replay.py — Replay Harness for Reflex Actions

Records MCP calls during monitor run, replays them offline to test reflex logic.

## Purpose
- Record: Monitor writes snapshots with full MCP responses
- Replay: Feed snapshots to `ReflexActor` without live MCP server
- Compare: Reflex decisions vs actual game outcomes

## Main Class: `MockCounselor`
Mimics `counselor` module but reads from snapshot files instead of MCP.

```python
class MockCounselor:
    def __init__(self, snapshots_dir: str):
        self.snapshots = sorted(glob.glob(f"{snapshots_dir}/day-*.json"))
        self.index = 0
    
    def game_state(self) -> dict:
        # Return current snapshot as game_state format
    
    def call_tool(self, name, args) -> dict:
        # Return recorded response from snapshot
```

## Functions
| Function | Description |
|----------|-------------|
| `run_replay(snapshots_dir, reflex_actions_path)` | Run reflex actor on recorded snapshots |
| `main()` | CLI entry point |

## CLI
```bash
python -m smartrim.replay memory/snapshots/run-005
python -m smartrim.replay --actions memory/reflex_actions.yaml memory/snapshots/run-005
```

## Output
- Per-snapshot reflex decisions
- Actions that would have fired
- Precondition pass/fail
- Comparison with actual `memory/actions.jsonl`

## Notes
- 231 lines
- Used for regression testing reflex logic
- `sidecar/replay.py` is a duplicate entry point