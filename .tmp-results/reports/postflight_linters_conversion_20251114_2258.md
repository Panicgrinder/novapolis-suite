Meta: Modus=Postflight, Modell=GPT-5 mini, Arbeitsverzeichnis=F:\VS Code Workspace\Main, RepoRoot=F:\VS Code Workspace\Main, PSScriptRoot=F:\VS Code Workspace\Main\scripts, PSVersion=7.5.4, Aufruf=Add Python wrappers for linters+format tasks and update `/.vscode/tasks.json`, SHA256s recorded below, STOP-Gate=aktiv, Wrapper-Policy=erfüllt, Wrapper-Guards=PfadCheck:PASS|StopGate:PASS, Quellen=scripts\checks_linters.ps1;scripts\task_wrappers\lint_ruff.ps1;scripts\task_wrappers\format_black.ps1;scripts\task_wrappers\fix_ruff.ps1;.vscode\tasks.json

Aktion: Neue Python-Wrapper angelegt (lint_ruff.py, format_black.py, fix_ruff.py, checks_linters.py) und `/.vscode/tasks.json` aktualisiert, damit Tasks die `.venv`-Python-Wrapper nutzen.

Prüfung:
- timestamp: 2025-11-14 22:58
- PSVersion: 7.5.4

Original PS1 SHA256s (zur Archivierung/reference):
- scripts\checks_linters.ps1: 161993CD85C43D92A960B87CAA08ACA1F383693FAC1D32E5F4C2A2F12DE839F9
- scripts\task_wrappers\lint_ruff.ps1: D84611C7B7B6A6AF3E4ACEFA09125CF269C62F53A55F7FA234B77F62BC79C556
- scripts\task_wrappers\format_black.ps1: 2BB64C8E7F39C75C35E47AD31D04400EA92FD9D6542838C5821285B6B0170682
- scripts\task_wrappers\fix_ruff.ps1: 4E4B7943AAAB7AE7CEDE8B26D808BA779F1FC0E3EE743D012A4B55CCC1268045

New Python wrapper SHA256s:
- scripts\task_wrappers\lint_ruff.py: 8D97ABE5CB352068D2056EB7A205117C923973AB418A311241627C76CF0DD2E1
- scripts\task_wrappers\format_black.py: 6067BDCE917F06E041F98E0FA436B82263B706187EB6BF88C094DEC7D0C88E20
- scripts\task_wrappers\fix_ruff.py: 86B5494C6FB9236994D79C73C91B1FD09A8BEED0064C2CFBDAA50AB4E45E711A
- scripts\task_wrappers\checks_linters.py: 50D7F6F58028BF31D62833EB8E2C123F441A11C97B05356C54B18FAAB0D7AD8C

Geänderte Dateien:
- .vscode\tasks.json (updated to call .venv Python wrappers)
- scripts\task_wrappers\lint_ruff.py (new)
- scripts\task_wrappers\format_black.py (new)
- scripts\task_wrappers\fix_ruff.py (new)
- scripts\task_wrappers\checks_linters.py (new)

Empfehlung: Führe `python scripts/run_checks_and_report.py` aus der Workspace-venv aus, um Lint/Typ/Tests-Status zu validieren (empfohlen nach Wrapper-Umstellungen).

Todos: offen=2 (Create PR; finalize aggregated Postflight + DONELOG)

Ende: Timestamp=2025-11-14 22:58
