---
archived: "true"
Timestamp: 2025-11-15 04:07
---
param(
    [string]$WorkspaceRoot
)

$ErrorActionPreference = 'Stop'

if (-not $WorkspaceRoot) {
    $WorkspaceRoot = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
}

$workspace = Resolve-Path $WorkspaceRoot
Set-Location $workspace

$python = Join-Path $workspace '.venv\Scripts\python.exe'
if (-not (Test-Path -LiteralPath $python)) {
    $python = 'python'
}

& $python -m ruff check .
$ruffExit = $LASTEXITCODE

& $python -m black --check .
$blackExit = $LASTEXITCODE

if ($ruffExit -ne 0 -or $blackExit -ne 0) {
    exit 1
}

Write-Host 'Ruff and Black checks PASS'
