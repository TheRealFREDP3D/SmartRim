# SmartRim Project Overview

## Vision

SmartRim is an autonomous RimWorld sidecar that observes colony state through the RimMolt MCP server, maintains a persistent lesson store, and advises (or pauses) on threats. The ultimate goal is a system that **auto-plays RimWorld**, with the human as a spectator who can intervene at any time.

## What is RimWorld?

RimWorld is a colony management simulation game where players manage survivors on a procedurally generated planet. The game features:
- Complex AI storytellers that create dynamic challenges
- Deep simulation of colonist needs, health, and social interactions
- Combat system with raids, wildlife, and faction interactions
- Research progression and technology trees
- Multiple DLCs (Royalty, Ideology, Biotech, Anomaly) adding mechanics

## SmartRim Architecture

SmartRim operates as a Python sidecar that:
1. **Observes** game state via RimMolt MCP server (JSON-RPC over HTTP on localhost:8787)
2. **Monitors** colony state continuously, taking snapshots at regular intervals
3. **Evaluates** situations against a lesson store of known threats and best practices
4. **Advises** the human player (or pauses the game) when threats are detected
5. **Learns** from each run through debriefing and lesson refinement

## Key Components

### Sidecar (Python)
- `monitor.py` - Main reflex monitor, takes snapshots, detects threats
- `situation.py` - Analyzes game state and identifies dangerous situations
- `counselor.py` - Generates advice based on lessons and context
- `lessons.py` - Manages the persistent lesson store
- `mcp_client.py` - Wraps RimMolt MCP server interactions
- `debrief.py` - Post-run analysis and lesson extraction
- `evaluate.py` - Scores debrief responses against rubric

### Schemas (JSON)
- `snapshot.schema.json` - Game state snapshot structure
- `lesson.schema.json` - Lesson definition and structure
- `advice.schema.json` - Advice output format

### Memory (Knowledge Base)
- `lessons.jsonl` - Persistent lesson store
- `phases.md` - Game phase definitions
- `wiki/` - Cached RimWorld wiki pages for reference
- `session-logs/` - Detailed run records
- `snapshots/` - Runtime game state captures (gitignored)

### Tests
- Pytest suite validating all components
- Protocol compliance tests
- Integration tests with mock MCP server

## Current Status

SmartRim is in active development. It successfully:
- Connects to RimWorld via RimMolt MCP
- Monitors colony state with configurable intervals
- Detects urgent alerts (food shortages, health crises, combat threats)
- Generates context-aware advice from lessons
- Completes 10-day evaluation runs under fixed protocol

## Evaluation Protocol

To ensure comparable results, all evaluation runs follow a strict protocol:
- **Scenario**: Crashlanded (3 colonists)
- **Storyteller**: Cassandra Classic
- **Difficulty**: Adventure Story
- **Run length**: 10 full days (ends at daysPassed=11)
- **Ideoligion**: Fluid, generated defaults
- **Tile**: Flat temperate forest
- **No reloading** during runs

Metrics compared across runs:
- Days survived within 10-day window
- Colonists alive at day 10
- Lowest mood reached
- Days until first low-food and medicine alerts
- Number of urgent alerts and auto-pauses
- Advice effectiveness (helped/failed counts)

## Getting Started

1. Install Python 3.13+ and create a venv
2. Copy `.env.example` to `.env` and configure
3. Start RimWorld with RimMolt mod (MCP server on localhost:8787)
4. Run tests: `python -m pytest`
5. Validate lessons: `python sidecar/lessons.py validate`
6. Start monitor: `.\start-monitor.ps1` (adviser on) or `.\start-monitor.ps1 -ObserveOnly`

## Repository Structure

```
SmartRim/
├── sidecar/          # Python sidecar modules
├── schemas/          # JSON schemas
├── memory/           # Knowledge base (gitignored runtime data)
├── tests/            # Pytest suite
├── scratchpad/       # One-off scripts (gitignored)
├── .notebooklm/      # NotebookLM sources (this directory)
├── README.md         # Project documentation
├── MCP-REFERENCE.md  # MCP tool reference
└── RUN-PROTOCOL.md   # Evaluation protocol
```

## Future Vision

The project is evolving from "advisor-only" to full auto-play. Future phases will:
- Directly issue orders via MCP tools
- Make autonomous decisions on base building, research, and priorities
- Handle complex multi-step strategies
- Optimize colony performance over long timescales
