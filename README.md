# SmartRim

SmartRim is an autonomous RimWorld sidecar. It observes colony state over the
RimMolt MCP server, keeps a persistent lesson store, and advises (or pauses) on
threats.

**RimMolt** is an MCP (Model Context Protocol) server mod for RimWorld that exposes
game state via a local HTTP API. Get it from: [Steam Workshop](https://steamcommunity.com/sharedfiles/filedetails/?id=3796006886)

- **MCP config for RimWorld**: `.mcp.json` (rimmolt @ localhost:8787)

## Getting started

1. Install Python 3.11+.
2. Run the installer (creates a venv automatically if none exists):
   - **Windows**: `.\install.ps1`
   - **Linux/macOS**: `./install.sh`
3. Copy `.env.example` to `.env` and adjust values.
4. Start RimWorld with the RimMolt mod (MCP server on localhost:8787).
5. Run tests: `python -m pytest`
6. Validate lessons: `python -m smartrim.situation validate`
7. Start the reflex monitor:
   - **Windows**: `.\start-monitor.ps1` (adviser on) or `.\start-monitor.ps1 -ObserveOnly`
   - **Linux/macOS**: `./start-monitor.sh` (adviser on) or `./start-monitor.sh --observe-only`
   - The monitor displays a daily status + advice message in-game at configured hours (default: 6am and 6pm).
   - Configure hours via `SAY_DAILY_HOURS` env var (e.g., `SAY_DAILY_HOURS=6,12,18` for 3 messages/day).
   - Manual trigger: `python -m smartrim.say_daily` or `python -m smartrim.say_daily --slot evening`.
8. (Optional) Start the Streamlit dashboard:
   - First install dashboard dependencies: `pip install -e ".[dashboard]"`
   - **Windows**: `.\start-dashboard.ps1` or `streamlit run src/smartrim/dashboard.py`
   - **Linux/macOS**: `./start-dashboard.sh` or `streamlit run src/smartrim/dashboard.py`
9. Layer 2 reflex actor (opt-in): set `REFLEX_KILL=0` in `.env` to enable whitelisted actions
   (`draft-and-focus-fire`, `designate-firefighting`, `assign-beds-to-unassigned`). Default is
   `REFLEX_KILL=1` (all reflex actions dry-run only / disabled).    Use `python -m smartrim.cli reflex pause|resume|status`
   to manage the one in-game day pause. All reflex actions ship `dry_run: true` by default; set
   `REFLEX_DRY_RUN=0` to allow actual MCP writes.
   - `python -m smartrim.cli reflex status` - show kill/dry-run/pause/lock/human-action state
   - `python -m smartrim.cli reflex pause` - suspend reflex actions for one in-game day (cleared on day roll)
   - `python -m smartrim.cli reflex resume` - clear the pause early
   - Human actions (`order_pawn`, `build`, `designate` via CLI) are recorded to
     `memory/last_human_action.json` and defer reflexes for 60 seconds.
   - Reflex actions are audited to `memory/actions.jsonl` (gitignored) and never touch
     `advice_log` or `auto_pauses`.

## Layout

- `src/smartrim/` - Python package (monitor, situation, lessons, outcomes, evaluate, debrief, llm, wiki, reflex_actor, reflex_preconditions, cli, counselor, config, mcp_client, say_daily, quests, replay, advice_log, debrief_llm, debrief_bundle, eval_models, logging_config)
- `schemas/` - JSON schemas for lessons, advice, snapshots
- `docs/local_llm/ollama/` - Modelfiles for the tuned Ollama models (`gemma4-e2b-rimworld`, `qwen3-rimworld`)
- `memory/` - persistent knowledge base (lessons.jsonl, phases, wiki cache, run data)
- `tests/` - pytest suite
- `*.ps1` / `*.sh` - Cross-platform installer and launcher scripts
- `scratchpad/` - optional one-off scripts (gitignored; create if needed)

## Wiki cache

The cleaned markdown in `memory/wiki/*.md` is what the LLM reads and is tracked
in git. Raw HTML scrapes live in `memory/wiki/raw/` (gitignored) and exist only
to re-scrape or re-convert:

```bash
python -m smartrim.wiki fetch     # download raw HTML into memory/wiki/raw/
python -m smartrim.wiki convert   # regenerate memory/wiki/*.md from the raw cache
```

## Runtime data

`memory/snapshots/`, `memory/debriefs/`, `memory/alerts/`,
`memory/monitor.log` are gitignored. Archive completed runs by copying their
snapshot directory before starting a new run.

The following runtime files are also gitignored and written by the reflex actor:
`memory/actions.jsonl`, `memory/reflex.lock`, `memory/reflex_pause.json`,
`memory/last_human_action.json`.

## Tests

```shell
python -m pytest
```

See `memory/phases.md` and `RUN-PROTOCOL.md` for evaluation protocol.

## License

MIT License - see [LICENSE](LICENSE) for details.
