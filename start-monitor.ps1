# RimWorld Counselor Sidecar — Reflex Monitor Launcher
$ErrorActionPreference = "Stop"

$monitorScript = "sidecar\monitor.py"
$logFile = "memory\monitor.log"

$venvPython = Join-Path $PSScriptRoot ".venv\Scripts\python.exe"
$pythonExe = if (Test-Path $venvPython) { $venvPython } else { "python" }

# Check if already running
$existing = Get-CimInstance Win32_Process -Filter "Name='python.exe'" |
    Where-Object { $_.CommandLine -like "*monitor.py*" }
if ($existing) {
    Write-Host "Monitor is already running (PID $($existing.ProcessId))" -ForegroundColor Yellow
    Write-Host "View log: $logFile"
    exit 0
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
Write-Host "Starting reflex monitor..." -ForegroundColor Cyan
Start-Process -FilePath $pythonExe -ArgumentList "-u", $monitorScript -RedirectStandardOutput $logFile -RedirectStandardError "memory\monitor.err.log" -NoNewWindow -PassThru | Select-Object Id, StartTime

Write-Host "Monitor started. Alerts: memory\alerts\current.json" -ForegroundColor Green
Write-Host "Log: $logFile"
Write-Host "Stop with: .\stop-monitor.ps1"
