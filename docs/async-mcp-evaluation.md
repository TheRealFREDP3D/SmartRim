# Async MCP Client Evaluation

## Current Implementation

The current `McpClient` in `sidecar/mcp_client.py` uses synchronous `requests`:
- Sequential tool calls with throttling (MCP_DELAY, default 0.15s)
- Retry logic for read-only tools (max_retries, default 3)
- Simple, blocking API

## Potential Async Implementation

An async version would use `aiohttp`:
```python
import aiohttp
import asyncio

class AsyncMcpClient:
    async def call_tool(self, name, arguments):
        async with aiohttp.ClientSession() as session:
            async with session.post(self.url, json=payload) as resp:
                return await resp.json()
```

## Evaluation

### Pros
- **Concurrent calls**: Could poll multiple tools simultaneously (e.g., get_status + get_conditions + get_alerts)
- **Non-blocking**: Better for high-frequency polling or parallel monitoring
- **Scalability**: Handles multiple colonies or concurrent operations better

### Cons
- **Complexity**: Requires async/await throughout the monitoring loop
- **Compatibility**: Requires refactoring all synchronous code to async
- **Throttling complexity**: Current throttling is simple; async rate limiting is more complex
- **Debugging**: Async call stacks are harder to debug
- **Marginal benefit**: Current delay (0.15s) and typical response times (<1s) mean sequential calls are already fast

## Current Performance Analysis

Typical monitoring loop:
- Poll interval: 30s (configurable via POLL_INTERVAL)
- Tool calls per poll: 3-5 (get_conditions, get_status, reflex checks)
- Total latency per poll: ~0.5-1s (well within 30s window)
- Throttling already prevents server overload

## Recommendation

**Do not implement async MCP client at this time.**

**Reasons:**
1. Current synchronous implementation is sufficient for the monitoring loop's 30s polling interval
2. The complexity of async doesn't justify the marginal performance gain
3. The monitoring loop is deliberately paced to avoid overwhelming the game server
4. Future optimization: Only consider async if:
   - Multiple colonies need simultaneous monitoring
   - Polling frequency increases significantly (e.g., sub-second)
   - Concurrent operations are needed (e.g., while polling, also processing debriefs)

## Alternative Optimizations

If performance becomes a concern, consider:
1. **Batch tool calls**: Create a custom MCP endpoint that returns multiple states in one call
2. **Smart polling**: Only poll tools that changed since last check
3. **Caching**: Cache static data (e.g., colonist bio) locally
4. **Event-driven**: Use MCP's notification features instead of polling (if rimmolt supports it)
