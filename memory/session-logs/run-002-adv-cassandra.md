# Run 002 — run-002-adv-cassandra (adviser ON, 2026-10-19)

First completed 11-day evaluation run with the adviser arm on. Colony survived the full window with no deaths, no downed colonists and no mental breaks.

## Game setup (per RUN-PROTOCOL.md)

- **Run ID**: run-002-adv-cassandra (arm: on)
- **Colony**: Tedlor
- **Tile**: 17 — flat temperate forest, 13.4 C, swampiness 0.06
- **Storyteller**: Cassandra Classic
- **Difficulty**: Adventure story
- **Scenario**: Crashlanded
- **Reload**: anytime, never used
- **Run length**: 10 full days after Day 1; monitor ended the run at `daysPassed` = 11 (3rd of Jugust, 6h)

## Colonists

| Name | Top skills | Role |
|---|---|---|
| Matthew Po | Social 14, Melee 12, Shooting 10 | Shooter, researcher, social |
| Antonino 'Toni' Cefalu | Melee 12, Animals 12, Medicine 8 | Melee fighter, doctor, grower |
| Niklas Fischer | Shooting 10, Plants 7, Crafting 7 | Shooter, grower, cook, smith |

Team rule satisfied: two shooting 5+ (Matthew 10, Niklas 10) and one melee 5+ (Toni 12, Matthew 12). Construction, plants, medical and intellectual all covered between the three.

## Base built

- Dining room x190-196 z130-136 (table, stools, horseshoes outside)
- Research room x198-204 z138-144 (simple research bench, torch lamp)
- Kitchen x198-204 z146-152 (fueled stove, butcher table, food stockpile zone 2)
- Bedrooms x194-206 z156-162 (3 rooms: double bed for Toni/Niklas, single beds for Matthew and the quest knight)
- Storage x197-206 z129-138, fully enclosed and roofed around stockpile zone 1
- Workshop corner with fueled smithy (75 steel) inside the research room block
- Growing: field 1 (rice, converted from potato) + zone 4 on rich soil x201-204 z114-119
- 4 graves south of the bedrooms

## Timeline

| Day | Colonists | Min mood | Min HP | Food (days) | Notes |
|---|---|---|---|---|---|
| 8 Aprimay | 3 | 62 | 100 | 0.0 | alert: need beds, need research bench; base still being built |
| 9 Aprimay | 3 | 49 | 100 | 5.5 | growing/first harvest, research setup |
| 10 Aprimay | 3 | 43 | 100 | 4.3 | "Need defenses", trader passed |
| 11 Aprimay | 3 | 47 | 100 | 3.2 | storage room finished and roofed |
| 12 Aprimay | 3 | 64 | 100 | 2.0 | Low food alert |
| 13 Aprimay | 3 | 56 | 83 | 4.8 | first raid: Toxoid Pests waster "Crusher, Captain"; Toni took a club bruise to the neck |
| 14 Aprimay | 3 | 64 | 100 | 4.3 | Low food; berry and wild-plant harvest push |
| 15 Aprimay | 3 | 49 | 100 | 38.3 | rice harvest landed (324 rice in one tick); food crisis over |
| 1 Jugust | 3 | 54 | 100 | 30.7 | LongBlades done; longsword crafted and equipped by Toni |
| 2 Jugust | 4 | 18 | 100 | 14.2 | Hunted Knight joined and left; mood 18 on the knight; plate armor research done |
| 3 Jugust | 3 | 51 | 100 | 13.8 | run complete at `daysPassed` 11 |

## Decisions worth recording

1. **Turned the potato field into rice.** Rice yields more per day on rich soil and the colony was on a 2-day food clock.
2. **Expanded the food stockpile from 5 to 13 cells.** Harvested rice sat on the ground un-hauled because the kitchen stockpile was full; the resource readout only counts stored items, so food looked far worse than it was.
3. **Set the cook bill to a target count of 12 meals instead of "forever".** With a forever bill, Niklas cooked nonstop and never reached the smithy.
4. **Mined compacted steel next to the workshop** (40 steel per tile) when the longsword turned out to cost 100 steel and only 95 were in stock.
5. **Accepted "The Hunted Knight"** on day 10. Antigonos Baspho (Knight, psylink 3, Social 12, Intellectual 9, Melee 4) joined, was chased by a manhunter rat while wandering ~100 cells from base, got downed at (249,51) and was saved by Matthew and Toni killing the rat. He recovered, was treated with 2 industrial medicine, hit mood 15 (malnourished, pain, flu) and then the quest ended in success when the imperial shuttle collected him.
6. **Chose PlateArmor over power/freezer tech** for the last two days: it completed and gave the colony a real armor option. Simple helmet finished after it and was auto-equipped by Matthew.
7. **Never touched the ancient danger**, and left the mechanoid grav-engine quest (6 ship chunks, ~100 cells NE) alone.

## Final state (3rd of Jugust, 6h, paused by monitor)

- **Colonists**: 3 alive, all 100 HP, none downed
- **Moods**: min 51 (Niklas, Pessimist)
- **Food**: 10 simple meals, 64 rice, 9 hedgehog meat, 13.8 days of food
- **Medicine**: 27 industrial + 7 herbal
- **Resources**: 800 silver, 47 steel, 30 components, 8 wood, 27,294 colony wealth
- **Research**: 11 projects complete (includes Electricity, Smithing, LongBlades, PlateArmor); Batteries started
- **Alerts**: Rector role unfilled only
- **Monitor marker**: `urgent_alerts: 12`, `auto_pauses: 12`, `stop_reason: run_length`

## Surprises and lessons

1. **Modal dialogs silently stop time.** "Research finished: ..." force-pauses the game, and `wait_for_event` then returns `ticksWaited: 0` with the same hour forever. Always check `list_windows` when time stops advancing; close the dialog before waiting.
2. **"A wait is already in progress" is recoverable** by unpausing, letting the stale wait expire in real time, then re-pausing. Do not start new waits while one is pending.
3. **Smithing and Crafting are separate work types in this build.** The longsword bill sat untouched for hours with a colonist at Crafting 1; setting Smithing 1 started it immediately.
4. **Recipe material costs matter before promising a weapon.** Longsword = 100 steel; the colony had 95 and needed to mine.
5. **Ground food is invisible to `get_resource_readout`.** 34 rice stacks in the field did not show up until they were hauled and merged into one stack.
6. **Forever bills starve other work.** Target counts on cooking keep a producer available for smithing/research.
7. **A quest colonist wanders.** Antigonos walked to the river to swim and got downed 100 cells from base; new colonists should get an allowed area near the colony.
8. **Monitor advice log spam (bug, fixed).** 104 records for the stale run id `run-001` were written on 2026-10-19 between 07:16 and 07:40, 99 of them identical ("Medicine stock low (0); Food stock low (0 units)") plus 3 false "All colonists dead" alerts. Cause: the monitor polled while the game was not loaded (empty resource readout and zero colonists), and the duplicate guard lived only in process memory, so restarts re-logged the same urgent set. Fixed in `sidecar/monitor.py`: an identical still-open situation is never logged twice (`advice_log.find_open_duplicate`), the last signature is persisted to `memory/alerts/last_signature.json`, low-stock checks are skipped when the readout is empty, and "all colonists dead" requires the monitor to have seen the colony alive at least once. Run-002's own 23 records are clean (19 expired, 3 helped, 1 failed).
9. **Low-mood knights are a mood sink.** High expectations (+6) never offset pain (-10), illness (-5) and malnutrition (-20); the knight spent two days between 15 and 30 mood. Only accept that quest when the colony has a proper bedroom, food access and a meditation spot.

## Additions to memory to follow up

- `mechanics.md`: separate Smithing/Crafting work types; modal dialogs stall time.
- `lessons-learned.md`: ground food not counted by the resource readout; forever-bill labour starvation; new colonists need an allowed area.
- `sidecar/monitor.py`: dedupe guard for repeated identical urgent signatures and a "game not loaded" startup check.
