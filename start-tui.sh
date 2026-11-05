#!/usr/bin/env bash
# Start the SmartRim TUI
set -e

echo "Starting SmartRim TUI..."

if [ -f ".venv/bin/activate" ]; then
    echo "Activating virtual environment..."
    source .venv/bin/activate
fi

echo "Checking required packages..."
pip install -q textual

python -m smartrim.tui