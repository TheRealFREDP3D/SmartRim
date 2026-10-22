# SmartRim Run Protocol and Evaluation

## Purpose

The run protocol ensures all evaluation runs are comparable and scientifically valid. It standardizes game settings, run length, and decision-making rules so that improvements can be measured objectively.

## Fixed Settings

| Setting | Value | Rationale |
|---------|-------|-----------|
| Scenario | Crashlanded | 3 colonists, balanced start - same as early sessions |
| Storyteller | Cassandra Classic | Baseline storyteller with predictable escalation |
| Difficulty | Adventure Story | 60% threat scale, 100% research speed - baseline difficulty |
| Reload Mode | Reload Anytime (but no reloading during run) | Required by game setup, but no save-scumming allowed |
| Run Length | 10 full days (ends at daysPassed=11) | Fixed window for comparison |
| Ideoligion | Fluid, generated defaults, no edits | Keeps setup time equal across runs |
| Tile | Flat temperate forest (record tile ID) | Same biome for every run |
| Starting Team | No incapable of Violent or Caring among fighters/doctors | Avoids team quality as hidden variable |

## Day Counting

The run starts on Day 1 (when `daysPassed` = 0). Ten full days must complete after it, so the run ends when `daysPassed` from `get_status` reaches 11.

The monitor enforces this automatically in `sidecar/monitor.py` via the `run_length_reached()` function.

## Run Types

Evaluation runs alternate between two modes:

### Adviser On
- Monitor pauses game on urgent alerts
- Advice is generated and logged
- Human can review advice before acting
- Tests the full advisory system

### Adviser Off (Observe Only)
- Monitor takes snapshots only
- No pauses, no advice generation
- Pure observation mode
- Provides baseline data for comparison

## Starting a Run

### Step 1: Start RimWorld with RimMolt
- Launch RimWorld with RimMolt mod loaded
- Verify MCP server is running on localhost:8787
- Confirm connection: `notebooklm status` or MCP helper script

### Step 2: Start the Monitor
```powershell
# Set unique run ID
$env:RUN_ID = "run-001-adv-cassandra"

# Adviser on (default)
.\start-monitor.ps1

# Adviser off (observe only)
.\start-monitor.ps1 -ObserveOnly
```

### Step 3: Create Colony
- Use fixed settings from table above
- Record tile ID in session log
- Record colonist names in session log
- Choose starting team following "no incapable" rule

### Step 4: Verify Monitor
- Check `memory/monitor.log` shows "Reflex monitor started"
- Confirm run ID is correct
- Verify MCP connection is stable

## During the Run

### Time Advancement Rules
- **Always** use `wait_for_event` or real-time waits
- **Never** bare-unpause at game speed
- This ensures the monitor can detect threats promptly

### Decision Recording
- Record every in-game decision using the `say` MCP tool
- Human can see these messages in the AI window
- Example: `Say-Message "Prioritizing rice planting over construction"`

### Alert Handling
- Monitor auto-pauses on urgent alerts (adviser mode only)
- When paused, log the response:
  ```bash
  python sidecar/advice_log.py update <advice-id> <status> <note>
  ```
  Status options: `helped`, `failed`, `ignored`, `deferred`

### Run Integrity Rules
- **No reloading** during a run
- **No restarting** the colony
- **No manual save-scumming**
- If the run is broken (crash, bug, protocol violation), end it and start a new run ID

## Ending a Run

### Step 1: Confirm Completion
- Monitor automatically pauses at day 10
- Verify `memory/runs/<run-id>.end.json` exists
- This marker confirms the run completed properly

### Step 2: Update Advice Log
- Resolve any open advice records
- Mark final outcomes for all advice
- Close pending records with appropriate status

### Step 3: Record Event Causes
The bundle can see symptoms but not causes. Tag incidents:
```bash
# Match multiple incidents to a cause (e.g., raid with multiple fires)
python sidecar/advice_log.py cause-match <run-id> fire "raider arson"

# Tag single advice record
python sidecar/advice_log.py cause <advice-id> "quest target downed before extraction"
```

Ask the player what happened whenever the cause is not obvious from game text.

### Step 4: Write Session Log
Create `memory/session-logs/<run-id>.md` with:
- Setup (scenario, storyteller, tile, colonists)
- Timeline by day (major events, decisions)
- Outcome (colonists alive, resources, incidents)
- Surprises (unexpected events, decisions that worked poorly)

### Step 5: Generate Debrief Bundle
```bash
python sidecar/debrief.py <run-id>
```
- Verify bundle includes quest context (if applicable)
- If quest involved but not in bundle, add to `memory/runs/<run-id>.meta.json`
- Check that recorded causes appear in bundle

### Step 6: Score Debrief
- Paste bundle into chosen LLM
- Record answer in response file
- Score with `memory/debrief-rubric.md`
- Ask player for corrections before finalizing score

### Step 7: Commit and Archive
- Commit session log and run-end marker
- Snapshots and debriefs remain gitignored
- Archive completed runs by copying snapshot directory before starting new run

### Step 8: End Session
- Do not continue the colony past day 10
- Close RimWorld or return to main menu
- Stop the monitor

## Comparison Metrics

These metrics are compared across all runs to measure improvement:

### Survival Metrics
- **Days survived** within 10-day window (all runs should reach 10 unless early failure)
- **Colonists alive** at day 10
- **Lowest mood reached** during run
- **Mental breaks** - whether any occurred
- **Downed colonists** - count and duration

### Resource Metrics
- **Days until first low-food alert**
- **Days until first medicine alert**
- **Food stores at day 10** (days of food remaining)
- **Steel/wood at day 10**

### Alert Metrics
- **Total urgent alerts** during run
- **Auto-pauses** (adviser mode only)
- **Advice records** - total generated
- **Advice helped** - count
- **Advice failed** - count
- **Advice ignored/deferred** - count

### Phase 2 Metrics (Future)
The evaluation harness (`PHASE2-PLAN.md`) will add:
- Colonist happiness trends
- Work efficiency metrics
- Base quality scores
- Research progress rate
- Resource utilization efficiency

## Protocol Decisions

### Run Length: 10 Days
**Decision:** Fixed length of 10 full days after Day 1 (ends at daysPassed=11)
**Rationale:**
- Long enough to see early game threats (first raid, food crisis)
- Short enough for rapid iteration
- Avoids mid-game complexity that obscures early-game learning
- Confirmed by project review

### Reloads: None During Run
**Decision:** No reloading, no restarting, no save-scumming
**Rationale:**
- Reloads make runs incomparable
- Save-scumming defeats the purpose of learning from failure
- Forces the system to handle adversity
- Confirmed by project review

### Reload Mode at Setup
**Decision:** Game requires reload mode choice; recorded as "anytime" but not used
**Rationale:**
- RimWorld requires a reload mode at setup
- Recording the choice documents the configuration
- Actual reloading is prohibited by protocol
- This is a game constraint, not a project decision

### Starting Team Rule
**Decision:** No colonists incapable of Violent or Caring among fighters/doctors
**Rationale:**
- Incapable of Violent = can't fight = guaranteed death in raids
- Incapable of Caring = can't doctor = high risk of death from wounds
- These traits create hidden difficulty variables
- Rule ensures comparable team quality

## Protocol Violations

A run is invalid and must be restarted if:
- Any fixed setting is changed
- Reloading occurs during the run
- Monitor crashes and is restarted mid-run
- Game crashes and is reloaded from a save
- MCP connection is lost and not recovered
- Run length is extended or shortened

If a violation occurs:
1. End the current run immediately
2. Document the violation in the session log
3. Start a new run with a new run ID
4. Do not include the invalid run in comparisons

## Documentation

All runs are documented in:
- `memory/session-logs/<run-id>.md` - Narrative log
- `memory/runs/<run-id>.end.json` - Completion marker
- `memory/runs/<run-id>.meta.json` - Metadata (quests, causes)
- `memory/snapshots/day-<N>.json` - Runtime state (gitignored)
- `memory/advice/<id>.json` - Advice records (gitignored)
- `memory/debriefs/<run-id>.json` - Debrief bundle (gitignored)

## Version History

### Initial Protocol (RUN-PROTOCOL.md)
- Defined fixed settings and 10-day run length
- Established no-reload rule
- Created comparison metrics
- Documented start/end procedures

### Current Version
- Added adviser on/off alternation
- Clarified day counting (daysPassed=11)
- Added event cause tagging
- Standardized session log format
- Added protocol violation handling
