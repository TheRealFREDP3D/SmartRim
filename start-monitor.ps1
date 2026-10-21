# SmartRim Sidecar — Reflex Monitor Launcher
# Adviser on (default): .\start-monitor.ps1
# Adviser off:          .\start-monitor.ps1 -ObserveOnly
param(
    [switch]$ObserveOnly
)
$ErrorActionPreference = "Stop"

$monitorScript = "sidecar\monitor.py"
$logFile = "memory\monitor.log"

# Rotate oversized log files to keep them manageable
if (Test-Path $logFile) {
    $size = (Get-Item $logFile).Length
    if ($size -gt 5MB) {
        $archive = "memory\monitor.$(Get-Date -Format 'yyyyMMdd-HHmmss').log"
        Move-Item $logFile $archive -Force
        Write-Host "Rotated oversized log to $archive" -ForegroundColor Yellow
    }
}

$venvPython = Join-Path $PSScriptRoot ".venv\Scripts\python.exe"
$pythonExe = if (Test-Path $venvPython) { $venvPython } else { "python" }

# Check if already running via PID file
$pidFile = "memory\monitor.pid"
if (Test-Path $pidFile) {
    $oldPid = [int](Get-Content $pidFile -ErrorAction SilentlyContinue)
    $proc = Get-Process -Id $oldPid -ErrorAction SilentlyContinue
    if ($proc) {
        Write-Host "Monitor is already running (PID $oldPid)" -ForegroundColor Yellow
        Write-Host "View log: $logFile"
        exit 0
    }
    # stale PID file
    Remove-Item $pidFile -Force -ErrorAction SilentlyContinue
}

# Check MCP server reachable
try {
    $response = Invoke-WebRequest -Uri "http://localhost:8787/" -Method POST -Body '{"jsonrpc":"2.0","id":1,"method":"tools/list","params":{}}' -ContentType "application/json" -UseBasicParsing -TimeoutSec 3
    Write-Host "MCP server: OK" -ForegroundColor Green
} catch {
    Write-Host "WARNING: MCP server not reachable at localhost:8787" -ForegroundColor Red
    Write-Host "Start RimWorld with the RimMolt mod before using the monitor" -ForegroundColor Yellow
    $continue = Read-Host "Start monitor anyway? (y/N)"
    if ($continue -ne "y") { exit 1 }
}

# Start monitor in background
$pyArgs = @("-u", $monitorScript)
if ($ObserveOnly) {
    $env:OBSERVE_ONLY = "1"
    $pyArgs += "--observe-only"
    Write-Host "Starting reflex monitor (adviser OFF: observe only, no pause, no advice)..." -ForegroundColor Cyan
} else {
    $env:OBSERVE_ONLY = "0"
    Write-Host "Starting reflex monitor (adviser ON)..." -ForegroundColor Cyan
}
Start-Process -FilePath $pythonExe -ArgumentList $pyArgs -RedirectStandardOutput $logFile -RedirectStandardError "memory\monitor.err.log" -NoNewWindow -PassThru | Select-Object Id, StartTime

Write-Host "Monitor started. Alerts: memory\alerts\current.json" -ForegroundColor Green
Write-Host "Log: $logFile"
Write-Host "Stop with: .\stop-monitor.ps1"
