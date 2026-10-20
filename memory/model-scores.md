# Model scores — debrief bundle comparison

Purpose: track how well different models turn a run's debrief bundle into reusable, wiki-grounded
lessons. Scores use `memory/debrief-rubric.md` (10 criteria, 20 points). Raw answers and the filled-in
scorecards live in `memory/debriefs/` (gitignored); this table is the durable summary.

Rules:
- Same bundle version for every model in a comparison row. If the bundle changes, re-run the models,
  do not mix versions.
- Record the provider/model as reported by the tooling. "Unknown" is not comparable.
- Note which criterion lost points if the loss is a bundle defect rather than a model defect.

## run-002-adv-cassandra (11 days, adviser on, 3/3 colonists alive, 12 urgent alerts)

| Model | Provider | Date | Bundle version | Total | Weakest criteria | Notes |
|---|---|---|---|---|---|---|
| unknown (pasted 2026-10-19) | not recorded | 2026-10-19 | pre-digest | 16 / 20 | 2 grounding, 4 unverified, 5 invention, 10 calibration | Dated the fire + raid to 13th Aprimay; monitor logged it on the 12th. The bundle at the time carried no in-game day on advice records, so criterion 2 is partly a bundle defect — re-run on the current bundle before comparing. |

Bundle versions:
- **pre-digest** — sections 1-5 plus advice log; advice records had only real timestamps.
- **digest** (2026-10-19) — adds section 6 "Notable changes (event digest)": new alerts per day, health
  drops >= 10, DOWNED events, food swings, and urgent advice dated by in-game day. Advice records in
  section 7 also carry `day=`.

## What good answers did

- Used the wiki block's base mood (37) and break thresholds (35/20) rather than inventing numbers.
- Scoped candidates to the actual difficulty/storyteller instead of "any" everywhere.
- Named the joiner-mood near-miss (18% -> 14% with major break risk) instead of only summarising the good outcome.

## What answers keep getting wrong

- Treating real timestamps as in-game days (fixed in the digest bundle, but check future models still cite days).
- Optimistic resource claims ("food transition was smooth") when the food alert was up for days.
- Confidence above 0.5 on a single observation; the rubric ladder is 0.3 single / 0.5 wiki-backed / 0.7 repeated.
