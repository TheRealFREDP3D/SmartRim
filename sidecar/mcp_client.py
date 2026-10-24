import json
import time
from typing import Any

import requests


class McpError(Exception):
    """Base exception for MCP client errors."""


READ_ONLY_TOOLS: set[str] = {
    "get_status",
    "get_conditions",
    "list_colonists",
    "get_resources",
    "get_research",
    "get_alerts",
    "list_things",
    "get_map",
    "get_map_info",
    "get_quest",
}


class McpClient:
    def __init__(self, url: str, delay: float = 0.15, max_retries: int = 3) -> None:
        self.url = url
        self.id_counter = 0
        self.delay = delay
        self.max_retries = max_retries
        self._last_call = 0.0

    def ping(self, timeout: float = 1.5) -> tuple[bool, str | None]:
        """Quick check if MCP server is reachable.

        Returns (True, None) if reachable, or (False, error_message).
        """
        payload = {
            "jsonrpc": "2.0",
            "id": 0,
            "method": "tools/list",
            "params": {},
        }
        try:
            resp = requests.post(self.url, json=payload, timeout=timeout)
            resp.raise_for_status()
            return True, None
        except Exception as e:
            return False, str(e)

    def _throttle(self) -> None:
        now = time.time()
        elapsed = now - self._last_call
        if elapsed < self.delay:
            time.sleep(self.delay - elapsed)
        self._last_call = time.time()

    def call_tool(self, name: str, arguments: dict[str, Any] | None = None) -> dict[str, Any]:
        self.id_counter += 1
        payload = {
            "jsonrpc": "2.0",
            "id": self.id_counter,
            "method": "tools/call",
            "params": {"name": name, "arguments": arguments or {}},
        }
        last_err = None
        max_attempts = self.max_retries if name in READ_ONLY_TOOLS else 1
        for attempt in range(max_attempts):
            self._throttle()
            try:
                resp = requests.post(self.url, json=payload, timeout=30)
                resp.raise_for_status()
                result = resp.json()
                if "error" in result:
                    return {"error": result["error"]}
                if "result" in result and "content" in result["result"]:
                    content = result["result"].get("content") or []
                    if not content or not isinstance(content[0], dict) or "text" not in content[0]:
                        return result
                    text = content[0]["text"]
                    try:
                        return json.loads(text)
                    except (json.JSONDecodeError, TypeError):
                        return {"text": text}
                return result
            except (requests.exceptions.RequestException, ValueError) as e:
                last_err = e
                if attempt < max_attempts - 1:
                    time.sleep(0.5 * (attempt + 1))
        raise McpError(f"transport/parse error calling {name}: {last_err}")
