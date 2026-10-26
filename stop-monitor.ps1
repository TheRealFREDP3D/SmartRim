# SmartRim Sidecar — Stop Reflex Monitor
# The monitor runs as `python -m smartrim.monitor`; match on that as well as the
# legacy `monitor.py` entrypoint so it can actually be stopped.
$procs = Get-CimInstance Win32_Process -Filter "Name='python.exe'" |
    Where-Object { $_.CommandLine -like "*smartrim.monitor*" -or $_.CommandLine -like "*monitor.py*" }
if (-not $procs) {
    Write-Host "No monitor process found" -ForegroundColor Yellow
    exit 0
}
foreach ($proc in $procs) {
    Stop-Process -Id $proc.ProcessId -Force -ErrorAction SilentlyContinue
    Write-Host "Stopped monitor (PID $($proc.ProcessId))" -ForegroundColor Green
}
Remove-Item "memory\monitor.pid" -Force -ErrorAction SilentlyContinue
