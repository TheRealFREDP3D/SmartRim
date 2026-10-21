# SmartRim

SmartRim is an autonomous RimWorld sidecar. It observes colony state over the
RimMolt MCP server, keeps a persistent lesson store, and advises (or pauses) on
threats. This directory is the git repository and contains the sidecar, schemas,
memory, and tests.

## Repository boundary

- **Repository root**: `SmartRim\` (this directory; git repo)
- **MCP config for RimWorld**: `SmartRim/.mcp.json` (rimmolt @ localhost:8787)

## Getting started

1. Install Python 3.13+ and create a venv (optional; global Python works for tests).
2. Copy `.env.example` to `.env` and adjust values.
3. Start RimWorld with the RimMolt mod (MCP server on localhost:8787).
4. Run tests: `python -m pytest`
5. Validate lessons: `python sidecar/lessons.py validate`
6. Start the reflex monitor: `.\start-monitor.ps1` (adviser on) or `.\start-monitor.ps1 -ObserveOnly`.

## Layout

- `sidecar/` - Python sidecar (monitor, situation, lessons, outcomes, evaluate, debrief)
- `schemas/` - JSON schemas for lessons, advice, snapshots
- `memory/` - persistent knowledge base (lessons.jsonl, phases, wiki cache, run data)
- `tests/` - pytest suite
- `scratchpad/` - one-off scripts (gitignored)

## Runtime data

`memory/snapshots/`, `memory/debriefs/`, `memory/advice/`, `memory/alerts/`,
`memory/monitor.log` are gitignored. Archive completed runs by copying their
snapshot directory before starting a new run.

## Tests

```
python -m pytest
```

See `PHASE2-KICKOFF.md` and `RUN-PROTOCOL.md` for evaluation protocol.
