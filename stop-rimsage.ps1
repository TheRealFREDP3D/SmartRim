# Stop RimSage MCP Server

$pidFile = "C:\Users\fred\Desktop\RimSage\rimsage.pid"

if (Test-Path $pidFile) {
    $pid = Get-Content $pidFile
    $process = Get-Process -Id $pid -ErrorAction SilentlyContinue

    if ($process) {
        Write-Host "Stopping RimSage (PID: $pid)..."
        Stop-Process -Id $pid -Force
        Remove-Item $pidFile
        Write-Host "RimSage stopped"
    } else {
        Write-Host "RimSage process not found, cleaning up PID file"
        Remove-Item $pidFile
    }
} else {
    Write-Host "RimSage PID file not found - may not be running"
}
