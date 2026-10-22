# SmartRim Memory and Knowledge Base

## Overview

The `memory/` directory is SmartRim's persistent knowledge store. It contains lessons, game knowledge, session logs, and runtime data. Some files are version-controlled (lessons, wiki cache, session logs), while runtime data (snapshots, advice, debriefs) is gitignored to avoid bloating the repository.

## Directory Structure

```
memory/
├── README.md              # This directory's documentation
├── lessons.jsonl          # Persistent lesson store (versioned)
├── phases.md              # Game phase definitions
├── mechanics.md          # Core game mechanics reference
├── base-design.md         # Base building strategies
├── beginner-guide.md      # Beginner strategy guide
├── colonist-management.md # Colonist roles and priorities
├── combat.md              # Combat tactics
├── research-tree.md       # Research priorities
├── debrief-rubric.md      # Debrief evaluation rubric
├── lessons-learned.md     # Compiled learnings from runs
├── model-scores.md        # LLM performance tracking
├── eval-2026-10-19.md     # Evaluation report
├── wiki-audit-20261018.md # Wiki cache audit
├── wiki/                  # Cached RimWorld wiki pages
│   ├── AI_Storytellers.md
│   ├── Animals.md
│   ├── Food.md
│   ├── Research.md
│   └── ... (200+ pages)
├── dlc/                   # DLC-specific documentation
│   ├── royalty/README.md
│   ├── ideology/README.md
│   ├── biotech/README.md
│   └── anomaly/README.md
├── session-logs/          # Detailed run records
│   ├── session-1.md
│   ├── session-2.md
│   └── ...
├── snapshots/             # Runtime game state (gitignored)
├── debriefs/              # Debrief bundles (gitignored)
├── advice/                # Advice records (gitignored)
├── alerts/                # Alert logs (gitignored)
├── runs/                  # Run metadata (gitignored)
│   ├── <run-id>.end.json
│   └── <run-id>.meta.json
└── monitor.log            # Monitor runtime log (gitignored)
```

## Lesson Store (`lessons.jsonl`)

The lesson store is SmartRim's core knowledge - a JSONL file containing validated lessons that the system uses to generate advice.

### Lesson Structure

Each line is a JSON object:
```json
{
  "id": "unique-lesson-id",
  "title": "Lesson title",
  "trigger": "When this lesson applies",
  "content": "Lesson content/advice",
  "severity": "urgent|warning|info",
  "category": "food|health|combat|mood|base|research",
  "created": "2026-10-21T00:00:00Z",
  "used_count": 0,
  "helped_count": 0,
  "failed_count": 0
}
```

### Lesson Categories

- **food**: Food production, storage, meals
- **health**: Medical care, wounds, disease
- **combat**: Raids, wildlife, defense
- **mood**: Mental breaks, needs, recreation
- **base**: Building, power, temperature
- **research**: Technology priorities

### Lesson Lifecycle

1. **Creation**: Added manually or extracted from debrief analysis
2. **Validation**: Checked against schema and reviewed
3. **Use**: Retrieved by counselor when trigger matches
4. **Outcome**: Tracked as helped/failed/ignored
5. **Refinement**: Updated based on performance data

### Managing Lessons

```bash
# Validate lesson store
python sidecar/lessons.py validate

# Search lessons by category
python sidecar/lessons.py search --category food

# Record outcome
python sidecar/lessons.py record_outcome <lesson-id> helped
```

## Game Knowledge Files

### Core Documentation

**`phases.md`** - Defines game phases:
- Early game (Days 1-5): Survival setup
- Mid game (Days 6-15): First raids, expansion
- Late game (Days 16+): Advanced threats, DLC content

**`mechanics.md`** - Core game mechanics:
- Needs system (hunger, rest, mood)
- Work priorities and time management
- Temperature and power
- Wealth and threat scaling

**`base-design.md`** - Base building strategies:
- Room layouts (bedrooms, kitchen, hospital)
- Zoning and stockpiles
- Power grid design
- Defense structures

**`beginner-guide.md`** - Beginner strategy:
- Day 1 checklist
- Colonist role assignment
- Critical rules (pause often, freeze food, etc.)
- First 30 days plan

**`colonist-management.md`** - Colonist optimization:
- Skill prioritization
- Work tab configuration
- Schedule management
- Trait handling

**`combat.md`** - Combat tactics:
- Drafting and positioning
- Cover usage
- Focus-fire strategy
- Post-raid cleanup

**`research-tree.md`** - Research priorities:
- Early research path
- Key technologies and timing
- DLC research considerations

### Evaluation Documentation

**`debrief-rubric.md`** - Scoring criteria for debriefs:
- Accuracy of cause identification
- Completeness of timeline
- Actionability of recommendations
- Insightfulness of observations

**`lessons-learned.md`** - Compiled insights from runs:
- What works well
- Common failure modes
- Recommended adjustments

**`model-scores.md`** - LLM performance tracking:
- Model name and version
- Scores on debrief rubric
- Comparison across models

**`eval-2026-10-19.md`** - Evaluation report:
- Run results summary
- Metric comparisons
- Lessons extracted

## Wiki Cache (`wiki/`)

The wiki cache contains cached RimWorld wiki pages for offline reference. This ensures SmartRim has access to accurate game knowledge without relying on live web access.

### Cache Contents

200+ wiki pages covering:
- Game mechanics (Needs, Work, Time)
- Items and materials (Steel, Wood, Cloth, etc.)
- Buildings (Beds, Tables, Coolers, etc.)
- Plants and crops (Rice, Potatoes, etc.)
- Animals (Wild and tame)
- Health and medicine
- Research projects
- DLC content (Royalty, Ideology, Biotech, Anomaly)

### Cache Management

```bash
# Audit cache completeness
# See memory/wiki-audit-20261018.md

# Refresh cache (if needed)
# Use rimworld-wiki skill to fetch updates
```

### Wiki Audit

The cache was audited on 2026-10-18 (`wiki-audit-20261018.md`):
- Verified coverage of core mechanics
- Checked for outdated pages
- Identified gaps in DLC content
- Recommended additions

## DLC Documentation (`dlc/`)

Each DLC has a dedicated README with:
- Key mechanics introduced
- New tools available via MCP
- Integration considerations
- Specific lessons learned

### Royalty (`dlc/royalty/README.md`)
- Royal titles and honor system
- Psychic abilities
- New threats (Empire raids)
- Monument quests

### Ideology (`dlc/ideology/README.md`)
- Ideoligion creation and customs
- Memes and precepts
- Rituals and ceremonies
- Social structure impact

### Biotech (`dlc/biotech/README.md`)
- Xenotypes and genes
- Mechanitors and mechanoids
- Child rearing
- Pollution mechanics

### Anomaly (`dlc/anomaly/README.md`)
- Void monolith and entities
- Study system
- Anomalous events
- New combat threats

## Session Logs (`session-logs/`)

Session logs are detailed narrative records of each run. They document:
- Setup (scenario, storyteller, tile, colonists)
- Timeline by day (events, decisions, outcomes)
- Major incidents and causes
- Surprises and unexpected events
- Final state and lessons learned

### Session Log Format

```markdown
# Session <N> — <date>

## Setup
- Scenario: ...
- Storyteller: ...
- Difficulty: ...
- Tile: ...
- Colonists: ...

## Timeline

### Day 1
- Events: ...
- Decisions: ...
- Outcome: ...

### Day 2
...

## Outcome
- Colonists alive: ...
- Resources: ...
- Incidents: ...

## Surprises
- ...

## Lessons Learned
- ...
```

### Examples

- `session-1.md` - Initial MCP connection test
- `session-2.md` - First full colony run
- `session-3.md` - Day 3 save (wild sparrow incident)
- `session-5.md` - Day 7 completion (first raid survived)
- `run-002-adv-cassandra.md` - Evaluation run with adviser

## Runtime Data (Gitignored)

### Snapshots (`snapshots/`)

Snapshots are structured game state captures taken by the monitor:
- `day-1.json` - State at end of Day 1
- `day-2.json` - State at end of Day 2
- ...
- Up to `day-10.json` for a complete run

**Snapshot Structure** (validated against `schemas/snapshot.schema.json`):
```json
{
  "run_id": "run-001",
  "day": 1,
  "daysPassed": 1,
  "colonists": [...],
  "resources": {...},
  "buildings": [...],
  "alerts": [...],
  "research": {...},
  "conditions": {...}
}
```

Snapshots are gitignored because:
- They are large (several KB each)
- They are runtime artifacts, not source
- They can be regenerated from saved games
- They would bloat the repository

### Debriefs (`debriefs/`)

Debrief bundles are generated from snapshots for post-run analysis:
- `<run-id>.json` - Complete debrief bundle
- Used for LLM analysis
- Used for lesson extraction

### Advice (`advice/`)

Advice records are generated when the counselor detects threats:
- `<timestamp>.json` - Individual advice
- Linked to lesson IDs
- Tracked for outcome (helped/failed)

### Alerts (`alerts/`)

Alert logs track urgent alerts detected by the monitor:
- `<timestamp>.json` - Alert details
- Used for metric tracking
- Helps identify alert patterns

### Runs (`runs/`)

Run metadata tracks run completion and context:
- `<run-id>.end.json` - Completion marker
- `<run-id>.meta.json` - Additional metadata (quests, causes)

### Monitor Log (`monitor.log`)

The monitor log is a continuous runtime log:
- Startup and shutdown events
- MCP connection status
- Snapshot timestamps
- Alert detections
- Advice generation
- Errors and warnings

## Memory Management

### Cleanup

Periodic cleanup of gitignored data:
```bash
# Archive completed runs before starting new ones
# Copy memory/snapshots/ to external storage
# Delete old snapshots from memory/snapshots/

# Clear old advice/alert logs
# Keep current run, archive older ones
```

### Backup

Version-controlled data is backed up via git:
- `lessons.jsonl`
- `phases.md`, `mechanics.md`, etc.
- `wiki/` cache
- `session-logs/`

Runtime data should be archived manually:
- Snapshots from important runs
- Debriefs with high scores
- Session logs with significant learnings

## Access Patterns

### During a Run
- Monitor writes to `snapshots/`
- Counselor writes to `advice/`
- Monitor appends to `monitor.log`
- Alert detection writes to `alerts/`

### Post-Run
- Debrief reads from `snapshots/`
- Debrief writes to `debriefs/`
- Lesson extraction updates `lessons.jsonl`
- Session log written to `session-logs/`

### Lesson Retrieval
- Counselor reads `lessons.jsonl`
- Filters by trigger and category
- Updates usage counts
- Records outcomes

## Future Enhancements

Planned improvements to the memory system:
- Lesson versioning and A/B testing
- Automated lesson pruning based on performance
- Wiki cache auto-refresh
- Session log search and analytics
- Snapshot compression for long-term storage
- Debrief bundle versioning for comparison
