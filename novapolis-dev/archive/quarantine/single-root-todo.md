---
stand: 2026-02-21 04:15
update: Vollstaendig abgehakten Root-Aufgabenblock validiert und ins Root-Archiv verschoben.
checks: "npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-dev/archive/quarantine/single-root-todo.md' PASS (2026-02-17 03:26); & .\\.venv\\Scripts\\python.exe scripts\\check_frontmatter.py novapolis-dev/archive/quarantine/single-root-todo.md PASS (2026-02-17 03:26)"
archived: true
---
<!-- markdownlint-disable MD001 MD022 MD041 -->

Single Root TODO (Novapolis Suite) — Archivkopie
=================================

Dieses Dokument war die zentrale, lesefreundliche Übersicht über alle laufenden Arbeiten im Monorepo. Es liegt heute als Archivkopie unter `novapolis-dev/archive/quarantine/single-root-todo.md` (`archived: true`) vor; der historische Verlauf ist in den Root-/Modul-Archiven dokumentiert. Die fachlichen Single Sources of Truth (SSOT) bleiben in den Modul-TODOs unter `novapolis-dev/docs/` erhalten.

### Hinweise

- SSOT: Modul-TODOs bleiben maßgeblich. Diese Datei dient als komfortabler Root-Einstieg.
- Archivierung: Fertige Blöcke (alle [x]) bitte in die jeweiligen Modul-Archive unter `novapolis-dev/archive/` verschieben.
- Snapshot-Kopf: YAML-Frontmatter oben bei Änderungen aktualisieren (`stand`, `update`, `checks`).
- Lint: Markdownlint läuft repo-weit ausschließlich manuell via `npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc '**/*.md'` (keine VS Code Tasks oder Wrapper). Bei FAIL bitte minimalen Patch anwenden.
- Terminal/Pwsh: Standard ist PowerShell 7 (`pwsh`). Bei manuellen Aufrufen `-NoProfile` verwenden. Für komplexe/mehrachsige Abläufe bevorzugt Python-Wrapper nutzen (z. B. `& .\.venv\Scripts\python.exe scripts\<script>.py`); Details siehe `.github/copilot-instructions.md`.
- STOP-Hinweis: „Grün“ gilt nur bis zur nächsten Abweichung/Unsicherheit - dann STOP, Rückfrage, weiter nach Freigabe. Details: `.github/copilot-instructions.md` → Abschnitt „Unklarheiten-STOP (global, immer gültig)“.

### Kurzüberblick (Module & Quellen)

- Index: `novapolis-dev/docs/todo.index.md`
- Agent: `novapolis-dev/docs/todo.agent-board.md`
- Dev: `novapolis-dev/docs/todo.dev.md`
- RP: `novapolis-dev/docs/todo.rp.md`
- Sim: `novapolis-dev/docs/todo.sim.md`
- Root-Übersicht (ausführlich): `todo.root.md`

### Offene Aufgaben (Root - quer durchs Repo) - validiert archiviert

- Der vollstaendig abgehakte Block `Offene Aufgaben (Root - quer durchs Repo)` wurde inhaltlich nach `novapolis-dev/archive/todo.root.archive.md` verschoben.
- Verifikationsstand vor dem Verschieben (erneut geprueft):
  - Wrapper-/Snapshot-Policy weiter in Root-Governance dokumentiert.
  - Root-`.vscode` ist konsolidiert (`settings.json` als massgebliche Konfiguration).
  - Backups-/Manifest-Artefakte vorhanden: `Backups/AUDIT.md`, `Backups/README.md`, `Backups/manifest.v1.json`.
  - Zugehoerige Skripte vorhanden: `scripts/update_backups_manifest.py`, `scripts/rotate_backups.py`.


### Modul-Fokus (Auszüge) - validiert archiviert

- Der vollstaendig abgehakte Block `Modul-Fokus (Agent/Dev/RP/Sim)` wurde inhaltlich nach `novapolis-dev/archive/todo.root.archive.md` verschoben.
- Die lebenden SSOT-Boards bleiben unveraendert unter:
  - `novapolis-dev/docs/todo.agent-board.md`
  - `novapolis-dev/docs/todo.dev.md`
  - `novapolis-dev/docs/todo.rp.md`
  - `novapolis-dev/docs/todo.sim.md`

### Validierte Abschlusspakete (ins Root-Archiv verschoben)

- Der vollstaendig abgehakte Block `Monorepo Single Root - Umstellungsplan` (inkl. Etappen 0-5, Workflows, Pruef-/Release-Checks, Akzeptanzkriterien, VS-Code-Workspace und Konflikt-Konfigurationen) wurde inhaltlich nach `novapolis-dev/archive/todo.root.archive.md` verschoben.
- Verifikationsstand vor dem Verschieben (erneut geprueft):
  - nur Root-`.vscode` vorhanden (`settings.json`, `tasks.json`, `launch.json`),
  - keine Modul-Workflows unter `novapolis_agent/.github/workflows` oder `novapolis-rp/.github/workflows`,
  - Root-Workflows zentral unter `/.github/workflows/*.yml`,
  - keine aktive `*.code-workspace` im Workspace,
  - kein aktiver `novapolis_agent/.devcontainer/**`,
  - Root-`pyproject.toml` weiterhin tools-only.

Archiv-Hinweis: Archiviert am 2025-11-09, siehe Historie/Backups.

Postflight:
Meta: Modus=Postflight, Timestamp=2025-11-09 04:05
Regeln: IDs=R-WRAP,R-STOP,R-FM,R-LINT,R-SCAN,R-CTX,R-SEC,R-LOG,R-COV,R-IDX,R-COMM,R-RED,R-TODO,R-TIME,R-SAFE
Lint: PASS, verbleibend=none
Frontmatter: PASS
Checklist: PASS (closed=ALL, open=0)
Archiv-Move: OK → als Archivkopie in `novapolis-dev/archive/quarantine/single-root-todo.md` geführt; Root-Historie siehe `novapolis-dev/archive/todo.root.archive.md`



