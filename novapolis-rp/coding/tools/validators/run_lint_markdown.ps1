Write-Host "run_lint_markdown.ps1 ist veraltet." -ForegroundColor Yellow
Write-Host "Bitte nutze stattdessen: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc '**/*.md'" -ForegroundColor Yellow
exit 1
