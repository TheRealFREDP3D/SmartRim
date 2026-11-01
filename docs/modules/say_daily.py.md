# say_daily.py — Daily In-Game Status + Advice Message

Builds and displays daily status message via MCP `say` command.

## Main Function
```python
def build_message(slot, use_llm, conditions, status, alerts, research, resources, colonists_param):
    # Returns (message_text, meta_dict)
```

## Slots
- `morning` (hour < 12) — overnight summary + day plan
- `evening` (hour >= 12) — day review + night prep

## Message Components
1. **Header**: "SmartRim Daily — Morning/Evening Report — Day X"
2. **Colonists**: Count, min mood, min health, downed
3. **Resources**: Food days, medicine, key materials
4. **Alerts**: Active urgent/warning alerts
4. **Research**: Current project + progress
5. **Advice**: Top 3 ranked actions from situation + lessons

## LLM Advice (`use_llm=True`)
```python
def build_llm_advice(slot, conditions, status, alerts, research, resources, colonists):
    # Prompt includes: situation summary, top lessons, asks for 2-3 specific actions
    # Returns advice text or falls back to rule-based
```

## Rule-Based Fallback
- Food < 2 days → "Prioritize food production"
- Medicine < 5 → "Craft/buy medicine"
- Mood breaks → "Address recreation/beds"
- Raid prep → "Draft shooters, check defenses"
- Idle colonists → "Assign work priorities"

## CLI
```bash
python -m smartrim.say_daily --slot morning
python -m smartrim.say_daily --slot evening --hour 18
```

## Integration
- Called by `monitor._say_daily_message()` at `SAY_DAILY_HOURS`
- Uses `_say_visible()` to briefly unpause for rendering
- `SAY_DAILY_USE_LLM` env var controls LLM vs rule-based (currently accessed via globals() hack)

## Notes
- 238 lines
- `build_message()` is pure (testable with fixtures)
- `say_message()` sends via counselor.say()