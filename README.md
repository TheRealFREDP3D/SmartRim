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
8. (Optional) Start the Streamlit dashboard (now opens on the **Command Center** view):
   - First install dashboard dependencies: `pip install -e ".[dashboard]"`
   - **Windows**: `.\start-dashboard.ps1` or `streamlit run src/smartrim/dashboard.py`
   - **Linux/macOS**: `./start-dashboard.sh` or `streamlit run src/smartrim/dashboard.py`

12. (Optional) Start the terminal UI (TUI):
   - First install TUI dependencies: `pip install -e ".[tui]"` (or `pip install textual`)
   - **Windows**: `.\start-tui.ps1` or `python -m smartrim.tui`
   - **Linux/macOS**: `./start-tui.sh` or `python -m smartrim.tui`
   - Keyboard-driven, 7 views (Command Center, Live Monitor, Advice, Lessons, Runs, Debriefs, Timelapse), auto-refreshes every 10s (configurable via `TUI_REFRESH`).
   - The Command Center auto-refreshes (configurable in the sidebar) and is designed to
     sit on a second monitor next to the game: alert banner, vitals, colonist cards,
     resources, current advice, reflex log, and quick actions.
9. (Optional) Timelapse of the colony:
   - Captures a screenshot twice a day (default 6am & 6pm, configurable via
     `TIMELAPSE_HOURS`) when the monitor is running (`TIMELAPSE_ENABLED=1`).
   - Manual capture: `python -m smartrim.timelapse capture`
   - Build an animated GIF: `python -m smartrim.timelapse build`
   - View in the dashboard's **Timelapse** tab (capture now / build GIF / browse frames).
10. (Optional) Start the desktop notifier for pop-up alerts even when you are not focused on the terminal.\r\n   looking at the second screen:
   - **Windows**: `.\start-notify.ps1`
   - **Linux/macOS**: `./start-notify.sh`
   - Or one-shot: `python -m smartrim.notify --once`
11. Layer 2 reflex actor (opt-in): set REFLEX_KILL=0 in .env to enable whitelisted actions.\r\n   (`draft-and-focus-fire`, `designate-firefighting`, `assign-beds-to-unassigned`). Default is
   `REFLEX_KILL=1` (all reflex actions dry-run only / disabled).    Use `python -m smartrim.cli reflex pause|resume|status`
   to manage the one in-game day pause. All reflex actions ship `dry_run: true` by default; set
   `REFLEX_DRY_RUN=0` to allow actual MCP writes.
   - `python -m smartrim.cli reflex status` - show kill/dry-run/pause/lock/human-action state
   - `python -m smartrim.cli reflex pause` - suspend reflex actions for one in-game day (cleared on day roll)
   - `python -m smartrim.cli reflex resume` - clear the pause early
   - Human actions (`order_pawn`, `build`, `designate` via CLI) are recorded to
     `runtime/control/last_human_action.json` and defer reflexes for 60 seconds.
   - Reflex actions are audited to `runtime/<run>/actions.jsonl` (gitignored) and never touch
     `advice_log` or `auto_pauses`.

## Layout

- `src/smartrim/` - Python package (monitor, situation, lessons, outcomes, evaluate, debrief, llm, wiki, reflex_actor, reflex_preconditions, cli, counselor, config, mcp_client, say_daily, quests, replay, advice_log, debrief_llm, debrief_bundle, eval_models, logging_config)
- `schemas/` - JSON schemas for lessons, advice, snapshots
- `docs/local_llm/ollama/` - Modelfiles for the tuned Ollama models (`gemma4-e2b-rimworld`, `qwen3-rimworld`)
- `memory/` - durable knowledge base (lessons.jsonl, wiki cache, phases, rubrics); runtime state lives in `runtime/`
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

Everything disposable lives under `runtime/` and is gitignored:

```
runtime/
  control/                  # stable, no run id needed
    active.json             # {"run_id","pid","arm","started_at"} written at monitor start
    monitor.pid  monitor.log  monitor.err.log  monitor.startup.lock
    reflex.lock  reflex_pause.json  last_human_action.json
    monitor.watchdog.log  monitor.watchdog.stop
  run-010-adv/              # one directory per run
    end.json  meta.json
    snapshots/  timelapse/  debriefs/  candidates/  alerts/
    advice.jsonl  actions.jsonl  quests.json
```

`RUN_ID` is allocated by the monitor at startup (`run-NNN-adv` / `run-NNN-obs`)
and published in `runtime/control/active.json`. Every other process (TUI,
dashboard, CLI) resolves the active run from that file instead of guessing.

`memory/` keeps only durable knowledge: `lessons.jsonl`, `lessons.sqlite`
(derived), `wiki/`, `phases.md`, rubrics and `reflex_actions.yaml`.

Deleting `runtime/` is always safe; it rebuilds on the next monitor start.
Archive a completed run with `python -m smartrim.debrief add-lessons <run-id>`,
which moves `runtime/<run-id>/` into `runtime/archive/`.

## Tests

```shell
python -m pytest
```

See `memory/phases.md` and `docs/local_llm/RUN-PROTOCOL.md` for evaluation protocol.

## License

MIT License - see [LICENSE](LICENSE) for details.
