# Start the SmartRim TUI
# This script launches the Textual terminal UI

Write-Host "Starting SmartRim TUI..." -ForegroundColor Green

# Activate virtual environment if it exists
if (Test-Path ".venv\Scripts\Activate.ps1") {
    Write-Host "Activating virtual environment..." -ForegroundColor Yellow
    & .venv\Scripts\Activate.ps1
}

# Install required packages if not already installed
Write-Host "Checking required packages..." -ForegroundColor Yellow
pip install -q textual

# Start the TUI
python -m smartrim.tui