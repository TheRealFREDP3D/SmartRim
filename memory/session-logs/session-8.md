# Session 8 - Run 007 (adviser on, 2026-10-25)

## Game Setup (per RUN-PROTOCOL.md)

- **Run ID**: run-007-adv-cassandra
- **Colony**: New Arrivals -> renamed "Ereston"; faction "Alliance of Doroeron"
- **Scenario**: Crashlanded (3 survivors)
- **Tile**: 39 - Temperate Forest, Flat, 11.8 C, rainfall 1867mm, swampiness 0, pollution 0
  - Surroundings: 91/91 tiles temperate forest, 79 flat, river + road nearby, no hostile settlements
  - Rejected tile 5 (hostile Dozvzaz settlement 3 tiles NE)
- **Storyteller**: Cassandra Classic
- **Difficulty**: Adventure story (Medium)
- **Reload Mode**: Reload Anytime (no reloading during run)
- **Ideology**: Fluid - "Deviism", generated defaults, no edits
- **Run length**: 10 full days after Day 1 (ends at daysPassed=11)
- **Monitor**: RUN_ID=run-007-adv-cassandra, adviser ON, 30s poll interval
- **Division of labour**: agent drove setup via MCP, then the player took over the colony.
  The agent did not act in-game after landing.

## Colonists

| Name | Age | Gender | Top Skills | Traits | Incapable Of | Health | Role |
|------|-----|--------|------------|--------|--------------|--------|------|
| Leighton 'Speedy' Blackburn | 54 | M | Intellectual 11, Medical 9, Cooking 7, Construction 5 | Ascetic | - | 100 HP | Researcher/Medic/Cook |
| Steven Wilcox | 25 | M | Shooting 9, Melee 8, Social 8, Animals 7 | Desensitized, Kind | - | 100 HP | Fighter |
| Niklas Fischer | 34 | M | Shooting 10, Cooking 7, Construction 6, Medical 6 | Groundbreaker | Artistic | 100 HP | Shooter/Medic/Cook |

Team totals: shooting 22, melee 10, medical 15, construction 12, intellectual 13, cooking 16.

Protocol gate: all three PASS (none incapable of Violent or Caring).

### Selection notes
- Default team rejected: only 1 shooter, a pregnant colonist, no construction/plants coverage.
- Slot 0 rerolled twice. First roll (Samantha von Aachen: intellectual 6, medical 1) was a
  regression - rejected. Second roll used `intellectual >= 8` + healthy, matched after 7 attempts.
- Slot 1 rerolled with `shooting >= 6, melee >= 5`, avoid Pyromaniac/Slothful, healthy - matched
  after 29 attempts. This avoided a Pyromaniac who was also incapable of Firefighting.
- Slot 2 rerolled with `shooting >= 5` + healthy - matched after 34 attempts.
- Player validated the selection before `start_game` was called.

## Timeline

| Day | Date | Food days | Moods (S/L/N) | Notable alerts |
|-----|------|-----------|---------------|----------------|
| 0 | 6th of Aprimay | 0.0 | 71/59/71 | Need colonist beds, Pen needed, Combatant unarmed, Need recreation variety |
| 1 | 7th of Aprimay | 7.2 | 75/71/67 | Pen needed |
| 2 | 8th of Aprimay | 3.5 | 71/78/68 | Need research project |
| 3 | 9th of Aprimay | 7.0 | 77/77/63 | Need defenses |
| 4 | 10th of Aprimay | 6.0 | 77/76/80 | Need defenses |
| 5 | 11th of Aprimay | 5.3 | 60/61/79 | Need defenses -> **raid, enemy downed** (auto-pause) |
| 6 | 12th of Aprimay | 5.0 | 76/93/88 | (none) |
| 7 | 13th of Aprimay | 4.2 | 76/87/81 | (none) |
| 8 | 14th of Aprimay | 3.3 | 67/69/67 | (none) |
| 9 | 15th of Aprimay | 2.5 | 75/54/76 | Starvation, Need batteries |
| 10 | 1st of Jugust | 1.5 | 69/71/68 | Need batteries, Quest expires in 4 hours -> rice harvest (food 15 -> 205) |
| 11 | 2nd of Jugust | 2.2 | **17**/58/72 | Need batteries, Archaka role unfilled, Trader, **Starvation**, **Major break risk** |

## Event causes (confirmed by the player)

- **Starvation (days 9-11)**: plant-cutting work was not assigned a high enough priority, so
  harvested crops were not processed into meals. This is recorded in the run metadata and now
  renders in bundle section 2 as ground truth.
- **Raid on 11th of Aprimay (enemy downed, auto-pause)**: hostile raid; one enemy downed,
  no colonist injuries.

Note: the starvation cause did **not** produce an advice record, so `advice_log cause-match`
could not attach it (it matches on the advice `situation` field only). A run-level `causes`
list in the run metadata was added to carry causes that belong to the whole run.

## Outcome

- **Survived the full run** (11 days, run-limited). 3 colonists alive, all at 100 HP, none downed.
- **Lowest end-of-day mood: 17%** (Steven Wilcox) - major break risk at the end.
- **Ended in Starvation** with 2.2 days of food, despite a rice harvest landing on day 10.
- **Wealth**: 24364. **Research**: Batteries 44%, 7 completed / 164 total.
- **1 urgent alert** (enemy downed during a raid), **1 auto-pause**, **1 reflex snapshot**.
- **Construction stalled**: 18 wall sites sat unbuilt for 3+ days; 'Need defenses' alert from day 3.
- **Quests**: Beggars Seek Aid (EndedSuccess), Mechanoid Signal (Ongoing),
  The Fleeing Knight (accepted by Kaleun, EndedOfferExpired).

## What went wrong / what to look at next

1. **Food was the failure mode, not raids.** Food days never recovered above 7.2 and decayed
   steadily from day 7. A rice harvest landed on 1st of Jugust (15 -> 205 units) but the colony
   burned through it within a day, and the 'Starvation' alert still fired. L-0016
   ("Food runs low by Day 6-7") was retrieved by the adviser on 7 of 14 days but the run
   still ended starving. Either the cooking bill target was set too high / "forever", or
   the growing zone was too small to cover 3 consumers. **L-0041** (forever cook bills) is the
   likely culprit and it was applied on 4 days.
2. **Construction never got going.** 18 walls unbuilt for 3+ days and 'Need defenses' from
   day 3 onward. L-0017 (construction not prioritised) has `times_applied: 0` - it was never
   even surfaced. This is a retrieval gap, not a player failure.
3. **Steven's mood collapse (17%)** followed the starvation, not the raid. His traits
   (Desensitized, Kind) are mood-neutral, so the food shortage is the driver.
4. **The adviser's daily advice repeated the same three actions almost every day**
   (wait_for_event fallback, Smithing work type, research queue) and rarely mentioned food
   until day 9. The retrieval prioritised generic lessons over the run-specific L-0016/L-0041.

## Bugs found and fixed during this session

- `setup_logging()` was never called by any module -> the monitor wrote an empty log and
  looked dead. Fixed in `monitor.main()`.
- `stop-monitor.ps1` matched `*monitor.py*` but the monitor runs as `-m smartrim.monitor`,
  so it could never stop it.
- No monitor watchdog: added `watchdog-monitor.ps1` (verified by killing the monitor -
  restarted within ~16s).
- `debrief.py` treated `--help` as a run id and generated a full bundle for a file named
  `--help.md`. Now prints usage.
- `quests_from_snapshots()` duplicated the quest state history on every snapshot
  (`NotYetAccepted -> Ongoing -> EndedSuccess` repeated 8x). Now merges as an ordered union.

## Debrief

- Bundle: `memory/debriefs/run-007-adv-cassandra.bundle.md` (15,159 chars, 8 sections, all populated)
- Response: `memory/debriefs/run-007-adv-cassandra.response.md` (to be filled by the model)
- Candidate lessons template: `memory/candidates/run-007-adv-cassandra.md`
- Score with `memory/debrief-rubric.md`; ask the player for corrections before finalising.
