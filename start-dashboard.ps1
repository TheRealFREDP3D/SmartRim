# Start the SmartRim Dashboard
# This script launches the Streamlit dashboard

Write-Host "Starting SmartRim Dashboard..." -ForegroundColor Green

# Activate virtual environment if it exists
if (Test-Path ".venv\Scripts\Activate.ps1") {
    Write-Host "Activating virtual environment..." -ForegroundColor Yellow
    & .venv\Scripts\Activate.ps1
}

# Install required packages if not already installed
Write-Host "Checking required packages..." -ForegroundColor Yellow
pip install -q streamlit plotly pandas

# Start the dashboard
Write-Host "Launching dashboard at http://localhost:8501" -ForegroundColor Green
streamlit run sidecar/dashboard.py
