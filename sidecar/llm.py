"""Optional LLM helper for local (Ollama) or cloud providers.

Usage:
    from llm import generate
    text = generate("Summarise this colony run: ...", provider="ollama", model="qwen3-rimworld")
"""

import json
import os
import urllib.error
import urllib.request

try:
    from config import LLM_API_KEY, LLM_MODEL, LLM_PROVIDER, OLLAMA_BASE_URL
except ImportError:
    LLM_PROVIDER = os.getenv("LLM_PROVIDER", "ollama")
    LLM_MODEL = os.getenv("LLM_MODEL", "qwen3-rimworld")
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


def generate(prompt, provider=None, model=None, system=None, **kwargs):
    provider = (provider or LLM_PROVIDER or "ollama").lower()
    if model is None:
        if provider == "ollama":
            model = os.getenv("OLLAMA_MODEL", "gemma4-e2b-rimworld") or LLM_MODEL or "gemma4-e2b-rimworld"
        else:
            model = LLM_MODEL or "qwen3-rimworld"
    if provider == "ollama":
        base = kwargs.pop("base_url", OLLAMA_BASE_URL)
        return _ollama_generate(prompt, model, base, system=system, **kwargs)
    raise NotImplementedError(f"Provider '{provider}' not implemented in llm.py (use openai/anthropic SDKs directly).")


if __name__ == "__main__":
    import sys
    p = " ".join(sys.argv[1:]) or "Reply with JSON only: {\"ok\": true}"
    print(generate(p))