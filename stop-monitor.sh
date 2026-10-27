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

# Validate PID is a positive integer
if ! [[ "$pid" =~ ^[1-9][0-9]*$ ]]; then
    echo "ERROR: Invalid PID in PID file: $pid"
    rm -f "$pidFile"
    exit 1
fi

# Verify the process is actually a SmartRim monitor
if kill -0 "$pid" 2>/dev/null; then
    # Check command line to verify it's a SmartRim monitor
    if ! ps -p "$pid" -o command= 2>/dev/null | grep -q "smartrim.monitor"; then
        echo "ERROR: PID $pid exists but is not a SmartRim monitor"
        rm -f "$pidFile"
        exit 1
    fi
    echo "Stopping monitor (PID $pid)..."
    kill "$pid"
    # Wait for process to exit
    for i in {1..10}; do
        if ! kill -0 "$pid" 2>/dev/null; then
            echo "Monitor stopped"
            # Verify PID file still contains the same PID before removal
            current_pid=$(cat "$pidFile" 2>/dev/null || echo "")
            if [ "$current_pid" = "$pid" ]; then
                rm -f "$pidFile"
            fi
            exit 0
        fi
        sleep 0.5
    done
    # Force kill if still running
    kill -9 "$pid" 2>/dev/null || true
    echo "Monitor force-stopped"
    # Verify PID file still contains the same PID before removal
    current_pid=$(cat "$pidFile" 2>/dev/null || echo "")
    if [ "$current_pid" = "$pid" ]; then
        rm -f "$pidFile"
    fi
else
    echo "Monitor is not running (stale PID file)"
fi

rm -f "$pidFile"
