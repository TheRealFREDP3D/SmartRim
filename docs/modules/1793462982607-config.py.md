# config.py — Environment Configuration

Central configuration via environment variables. Loads `.env` via `python-dotenv` if available.

## Exported Constants

| Variable | Default | Description |
| ---------- | --------- | ------------- |
| `MCP_URL` | `http://localhost:8787/` | RimMolt MCP server endpoint |
| `POLL_INTERVAL` | `30` | Monitor poll interval (seconds) |
| `MCP_DELAY` | `0.15` | Throttle between MCP calls |
| `BASE_DIR` | Computed | Project root directory |
| `ALERTS_DIR` | `memory/alerts` | Alert output directory |
| `SNAPSHOTS_DIR` | `memory/snapshots` | Daily snapshot directory |
| `DEBRIEFS_DIR` | `memory/debriefs` | Debrief output directory |
| `CANDIDATES_DIR` | `memory/candidates` | Candidate lessons directory |
| `HEALTH_THRESHOLD` | `50` | Health % for urgent alert |
| `MOOD_MINOR_THRESHOLD` | `35` | Mood % for minor break risk |
| `MOOD_MAJOR_THRESHOLD` | `20` | Mood % for major break risk |
| `MOOD_EXTREME_THRESHOLD` | `5` | Mood % for extreme break risk |
| `URGENT_KEYWORDS` | `["fire","predator","raid",...]` | Keywords for urgent alert classification |
| `LLM_API_KEY` | `None` | API key for cloud LLM |
| `LLM_PROVIDER` | `ollama` | `ollama` \| `openai` \| `anthropic` |
| `LLM_MODEL` | `None` | Default model |
| `OLLAMA_BASE_URL` | `http://localhost:11434` | Ollama server URL |
| `LLM_MODEL_DAILY` | `llama3.2:1b-instruct-q4_K_M` | Daily advice model |
| `LLM_MODEL_DEBRIEF` | `gemma4-e2b-rimworld` | Debrief analysis model |
| `LLM_MODEL_CHAT` | `qwen3-rimworld` | Chat model |
| `RUN_ID` | `current-run` | Run identifier for advice logging |
| `SAY_DAILY_HOURS` | `[6, 18]` | Hours for daily in-game message |
| `SAY_DAILY_USE_LLM` | `False` | Use LLM for daily advice |
| `RUN_DAYS` | `11` | Fixed run length (daysPassed target) |

## Notes

- Imported by nearly every module — keep side-effect-free
- `.env` and `.env.*` are gitignored; `.env.example` is tracked
