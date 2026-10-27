#!/bin/bash
# Start the SmartRim Dashboard
# This script launches the Streamlit dashboard

echo "Starting SmartRim Dashboard..."

# Activate virtual environment if it exists
if [ -f ".venv/bin/activate" ]; then
    echo "Activating virtual environment..."
    source .venv/bin/activate
elif [ -f ".venv/Scripts/activate" ]; then
    echo "Activating virtual environment..."
    source .venv/Scripts/activate
fi

# Install required packages if not already installed
echo "Checking required packages..."
pip install -q streamlit plotly pandas

# Start the dashboard
echo "Launching dashboard at http://localhost:8501"
streamlit run src/smartrim/dashboard.py
