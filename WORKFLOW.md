# Lesson Workflow

How a SmartRim lesson is created, reviewed, saved and retired — from a colony
observation to a retrievable row in `memory/lessons.jsonl`.

Lessons are the only thing SmartRim must not lose. Everything else (snapshots,
advice, debriefs, timelapse, the SQLite index) is derived or disposable.

---

## Where lessons live

| Path | Role | Git |
|---|---|---|
| `memory/lessons.jsonl` | **Source of truth.** One JSON object per line, hand-editable | tracked |
| `memory/lessons.sqlite` | Derived FTS5 query index; auto-rebuilt when the JSONL is newer | ignored |
| `runtime/<run>/candidates/*.jsonl` | LLM-proposed lessons awaiting human review | ignored |
| `memory/lessons-learned.md` | Human-readable render; never edit by hand | tracked |
| `schemas/lesson.schema.json` | Field/schema contract | tracked |

Durable knowledge lives in `memory/`; everything a run produces lives in
`runtime/<run-id>/` and can be deleted at any time.

The JSONL file is authoritative. If the SQLite index is deleted or stale it is
rebuilt automatically on the next read, or explicitly with
`python -m smartrim.situation reindex`.

---

## Big picture

```
monitor poll ──> build_situation() ──> retrieve() ──> advice_log.log_advice(linked_lessons)
     │                                                        │
     │ daily roll                                             │ outcome closes
     └──> outcomes.close_outcomes() <─────────────────────────┘
              (times_applied/helped/failed, confidence ±, needs_review)

run end ──> debrief_bundle.build_bundle() ──> debrief_llm.analyze_debrief()
                                                    │ Section A JSON (validated)
                                                    ▼
                                   runtime/<run>/candidates/<run>-<timestamp>.jsonl
                                                    │
                                situation promote (interactive review)
                                                    ▼
                                   memory/lessons.jsonl  ──> reindex ──> lessons.sqlite
```

---

## Part A — Automatic path (runtime)

### Step 1. Observe and classify

`monitor.poll_once()` reads the game over MCP (`get_status`, `get_conditions`,
`list_colonists`, `get_resources`, `get_alerts`, …) and
`situation.build_situation()` reduces it to:

```json
{
  "phase": "early_survival",
  "threats": ["low_food", "mood_break_risk"],
  "resources": ["food_under_2_days"],
  "difficulty": "Adventure story",
  "storyteller": "Cassandra Classic",
  "biome": "temperate forest"
}
```

### Step 2. Retrieve lessons and advise

`situation.retrieve()` filters lessons by `status == "active"`, then by phase,
threats/resources, difficulty, storyteller and biome. Survivors are ranked by
FTS5 relevance (query text), then confidence, then `times_helped - times_failed`.
The matched ids become `linked_lessons` on the advice record written by
`advice_log.log_advice()`.

A lesson is considered **applied** the moment linked advice is issued.

### Step 3. Close outcomes (confidence drift)

On each in-game day roll the monitor calls `outcomes.close_outcomes()`:

| Outcome | Effect on the lesson |
|---|---|
| `helped` | `times_helped + 1`, `confidence + 0.10` (cap 1.0) |
| `failed` | `times_failed + 1`, `confidence - 0.15` (floor 0.0); after 3 failures with more failures than helps, `status = needs_review` |
| either (helped or failed) | `times_applied + 1`, `last_updated = today`, run id appended to `source_runs` (expired verdicts count nothing) |

Closing is idempotent. Records are **judged first** at each day roll; only records that stay
undecidable are then aged out to `expired` — after 3 in-game days when the record and the
snapshot both carry `days_passed` (monitor-written records do), otherwise after 7 wall-clock
days (`ADVICE_EXPIRE_IN_GAME_DAYS` / `ADVICE_EXPIRE_DAYS`). **Only helped/failed verdicts
touch lesson counters**: `times_applied` counts judged advice, and inconclusive closures
(`expired`) leave the lessons, confidence and `source_runs` untouched.

### Step 4. Run ends

When `RUN_DAYS` is reached (or the colony dies) the monitor writes
`runtime/<run-id>/end.json` and a final snapshot. Debrief tooling then has a
stable run id to work with.

If the run is **abandoned** (game closed, save dropped, monitor stopped before
the ending) it never gets a definitive marker from the monitor. Instead the next
monitor start auto-closes it via `runmarker` (or you can run
`python -m smartrim.runmarker close <run-id> [--reason manual_close|monitor_abort]`):
an inconclusive marker is written from the last available snapshot — no live
capture, since the game may be gone — and the run is **excluded from evaluation**
by default (`python -m smartrim.evaluate summarize --include-inconclusive` to
override). Definitive endings (`run_length`, `colony_death`) stay the only valid
comparison datapoints.

All of Steps 5–10 can be run as one command:

```bash
python -m smartrim.pipeline <run-id>
```

This builds the debrief and v3 bundle, runs the LLM analysis, auto-promotes
candidates that pass the quality rules (cited source, schema-valid, scoped
trigger, not a duplicate — always as `needs_review`, never auto-activated), and
regenerates `memory/lessons-learned.md`. `--skip-llm` reuses the newest
candidates file; `--dry-run` reports without writing; `--no-promote` stops
after the analysis. Everything else can still be done manually:

### Step 5. Build the debrief bundle

```bash
python -m smartrim.debrief <run-id>
```

This writes:

- `runtime/<run>/debriefs/<run-id>.md` — timeline prompt plus a candidate template
- `runtime/<run>/debriefs/<run-id>.bundle.md` — the v3 bundle the model reads
- `runtime/<run>/debriefs/<run-id>.response.md` — empty answer template

The bundle contains: instructions, run metadata (outcome, biome, quests, causes),
verified wiki facts, explicitly unverified claims, the daily timeline, an event
digest (transitions and urgent incidents), the advice log, and the task.

Urgent advice is auto-tagged with a best-effort cause at log time
(`event_cause`, e.g. `hostile_raid`, `fire_during_raid`, `food_exhaustion` —
derived from the game's own alerts; see `smartrim/event_cause.py`). Scheduled,
informational advice stays untagged. Auto-tags are never overwritten by
re-tagging; override or refine one with:

```bash
python -m smartrim.advice_log cause <advice-id> "raider arson"       # one record
python -m smartrim.advice_log cause-match <run-id> fire "raider arson"  # whole burst
```

Backfill historical runs: `python -m smartrim.event_cause backfill --all` (idempotent; `--dry-run` to preview).

### Step 6. Ask the LLM for candidates

```bash
python -m smartrim.debrief_llm --run <run-id>
```

`debrief_llm.analyze_debrief()` sends the bundle to the configured model
(`LLM_PROVIDER`, default ollama; `LLM_MODEL_DEBRIEF`, default
`gemma4-e2b-rimworld`) and expects **Section A** as a fenced JSON array.

Each object is validated by the Pydantic `LessonCandidate` model:

| Field | Rule |
|---|---|
| `title` | short, specific |
| `cause_chain` | list of short strings |
| `trigger` | `phases`, `threats`, `resources`, `difficulty`, `storyteller`, `biome` |
| `recommendation` | what to do |
| `rationale` | failure mode prevented |
| `source` | day strings and/or `wiki:<Page>` |
| `wiki_pages_used` | pages the model actually used |
| `unverified_claims` | anything it could not ground |
| `confidence` | 0.3–0.7 (single-observation range) |

If validation fails, the model is re-asked up to 3 times with the exact schema
error plus the allowed trigger vocabulary. A final failure is recorded rather
than guessed.

The analysis is written to `runtime/<run>/debriefs/<run-id>-llm.md`.

### Step 7. Candidates are saved, not activated

`debrief_llm._write_candidate_lessons()` writes
`runtime/<run>/candidates/<run-id>-<YYYYmmdd-HHMMSS>.jsonl` with:

```json
{"id": "C-<run-id>-0", "status": "needs_review", "confidence": 0.3,
 "times_applied": 0, "times_helped": 0, "times_failed": 0,
 "source_runs": ["<run-id>"], "last_updated": "YYYY-MM-DD"}
```

A candidate is deliberately unusable at runtime: `needs_review` is not
`active`, so retrieval skips it.

---

## Part B — Human review and promotion

### Step 8. Promote (interactive)

```bash
python -m smartrim.situation promote runtime/<run>/candidates/<run-id>-<stamp>.jsonl
```

The command lists candidates and asks which to keep (`0,2` or `all`). For each
selected candidate you can edit `status` and `confidence`; blank keeps the
current value. It then:

1. assigns the next free `L-XXXX` id (auto-increment, never reused),
2. validates against the full lesson schema,
3. appends to `memory/lessons.jsonl`,
4. refreshes the SQLite index.

If validation fails you are asked to confirm before it is written anyway.

### Step 9. Validate

```bash
python -m smartrim.situation validate
```

Fails on: bad ids, missing title, missing trigger keys, enum violations,
confidence outside 0–1, a source-less lesson above 0.3, unknown status, or
negative counters.

### Step 10. Rebuild the query index

```bash
python -m smartrim.situation reindex
```

Only needed after hand-editing the JSONL; normal writes through the store and the
`_ensure_fresh` mtime check keep it current.

### Step 11. Refresh the readable render

```bash
python -m smartrim.situation render > memory/lessons-learned.md
```

---

## Part C — Manual authoring

Append one line to `memory/lessons.jsonl`:

```json
{"id": "L-0066", "title": "Short, specific lesson", "trigger": {"phases": ["early_survival"], "threats": ["low_food"], "resources": [], "difficulty": [], "storyteller": [], "biome": []}, "recommendation": "What to do.", "rationale": "Why it matters.", "source": ["session-3.md", "wiki:Food"], "confidence": 0.4, "times_applied": 0, "times_helped": 0, "times_failed": 0, "status": "active", "tags": ["food"], "source_runs": ["session-3"], "last_updated": "2026-11-04"}
```

Then run Steps 9 and 10.

Rules that matter:

- `confidence <= 0.3` is mandatory when `source` is empty. Uncited intuition may
  not outrank cited experience.
- A lesson with no phase, threat, resource, difficulty, storyteller or biome is
  too broad and is never retrieved.
- Ids are stable. Retire with `"status": "retired"`; never delete or renumber.

---

## Lesson anatomy

| Field | Notes |
|---|---|
| `id` | `L-\d{4}`, unique, never reused |
| `title` | human label |
| `trigger` | retrieval filter; `phases`/`threats`/`resources` required |
| `recommendation` | the action shown to the player |
| `rationale` | evidence / failure mode prevented |
| `source` | session files, snapshot days, `wiki:<Page>` |
| `confidence` | 0–1, moved by outcomes |
| `status` | `active` → retrieved; `needs_review` → skipped; `retired` → kept for history |
| `tags` | free-form; `early_game` sets advice timing |
| `times_applied/helped/failed` | outcome counters |
| `source_runs` | run ids that contributed or used it |
| `last_updated` | `YYYY-MM-DD` |

### Trigger vocabulary

| Field | Allowed values |
|---|---|
| `phases` | `early_survival`, `stabilization`, `raid_prep`, `expansion`, `crisis` |
| `threats` | `colonist_downed`, `mood_break_risk`, `colonist_injured`, `danger_high`, `raid_incoming`, `predator_near_worker`, `low_food`, `medical_untreated`, `idle_colonists`, `threat_response`, `colony_death`, `other_game_alert` |
| `resources` | `food_under_5_days`, `food_under_2_days`, `no_medicine`, `medicine_under_5`, `low_wood`, `low_steel` |
| `difficulty` | `Peaceful`, `Community builder`, `Adventure story`, `Strive to survive`, `Blood and dust`, `Losing is fun` |
| `storyteller` | `Cassandra Classic`, `Phoebe Chillax`, `Randy Random` |
| `biome` | any free string |

Empty list or `"any"` means unscoped for that field. These enums live in
`src/smartrim/situation.py` and must stay in sync with
`schemas/lesson.schema.json`.

---

## Command cheat sheet

| Goal | Command |
|---|---|
| Validate all lessons | `python -m smartrim.situation validate` |
| Rebuild SQLite index | `python -m smartrim.situation reindex` |
| Render markdown | `python -m smartrim.situation render > memory/lessons-learned.md` |
| Test retrieval | `python -m smartrim.situation retrieve sit.json` |
| Promote candidates | `python -m smartrim.situation promote <candidate-file>` |
| Trace a run | `python -m smartrim.situation lineage <run-id>` |
| One-command post-run pipeline | `python -m smartrim.pipeline <run-id>` |
| Build bundle | `python -m smartrim.debrief <run-id>` |
| LLM analysis | `python -m smartrim.debrief_llm --run <run-id>` |
| Backfill event causes | `python -m smartrim.event_cause backfill --all [--dry-run]` |
| Compare runs | `python -m smartrim.evaluate compare` |
| Lesson effectiveness | `python -m smartrim.evaluate lessons [--dupes]` |

---

## Gotchas

- **Never edit `memory/lessons-learned.md`.** It is generated.
- **Never hand-edit `memory/lessons.sqlite`.** It is derived.
- **`memory/` is durable, `runtime/` is disposable.** Lessons, wiki and docs are
  the only things worth backing up; deleting `runtime/` is always safe.
- **`current-run` is a sentinel, not a run id.** The monitor allocates a real
  `run-NNN-adv`/`run-NNN-obs` id at startup, writes it to
  `runtime/control/active.json`, and other processes resolve it with
  `config.resolve_run_id()`. The sentinel never names a directory.
- **Tests must not touch `memory/` or `runtime/`.** `tests/conftest.py` redirects
  the whole runtime root into `tmp_path` for every test. Leaks there previously
  produced phantom `current-run` snapshots that showed up in the UI.
- **A better lesson is not a longer one.** Prefer fewer, better-supported
  candidates; the bundle prompt caps proposals at six.
