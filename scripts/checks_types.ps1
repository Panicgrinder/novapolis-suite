$ErrorActionPreference = 'Stop'

$repoRoot = Split-Path -Parent $PSScriptRoot
$agentRoot = Join-Path $repoRoot 'novapolis_agent'
Set-Location -LiteralPath $agentRoot

$pyright = Join-Path $repoRoot '.venv\Scripts\pyright.exe'
if (-not (Test-Path -LiteralPath $pyright)) {
    $pyright = 'pyright'
}

& $pyright -p pyrightconfig.json
if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}

$python = Join-Path $repoRoot '.venv\Scripts\python.exe'
if (-not (Test-Path -LiteralPath $python)) {
    $python = 'python'
}

& $python -m mypy --config-file mypy.ini app scripts utils
exit $LASTEXITCODE
