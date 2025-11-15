---
archived: "true"
Timestamp: 2025-11-15 04:07
---
param()

$ErrorActionPreference = 'Stop'
$root = Split-Path -Path $PSScriptRoot -Parent
Set-Location $root

$python = Join-Path $root ".venv\Scripts\python.exe"
if (-not (Test-Path -LiteralPath $python)) { $python = 'python' }
& $python -m pytest -q
exit $LASTEXITCODE
