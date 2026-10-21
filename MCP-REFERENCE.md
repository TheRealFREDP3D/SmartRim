# RimWorld MCP Project

## Project goal (reoriented)

The end goal is a system that **auto-plays RimWorld**. The human is a spectator who can intervene at any time: give orders, change parameters, pause/resume, or override decisions. The advisor-only stance from earlier phases is a stepping stone, not the destination.


## Overview

This project uses a Model Context Protocol (MCP) server running inside RimWorld to allow LLMs to observe and interact with a live game session. The MCP server is embedded in the RimWorld process and exposes game state, issues orders, and manages colonists via JSON-RPC over HTTP.

## Quick Start

Load the helper at the start of each session:

```powershell
. C:\Users\fred\Desktop\RimWorld Consellor\SmartRim\mcp-helper.ps1
```

Then use natural commands:

```powershell
Get-GameStatus          # See colony status
Get-Conditions          # Date, weather, temperature
Get-ColonistNeeds "Roni" # Check colonist mood/needs
Pause-Game              # Pause the game
Resume-Game             # Resume (speed controlled in-game; use Wait-Days for safe advance)
Build-Thing "Bed" 106 86 # Build a bed at coordinates
New-GrowingZone 112 82 120 87 # Create rice field
Set-Research "Smithing" # Start research
Say-Message "Hello!"   # Send message to AI window
New-DailySummary        # Generate daily summary
```

## MCP Server

- **Host**: `localhost`
- **Port**: `8787`
- **Protocol**: JSON-RPC 2.0 over HTTP POST
- **Process**: `RimWorldWin64` (PID varies per session)

### Initialize Connection

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "initialize",
  "params": {
    "protocolVersion": "2024-11-05",
    "capabilities": {},
    "clientInfo": {"name": "opencode", "version": "1.0.0"}
  }
}
```

### List Available Tools

```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "method": "tools/list",
  "params": {}
}
```

### Call a Tool

```json
{
  "jsonrpc": "2.0",
  "id": 3,
  "method": "tools/call",
  "params": {
    "name": "<tool_name>",
    "arguments": { ... }
  }
}
```

## Tool Categories

### Status & Observation

| Tool | Description |
| ------ | ------------- |
| `get_status` | Overall game status (tick, speed, maps, colonists). Call first. Bundles other read-only tools. |
| `get_map` | ASCII terrain summary of a map. Call after colony loads. |
| `list_colonists` | All colonists with health, mood, jobs, skills. |
| `get_pawn` | Detailed info on any pawn (colonist, raider, visitor). |
| `get_resources` | Stockpiled resources and colony wealth. |
| `get_resource_readout` | Full item readout from the corner HUD. |
| `get_research` | Current research project(s) and progress. |
| `get_alerts` | Active threats, warnings, danger ratings. |
| `read_letter` | Read full text of an in-game letter. |
| `get_conditions` | Map conditions (date, season, weather, temperature). |
| `get_room` | Evaluate a room (role, temperature, impressiveness). |
| `inspect_thing` | Select a thing and return its info + available actions. |
| `get_info_card` | Detailed stat list for a thing. |
| `get_inspect_pane` | Bottom-left inspect pane contents. |
| `screenshot` | Capture game window to PNG file. |

### Spatial & Map

| Tool | Description |
| ------ | ------------- |
| `get_area` | Spatial layout, terrain, base structure (recommended over read_area). |
| `list_things` | List spawned things by category/faction. |
| `list_unmanaged_items` | Forbidden items needing attention. |
| `list_fires` | All fires on a map. |
| `list_power_grids` | Power grid status, unpowered devices. |
| `room_graph` | Base room connectivity check. |
| `list_zones` | All zones (stockpile, growing). |
| `list_wildlife` | Wild animals on a map. |
| `list_animals` | Colony animals across maps. |

### Orders & Actions

| Tool | Description |
| ------ | ------------- |
| `order_pawn` | Right-click order (go, haul, attack, etc.). |
| `draft` | Draft/undraft colonists in bulk. |
| `designate` | Apply designators (cut, mine, hunt, harvest, deconstruct). |
| `build` | Place building or floor. |
| `do_thing_action` | Execute a gizmo action on a thing. |
| `set_speed` | Pause or unpause game. |
| `wait_for_event` | Advance time until something notable happens. |

### Colony Management

| Tool | Description |
| ------ | ------------- |
| `set_work_priority` | Set colonist work tab priorities. |
| `manage_gear` | Manage colonist gear/loadout. |
| `set_schedule` | Read or set colonist timetable. |
| `set_outfit` | Set apparel policy. |
| `set_drug_policy` | Set drug policy. |
| `set_food_policy` | Set food policy. |
| `set_hostility_response` | Set Attack/Flee/Ignore response. |
| `set_allowed_area` | Restrict colonist to area. |
| `set_medical_care` | Set medical care level. |
| `assign_building` | Assign pawn to bed, throne, grave, etc. |
| `rename_pawn` | Rename a colonist. |
| `manage_prisoner` | Set prisoner treatment/recruitment. |

### Areas & Zones

| Tool | Description |
| ------ | ------------- |
| `manage_area` | Create/edit map areas. |
| `manage_apparel_policy` | Manage apparel policy contents. |
| `manage_food_policy` | Edit food policy contents. |
| `manage_drug_policy` | Edit drug policy contents. |
| `select_zone` | Select zone in live UI. |
| `rename_zone` | Rename a zone. |
| `delete_zone` | Delete a zone. |
| `set_growing_zone` | Configure growing zone plant. |
| `set_stockpile_priority` | Set stockpile priority. |
| `set_stockpile_filter` | Edit stockpile item filter. |

### Production

| Tool | Description |
| ------ | ------------- |
| `list_recipes` | Recipes a work table can make. |
| `list_bills` | Bills on a work table. |
| `add_bill` | Add production bill. |
| `set_bill` | Edit a bill. |
| `delete_bill` | Remove a bill. |

### World & Travel

| Tool | Description |
| ------ | ------------- |
| `get_world` | Factions, goodwill, active quests. |
| `list_world_objects` | World map objects (settlements, etc.). |
| `get_world_tile` | Inspect a world tile. |
| `caravan_action` | Control your caravans. |
| `world_target` | Select destination for transport pods. |
| `find_world_tiles` | Scan world map for matching tiles. |
| `form_caravan` | Form caravan via in-game dialog. |
| `world_object_action` | Operate world object gizmos. |

### Trade

| Tool | Description |
| ------ | ------------- |
| `list_trade` | Current trade deal items. |
| `set_trade` | Set trade quantities. |
| `trade_action` | Accept or reset trade. |

### Quests

| Tool | Description |
|------|-------------|
| `get_quest` | Quest details. |
| `quest_action` | Accept/abandon quest. |

### Surgery

| Tool | Description |
|------|-------------|
| `list_surgeries` | Available operations on a pawn. |
| `add_surgery` | Queue a surgery. |

### Ideology

| Tool | Description |
| ------ | ------------- |
| `set_ideo_role` | Assign/remove ideoligion roles. |
| `choose_ideoligion` | Pick ideoligion creation mode (new game). |
| `edit_ideoligion` | Customize custom ideoligion. |
| `reform_ideoligion` | Reform fluid ideoligion in running colony. |

### Royalty DLC

| Tool | Description |
| ------ | ------------- |
| `get_royalty` | Royal titles and honor. |
| `list_titles` | Title track for a faction. |
| `manage_permits` | Royal permits screen. |
| `use_permit` | Use a royal permit ability. |

### Biotech DLC

| Tool | Description |
| ------ | ------------- |
| `list_genes` | Xenotypes and gene summaries. |
| `create_xenogerm` | Assemble xenogerm from genepacks. |
| `implant_xenogerm` | Order xenogerm implantation. |
| `list_mechs` | Mechanitors and mechanoids. |
| `set_mech_control` | Manage mechanitor's mechanoids. |

### Anomaly DLC

| Tool | Description |
| ------ | ------------- |
| `get_anomaly` | Void monolith status. |
| `entity_codex` | Bestiary of anomalous entities. |
| `list_study_targets` | Studyable entities for knowledge. |
| `set_study` | Enable/disable study on a target. |

### Game Flow

| Tool | Description |
| ------ | ------------- |
| `game_setup_status` | Where in new-game flow. |
| `main_menu` | Main menu actions (new colony, etc.). |
| `save_game` | Save current game. |
| `load_game` | Load a saved game. |
| `return_to_title` | Quit to main menu. |
| `select_scenario` | Pick scenario. |
| `select_storyteller` | Choose storyteller + difficulty. |
| `create_world` | Generate planet. |
| `select_starting_site` | Choose colony tile. |
| `start_game` | Finalize character creation, start game. |
| `edit_starting_pawn` | Adjust starting colonists. |

### UI & Communication

| Tool | Description |
| ------ | ------------- |
| `list_main_buttons` | Bottom button row. |
| `list_architect` | Architect menu categories/items. |
| `list_windows` | Open pop-up windows/dialogs. |
| `get_window_ui` | Modal window contents. |
| `window_action` | Respond to a pop-up. |
| `learning_helper` | Learning helper topics. |
| `list_policies` | Assignable policies. |
| `say` | Display text to the human watching. |
| `get_live_chat` | YouTube live chat comments (experimental). |

### Setup

| Tool | Description |
|------|-------------|
| `help` | Discover all tools with summaries. |
| `bundle_add` / `bundle_remove` / `bundle_set` | Configure get_status bundle. |

## Beginner Strategy Notes

Sources: earlyguides.com, jeu.video, roguewiki.com, rimworldwiki.com

### Recommended Setup

- **Scenario**: Crashlanded (3 colonists, balanced start)
- **Storyteller**: Cassandra Classic (predictable escalation)
- **Difficulty**: Medium / Adventure Story (reload any mode OK)
- **Biome**: Temperate Forest (long growing season, wood, fertile soil)

### Day 1 Checklist

1. Pause immediately — survey map (geysers, fertile soil, mountains)
2. Build shelter — enclosed room with walls and door
3. Stockpile zone — inside shelter, priority Important
4. Plant rice — fastest crop, 40-60 tiles for 3 pawns
5. Build beds — one per colonist (no sleeping on ground)
6. Table + chairs — eating without table = mood debuff
7. Torch lamp — mood + work speed in darkness

### Colonist Role Assignment (manual work priorities)

| Role | Priority 1 | Priority 2 |
| ------ | ----------- | ----------- |
| Cook | Cooking | — |
| Builder/Grower | Construction, Growing | Plants |
| Researcher | Research | Crafting |

### Critical Rules

- **Pause often** — spacebar is free
- **Freeze food** — cooler at -5°C to -10°C
- **Bury/butcher bodies** — corpses tank mood
- **Sandbags before first raid** — days 8-15 window
- **Don't hoard** — wealth scales raid difficulty
- **No pyromaniacs** — they burn bases down
- **Rice first** — fastest food crop
- **Cook meals** — raw food = mood penalty

### First 30 Days Plan

| Days | Focus |
| ------ | ------- |
| 1-3 | Shelter, stockpile, plant rice, beds, table |
| 4-7 | Cook meals, build freezer, wind turbine, sandbags |
| 8-15 | Survive first raid (draft, focus-fire, cover) |
| 16-30 | Kitchen, bedrooms, recreation, work priorities |

### Combat Basics

- Draft colonists during raids
- Focus-fire one enemy at a time (don't split fire)
- Use sandbags/cover — standing in open = suicide
- After raid: tend wounds, haul bodies, strip weapons from raiders

### Mood Management

- Cooked meals, private bedrooms, recreation variety
- Check Needs tab often (hunger, tiredness, pain, dirt, darkness)
- Avoid shared barracks long-term
- Haul/bury corpses promptly

## Session Log

<!-- Append session logs below this line -->

### Session 1 — 2026-09-17

- MCP server connected on port 8787 (PID 10300, RimWorldWin64)
- Game state: Main menu (`programState: "Entry"`)
- No colony loaded
- Available tools enumerated: 80+ tools across all DLC categories
- Created AGENT.md for project documentation
- Researched beginner guides (earlyguides.com, jeu.video, roguewiki.com, rimworldwiki.com)
- Compiled beginner strategy notes into AGENT.md

### Session 2 — 2026-10-02

- Started new colony "Session2-Start" — same params as Session 1 (Crashlanded, Cassandra, Adventure Story, Reload Anytime, Temperate Forest)
- New world, Tile 17 (flat, 12.3°C, rainfall 857); ideoligion "Neo-Womanism" (fluid, generated defaults)
- New colonist team: Noah Watkins (builder/doctor), Shinua 'Shin' Asahi (fighter/researcher), Aenne 'Peachy' Schumann (grower/cook)
- Full log: memory/session-logs/session-2.md

### Session 3 — 2026-10-03
- New colony "Session3-Day3" (Classic ideoligion, world tile 203, Temperate Forest, Permanent Summer)
- Colonists: Larian Lorall, Nils 'Nilz' Martens, Sammy 'Sunshine' Mitchell
- Paused/saved Day 3 (~Hour 15): Nilz + Sammy downed by wild sparrow inside base; Larian tending Nilz
- DangerRating: High; pirate raid alert active (first raid window Days 8-15)
- Full log: memory/session-logs/session-3.md
- Outcome: paused/saved; final outcome not recorded

### Session 4 — 2026-10-18 (in progress)
- Colony "Doder Coalition", map "Hypnotist's Inlet", Cassandra Classic, Community Builder difficulty
- Colonists: Zack Buckley, Freya 'Tail' Fairwing, Creedance 'Creed' Osgood (all healthy, Day 9 at last snapshot)
- Status at last snapshot (Day 9, Hour 0): Low food alert (3 days of food); Smithing 25%; 13 packaged meals; Ambrosia sprout + Mechanoid Signal quest active
- Monitor running; snapshots day-1..day-8 stored in memory/snapshots/
- No session log file yet

### Session 5 — 2026-10-18
- Colony "Northwest Asora Covenant" (Lajitas, tile 35, temperate forest, flat, 9.2°C)
- Storyteller: Phoebe Chillax | Difficulty: Community Builder | Reload Anytime
- Colonists: Chaz Targrin (researcher), Tyren Nordgren (fighter, psychopath), Henry 'Lawman' Jensen (shooter, misogynist)
- Result: Day 7, all 3 alive. First raid survived (Pollution Unit, 1 raider killed). Tyren wounded (80→100 HP). Game crashed/quit on Day 7.
- Buildings: 7x7 shelter, 4 beds (1 medical), table, stove, research bench, horseshoes pin, 2 stockpiles, 197-cell rice field
- Research: Smithing complete (Day 5), Batteries 42% (Day 7)
- Resources at end: 9 meals, 4 rice, 900 steel, 375 wood, 30 medicine
- Full log: memory/session-logs/session-5.md
