param(
    [switch]$VerboseMode
)

$ErrorActionPreference = [System.Management.Automation.ActionPreference]::Stop
$script:dotSourced = ($MyInvocation.InvocationName -eq ".")
function Finish([int]$code) { $global:LASTEXITCODE = $code; if ($script:dotSourced) { if ($VerboseMode) { Write-Host "[lint:markdown] dot-sourced; returning code $code" -ForegroundColor Yellow }; return } else { exit $code } }

$workspaceRoot = (Resolve-Path (Join-Path $PSScriptRoot "..\..\..")).Path
$configPath = Join-Path $workspaceRoot ".markdownlint-cli2.jsonc"
$hasDocker = $null -ne (Get-Command docker -ErrorAction SilentlyContinue)

# Resolve node.exe (absolute) to avoid PATH issues
$nodeExe = $null
$cmdNode = Get-Command node -ErrorAction SilentlyContinue
if ($cmdNode) { $nodeExe = $cmdNode.Source }
if (-not $nodeExe -and (Test-Path "C:\\Program Files\\nodejs\\node.exe")) { $nodeExe = "C:\\Program Files\\nodejs\\node.exe" }
if (-not $nodeExe -and (Test-Path "C:\\Program Files (x86)\\nodejs\\node.exe")) { $nodeExe = "C:\\Program Files (x86)\\nodejs\\node.exe" }
# Per-user install (Node.js for current user)
if (-not $nodeExe -and $Env:LOCALAPPDATA) {
    $userNode = Join-Path $Env:LOCALAPPDATA "Programs\nodejs\node.exe"
    if (Test-Path $userNode) { $nodeExe = $userNode }
}

# Resolve npx command and npx-cli.js
$npxCmd = $null
$cmd = Get-Command npx -ErrorAction SilentlyContinue; if ($cmd) { $npxCmd = $cmd.Source }
if (-not $npxCmd -and (Test-Path "C:\\Program Files\\nodejs\\npx.cmd")) { $npxCmd = "C:\\Program Files\\nodejs\\npx.cmd" }
if (-not $npxCmd -and (Test-Path "C:\\Program Files (x86)\\nodejs\\npx.cmd")) { $npxCmd = "C:\\Program Files (x86)\\nodejs\\npx.cmd" }
# Per-user install
if (-not $npxCmd -and $Env:LOCALAPPDATA) {
    $userNpx = Join-Path $Env:LOCALAPPDATA "Programs\nodejs\npx.cmd"
    if (Test-Path $userNpx) { $npxCmd = $userNpx }
}
$npxCli = $null
if ($nodeExe) {
    $nodeDir = Split-Path $nodeExe -Parent
    $candidate = Join-Path $nodeDir "node_modules\\npm\\bin\\npx-cli.js"
    if (Test-Path $candidate) { $npxCli = $candidate }
}

# Also resolve npm.cmd for npm exec fallback (uses sibling node.exe)
$npmCmd = $null
$cmd = Get-Command npm -ErrorAction SilentlyContinue; if ($cmd) { $npmCmd = $cmd.Source }
if (-not $npmCmd -and (Test-Path "C:\\Program Files\\nodejs\\npm.cmd")) { $npmCmd = "C:\\Program Files\\nodejs\\npm.cmd" }
if (-not $npmCmd -and (Test-Path "C:\\Program Files (x86)\\nodejs\\npm.cmd")) { $npmCmd = "C:\\Program Files (x86)\\nodejs\\npm.cmd" }
if (-not $npmCmd -and $Env:LOCALAPPDATA) {
    $userNpm = Join-Path $Env:LOCALAPPDATA "Programs\nodejs\npm.cmd"
    if (Test-Path $userNpm) { $npmCmd = $userNpm }
}

$hasNode = [string]::IsNullOrWhiteSpace($nodeExe) -eq $false
$hasNpxCmd = [string]::IsNullOrWhiteSpace($npxCmd) -eq $false
$hasNpxCli = [string]::IsNullOrWhiteSpace($npxCli) -eq $false
$hasNpmCmd = [string]::IsNullOrWhiteSpace($npmCmd) -eq $false

# Status-/Log-Verzeichnis vorbereiten
$statusDir = Join-Path $workspaceRoot "coding\tools\validators\.last-run"
New-Item -ItemType Directory -Force -Path $statusDir | Out-Null
$statusTxt = Join-Path $statusDir "lint-markdown.txt"
$statusJson = Join-Path $statusDir "lint-markdown.json"

function Write-Status([bool]$ok, [int]$exitCode, [string]$runner, [string]$output) {
    try {
        # Textlog immer schreiben (überschreiben)
        $textOut = if ($null -ne $output) { $output } else { "" }
        Set-Content -Path $statusTxt -Value $textOut -Encoding UTF8 -Force
        # JSON-Status schreiben
        $payload = [ordered]@{
            tool = 'markdownlint-cli2'
            ok = $ok
            exitCode = $exitCode
            runner = $runner
            ts = (Get-Date).ToString('s')
            cwd = (Get-Location).Path
        }
        $json = $payload | ConvertTo-Json -Depth 5
        Set-Content -Path $statusJson -Value $json -Encoding UTF8 -Force
        if ($VerboseMode) { Write-Host "[lint:markdown] Status geschrieben → $statusJson" -ForegroundColor DarkCyan }
    }
    catch {
        Write-Host "[lint:markdown] WARN: Konnte Status-Dateien nicht schreiben: $($_.Exception.Message)" -ForegroundColor Yellow
    }
}

if ($VerboseMode) {
    Write-Host "Workspace: $workspaceRoot"
    Write-Host "Docker: $hasDocker, Node: $hasNode, npx.cmd: $hasNpxCmd, npx-cli.js: $hasNpxCli, npm.cmd: $hasNpmCmd"
    if ($hasNode) { Write-Host "node.exe: $nodeExe" }
    if ($hasNpxCmd) { Write-Host "npx.cmd: $npxCmd" }
    if ($hasNpxCli) { Write-Host "npx-cli.js: $npxCli" }
    if ($hasNpmCmd) { Write-Host "npm.cmd: $npmCmd" }
}

if ($hasDocker) {
    Write-Host "[lint:markdown] Running in Docker (node:20-alpine)" -ForegroundColor Cyan
    $out = & docker run --rm -v "${workspaceRoot}:/workdir" -w /workdir node:20-alpine sh -lc "npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc '**/*.md'" 2>&1
    $code = $LASTEXITCODE
    $out | ForEach-Object { Write-Host $_ }
    Write-Status ($code -eq 0) $code 'docker:npx' ($out -join [Environment]::NewLine)
    Finish $code
}
elseif ($hasNpmCmd) {
    # Prefer lokaler Install+direkter Node-Aufruf, um PATH vollständig zu umgehen
    Write-Host "[lint:markdown] Preparing local install (markdownlint-cli2)" -ForegroundColor Cyan
    $validatorsDir = (Join-Path $workspaceRoot "coding\tools\validators")
    Push-Location $validatorsDir
    # Installiere CLI und Default-Formatter ohne das Repo zu verändern (no-save)
    $inst = & $npmCmd install --no-audit --no-fund --no-save markdownlint-cli2 markdownlint-cli2-formatter-default 2>&1
    if ($LASTEXITCODE -ne 0) { $code = $LASTEXITCODE; Pop-Location; Write-Host ($inst -join [Environment]::NewLine); Write-Status $false $code 'npm:install' ($inst -join [Environment]::NewLine); Finish $code }
    # Ermittle Binärpfad aus package.json
    $pkgPath = Join-Path $validatorsDir "node_modules\markdownlint-cli2\package.json"
    if (-not (Test-Path $pkgPath)) { Write-Host "[lint:markdown] Konnte package.json von markdownlint-cli2 nicht finden." -ForegroundColor Red; $code = 1; Pop-Location; Finish $code }
    $pkg = Get-Content -Raw -Path $pkgPath | ConvertFrom-Json
    $binRel = $null
    if ($pkg.bin -is [string]) { $binRel = $pkg.bin }
    elseif ($pkg.bin -and $pkg.bin.PSObject.Properties.Name -contains 'markdownlint-cli2') { $binRel = $pkg.bin.'markdownlint-cli2' }
    if (-not $binRel) { Write-Host "[lint:markdown] Konnte Binärpfad in package.json nicht ermitteln." -ForegroundColor Red; $code = 1; Pop-Location; Finish $code }
    $binAbs = (Resolve-Path (Join-Path (Split-Path $pkgPath -Parent) $binRel)).Path
    # Ausführung vom Workspace-Root, damit Glob-Pfade stimmen
    Pop-Location
    Push-Location $workspaceRoot
    Write-Host "[lint:markdown] Running locally (node + installed bin)" -ForegroundColor Cyan
    $out = & $nodeExe $binAbs "--config" $configPath "**/*.md" 2>&1
    $code = $LASTEXITCODE
    $out | ForEach-Object { Write-Host $_ }
    Write-Status ($code -eq 0) $code 'node:local-bin' ($out -join [Environment]::NewLine)
    Pop-Location
    Finish $code
}
elseif ($hasNode -and $hasNpxCli) {
    Write-Host "[lint:markdown] Running locally (node + npx-cli.js)" -ForegroundColor Cyan
    Push-Location $workspaceRoot
    $out = & $nodeExe $npxCli --yes markdownlint-cli2 --config $configPath "**/*.md" 2>&1
    $code = $LASTEXITCODE
    $out | ForEach-Object { Write-Host $_ }
    Write-Status ($code -eq 0) $code 'node:npx-cli' ($out -join [Environment]::NewLine)
    Pop-Location
    Finish $code
}
elseif ($hasNpxCmd) {
    Write-Host "[lint:markdown] Running locally (npx.cmd)" -ForegroundColor Cyan
    $out = & $npxCmd --yes markdownlint-cli2 --config $configPath "**/*.md" 2>&1
    $code = $LASTEXITCODE
    $out | ForEach-Object { Write-Host $_ }
    Write-Status ($code -eq 0) $code 'npx:cmd' ($out -join [Environment]::NewLine)
    Finish $code
}
else {
    Write-Host "Voraussetzungen fehlen: Docker Desktop oder Node.js (npx). Optionen: 1) Dev Containers 2) Docker Desktop 3) Node.js LTS 4) CI-Lint via GitHub Action abwarten." -ForegroundColor Yellow
    Write-Status $false 1 'none' 'Prerequisites missing'
    Finish 1
}
