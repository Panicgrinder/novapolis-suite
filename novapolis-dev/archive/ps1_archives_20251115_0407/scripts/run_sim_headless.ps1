---
archived: "true"
Timestamp: 2025-11-15 04:07
---
<#
Run the Novapolis Sim verifier headless (no editor window).

This script will:
- locate a Godot binary in `novapolis-sim` (common names)
- run the headless verifier script `res://scripts/verify_sim.gd` with `--headless`

Usage: pwsh -File .\scripts\run_sim_headless.ps1
#>

Set-StrictMode -Version Latest
$root = Resolve-Path -Path (Join-Path $PSScriptRoot "..")
$simDir = Join-Path $root "novapolis-sim"
$possible = @("Godot_v4.5.1-stable_win64.exe", "Godot_v4.5.1-stable_win64_console.exe", "Godot.exe")
$godot = $null
foreach ($name in $possible) {
    $candidate = Join-Path $simDir $name
    if (Test-Path $candidate) { $godot = $candidate; break }
}
if (-not $godot) {
    Write-Host "ERROR: Keine Godot-Binary unter $simDir gefunden. Bitte Godot Release Binary dort ablegen oder Pfad anpassen." -ForegroundColor Red
    exit 2
}
Write-Host "Using Godot: $godot"
$arg = "--path `"$simDir`" -s res://scripts/verify_sim.gd --headless"
Write-Host "Starting headless verifier..."
$proc = Start-Process -FilePath $godot -ArgumentList $arg -PassThru -NoNewWindow
$proc.WaitForExit()
$exit = $proc.ExitCode
Write-Host "Godot exited with code $exit"
exit $exit
