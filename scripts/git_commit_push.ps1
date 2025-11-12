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

function Confirm-ExpectedInput {
    param (
        [string]$Prompt,
        [string]$Expected
    )

    $response = Read-Host $Prompt
    if ($response -ne $Expected) {
        Write-Host "Abbruch: Eingabe '$Expected' nicht bestätigt." -ForegroundColor Yellow
        exit 1
    }
}

Write-Host "STOP: Git commit+push Task gestartet." -ForegroundColor Yellow
Write-Host "Gib 'START' ein, um die Sequenz zu beginnen, ansonsten wird abgebrochen." -ForegroundColor Yellow

Confirm-ExpectedInput -Prompt "STOP‑Gate Eingabe" -Expected "START"

Write-Host ""  # leere Zeile

Invoke-GitCommand -Arguments @("status", "--short", "--branch") -Label "PLAN"
$statusLines = git status --porcelain
if (-not $statusLines) {
    Write-Host "Keine Änderungen gefunden. Vorgang beendet." -ForegroundColor Yellow
    exit 1
}

Write-Host ""  # leere Zeile
$proceedDry = Read-Host "Weiter zum DRY RUN? (yes/no)"
if ($proceedDry.ToLowerInvariant() -ne "yes") {
    Write-Host "Abbruch vor DRY RUN." -ForegroundColor Yellow
    exit 1
}

Invoke-GitCommand -Arguments @("add", "--all", "--dry-run") -Label "DRY RUN"

Write-Host ""  # leere Zeile
$commitMessage = Read-Host "Commit-Message"
while ([string]::IsNullOrWhiteSpace($commitMessage)) {
    $commitMessage = Read-Host "Commit-Message (nicht leer)"
}

Confirm-ExpectedInput -Prompt "Tippe 'PROCEED TO APPLY' um fortzufahren" -Expected "PROCEED TO APPLY"

Invoke-GitCommand -Arguments @("add", "--all") -Label "APPLY"
Invoke-GitCommand -Arguments @("commit", "-m", $commitMessage) -Label "APPLY"
Invoke-GitCommand -Arguments @("push") -Label "APPLY"

Invoke-GitCommand -Arguments @("status", "--short", "--branch") -Label "VERIFY"

Write-Host "Git commit+push Task abgeschlossen." -ForegroundColor Green

