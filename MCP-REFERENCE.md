# RimWorld MCP Tool Reference

This document provides a reference for the RimMolt MCP server tools available for interacting with RimWorld.

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
