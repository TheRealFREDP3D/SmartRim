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
    pythonExe=$(command -v python3 || command -v python)
    if [ -z "$pythonExe" ]; then
        echo "ERROR: Python not found. Install Python 3.11+ from python.org"
        exit 1
    fi
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
