# mcp_client.py — MCP JSON-RPC Client

Thin client for the RimMolt MCP server (Model Context Protocol).

## Class: `McpClient`

```python
McpClient(url: str, delay: float = 0.15, max_retries: int = 3)
```

### Methods

| Method | Description |
|--------|-------------|
| `ping(timeout=1.5)` | Quick health check → `(bool, error_msg)` |
| `call_tool(name, arguments)` | Execute MCP tool, return parsed JSON |

### Behavior
- **Throttling**: Enforces `delay` between calls (`_throttle()`)
- **Retries**: Read-only tools retry up to `max_retries` (3); write tools try once
- **Response parsing**: Extracts `result.content[0].text` and parses as JSON
- **Errors**: Returns `{"error": ...}` for MCP errors; raises `McpError` for transport/parse failures

### Read-Only Tools (auto-retry)
`get_status`, `get_conditions`, `list_colonists`, `get_resources`, `get_research`, `get_alerts`, `list_things`, `get_map`, `get_map_info`, `get_quest`

### Exception
```python
class McpError(Exception): ...
```

## Usage
```python
client = McpClient("http://localhost:8787/")
status = client.call_tool("get_status")
colonists = client.call_tool("list_colonists")
```