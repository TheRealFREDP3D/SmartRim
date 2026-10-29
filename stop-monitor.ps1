# SmartRim Sidecar — Stop Reflex Monitor
$pidFile = "memory\monitor.pid"

if (Test-Path $pidFile) {
    $pid = [int](Get-Content $pidFile -ErrorAction SilentlyContinue)
    if ($pid -gt 0) {
        # Validate PID is a positive integer
        $proc = Get-Process -Id $pid -ErrorAction SilentlyContinue
        if ($proc) {
            # Verify it's actually a SmartRim monitor
            $cmdLine = (Get-WmiObject Win32_Process -Filter "ProcessId = $pid" -ErrorAction SilentlyContinue).CommandLine
            if ($cmdLine -and ($cmdLine -like "*smartrim.monitor*" -or $cmdLine -like "*monitor.py*")) {
                Write-Host "Stopping monitor (PID $pid)..." -ForegroundColor Cyan
                Stop-Process -Id $pid -Force -ErrorAction SilentlyContinue
                Write-Host "Monitor stopped" -ForegroundColor Green
                # Verify PID file still contains the same PID before removal
                $currentPid = [int](Get-Content $pidFile -ErrorAction SilentlyContinue)
                if ($currentPid -eq $pid) {
                    Remove-Item $pidFile -Force -ErrorAction SilentlyContinue
                }
                exit 0
            } else {
                Write-Host "ERROR: PID $pid exists but is not a SmartRim monitor" -ForegroundColor Red
                Remove-Item $pidFile -Force -ErrorAction SilentlyContinue
                exit 1
            }
        } else {
            Write-Host "Monitor is not running (stale PID file)" -ForegroundColor Yellow
        }
    } else {
        Write-Host "ERROR: Invalid PID in PID file: $pid" -ForegroundColor Red
        Remove-Item $pidFile -Force -ErrorAction SilentlyContinue
        exit 1
    }
    Remove-Item $pidFile -Force -ErrorAction SilentlyContinue
} else {
    Write-Host "Monitor is not running (no PID file)" -ForegroundColor Yellow
}

# Fallback: search for monitor processes by command line
$procs = Get-CimInstance Win32_Process -Filter "Name='python.exe'" |
    Where-Object { $_.CommandLine -like "*smartrim.monitor*" -or $_.CommandLine -like "*monitor.py*" }
if ($procs) {
    foreach ($proc in $procs) {
        Stop-Process -Id $proc.ProcessId -Force -ErrorAction SilentlyContinue
        Write-Host "Stopped monitor (PID $($proc.ProcessId))" -ForegroundColor Green
    }
}
