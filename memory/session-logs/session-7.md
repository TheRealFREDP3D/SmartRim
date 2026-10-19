# Session 7 — Run 001 (partial, 2026-10-19)

## Game Setup (per RUN-PROTOCOL.md)
- **Run ID**: run-001
- **Colony**: New Arrivals
- **Tile**: 13 — Temperate Forest, Flat, 13.1°C, 1062 rainfall
- **Storyteller**: Cassandra Classic
- **Difficulty**: Adventure Story (Medium) — baseline for comparison with Sessions 1-3
- **Reload Mode**: Reload Anytime (no reloading during run)
- **Scenario**: Crashlanded
- **Run length**: 10 full days after Day 1 (ends at daysPassed=11)

## Colonists
| Name | Age | Gender | Top Skills | Traits | Incapable Of | Role |
|------|-----|--------|------------|--------|--------------|------|
| Taten 'Tater' Stamm | 22 | M | Shooting 13, Social 9, Melee 6 | Slothful, Tough | None | Shooter/Fighter |
| Bran 'Sawyher' Shawb | 47 | M | Mining 10, Animals 8, Construction 5, Shooting 5 | Psychically dull, Delicate | Social | Builder/Miner |
| Baran Gargatosh | 38 | M | Medical 9, Melee 5, Shooting 4, Construction 4, Plants 4 | Fast learner, Nimble | None | Medic/Builder |

## Day 0 Accomplishments
- [x] Unforbid all 30 starting items
- [x] Set work priorities for all 3
- [x] Built 7x7 wooden shelter with door at (155,140)-(161,146)
- [x] Placed 3 beds, table, stove (outside), research bench (outside), horseshoes pin (outside)
- [x] Stockpile zones: interior (156-159,143-143) + exterior (139-143,146-150)
- [x] Growing zones: potato + rice (exterior, 111 cells)
- [x] Equipped: Taten=rifle+flak vest, Bran=revolver+flak helmet, Baran=knife+flak pants
- [x] Set research to Smithing
- [x] All colonists healthy (100 HP), moods 58-74

## Day 1-2 (1st-2nd Aprimay)
- Colonists hauling, sowing rice/potato fields, researching Smithing
- No raids yet (first raid window unknown)
- Moods: Bran 50-66, Taten 55-69, Baran 63-78
- Resources: 500 silver, 150 steel, 30 components, 32 medicine
- Alerts: Need colonist beds, Pen needed, 1 colonist idle, Need research bench
- Ancient danger letter: "As Sawyher draws near the ancient wall, a sense of foreboding" — marked and avoided

## Final State (Day 2, Hour 18, paused)
- **Colonists**: 3 alive, all 100 HP
- **Moods**: Bran 66, Taten 69, Baran 73
- **Resources**: 500 silver, 150 steel, 30 components, 32 medicine (no food in stockpile yet)
- **Research**: Smithing 0%
- **Alerts**: Need colonist beds, Pen needed, 1 colonist idle
- **Buildings**: 7x7 shelter, 3 beds (blueprint), table, stove (blueprint), research bench (blueprint outside), horseshoes pin (outside), 2 stockpiles, potato + rice growing zones

## Outcome
Session ended by user on Day 2. No deaths. No raids yet. Colony stable but items still deteriorating outside (steel/wood on ground). Research bench and stove are blueprints (0% built).

## Key Lessons
1. **Colonist selection**: Must have 2 shooters (5+ shooting) and 1 melee (5+). No colonist without fighting skills. All 4 critical skills (construction, plants, medical, intellectual) must be covered. Reroll until good combo.
2. **Research bench placement**: Placed outside shelter — "Need research bench" alert. Interior placement conflicts with bed interaction spots. Plan layout.
3. **Ancient danger**: Letter appeared Day 1. Mark and avoid. Can be useful later.
4. **Items deteriorating outside**: Starting gear on ground. Need stockpile zones near landing site.
5. **Pen needed**: Animal pen alert. Need to set up pen for animals.
6. **Colonist beds**: "Need colonist beds" alert. Beds are blueprints, not built yet.
7. **Single room issue**: Packed everything into 7x7 again. Need separate rooms per wiki (Room_roles).
8. **Reroll pool**: 100 rerolls may not find perfect team. Accept good-enough combo.

## Session Notes
- Monitor running with RUN_ID=run-001, 30s poll interval
- No game freeze (rate limiting + reduced poll frequency worked)
- Naming dialog appeared and was closed
- "A wait is already in progress" from stuck wait_for_event; used real-time sleep
- Game crashed once during a wide scan (4900 inspect_thing calls) — recovered
- New alert: "Ancient danger" letter (Bran drew near ancient wall)
