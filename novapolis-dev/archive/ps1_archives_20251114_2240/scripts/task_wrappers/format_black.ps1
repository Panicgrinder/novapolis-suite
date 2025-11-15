---
archived: "true"
Timestamp: 2025-11-15 05:59
---

param()
$ErrorActionPreference = 'Stop'
$root = (Get-Location).Path
$python = Join-Path $root '.venv\Scripts\python.exe'
if (-not (Test-Path -LiteralPath $python)) { $python = 'python' }
& $python -m black .
exit $LASTEXITCODE
