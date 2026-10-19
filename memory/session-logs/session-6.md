# Session 6 — Run 001 (2026-10-19)

## Game Setup (per RUN-PROTOCOL.md)
- **Run ID**: run-001
- **Colony**: New Arrivals (settlement unnamed)
- **Tile**: 13 — Temperate Forest, Flat, 13.1°C, 1062 rainfall
- **Storyteller**: Cassandra Classic
- **Difficulty**: Adventure Story (Medium) — baseline for comparison with Sessions 1-3
- **Reload Mode**: Reload Anytime (no reloading during run)
- **Scenario**: Crashlanded
- **Run length**: 10 full days after Day 1 (ends at daysPassed=11)

## Colonists
| Name | Age | Gender | Top Skills | Traits | Incapable Of | Role |
|------|-----|--------|------------|--------|--------------|------|
| Matthew Po | 35 | M | Intellectual 11, Melee 9, Shooting 8 | Trigger-happy | Dumb labor | Researcher/Fighter |
| Camilla 'Cami' Maney | 28 | F | Melee 9, Cooking 7, Social 7, Medical 6 | Kind, Steadfast, Sickly | — | Cook/Medic |
| Andrew 'Andy' Camden | 30 | M | Intellectual 8, Melee 7, Shooting 6 | Industrious | — | Builder/Fighter |

## Day 0 Accomplishments
- [x] Unforbid all 52 starting items
- [x] Set work priorities for all 3
- [x] Built 7x7 wooden shelter with door at (139,137)-(145,143)
- [x] Placed 3 beds + 1 medical bed, 2 tables (1x2), stove (outside), research bench (outside), horseshoes pin (outside)
- [x] Stockpile zones: interior (143-144,138-139) + exterior (139-143,146-150)
- [x] Growing zones: potato + rice (exterior, 121 cells)
- [x] Equipped: Matthew=rifle, Cami=knife+flak vest+pants, Andy=revolver
- [x] Set research to Smithing
- [x] All colonists healthy (100 HP), moods 58-71

## Day 1-2 (7th-8th Aprimay)
- Colonists hauling, sowing rice/potato fields, researching Smithing
- No alerts (except "Need research bench" — bench is outside shelter)
- Moods: Andy 44-58, Matthew 48-70, Cami 58-76
- Resources: 49 meals, 1050 steel, 800 silver, 32 medicine, 30 components

## Final State (Day 2, Hour 16, paused)
- **Colonists**: 3 alive, all 100 HP
- **Moods**: Andy 52, Matthew 56, Cami 59
- **Resources**: 30 meals, 908 steel, 591 silver, 32 medicine, 30 components
- **Research**: Solar panel 17% (Smithing completed, switched to Solar panel)
- **Alerts**: Need defenses
- **Buildings**: 7x7 shelter, 4 beds (1 medical), 2 tables, stove, research bench (outside), horseshoes pin (outside), 2 stockpiles, potato + rice growing zones

## Outcome
Session ended by user on Day 2. No deaths. No raids yet (first raid window Days 8-15). Colony stable.

## Key Lessons
1. **Research bench placement**: Placing it outside the shelter caused "Need research bench" alert. Interior placement conflicts with bed interaction spots. Need to plan layout.
2. **Duplicate table**: Accidentally placed 2 tables. Minor waste.
3. **No sandbags**: "Need defenses" alert appeared Day 1. No cloth available for sandbags (need cotton).
4. **Moods**: Andy's mood (44-52) is lowest. Shared barracks + no individual bedrooms. Horseshoes pin helped Cami (+76).
5. **Research**: Smithing completed quickly, switched to Solar panel. Good progress.
6. **Food**: 30 meals remaining, rice/potato fields being sown. Food stable.
7. **Monitor worked**: No false pauses after food/medicine became advisory. Monitor polled every 30s without game hitches.

## Session Notes
- Monitor running with RUN_ID=run-001, 30s poll interval
- No game freeze (rate limiting + reduced poll frequency worked)
- Naming dialog appeared and was closed
- "A wait is already in progress" from stuck wait_for_event; used real-time sleep
- Game crashed once during a wide scan (4900 inspect_thing calls) — recovered
