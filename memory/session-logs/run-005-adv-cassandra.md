# Run 005 — run-005-adv-cassandra (adviser ON, 2026-10-22..23)

## Game setup (per RUN-PROTOCOL.md)

- **Run ID**: run-005-adv-cassandra (arm: on, adviser ON)
- **Colony**: New Arrivals → auto-renamed "Moral Covenant of Southeastern Rehejadio", settlement "Body's Lagoon"
- **Tile**: 29631 — temperate forest, LargeHills, region "Lanlalium Cliffs", road nearby, no river
- **Storyteller**: Cassandra Classic
- **Difficulty**: Adventure story
- **Scenario**: Crashlanded
- **Reload**: anytime, never used
- **Run length**: 10 full days after Day 1; monitor ended the run at `daysPassed` = 11
- **Monitor**: reflex monitor, adviser ON, 30s poll (raised to 120s mid-run to reduce in-game disruption)

## Colonists

| Name | Top skills | Role |
|---|---|---|
| Yuudai O'Neal | Melee 11, Mining 7, Shooting 6 | Melee fighter, miner, shooter |
| Sera 'Kaleun' Steiner | Social 12, Intellectual 13, Shooting 8 | Shooter, researcher, social/recruiter, noble |
| Alexander 'Alex' Millev | Construction 9, Melee 7, Intellectual 6 | Builder, melee fighter, doctor |
| Ishca Jean (joined day 9) | Animals 9, Construction 4, Cooking 4 | Handler, general labour |

Team rule satisfied: two shooting 5+ (Yuudai 6, Sera 8), one melee 5+ (Yuudai 11, Alex 7). Construction, mining, medical, intellectual and social all covered. No incapabilities of Violent or Caring. Tiles is LargeHills rather than flat; temperate-forest biome matches the protocol.

## Timeline by day (Aprimay 5500)

| Day | Highlights |
|---|---|
| 1 (1st) | Crashlanded, 3 founders. All 12 starting items unforbidden. Work priorities set (Firefighter/Patient 1; Yuudai Mining 1; Sera Research 1; Alex Construction 1). Steel 150. |
| 2 (2nd) | Research Batteries 24%. Steel 398. Moods 54-81. |
| 3 (3rd) | Batteries 49%. Cargo-pod medicine (25) and berries (10) recovered. First **Low food** alert. First trader. |
| 4 (4th) | Batteries 73%. Silver 500. Trader. |
| 5 (5th) | Batteries complete; **Solar panels** started. Wood 120. Alerts: Need batteries, Need colonist beds, Low food. |
| 6 (6th) | Solar 20%. Packaged survival meals 13, smokeleaf 6. **Raid ~21:00**: hostile "Swamp" (Priest) downed; Alex fought him in melee, dropped to 76 HP, treated same night. |
| 7 (7th) | Solar 24%. "Wild woman wanders in" event. **Mechanoid Signal** quest surfaces. Food buffer 10.2 days. |
| 8 (8th) | Solar 24%. "Ancient mech" letter. **Ally downed: Eggs** (Critical). Animal wandering away. Min mood 42. |
| 9 (9th) | **Kaleun's Novice Ceremony** (EndedSuccess) and **The Ambushed Praetor** accepted + EndedSuccess (8 honor). Yuudai mood crashed to 16-17% with **Starvation** — ate a packaged survival meal, recovered. Wild woman **Ishca Jean joins** at 46% HP. Jean downed ~hour 20. Low food (2 days). |
| 10 (10th) | Jean recovering (71%). Bulk-goods trader from Paberon. Solar 35%. Low food continues (5-6 bars). |
| 11 (11th, ends 12th Aprimay 07:00) | Run end. **Starvation** (Kaleun, Alex, then Yuudai). **Minor break risk** (Jean). All 4 colonists alive. |

## Decisions

- Picked the team by the protocol rule (rerolled to safe fighters/doctors), not by best skills.
- Prioritised survival basics: unforbid crash-site loot, set Mining/Construction/Research to 1 for the specialists.
- Left the mechanoid-signal quest unaccepted (no fighter margin, mechanoid risk on Adventure).
- Accepted and completed the Empire chain (Ambushed Praetor → Novice Ceremony) for honor/psylink and the mood bonus.
- Did not build a freezer, medical beds or enclosed pens: the run ended before those paid back (see Surprises).
- Investigated and fixed a camera-steal bug in the monitor mid-run (removed `get_pawn`, removed duplicate predator/hostile proximity checks — `get_alerts` already covers them), and removed redundant deep checks.

## Outcome

- **Days survived**: 11/11 (full protocol length, `stop_reason: run_length`).
- **Colonists alive at end**: 4/4 (health 83-100, mood 30-72).
- **Lowest mood reached**: 16% (Yuudai, day 9) — major break risk, no break occurred.
- **Downed**: Ishca Jean (day 10), recovered to 83%. No founder downed.
- **Urgent alerts / auto-pauses**: 11 urgent records, 11 auto-pauses (all reflex urgents). Marked helped 4, failed 0.
- **First Low food alert**: day 3 (3rd Aprimay). **First medical alert**: day 6 (raid).
- **Research**: 8 completed; solar panels 35% at end.
- **Wealth**: ~19,529. Final resources: silver 635, wood 281, steel 98, rice 96, berries 10, medicine 28, components 26.
- **Final alerts**: Low food, Starvation, Minor break risk (Jean), Need colonist beds, Need batteries, Unroofed electrical, Combatant unarmed, Shaman role unfilled.
- **Quests**: Mechanoid Signal (Ongoing, unaccepted); The Ambushed Praetor (EndedSuccess); Kaleun's Novice Ceremony (EndedSuccess).

## What surprised me

1. **Starvation beside a full pantry.** The end-of-run Starvation alert (Kaleun, Alex, Yuudai) fired with ~96 rice and 10 berries stored and the game reporting "12 days worth of food". The cause was mechanical, not behavioural: **one hidden conduit was never built, the electric stove had no power, and no cooked meals were produced** — and the colonists would not eat raw rice/berries. The player did not realise the stove was unpowered. This was the single biggest risk of the run and the reflex layer could not see it (the alert says "no food", the data said "96 rice").
2. **The same incident generated 5 urgent records.** Ishca Jean's health alerts fired at 46%, 47%, 48% and 49% plus the DOWNED record — five auto-pauses for one slow bleed-out that was already being treated. The dedupe in `find_open_duplicate` only matches identical situation strings, so a one-point drift defeats it.
3. **The run-end metrics were reset by a mid-run monitor restart.** `run-005-adv-cassandra.end.json` reports `urgent_alerts: 0, auto_pauses: 0, reflex_snapshots: 0`, but the append-only advice log holds 11 urgent records and 11 auto-pauses. The counter reset makes the end marker disagree with the ground truth used by the comparison set.
4. **A wild-woman join is not a free colonist.** Jean arrived at 46% HP, occupied a bed and a doctor for most of day 9-10, and was downed before recovering. The colony gained a colonist but lost two days of Alex's building time.
5. **Mood is the binding constraint, not raw food.** Two days had min mood 42/37/16 — driven by starvation (no cooked meals), shared barracks and a missing meditation spot — while the pantry was never really empty. Mood management (usable cooking, beds, recreation, meditation, eating) is what nearly broke the colony.
6. **Zero mental breaks despite repeated major-break-risk warnings.** The mood-major reflex pause came with concrete actions (corpse removal, recreation, bedrooms) and the risk cleared each time; that is the reflex layer working as intended.

## Protocol deviations (affect comparability)

1. **Game crash + reload.** RimWorld crashed mid-run and was restarted from the latest save. The
   protocol forbids reloading during a run; this was an unintended reload, not save-scumming, but
   it breaks strict comparability with run-002/run-004.
2. **Monitor restarts mid-run.** The monitor was stopped/started several times to ship the
   camera-steal fix. Because the end marker's counters reset on each restart,
   `run-005-adv-cassandra.end.json` reports `urgent_alerts: 0, auto_pauses: 0, reflex_snapshots: 0`
   while the append-only advice log holds **11 urgent records and 11 auto-pauses**. The advice log
   is the ground truth; the end marker under-counts.
3. **Tile not flat.** The tile picked (29631) is LargeHills rather than the flat temperate forest
   the protocol specifies; biome matches.
4. **Full-suite bootstrap.** All three founders were picked without incapabilities as required.

## Causes (recorded after the run, from the player)

The bundle can see symptoms, not causes. These are the player's accounts, tagged into
`memory/advice/advice.jsonl` as `event_cause` for the relevant advice ids.

- **Day 6 hostile (Swamp, Priest)** — a faction/quest attacker. Alex met him in melee and was
  wounded to 76 HP; the attacker was downed. (adv-...-010751, adv-...-010824)
- **Day 8 ally `Eggs` downed + killed** — a **colonist social fight**: a pawn insulted the
  others, the player tried to arrest him and failed, violence escalated and gunshots were fired.
  By the time the player realised what was happening it was too late to save Eggs. (adv-...-014746)
  *Lesson pointer: a failed arrest of an insulting colonist escalates to lethal gunfire; separate
  or down the aggressor before attempting an arrest.*
- **Day 9 Yuudai mood 16-17%** — starvation, because there were **no cooked meals** (see below);
  he ate a packaged survival meal and the mood recovered. Shared barracks contributed. (adv-...-043733, adv-...-043908)
- **Day 9-10 Ishca Jean downed at 46-50% HP** — the player **did not observe** what happened
  (she was bedridden and being tended). She joined at 46% HP, was downed while treated, and
  recovered to 83% by run end. (adv-...-044249, -044425, -044734, -054842, -044043, -054914)
- **End-of-run starvation (Kaleun, Alex, Yuudai) with ~96 rice stored** — **one hidden conduit
  was never built, so the electric stove had no power**. The stove was unusable, so no cooked
  meals were produced, and the colonists would not fall back on raw rice/berries. The player did
  not realise the stove was unpowered. (adv-...-878a68, adv-...-7b6601)
  *Lesson pointer: verify powered cooking (or a fueled stove) before assuming food security; a
  "low food"/"starvation" alert can mean "no edible meals", not "no foodstuffs".*
