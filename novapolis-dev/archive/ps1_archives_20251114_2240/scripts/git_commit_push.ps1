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
