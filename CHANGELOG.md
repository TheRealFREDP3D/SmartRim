# Changelog

All notable changes to SmartRim will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed

- **Runtime state moved to `runtime/`.** Per-run artifacts (snapshots, timelapse,
  debriefs, candidates, alerts, advice, actions, quests, run markers) now live in
  `runtime/<run-id>/`; process files (pid, logs, locks, active-run pointer) live in
  `runtime/control/`. `memory/` keeps only durable knowledge (lessons, wiki, docs).
- `RUN_ID` is allocated by the monitor at startup and published to
  `runtime/control/active.json`; `config.resolve_run_id()` replaces the
  `current-run` placeholder as the cross-process run lookup.
- `current-run` is now an explicit `UNSET_RUN_ID` sentinel and can never name a
  directory.
- Start/stop/watchdog scripts and the TUI/dashboard read the new control paths;
  the watchdog resumes the run recorded in `active.json` after a crash.
- `tests/conftest.py` isolates `runtime/` per test, so the suite cannot write into
  the repo (this leak previously produced phantom `current-run` snapshots).

### Added

- NVIDIA NIM provider (`LLM_PROVIDER=nvidia`, `NVIDIA_BASE_URL`, `NVIDIA_API_KEY`, `NVIDIA_MODEL`):
  OpenAI-compatible client, env provider overrides the task registry, and the model comes
  from `NVIDIA_MODEL` rather than a local Ollama tag
- Desktop notifier for urgent alerts (`python -m smartrim.notify` + start/stop scripts): pop-up + beep when a *new* urgent signature appears
- Dashboard resource icons (`src/smartrim/assets/icons/`)
- Stale-advice sweeper `advice_log.expire_stale()` — open records older than 3 days auto-expire before each debrief (wired into `outcomes.close_outcomes`, plus CLI `python -m smartrim.advice_log expire [days]`)
- `tests/test_advice_maintenance.py` — sweeper semantics, boundary ages, idempotency, atomic-write pin (test suite grows 186 → 194)
- `.mcp.json.example` template so fresh clones get the rimmolt config
- `docs/local_llm/RUN-PROTOCOL.md` tracked in the repo (moved out of gitignored `.DEV/`)
- MIT License
- Gitleaks configuration with allowlist for wiki raw HTML
- Gitleaks pre-commit hook for secret scanning
- Cross-platform shell scripts (install.sh, start-monitor.sh, stop-monitor.sh, start-dashboard.sh)
- CLI entry point (main() function) to smartrim.cli for module invocation
- Streamlit dashboard optional dependency
- Structured logging configuration
- Type hints to key modules (monitor.py, mcp_client.py, config.py)
- Custom exception classes for MCP client and monitor operations
- CHANGELOG.md for tracking project changes
- CONTRIBUTING.md for contribution guidelines

### Changed

- **MCP config is dev-only**: `.mcp.json` removed from the repo and gitignored (machine-specific servers stay local); committed template covers rimmolt only
- **`advice_log.py` is the single owner of `memory/advice/advice.jsonl`**: `outcomes.py` delegates its reads/writes — all advice rewrites now use one atomic tmp+`os.replace` implementation
- Cheat sheet rewritten and verified against the code (every command, flag, and env default checked; fixed broken code fences, `debrief_bundle` positional run id, stale `sidecar/replay.py` path)
- Project docs accuracy pass: README (module roster, `RUN-PROTOCOL.md` path, per-run snapshot layout), PROJECT-OVERVIEW (sidecar section rewrite, drifted line counts), stale `python sidecar/...` usage examples in module docstrings fixed to `python -m smartrim...`
- Dashboard rewrite: opens on a second-monitor **Command Center** view (alert banner, vitals, colonist cards, resources with icons, current advice, reflex log, quick actions, auto-refresh)
- Monitor: `contextlib.suppress` used for best-effort say pause/unpause cleanup
- Pre-commit ruff hook fixed: `sidecar tests` → `src tests`
- Lint baseline green: collapsed placeholder-only f-strings in `debrief_llm.py` (braces preserved for `.format()`), unused `resolved_model` binding dropped, import sorting, ruff `allowed-confusables` for `×`/`≈` math notation
- Updated README with cross-platform setup instructions (Windows PowerShell and Linux/macOS bash)
- Updated README to explain RimMolt and link to Steam Workshop
- Removed "Windows/PowerShell-based" limitation from README
- Fixed Python version requirement to 3.11+ (matching pyproject.toml)
- Replaced star imports with explicit imports in monitor.py and dashboard.py
- Removed unused variables (cid, situation_risks, date) to fix lint warnings
- Migrated pytest configuration from pytest.ini to pyproject.toml
- Removed deprecated requirements-dev.txt (using pyproject.toml extras)
- Updated .gitignore to fix reflex actor runtime file ignore rules
- Added python-dotenv and version bounds to dependencies

### Fixed

- `RUN_DAYS` tests no longer break when `.env` overrides it for long runs (env-forced reload + mock instead of hardcoded default)
- Non-atomic rewrite of the tracked `memory/advice/advice.jsonl` in `outcomes.py` (crash mid-write could truncate the ledger)
- Pre-commit ruff hook referenced a nonexistent `sidecar/` directory
- High-priority lint issues (F405 star-import warnings, F841 unused variables)
- Fixed .gitignore Streamlit skills paths (backslash to forward slash)
- Fixed .gitignore + prefix artifacts from diff merge

## [0.1.0] - 2026-10-26

### Added

- Initial SmartRim implementation
- MCP client for rimmolt server integration
- Colony monitoring with reflex alerts
- LLM integration for debrief analysis and daily advice
- Wiki caching system for RimWorld mechanics
- Streamlit dashboard for colony visualization
- Persistent snapshots, alerts, and debriefs
- Reflex actor (Layer 2) with whitelisted guarded actions
- Test suite with 186 tests
