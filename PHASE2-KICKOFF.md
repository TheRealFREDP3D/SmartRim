# Phase 2 Kickoff Design

Status: draft for ratification. Supersedes nothing in `PHASE2-PLAN.md`; this
document makes the plan's open decisions concrete and defines exact files,
interfaces, test fixtures, and acceptance criteria so each step can be executed
without re-discussing design.

## 1. Goal and scope (unchanged from PHASE2-PLAN)

By the end of Phase 2 the adviser:

1. Stores lessons as structured data (trigger conditions, scope, confidence, counters).
2. Retrieves lessons matching the current situation instead of re-reading markdown.
3. Ranks priorities for the current situation from reflex alerts + retrieved lessons.
4. Is measured, via fixed-difficulty runs with and without it.

Out of scope: embeddings, LLM advice/debriefs, the C# mod (Phase 3), autonomous
actions beyond pause (Phase 4).

## 2. Decisions to ratify (recommendations from the plan)

| # | Question | Recommendation | Why |
|---|---|---|---|
| D1 | Store format | **JSONL** at `memory/lessons.jsonl` | Dozens of lessons; git diffs matter for review. Revisit at ~500 lessons. |
| D2 | Retrieval | **Keyword + tag matching, deterministic** | Explainable, testable, zero deps. Embeddings only if matching proves weak (Phase 4). |
| D3 | Lesson ID | `L-0001`…, stable, never reused (retired lessons stay with `status: retired`) | Links from advice records must never dangle. |
| D4 | Threat vocabulary | Lesson `trigger.threats` values **mirror the monitor's alert categories** (§4.3) | One shared vocabulary between reflex layer and lesson store; no translation table to maintain by hand at call time (a static mapping is defined once, in code). |

If no objection, D1–D4 are considered approved and steps 0–1 start immediately.

## 3. Architecture and data flow

```
RimWorld (RimMolt MCP :8787)
      │  get_status / get_alerts / get_resources / get_conditions ...
      ▼
sidecar/monitor.py  ──reflex checks──►  alerts[]  (typed, categorized)
      │                                    │
      │ daily snapshot                     │ same poll
      ▼                                    ▼
memory/snapshots/*.json          sidecar/situation.py  (NEW)
      │                            - phase classifier
      │                            - risk list from alerts
      ▼                                    │
sidecar/outcomes.py (NEW)                ▼
- closes open advice at      sidecar/lessons.py  (NEW)
  each daily snapshot        - retrieve(situation) → ranked lessons
- updates lesson counters            │
      │                              ▼
      ▼                    advice record (existing advice_log.py,
memory/lessons.jsonl        now with actions[] + linked_lessons[] filled)
```

Deterministic everywhere. No LLM in Phase 2. The only existing files modified:
`monitor.py` (call situation/lessons, alert-diff logging), `advice_log.py`
(none — `linked_lessons` already exists as a parameter), `config.py` (new
constants). Everything else is new files.

## 4. Step 0 — Schema and phase definitions (0.5 day)

### 4.1 `schemas/lesson.schema.json`

Exactly the fields in PHASE2-PLAN §"Lesson schema". Emphases that the schema
must enforce (these are the failure modes of a hand-edited store):

- `id` pattern `^L-\d{4}$`.
- `trigger.phases` ⊆ `early_survival | stabilization | raid_prep | expansion | crisis`.
- `trigger.threats` values from the closed enum in §4.3 (extend the enum only
  with a code change, so typos fail validation instead of silently never matching).
- `trigger.resources` values from a closed enum: `food_under_5_days |
  food_under_2_days | no_medicine | medicine_under_5 | low_wood | low_steel`.
- `confidence` in [0, 1]. A lesson with empty `source` MUST have
  `confidence <= 0.3` (enforced by a small Python validator, not expressible
  in JSON Schema — put it in `tests/test_lessons_schema.py`).
- Counter fields `times_applied/helped/failed` are integers ≥ 0, default 0,
  updated only by `sidecar/outcomes.py` (never hand-edited).

Validation entry point: `python sidecar/lessons.py validate` exits non-zero on
any schema violation. Run it in a git pre-commit hook.

### 4.2 `memory/phases.md` + `sidecar/situation.py` phase classifier

Phase boundaries (our labels, marked as such — not wiki facts):

| Phase | Rule |
|---|---|
| `early_survival` | day ≤ 7 (day counted as `daysPassed`, Day 1 = 1st day) |
| `stabilization` | 8 ≤ day ≤ 20 AND no active raid/threat alert |
| `raid_prep` | any raid-related alert/letter active, or day within a known raid window |
| `expansion` | day > 20 AND no active threat |
| `crisis` | any of: colonist downed, predator/hostile near, danger_rating high/extreme, colony_death. **Overrides all other phases.** |

Classifier signature: `classify_phase(snapshot_summary, alerts) -> str`. Pure
function, unit-tested against the 13 archived snapshots (they contain day 1–10
plus a day-13 one — expect `early_survival` for all, and we can synthesize a
crisis fixture from Session 3's danger:High + raid alert state).

### 4.3 Threat taxonomy (D4)

Map each monitor alert `category` to exactly one threat tag — this mapping is
the single source of truth, defined once in `situation.py`:

| monitor `category` | threat tag |
|---|---|
| `downed` | `colonist_downed` |
| `mood_extreme`, `mood_major`, `mood_minor` | `mood_break_risk` |
| `health` | `colonist_injured` |
| `danger_rating` (High/Extreme) | `danger_high` |
| `hostile` | `raid_incoming` |
| `predator_near` | `predator_near_worker` |
| `food_low` | `low_food` |
| `medicine_low` | `medical_untreated` (also fires on `medical_treatment_needed`) |
| `idle_colonist` | `idle_colonists` |
| `sleeping_during_threat` | `threat_response` |
| `colony_death` | `colony_death` |
| `game_alert` | `other_game_alert` (matched by keyword in the label: raid/enemy → `raid_incoming`, etc.) |

**Exit (step 0):** `schemas/lesson.schema.json` validates an example lesson;
`memory/phases.md` documents the table above; `classify_phase` passes its unit
tests on archived snapshots.

## 5. Step 1 — Migrate lessons to JSONL (2 days)

### 5.1 Source and mapping

Source: `memory/lessons-learned.md` (critical mistakes 1–6, important mistakes
7–11, "what worked", session lessons, tool gotchas). Each becomes one JSONL
record. Scope assignment (from `memory/session-logs/`):

| Source session | difficulty | storyteller | confidence basis |
|---|---|---|---|
| Sessions 1–3 | Adventure story | Cassandra Classic | single observation → 0.3, wiki-backed → 0.5 |
| Session 4–5 | Community builder | Phoebe Chillax | scope set; confidence 0.3/0.5 as above |

Confidence rule from the plan: 0.3 single observation, 0.5 wiki-backed rule,
0.7 only after it helped in two independent runs (so **no** migrated lesson
starts at 0.7 — that value can only be earned via `outcomes.py`).

Claims the wiki does not support (per `memory/wiki-audit-20261018.md`):
`status: needs_review`, regardless of confidence. Examples named in the audit:
raid-day windows, Community Builder pre-research list, medical bed mechanics.

### 5.2 No-drift rule

`memory/lessons-learned.md` becomes **generated**: `python sidecar/lessons.py
render > memory/lessons-learned.md`. Hand-edits to the markdown are overwritten
by CI/lint (a line in the file header: "GENERATED — edit lessons.jsonl").
Review workflow: edit JSONL → validate → render → diff.

### 5.3 Exit

Every lesson in the original markdown appears exactly once in the JSONL
(rendered markdown reviewed against the original); `validate` passes; scopes
and `needs_review` markings match the wiki audit.

## 6. Step 2 — Retrieval (2 days)

`sidecar/lessons.py`:

```python
def build_situation(snapshot_summary: dict, alerts: list[dict]) -> Situation
    # phase, difficulty, storyteller, biome, food_days, medicine_count,
    # threats (set), resources (set) — pure derivation from inputs

def retrieve(situation: Situation, limit: int = 5) -> list[Lesson]
    # deterministic; see algorithm below
```

Matching algorithm (in order):

1. `status == active` only.
2. Phase overlap: `situation.phase ∈ lesson.trigger.phases` (or lesson lists all).
3. Threat overlap: intersection of situation threats and `lesson.trigger.threats` non-empty — **unless** the lesson's trigger is resource-only (empty threats), in which case it is eligible when resources match.
4. Resource overlap: same rule, mirrored.
5. Scope match: `lesson.difficulty`, `.storyteller`, `.biome` each match or are empty. **Strict — never relax silently** (drift risk named in PHASE2-PLAN).
6. Rank: confidence desc, then `times_helped - times_failed` desc, then `last_updated` asc (older first — stable, deterministic tie-break), then id asc.

At least one of (threat, resource) must match — a lesson matching only on
phase+scope is never retrieved (it would fire constantly and teach nothing).

**Exit:** unit tests with fixtures from `tests/fixtures/`: the Session 5 state
(Day 7, raid survived, Tyren wounded, food low) must return the medicine and
raid-prep lessons in the top 5; a synthesized early-raid state must return the
`raid_incoming` lessons. Same input → same output, asserted.

## 7. Step 3 — Situation classifier in the live loop + priority ranking (2 days)

### 7.1 Wiring into `monitor.py`

After `run_reflex_checks` each poll:

```python
situation = situation.build_situation(snapshot_summary, alerts)
lessons   = lessons.retrieve(situation)
```

On urgent alerts (the existing auto-pause path), the advice record now carries
`linked_lessons=[L-...]` and `actions` ranked by §7.2. Scheduled (daily)
assessment: at each day roll, write one `trigger="scheduled"` advice record
with the ranked action list — this is the record the evaluation arm measures.

### 7.2 Ranking

Risks = the current alerts, severity mapped (urgent→critical risk, warning→
warning). Each risk pulls its threat tag, retrieves up to 3 lessons, and
produces candidate actions (`lesson.recommendation` as the action text,
`lesson.rationale`, `estimated_time` from the lesson's `tags` if present).
Final ranking: risk severity first, then lesson confidence. Output capped at 5
actions. Written into the advice record exactly per `schemas/advice.schema.json`
(the `actions` and `linked_lessons` fields already exist in the schema and in
`advice_log.log_advice` — no schema change needed).

### 7.3 Exit

The daily advice record contains ranked actions and linked lessons; a fixture
replays to the identical ranking every time.

## 8. Step 4 — Outcome tracking and confidence updates (1.5 days)

`sidecar/outcomes.py`, run at each daily snapshot write:

1. Load open advice records for the run.
2. For each, re-derive the situation from the new snapshot and close it:
   - `helped`: the risk cleared (e.g. `food_low` advice + `food_days` back ≥ 5;
     `medical_treatment_needed` + no untreated injuries in the new snapshot;
     mood advice + min mood above threshold).
   - `failed`: risk worsened (food_days fell further, colonist died/downed,
     mental break occurred).
   - `expired`: neither by the next snapshot and the trigger no longer applies.
   - `applied/dismissed` remain human-set via the existing CLI; outcome is
     orthogonal where possible — a record can be `applied` then `helped`.
3. Update every linked lesson: `times_helped`/`times_failed` per closure.
   Confidence: +0.1 on helped, −0.15 on failed, clamped [0,1].
   `needs_review` when failures ≥ 3 and failures > helped.
4. Idempotent: re-running on the same snapshot set changes nothing (guarded by
   per-advice closure marker). Required, because we will replay history.

**Replay validation (the valuable shortcut):** you have 13 archived daily
snapshots (days 1–10 + day 13) and `memory/advice/advice.jsonl`. Replay
outcome closing over that history before any new live run. This validates the
whole pipeline — retrieval, ranking, outcome rules — using data you already
own, without game time. This partially covers Phase 1 step 7 (below).

**Exit:** after a replay, lesson counters match a hand-computed expectation
from the archived run; idempotency test passes.

## 9. Prerequisite — Phase 1, step 7 (live near-miss test), defined

Before the evaluation harness can claim anything, prove the reflex layer
catches a real near-miss live. Definition for step 7:

1. Start a protocol run (`RUN-PROTOCOL.md` settings).
2. At the first **non-critical** warning-tier alert (e.g. `food_low` or
   `predator_near`), do **not** act immediately; let the monitor surface it.
3. Pass = the alert appears in `alerts/current.json` with correct category and
   severity, AND a scheduled/reflex advice record exists naming the matching
   lesson(s), AND the auto-pause path works for the urgent tier (can be tested
   by synthesizing an urgent alert or waiting for one).
4. Record in `memory/session-logs/` which alert fired and what the adviser
   recommended. This run doubles as evaluation-arm run #1 if protocol is kept.

## 10. Step 5 — Evaluation harness (2 days + game time)

`sidecar/evaluate.py`:

```
usage: evaluate.py summarize [--runs-dir memory/runs]
       evaluate.py compare  --runs <ids...>
```

- Reads `<run-id>.end.json` markers + advice log + snapshots; emits one summary
  row per run: arm (on/off), days survived, colonists alive at day 10, lowest
  mood, downed/break events, first low-food day, first medicine-alert day,
  urgent alert count, auto-pauses, advice helped/failed/ignored counts.
- Two arms, same fixed setup, **alternating order** (on, off, on, off…), ≥3
  runs each. Adviser-off runs: monitor observes and snapshots but never pauses
  and writes no advice (a `--observe-only` flag on `monitor.py`).
- Analysis is descriptive only — with n=3, report medians and ranges, no
  significance claims (risk already noted in the plan).

**Code status (2026-10-19):** `sidecar/evaluate.py` prints the summary table
and writes the markdown report with `--write`. Adviser-off is
`.\start-monitor.ps1 -ObserveOnly` (no alert pause, no advice). Both arms still
pause once at the protocol stop so the window closes; that stop is not an
auto-pause. Snapshots for a run go in `memory/snapshots/<run-id>/`.

**Exit:** harness prints the summary table; both arms ≥3 runs; results written
to `memory/eval-2026-XX.md` with the protocol's comparison metrics. The live
runs are still open. Do not treat a table with n<3 as a result.

## 11. Code-hygiene items folded into Phase 2

These were observed in the current code and get fixed as part of the steps above:

1. **Monitor log noise** — `monitor.py` prints `{n} alert(s)` every poll
   (the last 200+ lines of `memory/monitor.log` are this line). Change to
   log only when the alert set changes (count or categories), plus urgent
   events. Done in step 3 wiring.
2. **Snapshot schema drift** — on-disk snapshots nest raw tool responses under
   `status/conditions/...` plus a `summary` object, but `schemas/snapshot.schema.json`
   declares top-level `food_days`, `medicine_count`, etc. Align them: extend
   `normalize_snapshot` to compute `food_days` (consumption-based, per schema
   description) and `medicine_count` into `summary`, and either relax the
   schema to validate `summary` or have the monitor emit schema-shaped files.
   Decide once, in step 0, and record the decision here.
3. **Config hygiene** — `.env.example` documents `HEALTH_THRESHOLD`/`MOOD_THRESHOLD`
   while `monitor.py` reads `MOOD_EXTREME/MAJOR/MINOR_THRESHOLD`; reconcile in
   `config.py` (step 0).

## 12. Timeline and milestones

| Milestone | Content | Acceptance |
|---|---|---|
| M0 (day 1) | Step 0 + hygiene items | Schema validates; phases tested on archived snapshots; config reconciled |
| M1 (days 2–3) | Step 1 migration | lessons.jsonl complete, validated, rendered markdown matches original |
| M2 (days 4–5) | Step 2 retrieval | Unit tests pass incl. Session-5 and early-raid fixtures |
| M3 (days 6–7) | Step 3 wiring + ranking | Daily advice records carry ranked actions + linked lessons; replay-stable |
| M4 (day 8) | Step 4 outcomes | Replay over archived run produces expected counters; idempotent |
| M5 (day 9+) | Step 7 near-miss test | Live run records a caught near-miss end-to-end |
| M6 (weeks 4–6) | Step 5 evaluation | ≥3 runs per arm, summary table produced |

Total: ~8 working days of coding (matches the plan), plus ~17h wall-clock of
evaluation game time.

## 13. Risks (carried from plan, with mitigation owner)

- **n=3 per arm** — treat as first signal only; pre-registered metrics, no p-values.
- **Lesson drift across difficulty** — strict scope matching (§6 rule 5); `needs_review` gates promotion.
- **Wiki gaps** — unsupported claims stay `needs_review`, capped at 0.3 confidence.
- **Advice ignored vs. advice wrong** — advice records carry `status` transitions; evaluation reports both separately.
- **JSONL merge conflicts** — one line per lesson, append-only counters updated by script only; git diff stays readable.
- **Alert vocabulary creep** — new monitor alert categories must update the §4.3 table in the same commit, enforced by a test that maps every observed category in fixtures.
