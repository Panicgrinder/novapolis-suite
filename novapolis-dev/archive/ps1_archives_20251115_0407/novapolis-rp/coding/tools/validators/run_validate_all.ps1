---
archived: "true"
Timestamp: 2025-11-15 04:07
---
param(
    [switch]$VerboseMode
)

$ErrorActionPreference = [System.Management.Automation.ActionPreference]::Stop
$script:dotSourced = ($MyInvocation.InvocationName -eq ".")
function Finish([int]$code) { $global:LASTEXITCODE = $code; if ($script:dotSourced) { if ($VerboseMode) { Write-Host "[validate] dot-sourced; returning code $code" -ForegroundColor Yellow }; return } else { exit $code } }

$workspaceRoot = (Resolve-Path (Join-Path $PSScriptRoot "..\..\..")).Path
$hasDocker = $null -ne (Get-Command docker -ErrorAction SilentlyContinue)
$nodeExe = $null
$cmdNode = Get-Command node -ErrorAction SilentlyContinue
if ($cmdNode) { $nodeExe = $cmdNode.Source }
if (-not $nodeExe -and (Test-Path "C:\\Program Files\\nodejs\\node.exe")) { $nodeExe = "C:\\Program Files\\nodejs\\node.exe" }
if (-not $nodeExe -and (Test-Path "C:\\Program Files (x86)\\nodejs\\node.exe")) { $nodeExe = "C:\\Program Files (x86)\\nodejs\\node.exe" }
$npmCmd = $null
$cmd = Get-Command npm -ErrorAction SilentlyContinue
if ($cmd) { $npmCmd = $cmd.Source }
if (-not $npmCmd -and (Test-Path "C:\\Program Files\\nodejs\\npm.cmd")) { $npmCmd = "C:\\Program Files\\nodejs\\npm.cmd" }
if (-not $npmCmd -and (Test-Path "C:\\Program Files (x86)\\nodejs\\npm.cmd")) { $npmCmd = "C:\\Program Files (x86)\\nodejs\\npm.cmd" }
$hasNpm    = [string]::IsNullOrWhiteSpace($npmCmd) -eq $false

if ($VerboseMode) { Write-Host "Workspace: $workspaceRoot"; Write-Host "Docker: $hasDocker, Npm: $hasNpm" }

if ($hasDocker) {
    Write-Host "[validate] Running in Docker (node:22-alpine)" -ForegroundColor Cyan
    & docker run --rm -v "${workspaceRoot}:/workdir" -w /workdir node:22-alpine sh -lc "npm ci --prefix coding/tools/validators && npm --prefix coding/tools/validators run validate"
    Finish $LASTEXITCODE
}
elseif ($hasNpm) {
    Write-Host "[validate] Running locally (npm)" -ForegroundColor Cyan
    Push-Location (Join-Path $workspaceRoot "coding\tools\validators")
    & $npmCmd ci
    if ($LASTEXITCODE -ne 0) {
        Write-Host "[validate] npm ci failed (likely missing package-lock). Falling back to npm install..." -ForegroundColor Yellow
        & $npmCmd install --no-audit --no-fund
        if ($LASTEXITCODE -ne 0) { Pop-Location; Finish $LASTEXITCODE; return }
    }
    # Dependencies are installed; switch to workspace root for validation runs
    Pop-Location
    Push-Location $workspaceRoot
    & $nodeExe "coding/tools/validators/src/validate-curated.js"
    if ($LASTEXITCODE -ne 0) { $code = $LASTEXITCODE; Pop-Location; Finish $code; return }
    & $nodeExe "coding/tools/validators/src/validate-rp.js"
    if ($LASTEXITCODE -ne 0) { $code = $LASTEXITCODE; Pop-Location; Finish $code; return }
    & $nodeExe "coding/tools/validators/src/check-crossrefs.js"
    $code = $LASTEXITCODE
    Pop-Location
    if ($code -ne 0) { Finish $code } else { Finish 0 }
}
else {
    Write-Host "Voraussetzungen fehlen: Docker Desktop oder Node.js (npm). Optionen: 1) Dev Containers 2) Docker Desktop 3) Node.js LTS" -ForegroundColor Yellow
    Finish 1
}
