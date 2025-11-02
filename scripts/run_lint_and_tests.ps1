Param(
    [string]$PythonExec
)

$ErrorActionPreference = "Stop"

function Write-Status {
    param (
        [string]$Message
    )

    Write-Host $Message
}

$workspaceRoot = Split-Path -Parent $PSScriptRoot
if (-not $workspaceRoot) {
    $workspaceRoot = Get-Location
}

Write-Host "==> Running markdownlint (all md)" -ForegroundColor Cyan
Push-Location -LiteralPath $workspaceRoot
& npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc "**/*.md"
$lintExit = $LASTEXITCODE
Pop-Location

if ($lintExit -ne 0) {
    Write-Status "STATUS: LINT=FAIL ERRORS=$lintExit"
    Write-Status "STATUS: SUITE=FAIL"
    exit $lintExit
}

Write-Status "STATUS: LINT=PASS"

$pythonExec = $PythonExec
if ([string]::IsNullOrWhiteSpace($pythonExec)) {
    $pythonExec = $env:PYTHON_EXEC
}
if ([string]::IsNullOrWhiteSpace($pythonExec)) {
    $pythonExec = "python"
}

$pytestArgs = @("-m", "pytest", "-q")
$pytestCwd = Join-Path $workspaceRoot "novapolis_agent"

Write-Host "==> Running pytest (-q)" -ForegroundColor Cyan
Push-Location -LiteralPath $pytestCwd
& $pythonExec @pytestArgs
$pytestExit = $LASTEXITCODE
Pop-Location

if ($pytestExit -ne 0) {
    Write-Status "STATUS: TESTS=FAIL ERRORS=$pytestExit"
    Write-Status "STATUS: SUITE=FAIL"
    exit $pytestExit
}

Write-Status "STATUS: TESTS=PASS"
Write-Status "STATUS: SUITE=PASS"
exit 0
