# SmartRim — Optimal Ollama Server Launcher
# Applies tuned env vars and starts `ollama serve` if not already running.
# Usage: .\start-ollama.ps1

$ErrorActionPreference = "Stop"

$ollamaExe = "C:\Users\fred\AppData\Local\Programs\Ollama\ollama.exe"
if (-not (Test-Path $ollamaExe)) {
    $cmd = Get-Command ollama -ErrorAction SilentlyContinue
    if ($cmd) { $ollamaExe = $cmd.Source } else { throw "ollama.exe not found" }
}

# Tuned for: GTX 1050 Ti 4GB VRAM, 32GB RAM, i7-6700K
$env:OLLAMA_HOST            = "127.0.0.1:11434"
$env:OLLAMA_MODELS          = "D:\BACKUP\MODELS"
$env:OLLAMA_FLASH_ATTENTION = "1"
$env:OLLAMA_KV_CACHE_TYPE   = "q8_0"   # ~2x KV memory savings vs f16
$env:OLLAMA_NUM_PARALLEL    = "1"      # single user, avoid VRAM split
$env:OLLAMA_MAX_LOADED_MODELS = "2"    # chat + embedder
$env:OLLAMA_KEEP_ALIVE      = "30m"    # keep model hot
$env:OLLAMA_NUM_GPU         = "999"    # offload max layers
$env:OLLAMA_ORIGINS         = "*"
$env:OLLAMA_DEBUG           = "1"

$healthUrl = "http://127.0.0.1:11434/api/version"

# Check if server already up
$up = $false
try {
    $v = Invoke-RestMethod -Uri $healthUrl -TimeoutSec 3
    if ($v.version) { $up = $true }
} catch { $up = $false }

if ($up) {
    Write-Host "Ollama server already running: $($v.version)" -ForegroundColor Green
} else {
    Write-Host "Starting Ollama server with tuned env..." -ForegroundColor Cyan
    $outLog = Join-Path $env:TEMP "ollama-serve.out.log"
    $errLog = Join-Path $env:TEMP "ollama-serve.err.log"
    Remove-Item $outLog, $errLog -ErrorAction SilentlyContinue
    $proc = Start-Process -FilePath $ollamaExe -ArgumentList "serve" -RedirectStandardOutput $outLog -RedirectStandardError $errLog -PassThru -WindowStyle Hidden

    # wait for readiness (GPU discovery can take a few seconds)
    for ($i = 0; $i -lt 40; $i++) {
        Start-Sleep -Milliseconds 500
        if ($proc.HasExited) {
            $err = if (Test-Path $errLog) { Get-Content $errLog -Raw } else { "" }
            throw "Ollama process exited before ready. stderr:`n$err"
        }
        try {
            $v = Invoke-RestMethod -Uri $healthUrl -TimeoutSec 2
            if ($v.version) { $up = $true; break }
        } catch { }
    }
    if (-not $up) {
        $err = if (Test-Path $errLog) { Get-Content $errLog -Raw } else { "" }
        throw "Ollama server did not become ready. stderr:`n$err"
    }
    Write-Host "Ollama server started: $($v.version)" -ForegroundColor Green
}

Write-Host ""
Write-Host "Recommended model: gemma4-e2b-rimworld (gemma-4-E2B tuned, 8k ctx, temp 0.2) - best speed/quality" -ForegroundColor Cyan
Write-Host "  Quality option: qwen3-rimworld (5 tok/s)   Speed option: llama3.2:1b-instruct-q4_K_M (41 tok/s)"
Write-Host ""
Write-Host "Env applied (user-level persisted already):"
Write-Host "  FLASH_ATTENTION=1  KV_CACHE=q8_0  PARALLEL=1  KEEP_ALIVE=30m  MAX_LOADED=2"
Write-Host "Verify with: ollama ps  (after a request)"