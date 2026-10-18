# RimWorld Counselor Sidecar — Stop Reflex Monitor
$procs = Get-CimInstance Win32_Process -Filter "Name='python.exe'" |
    Where-Object { $_.CommandLine -like "*monitor.py*" }
if (-not $procs) {
    Write-Host "No monitor process found" -ForegroundColor Yellow
    exit 0
}
foreach ($proc in $procs) {
    Stop-Process -Id $proc.ProcessId -Force
    Write-Host "Stopped monitor (PID $($proc.ProcessId))" -ForegroundColor Green
}
