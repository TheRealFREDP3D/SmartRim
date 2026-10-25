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
   - The monitor displays a daily status + advice message in-game at configured hours (default: 6am and 6pm).
   - Configure hours via `SAY_DAILY_HOURS` env var (e.g., `SAY_DAILY_HOURS=6,12,18` for 3 messages/day).
   - Manual trigger: `python sidecar/say_daily.py` or `python sidecar/say_daily.py --slot evening`.

## Layout

- `src/smartrim/` - Python package (monitor, situation, lessons, outcomes, evaluate, debrief, llm, wiki)
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

## Tests

```
python -m pytest
```

See `PHASE2-KICKOFF.md` and `RUN-PROTOCOL.md` for evaluation protocol.
