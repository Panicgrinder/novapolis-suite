#!/usr/bin/env pwsh
# Purpose: Quick wrapper to run pytest -q for Agent tests with cwd set, per wrapper policy.
# Usage: pwsh -NoProfile -File scripts/run_pytest_quick.ps1

$ErrorActionPreference = 'Stop'

$root = Split-Path -Parent $PSScriptRoot
$python = Join-Path $root '.venv\Scripts\python.exe'
if (-not (Test-Path -LiteralPath $python)) { $python = 'python' }

$cwd = Join-Path $root 'novapolis_agent'
Set-Location $cwd

& $python -m pytest -q
exit $LASTEXITCODE
