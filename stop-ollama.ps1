# Stop the Ollama server process.
$ErrorActionPreference = "SilentlyContinue"
$procs = Get-Process -Name "ollama" -ErrorAction SilentlyContinue
if ($procs) {
    $procs | Stop-Process -Force
    Write-Host "Stopped Ollama server (PID: $($procs.Id -join ', '))" -ForegroundColor Green
} else {
    Write-Host "No Ollama server process running" -ForegroundColor Yellow
}