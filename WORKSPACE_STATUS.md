---
stand: 2025-11-07 19:13
update: Frontmatter sync (env-Doku zentralisiert); Sammel-Stand aktualisiert.
checks: keine
---

Workspace-Status
================

Überblick
---------

- Hinweis: „Grün“ gilt nur bis zur nächsten Abweichung/Unsicherheit – dann STOP, Rückfrage, weiter nach Freigabe. Details: `.github/copilot-instructions.md` → „Unklarheiten‑STOP (global, immer gültig)“.

- 2025-11-07 02:29: Tree-Snapshots aktualisiert (`workspace_tree_full.txt`, `workspace_tree.txt`, `workspace_tree_dirs.txt`) und entfernte Markdownlint-Overrides in `novapolis-rp/database-curated/staging/**` festgehalten; Staging‑Reports (Setext+Frontmatter) gelinted → PASS.
- 2025-11-07 06:30: Alle Markdownlint VS-Code-Tasks & Wrapper-Doku entfernt; Ausführung jetzt ausschließlich manuell via `npx --yes markdownlint-cli2` (Policy npx-only).
- 2025-11-07 02:10: markdownlint-cli2 repo-weit ausgeführt (367× MD003 offen); Skriptprüfung für Markdown-Ausgaben (Chat-Exporter, Reports, todo_gather) vorbereitet.
- 2025-11-07 01:39: TODO aktualisiert (Single-Repo-Reminder; Aufgaben zu Lint-Overrides, Staging-Reports, Metadata-Konsolidierung, Archiv-Ablage).
- 2025-11-07 01:27: Konfliktanalyse durchgeführt (Markdownlint-Overrides, Staging-Reports ohne Frontmatter, doppelte Metadata-Skripte, Chat-Router-Notiz). Maßnahmen in TODO/DONELOG erfasst.
- Mono-Repo bündelt `novapolis_agent`, `novapolis-rp`, `novapolis-dev`, `novapolis-sim`, gemeinsame Pakete unter `packages/`
- Produktiver Code liegt ausschließlich im Agent-Backend; RP-Workspace enthält weiterhin Daten, Workflows, Tools
- Root-Dokumente (`README.md`, `todo.root.md`, `WORKSPACE_STATUS.md`) wurden am 2025-11-02 synchronisiert und liefern Einstieg ohne Projektwechsel
- Kopilot-Anweisungen konsolidiert unter `.github/copilot-instructions.md`
- Struktur-Snapshots (`workspace_tree.txt`, `workspace_tree_dirs.txt`, `workspace_tree_full.txt`) am 2025-11-06 via Tasks `Workspace tree:*` regeneriert; nächste Prüfung Mitte November.
- PowerShell-Standard: Terminal-Profile & VS-Code-Tasks laufen jetzt über `pwsh` 7.5.4; Windows PowerShell bleibt nur noch Fallback.

Aktueller Arbeitsmodus
----------------------

- Modus: General (GPT‑5)
- STOP‑Gate: an (vor Code‑/kanon‑kritischen Aktionen explizite Bestätigung erforderlich)
- Erinnerungen: Wechselhinweise bei Code‑Triggern aktiv; „Bitte nicht erinnern“ schaltet Hinweise ab bis zur Reaktivierung

Health-Checks & Open Items
---------------------------

- Tests: 2025-10-31 – `pytest -q`, `pyright -p pyrightconfig.json`, `python -m mypy --config-file mypy.ini app scripts` im Agent-Projekt grün (keine neuen Läufe seitdem dokumentiert)
- TODO-Backlog: siehe `todo.root.md` (Stand 2025-11-07; Fokus Agent: RAG/Tool-Use/Policies, RP: Kurations-Pipeline & Canvas-Pflege, Skriptprüfung für Markdown-Ausgaben)
- Policies & Behaviour: maßgeblich `.github/copilot-instructions.md` (SSOT)
- Risiken kurz:
  - Verzeichnis-Bulk unter `outputs/` (LoRA-Runs) wächst; mittelfristig archivieren oder auslagern
  - RP-Datenpflege erfordert regelmäßigen Sync mit Memory-Bundle (seit 2025-11-02 aktualisiert, siehe `novapolis-rp/database-rp/00-admin/memory-bundle.md`)
  - Tree-Snapshots benötigen Refresh zur nächsten Inventur (letzter Stand 2025-10-31)
  - VS-Code-Settings: Nutzer-/Profil-Overrides entfernt, nur Root-Workspace-Config aktiv
  - VS Code Multi‑Root (temporär): Wrapper‑Tasks verhalten sich unzuverlässig (CWD/Quoting). Bis zur Bereinigung gilt: KEINE WRAPPER; Terminal ausschließlich manuell. Fallakte: `novapolis-dev/logs/open-case-terminal-multi-root-20251103.md`

Wichtige Artefakte & Logs
-------------------------

- DONELOGs: `novapolis_agent/docs/DONELOG.txt`, `novapolis-dev/docs/donelog.md`
- Changelog-Übersicht auf Root-Ebene: `DONELOG.md` (aktualisiert 2025-11-01)
- Auswertungen & Berichte: `novapolis_agent/eval/results/`, `novapolis_agent/scripts/reports/`
- Backups/Exports: `Backups/` (Release-Artefakte), `novapolis-rp/database-raw/99-exports/`
- VS-Code-Empfehlungen: `.vscode/extensions.json` bündelt Python-, Markdownlint-, Copilot-, GitLens- und PowerShell-Extensions
- Gitignore: `Fehleranalyse und Auditplan.pdf` sowie Godot-Editor-Binaries (`novapolis-sim/Godot_v*.exe`) als lokale Artefakte ausgeschlossen

- Struktur-Snapshot
-------------------

- Vollständiger Verzeichnisbaum: `workspace_tree_full.txt` (Stand 2025-11-07 02:29; Terminal `tree /A /F`)
- Arbeitsansicht: `workspace_tree.txt` (Stand 2025-11-07 02:29; Terminal `tree /A`) und kompaktes Verzeichnis-Listing `workspace_tree_dirs.txt` (Stand 2025-11-07 02:29; Script `scripts/update_workspace_tree_dirs.ps1`)
- Historische Agent-Dateiinventur: `novapolis_agent/WORKSPACE_INDEX.md`
- Für gezielte Suchen weiterhin `scripts/audit_workspace.py` nutzen (prüft Referenzen & Altlasten)

VS-Code-Erweiterungen
---------------------

- **Empfohlen (Workspace)**: `ms-python.python`, `ms-python.vscode-pylance`, `davidanson.vscode-markdownlint`, `github.copilot`, `github.copilot-chat`, `eamodio.gitlens`, `ms-vscode.powershell`
- **Zusätzliche lokale Installationen**: u. a. `donjayamanne.githistory`, GitHub-/Remote-/Containers-Tools sowie die .NET-Suite; bleiben optional und sind nicht als Workspace-Empfehlung erforderlich

Nächste Empfehlungen
--------------------

- Root-`.vscode` ist maßgeblich; optionale Ergänzungen (z. B. PowerShell-7-Tasks) bei Bedarf ergänzen
- Outputs/Checkpoints reviewen und aussortieren oder in Backups verschieben (LoRA-Zwischenstände)
- Regelmäßige Aktualisierung: `WORKSPACE_STATUS.md`, `workspace_tree_full.txt` und `workspace_tree_dirs.txt` gemeinsam mit `todo.root.md` pflegen (empfohlen bis Mitte November oder nach strukturellen Änderungen)

