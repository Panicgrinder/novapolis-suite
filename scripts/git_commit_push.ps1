param(
    [string]$Message = ""
)

$ErrorActionPreference = "Stop"

function Invoke-GitCommand {
    param (
        [string[]]$Arguments,
        [string]$Label
    )

    if ($Label) {
        Write-Host "[$Label] git $($Arguments -join ' ')" -ForegroundColor Cyan
    } else {
        Write-Host "git $($Arguments -join ' ')" -ForegroundColor Cyan
    }

    & git @Arguments
    $exitCode = $LASTEXITCODE
    if ($exitCode -ne 0) {
        Write-Host "Command failed with exit code $exitCode." -ForegroundColor Red
        exit $exitCode
    }
}

Write-Host "Git commit+push (non-interactive) gestartet." -ForegroundColor Yellow

Invoke-GitCommand -Arguments @("status", "--short", "--branch") -Label "PLAN"

$statusLines = git status --porcelain
if (-not $statusLines) {
    Write-Host "Keine Änderungen gefunden. Vorgang beendet." -ForegroundColor Yellow
    exit 1
}

Write-Host ""  # leere Zeile
Invoke-GitCommand -Arguments @("add", "--all", "--dry-run") -Label "DRY RUN"

Write-Host ""  # leere Zeile
if ([string]::IsNullOrWhiteSpace($Message)) {
    $Message = "chore(rp): database-rp consistency fixes"
}
Write-Host "Commit-Message: $Message" -ForegroundColor Cyan

Invoke-GitCommand -Arguments @("add", "--all") -Label "APPLY"

# Commit can fail if nothing to commit (race) – handle gracefully.
& git commit -m $Message
$commitExit = $LASTEXITCODE
if ($commitExit -ne 0) {
    Write-Host "Commit fehlgeschlagen (Exit $commitExit)." -ForegroundColor Red
    exit $commitExit
}

# Push: if upstream missing, set it.
$hasUpstream = $true
try {
    & git rev-parse --abbrev-ref --symbolic-full-name "@{u}" *> $null
    if ($LASTEXITCODE -ne 0) { $hasUpstream = $false }
} catch {
    $hasUpstream = $false
}

if ($hasUpstream) {
    Invoke-GitCommand -Arguments @("push") -Label "APPLY"
} else {
    Invoke-GitCommand -Arguments @("push", "-u", "origin", "HEAD") -Label "APPLY"
}

Invoke-GitCommand -Arguments @("status", "--short", "--branch") -Label "VERIFY"

Write-Host "Git commit+push abgeschlossen." -ForegroundColor Green
