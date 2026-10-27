#!/bin/bash
# SmartRim Sidecar — Stop Monitor

set -e

pidFile="memory/monitor.pid"

if [ ! -f "$pidFile" ]; then
    echo "Monitor is not running (no PID file)"
    exit 0
fi

pid=$(cat "$pidFile" 2>/dev/null || echo "")
if [ -z "$pid" ]; then
    echo "Monitor is not running (empty PID file)"
    rm -f "$pidFile"
    exit 0
fi

if kill -0 "$pid" 2>/dev/null; then
    echo "Stopping monitor (PID $pid)..."
    kill "$pid"
    # Wait for process to exit
    for i in {1..10}; do
        if ! kill -0 "$pid" 2>/dev/null; then
            echo "Monitor stopped"
            rm -f "$pidFile"
            exit 0
        fi
        sleep 0.5
    done
    # Force kill if still running
    kill -9 "$pid" 2>/dev/null || true
    echo "Monitor force-stopped"
else
    echo "Monitor is not running (stale PID file)"
fi

rm -f "$pidFile"
