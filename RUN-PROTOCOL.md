# Run protocol

Every comparable run follows this protocol. A run that breaks it is recorded as a different run, not as a member of the comparison set.

## Fixed settings

| Setting | Value | Why |
|---|---|---|
| Scenario | Crashlanded | Same starting team size as Sessions 1–3 |
| Storyteller | Cassandra Classic | Baseline (wiki: AI_Storytellers) |
| Difficulty | Adventure story | Baseline (wiki threat scale 60%, research speed 100%) |
| Reload mode | Reload anytime (required by the game setup), but **no reloading during a run** | Keeps save-scumming out of the comparison |
| Run length | The 1st day is Day 1; 10 full days complete after it. Ends when `daysPassed` reaches 11 (`RUN_DAYS=11`) | Fixed length for comparison |
| Ideoligion | Fluid, generated defaults, no edits | Keeps setup time equal |
| Tile | Flat temperate forest, record the tile id in the session log | Same biome for every run |
| Starting team | Pick by rule: no incapable of Violent or Caring among the three fighters/doctors; record the names | Avoids team quality as a hidden variable |

Day counting: the run starts on the 1st day (`daysPassed` = 0). Ten full days must complete after it, so the run ends when `daysPassed` from `get_status` reaches 11. The monitor enforces this (`sidecar/monitor.py`, `run_length_reached`, `RUN_DAYS` in `sidecar/config.py`).

## Start

1. Start RimWorld and load the MCP server (RimMolt mod).
2. Start the run's monitor with a fresh run id. Evaluation runs alternate adviser on, then off.
   ```powershell
   $env:RUN_ID = "run-NNN-adv-cassandra"   # NNN = next run number
   .\start-monitor.ps1                     # adviser on: pauses and logs advice
   .\start-monitor.ps1 -ObserveOnly        # adviser off: snapshots only, no pause, no advice
   ```
3. Create the colony with the fixed settings above. Record the tile id and team names in `memory/session-logs/<run-id>.md`.
4. Confirm the monitor log shows `Reflex monitor started` with the run id.

## During the run

- Advance time with `wait_for_event` or real-time waits. Never bare-unpause at speed.
- Record every decision you make in-game with `say` (the human can see them).
- The monitor auto-pauses on urgent alerts. When it pauses, log the response in the advice log (`sidecar/advice_log.py update <id> <status> <note>`).
- No reloading, no restarting the colony, no manual save-scumming. If the run is broken, end it and start a new run id.

## End

1. The monitor pauses the game at 10 days, writes the final snapshot, and writes `memory/runs/<run-id>.end.json`. Confirm the marker exists.
2. Update the advice log outcomes for any open records.
3. Write the session log (`memory/session-logs/<run-id>.md`): setup, timeline by day, decisions, outcome, and what surprised you.
4. Generate the debrief bundle: `python sidecar/debrief.py <run-id>`. Paste the bundle into the chosen model, record the answer in the response file, and score it with `memory/debrief-rubric.md`.
5. Commit the session log and the run-end marker (snapshots and debriefs stay gitignored).
6. End the session. Do not continue the colony past day 10.

## What is compared across runs

- Days survived within the 10-day window (all runs should reach 10 unless they end early).
- Colonists alive at day 10, lowest mood reached, and whether any downed or mental break happened.
- Days until the first low-food and first medicine alerts.
- Number of urgent alerts and auto-pauses, and how many advice records were marked helped or failed.

These are the only metrics defined so far. Phase 2's evaluation harness (`PHASE2-PLAN.md`) will use them.

## Decisions

- Run length: 10 full days after the 1st day (ends at `daysPassed` 11). Confirmed.
- Reloads: none during a run (no-reload rule). Confirmed. The game still requires a reload-mode choice at setup; that choice is recorded as "anytime" but is not used.
