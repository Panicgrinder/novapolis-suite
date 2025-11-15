#!/usr/bin/env pwsh
# Requires: PowerShell 7+
# Purpose: Create/ensure root .venv and install dependencies (idempotent)
# Usage: pwsh -NoProfile -File scripts/setup_root_venv.ps1

[CmdletBinding()]
param(
    [switch] $Recreate
)

$ErrorActionPreference = 'Stop'

function Write-Info([string]$msg) { Write-Host "[setup_venv] $msg" -ForegroundColor Cyan }
function Write-Warn([string]$msg) { Write-Host "[setup_venv] WARN: $msg" -ForegroundColor Yellow }
function Write-Err([string]$msg) { Write-Host "[setup_venv] ERROR: $msg" -ForegroundColor Red }

$root = Split-Path -Parent $PSScriptRoot
Set-Location $root
$venvPath = Join-Path $root '.venv'
$venvPython = Join-Path $venvPath 'Scripts\python.exe'

Write-Info "Root: $root"
Write-Info "Venv: $venvPath"

if ($Recreate -and (Test-Path -LiteralPath $venvPath)) {
    Write-Warn "Recreate requested: removing existing .venv"
    Remove-Item -Recurse -Force -LiteralPath $venvPath
}

if (-not (Test-Path -LiteralPath $venvPath)) {
    Write-Info "Creating virtual environment (.venv)"
    & py -3 -m venv $venvPath
}

if (-not (Test-Path -LiteralPath $venvPython)) {
    Write-Err "python.exe not found in .venv (expected: $venvPython)"
    exit 1
}

Write-Info "Upgrading pip"
& $venvPython -m pip install --upgrade pip

Write-Info "Done."
