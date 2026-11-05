# Model scores — debrief bundle comparison

Purpose: track how well different models turn a run's debrief bundle into reusable, wiki-grounded
lessons. Scores use `memory/debrief-rubric.md` (10 criteria, 20 points). Raw answers and the filled-in
scorecards live in `runtime/<run>/debriefs/` (gitignored); this table is the durable summary.

Rules:
- Same bundle version for every model in a comparison row. If the bundle changes, re-run the models,
  do not mix versions.
- Record the provider/model as reported by the tooling. "Unknown" is not comparable.
- Note which criterion lost points if the loss is a bundle defect rather than a model defect.

## Ollama benchmark — 2026-11-05 (run-009-adv bundle)

Hardware: GTX 1050 Ti (4 GB VRAM), 32 GB RAM, 31.9 GB usable. Ollama 0.40.11.
Bundle: `run-009-adv.bundle.md` (28,014 chars, v3). Settings: `num_ctx=16384`,
`temperature=0.3`, `num_predict=4096`, cold load, one run per model, zero-shot.
Digests are recorded per row; `qwen3:latest` and `qwen3:8b` share one digest.

| Model | Digest | GB | Rubric | Decode tok/s | Wall | Schema |
|---|---|---:|---:|---:|---:|:--:|
| gemma-4-E2B-it-Q4_K_M | `ebb4e91482e6` | 3.1 | **19/20** | 16.7 | 196 s | fail |
| Qwen3-1.7B-Q6_K | `ad47863af7c1` | 1.7 | 17/20 | 15.4 | 167 s | fail |
| llama3.2:3b | `a80c4f17acd5` | 2.0 | 15/20 | 5.5 | 291 s | fail |
| gemma4-e2b-rimworld | `c95ec9b9354f` | 3.1 | 14/20 | 16.0 | 234 s | fail |
| gemma3:1b | `8648f39daa8f` | 0.8 | 9/20 | **29.4** | 154 s | fail |
| gemma-3-1B-it-QAT-Q4_0 | `02f708abca79` | 0.7 | 0/20 | **32.7** | 47 s | fail |
| llama3.2:1b-instruct-q4_K_M | `22bc6b92eb01` | 0.8 | 0/20 | 31.8 | 149 s | fail |
| deepseek-r1:1.5b | `a42b25d8c10a` | 1.1 | 0/20 | 23.2 | 209 s | fail |

Timed out at 300 s (7): Mistral-7B-Instruct-v0.3, llama3.1:latest,
qwen3-rimworld, qwen3:latest, deepseek-r1:8b, DeepSeek-R1-0528-Qwen3-8B,
DeepSeek-R1-Distill-Llama-8B. `llama3.2-vision` returned HTTP 500 on load.
Phi-4-mini-reasoning also timed out at 300 s.

**Key finding:** no model produced a schema-valid Section A zero-shot. The
failures are vocabulary/type errors (`"injury"` vs `colonist_injured`,
`"low food"` vs `low_food`, string where a list is required), not missing
content — the rubric's best answer scored 19/20 while failing the contract.
The monitor's debrief path retries up to 3 times with the exact error plus the
allowed vocabulary; treat the zero-shot column as a robustness signal, not a
verdict.

**Hardware ceiling:** every model above 4 GB splits or runs on CPU here. The
7–11B group could not answer within 300 s, so it is not usable for interactive
advice on this machine regardless of quality.

### Retry pass (app's 3-attempt repair loop)

| Model | Attempts | Total wall | Rubric | Schema |
|---|---:|---:|---:|:--:|
| gemma-4-E2B-it-Q4_K_M | 3 | 598 s | **20/20** | fail |
| gemma4-e2b-rimworld | 3 | 600 s | 20/20 | fail |
| Qwen3-1.7B-Q6_K | 3 | 463 s | 17/20 | fail |
| llama3.2:3b | 3 | 435 s | 16/20 | fail |

After retries the vocabulary is correct but the models emit scalars where the
schema requires lists (`phases='stabilization'`). `TriggerCandidate` accepted a
scalar only for `difficulty`/`storyteller`/`biome`, so semantically correct
answers still failed on shape.

**Fixed:** scalar→list coercion for `phases`/`threats`/`resources` (invalid
vocabulary still fails). Verified after the change:

| Model | Attempts | Total wall | Rubric | Schema |
|---|---:|---:|---:|:--:|
| gemma-4-E2B-it-Q4_K_M | 2 | 433 s | 19/20 | ok |
| Qwen3-1.7B-Q6_K | 2 | 417 s | 17/20 | ok |

Full report: `docs/local_llm/BENCHMARK-2026-11-05.md`.



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

## run-007-adv-cassandra (11 days, adviser on, 3/3 colonists alive, 1 urgent alert, ended in starvation)

| Model | Provider | Date | Bundle version | Total | Weakest criteria | Notes |
|---|---|---|---|---|---|---|
| gemma4-e2b-rimworld | ollama | 2026-10-25 | v3 | 19 / 20 | 10 calibration | **Scored by `smartrim.eval_models`.** First v3 run, and the ceiling moved: 19/20 without author knowledge, versus 16/20 for both run-002 answers on the older bundle. Only calibration lost a point: candidate 0 gave confidence 0.7 although one of its two sources is a player cause-annotation rather than independent evidence. The player confirmed the starvation cause (plant-cutting priority too low) and the bundle carried it as ground truth, so the model built its main lesson on it instead of re-diagnosing. |

### What changed vs the run-002 answers
- **Grounding recovered (2/2).** Every candidate cites a specific in-game day ("Day 9-11",
  "11th of Aprimay, 5500", "15th of Aprimay, 5500"). The v3 digest plus run-level causes gave
  it something concrete to cite.
- **Failure analysis recovered (2/2).** The cause chains are causal, not descriptive.
- **Schema compliance needed work.** The first answers used free-text trigger values
  (`"Starvation"`, `"Raid"`) instead of the fixed vocabulary, which failed Pydantic validation.
  Fixed by making the schema-retry prompt spell out the allowed values; the next run was
  schema-valid on the first attempt.
- **Format: the model never labels "Section A".** It emits the bare fenced JSON array, then
  `**Section B: Summary**`. The scorer now treats a JSON fence before the Section B marker as
  an implicit Section A. This is a scorer fix, not a model improvement — the rubric's
  "exactly Section A" wording is strict but the answer is unambiguous.


