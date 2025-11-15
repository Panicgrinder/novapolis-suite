---
archived: "true"
Timestamp: 2025-11-15 05:59
---

<#
Runs pytest with coverage using the workspace's root venv if available.
#>

# Derive workspace root from this script's location (scripts/ -> root)
$scriptDir = $PSScriptRoot
if (-not $scriptDir) { $scriptDir = Split-Path -Path $MyInvocation.MyCommand.Path -Parent }
$root = Split-Path -Path $scriptDir -Parent

# Determine Python interpreter (prefer root .venv)
$python = Join-Path -Path $root -ChildPath '.venv\Scripts\python.exe'
if (-not (Test-Path -LiteralPath $python)) { $python = 'python' }

& $python -m pytest -q
exit $LASTEXITCODE
