# RimWorld Counselor Sidecar — Installer
$ErrorActionPreference = "Stop"

Write-Host "=== RimWorld Counselor Sidecar Installer ===" -ForegroundColor Cyan

# Check Python
$python = Get-Command python -ErrorAction SilentlyContinue
if (-not $python) {
    Write-Host "ERROR: Python not found. Install Python 3.10+ from python.org" -ForegroundColor Red
    exit 1
}
$version = python --version 2>&1
Write-Host "Found: $version"

# Install dependencies
Write-Host "`nInstalling dependencies..." -ForegroundColor Yellow
pip install -r sidecar/requirements.txt
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: pip install failed" -ForegroundColor Red
    exit 1
}

# Ensure directories exist
$dirs = @("memory\alerts", "memory\snapshots", "memory\debriefs")
foreach ($dir in $dirs) {
    if (-not (Test-Path $dir)) {
        New-Item -ItemType Directory -Force -Path $dir | Out-Null
        Write-Host "Created: $dir"
    }
}

Write-Host "`n=== Install complete ===" -ForegroundColor Green
Write-Host "Run .\start-monitor.ps1 to start the reflex monitor"
