# SmartRim — Project Feature Map

> A file-by-file inventory of the SmartRim codebase: what each module does, what it exposes, and how it fits the overall autonomous RimWorld sidecar.

**Last reviewed:** 2026-10-29 (after adding `_say_visible` to the reflex monitor).  
**Source root:** `src/smartrim/` (installed editable; `PYTHONPATH=src`).  
**Tests:** `python -m pytest` → 186 passing.  
**Lint:** `ruff check` (target `py313`, line-length 100).

---

## 1. What SmartRim is

SmartRim is an **autonomous sidecar** for RimWorld. It does not modify the game; it talks to the **RimMolt MCP server** (`localhost:8787`) that the game exposes, observes colony state, classifies the situation, retrieves matching **lessons**, and either advises the player (in-game `say`) or performs guarded reflex actions. It keeps a persistent lesson store, tracks outcomes, and produces end-of-run debriefs.

High-level loop:

```
RimWorld (RimMolt MCP)  <--poll-->  monitor.py  -->  situation.py (classify + retrieve lessons)
                                          |-->  reflex_actor.py (guarded actions)
                                          |-->  say_daily.py (daily status/advice)
                                          |-->  advice_log.py / outcomes.py (tracking)
                                          |-->  dashboard.py (Streamlit UI)
                                          \-->  debrief*.py (end-of-run analysis)
```

---

## 2. Top-level layout

| Path | Role |
|---|---|
| `src/smartrim/` | Main Python package (src layout). |
| `sidecar/` | Replay harness and one-off scripts. |
| `schemas/` | JSON schemas for lessons, advice, snapshots. |
| `tests/` | pytest suite (`unittest.TestCase` style, 186 tests). |
| `memory/` | Persistent runtime data (gitignored except `lessons.jsonl` and wiki cache). |
| `local_llm/ollama/` | Modelfiles for tuned Ollama models. |
| `scripts/` | Helper launchers. |
| `start-monitor.*`, `start-dashboard.*` | Launchers for monitor/dashboard. |
| `install.*` | Venv + dependency installer. |
| `.env` / `.env.example` | Environment configuration. |
| `pyproject.toml`, `ruff.toml` | Packaging, pytest config, lint config. |
| `AGENTS.md`, `README.md`, `CONTRIBUTING.md`, `CHANGELOG.md` | Docs. |

---

## 3. Core runtime modules (`src/smartrim/`)

### 3.1 `__init__.py`
- **Role:** Package marker. One-line docstring only.

### 3.2 `config.py`
- **Role:** Central environment-variable configuration. Loads `.env` via `python-dotenv` if available.
- **Capabilities:** Exposes `MCP_URL`, `POLL_INTERVAL`, `MCP_DELAY`, `BASE_DIR`, directory paths (`ALERTS_DIR`, `SNAPSHOTS_DIR`, `DEBRIEFS_DIR`, `CANDIDATES_DIR`), health/mood thresholds (`HEALTH_THRESHOLD`, `MOOD_*_THRESHOLD`), `URGENT_KEYWORDS`, `SAY_DAILY_*`, `RUN_DAYS`, `REFLEX_*` flags, LLM model names.
- **Notes:** Imported by nearly every module; keep side-effect-free.

### 3.3 `mcp_client.py`
- **Role:** JSON-RPC client for the RimMolt MCP server.
- **Capabilities:** `McpClient(url, delay, max_retries)` with `ping()`, `call_tool(name, arguments)`. Parses JSON-RPC responses, retries read-only tools, throttles calls. `READ_ONLY_TOOLS` set defines which tools may be retried/bundled. `McpError` for transport/parse failures.
- **Used by:** monitor, counselor, cli, dashboard, debrief, replay, say_daily, wiki.

### 3.4 `monitor.py` (860 lines) — the heart of the sidecar
- **Role:** Colony monitoring loop + reflex alerts + daily say + snapshots.
- **Capabilities:**
  - `main()` polling loop with lock file (`_acquire_lock`/`_release_lock`), PID tracking, stale-PID detection.
  - `poll_once(client, state)` → `PollResult`: fetches status/conditions/colonists/alerts, builds situation, retrieves lessons, detects urgent alerts, writes snapshots.
  - `run_reflex_checks(...)` evaluates reflex actions via `reflex_actor`.
  - `_say_daily_message(...)` builds and displays daily status+advice via `say_daily.build_message` + `say` (now `_say_visible` to render while paused).
  - `_log_scheduled` / `_log_urgent` write advice to `advice_log`.
  - Snapshot writing: `write_snapshot`, `write_reflex_snapshot`, `normalize_snapshot`, `snapshot_dir_for`.
  - `adviser_acts()` honors `OBSERVE_ONLY` / `REFLEX_KILL`.
  - `_say_visible()` briefly unpauses to render `say` messages, then restores pause state.
  - Auto-pause on urgent alerts (`set_speed pause`).
  - Run-end marker writing (`write_run_end`) when `RUN_DAYS` reached.
- **Key types:** `PollResult`, `ensure_dirs`, `configure_observe_only`.

### 3.5 `situation.py` (890 lines)
- **Role:** Situation classifier + lesson retrieval (pure Python, no MCP/LLM — fully testable).
- **Capabilities:**
  - `classify_phase(...)`, `build_threats(...)`, `build_resources(...)`, `build_situation(...)` → situation dict.
  - `rank_actions(...)`, `retrieve(...)` FTS-backed lesson matching.
  - `load_lessons(...)`, `validate_lesson(...)`, `validate_all(...)` (CLI `validate`).
  - `render_markdown(...)` for human-readable situation.
  - `main()` CLI: `validate`, `reindex` (rebuild SQLite index), retrieval helpers.
- **Enums:** `_PHASES_ENUM`, `_THREATS_ENUM`, `_RESOURCES_ENUM`, `_DIFFICULTY_ENUM`, `_STORYTELLER_ENUM` — must stay in sync with `schemas/lesson.schema.json`.

### 3.6 `lesson_store.py` (608 lines)
- **Role:** Lesson persistence abstraction.
- **Capabilities:**
  - Dataclass `Lesson` with normalization of mutable defaults.
  - Protocol `LessonStore` + `JsonlLessonStore` (human-editable source of truth) + `SqliteLessonStore` (FTS5 index).
  - `get_store(...)`, `sync_sqlite(...)` (rebuild index).
  - `_ci_contains`, `_normalize_list` helpers.
- **Storage:** `memory/lessons.jsonl` (tracked) → `memory/lessons.sqlite` (derived, gitignored).

### 3.7 `reflex_actor.py` (575 lines)
- **Role:** Layer 2 reflex actor — whitelisted, guarded, audited in-game actions.
- **Capabilities:**
  - `ReflexAction` dataclass, `load_reflex_actions(...)` from YAML.
  - `ReflexActor` evaluates preconditions, executes MCP writes (draft, order, designate, build, etc.), logs outcomes.
  - `close_action_outcomes()` persists audit trail.
  - Respects `REFLEX_KILL` / `REFLEX_DRY_RUN`.
- **Config:** `memory/reflex_actions.yaml` (whitelist).

### 3.8 `reflex_preconditions.py` (90 lines)
- **Role:** Predicate helpers for reflex actions.
- **Capabilities:** `has_raid_alert`, `has_fire_alert`, `has_unassigned_colonist`, `has_shooter_above_5`, `none_drafted`, plus `_alerts`, `_colonists`, `_alert_text`.

### 3.9 `counselor.py` (507 lines)
- **Role:** Reusable tool library for game interaction via MCP (high-level wrappers).
- **Capabilities:** Dozens of helpers: `ping`, `status`, `conditions`, `colonists`, `alerts`, `resources`, `research`, `zones`, `wildlife`, `pawns`, `main_menu`, `game_setup_status`, `select_scenario`, `select_storyteller`, `create_world`, `select_starting_site`, `start_game`, `edit_starting_pawn`, `pause`/`resume`, `wait`, `save`, `build`, `build_wall`, `inspect`, `area`, `set_priority`, `draft`, `undraft`, `order`, `do_action`, `assign`, `set_research`, `designate`, `growing_zone`, `stockpile`, `say`, `read_letter`, `screenshot`, `things`, `get_map`, `power`, `world`, `unforbid_all`, `survey`, `find_rich_soil`, `chop_trees`, `raid_status`, `equip`, `find_corpses`, `scan_area`, `_safe`, `game_state`, `daily_summary`.

### 3.10 `cli.py` (217 lines)
- **Role:** CLI entry point for reflex control and human actions.
- **Capabilities:** `run_ping`, `check_connection`, `_record_human_action`, `_build`, `_order`, `_designate`, `run_reflex`, `main()` (argparse). Commands: `reflex status/pause/resume`, human actions (`build`, `order`, etc.).
- **Invocation:** `python -m smartrim.cli ...`

### 3.11 `config.py` — see 3.2.

### 3.12 `logging_config.py` (33 lines)
- **Role:** Logging setup.
- **Capabilities:** `setup_logging()`, `get_logger(name)`.

---

## 4. AI / LLM layer

### 4.1 `llm.py` (247 lines)
- **Role:** Optional LLM integration (Ollama/OpenAI/Anthropic) with graceful degradation.
- **Capabilities:** `LlmClient`, `OllamaClient`, `OpenAIClient`, `AnthropicClient`; `get_client()`, `resolve_model()`, `resolve_task_params()`, `generate()`, `ModelForTask`. `_ollama_generate()` low-level helper. Optional imports wrapped in try/except.

### 4.2 `say_daily.py` (238 lines)
- **Role:** Daily in-game status + advice message builder.
- **Capabilities:** `build_message(slot, use_llm, conditions, status, alerts, research, resources, colonists_param)` → (message, meta); `build_llm_advice(...)`; `say_message(text)`; `main()` CLI (`--slot`, `--hour`).
- **Used by:** `monitor._say_daily_message`.

### 4.3 `chat.py` (77 lines)
- **Role:** Interactive colony chat via local LLM.
- **Capabilities:** `get_context()`, `chat_loop()`, `main()`.

---

## 5. Debrief & evaluation

### 5.1 `debrief.py` (201 lines)
- **Role:** Debrief generation from snapshots/advice.
- **Capabilities:** `_day_key()`, `generate_debrief(...)`.

### 5.2 `debrief_bundle.py` (564 lines)
- **Role:** AI-ready debrief bundle (template-only, no API calls).
- **Capabilities:** `_load_wiki_facts`, `_parse_day`, `_make_sort_key`, `_colonists`, `_is_valid`, `_day_label`, `_timeline`, `_advice_section`, `_food_units`, `_quest_records`, `_incident_lines`, `_event_digest`, `_load_run_marker`, `_derive_outcome`, `build_bundle(...)`.

### 5.3 `debrief_llm.py` (435 lines)
- **Role:** LLM-backed debrief analysis (replaces manual paste).
- **Capabilities:** `SchemaValidationError`, `TriggerCandidate`, `LessonCandidate`; `_extract_first_json_fence`, `_validate_lesson_candidates`, `_system_with_fence_instruction`, `_schema_retry_prompt`, `_generate_once`, `analyze_debrief`, `find_bundle`, `write_analysis`, `_write_candidate_lessons`, `_normalize_trigger`, `main()`.

### 5.4 `evaluate.py` (462 lines)
- **Role:** Phase 2 evaluation harness (summarize/compare runs).
- **Capabilities:** `_load_json`, `_load_end_marker`, `_load_advice`, `resolve_snapshots_dir`, `_snapshot_sort_key`, `_load_snapshots`, `_summary`, `_days_passed`, `_day_label`, `_is_day10`, `_colonists_alive`, `_alert_texts`, `_first_day`, `_is_food`, `_is_medicine`, `_is_break`, `_arm`, `summarize_run`, `_numbers`, `_median_range`, `arm_summary`, `format_table`, `_cell`, `_fmt_range`, `format_arm_summary`, `render_report`, `_print_rows`, `_maybe_write`, `_rows_from_dir`, `cmd_summarize`, `cmd_compare`, `main()`.

### 5.5 `eval_models.py` (465 lines)
- **Role:** Evaluate multiple models on the same debrief bundle (A/B), score with rubric.
- **Capabilities:** `_repo_root`, `_load_rubric_labels`, `ScoreRow`, `_safe_load_json`, `_extract_fenced_json`, `_detect_sections`, `_count_bullets`, `score_debrief_answer`, `_safe_model_suffix`, `eval_one`, `main()`.

### 5.6 `ab_debrief.py` (50 lines)
- **Role:** A/B harness: run the same debrief bundle against two models.
- **Capabilities:** `main()`.

### 5.7 `outcomes.py` (193 lines)
- **Role:** Outcome tracking — close open advice records at each daily snapshot and update lesson confidence.
- **Capabilities:** `_read_advice`, `_write_advice`, `_read_lessons`, `_write_lessons`, `_close_advice`, `close_outcomes(...)`.

### 5.8 `advice_log.py` (199 lines)
- **Role:** Append-only JSONL of every piece of advice, with outcome tracking.
- **Capabilities:** `_ensure_dir`, `new_advice_id`, `log_advice`, `update_outcome`, `set_event_cause`, `set_cause_matching`, `find_open_duplicate`, `read_advice`.

---

## 6. Data, wiki, and persistence

### 6.1 `wiki.py` (372 lines)
- **Role:** Fetch RimWorld wiki pages and convert to clean markdown.
- **Capabilities:** `_load_manifest`, `_save_manifest`, `fetch_pages`, `_strip_html`, `convert_pages`, `main()` (fetch/convert subcommands).

### 6.2 `quests.py` (171 lines)
- **Role:** Quest context for snapshots and debrief bundle (bundle v3).
- **Capabilities:** `clean_text`, `load_registry`, `save_registry`, `list_quests`, `_detail`, `update`, `summary_lines`, `quests_from_snapshots`.

### 6.3 `replay.py` (231 lines)
- **Role:** Replay harness for Layer 2 reflex actions (records MCP calls instead of writing).
- **Capabilities:** `MockCounselor`, `_snapshot_sort_key`, `_load_snapshots`, `_game_state_from_snapshot`, `_drafted_names`, `_has_drafted_status`, `run_replay`, `main()`.

---

## 7. UI

### 7.1 `dashboard.py` (532 lines)
- **Role:** Streamlit dashboard for monitoring, advice browser, lessons, run history, debriefs.
- **Capabilities:** `load_current_alerts`, `load_all_advice`, `load_lessons`, `load_runs_metadata`, `load_run_snapshots`, `load_debriefs`, `get_live_game_state`, tabs: `live_monitor_tab`, `advice_browser_tab`, `lesson_explorer_tab`, `run_history_tab`, `debrief_viewer_tab`, `main()`.

---

## 8. Sidecar (`sidecar/`)

### 8.1 `sidecar/reflex.py`
- **Role:** Layer 2 reflex actor entry point (sidecar variant).

### 8.2 `sidecar/replay.py`
- **Role:** Replay harness (sidecar copy).

---

## 9. Schemas (`schemas/`)

| File | Role |
|---|---|
| `lesson.schema.json` | Schema for lessons (`memory/lessons.jsonl`). Must stay in sync with situation enums. |
| `advice.schema.json` | Schema for advice records. |
| `snapshot.schema.json` | Schema for daily snapshots. |

---

## 10. Tests (`tests/`)

186 tests, `unittest.TestCase` style, `pythonpath = ["src"]`.

| Test file | Covers |
|---|---|
| `test_situation.py` | Situation classifier + lesson retrieval. |
| `test_lesson_store.py` | Jsonl/SQLite lesson store. |
| `test_phase1.py` | Phase 1 monitor/reflex. |
| `test_no_colony.py` | Monitor behavior without colony. |
| `test_reflex_actor.py` | Reflex actor + preconditions. |
| `test_replay.py` | Replay harness. |
| `test_cli.py` | CLI commands. |
| `test_outcomes.py` | Outcome tracking. |
| `test_advice_dedupe.py` | Advice deduplication. |
| `test_bundle_v3.py` | Debrief bundle v3. |
| `test_debrief_llm.py` | LLM debrief analysis. |
| `test_debrief_bundle.py` | Debrief bundle. |
| `test_evaluate.py` | Evaluation harness. |
| `test_eval_models.py` | Model evaluation. |
| `test_run_protocol.py` | Run protocol. |
| `test_candidate_lessons.py` | Candidate lesson generation. |
| `test_wiki.py` | Wiki fetch/convert. |

Fixtures live in `tests/fixtures/` (e.g., `snapshot_day13.json`).

---

## 11. Scripts & launchers

| File | Role |
|---|---|
| `install.ps1` / `install.sh` | Create venv + install deps (`pip install -e ".[dev]"`). |
| `start-monitor.ps1` / `.sh` | Launch reflex monitor (adviser on by default; `--observe-only`). |
| `start-dashboard.ps1` / `.sh` | Launch Streamlit dashboard. |
| `stop-monitor.ps1` / `.sh` | Stop monitor (fixed `$pid` read-only bug). |
| `scripts/start_monitor.*` | Alternate monitor launchers. |
| `start-ollama.ps1`, `stop-ollama.ps1` | Ollama lifecycle helpers. |
| `watchdog-monitor.ps1` | Monitor watchdog. |

---

## 12. Configuration & metadata

| File | Role |
|---|---|
| `pyproject.toml` | Project metadata, optional extras (`dev`, `dashboard`, `llm`), pytest config (`pythonpath = ["src"]`). |
| `ruff.toml` | Lint config: target `py313`, line-length 100, rules E,F,I,UP,B,SIM,C4,ISC,PIE,RUF. |
| `.env.example` | Template for environment variables. |
| `.gitignore` | Ignores runtime data, venv, caches. |
| `AGENTS.md` | Agent/human working guide (this is the canonical reference). |
| `README.md` | User-facing getting started. |
| `CONTRIBUTING.md` | Contribution workflow. |
| `CHANGELOG.md` | Change log. |
| `TODO.md` | Task list. |
| `MCP-REFERENCE.md` | MCP tool reference. |
| `smartrim_code_review.md` | Prior code review (bugs/dead code). |

---

## 13. Data flow summary

1. **Monitor** polls MCP (`get_status`, `get_conditions`, `list_colonists`, `get_alerts`, …) every `POLL_INTERVAL`.
2. **Situation classifier** (`situation.py`) turns raw state into a situation dict (phase, threats, resources, difficulty, storyteller, biome).
3. **Lesson retrieval** (`lesson_store.py`) FTS-searches `memory/lessons.jsonl` (via SQLite index) for matching lessons.
4. **Reflex actor** (`reflex_actor.py`) executes whitelisted guarded actions (dry-run by default).
5. **Daily say** (`say_daily.py`) composes a status+advice message and displays it via MCP `say` (unpauses briefly to render).
6. **Advice log / outcomes** record what was advised and close outcomes at snapshots; lesson confidence updated.
7. **Dashboard** (Streamlit) visualizes alerts, advice, lessons, runs, debriefs.
8. **Debrief** (end of run) builds a bundle from snapshots/advice and optionally runs LLM analysis, emitting candidate lessons.

---

## 14. Key design principles (from CONTRIBUTING.md)

- Deterministic monitoring; LLM only for advisory analysis.
- Graceful degradation when LLM/MCP unavailable.
- MCP writes only through reflex actor with dry-run defaults.
- `src` layout; explicit imports; dataclasses for data.
- Ruff-clean, pytest-green, lessons validated (`python -m smartrim.situation validate`).

---

*Generated from a full repository review. For bug-level findings, see `smartrim_code_review.md`.*
