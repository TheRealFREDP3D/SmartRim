# Session 5 — 2026-10-18 (Northwest Asora Covenant)

## Game Setup
- **Colony**: Northwest Asora Covenant (settlement "Lajitas")
- **Tile**: 35 — Temperate Forest, Flat, 9.2°C, 826 rainfall, 0.16 swampiness
- **Storyteller**: Phoebe Chillax
- **Difficulty**: Community Builder (Easy)
- **Reload Mode**: Reload Anytime
- **Scenario**: Crashlanded

## Colonists
| Name | Age | Gender | Top Skills | Traits | Incapable Of | Role |
|------|-----|--------|------------|--------|--------------|------|
| Chaz Targrin | 35 | F | Intellectual 8, Construction 7, Crafting 6 | Delicate, Body purist | — | Researcher/Builder |
| Tyren Nordgren | 22 | M | Shooting 11, Melee 10, Artistic 9 | Psychopath, Nimble, Trigger-happy | Social, Animals | Fighter |
| Henry 'Lawman' Jensen | 28 | M | Social 11, Shooting 7, Animals 5 | Misogynist | — | Shooter/Grower |

## Day 0 Accomplishments
- [x] Unforbid all 35 starting items
- [x] Set work priorities (Chaz: research/build/craft; Tyren: fight/hunt/plant-cut; Henry: build/hunt/grow)
- [x] Built 7x7 wooden shelter with door at (135,116)-(141,122)
- [x] Placed 3 beds + 1 medical bed, table (1x2), stockpile zone (interior), horseshoes pin
- [x] Created 197-cell rice growing zone on rich soil (120-139, 100-109)
- [x] Equipped: Chaz=rifle, Tyren=knife, Henry=revolver
- [x] Set research to Smithing
- [x] Built fueled stove (outside) + cooking bill (10 simple meals)
- [x] Built simple research bench
- [x] Created exterior stockpile zone (130-134, 110-114)
- [x] Named faction "Northwest Asora Covenant", settlement "Lajitas"

## Day 1-5
- Chaz researched Smithing (completed Day 5)
- Henry sowed 197-cell rice field
- Tyren hauled steel/wood to stockpiles
- First raid: Pollution Unit (1 raider "Swamp"), Day 5. Drafted all 3. Tyren took knife wounds (80 HP). Raider killed. Tyren healed to 100 by Day 7.
- Moods fluctuated 40-77. Horseshoes pin built Day 4 helped.
- Research set to Batteries (42% by Day 7)

## Day 6-7
- Rice harvest began (Day 6). 4 rice harvested by Day 7.
- Food low: 9-10 packaged meals remaining. Low food alert active.
- Tyren fully healed (100 HP) by Day 7.
- Moods: Tyren 61, Henry 48, Chaz 68 (Day 7). Henry's mood low (misogynist + Chaz).
- No second raid. "Need defenses" alert persistent (no sandbags — no cloth).
- Medical bed set for Tyren (healed).

## Final State (Day 7, Hour 3, paused)
- **Colonists**: 3 alive, all 100 HP
- **Moods**: Tyren 61, Henry 48, Chaz 68
- **Resources**: 9 packaged meals, 4 rice, 900 steel, 375 wood, 30 medicine, 30 components, 800 silver
- **Research**: Batteries 42%
- **Alerts**: Low food, 1 colonist idle, Need defenses
- **Buildings**: 7x7 shelter, 4 beds (1 medical), table, stove, research bench, horseshoes pin, 2 stockpiles, 197-cell rice field

## Outcome
Colony ended (game quit/crashed) on Day 7. All colonists alive and healthy at end. First raid survived. Food was the emerging bottleneck (9 meals left). Moods were declining (especially Henry at 48). No deaths.

## Key Lessons
1. **Food timing**: 50 starting meals lasted ~6-7 days. Rice field (197 cells) took 5-6 days to sow; harvest started Day 6. Need to start cooking from rice as soon as harvest begins. Consider planting a smaller, faster field earlier.
2. **Sandbags need cloth**: No cloth available → no sandbags → "Need defenses" alert persisted. Plant cotton on Day 1.
3. **Tyren (psychopath) in melee**: Took knife wounds (80 HP) in close combat. Fix: keep fighters at range; use melee only as last resort.
4. **Shared barracks mood penalty**: All 3 in one room. Moods stayed 40-77. Individual bedrooms would help.
5. **Henry (misogynist) + Chaz (female)**: Social friction. Henry's mood 48-57. Monitor or separate.
6. **Medical bed**: Setting a bed to medical helped Tyren heal. Do this early.
7. **Research bench placement**: Inside shelter, conflicts with bed placement (interaction spots). Plan interior layout.
8. **Idle colonist**: Chaz idle when research bench occupied or work done. Give secondary work (haul/clean/construct).
9. **Rice harvest**: Colonists harvested rice starting Day 6. Need to process into meals quickly.
10. **First raid (Day 5)**: Single raider, handled by 3 armed colonists. Tyren took damage. Draft all, focus fire, tend wounds after.

## Session Notes
- Game frozen/crashed on Day 7. Colony state saved in autosaves.
- Monitor was not restarted for this colony (snapshots from previous Doder run).
- Used rate-limited API calls (0.15s delay) to avoid game freeze.
- Naming dialog (faction/settlement) appeared multiple times; closed with window_action close.
- "A wait is already in progress" error from stuck wait_for_event; used real-time sleep instead.
