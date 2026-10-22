# SmartRim Technical Implementation

## Technology Stack

### Core Technologies
- **Python 3.13+** - Primary language for sidecar
- **JSON-RPC 2.0** - Protocol for MCP communication
- **Ollama** - Local LLM inference
- **Pytest** - Testing framework
- **JSON Schema** - Data validation

### Dependencies

**Runtime dependencies** (`sidecar/requirements.txt`):
```
# MCP client
httpx  # HTTP client for JSON-RPC

# LLM integration
ollama  # Python client for Ollama

# Data handling
pydantic  # Data validation
jsonschema  # Schema validation

# Utilities
python-dotenv  # Environment variable loading
```

**Development dependencies**:
```
pytest  # Testing
pytest-cov  # Coverage reporting
```

## Project Layout

```
SmartRim/
├── sidecar/              # Python sidecar modules
│   ├── monitor.py        # Main monitoring loop
│   ├── situation.py      # Situation analysis
│   ├── counselor.py      # Advice generation
│   ├── lessons.py        # Lesson store management
│   ├── mcp_client.py     # MCP server client
│   ├── debrief.py        # Debrief orchestration
│   ├── debrief_bundle.py # Bundle generation
│   ├── evaluate.py       # Debrief scoring
│   ├── outcomes.py       # Outcome tracking
│   ├── quests.py         # Quest handling
│   ├── llm.py            # LLM abstraction
│   ├── config.py         # Configuration
│   └── cli.py            # Command-line interface
├── schemas/              # JSON schemas
│   ├── snapshot.schema.json
│   ├── lesson.schema.json
│   └── advice.schema.json
├── tests/                # Test suite
│   ├── test_advice_dedupe.py
│   ├── test_bundle_v3.py
│   ├── test_cli.py
│   ├── test_debrief_bundle.py
│   ├── test_evaluate.py
│   ├── test_no_colony.py
│   ├── test_outcomes.py
│   ├── test_phase1.py
│   ├── test_run_protocol.py
│   └── test_situation.py
├── memory/               # Knowledge base (documented separately)
├── .env.example          # Environment template
├── .gitignore           # Git ignore rules
├── .mcp.json            # MCP server configuration
├── README.md            # Project documentation
├── MCP-REFERENCE.md     # MCP tool reference
└── RUN-PROTOCOL.md      # Evaluation protocol
```

## Key Modules

### 1. Monitor (`sidecar/monitor.py`)

**Purpose**: Main loop that observes game state and triggers analysis.

**Key Functions**:
```python
def main_loop():
    """Main monitoring loop - polls game state at intervals."""
    while not run_length_reached():
        snapshot = take_snapshot()
        alerts = check_urgent_alerts(snapshot)
        if alerts:
            situation = analyze_snapshot(snapshot)
            advice = generate_advice(situation)
            if config.ADVISER_MODE:
                pause_game()
                log_advice(advice)
        sleep(config.SNAPSHOT_INTERVAL)

def take_snapshot() -> dict:
    """Capture full game state via MCP tools."""
    status = mcp_client.get_status()
    colonists = mcp_client.list_colonists()
    resources = mcp_client.get_resources()
    research = mcp_client.get_research()
    alerts = mcp_client.get_alerts()
    conditions = mcp_client.get_conditions()
    return {
        "run_id": config.RUN_ID,
        "day": extract_day(status),
        "colonists": colonists,
        "resources": resources,
        "research": research,
        "alerts": alerts,
        "conditions": conditions
    }

def check_urgent_alerts(snapshot: dict) -> list:
    """Detect urgent threats from snapshot."""
    urgent = []
    for alert in snapshot["alerts"]:
        if alert["severity"] in ["critical", "red"]:
            urgent.append(alert)
    return urgent
```

**Configuration**:
- `SNAPSHOT_INTERVAL = 30` seconds
- `RUN_DAYS = 11` (ends at daysPassed=11)
- `URGENT_ALERTS = ["food", "health", "combat", "mood"]`

### 2. Situation Analyzer (`sidecar/situation.py`)

**Purpose**: Analyze snapshot to identify threats and context.

**Key Functions**:
```python
def analyze_snapshot(snapshot: dict) -> dict:
    """Main analysis entry point."""
    threats = []

    # Check food crisis
    food_days = calculate_food_days(snapshot)
    if food_days < 2:
        threats.append({
            "type": "food_crisis",
            "severity": "urgent",
            "data": {"days_remaining": food_days}
        })

    # Check health crisis
    for colonist in snapshot["colonists"]:
        if colonist["health"] < 0.3:
            threats.append({
                "type": "health_crisis",
                "severity": "urgent",
                "data": {"colonist": colonist["name"], "health": colonist["health"]}
            })

    # Check combat threat
    if any(alert["type"] == "raid" for alert in snapshot["alerts"]):
        threats.append({
            "type": "combat_threat",
            "severity": "urgent",
            "data": get_raid_details(snapshot)
        })

    return {
        "snapshot_id": snapshot["run_id"],
        "day": snapshot["day"],
        "threats": threats,
        "context": extract_context(snapshot)
    }

def calculate_food_days(snapshot: dict) -> float:
    """Calculate days of food remaining."""
    total_meals = snapshot["resources"]["meals"]
    colonist_count = len(snapshot["colonists"])
    meals_per_day = colonist_count * 2  # 2 meals per colonist per day
    return total_meals / meals_per_day if meals_per_day > 0 else 0
```

### 3. Counselor (`sidecar/counselor.py`)

**Purpose**: Generate context-aware advice from lessons.

**Key Functions**:
```python
def generate_advice(situation: dict) -> dict:
    """Generate advice based on situation and lessons."""
    relevant_lessons = select_relevant_lessons(situation)
    recommendations = []

    for lesson in relevant_lessons:
        if lesson_applies(lesson, situation):
            recommendations.append({
                "action": lesson["content"],
                "reason": lesson["trigger"],
                "lesson_id": lesson["id"]
            })

    return {
        "situation": describe_situation(situation),
        "severity": get_max_severity(situation),
        "recommendations": prioritize_actions(recommendations),
        "context": get_context(situation)
    }

def select_relevant_lessons(situation: dict) -> list:
    """Filter lessons by situation type."""
    threat_types = {t["type"] for t in situation["threats"]}
    relevant = []

    for lesson in load_lessons():
        if lesson["category"] in threat_types:
            relevant.append(lesson)

    return relevant

def prioritize_actions(recommendations: list) -> list:
    """Order recommendations by urgency."""
    # Sort by lesson severity and usage stats
    return sorted(
        recommendations,
        key=lambda r: (
            r["severity"],
            -get_lesson_helped_rate(r["lesson_id"])
        )
    )
```

### 4. MCP Client (`sidecar/mcp_client.py`)

**Purpose**: Wrap RimMolt MCP server interactions.

**Key Functions**:
```python
class MCPClient:
    def __init__(self, host: str, port: int):
        self.base_url = f"http://{host}:{port}"
        self.session_id = None

    async def call_tool(self, name: str, arguments: dict) -> dict:
        """Generic MCP tool invocation."""
        payload = {
            "jsonrpc": "2.0",
            "id": generate_id(),
            "method": "tools/call",
            "params": {
                "name": name,
                "arguments": arguments
            }
        }
        response = await httpx.post(self.base_url, json=payload)
        return response.json()

    async def get_status(self) -> dict:
        """Get overall game status."""
        return await self.call_tool("get_status", {})

    async def list_colonists(self) -> list:
        """Get all colonists."""
        return await self.call_tool("list_colonists", {})

    async def get_resources(self) -> dict:
        """Get resource counts."""
        return await self.call_tool("get_resources", {})

    async def set_speed(self, paused: bool) -> dict:
        """Pause or unpause game."""
        return await self.call_tool("set_speed", {"paused": paused})
```

### 5. Lesson Store (`sidecar/lessons.py`)

**Purpose**: Manage persistent lesson store.

**Key Functions**:
```python
def load_lessons() -> list:
    """Load all lessons from JSONL file."""
    lessons = []
    with open("memory/lessons.jsonl", "r") as f:
        for line in f:
            lessons.append(json.loads(line))
    return lessons

def validate() -> bool:
    """Validate lesson store against schema."""
    schema = load_schema("schemas/lesson.schema.json")
    lessons = load_lessons()

    for lesson in lessons:
        if not validate_schema(lesson, schema):
            return False

    return True

def record_outcome(lesson_id: str, outcome: str):
    """Update lesson usage statistics."""
    lessons = load_lessons()
    for lesson in lessons:
        if lesson["id"] == lesson_id:
            lesson["used_count"] += 1
            if outcome == "helped":
                lesson["helped_count"] += 1
            elif outcome == "failed":
                lesson["failed_count"] += 1
            break

    save_lessons(lessons)
```

### 6. Debrief Bundle (`sidecar/debrief_bundle.py`)

**Purpose**: Compile snapshots into structured analysis bundle.

**Key Functions**:
```python
def generate_bundle(run_id: str) -> dict:
    """Generate debrief bundle from snapshots."""
    snapshots = load_snapshots(run_id)

    bundle = {
        "run_id": run_id,
        "section_1_setup": extract_setup(snapshots[0]),
        "section_2_timeline": build_timeline(snapshots),
        "section_3_incidents": extract_incidents(snapshots),
        "section_4_resources": analyze_resources(snapshots),
        "section_5_questions": generate_questions(snapshots)
    }

    return bundle

def build_timeline(snapshots: list) -> list:
    """Build day-by-day timeline."""
    timeline = []
    for snapshot in snapshots:
        day_events = {
            "day": snapshot["day"],
            "events": extract_events(snapshot),
            "decisions": extract_decisions(snapshot),
            "outcomes": extract_outcomes(snapshot)
        }
        timeline.append(day_events)
    return timeline

def extract_incidents(snapshots: list) -> list:
    """Extract key incidents from all snapshots."""
    incidents = []
    for snapshot in snapshots:
        for alert in snapshot["alerts"]:
            if alert["severity"] in ["critical", "red"]:
                incidents.append({
                    "day": snapshot["day"],
                    "type": alert["type"],
                    "description": alert["description"]
                })
    return incidents
```

### 7. Evaluation (`sidecar/evaluate.py`)

**Purpose**: Score debrief quality against rubric.

**Key Functions**:
```python
def score_debrief(debrief_response: str, rubric_path: str) -> dict:
    """Score debrief response against rubric."""
    rubric = load_rubric(rubric_path)

    scores = {}
    for category, criteria in rubric.items():
        score = assess_category(debrief_response, criteria)
        scores[category] = score

    return {
        "total": sum(scores.values()) / len(scores),
        "by_category": scores
    }

def assess_category(response: str, criteria: dict) -> float:
    """Assess a single category."""
    # Use LLM to assess response against criteria
    prompt = f"""
    Assess this response against these criteria:
    {criteria}

    Response:
    {response}

    Return a score from 0-5.
    """
    score = llm.complete(prompt)
    return float(score)
```

## LLM Integration

### Abstraction Layer (`sidecar/llm.py`)

```python
class LLMClient:
    def __init__(self, base_url: str, model: str):
        self.base_url = base_url
        self.model = model

    def complete(self, prompt: str) -> str:
        """Generate completion from prompt."""
        response = ollama.generate(
            model=self.model,
            prompt=prompt,
            host=self.base_url
        )
        return response["response"]
```

### Ollama Configuration

Environment variables (`.env`):
```
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama3.2
```

### Usage Patterns

**Advice Generation**:
```python
llm = LLMClient(
    base_url=os.getenv("OLLAMA_BASE_URL"),
    model=os.getenv("OLLAMA_MODEL")
)

prompt = f"""
Generate advice for this situation:
{situation}

Relevant lessons:
{lessons}

Provide specific, actionable recommendations.
"""
advice = llm.complete(prompt)
```

**Debrief Analysis**:
```python
prompt = f"""
Analyze this RimWorld run:
{debrief_bundle}

Identify:
1. What went well
2. What went poorly
3. Key lessons learned
4. Recommended improvements
"""
analysis = llm.complete(prompt)
```

## Configuration

### Environment Variables (`.env`)

```bash
# MCP Server
MCP_HOST=localhost
MCP_PORT=8787

# LLM
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama3.2

# Monitor
RUN_ID=run-001
ADVISER_MODE=true

# Paths
MEMORY_PATH=memory
SNAPSHOT_PATH=memory/snapshots
ADVICE_PATH=memory/advice
```

### Config Module (`sidecar/config.py`)

```python
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    MCP_HOST = os.getenv("MCP_HOST", "localhost")
    MCP_PORT = int(os.getenv("MCP_PORT", "8787"))
    OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
    OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.2")
    RUN_ID = os.getenv("RUN_ID", "default")
    ADVISER_MODE = os.getenv("ADVISER_MODE", "true").lower() == "true"

    RUN_DAYS = 11
    SNAPSHOT_INTERVAL = 30
    URGENT_ALERTS = ["food", "health", "combat", "mood"]
```

## Data Validation

### JSON Schemas

All data structures are validated against schemas in `schemas/`:

**Snapshot Schema** (`schemas/snapshot.schema.json`):
```json
{
  "type": "object",
  "required": ["run_id", "day", "colonists", "resources", "alerts"],
  "properties": {
    "run_id": {"type": "string"},
    "day": {"type": "integer"},
    "colonists": {"type": "array"},
    "resources": {"type": "object"},
    "alerts": {"type": "array"}
  }
}
```

**Lesson Schema** (`schemas/lesson.schema.json`):
```json
{
  "type": "object",
  "required": ["id", "title", "trigger", "content", "category"],
  "properties": {
    "id": {"type": "string"},
    "title": {"type": "string"},
    "trigger": {"type": "string"},
    "content": {"type": "string"},
    "category": {"type": "string"},
    "severity": {"type": "string"},
    "created": {"type": "string"},
    "used_count": {"type": "integer"},
    "helped_count": {"type": "integer"},
    "failed_count": {"type": "integer"}
  }
}
```

**Advice Schema** (`schemas/advice.schema.json`):
```json
{
  "type": "object",
  "required": ["situation", "severity", "recommendations"],
  "properties": {
    "situation": {"type": "string"},
    "severity": {"type": "string"},
    "recommendations": {"type": "array"},
    "context": {"type": "string"}
  }
}
```

### Validation Functions

```python
from jsonschema import validate, ValidationError

def validate_snapshot(snapshot: dict) -> bool:
    """Validate snapshot against schema."""
    schema = load_schema("schemas/snapshot.schema.json")
    try:
        validate(instance=snapshot, schema=schema)
        return True
    except ValidationError:
        return False

def validate_lesson(lesson: dict) -> bool:
    """Validate lesson against schema."""
    schema = load_schema("schemas/lesson.schema.json")
    try:
        validate(instance=lesson, schema=schema)
        return True
    except ValidationError:
        return False
```

## Error Handling

### MCP Connection Errors

```python
async def call_tool_with_retry(name: str, arguments: dict, max_retries: int = 3):
    """Call MCP tool with retry logic."""
    for attempt in range(max_retries):
        try:
            return await mcp_client.call_tool(name, arguments)
        except ConnectionError:
            if attempt == max_retries - 1:
                raise
            await asyncio.sleep(2 ** attempt)  # Exponential backoff
```

### Snapshot Validation Errors

```python
def take_snapshot_safe() -> dict:
    """Take snapshot with validation fallback."""
    try:
        snapshot = take_snapshot()
        if not validate_snapshot(snapshot):
            log_error("Invalid snapshot data")
            return None
        return snapshot
    except Exception as e:
        log_error(f"Snapshot failed: {e}")
        return None
```

### LLM Timeout Errors

```python
def complete_with_timeout(prompt: str, timeout: int = 60) -> str:
    """Generate completion with timeout."""
    try:
        return llm.complete(prompt)
    except TimeoutError:
        log_error("LLM timeout, using cached response")
        return get_cached_response(prompt)
```

## Testing

### Test Structure

```python
# test_situation.py
def test_food_crisis_detection():
    snapshot = {
        "resources": {"meals": 5},
        "colonists": [{"name": "A"}, {"name": "B"}, {"name": "C"}]
    }
    situation = analyze_snapshot(snapshot)
    assert any(t["type"] == "food_crisis" for t in situation["threats"])

def test_health_crisis_detection():
    snapshot = {
        "colonists": [
            {"name": "A", "health": 0.8},
            {"name": "B", "health": 0.2}  # Critical
        ]
    }
    situation = analyze_snapshot(snapshot)
    assert any(t["type"] == "health_crisis" for t in situation["threats"])
```

### Running Tests

```bash
# Run all tests
python -m pytest

# Run with coverage
python -m pytest --cov=sidecar

# Run specific test
python -m pytest tests/test_situation.py::test_food_crisis_detection
```

## Performance Considerations

### Snapshot Interval
- Default: 30 seconds
- Trade-off: More frequent = better threat detection, higher CPU load
- Configurable via `SNAPSHOT_INTERVAL`

### LLM Latency
- Local Ollama: ~2-5 seconds per completion
- Mitigation: Cache common responses, batch requests
- Future: Consider smaller models for real-time advice

### Memory Usage
- Snapshots: ~5-10 KB each
- 10-day run: ~50-100 KB total
- Wiki cache: ~5 MB
- Lesson store: < 100 KB

## Future Technical Enhancements

Planned improvements:
- Async MCP client for concurrent tool calls
- Snapshot compression for long-term storage
- Lesson versioning and A/B testing
- Streaming LLM responses for faster feedback
- Metrics dashboard for real-time monitoring
- Integration with CI/CD for automated testing
