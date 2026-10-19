# Phases (our labels, not wiki terms)

The phase classifier in `sidecar/situation.py` assigns each colony state to one of five
phases. Boundaries are our own rules; the wiki does not define game phases.

| Phase | Rule |
|---|---|
| `early_survival` | day <= 7 |
| `stabilization` | 8 <= day <= 20 and no active raid/threat alert |
| `raid_prep` | any raid-related alert or letter is active, or the colony is inside a known raid window |
| `expansion` | day > 20 and no active threat |
| `crisis` | any of: colonist downed, predator or hostile near a colonist, danger rating High or Extreme, colony death. Overrides all other phases. |

`day` is `daysPassed` from `get_status` (the 1st day is Day 1, so `daysPassed` 0 = Day 1).
`crisis` overrides everything. `raid_prep` overrides `stabilization` and `expansion`.

## Threat taxonomy (monitor alert category -> threat tag)

Defined once in `sidecar/situation.py`. Lesson `trigger.threats` values must use this vocabulary.

| Monitor `category` | Threat tag |
|---|---|
| `downed` | `colonist_downed` |
| `mood_extreme`, `mood_major`, `mood_minor` | `mood_break_risk` |
| `health` | `colonist_injured` |
| `danger_rating` (High/Extreme) | `danger_high` |
| `hostile` | `raid_incoming` |
| `predator_near` | `predator_near_worker` |
| `food_low` | `low_food` |
| `medicine_low` | `medical_untreated` (also fires on `medical_treatment_needed`) |
| `idle_colonist` | `idle_colonists` |
| `sleeping_during_threat` | `threat_response` |
| `colony_death` | `colony_death` |
| `game_alert` | `other_game_alert` (label keywords refine: raid/enemy -> raid_incoming) |

## Resource vocabulary

Lesson `trigger.resources` values: `food_under_5_days`, `food_under_2_days`, `no_medicine`,
`medicine_under_5`, `low_wood`, `low_steel`.

## Note on wiki facts

Phase boundaries and threat tags are our own definitions. The wiki provides the underlying
mechanics (mood thresholds, raid points, etc.) but does not define phases or alert taxonomies.
