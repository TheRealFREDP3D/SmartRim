# llm.py — LLM Integration (Optional)

Graceful degradation: works without any LLM provider.

## Architecture
- Protocol: `LlmClient` with `generate(prompt, system, temperature, ...)`
- Implementations: `OllamaClient`, `OpenAIClient`, `AnthropicClient`
- Factory: `get_client(provider)` → returns client or raises if unavailable
- Optional imports wrapped in try/except

## Models (per-task)
| Task | Env Var | Default |
|------|---------|---------|
| Daily advice | `LLM_MODEL_DAILY` | `llama3.2:1b-instruct-q4_K_M` |
| Debrief | `LLM_MODEL_DEBRIEF` | `gemma4-e2b-rimworld` |
| Chat | `LLM_MODEL_CHAT` | `qwen3-rimworld` |

## Functions

| Function | Description |
|----------|-------------|
| `get_client(provider=None)` | Get LlmClient for provider (ollama/openai/anthropic) |
| `resolve_model(task, provider=None)` | Resolve model name for task |
| `resolve_task_params(task, provider=None)` | Get (model, temperature, num_ctx) for task |
| `generate(prompt, task, provider=None, model=None, system=None, temperature=None, num_ctx=None, cache_system=False)` | High-level generate |

## Providers

### Ollama (default)
- Base URL: `OLLAMA_BASE_URL` (default `http://localhost:11434`)
- No API key needed
- Uses `/api/generate` endpoint

### OpenAI
- Requires `OPENAI_API_KEY` or `LLM_API_KEY`
- Uses `openai` package

### Anthropic
- Requires `ANTHROPIC_API_KEY` or `LLM_API_KEY`
- Uses `anthropic` package

## Low-Level
```python
def _ollama_generate(prompt, model, system, temperature, num_ctx, base_url):
    # Direct HTTP to Ollama
```

## Fallback
If no provider available, `generate()` returns rule-based heuristic response (see `say_daily.py`).

## Notes
- 247 lines
- `cache_system=True` for repeated system prompts (debrief bundles)
- Temperature defaults: daily=0.3, debrief=0.3, chat=0.7