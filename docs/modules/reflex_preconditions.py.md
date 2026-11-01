# reflex_preconditions.py — Precondition Predicates

Pure functions `(game_state) -> bool` for reflex action guards. Testable without MCP.

## Exported
```python
__all__ = ["PRECONDITIONS", "has_fire_alert", "has_raid_alert", "has_shooter_above_5", "has_unassigned_colonist", "none_drafted"]
```

## Predicates

| Name | Function | Description |
|------|----------|-------------|
| `has_raid_alert` | `has_raid_alert(game_state)` | Any alert contains raid/enemy/attack |
| `has_fire_alert` | `has_fire_alert(game_state)` | Any alert contains fire |
| `has_unassigned_colonist` | `has_unassigned_colonist(game_state)` | Idle alert OR colonist without bed |
| `has_shooter_above_5` | `has_shooter_above_5(game_state)` | ≥5 combat-ready colonists (not downed, not sleeping, healthy) |
| `none_drafted` | `none_drafted(game_state)` | No colonist currently drafted |

## Registry
```python
PRECONDITIONS = {
    "has_raid_alert": has_raid_alert,
    "has_fire_alert": has_fire_alert,
    "has_unassigned_colonist": has_unassigned_colonist,
    "has_shooter_above_5": has_shooter_above_5,
    "none_drafted": none_drafted,
}
```

## Helpers (private)
- `_alerts(game_state)` → list of alerts
- `_colonists(game_state)` → list of colonists
- `_alert_text(alert)` → combined label+message lowercase

## Missing (referenced in YAML but not implemented)
- `has_downed_colonist` — needed by `rescue-downed`
- `has_wounded_colonist` — needed by `prioritize-treatment`

## Notes
- 90 lines
- Unknown precondition names in YAML are silently dropped → vacuously true (fail-open bug)
- Should fail closed: raise at load time if precondition not in `PRECONDITIONS`