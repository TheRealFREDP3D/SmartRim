# Phase 2 plan: structured lessons, retrieval, and evaluation

Source: `New plan.md`, Phase 2 and sections 3–4. Facts are checked against `memory/wiki/` (the wiki is the source of truth).
Prerequisite: Phase 1 is complete. Step 7 of `PHASE1-PLAN.md` (live near-miss test) is still open. Phase 2 needs it for the evaluation harness, so run it first on the next colony.

## Goal

By the end of Phase 2 the adviser should:

1. Store every lesson as structured data with trigger conditions, confidence, and outcome counters, instead of only as markdown.
2. Retrieve the lessons that match the current situation (phase, difficulty, storyteller, threats, resources), not re-read the whole file.
3. Rank priorities for the current situation from the reflex alerts and the retrieved lessons.
4. Measure whether the adviser helps, using fixed-difficulty runs with and without it.

Phase 2 does not include the C# mod (Phase 3) or autonomous actions beyond pause (Phase 4).

## Decisions

Recorded from earlier answers:

- Lesson scope includes difficulty and storyteller (Session 5 showed Phoebe raids on Day 5, which Cassandra does not).
- Baseline runs: Adventure story with Cassandra Classic (wiki threat scale 60%, research speed 100%).
- Auto-pause on urgent alerts only. Food and medicine stay advisory.
- Debrief stays template-only (no LLM).

Still open (answer before step 5):

1. **Store format.** JSONL (one lesson per line, easy to diff in git) or SQLite (indexed queries)? Recommendation: JSONL, because the lesson count is in the dozens and the diffs matter for review. Revisit if it passes about 500.
2. **Retrieval method.** Keyword and tag matching only, or add embeddings later? Recommendation: keyword and tag matching in Phase 2. Embeddings are Phase 4 unless matching proves too weak.

## Lesson schema

Fields from the plan, plus the scope fields we decided on. The schema file is `schemas/lesson.schema.json`.

- `id`: stable string, e.g. `L-0007`.
- `title`: short description.
- `trigger`: conditions that make the lesson relevant.
  - `phases`: subset of `early_survival` (day 0–7), `stabilization` (day 8–20), `raid_prep`, `expansion`, `crisis`. Phase boundaries are our own labels, not wiki terms. Document them in the schema.
  - `threats`: e.g. `predator_near_worker`, `raid_incoming`, `low_food`, `medical_untreated`, `mood_break_risk`.
  - `resources`: e.g. `food_under_5_days`, `no_medicine`.
  - `difficulty`, `storyteller`, `biome`: scope. Empty means "any".
- `recommendation`: the action, one or two sentences.
- `rationale`: the failure mode it prevents.
- `source`: list of references. Each entry is a snapshot day, a session log, or a wiki page slug (e.g. `wiki:Mental_break`). A lesson with no source cannot be promoted above confidence 0.3.
- `confidence`: 0–1. Starts at 0.3 for a single observation, 0.5 for a wiki-backed rule, 0.7 after it helped in two independent runs.
- `times_applied`, `times_helped`, `times_failed`: counted from the advice log outcomes (Phase 1, step 4).
- `status`: `active`, `needs_review`, `retired`.
- `tags`: free tags (medicine, food, defense, mood, animals, research, time-control).
- `source_runs`, `last_updated`.

## Work breakdown

### Step 0: Schema and phase definitions (0.5 day)

- Write `schemas/lesson.schema.json`.
- Write the phase definitions (day ranges and the threat/resource signals that move a colony between phases) in `memory/phases.md`. Mark the day ranges as our rules, not wiki facts.
- Exit: schema validates an example lesson; phases documented.

### Step 1: Migrate lessons (2 days)

- Convert the lessons in `memory/lessons-learned.md` (the critical mistakes, the important mistakes, the tool gotchas, and the session lessons) into `memory/lessons.jsonl`.
- For each lesson, set scope from its source session (Sessions 1–3 are Adventure story or Classic, Session 4–5 are Community builder or Phoebe, so mark those as scoped).
- Apply the wiki audit corrections already made (e.g. the herbal recipe, the mood thresholds, the raid-day claim). Mark claims the wiki does not support as `needs_review`.
- `lessons-learned.md` stays as the human view. Generate it from the JSONL with a script so the two cannot drift.
- Exit: every lesson in the markdown appears in the JSONL once; the generated markdown reviews cleanly against the original.

### Step 2: Retrieval (2 days)

- `sidecar/lessons.py`: `retrieve(situation)` returns the top N active lessons. Matching: phase and threat tags must overlap, scope must match (or be empty), ranked by confidence then by recency.
- Input is the same structure the monitor already produces: the alerts list plus the colony summary (phase, difficulty, storyteller, food days, medicine count).
- Exit: unit tests with fixtures from `tests/fixtures/` return the expected lessons for the Session 5 state and for an early raid state.

### Step 3: Situation classifier and priority ranking (2 days)

- Phase: computed from the day and the threat signals in step 0.
- Priorities: the reflex alerts become risks (severity from the alert). Each risk is matched to lessons. Output is a ranked list of actions, each linked to the lesson IDs used. This is the `actions` and `linked_lessons` fields of the advice schema.
- Deterministic only. No LLM in Phase 2.
- Exit: the advice record written by the monitor now contains ranked actions and linked lessons; an existing fixture produces the same ranking every run.

### Step 4: Outcome tracking and confidence updates (1.5 days)

- At each daily snapshot, close the open advice records: `helped` if the risk cleared (e.g. food days went back above 5), `failed` if the colonist was lost or the risk got worse.
- Update each linked lesson's counters. Confidence moves by a fixed step (up 0.1 on a help, down 0.15 on a failure, bounded 0–1). Set `needs_review` when a lesson has 3 failures and fewer helps.
- Exit: after a replayed run, counters match the advice log.

### Step 5: Evaluation harness (2 days, plus game time)

- Define the metrics: median days survived, deaths before day 15, days until the first medicine shortage, days until the first low-food alert.
- Two arms on the same fixed setup (Adventure story, Cassandra Classic, same tile and start if the game allows): adviser on (monitor auto-pauses and logs advice) and adviser off (monitor observes only, no pause).
- The arms run in alternating order to reduce drift. Each run is recorded with its difficulty and storyteller.
- Exit: harness script writes one summary row per run; both arms have at least 3 runs.

## Timeline

| Week | Steps | Milestone |
|---|---|---|
| 1 | 0, 1 | Schema, phases, migrated lessons |
| 2 | 2, 3 | Retrieval and ranked priorities |
| 3 | 4 | Outcome tracking and confidence |
| 4–6 | 5 | Evaluation runs (game time dominates) |

Estimated effort: about 8 working days of coding, plus evaluation play time. Each evaluation run takes real time because the game runs at normal speed (about 17 minutes per in-game day), so 6 runs will take a substantial session block.

## Out of scope for Phase 2

- Embedding search (Phase 4 if keyword matching is too weak).
- LLM-based advice or debrief analysis (template-only, per decision).
- C# mod (Phase 3).
- Autonomous actions beyond pause (Phase 4).

## Risks

- **Too few runs for a real comparison.** Six runs will show large effects only. Treat the evaluation as a first signal, not a proof.
- **Lesson drift across difficulty.** Scope fields and confidence reduce this, but a lesson from one difficulty can still mislead another. Keep the scope fields strict.
- **Wiki gaps.** The raid-day window, the Community Builder pre-research list, and medical bed mechanics are not in the wiki. Lessons that depend on them stay `needs_review`.
- **Measurement noise from play style.** The same adviser can look better or worse depending on how carefully it is followed. Log what was actually applied (step 4), so the analysis separates "advice ignored" from "advice wrong".
