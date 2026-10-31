# cli.py — Human Command Interface

**Entry point:** `python -m smartrim.cli <command> [args...]`

Wraps `counselor.py` MCP calls for manual game control and reflex management.

---

## Command Reference

### Connection

| Command | Description |
|---------|-------------|
| `ping` | Test MCP server reachability |

### Game State (read-only)

| Command | Description |
| --------- | ------------- |
| `status` | Full game state via `counselor.game_state()` |
| `colonists` | List all colonists with health, mood, jobs |
| `alerts` | Current game alerts |
| `resources` | Resource stockpiles |
| `research` | Research progress |
| `zones` | Zone definitions |
| `map` | Map info |
| `power` | Power network status |
| `world` | World data |
| `daily` | Daily summary |

### Game Control

| Command | Description |
| --------- | ------------- |
| `pause` | Pause game (`set_speed pause`) |
| `resume` | Resume game (`set_speed unpause`) |
| `wait <ticks>` | Wait N in-game ticks (default 1) |
| `save [name]` | Save game |
| `screenshot` | Take screenshot |
| `say <text>` | Display in-game message |

### Pawn Control

| Command | Args | Description |
| --------- | ------ | ------------- |
| `draft` | `<name>...` | Draft colonists |
| `undraft` | `<name>...` | Undraft colonists |
| `order` | `<name> <verb> [target]` | Order pawn (Goto, Attack, etc.) |
| `inspect` | `<x> <y>` | Inspect cell |
| `priority` | `<name> <work_type> <priority>` | Set work priority |
| `area` | `<x1> <y1> <x2> <y2>` | Show area summary |

### Construction & Zoning

| Command | Args | Description |
|---------|------|-------------|
| `build` | `<def> <x> <y> [stuff]` | Build structure |
| `designate` | `<type> <x1> <y1> <x2> <y2>` | Designate area (Mine, Chop, etc.) |
| `research_set` | `<project>` | Set research project |

### Human Actions (recorded + defer reflex)

These write to `memory/last_human_action.json` **before** the MCP call, deferring reflex actions for 60 seconds.

| Command | Args |
|---------|------|
| `build` | `<def> <x> <y> [stuff]` |
| `order` | `<name> <verb> [target]` |
| `designate` | `<type> <x1> <y1> <x2> <y2>` |

### Reflex Control

| Command | Description |
| --------- | ------------- |
| `reflex pause` | Suspend reflex for one in-game day |
| `reflex resume` | Clear pause early |
| `reflex status` | Show kill/dry-run/pause/lock/human-action state |

---

## Usage Examples

```bash
# Test connection
python -m smartrim.cli ping

# Reflex management
python -m smartrim.cli reflex status
python -m smartrim.cli reflex pause
python -m smartrim.cli reflex resume

# Manual building (recorded as human action)
python -m smartrim.cli build Wall 10 15 WoodLog

# Direct pawn order
python -m smartrim.cli order "John" Goto 20 30

# Designate mining area
python -m smartrim.cli designate Mine 10 10 20 20
```

---

## Implementation Notes

- **Reflex pause** uses atomic write: `.tmp` → `os.replace` (see `_record_human_action` and `run_reflex`)
- **Human action window** = 60 seconds (see `reflex_actor.py:348` `HUMAN_WINDOW_SECONDS`)
- Most commands are thin lambdas delegating to `counselor` module
- `run_reflex()` instantiates `ReflexActor()` to manage pause file
