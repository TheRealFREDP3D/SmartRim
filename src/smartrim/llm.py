"""Optional LLM helper for local (Ollama) or cloud providers.

Usage:
    from smartrim.llm import generate
    text = generate("Summarise this colony run: ...", provider="ollama", model="qwen3-rimworld")
"""

import json
import os
import urllib.error
import urllib.request

try:
    from smartrim.config import (
        LLM_API_KEY,
        LLM_MODEL,
        LLM_MODEL_CHAT,
        LLM_MODEL_DAILY,
        LLM_MODEL_DEBRIEF,
        LLM_PROVIDER,
        OLLAMA_BASE_URL,
    )
except ImportError:
    LLM_PROVIDER = os.getenv("LLM_PROVIDER", "ollama")
    LLM_MODEL = os.getenv("LLM_MODEL")
    LLM_MODEL_DAILY = os.getenv("LLM_MODEL_DAILY", "llama3.2:1b-instruct-q4_K_M")
    LLM_MODEL_DEBRIEF = os.getenv("LLM_MODEL_DEBRIEF", "gemma4-e2b-rimworld")
    LLM_MODEL_CHAT = os.getenv("LLM_MODEL_CHAT", "qwen3-rimworld")
    LLM_API_KEY = os.getenv("LLM_API_KEY")
    OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")


def _ollama_generate(prompt, model, base_url, system=None, temperature=0.2, num_ctx=8192, think=False):
    url = base_url.rstrip("/") + "/api/generate"
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "think": think,
        "options": {"temperature": temperature, "num_ctx": num_ctx},
    }
    if system:
        payload["system"] = system
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=300) as resp:
        obj = json.loads(resp.read().decode("utf-8"))
    return obj.get("response", "")


def resolve_model(task=None, model=None, provider=None):
    """Resolve (provider, model) from explicit args, task registry, or config fallback."""
    if model is not None and provider is not None:
        return provider, model
    if task is not None and task in MODEL_REGISTRY:
        reg_provider, reg_model = MODEL_REGISTRY[task]
        if provider is None:
            provider = reg_provider
        if model is None:
            model = reg_model
    if provider is None:
        provider = LLM_PROVIDER or "ollama"
    if model is None:
        model = LLM_MODEL
    if model is None:
        model = LLM_MODEL_DEBRIEF
    return provider, model


def generate(prompt, provider=None, model=None, task=None, system=None, **kwargs):
    provider, model = resolve_model(task=task, model=model, provider=provider)
    provider = (provider or "ollama").lower()
    if provider == "ollama":
        base = kwargs.pop("base_url", OLLAMA_BASE_URL)
        return _ollama_generate(prompt, model, base, system=system, **kwargs)
    raise NotImplementedError(f"Provider '{provider}' not implemented in llm.py (use openai/anthropic SDKs directly).")


# ModelRegistry: task -> (provider, model). Resolved after config import.
MODEL_REGISTRY = {
    "daily_advice": ("ollama", LLM_MODEL_DAILY),
    "debrief": ("ollama", LLM_MODEL_DEBRIEF),
    "chat": ("ollama", LLM_MODEL_CHAT),
}


if __name__ == "__main__":
    import sys
    p = " ".join(sys.argv[1:]) or "Reply with JSON only: {\"ok\": true}"
    print(generate(p))