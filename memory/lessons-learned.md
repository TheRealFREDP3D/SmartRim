# Lessons Learned

## Mistakes to Avoid

### Critical Mistakes (Caused Colony Death)

1. **No herbal medicine** — colonists died from injuries no one could treat
   - Fix: Harvest wild healroot on Day 1-2; plant healroot growing zone (needs Growing skill 8+)
   - Fix: Start with 30 medicine (Crashlanded scenario) — preserve it, don't waste on bruises
   - Fix: Build drug lab early to craft medicine from healroot + cloth + neutroamine

2. **Not building medical bed** — downed colonists can't heal
   - Fix: Build 1-2 beds designated as medical early (Bed → toggle to medical)
   - Fix: Assign doctor work type to best medicine pawn

3. **Ignoring animal threats** — guinea pig killed Vlad; timber wolf killed Shin (Session 2)
   - Fix: Check wildlife tab for predators; draft colonists if dangerous animals near
   - Fix: Do NOT hunt predators; avoid or fight only with a fighter escort + medic nearby
   - Fix: Build walls around growing zones and work areas

4. **Not burying corpses** — -10 mood debuff per corpse
   - Fix: Designate dumping stockpile for corpses, or butcher them
   - Fix: Set hauling priority high for corpse removal

5. **Roni mental break spiral** — lover death triggered mood collapse
   - Fix: Monitor colonist relationships; watch for grief debuffs
   - Fix: Have recreation and food ready during crises

6. **Hunter killed by predator** — Shin was mauled to death by a timber wolf while hunting the deer herd (Session 2, Day 5)
    - Fix: Before hunting, check wildlife tab for predators near the hunting ground
    - Fix: Never hunt alone at the map edge — draft a fighter escort or keep the bonded animal released nearby
    - Fix: Pause and watch when a hunt starts; a downed hunter at 9% HP is unrecoverable if unattended
    - Fix: The same superfast-speed time jump that hid the attack also hid the raid — see MCP gotchas

### Important Mistakes (Caused Mood Problems)

7. **No freezer early** — food rots, colonists eat raw food
   - Fix: Build 7x7 freezer room by Day 4-7, set cooler to -5°C
   - Fix: Place near kitchen for short hauling routes

8. **Eating without table** — -3 mood debuff
   - Fix: Place table + chairs in shelter on Day 1

9. **Sleeping outside/cold** — multiple mood debuffs
   - Fix: Build enclosed shelter with roof before nightfall

10. **No recreation variety** — mood stagnates
   - Fix: Build horseshoe pin Day 1; add chess table and TV later
   - Fix: 4 different recreation types prevent diminishing returns

11. **Cooking in dirty area** — food poisoning risk
    - Fix: Separate kitchen from workshop; floor the kitchen

## What Worked Well
- Building shelter and basic furniture on Day 0
- Using `say` tool for in-game AI messages
- Creating `mcp-helper.ps1` for natural language commands
- Research assignment worked immediately
- Walls built for defense
- Rice planted early (fast growth)
- Session 2: `wait_for_event` with game-hour limits — safe time advance with event/damage reporting
- Session 2: stripping corpses to recover gear; graves auto-haul corpses once built
- Session 2: 49-cell exterior stockpile (small zones jam to 100% and idle the whole colony)
- Session 2: bonded warg (Shin's Chili) — tame animals with high-Animals pawns for early defense

## What Didn't Work
- Not building medical beds — colonists died without treatment
- Not having herbal medicine — critical for early game
- Ignoring animal threats — guinea pig killed Vlad
- Not burying corpses promptly — mood debuff stack
- No freezer — food couldn't be preserved
- Only 1 growing zone — vulnerable to blight/weather
- Session 2: bare unpause at Superfast — wolf kill + raid happened unobserved; Shin died
- Session 2: outdoor stove on dirt (no floored kitchen) — Peachy's food poisoning crash to 20% mood
- Session 2: hunting the far map edge solo — Shin mauled with no one near to tend her
- Session 2: single small stockpile — colony went idle wandering (recurring; fixed with big zone)

## Next Colony Plan

### Day 0 (Pause Immediately)
1. Unforbid all starting items
2. Draft colonists, equip weapons
3. Find base location near: ruins, rich soil, geysers
4. Build small shelter (7x7) with door
5. Place stockpile zone inside
6. Build 3 beds (1 per colonist)
7. Place table + chairs
8. Build horseshoe pin

### Day 1
1. Build fueled stove + cook simple meal bill
2. Build research bench
3. Plant rice (40-60 tiles) on rich soil
4. Harvest wild healroot (if available)
5. Chop wood for materials
6. Set work priorities: Cook, Grow, Research, Construct, Hunt

### Day 2-3
1. Build butcher table + butcher forever bill
2. Build cooler room (7x7) at -5°C
3. Hunt easy animals (rabbits, deer — NOT predators)
4. Build sandbag cover near base entrance
5. Research Smithing (gateway to weapons)

### Day 4-7
1. Build freezer and stockpile food inside
2. Build medical beds (2-3)
3. Build walls around base perimeter
4. Craft weapons after Smithing research
5. Plant healroot growing zone (needs Growing 8+)
6. Build drug lab for medicine crafting

### Day 8-15 (First Raid Window)
1. All colonists armed with weapons
2. Sandbag line with cover positions
3. Focus-fire one enemy at a time
4. Draft non-combatants to safe zone
5. Treat wounded immediately after fight
6. Bury/haul all corpses

### Day 16-30
1. Individual bedrooms (3x3 each)
2. Separate kitchen (floored, clean)
3. Recreation room with variety
4. Power: solar panels + batteries
5. Start trading for medicine components

## Research Priority Order
1. Smithing (weapons) — Day 2-3
2. Batteries (power storage) — Day 4-5
3. Solar Panels (reliable power) — Day 5-7
4. Microelectronics (advanced research) — Day 10+
5. Machining (turrets, better weapons) — Day 15+

## Medicine Strategy
- Day 1: Harvest wild healroot (60% potency)
- Day 2: Plant healroot growing zone
- Day 3: Build drug lab
- Day 5+: Craft herbal medicine from healroot + cloth
- Buy standard medicine from traders when possible
- Restrict colonists to herbal medicine for minor injuries

## Defense Strategy
- Build killbox with single entrance
- Sandbags inside corridor
- Shooters behind cover
- Focus-fire one enemy at a time
- Retreat to medical area after fight
- Loot weapons from fallen raiders

## Experiment Log
### 2026-09-17 — Session 1
- **Colony**: Koberon (Crashlanded, Cassandra Classic, Adventure Story)
- **Result**: Colony collapse Day 5, recovered to 1 colonist by Day 9
- **Root cause**: Guinea pig attack → Vlad death → Roni mental break → death
- **Key lesson**: Animals can be lethal early game; always have medical supplies
- **MCP tool**: Created `mcp-helper.ps1` for natural language interaction
- **Research**: Compiled beginner guides for Day 1-30 survival strategy

### 2026-10-02 — Session 2
- **Colony**: New Arrivals (same seed settings, Neo-Womanism ideoligion; Noah/Shin/Peachy)
- **Result**: 3 → 2 colonists. Day 5: Shin killed by timber wolf while hunting. Day 7: burial started as session ended; game quit before final manual save
- **Raid**: Filth Faction (3 wasters) — all dead without us fighting them (megasloth/predators killed them); megasloth revenge + berserk warg on the same day
- **Root cause of death**: time advanced at Superfast while I was doing MCP calls → wolf attack and raid happened unobserved; hunter was alone at map edge
- **Mood crisis handled**: food poisoning (dirty outdoor kitchen) + grief dropped Peachy/Noah to 20%; recovered via sleep, psychic soothe, and Shin's burial ritual
- **Key lessons**:
  - Predators + hunting = death; always watch hunts start (mirrors Session 1 guinea pig lesson)
  - Graves auto-accept the NEAREST corpse — wrong corpses (Masahiro) fill your colonist's grave; build a spare grave first
  - Strip a colonist corpse immediately to recover their gear (Shin's flak + rifle recovered)
  - Unburied colonist corpse + dirty kitchen + grief stack fast into break risk — bury own colonists before strangers
  - Autosave rotation (Autosave-1/2/3) is the safety net when manual save fails — check the Saves folder

### 2026-10-03 — Session 3
- **Colony**: New Arrivals (same seed params as Session 1, Classic ideoligion, tile 203)
- **Result**: Day 3 paused/saved; Nilz + Sammy downed by a wild sparrow inside base; Larian tending Nilz; DangerRating High; pirate raid alert active
- **Crisis**: nilz extreme blood loss + Sammy moderate blood loss + Larian sparrow bites; no active doctor except Larian
- **Key lessons**:
  - Wildlife can break into the base — watch "DangerRating: High" and threat warnings
  - Downed but tended patients sleep in bed; check blood loss severity via get_pawn tab=health
  - Rescue works with exact "Rescue" command after drafting the rescuer
  - `add_bill` needs the thing id (e.g. FueledStove28981), not a def name only
  - `order_pawn` command list is specific ("Fire at sparrow", not "Auto attack (AI)" in that context)
- 2x/day colony summaries posted in-game via `say` (background pwsh loop, triggered at hours 6/18)

### 2026-10-18 — Session 5 (Northwest Asora Covenant)
- **Colony**: Northwest Asora Covenant (Lajitas, tile 35, temperate forest, flat, 9.2°C)
- **Difficulty**: Community Builder (Easy) — Phoebe Chillax (confounds comparison with Adventure Story / Cassandra baseline)
- **Result**: Day 7, all 3 alive. First raid survived (Pollution Unit, 1 raider). Tyren wounded (80→100 HP). Game crashed/quit on Day 7.
- **Key lessons**:
  - Food: 50 starting meals lasted 6-7 days; rice harvest started Day 6 (197-cell field). Low food alert Day 6. Fix: cook from rice as soon as harvest begins; plant smaller faster field earlier
  - Defense: "Need defenses" alert persisted all 7 days — no cloth for sandbags. Fix: plant cotton on Day 1
  - Tyren (psychopath) took knife wounds in melee (80 HP). Fix: keep fighters at range; melee only as last resort
  - Shared barracks + no recreation → moods 40-77. Fix: individual bedrooms, horseshoes pin (helped, +5-10 mood)
  - Henry (misogynist) + Chaz (female) → social friction, mood 48-57. Monitor or separate
  - Medical bed: setting a bed to medical helped Tyren heal. Do this early
  - Research bench placement conflicts with bed interaction spots. Plan interior layout
  - Idle colonist (Chaz) when research bench occupied. Give secondary work (haul/clean/construct)
  - First raid (Day 5): single raider, 3 armed colonists handled it. Draft all, focus fire, tend wounds after
  - Naming dialog (faction/settlement) appears repeatedly; close with window_action close
  - "A wait is already in progress" from stuck wait_for_event; use real-time sleep instead

### 2026-10-18 — Session 4 (Doder Coalition, in progress)
- **Colony**: Doder Coalition (Hypnotist's Inlet, tile 4, temperate forest, flat, 16.6C)
- **Difficulty**: Community Builder (Easy) — Phoebe Chillax (confounds comparison with Adventure Story / Cassandra baseline)
- **Result (so far)**: Day 9+, all 3 colonists alive and healthy; low food alert on Day 8 (3 days remaining)
- **Key lessons**:
  - Food: rice field too small / cooking inconsistent → low food by Day 8. Fix: plant 40-60 tiles rice on Day 1, cook simple meals steadily, keep >=2 weeks of food
  - Construction: "Need defenses" alert persisted Days 3-6; 13 wall blueprints sat unbuilt for 3+ days (RimMolt message). Fix: assign Construction priority 1 to a capable pawn early; verify blueprints actually get built
  - Medical: "Medical treatment needed" on Day 6 despite 30 medicine — injuries happen even on easy. Fix: keep doctor assigned, medicine stocked, medical bed ready
  - Research: "Need research project" Days 4-5 — bench placement/assignment issue. Fix: place research bench indoors with light; assign a dedicated researcher

## MCP Tool Gotchas (Session 2 — CRITICAL)

### Work Type Names
- Empirically valid names (Session 2): `Firefighter` (not Firefighting), `Patient`, `Doctor`, `Research`, `Construction`, `Mining`, `Growing`, `Cooking`, `Crafting`, `Hauling` (not Haul), `Cleaning`, `Handling`, `Hunting`, `Art`, `Warden`
- `Bed Rest` appears unsettable via MCP; `Basic` unverified; `PlantCutting` unverified
- Colonists may be incapable of certain work types (e.g., "incapable of Dumb labor" → can't haul or clean)
- Names vary by RimWorld build — re-run `scratchpad/check_worktypes3.py` against a live colony to confirm
1. **`set_speed` takes only `action=pause|unpause`** — numeric `speed` param is silently ignored; unpause resumes at the LAST selected speed (usually Superfast). `Resume-Game -Speed 1` does NOT slow anything down
2. **Never advance time with bare unpause** — use `wait_for_event` with `maxGameHours` + `pause="always"`; it has a 1-game-hour crisis cap when hostiles/fire/life-threatening conditions exist, and returns letters/damage deltas
3. **`draft`** requires `action="draft"` + `ids` (comma-separated ThingIDs, not names)
4. **`order_pawn`** params are `id` (pawn ThingID) + `targetId`; omit `command` first to list options, then execute with the exact label (e.g. `Auto attack (AI): rat`)
5. **`do_thing_action`** runs inspect_thing gizmos via `label` (e.g. funeral ritual button on a grave)
6. **`set_schedule` with no hours sets the WHOLE day** — always pass explicit `hourStart`/`hourEnd`/`hours`
7. **Corpse search**: `defName="Corpse_Human"`; `category="corpse"` is wrong (returns rocks)
8. **Designator names differ**: `Designator_ZoneAdd_Growing` (with underscore), `Designator_PlantsHarvestWood`, `Designator_PlantsHarvest`, `Designator_Hunt`, `Designator_Cancel` — wrong name returns "Unknown designator" with a hint to use list_architect
9. **Sandbags stuff=Cloth only** — no cloth in stock means a stalled blueprint; plant cotton early or test stuff options before placing
10. **`save_game` can return `saved=False`** (window open / game shutting down) — verify, and know autosave names `Autosave-N.rws` in `%USERPROFILE%\AppData\LocalLow\Ludeon Studios\RimWorld by Ludeon Studios\Saves`
