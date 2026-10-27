# SmartRim Sidecar — Installer
$ErrorActionPreference = "Stop"

Write-Host "=== SmartRim Installer ===" -ForegroundColor Cyan

# Prefer the project venv if present
$venvPython = Join-Path $PSScriptRoot ".venv\Scripts\python.exe"
if (Test-Path $venvPython) {
    $pythonExe = $venvPython
} else {
    $python = Get-Command python -ErrorAction SilentlyContinue
    if (-not $python) {
        Write-Host "ERROR: Python not found. Install Python 3.10+ from python.org" -ForegroundColor Red
        exit 1
    }
    $pythonExe = "python"
}
$version = & $pythonExe --version 2>&1
Write-Host "Found: $version"

# Install dependencies
Write-Host "`nInstalling dependencies..." -ForegroundColor Yellow
& $pythonExe -m pip install -e ".[dev]"
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
Write-Host "Run .\start-monitor.ps1 (Windows) or ./start-monitor.sh (Linux/macOS) to start the reflex monitor"
