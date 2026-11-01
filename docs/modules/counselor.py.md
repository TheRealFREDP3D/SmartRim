# counselor.py — High-Level MCP Tool Wrappers

Reusable tool library for game interaction via MCP. Thin wrappers around `McpClient.call_tool()` with argument building and response parsing.

## Architecture
- Module-level `_client = McpClient(MCP_URL, MCP_DELAY)`
- Internal `_call(name, arguments)` handles errors, returns `{"error": str(e)}` on failure
- All public functions are thin: validate args → `_call()` → return dict

## Function Categories

### Game State (Read-Only)
| Function | MCP Tool | Returns |
|----------|----------|---------|
| `ping()` | `tools/list` | `(bool, error)` |
| `status()` | `get_status` | Full game state |
| `conditions()` | `get_conditions` | Date, weather, temperature |
| `colonists()` | `list_colonists` | Colonist list with health/mood/jobs |
| `alerts()` | `get_alerts` | Active alerts |
| `resources()` | `get_resources` | Stockpile counts |
| `research()` | `get_research` | Research progress |
| `zones()` | `list_zones` | Zone definitions |
| `wildlife()` | `list_wildlife` | Animals on map |
| `pawns(include_hostiles)` | `list_pawns` | All pawns |
| `things()` | `list_things` | All things |
| `get_map()` | `get_map` | Map data |
| `get_map_info()` | `get_map_info` | Map metadata |
| `power()` | `get_power` | Power network |
| `world()` | `get_world` | World data |
| `game_state()` | `get_status` | Bundled status + colonists + alerts |
| `daily_summary()` | `get_status` + `get_conditions` + `list_colonists` + `get_resources` + `get_alerts` | Composite summary |

### Game Flow
| Function | MCP Tool | Args |
|----------|----------|------|
| `pause()` | `set_speed` | `{"action": "pause"}` |
| `resume()` | `set_speed` | `{"action": "unpause"}` |
| `wait(ticks)` | `wait` | `{"ticks": n}` |
| `save(name?)` | `save_game` | `{"name": name}` |
| `say(text)` | `say` | `{"text": text}` |
| `read_letter(id)` | `read_letter` | `{"letter_id": id}` |
| `screenshot()` | `screenshot` | `{}` |

### New Game Setup
| Function | MCP Tool |
|----------|----------|
| `main_menu(action)` | `main_menu` |
| `game_setup_status()` | `game_setup_status` |
| `select_scenario(name)` | `select_scenario` |
| `select_storyteller(storyteller, difficulty?)` | `select_storyteller` |
| `create_world()` | `create_world` |
| `select_starting_site(tile_id?, x?, z?)` | `select_starting_site` |
| `start_game()` | `start_game` |
| `edit_starting_pawn(index, **kwargs)` | `edit_starting_pawn` |

### Colonist Management
| Function | MCP Tool |
|----------|----------|
| `set_priority(name, work_type, priority)` | `set_priority` |
| `draft(names)` | `draft` |
| `undraft(names)` | `undraft` |
| `order(name, verb, target?)` | `order` |
| `do_action(name, action, target?)` | `do_action` |
| `assign(name, bed_id?)` | `assign` |
| `equip(name, weapon_def)` | `equip` |
| `inspect(x, y)` | `inspect` |
| `area(x1, y1, x2, y2, summary)` | `area` |

### Construction & Zoning
| Function | MCP Tool |
|----------|----------|
| `build(def_name, x, y, stuff?)` | `build` |
| `build_wall(x, y, stuff?)` | `build` (Wall) |
| `designate(type, x1, y1, x2, y2)` | `designate` |
| `growing_zone(x1, y1, x2, y2)` | `designate` (GrowingZone) |
| `stockpile(x1, y1, x2, y2)` | `designate` (Stockpile) |
| `set_research(project)` | `set_research` |

### Utility
| Function | MCP Tool |
|----------|----------|
| `unforbid_all()` | `unforbid_all` |
| `survey()` | `survey` |
| `find_rich_soil()` | `find_rich_soil` |
| `chop_trees(x1, y1, x2, y2)` | `designate` (CutPlant) |
| `raid_status()` | `get_raid_status` |
| `find_corpses()` | `find_corpses` |
| `scan_area(x1, y1, x2, y2)` | `scan_area` |

## Notes
- 372 lines, ~35 functions — consider splitting by domain (game_state, colony_mgmt, construction, pawn_control)
- All functions return `dict` (parsed JSON) or `{"error": "..."}`
- Used by CLI, monitor, reflex_actor, dashboard, debrief