Meta: Modus=Postflight, Modell=GPT-5 mini, Arbeitsverzeichnis=F:\VS Code Workspace\Main, RepoRoot=F:\VS Code Workspace\Main, PSScriptRoot=F:\VS Code Workspace\Main\scripts, PSVersion=7.5.4, Aufruf=archive .vscode/tasks.json + patch .vscode/tasks.json -> replace selected ps1 invocations with Python wrappers under .venv, SHA256s below, STOP-Gate=aktiv, Wrapper-Policy=erfüllt, Wrapper-Guards=PfadCheck:PASS|StopGate:PASS, Quellen=.github/copilot-instructions.md;.vscode/tasks.json;githooks/pre-commit;novapolis-dev/archive/tasks_archive_20251114_tasks.json

Aktion: Archiviert und aktualisiert `/.vscode/tasks.json` — zwei Tasks auf Python-Wrapper umgestellt (`Tests: coverage (fail-under)`, `Workspace tree: summary (dirs)`). Archivpfad: `novapolis-dev/archive/tasks_archive_20251114_tasks.json`.

Prüfung:
- timestamp: 2025-11-14 22:56
- PSVersion: 7.5.4
- SHA256(`.vscode/tasks.json`): ECC75E648119A2E3C9A53A7698C65AF72E4FDC9CBCEBC1F6DD97733CDF8DD968
- SHA256(`novapolis-dev/archive/tasks_archive_20251114_tasks.json`): 45B2B54D3EDE7861734F47184EF9C56B54A2ABA9216B2F533EB7EE59687DDCF4

Guards & Regeln:
- R-WRAP (Wrapper-Policy): erfüllt — neue Tasks rufen `.venv` Python-Wrapper auf
- R-STOP (STOP-Gate): aktiv — Änderungen wurden nur für safe subset vorgenommen; Archiv angelegt
- R-FM (Frontmatter-Policy): nicht betroffen
- R-LINT: not-run (Task mutations only); recommend running `python scripts/run_checks_and_report.py` to revalidate repo state

Geänderte Dateien:
- `.vscode/tasks.json` (updated)
- `novapolis-dev/archive/tasks_archive_20251114_tasks.json` (archived original)

Todos (nach Postflight):
- offen=2 (Create PR for branch; Update aggregated Postflight receipts + DONELOG)

Ende: Timestamp=2025-11-14 22:56
