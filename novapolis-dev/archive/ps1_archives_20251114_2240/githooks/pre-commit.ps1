# PowerShell body for the Git pre-commit hook.
# This script contains the checks previously inlined via -Command in the shell hook.
$ErrorActionPreference = 'Stop'

try {
    & 'scripts/snapshot_gate.ps1'
    if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

    $stagedAll = git diff --cached --name-only --diff-filter=ACMRT
    if (-not $stagedAll) { exit 0 }

    $needsDoneLog = $stagedAll | Where-Object { $_ -match '^novapolis_agent/(app|scripts|utils)/' }
    if ($needsDoneLog) {
      $doneLogPath = 'novapolis_agent/docs/DONELOG.txt'
      if (-not (Test-Path -LiteralPath $doneLogPath)) {
        Write-Error "[pre-commit] Erwartete Datei $doneLogPath fehlt."; exit 1 }
      $year = (Get-Date).ToString('yyyy')
      if (-not (Select-String -Path $doneLogPath -SimpleMatch $year -Quiet)) {
        Write-Error '[pre-commit] DONELOG-Eintrag für dieses Jahr fehlt. Bitte aktualisieren.'; exit 1 }
    }

    $stagedMd = $stagedAll | Where-Object { $_ -match '\.md$' }
    if ($stagedMd) {
      if (Get-Command npx -ErrorAction SilentlyContinue) {
        $mdArgs = @('--config', '.markdownlint-cli2.jsonc') + $stagedMd
        & npx --yes markdownlint-cli2 @mdArgs
        if ($LASTEXITCODE -ne 0) {
          Write-Warning '[pre-commit] markdownlint-cli2 meldet Probleme. Versuche automatische Korrektur.'
          & npx --yes markdownlint-cli2-fix @mdArgs
          if ($LASTEXITCODE -eq 0) {
            git add $stagedMd | Out-Null
            Write-Error '[pre-commit] Markdownlint-Fix angewendet. Bitte Änderungen prüfen und erneut committen.'
          } else {
            Write-Error '[pre-commit] markdownlint-cli2 konnte nicht automatisch reparieren. Bitte manuell beheben.'
          }
          exit 1
        }
      } else {
        Write-Warning '[pre-commit] npx nicht gefunden. Überspringe markdownlint-cli2. Bitte manuell prüfen.'
      }
    }

    if (-not $stagedMd -or $stagedMd.Count -eq 0) { Write-Host '[pre-commit] Keine Markdown-Dateien im Commit. Frontmatter-Check übersprungen.'; exit 0 }
    $root = (Get-Location).Path; $py = Join-Path $root '.venv\Scripts\python.exe'; if (-not (Test-Path -LiteralPath $py)) { $py = 'python' }
    & $py 'scripts/check_frontmatter.py' @stagedMd; exit $LASTEXITCODE
}
catch {
  Write-Error $_.Exception.Message
  exit 1
}
