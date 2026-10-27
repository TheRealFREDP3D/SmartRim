#!/bin/bash
# SmartRim Sidecar — Installer

set -e

echo "=== SmartRim Installer ==="

# Prefer the project venv if present
if [ -f ".venv/bin/python" ]; then
    pythonExe=".venv/bin/python"
elif [ -f ".venv/Scripts/python.exe" ]; then
    pythonExe=".venv/Scripts/python.exe"
else
    # Create a venv if none exists
    echo "No project venv found. Creating one..."
    python3 -m venv .venv 2>/dev/null || python -m venv .venv 2>/dev/null || {
        echo "ERROR: Failed to create venv. Install Python 3.11+ from python.org"
        exit 1
    }
    if [ -f ".venv/bin/python" ]; then
        pythonExe=".venv/bin/python"
    elif [ -f ".venv/Scripts/python.exe" ]; then
        pythonExe=".venv/Scripts/python.exe"
    else
        echo "ERROR: Failed to locate Python in created venv"
        exit 1
    fi
    echo "Created virtual environment at .venv"
fi

version=$($pythonExe --version 2>&1)
echo "Found: $version"

# Install dependencies
echo ""
echo "Installing dependencies..."
$pythonExe -m pip install -e ".[dev]"

# Ensure directories exist
dirs=("memory/alerts" "memory/snapshots" "memory/debriefs")
for dir in "${dirs[@]}"; do
    if [ ! -d "$dir" ]; then
        mkdir -p "$dir"
        echo "Created: $dir"
    fi
done

echo ""
echo "=== Install complete ==="
echo "Run ./start-monitor.sh to start the reflex monitor"
