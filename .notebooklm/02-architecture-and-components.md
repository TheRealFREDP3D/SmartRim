# SmartRim Architecture and Components

## System Architecture

SmartRim follows a monitor-evaluate-advise pattern:

```
RimWorld (with RimMolt mod)
    ↓ JSON-RPC over HTTP (localhost:8787)
RimMolt MCP Server
    ↓
SmartRim Sidecar (Python)
    ├─ Monitor Loop
    │  ├─ Snapshot (observe state)
    │  ├─ Situation (analyze threats)
    │  ├─ Counselor (generate advice)
    │  └─ Action (pause + log advice)
    └─ Post-Run
       ├─ Debrief (analyze run)
       └─ Evaluate (score + refine lessons)
```

## Component Deep Dive

### 1. Monitor (`sidecar/monitor.py`)

The monitor is the heart of SmartRim - a continuous loop that:
- Polls game state at configurable intervals (default: every 30 seconds)
- Takes structured snapshots of colony state
- Detects urgent alerts (food shortages, health crises, combat)
- Invokes the situation analyzer when danger is detected
- Triggers the counselor to generate advice
- Optionally pauses the game for human review
- Logs all events to `memory/monitor.log`

**Key Functions:**
- `main_loop()` - Main polling loop
- `take_snapshot()` - Captures full game state via MCP
- `check_urgent_alerts()` - Detects immediate threats
- `run_length_reached()` - Enforces 10-day run limit

**Configuration (`sidecar/config.py`):**
- `RUN_DAYS = 11` - When to end runs (daysPassed threshold)
- `SNAPSHOT_INTERVAL = 30` - Seconds between snapshots
- `URGENT_ALERTS` - List of alert types that trigger advice

### 2. Situation Analyzer (`sidecar/situation.py`)

The situation analyzer interprets game state and identifies dangerous patterns:
- Parses snapshot data for threat indicators
- Matches patterns against lesson store
- Contextualizes threats (severity, urgency, options)
- Prioritizes multiple concurrent threats

**Key Functions:**
- `analyze_snapshot()` - Main analysis entry point
- `detect_food_crisis()` - Checks food stores vs colonist needs
- `detect_health_crisis()` - Identifies wounded, sick, or dying colonists
- `detect_combat_threat()` - Recognizes active raids or wildlife attacks
- `detect_mood_crisis()` - Flags mental break risks

**Output:** Structured situation report with:
- Threat type and severity
- Affected colonists/resources
- Recommended actions
- Relevant lesson references

### 3. Counselor (`sidecar/counselor.py`)

The counselor generates context-aware advice:
- Retrieves relevant lessons from lesson store
- Synthesizes advice based on current situation
- Tailors advice to colony state (resources, skills, buildings)
- Provides specific, actionable recommendations

**Key Functions:**
- `generate_advice()` - Main advice generation
- `select_relevant_lessons()` - Filters lessons by situation
- `format_advice()` - Structures output for human consumption
- `prioritize_actions()` - Orders recommendations by urgency

**Advice Format (from `schemas/advice.schema.json`):**
```json
{
  "situation": "Description of threat",
  "severity": "urgent|warning|info",
  "recommendations": [
    {
      "action": "Specific action to take",
      "reason": "Why this action",
      "lesson_id": "reference to lesson"
    }
  ],
  "context": "Additional context for decision"
}
```

### 4. Lesson Store (`sidecar/lessons.py`)

The lesson store is SmartRim's persistent knowledge base:
- Stores validated lessons as JSONL
- Provides lesson retrieval and validation
- Manages lesson metadata (created, used, effectiveness)

**Lesson Structure (from `schemas/lesson.schema.json`):**
```json
{
  "id": "unique-lesson-id",
  "title": "Lesson title",
  "trigger": "When this lesson applies",
  "content": "Lesson content/advice",
  "severity": "urgency level",
  "category": "food|health|combat|mood|base|research",
  "created": "ISO timestamp",
  "used_count": 0,
  "helped_count": 0,
  "failed_count": 0
}
```

**Key Functions:**
- `validate()` - Checks lesson store integrity
- `search()` - Finds lessons by trigger/category
- `record_outcome()` - Updates lesson effectiveness metrics

### 5. MCP Client (`sidecar/mcp_client.py`)

The MCP client wraps RimMolt server interactions:
- Provides Pythonic interface to MCP tools
- Handles JSON-RPC protocol details
- Manages connection lifecycle
- Provides helper methods for common operations

**Key Functions:**
- `call_tool()` - Generic MCP tool invocation
- `get_status()` - Bundle of game status info
- `list_colonists()` - Colonist data
- `get_resources()` - Resource counts
- `set_speed()` - Pause/unpause game

### 6. Debrief System (`sidecar/debrief.py`, `sidecar/debrief_bundle.py`)

The debrief system extracts learnings from completed runs:
- Compiles snapshot data into a structured bundle
- Generates context summaries for each day
- Identifies key events and decisions
- Packages data for LLM analysis
- Records new lessons based on analysis

**Debrief Bundle Structure:**
- Section 1: Colony setup (colonists, tile, scenario)
- Section 2: Timeline by day (events, decisions, outcomes)
- Section 3: Key incidents and causes
- Section 4: Resource trends
- Section 5: Questions for analysis

**Key Functions:**
- `generate_bundle()` - Creates debrief bundle from snapshots
- `analyze_with_llm()` - Sends bundle to LLM for insights
- `extract_lessons()` - Parses LLM response for new lessons

### 7. Evaluation (`sidecar/evaluate.py`)

The evaluation system scores debrief quality:
- Applies rubric to LLM analysis
- Scores accuracy, completeness, actionability
- Tracks improvement over time
- Identifies areas needing refinement

**Rubric Categories (from `memory/debrief-rubric.md`):**
- Accuracy of incident cause identification
- Completeness of timeline reconstruction
- Actionability of recommendations
- Insightfulness of observations

## Data Flow

### During a Run

1. **Snapshot**: Monitor calls MCP tools → captures game state → saves to `memory/snapshots/day-<N>.json`
2. **Analysis**: Situation analyzer reads snapshot → identifies threats → matches lessons
3. **Advice**: Counselor generates advice → saves to `memory/advice/<id>.json`
4. **Action**: Monitor pauses game (if adviser on) → logs to `memory/monitor.log`
5. **Repeat**: Loop continues until 10-day limit reached

### Post-Run

1. **Bundle**: Debrief compiles all snapshots → creates structured bundle
2. **Analysis**: LLM analyzes bundle → generates insights
3. **Scoring**: Evaluate scores analysis against rubric
4. **Learning**: New lessons extracted → added to lesson store
5. **Refinement**: Failed lessons reviewed → updated or removed

## Integration Points

### RimMolt MCP Server

SmartRim uses RimMolt as its bridge to RimWorld. Key MCP tools used:
- `get_status` - Overall game state
- `list_colonists` - Colonist health, mood, skills
- `get_resources` - Food, materials, wealth
- `get_alerts` - Active threats and warnings
- `set_speed` - Pause/unpause game
- `say` - Display messages to human player

### LLM Integration

SmartRim uses local LLMs (via Ollama) for:
- Advice generation (counselor)
- Debrief analysis
- Lesson refinement

Configuration in `.env`:
```
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama3.2
```

## Configuration

### Environment Variables (`.env`)

```
# MCP Server
MCP_HOST=localhost
MCP_PORT=8787

# LLM
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama3.2

# Monitor
RUN_ID=run-001
ADVISER_MODE=true
```

### Schemas

All data structures are validated against JSON schemas in `schemas/`:
- `snapshot.schema.json` - Game state snapshots
- `lesson.schema.json` - Lesson definitions
- `advice.schema.json` - Advice output

## Error Handling

The sidecar includes error handling for:
- MCP connection failures (retry with backoff)
- Invalid snapshot data (validation against schema)
- Missing lessons (fallback to generic advice)
- LLM timeouts (cached responses, manual review)

## Testing

The test suite (`tests/`) covers:
- Unit tests for each component
- Integration tests with mock MCP server
- Protocol compliance tests
- Lesson validation tests
- Debrief bundle generation tests

Run with: `python -m pytest`
