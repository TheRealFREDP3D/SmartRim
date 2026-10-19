# Phase 1 plan: finish the sidecar and close the feedback loop

Source: `New plan.md`, Phase 1. Facts are checked against `memory/wiki/` (wiki is the source of truth).
Status at start: the game is on the main menu. Phase 1 work does not need the game, except for the live tests in step 7.

## Goal

By the end of Phase 1 the sidecar should:

1. Watch the colony reliably, with no silent failures.
2. Raise reflex alerts for the failures that killed earlier colonies (food, medicine, downed or bleeding colonists, predators near workers, mood breaks).
3. Write a snapshot every game day, with the run's difficulty and storyteller recorded.
4. Log every piece of advice and, later, its outcome.
5. Turn each run's debrief into candidate lessons, reviewed by a human before they enter `lessons-learned.md`.

Phase 1 does not include a lesson database, a retrieval engine, or the C# mod. Those are Phase 2 and 3.

## Decisions needed before step 4

1. **LLM for the debrief.** Use an API key via `.env` (provider and model), or keep the debrief template-only for now? The debrief works without an LLM.
2. **Auto-pause scope.** Auto-pause only on urgent alerts (downed, extreme mood, colony death, hostile near a colonist). Food and medicine warnings stay advisory. Agree or change?
3. **Baseline difficulty.** Run the next colony on Adventure story with Cassandra Classic (the wiki's baseline, threat scale 60%) so it compares with Sessions 1–3? Community builder (threat 30%, research 120%) is easier but does not compare with Sessions 1–3.

## Work breakdown

### Step 0: Contracts (0.5 day)

- `schemas/snapshot.schema.json`: fields for run id, day, hour, difficulty, storyteller, biome, colonists (id, name, health, mood, downed, job, incapable), resources, food_days (projected), research, alerts.
- `schemas/advice.schema.json`: advice id, timestamp, trigger (reflex name or manual), situation summary, recommended actions with rationale, severity, status (open, applied, dismissed, helped, failed), outcome note, linked snapshot day.
- Exit: both files validate one example each.

### Step 1: Fix the reflex thresholds (0.5 day)

- Mood thresholds in `sidecar/config.py` are 25. Wiki base values are minor break 35%, major 20%, extreme 5% (Mental_break). Change to 35/20/5 and keep the traits note. Traits can move each colonist's own threshold, so flag this as an approximation.
- Exit: unit test shows a colonist at 33% triggers "minor break risk" and at 19% triggers "major break risk".

### Step 2: Expand reflex checks (2 days)

Each check is deterministic, runs on every poll, and has an alert category:

| Check | Source | Rule | Severity |
|---|---|---|---|
| Food days projection | snapshot history + `get_resources` | days = meals + raw food ÷ consumption per day (rolling 24 game hours). Warn under 5 days, urgent under 2 | warning / urgent |
| Medicine stock | `get_resources` | scales with colonist count (wiki: 1 per injury is not stated, so use a stated rule: under 1 per colonist warn, under 0.5 per colonist urgent) | warning |
| Downed or bleeding colonist | `list_colonists` `downed`, `get_pawn` health | downed = urgent | urgent |
| Medical bed missing while injured | `get_alerts` "Medical treatment needed" + bed list | no medical-tagged bed → warning | warning |
| Predator near a colonist | `list_wildlife` positions vs colonist positions | predator species (wiki Animals list) within 15 cells of a colonist or a hunter → urgent | urgent |
| Idle colonist | `get_alerts` "idle" | idle for 2 game hours → warning | warning |
| Mood break risk | `list_colonists` mood | below 35 warning, below 20 urgent, below 5 extreme | warning / urgent / urgent |
| Sleeping during a raid | `get_alerts` threats + pawn job | a colonist asleep while hostiles exist → urgent | urgent |
| Danger rating | `get_alerts` dangerByMap | not None → warning, High or Extreme → urgent | warning / urgent |

- Exit: each check has a unit test with a recorded fixture (step 6).

### Step 3: Harden the monitor (1 day)

- Single-instance lock (PID file) so two monitors cannot run.
- Every MCP error counted and written to `monitor.err.log` with the tool name; after 5 consecutive failures, write an alert.
- Log rotation (daily file, keep 14 days).
- Snapshot at each game-day rollover, plus a death snapshot when colonists reach 0. Keep the current label rule (previous day, with `conditions.date` stored inside).
- Record `difficulty`, `storyteller`, and `biome` from `get_status` in every snapshot and alert.
- Exit: kill the game during a run; the monitor logs the failure, retries, and writes an alert, and does not crash.

### Step 4: Advice log (1 day)

- Every alert that reaches the user or auto-pauses writes one advice record to `memory/advice/advice.jsonl`.
- Manual advice (from me during play) is logged the same way, with trigger = "manual".
- Outcome is filled in at the next snapshot: did the colonist survive, did the food run out, etc. The field stays `open` until it is set.
- Exit: after a 2-day play session, every alert and every manual action has one record.

### Step 5: Close the debrief loop (2 days)

- `debrief.py` reads snapshots and advice records for one run and writes:
  - a timeline (day, colonists, mood, food days, alerts),
  - the advice log with outcomes,
  - the analysis prompt (already there).
- Optional LLM pass (step 0 decision) writes `candidates/<run>.md`: proposed lessons in the schema form (trigger, recommendation, evidence, wiki link if any).
- Human review: a candidate is merged into `lessons-learned.md` only when it has a source (snapshot day or wiki page). The merge is manual, and I do not auto-write lessons.
- Exit: the Session 5 run (Day 7, Northwest Asora Covenant) goes through the full loop and produces at least 3 candidates.

### Step 6: Tests with recorded fixtures (1.5 days)

- Save the MCP responses from Session 5 snapshots as fixtures in `tests/fixtures/`.
- Mock `McpClient` and replay them. Test each reflex, the monitor loop, the snapshot writer, and the debrief generator.
- No game required. This is the main protection against the game freezing again during development.
- Exit: `python -m unittest` passes and covers all reflexes from step 2.

### Step 7: Live near-miss test (1 day, needs the game)

Run the monitor on the next colony and force the cases from the plan:

1. A predator near a hunter (use a hunt order near wildlife).
2. A colonist injured by a fight.
3. A food-low state (let stock fall below 5 days).

For each, check: the alert appears within one poll, auto-pause happens only where decided in step 0, and the advice record is written.

- Exit: a short report in `memory/session-logs/` listing each case, the time to alert, and whether it paused.

## Timeline

| Week | Steps | Milestone |
|---|---|---|
| 1 | 0, 1, 3 | Contracts, correct thresholds, hardened monitor |
| 2 | 2, 4 | Full reflex set, advice log |
| 3 | 5, 6 | Debrief loop, tests |
| 4 | 7 | Live near-miss test on the next colony |

Estimated effort: about 9–10 working days plus the live test.

## Out of scope for Phase 1

- Lesson store and retrieval (Phase 2).
- Situation classifier and ranked priorities (Phase 2).
- C# mod (Phase 3).
- Autonomous actions beyond pause (Phase 4).

## Risks

- **The game freezes under load.** Mitigation: `MCP_DELAY` rate limit (0.15 s), no unbounded loops, fixture tests for development.
- **Wiki gaps.** Medical bed, raid day range, and Community Builder pre-research are not documented (see `wiki-audit-20261018.md`). Rules that depend on them stay marked unverified.
- **Trait-adjusted break thresholds.** The 35/20/5 values are base values. A colonist with Iron-willed or Volatile has a different threshold, so mood alerts can be early or late for that colonist.
