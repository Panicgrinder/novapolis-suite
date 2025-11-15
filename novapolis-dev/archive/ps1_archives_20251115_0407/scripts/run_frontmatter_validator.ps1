---
archived: "true"
Timestamp: 2025-11-15 04:07
---
param(
    [string[]]$Paths
)

$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $PSScriptRoot
Set-Location -LiteralPath $root

$python = Join-Path -Path $root -ChildPath '.venv\Scripts\python.exe'
if (-not (Test-Path -LiteralPath $python)) {
    $python = 'python'
}

$scriptPath = Join-Path -Path $root -ChildPath 'scripts\check_frontmatter.py'
$arguments = @($scriptPath)
if ($Paths -and $Paths.Count -gt 0) {
    $arguments += $Paths
}

& $python @arguments
exit $LASTEXITCODE
