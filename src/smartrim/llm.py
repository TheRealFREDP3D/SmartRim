"""Optional LLM helper for local (Ollama) or cloud providers.

Usage:
    from smartrim.llm import generate
    text = generate("Summarise this colony run: ...", provider="ollama", model="qwen3-rimworld")
"""

import json
import os
import urllib.error
import urllib.request
from typing import Protocol, runtime_checkable

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


@runtime_checkable
class LlmClient(Protocol):
    def generate(self, prompt: str, *, system: str | None = None, temperature: float = 0.2,
                 num_ctx: int = 8192, max_tokens: int | None = None) -> str: ...


class OllamaClient:
    def __init__(self, model: str, base_url: str | None = None):
        self.model = model
        self.base_url = base_url or OLLAMA_BASE_URL

    def generate(self, prompt: str, *, system: str | None = None, temperature: float = 0.2,
                 num_ctx: int = 8192, max_tokens: int | None = None) -> str:
        return _ollama_generate(prompt, self.model, self.base_url, system=system,
                                temperature=temperature, num_ctx=num_ctx)


class OpenAIClient:
    def __init__(self, model: str, api_key: str | None = None):
        self.model = model
        self.api_key = api_key or os.getenv("OPENAI_API_KEY") or os.getenv("LLM_API_KEY")

    def generate(self, prompt: str, *, system: str | None = None, temperature: float = 0.2,
                 num_ctx: int = 8192, max_tokens: int | None = None) -> str:
        try:
            import openai
        except ImportError as e:
            raise ImportError("openai SDK not installed. pip install openai") from e
        client = openai.OpenAI(api_key=self.api_key)
        messages = []
        if system:
            messages.append({"role": "system", "content": system})
        messages.append({"role": "user", "content": prompt})
        kwargs = {"model": self.model, "messages": messages, "temperature": temperature}
        if max_tokens is not None:
            kwargs["max_tokens"] = max_tokens
        resp = client.chat.completions.create(**kwargs)
        choice = resp.choices[0].message.content if resp.choices else None
        return choice or ""


class AnthropicClient:
    def __init__(self, model: str, api_key: str | None = None):
        self.model = model
        self.api_key = api_key or os.getenv("ANTHROPIC_API_KEY") or os.getenv("LLM_API_KEY")

    def generate(self, prompt: str, *, system: str | None = None, temperature: float = 0.2,
                 num_ctx: int = 8192, max_tokens: int | None = None) -> str:
        try:
            import anthropic
        except ImportError as e:
            raise ImportError("anthropic SDK not installed. pip install anthropic") from e
        client = anthropic.Anthropic(api_key=self.api_key)
        kwargs = {"model": self.model, "max_tokens": max_tokens or 1024,
                  "messages": [{"role": "user", "content": prompt}]}
        if system:
            kwargs["system"] = system
        if temperature is not None:
            kwargs["temperature"] = temperature
        resp = client.messages.create(**kwargs)
        parts = [b.text for b in getattr(resp, "content", []) if getattr(b, "type", None) == "text"]
        return "".join(parts)


def get_client(provider: str | None = None, model: str | None = None, task: str | None = None) -> LlmClient:
    provider, model = resolve_model(task=task, model=model, provider=provider)
    provider = (provider or "ollama").lower()
    if provider == "ollama":
        return OllamaClient(model=model, base_url=OLLAMA_BASE_URL)
    if provider == "openai":
        return OpenAIClient(model=model)
    if provider == "anthropic":
        return AnthropicClient(model=model)
    raise ValueError(f"Unknown provider: {provider}")


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


def generate(prompt, provider=None, model=None, task=None, system=None, temperature=0.2, num_ctx=8192,
            max_tokens=None, **kwargs):
    client = get_client(provider=provider, model=model, task=task)
    return client.generate(prompt, system=system, temperature=temperature, num_ctx=num_ctx,
                           max_tokens=max_tokens)


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