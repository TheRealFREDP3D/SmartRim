# SmartRim Sidecar — Reflex Monitor Launcher
# Adviser on (default): .\start-monitor.ps1
# Adviser off:          .\start-monitor.ps1 -ObserveOnly
# Bypass pre-check:     .\start-monitor.ps1 -Force
param(
    [switch]$ObserveOnly,
    [switch]$Force
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

# Pre-flight check: MCP server reachable
$mcpUrl = "http://localhost:8787/"
Write-Host "Checking MCP connectivity ($mcpUrl)... " -NoNewline
try {
    $response = Invoke-WebRequest -Uri $mcpUrl -Method POST -Body '{"jsonrpc":"2.0","id":1,"method":"tools/list","params":{}}' -ContentType "application/json" -UseBasicParsing -TimeoutSec 2
    Write-Host "[OK]" -ForegroundColor Green
} catch {
    Write-Host "[OFFLINE]" -ForegroundColor Red
    Write-Host ""
    Write-Host "============================================================" -ForegroundColor Yellow
    Write-Host "[!] RimWorld MCP Server Not Reachable at $mcpUrl" -ForegroundColor Red
    Write-Host "============================================================" -ForegroundColor Yellow
    Write-Host "The reflex monitor requires a live connection to RimWorld." -ForegroundColor Gray
    Write-Host ""
    Write-Host "Please ensure:" -ForegroundColor Cyan
    Write-Host "  1. RimWorld is running." -ForegroundColor White
    Write-Host "  2. The RimMolt mod is active (listening on port 8787)." -ForegroundColor White
    Write-Host "  3. A colony / save game is loaded in-game." -ForegroundColor White
    Write-Host "============================================================" -ForegroundColor Yellow
    Write-Host ""

    if (-not $Force) {
        $continue = Read-Host "Start monitor anyway (it will retry every 30s)? (y/N)"
        if ($continue -notmatch '^[Yy]$') {
            Write-Host "Startup aborted. Start RimWorld and try again." -ForegroundColor Yellow
            exit 1
        }
        Write-Host "Proceeding with monitor startup..." -ForegroundColor DarkYellow
    } else {
        Write-Host "[-Force specified: proceeding with monitor startup]" -ForegroundColor DarkYellow
    }
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
