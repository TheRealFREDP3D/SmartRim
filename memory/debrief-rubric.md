# Debrief model comparison rubric

Use this to score each model's answer to the same bundle (`memory/debriefs/<run>.bundle.md`).
Score each criterion 0, 1, or 2. Record the scores in the response file under "Notes on the run".

| # | Criterion | 0 | 1 | 2 |
|---|---|---|---|---|
| 1 | Format | Not the two sections, or not valid JSON | Valid JSON but missing keys or extra prose | Exactly Section A (valid JSON, all keys) and Section B (max 10 bullets) |
| 2 | Grounding in the timeline | No day cited | Some days cited, some claims unsupported | Each candidate cites specific days or advice ids |
| 3 | Wiki accuracy | States a fact that contradicts the wiki facts block | Uses wiki facts but misses an obvious one | Uses wiki facts correctly, and cites the wiki page |
| 4 | Handling unverified claims | Treats unverified claims (e.g. Days 8-15 raid window) as fact | Mentions them but does not flag them | Lists them under unverified_claims |
| 5 | Invention | Invents mechanics or numbers not in the bundle or wiki | One minor unsupported detail | No invented facts |
| 6 | Scope fields | Trigger missing difficulty/storyteller | Some scope fields set | All six trigger fields set (use "any" when unscoped) |
| 7 | Actionability | Vague ("be careful") | Action named, no trigger | Action with trigger and rationale |
| 8 | Restraint | More than 6 candidates, or repeats the timeline | 6 candidates, some duplicates | 3–6 distinct candidates, no timeline repeat |
| 9 | Failure analysis | Misses the main failure chain | Names the cause but not the chain | Gives a cause chain (cause_chain array) that matches the timeline |
| 10 | Calibration | Confidence 0.7 on a single observation | Confidence not tied to evidence | 0.3 for single observations, 0.5 for wiki-backed, 0.7 only with repeated evidence |

Maximum score: 20.

## Run notes to record for every test

- Provider and model name, date, and whether it had web access.
- Time to answer and whether the answer was cut off.
- Any retries needed to get valid JSON.
- Whether the model asked for files it did not have (a sign it needed more context).

## How to decide

1. Score every model on the same bundle. Use the same bundle for all of them.
2. Discard any model that scores 0 on criterion 1 twice in a row (it cannot be used unattended).
3. Discard any model that scores 0 on criterion 3 or 5 on the same bundle (it invents or contradicts facts).
4. Of the rest, the highest total wins. Break ties on criterion 4 (handling unverified claims), then on criterion 2.
