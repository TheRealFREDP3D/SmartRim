# SmartRim Sidecar — Monitor Watchdog
#
# Restarts the reflex monitor if it dies, so an unattended play session keeps
# recording snapshots, alerts and auto-pauses.
#
# Usage:
#   .\watchdog-monitor.ps1            # run in the foreground (Ctrl+C to stop)
#   .\watchdog-monitor.ps1 -Detached # run in the background
#
# Stops when memory\monitor.watchdog.stop exists, or when the run-end marker
# for the current RUN_ID is written (the run is over, no need to keep polling).
param(
    [switch]$Detached,
    [int]$CheckIntervalSeconds = 15
)
$ErrorActionPreference = "Continue"

$root = $PSScriptRoot
Set-Location $root

$stopFile = Join-Path $root "memory\monitor.watchdog.stop"
$logFile = Join-Path $root "memory\monitor.watchdog.log"

function Write-WatchdogLog([string]$Message) {
    $line = "$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')  $Message"
    Add-Content -Path $logFile -Value $line
    Write-Host $line
}

function Get-MonitorProcess {
    Get-CimInstance Win32_Process -Filter "Name='python.exe'" |
        Where-Object { $_.CommandLine -like "*smartrim.monitor*" -or $_.CommandLine -like "*monitor.py*" }
}

if ($Detached) {
    # Re-launch this script detached so it survives the calling shell.
    $args = "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", "`"$($MyInvocation.MyCommand.Path)`""
    Start-Process -FilePath "powershell.exe" -ArgumentList $args -WindowStyle Hidden
    Write-Host "Watchdog started (detached). Log: $logFile" -ForegroundColor Green
    exit 0
}

Remove-Item $stopFile -Force -ErrorAction SilentlyContinue
Write-WatchdogLog "Watchdog started. RUN_ID=$env:RUN_ID"

while ($true) {
    if (Test-Path $stopFile) {
        Write-WatchdogLog "Stop file found. Exiting."
        Remove-Item $stopFile -Force -ErrorAction SilentlyContinue
        break
    }

    $runId = $env:RUN_ID
    if (-not $runId) { $runId = "current-run" }
    $endMarker = Join-Path $root "memory\runs\$runId.end.json"
    if (Test-Path $endMarker) {
        Write-WatchdogLog "Run-end marker present for $runId. Exiting."
        break
    }

    $procs = Get-MonitorProcess
    if (-not $procs) {
        Write-WatchdogLog "Monitor not running. Restarting..."
        $py = Join-Path $root ".venv\Scripts\python.exe"
        if (-not (Test-Path $py)) { $py = "python" }
        $env:PYTHONPATH = Join-Path $root "src"
        Start-Process -FilePath $py `
            -ArgumentList "-u", "-m", "smartrim.monitor" `
            -RedirectStandardOutput (Join-Path $root "memory\monitor.log") `
            -RedirectStandardError (Join-Path $root "memory\monitor.err.log") `
            -NoNewWindow | Out-Null
        Start-Sleep -Seconds 5
        $procs = Get-MonitorProcess
        if ($procs) {
            Write-WatchdogLog "Monitor restarted (PID $($procs[0].ProcessId))."
        } else {
            Write-WatchdogLog "Monitor restart FAILED. Will retry."
        }
    }

    Start-Sleep -Seconds $CheckIntervalSeconds
}
