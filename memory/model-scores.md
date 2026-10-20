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
| opencode / deepseek-v4.1-flash-free | opencode | 2026-10-19 | digest | 16 / 20 | 7 actionability, 9 failure analysis, 10 calibration | **Author-scored, then corrected by the player.** Originally 18/20; docked to 16 after the player revealed the fire was arson, research cannot be queued in vanilla, and the guest was a protection-quest target. Two of five lessons pointed the wrong way. |
| unknown (pasted 2026-10-19) | not recorded | 2026-10-19 | pre-digest | 16 / 20 | 2 grounding, 4 unverified, 5 invention, 10 calibration | Dated the fire + raid to 13th Aprimay; monitor logged it on the 12th. The bundle at the time carried no in-game day on advice records, so criterion 2 is partly a bundle defect — re-run on the current bundle before comparing. |

**Both answers scored 16/20 on different bundle versions, and both got the guest and the fire wrong the same way.** The models are not the limiting factor yet — the bundle is. See "Bundle ceiling" below.

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
- Asserting a sequence the bundle cannot prove, e.g. "the joiner was downed before he joined" — snapshot absence plus an advice timestamp is suggestive, not evidence. Put it under unverified_claims.
- **Assuming a temporary pawn is a colonist.** Both answers framed the quest guest as somebody to settle in; he was a liability to protect and then load onto a shuttle.
- **Assuming a fire during a raid is structural.** Both answers blamed wood and torch lamps; the raider lit it.

## Bundle ceiling

The run-002 bundle cannot support a score above roughly 16-17 because three classes of context are absent, and no amount of model quality invents them:

1. **Quest state** — who is a guest, who is a colonist, what ends the quest. This changed the correct lesson entirely.
2. **Event cause** — a "Fire!" record with no cause invites the wrong diagnosis. Cause can only come from the player or the agent's own log.
3. **Incident state** — daily snapshots miss a fight that starts and ends between two hours-0 captures.

Until the bundle carries these, scores measure the bundle, not the models. The correction loop that produced this finding is worth keeping: **score, then ask the player for corrections, then re-score.** A player correction that contradicts the answer is ground truth and should dock the score, not be explained away.

## Follow-ups

Bundle v3 (2026-10-19) closes these:

- **Quests** — `sidecar/quests.py` reads `get_quest`, keeps a description registry, and every
  snapshot embeds the quest list; section 2 of the bundle prints the objective text.
- **Event causes** — `advice_log.py cause <id>` / `cause-match <run> <needle> <text>`; section 6 and
  section 7 render `cause: ...`, and the prompt tells models it is ground truth.
- **Incident state** — the monitor writes a `reflex-*.json` snapshot when a new urgent alert fires
  (capped at 40 per run), rendered in section 6 without polluting the daily timeline.

Still open: a run scored with v3 to confirm the ceiling actually moves (expect 2 grounding +
9 failure analysis to recover, i.e. 18+ achievable without author knowledge).

