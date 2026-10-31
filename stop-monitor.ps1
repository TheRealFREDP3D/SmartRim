# SmartRim Sidecar - Stop Reflex Monitor
$pidFile = "memory\monitor.pid"

if (Test-Path $pidFile) {
    $monitorPid = [int](Get-Content $pidFile -ErrorAction SilentlyContinue)
    if ($monitorPid -gt 0) {
        $proc = Get-Process -Id $monitorPid -ErrorAction SilentlyContinue
        if ($proc) {
            $cmdLine = (Get-WmiObject Win32_Process -Filter "ProcessId = $monitorPid" -ErrorAction SilentlyContinue).CommandLine
            if ($cmdLine -and ($cmdLine -like "*smartrim.monitor*" -or $cmdLine -like "*monitor.py*")) {
                Write-Host "Stopping monitor (PID $monitorPid)..." -ForegroundColor Cyan
                Stop-Process -Id $monitorPid -Force -ErrorAction SilentlyContinue
                Write-Host "Monitor stopped" -ForegroundColor Green
                $currentPid = [int](Get-Content $pidFile -ErrorAction SilentlyContinue)
                if ($currentPid -eq $monitorPid) {
                    Remove-Item $pidFile -Force -ErrorAction SilentlyContinue
                }
                exit 0
            } else {
                Write-Host "ERROR: PID $monitorPid exists but is not a SmartRim monitor" -ForegroundColor Red
                Remove-Item $pidFile -Force -ErrorAction SilentlyContinue
                exit 1
            }
        } else {
            Write-Host "Monitor is not running (stale PID file)" -ForegroundColor Yellow
        }
    } else {
        Write-Host "ERROR: Invalid PID in PID file: $monitorPid" -ForegroundColor Red
        Remove-Item $pidFile -Force -ErrorAction SilentlyContinue
        exit 1
    }
    Remove-Item $pidFile -Force -ErrorAction SilentlyContinue
} else {
    Write-Host "Monitor is not running (no PID file)" -ForegroundColor Yellow
}

$procs = Get-CimInstance Win32_Process -Filter "Name='python.exe'" |
    Where-Object { $_.CommandLine -like "*smartrim.monitor*" -or $_.CommandLine -like "*monitor.py*" }
if ($procs) {
    foreach ($proc in $procs) {
        Stop-Process -Id $proc.ProcessId -Force -ErrorAction SilentlyContinue
        Write-Host "Stopped monitor (PID $($proc.ProcessId))" -ForegroundColor Green
    }
}