<# 
.SYNOPSIS
    Start the SmartRim reflex monitor.

.DESCRIPTION
    Starts the SmartRim reflex monitor (adviser on by default: pauses and logs advice).

.PARAMETER ObserveOnly
    Switch to run in observe-only mode (snapshots only, no pause, no advice).

.PARAMETER RunId
    Run identifier (default: current-run).

.EXAMPLE
    .\scripts\start_monitor.ps1
    # Starts the monitor in adviser-on mode.

.EXAMPLE
    .\scripts\start_monitor.ps1 -ObserveOnly
    # Starts the monitor in observe-only mode.
#>
[CmdletBinding()]
param(
    [switch]$ObserveOnly,
    [string]$RunId = "current-run"
)

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Definition
$repoRoot = Split-Path -Parent $scriptDir
Set-Location $repoRoot

$env:PYTHONPATH = "src" + [System.IO.Path]::PathSeparator + $env:PYTHONPATH
if ($RunId) { $env:RUN_ID = $RunId }

$args = @()
if ($ObserveOnly) { $args += "--observe-only" }

python -m smartrim.monitor @args
