# Start the SmartRim Desktop Notifier
# Polls urgent alerts and pops a window on new ones.

Write-Host "Starting SmartRim Notifier..." -ForegroundColor Green

if (Test-Path ".venv\Scripts\Activate.ps1") {
    & .venv\Scripts\Activate.ps1
}

python -m smartrim.notify
