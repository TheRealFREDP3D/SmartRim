import time
import requests
import json


class McpError(Exception):
    pass


class McpClient:
    def __init__(self, url, delay=0.15, max_retries=3):
        self.url = url
        self.id_counter = 0
        self.delay = delay
        self.max_retries = max_retries
        self._last_call = 0.0

    def _throttle(self):
        now = time.time()
        elapsed = now - self._last_call
        if elapsed < self.delay:
            time.sleep(self.delay - elapsed)
        self._last_call = time.time()

    def call_tool(self, name, arguments=None):
        self.id_counter += 1
        payload = {
            "jsonrpc": "2.0",
            "id": self.id_counter,
            "method": "tools/call",
            "params": {"name": name, "arguments": arguments or {}},
        }
        last_err = None
        for attempt in range(self.max_retries):
            self._throttle()
            try:
                resp = requests.post(self.url, json=payload, timeout=30)
                resp.raise_for_status()
                result = resp.json()
                if "error" in result:
                    return {"error": result["error"]}
                if "result" in result and "content" in result["result"]:
                    text = result["result"]["content"][0]["text"]
                    try:
                        return json.loads(text)
                    except (json.JSONDecodeError, TypeError):
                        return {"text": text}
                return result
            except (requests.exceptions.RequestException, ValueError) as e:
                last_err = e
                time.sleep(0.5 * (attempt + 1))
        raise McpError(f"transport/parse error calling {name}: {last_err}")
