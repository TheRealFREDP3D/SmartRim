import requests
import json


class McpError(Exception):
    pass


class McpClient:
    def __init__(self, url):
        self.url = url
        self.id_counter = 0

    def call_tool(self, name, arguments=None):
        self.id_counter += 1
        payload = {
            "jsonrpc": "2.0",
            "id": self.id_counter,
            "method": "tools/call",
            "params": {"name": name, "arguments": arguments or {}},
        }
        try:
            resp = requests.post(self.url, json=payload, timeout=10)
            resp.raise_for_status()
            result = resp.json()
        except (requests.exceptions.RequestException, ValueError) as e:
            raise McpError(f"transport/parse error calling {name}: {e}") from e

        if "error" in result:
            # JSON-RPC level error
            return {"error": result["error"]}
        if "result" in result and "content" in result["result"]:
            text = result["result"]["content"][0]["text"]
            try:
                return json.loads(text)
            except (json.JSONDecodeError, TypeError):
                return {"text": text}
        return result
