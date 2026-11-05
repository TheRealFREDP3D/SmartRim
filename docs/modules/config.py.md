# config.py — Environment Configuration

Central configuration via environment variables. Loads `.env` via `python-dotenv` if available.

## Exported Constants

| Variable | Default | Description |
| ---------- | --------- | ------------- |
| `MCP_URL` | `http://localhost:8787/` | RimMolt MCP server endpoint |
| `POLL_INTERVAL` | `30` | Monitor poll interval (seconds) |
| `MCP_DELAY` | `0.15` | Throttle between MCP calls |
| `BASE_DIR` | Computed | Project root directory |
| `RUNTIME_DIR` | `runtime` | Disposable runtime root (gitignored) |
| `CONTROL_DIR` | `runtime/control` | PID, logs, locks, `active.json` |
| `ACTIVE_RUN_FILE` | `runtime/control/active.json` | Active-run pointer written by the monitor |
| `MONITOR_PID_FILE` | `runtime/control/monitor.pid` | Monitor PID lock |
| `MONITOR_LOG_FILE` | `runtime/control/monitor.log` | Monitor stdout |
| `MONITOR_ERR_LOG_FILE` | `runtime/control/monitor.err.log` | Monitor stderr |
| `REFLEX_LOCK_FILE` | `runtime/control/reflex.lock` | Reflex PID lock |
| `REFLEX_PAUSE_FILE` | `runtime/control/reflex_pause.json` | One in-game day pause |
| `HUMAN_ACTION_FILE` | `runtime/control/last_human_action.json` | 60s reflex deferral window |
| `LESSONS_FILE` | `memory/lessons.jsonl` | Durable lesson source of truth |
| `LESSONS_DB` | `memory/lessons.sqlite` | Derived FTS index |
| `WIKI_DIR` | `memory/wiki` | Durable wiki cache |
| `REFLEX_ACTIONS_FILE` | `memory/reflex_actions.yaml` | Reflex whitelist config |
| `HEALTH_THRESHOLD` | `50` | Health % for urgent alert |
| `MOOD_MINOR_THRESHOLD` | `35` | Mood % for minor break risk |
| `MOOD_MAJOR_THRESHOLD` | `20` | Mood % for major break risk |
| `MOOD_EXTREME_THRESHOLD` | `5` | Mood % for extreme break risk |
| `URGENT_KEYWORDS` | `["fire","predator","raid",...]` | Keywords for urgent alert classification |
| `LLM_API_KEY` | `None` | API key for cloud LLM |
| `LLM_PROVIDER` | `ollama` | `ollama` \| `openai` \| `anthropic` |
| `LLM_MODEL` | `None` | Default model |
| `OLLAMA_BASE_URL` | `http://localhost:11434` | Ollama server URL |
| `NVIDIA_BASE_URL` | `https://integrate.api.nvidia.com/v1` | NVIDIA NIM (OpenAI-compatible) |
| `NVIDIA_API_KEY` | `None` | NVIDIA NIM API key |
| `NVIDIA_MODEL` | `nvidia/nemotron-3.5-super-vl-120b-a12b` | Model used when `LLM_PROVIDER=nvidia` |
| `LLM_MODEL_DAILY` | `llama3.2:1b-instruct-q4_K_M` | Daily advice model |
| `LLM_MODEL_DEBRIEF` | `gemma4-e2b-rimworld` | Debrief analysis model |
| `LLM_MODEL_CHAT` | `qwen3-rimworld` | Chat model |
| `RUN_ID` | `current-run` (sentinel) | Run id; the monitor replaces it at startup |
| `UNSET_RUN_ID` | `current-run` | Sentinel meaning "no run allocated yet" |
| `SAY_DAILY_HOURS` | `[6, 18]` | Hours for daily in-game message |
| `SAY_DAILY_USE_LLM` | `False` | Use LLM for daily advice |
| `RUN_DAYS` | `11` | Fixed run length (daysPassed target) |

## Run path helpers

Per-run paths are functions, not constants, so the run id can be resolved at
call time:

| Function | Returns |
|---|---|
| `run_dir(run_id)` | `runtime/<run_id>` |
| `run_subdir(name, run_id=None, create=False)` | a subdirectory inside a run (no side effect unless `create`) |
| `run_file(name, run_id=None, create=False)` | a file at the run root |
| `alerts_dir`, `snapshots_dir`, `debriefs_dir`, `candidates_dir`, `timelapse_dir` | per-run subdirectories |
| `advice_file`, `actions_file`, `quests_file` | per-run ledgers |
| `latest_run_id()` | newest run with data on disk, or `None` |
| `resolve_run_id()` | env `RUN_ID` → patched `RUN_ID` → `active.json` → `latest_run_id()` |
| `write_active_run`, `read_active_run`, `clear_active_run` | `runtime/control/active.json` lifecycle |

## Notes

- Imported by nearly every module — keep side-effect-free
- `.env` and `.env.*` are gitignored; `.env.example` is tracked
