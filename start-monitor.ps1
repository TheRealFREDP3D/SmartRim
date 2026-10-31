# SmartRim Sidecar — Reflex Monitor Launcher
# Adviser on (default): .\start-monitor.ps1
# Adviser off:          .\start-monitor.ps1 -ObserveOnly
# Bypass pre-check:     .\start-monitor.ps1 -Force
param(
    [switch]$ObserveOnly,
    [switch]$Force
)
$ErrorActionPreference = "Stop"

# (module launched via -m smartrim.monitor)
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

# Atomic startup lock to prevent concurrent launches
$startupLock = "memory\monitor.startup.lock"
$pidFile = "memory\monitor.pid"

# Acquire startup lock using directory creation (atomic operation)
try {
    New-Item -ItemType Directory -Path $startupLock -ErrorAction Stop | Out-Null
} catch {
    Write-Host "Another startup is in progress (lock file exists)" -ForegroundColor Yellow
    Write-Host "If this is stale, remove: $startupLock"
    exit 1
}

# Check if already running via PID file
if (Test-Path $pidFile) {
    $oldPid = [int](Get-Content $pidFile -ErrorAction SilentlyContinue)
    $proc = Get-Process -Id $oldPid -ErrorAction SilentlyContinue
    if ($proc) {
        # Verify it's actually a SmartRim monitor
        $cmdLine = (Get-WmiObject Win32_Process -Filter "ProcessId = $oldPid" -ErrorAction SilentlyContinue).CommandLine
        if ($cmdLine -and $cmdLine -match "smartrim\.monitor") {
            Write-Host "Monitor is already running (PID $oldPid)" -ForegroundColor Yellow
            Write-Host "View log: $logFile"
            Remove-Item $startupLock -Force -ErrorAction SilentlyContinue
            exit 0
        }
    }
    # stale PID file or wrong process
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
$pyArgs = @("-u", "-m", "smartrim.monitor")
if ($ObserveOnly) {
    $env:OBSERVE_ONLY = "1"
    $pyArgs += "--observe-only"
    Write-Host "Starting reflex monitor (adviser OFF: observe only, no pause, no advice)..." -ForegroundColor Cyan
} else {
    $env:OBSERVE_ONLY = "0"
    Write-Host "Starting reflex monitor (adviser ON)..." -ForegroundColor Cyan
}
$proc = Start-Process -FilePath $pythonExe -ArgumentList $pyArgs -RedirectStandardOutput $logFile -RedirectStandardError "memory\monitor.err.log" -NoNewWindow -PassThru
$childPid = $proc.Id
# Let the monitor process write its own PID file (its PID may differ from the shim's).

# Give the process a moment to start and acquire its own lock
Start-Sleep -Milliseconds 500

# Verify the process is still running (may have exited if it detected another monitor)
$procCheck = Get-Process -Id $childPid -ErrorAction SilentlyContinue
if (-not $procCheck) {
    Write-Host "ERROR: Monitor failed to start (exited immediately)" -ForegroundColor Red
    Remove-Item $pidFile -Force -ErrorAction SilentlyContinue
    Remove-Item $startupLock -Force -ErrorAction SilentlyContinue
    exit 1
}

Write-Host "Monitor started (PID $childPid). Alerts: memory\alerts\current.json" -ForegroundColor Green
Write-Host "Log: $logFile"
Write-Host "Stop with: .\stop-monitor.ps1 (Windows) or ./stop-monitor.sh (Linux/macOS)"

# Cleanup startup lock
Remove-Item $startupLock -Force -ErrorAction SilentlyContinue
