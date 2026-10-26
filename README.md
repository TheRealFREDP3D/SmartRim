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
5. Validate lessons: `python -m smartrim.situation validate`
6. Start the reflex monitor: `.\start-monitor.ps1` (adviser on) or `.\start-monitor.ps1 -ObserveOnly`.
   - The monitor displays a daily status + advice message in-game at configured hours (default: 6am and 6pm).
   - Configure hours via `SAY_DAILY_HOURS` env var (e.g., `SAY_DAILY_HOURS=6,12,18` for 3 messages/day).
   - Manual trigger: `python -m smartrim.say_daily` or `python -m smartrim.say_daily --slot evening`.
7. Layer 2 reflex actor (opt-in): set `REFLEX_KILL=0` in `.env` to enable whitelisted actions
   (`draft-and-focus-fire`, `designate-firefighting`, `assign-beds-to-unassigned`). Default is
   `REFLEX_KILL=1` (all reflex actions dry-run only / disabled). Use `python cli.py reflex pause|resume|status`
   to manage the one in-game day pause. All reflex actions ship `dry_run: true` by default; set
   `REFLEX_DRY_RUN=0` to allow actual MCP writes.
   - `python cli.py reflex status` - show kill/dry-run/pause/lock/human-action state
   - `python cli.py reflex pause` - suspend reflex actions for one in-game day (cleared on day roll)
   - `python cli.py reflex resume` - clear the pause early
   - Human actions (`order_pawn`, `build`, `designate` via CLI) are recorded to
     `memory/last_human_action.json` and defer reflexes for 60 seconds.
   - Reflex actions are audited to `memory/actions.jsonl` (gitignored) and never touch
     `advice_log` or `auto_pauses`.

## Layout

- `src/smartrim/` - Python package (monitor, situation, lessons, outcomes, evaluate, debrief, llm, wiki, reflex_actor, reflex_preconditions)
- `sidecar/` - replay harness (`sidecar/replay.py`) and other one-off scripts
- `schemas/` - JSON schemas for lessons, advice, snapshots
- `memory/` - persistent knowledge base (lessons.jsonl, phases, wiki cache, run data)
- `tests/` - pytest suite
- `local_llm/ollama/` - Modelfiles for the tuned Ollama models (`gemma4-e2b-rimworld`, `qwen3-rimworld`)
- `scratchpad/` - one-off scripts (gitignored)

## Wiki cache

The cleaned markdown in `memory/wiki/*.md` is what the LLM reads and is tracked
in git. Raw HTML scrapes live in `memory/wiki/raw/` (gitignored) and exist only
to re-scrape or re-convert:

```powershell
python -m smartrim.wiki fetch     # download raw HTML into memory/wiki/raw/
python -m smartrim.wiki convert   # regenerate memory/wiki/*.md from the raw cache
```

## Runtime data

`memory/snapshots/`, `memory/debriefs/`, `memory/advice/`, `memory/alerts/`,
`memory/monitor.log` are gitignored. Archive completed runs by copying their
snapshot directory before starting a new run.

The following runtime files are also gitignored and written by the reflex actor:
`memory/actions.jsonl`, `memory/reflex.lock`, `memory/reflex_pause.json`,
`memory/last_human_action.json`.

## Tests

```
python -m pytest
```

See `PHASE2-KICKOFF.md` and `RUN-PROTOCOL.md` for evaluation protocol.
