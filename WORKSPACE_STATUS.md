# Workspace-Status (Stand 2025-10-31)

## Überblick

- Mono-Repo bündelt `novapolis_agent`, `novapolis-rp`, `novapolis-dev`, `novapolis-sim`, gemeinsame Pakete unter `packages/`
- Produkttiver Code liegt ausschließlich im Agent-Backend; RP-Workspace enthält nur noch Daten, Workflows, Tools
- Root-Dokumente (`README.md`, `TODO.md`, `WORKSPACE_STATUS.md`) liefern Einstieg ohne Projektwechsel
- Kopilot-Anweisungen konsolidiert unter `.github/copilot-instructions.md`

## Health-Checks & Open Items

- Tests: 2025-10-31 – `pytest -q`, `pyright -p pyrightconfig.json`, `python -m mypy --config-file mypy.ini app scripts` im Agent-Projekt grün
- TODO-Backlog: siehe `TODO.md` (Agent-Fokus auf RAG/Tool-Use, RP auf Kurations-Pipeline)
- Policies & Behaviour: maßgeblich `novapolis_agent/docs/AGENT_BEHAVIOR.md`, `novapolis-dev/docs/copilot-behavior.md`
- Risiken kurz:
  - Verzeichnis-Bulk unter `outputs/` (LoRA-Runs) wächst; mittelfristig archivieren oder auslagern
  - VS-Code Settings liegen projektweise verteilt; Root-Scoping für gemeinsame Instruktionen in Planung
  - RP-Datenpflege erfordert regelmäßigen Sync mit Memory-Bundle (siehe `novapolis-dev/docs/todo.md`)

## Wichtige Artefakte & Logs

- DONELOGs: `novapolis_agent/docs/DONELOG.txt`, `novapolis-dev/docs/donelog.md`
- Changelog-Übersicht auf Root-Ebene: `DONELOG.md`
- Auswertungen & Berichte: `novapolis_agent/eval/results/`, `novapolis_agent/scripts/reports/`
- Backups/Exports: `Backups/` (Release-Artefakte), `novapolis-rp/database-raw/99-exports/`

## Struktur-Snapshot

- Vollständiger Verzeichnisbaum: `workspace_tree_full.txt` (Backup-Snapshot, generiert am 2025-10-31 via `tree /A /F`)
- Arbeitsansicht: `workspace_tree.txt` (unverändert) und kompaktes Verzeichnis-Listing `workspace_tree_dirs.txt`
- Historische Agent-Dateiinventur: `novapolis_agent/WORKSPACE_INDEX.md`
- Für gezielte Suchen weiterhin `scripts/audit_workspace.py` nutzen (prüft Referenzen & Altlasten)

## Nächste Empfehlungen

- Root-`.vscode` planen, um gemeinsame Copilot-/Interpreter-Defaults zu setzen (Projekt-spezifische Tasks bleiben lokal)
- Outputs/Checkpoints reviewen und aussortieren oder in Backups verschieben (LoRA-Zwischenstände)
- Regelmäßige Aktualisierung: `WORKSPACE_STATUS.md`, `workspace_tree_full.txt` und `workspace_tree_dirs.txt` gemeinsam mit `TODO.md` pflegen (z. B. monatlich oder nach strukturellen Änderungen)
