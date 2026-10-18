# Session 2 — 2026-10-02

## Game Setup (same parameters as Session 1)

- **Scenario**: Crashlanded
- **Storyteller**: Cassandra Classic
- **Difficulty**: Adventure Story (Medium)
- **Reload Mode**: Reload Anytime
- **Ideoligion**: Neo-Womanism (fluid, Female supremacy meme — generated defaults accepted)
- **World Tile**: 17 — Temperate Forest, Flat, 12.3°C, Rainfall 857 (Session 1: Tile 9, 12.6°C, 893)
- **Colony Name**: New Arrivals
- **Start Date**: 6th of Septober, 5500 (Spring), Hour 6, 4°C, Clear

## Colonists (new team — Session 1 characters not reusable)

| Name | Age | Gender | Top Skills | Traits | Incapable Of | Role |
| ------ | ----- | -------- | ------------ | -------- | -------------- | ------ |
| Noah Watkins | 58 | M | Medicine 9, Construction 7, Shooting 4 | Misandrist | Intellectual, Cooking | Builder/Doctor |
| Shinua 'Shin' Asahi | 38 | F | Animals 10, Shooting 8, Medicine 7, Int 6 | Annoying voice, Careful shooter | — | Fighter/Researcher |
| Aenne 'Peachy' Schumann | 42 | F | Plants 8, Cooking 7, Crafting 4 | Tough, Slowpoke, Abrasive | Violent | Grower/Cook |

### Team vs Session 1 (lessons applied)

- All 3 can haul/clean (Session 1's Jenni couldn't)
- No pyromaniacs, no children, no smokeleaf dependence
- Medicine 9+7 covered from day 1 (Session 1 died with no medicine)
- Both shooters capable (Noah 4, Shin 8 careful shooter); Peachy can't fight — keep her behind cover
- Noah (58) is misandrist but he's the only man — no social friction expected

## Day 0 Status

- **Game saved**: "Session2-Start"
- **State**: Paused, no threats (danger rating None)
- **Alerts**: Need warm clothes (high), Need colonist beds (high)
- **Map**: 250x250, flat, open ground with scattered rock formations
  - Mountain cluster NW of center (mineable)
  - Ancient-danger-style ruin structure (## with door) near center-east at ~x140-155, z~150
  - Water/marsh patches center-west and SE
  - No steam geysers spotted in coarse scan (recheck at full res)
- **Starting gear**: Crashlanded package (weapons, packaged meals, steel, wood, medicine) — needs unforbid

## Day 0 Priorities (from AGENT.md checklist)

1. Unforbid all starting resources
2. Survey map at full resolution (geysers, rich soil)
3. Build shelter (5x5+ room, walls, door)
4. Stockpile zone inside shelter
5. 3 beds, table + chairs
6. Growing zone — rice (40-60 tiles)
7. Set work priorities manually
8. Chop wood as needed

## Role Assignments (planned)

- Noah: Construction 1, Medical 1, Firefighting
- Peachy: Growing 1, Cooking 1, Plants Cut
- Shin: Research, Hunting, Handling, Shooting combat lead

## Session Notes

- MCP: port 8787, connected
- `select_scenario`/`select_storyteller` need explicit `name`/`storyteller` params (no defaults)
- World gen takes ~60-90s (poll `game_setup_status`)
- Ideoligion guided flow: `edit_ideoligion(action='next_step')` x13 then `finalize`
- `edit_starting_pawn` pool has 8 pawns; swap via `action='reorder', index, to` (first 3 slots = starting)
- Intro dialog: `window_action(index=0, option="OK")` (option is a label string, not index)
- `set_work_priority`: manual priorities must be ON first — setting any priority >1 auto-enables `manualPrioritiesEnabled`
- WorkType defNames: Firefighter, Patient, Doctor, Research, Construction, Mining, Growing, Cooking, Crafting, Hauling, Cleaning, Handling, Hunting, Art, Warden (NOT "Firefighting"/"Haul"/"BedRest" — Bed Rest appears unsettable)
- Build defNames: DiningChair (not Chair), SimpleResearchBench, FueledStove, HorseshoesPin, Table1x2c
- Stockpile gotcha: 6-cell zone hit 100% full → entire colony went idle/wandering. Always make stockpiles big (49-cell exterior added)
- `draft` takes `ids` (comma-separated ThingIDs) not `names`
- RimWorld superfast speed = huge real-time skips (60s ≈ 2 in-game days); use Speed 1-2 for controlled play

## Day 1-2 Events (9th Septober, 5500)

### Day 1

- [x] House completed — 8x8 walls, door, 3 beds, table + 3 chairs (0 blueprints left)
- [x] Rice growing zone sown (56 cells)
- [x] Loot hauled: wood 252, steel 450, silver 800, components 30, medicine 30, meals 27
- Stockpile jam fixed (added 49-cell exterior stockpile east of house)
- Built: fueled stove (106,136), simple research bench (113,137), horseshoes pin (120,133)
- Research started: Smithing (700)

### Day 2

- Mad rat event: rat got INSIDE house, bit Peachy 8x (dropped to 83% HP)
- Noah + Shin drafted, auto-attack AI killed rat; Noah tended Peachy → fully healed
- **Shin tamed warg "Chili"** (male,9, bonded to Shin; Tameness + Obedience trained)
- Cooking bill: 10 simple meals on fueled stove (need raw food — hunt or harvest rice)
- Visitor Ella Karpov (Lonin defector) arrived to trade — likely departed
- Shin equipped: bolt-action rifle (good), flak vest, flak helmet, flak pants
- Noah: bolt-action rifle (normal); Peachy: revolver (she's incapable of violence though)
- Game saved: **Session2-Day2**

## Current Status (Day 2 evening)

- Colonists: all 100% HP, moods 64-75%
- Animal: Chili the warg (Shin's bonded pet)
- Alarms: Need meal source (raw food for cooking), Need defenses, idle colonists
- Priorities: hunt for food, sandbags before first raid (days 8-15 window = 3-6 days away)

## Day 3-7 Events (11th-13th Septober, 5500)

- Rice harvested (56 plants, 94%+ grown), 24-cell cotton zone planted (future cloth/sandbags)
- **Day 5 disaster**: timber wolf mauled Shin while she hunted the deer herd — eye bitten out, hand/arm bitten off, bones shattered → **Shin DIED** (her first wound-tending never happened; wolf was 1-cell from her)
- Same day: Filth Faction raid (3 wasters: Gator, Masahiro, Foozie) — all three ended up dead on the map (Gator killed at the rice field, others NW); megasloth revenge event; Chili the warg went berserk (still berserk at session end, parked ~17 cells south of base)
- Peachy got food poisoning (dirty cooking area) — vomited for a day, mood crashed to 20 (major break risk); Noah grief-stricken to 20, cloudwatched
- Shin's corpse hauled 200 cells from far SE corner to a grave west of the house; graves: #1 Gator, #2 Masahiro (old 5498 corpse), #3 Shin
- **Burial of Womanism funeral started** for Shin (gizmo on Grave45009) just before session end
- Psychic soothe (Female) lifted moods: Peachy 66%, Noah 43% at end
- Research: Smithing reached 21% (researcher Shin died — now stalled)
- Resources end of session: 15 packaged meals, 6 simple meals, 58 rice, 800 silver, 345 steel, 112 wood, 29 medicine, 30 components
- Collected Shin's gear via strip: flak vest/pants/helmet + rifle in/near stockpile

## Tool gotchas learned (Day 3-7)

- `set_speed` takes ONLY action=pause|unpause (numeric speed param silently ignored — resumes at last selected speed, usually Superfast). `Resume-Game -Speed 1` does NOT limit speed
- To advance time safely use `wait_for_event` with maxGameHours + pause="always" (1-game-hour crisis cap when hostiles/life-threatening conditions exist)
- `draft` needs `action="draft"` + ids (ThingIDs)
- `order_pawn` params: `id` (pawn ThingID) + `targetId` + `command` (exact label); lists options first when command omitted
- `do_thing_action` executes inspect_thing actions via `label` param (used for ritual gizmos)
- Corpses: defName="Corpse_Human" (not "Corpse"); graves auto-accept nearest unburied corpse — build a spare grave or wrong corpses fill it
- `set_schedule` with no hours = whole day assignment (accidentally slept everyone); re-set all 24 hours to fix
- DefName list: Grave, Sandbags (cloth-only stuff), TrapSpike, Plant_Cotton

## Session End (Day 7, 13th Septober 20h)

- Game quit before final manual save — **last manual save: Session2-Day2** (Day 2); **latest autosave: Autosave-3** (2:36 PM, ~Day 7 state with funeral just begun)
- Remaining colonists: Noah (mood 43), Peachy (66); animal: Chili (berserk); graves: 3 (Shin buried); no active raiders
- Next session: check funeral completed, snap Chili out of berserk (draft + down), resume Smithing research, defense line (sandbags need cotton cloth — planted), freezer/cooler still missing
