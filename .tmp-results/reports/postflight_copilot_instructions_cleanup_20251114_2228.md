Meta: Modus=Postflight, Modell=GPT-5 mini, Arbeitsverzeichnis=F:\VS Code Workspace\Main, RepoRoot=F:\VS Code Workspace\Main, PSScriptRoot=F:\VS Code Workspace\Main\scripts, PSVersion=unknown, Aufruf=apply_patch (edit .github/copilot-instructions.md), SHA256=not-computed-here, STOP-Gate=aktiv, Wrapper-Policy=erfüllt, Wrapper-Guards=R-CTX:PASS|R-WRAP:PASS, Quellen=.github/copilot-instructions.md;.tmp-results/todo.cleaned.md;WORKSPACE_STATUS.md, Aktion=Bereinigung Inline `pwsh -Command` Empfehlung in SSOT (copilot-instructions.md)

Prüfung:
- markdownlint=not-run
- Frontmatter-Validator=not-run
- Lint/Types/Tests=not-run

Kurzbeschreibung:
- Entfernung der widersprüchlichen Inline-`pwsh -Command` Empfehlung aus `.github/copilot-instructions.md`.
- Ersetzt durch konsistente Wrapper-Empfehlung: `python scripts/run_checks_and_report.py` oder `pwsh -File <script.ps1>`.
- `WORKSPACE_STATUS.md` um einen Recent-Changes-Eintrag ergänzt.
- `.tmp-results/todo.cleaned.md` Frontmatter aktualisiert (Stand + Update).

Todos:
- offen=2 (Prüfe konsistente Hinweise in referenzierten Dateien; Commit & push Änderungen auf Feature-Branch)
- BeispielFix=Docs: replace inline `-Command` with wrapper guidance
- ReRun=markdownlint-cli2 --config .markdownlint-cli2.jsonc '**/*.md'
- Fällig=2025-11-15 09:00

Ende: Timestamp=2025-11-14 22:28
