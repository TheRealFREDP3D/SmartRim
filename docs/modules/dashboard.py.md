# dashboard.py — Streamlit Monitoring Dashboard

Web UI for monitoring, advice browsing, lessons, run history, debriefs.

## Tabs
| Tab | Function | Data Source |
|-----|----------|-------------|
| Live Monitor | `live_monitor_tab()` | MCP `get_status`, `get_alerts`, `memory/alerts/current.json` |
| Advice Browser | `advice_browser_tab()` | `memory/advice/advice.jsonl` |
| Lesson Explorer | `lesson_explorer_tab()` | `memory/lessons.jsonl` |
| Run History | `run_history_tab()` | `memory/runs/*.end.json` |
| Debrief Viewer | `debrief_viewer_tab()` | `memory/debriefs/*.md` |

## Data Loading (cached)
| Function | Cache TTL | Source |
|----------|-----------|--------|
| `load_current_alerts()` | 10s | `memory/alerts/current.json` |
| `load_all_advice()` | 60s | `memory/advice/advice.jsonl` |
| `load_lessons()` | 60s | `memory/lessons.jsonl` |
| `load_runs_metadata()` | 60s | `memory/runs/*.end.json` |
| `load_run_snapshots(run_id)` | 60s | `memory/snapshots/{run_id}/day-*.json` |
| `load_debriefs()` | 60s | `memory/debriefs/*.md` |
| `get_live_game_state()` | — | MCP `get_status` |

## Live Monitor Tab
- Current game status (colonists, day, season, temp)
- Active alerts table (color-coded: urgent=red, warning=orange, info=blue)
- Resource gauges (food days, medicine, wealth)
- Colonist roster with health/mood bars

## Advice Browser
- Filter by run, trigger, severity
- Show linked lessons
- Outcome status badges

## Lesson Explorer
- Search/filter by tag, phase, threat
- Show confidence, application counts
- Edit not supported (edit JSONL directly)

## Run History
- Table of completed runs
- Metrics: days, colonists, stop reason, arm
- Click to view snapshots

## Debrief Viewer
- Render markdown debriefs
- Side-by-side LLM analysis if available

## Launch
```bash
pip install -e ".[dashboard]"
streamlit run src/smartrim/dashboard.py
# or
.\start-dashboard.ps1
```

## Notes
- 532 lines with inline CSS
- **Bug**: `snapshots.sort(key=lambda x: x.get('day', ''))` — string sort breaks day_10 < day_9
- Consider extracting data layer, using Streamlit fragments for auto-refresh