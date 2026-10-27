#!/bin/bash
# SmartRim Sidecar — Reflex Monitor Launcher
# Adviser on (default): ./start-monitor.sh
# Adviser off:          ./start-monitor.sh --observe-only
# Bypass pre-check:     ./start-monitor.sh --force

set -e

# (module launched via -m smartrim.monitor)
logFile="memory/monitor.log"

# Rotate oversized log files to keep them manageable
if [ -f "$logFile" ]; then
    size=$(stat -f%z "$logFile" 2>/dev/null || stat -c%s "$logFile" 2>/dev/null)
    if [ "$size" -gt 5242880 ]; then  # 5MB
        archive="memory/monitor.$(date +%Y%m%d-%H%M%S).log"
        mv "$logFile" "$archive"
        echo "Rotated oversized log to $archive"
    fi
fi

# Find Python
if [ -f ".venv/bin/python" ]; then
    pythonExe=".venv/bin/python"
elif [ -f ".venv/Scripts/python.exe" ]; then
    pythonExe=".venv/Scripts/python.exe"
else
    pythonExe=$(command -v python3 || command -v python)
fi

# Check if already running via PID file
pidFile="memory/monitor.pid"
if [ -f "$pidFile" ]; then
    oldPid=$(cat "$pidFile" 2>/dev/null || echo "")
    if [ -n "$oldPid" ] && kill -0 "$oldPid" 2>/dev/null; then
        echo "Monitor is already running (PID $oldPid)"
        echo "View log: $logFile"
        exit 0
    fi
    # stale PID file
    rm -f "$pidFile"
fi

# Pre-flight check: MCP server reachable
mcpUrl="http://localhost:8787/"
echo -n "Checking MCP connectivity ($mcpUrl)... "
if curl -s -X POST -H "Content-Type: application/json" -d '{"jsonrpc":"2.0","id":1,"method":"tools/list","params":{}}' --max-time 2 "$mcpUrl" > /dev/null 2>&1; then
    echo "[OK]"
else
    echo "[OFFLINE]"
    echo ""
    echo "============================================================"
    echo "[!] RimWorld MCP Server Not Reachable at $mcpUrl"
    echo "============================================================"
    echo "The reflex monitor requires a live connection to RimWorld."
    echo ""
    echo "Please ensure:"
    echo "  1. RimWorld is running."
    echo "  2. The RimMolt mod is active (listening on port 8787)."
    echo "  3. A colony / save game is loaded in-game."
    echo "============================================================"
    echo ""

    if [ "$1" != "--force" ]; then
        read -p "Start monitor anyway (it will retry every 30s)? (y/N) " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            echo "Startup aborted. Start RimWorld and try again."
            exit 1
        fi
        echo "Proceeding with monitor startup..."
    else
        echo "[--force specified: proceeding with monitor startup]"
    fi
fi

# Start monitor in background
pyArgs=("-u" "-m" "smartrim.monitor")
if [ "$1" == "--observe-only" ]; then
    export OBSERVE_ONLY="1"
    pyArgs+=("--observe-only")
    echo "Starting reflex monitor (adviser OFF: observe only, no pause, no advice)..."
else
    export OBSERVE_ONLY="0"
    echo "Starting reflex monitor (adviser ON)..."
fi

nohup $pythonExe "${pyArgs[@]}" > "$logFile" 2> "memory/monitor.err.log" &
echo $! > "$pidFile"

echo "Monitor started. Alerts: memory/alerts/current.json"
echo "Log: $logFile"
echo "Stop with: ./stop-monitor.sh"
