# SmartRim workflow review — 2026-11-05

**Scope:** the end-to-end workflow — observe → classify → retrieve → advise/act → track outcomes → debrief → promote → permanent memory — assessed against the stated long-term goal: *an autonomous agent that plays RimWorld, analyzes its own runs, and accumulates permanent memory that makes it better over time.*

**Method:** code reading (`monitor.py`, `situation.py`, `outcomes.py`, `advice_log.py`, `reflex_actor.py`, `config.py`, `cli.py`), the 260-test suite (green), CI config, git history, and — decisively — the runtime data left by the 9 runs played today (`runtime/run-001..009-adv/`) and the durable store (`memory/lessons.jsonl`, 74 lessons).

---

## 1. Executive summary

The **scaffolding is good**: the safety layering, the disposable-runtime/durable-memory split, the validated lesson schema, the wiki cache, and the debrief bundle are all real, tested, and mostly thought through. The **loop does not close**. Every stage of the intended self-improvement circuit either (a) is disabled, (b) never fires, or (c) produces noise that nothing consumes:

- **0 of 56 advice records** across all runs have ever been judged `helped` or `failed`. They are all `expired` (36) or `open` (20). The feedback signal into lesson confidence is zero.
- **7 of 9 runs today never reached an end marker**, so they can never be debriefed, scored, or learned from. One of the two markers that exist (`run-009-adv`) carries a `stop_reason` the codebase never emits — it was hand-written.
- **Debrief candidates are never auto-promoted, and promotion defaults them to `needs_review`**, which retrieval skips — so even the lessons that *were* promoted from run-001/run-002 (L-0067..L-0074) never influence advice. Only L-0070 is active.
- **The agent has never successfully played a single turn.** Reflex is globally disabled in `.env` (`REFLEX_KILL=1`, `REFLEX_DRY_RUN=1`), and every recorded reflex action shows `executed: false` with no failure reason.
- `times_applied` (1,396) counts advice *closures*, not applications: `"expired"` increments it. The store rewards retrieval frequency, not causal value — L-0030 ("Wait is already in progress", a game quirk) has 278 "applies" and 103 "helped".

**Verdict:** SmartRim is currently an excellent *observation + advice harness* with a decorative learning loop. It is not yet an agent, and its memory grows without ever getting better. The good news: the failure modes are specific, measurable, and mostly closeable with focused work (Section 6).

---

## 2. The workflow as it actually runs today

Intended (from WORKFLOW.md / docs):

```
poll → situation → retrieve → advice → day-roll closes outcomes → end.json
     → debrief bundle → LLM analysis → candidate lessons → human promote
     → lessons.jsonl → SQLite → better retrieval tomorrow
```

Verified actual (today's data):

```
poll (30s) ✅ → classify ✅ → retrieve (FTS, works) ✅ → advice logged ✅
day-roll closes outcomes ❌ (see F1) → end.json only for 2/9 runs ❌ (F3)
bundle built for 3 runs ⚠️ → LLM analysis never run ❌ → candidates promoted
by hand, 7 of 8 left needs_review ❌ → retrieval unchanged ❌
```

Key numbers:

| Metric | Value |
|---|---|
| Runs played (2026-11-05) | 9, all adviser-on; none an observe-only control |
| Runs with `end.json` | 2 (run-001 `run_length` — legit; run-009 `manual_close` — not a code path) |
| Runs with debrief bundle | 3 (001, 002, 009) |
| Runs with LLM candidate analysis | 0 (run-009 bundle built, analysis never ran; candidates file is an empty template) |
| Advice records | 56 (50 scheduled, 6 reflex) — 36 expired, 20 open, **0 helped/failed** |
| Reflex actions recorded | ~43; **0 executed**; all `dry_run: false` but blocked/failed silently, no reason logged |
| Lessons promoted from runs | 8 (L-0067..L-0074); 7 left `needs_review` → invisible to retrieval |
| Lessons with inflated counters | L-0030 (278/103/16), L-0040 (235/94/4), L-0044, L-0048, L-0022 — all `conf=1.0` by drift on noise |
| Wiki-fact grounding in debriefs | Works (bundle verified against local wiki); `event_cause` filled on **0/56** records |
| Tests / CI | 260 passed; CI runs ruff + pytest + `situation validate` — good |

---

## 3. Findings (by severity)

### F1 — Critical: the outcome feedback loop is dead, so memory cannot improve

`outcomes.close_outcomes()` runs at each day roll, but:

1. It calls `expire_stale()` **first**, marking every `open` record older than **3 wall-clock days** as `expired`. Only records still `open`/`applied` are then judged — so anything not judged within 3 days can never produce a signal. (A 10-day run routinely exceeds that.)
2. Even for young records, judging only works for advice whose situation text contains `food|medicine|mood|injur|health`. Scheduled daily assessments match none of these branches; they fall through to `"risk cleared"` → `expired` — which **also increments `times_applied`** (any non-`None` status does).
3. `times_applied` therefore means "this lesson was linked to a daily advice that got closed", i.e. retrieval frequency × days, not "the agent applied the lesson and it worked". L-0030 matches every phase with no threat/resource scoping → 278 applies → confidence ratcheted to 1.0. Same mechanism for L-0040, L-0044, L-0048, L-0022.
4. `helped`/`failed` require the food/medicine/mood branch and an in-game improvement the heuristic can see; today that produced **zero** labels. Confidence has effectively never moved from measured outcomes.
5. `expire_stale` (wall-clock) also silently discards information for the debrief: by analysis time, most records are `expired` and `debrief_bundle` sees a pile of dead entries.

**Consequence:** the system's central promise — *permanent memory that gets better* — is unfulfilled. Memory can only grow (never be demoted by evidence) and its most-used lessons float to confidence 1.0 regardless of value.

**Fix (small, surgical):**
- Judge at each day roll **before** expiring; replace wall-clock age with **in-game age** (from `daysPassed` in the snapshot vs the record's `snapshot_day`).
- Count `times_applied` only on `helped`/`failed` (or track `times_linked` separately and stop using it for ranking).
- Let expiry leave advice `open` for N day-rolls and write a distinct `expired` that does **not** touch lesson counters.
- Rank retrieval by `(helped − failed) / max(applied, 1)` with a minimum-evidence threshold, not raw confidence.

### F2 — Critical: debrief → promote → retrieve is manual and unused; memory never reaches the agent

- Runs 003–008 (6 of 9) were never debriefed. Run-009 got a bundle but no LLM analysis; its `candidates/` contains the empty debrief template.
- Promotion is interactive (`situation promote`, stdin prompts) with no batch/CI/non-interactive mode — the pipeline doc lists "non-interactive promotion" as a *future* item.
- Promoted lessons default to `needs_review`; retrieval filters `status == "active"`. Today's promoted set (L-0067..L-0074): **7 of 8 never injected** into advice. L-0070 (active) is the only one that can help, and it's a single observation.
- No deduplication: run-001 and run-002 independently re-proposed the same lessons (food buffer, defenses-before-raid, medicine stockpile). Promoting both generations pollutes the store with near-copies.
- The human must remember to run three manual steps after every run; nothing in the monitor nudges, triggers, or verifies this. Predictably, it rarely happened.

**Fix:** one command — `smartrim debrief <run-id>` → build bundle → LLM (with the benchmark-winning settings) → validate → **auto-promote if cited + schema-valid + not a duplicate, else queue for review** → regenerate render → commit. Human approval becomes the exception (low-confidence/conflicting candidates). Log every auto-promotion to `runtime/<run>/actions.jsonl`-style audit.

### F3 — High: abandoned runs have no closeout path; evaluation data is corrupted

- 7 of 9 runs have no `end.json`. The debrief bundle requires it (`_load_run_marker` / `_derive_outcome`); `evaluate summarize/compare` requires it; the human simply closed the game and started a new one.
- `run-009-adv/end.json` says `"stop_reason": "manual_close"` with `"days_passed": 13` — **no code path in the repo writes `manual_close`** (only `run_length` / `colony_death`), and the monitor log shows it never hit the day-11 stop. The marker was hand-written to "close" the run, bypassing every check (`RUN_DAYS=11` in `.env`).
- RUN-PROTOCOL demands alternate adviser on/off runs for comparison; today has zero `obs` arms, so the adviser's effect on outcomes is unmeasured. Protocol drift has become the default.

**Fix:** real code path for manual/abort closeout: on shutdown, on next monitor start (scan for the previous run dir with snapshots but no `end.json`), or via `smartrim close` — capture a final snapshot, derive outcome, write `end.json` with `stop_reason` from an enum the schema enforces, and flag the run `inconclusive` for evaluation. Evaluation tooling must **exclude or quarantine inconclusive runs**, not silently mix them in.

### F4 — High: "getting better over time" is currently unmeasurable

- `evaluate compare` can compare arms, but there is no paired data (F3) and no instrumentation of "did this run play well" beyond days-survived/colonists-alive/alert counts.
- No baseline arm, no seeded identical starts (the protocol fixes scenario/storyteller/difficulty/team pick, which is good), no lesson-effectiveness report.
- Nothing measures retrieval precision (were the linked lessons the right ones?), advice acceptance by the human, or downstream colony impact.

**Fix:** protocol enforcement as tooling (monitor refuses to start a run without a recorded tile id/team; writes a settings fingerprint into `meta.json`); `evaluate compare` refuses mismatched protocols; per-lesson effectiveness report (`smartrim evaluate lessons`) — helped rate with min-N evidence; feed that back into retrieval ranking (see F1).

### F5 — High: the agent cannot play yet — reflex is disabled and unproven

- `.env` today: `REFLEX_KILL=1`, `REFLEX_DRY_RUN=1`. Even while enabled (yesterday's commits), **every recorded action shows `executed: false`**. For `ensure_food_supply` with preconditions passing, `_execute()` returned false and the audit record doesn't say why (zones unread? cooking bill refused? MCP error swallowed?).
- Reflex coverage is ~7 whitelisted actions, all reactive (draft, rescue, beds, food, research). No build/plan/economy/defense layer; no objective-driven play.
- The monitor **pauses the game on every urgent alert** unless reflex is enabled — the opposite of an autonomous player's behavior, and with reflex off it means SmartRim is a notifier, not an actor.
- `write_run_end` + `set_speed pause` on run end is fine; but there is no "resume and keep playing" arm.

**Fix:** (1) instrument `_execute` to record the failing step/MCP error into the audit record; (2) pick **one** action (`ensure_food_supply`), fix it end-to-end, prove `executed: true` on a disposable save, then expand the whitelist one action at a time; (3) define a minimal daily plan objective (food≥3d, research set, beds assigned, defenses up) and have the reflex work the plan, not just react to alerts; (4) only then discuss "playing" vs "assisting".

### F6 — Medium: memory hygiene — pile-up, duplicates, inflated broad lessons

- 13 `needs_review` lessons accumulate (candidates + failed-3×); nothing reclaims or reminds.
- Duplicates across runs (food buffer ×2, defenses ×2, medicine ×2 — today).
- Retrieval has no specificity term: phase-only broad lessons (L-0030 class) are retrieved constantly and starve out specific ones.
- No anti-triggers (`not_when`), no counter-evidence recording beyond counters.
- `lessons.jsonl` is hand-edited; CI validates schema but not duplication/contradiction.

**Fix:** dedup on promotion (title/recommendation embedding similarity, reject >0.85); specificity score in ranking; quarantine report; `retire` policy with reason; weekly `smartrim memory doctor` (dupes, never-retrieved, retrieved-but-never-helped).

### F7 — Medium: `event_cause` is never filled (0/56) — debriefs see symptoms, not causes

The protocol requires tagging causes before debrief; the LLM debrief quality depends on it; nobody did it once in nine runs. The tooling exists (`advice_log cause-match`) but is manual and un-prompted.

**Fix:** the monitor asks one in-game question per incident via `say` ("SmartRim: cause of the fire?") and the pre/post-incident snapshot diff is auto-attached; if RimMolt can't capture the answer, auto-tag with the game's own letter text (RimMolt exposes letters) instead of humans.

### F8 — Medium: documentation drift and protocol decay

- RUN-PROTOCOL.md and PROJECT-OVERVIEW.md still reference `sidecar/` paths and `python cli.py`; WORKFLOW.md documents the intended flow accurately but not the manual/abandoned-run failure mode that is now the common case; `memory/session-logs/` referenced throughout, never existed.
- The protocol is unenforced by tooling, so it is decorative — 9 runs in a day, zero compliant.

**Fix:** treat protocol as config, not prose: `smartrim run start --arm adv|off` writes `meta.json` (tile, team, settings fingerprint), `preflight` check, and the debrief/evaluate steps refuse on inconclusive runs. Prune stale docs; keep WORKFLOW.md as the single source and make the review date part of CI.

### F9 — Low: architectural fragility around run identity and retrieval

- Run-id resolution is patched across module globals (`monitor` patches `smartrim.config.RUN_ID`); `ReflexActor` resolved its audit path at import time and wrote run-003's actions into run-002's `actions.jsonl` (fixed at 21:58 in `194412e`; runs 006–009 clean). The class of bug persists in the pattern `config.RUN_ID` + `resolve_run_id()` fallbacks + `rebind_run`.
- Dual retrieval paths (legacy JSONL scan vs SQLite FTS) must stay behavior-identical; `rank_actions` re-queries FTS per alert (N+1).
- `monitor.py` ≈ 1,000 lines with pid/lock/threading/background-LLM concerns interleaved; the background executor is fire-and-forget with no backpressure.

**Fix:** pass `run_id` explicitly through call chains (no module-global patching); single retrieval path; cache the store; extract the poll-cycle into testable stages.

### F10 — Low: the product goal mismatch — companion vs agent

Everything is built to *advise a human* (say, pause, debrief-assist). The stated goal is an agent that plays. The pause-on-urgent default, the human-only promotion step, and the disabled reflex all optimize for the human. This isn't a bug, but it means "autonomous play" needs deliberate product decisions (see Section 6, P2), not just enablement of existing flags.

---

## 4. What is genuinely good (keep)

- **Safety layering for actions**: KILL → per-day PAUSE → PID lock → 60 s human-action window → preconditions → cooldown → dry-run → say-intent → audit. Designed well; hold onto it.
- **Memory separation**: `memory/` durable + tracked; `runtime/` disposable; SQLite derived; `lessons-learned.md` generated. Sound.
- **Schema + CI gate**: lessons validated in CI; promotion reuses the same validator. Good bones for auto-promotion.
- **Bundle v3**: event digest, verified-wiki-facts section, explicit unverified-claims list — better grounded than most LLM pipelines.
- **Testability**: situation/outcomes/retrieval are pure and tested; 260 green.
- **Honest audit trail** (when it works): actions.jsonl + advice.jsonl are enough to reconstruct decisions — the data exists, it's just not consumed.

---

## 5. Gap analysis vs the long goal

| Capability (goal) | Present? | Reality |
|---|---|---|
| Observe colony state | ✅ | Solid, well-structured snapshots + alerts derivation |
| Classify situations | ✅ | Pure, tested; vocabulary synced with schema |
| Retrieve relevant knowledge | ✅ | FTS works; ranking broken by F1/F6 |
| Advise / act on it | ⚠️ | Advice yes; action disabled + unproven (F5) |
| End-of-run self-analysis | ⚠️ | Bundle + LLM path built; never run end-to-end; manual triggers (F2) |
| Convert lessons into permanent memory | ⚠️ | Format + store fine; feedback dead (F1), promotion invisible (F2) |
| Get measurably better over time | ❌ | No paired evaluation, no lesson efficacy tracking (F4) |
| Play autonomously | ❌ | No planner, no execute-verified actions, pause-not-play (F5, F10) |

---

## 6. Recommended plan (ordered)

**P0 — Close the loop (1–2 sessions)**
1. Fix outcome judging: pre-judge before expire; in-game-day age; split `times_linked` from `times_applied`; drop `expired` from lesson counters. (F1)
2. Auto-closeout for abandoned runs; `stop_reason` enum in schema; evaluate quarantines inconclusive runs. (F3)
3. One-command debrief with auto-promote-by-rule (cited + valid + non-duplicate + confidence ≤0.6) and a review queue for the rest; end-of-run hook in the monitor prompts once, non-interactively. (F2)
4. Record `event_cause` automatically from letters / auto-tag; make it part of the bundle, not homework. (F7)

**P1 — Make improvement measurable (next)**
5. Enforce the adv/obs pair; settings fingerprint in `meta.json`; `evaluate` refuses mismatched protocols. (F4)
6. Per-lesson effectiveness report; retrieval ranked by win-rate with min-N evidence; specificity term; dedup on promote; memory doctor. (F1, F6)
7. Wire confidence demotion into retrieval (a 0-fer-10 lesson must sink). Retire by evidence, not by hand.

**P2 — Toward actual play (then)**
8. Fix one reflex action end-to-end; prove `executed: true`; expand whitelist incrementally; audit records must say *why* on failure. (F5)
9. Introduce a minimal daily plan objective (food buffer, research, beds, defenses, power) and let reflex work the plan; keep humans as supervisors, not micro-managers. (F10)
10. Protocol as config: `smartrim run start/close` instead of prose; prune `sidecar/` references; single WORKFLOW.md source of truth. (F8)

---

## 7. What I verified (and how)

- Test suite: `python -m pytest` → **260 passed, 1 skipped**.
- Runtime evidence: all 9 runs' `advice.jsonl`, `actions.jsonl`, `end.json`/absence, debriefs, candidates; `memory/lessons.jsonl` aggregates; monitor log; `.env` flags; CI workflow; git history (incl. `194412e` "audit into the right run").
- Not verified: the game itself / RimMolt behavior in-session; whether `manual_close` end.json was produced by an external agent or hand-edited (no code path writes it either way — flagging as data of unknown provenance).
- `.env` currently has reflex fully disabled; any claim about live reflex behavior should be re-tested on a disposable save before trusting it.

---

## 8. Bottom line

SmartRim has built the **nervous system and the memory organ**, but the memory organ is not connected to the nervous system's outcome signals — it fills up with observations that are never judged and never recalled. Close the loop (P0), make improvement measurable (P1), and only then ask it to play (P2). Do those in order and the long goal is reachable; today, more features added to the play layer would outrun the feedback loop that is supposed to make them safe and cumulative.
