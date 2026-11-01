# chat.py — Interactive Colony Chat

REPL for chatting about colony state via local LLM.

## Functions

| Function | Description |
|----------|-------------|
| `get_context()` | Fetch current game state (status, conditions, colonists, alerts) |
| `chat_loop()` | REPL: prompt → context + history → LLM → response |
| `main()` | Entry point |

## Usage

```bash
python -m smartrim.chat
```

## Flow

1. `get_context()` → calls counselor for status, conditions, colonists, alerts
2. Build system prompt with context
3. Loop: user input → append to history → `llm.generate()` → print response
4. Context refreshed every 5 turns

## Notes

- 77 lines
- Requires LLM (Ollama by default)
- Graceful degradation if LLM unavailable
- Simple terminal interface
