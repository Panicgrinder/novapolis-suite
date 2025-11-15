---
archived: "true"
Timestamp: 2025-11-15 05:59
---

param()

$ErrorActionPreference = 'Stop'
$root = Split-Path -Path $PSScriptRoot -Parent
$agent = Join-Path $root "novapolis_agent"
Set-Location $agent

$pyright = Join-Path $root ".venv\Scripts\pyright.exe"
if (-not (Test-Path -LiteralPath $pyright)) { $pyright = 'pyright' }
& $pyright -p pyrightconfig.json
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

$python = Join-Path $root ".venv\Scripts\python.exe"
if (-not (Test-Path -LiteralPath $python)) { $python = 'python' }
& $python -m mypy --config-file mypy.ini app scripts
exit $LASTEXITCODE
