---
stand: 2025-11-16 00:19
update: Frontmatter-Autofix + --touch dokumentiert
checks: python scripts/check_frontmatter.py PASS
---

Recent Changes
--------------

- 2025-11-15 09:27: Frontmatter-Autofix + `--touch` (Stand-Aktualisierung) in `scripts/check_frontmatter.py` ergänzt; Governance-Referenzblock erweitert; Validator PASS (`python scripts/check_frontmatter.py`).
- 2025-11-15 09:20: Dokumentationssweep (context.local.md Frontmatter repariert, todo/Status/Index aktualisiert); Frontmatter-Validator PASS (`python scripts/check_frontmatter.py`).
- 2025-11-15 09:00: Dokumentationssweep (context.local.md Frontmatter repariert, todo/Status/Index aktualisiert); Frontmatter-Validator PASS (`python scripts/check_frontmatter.py`).
- 2025-11-12 03:37: Checks: full Review abgeschlossen (damals PowerShell-Runner, inzwischen durch `python scripts/run_checks_and_report.py` ersetzt; PSScriptAnalyzer-Phase verifiziert, Receipt-Struktur JSON + Postflight-Vorlage bestätigt). Link-Scanner Rescan nun 0 defekte Verweise.
- 2025-11-12 02:46: Governance: Vorangestellte Start-Checks entfernt aus `.github/copilot-instructions.md`; Postflight-Formulierung präzisiert (finaler Block am Ende der Nachricht); Headings-Extrakt aktualisiert & veraltete Regel-ID-Vorschläge gestrichen; Lint PASS (`.github/copilot-instructions-headings.md`).

 - 2025-11-10 12:12: Sim-Verifizierung: Verbindung Godot ↔ Agent (`POST /world/step`) erfolgreich verifiziert; Headless-Verifier und PowerShell-Smoke-Test PASS. Screenshot/Audit-Beleg im Arbeitsverzeichnis erstellt.
 - 2025-11-11 00:09: Dokumentation: Review des damaligen PowerShell-Checks-Wrappers ergänzt; ToDo für Status-Fix (STOP -> FAIL) eingetragen; zugehörige Doku-Änderungen committet. Seit 2025-11-12 ist `python scripts/run_checks_and_report.py` der einzige Entry-Point.
 - 2025-11-11 00:23: Code: PowerShell-Wrapper angepasst (STOP-Fall jetzt als FAIL; STOP-Flag in Regel-Output; robustere Postflight/Exitcodes). Änderung inzwischen in die Python-Variante übernommen (Commit `abe6829`).
 - 2025-11-11 11:00: Code: PowerShell-Wrapper um `PSScriptAnalyzer`-Integration erweitert; Erkenntnisse in die Python-Dokumentation übernommen. Der Analyzer läuft bei Bedarf separat über `scripts/` neben `python scripts/run_checks_and_report.py`.
 - 2025-11-10 08:40: Skript-Cleanup: entfernt `scripts/run_linters.ps1`, `scripts/tests_pytest_root.ps1`; archiviert Snapshot-Skripte nach `novapolis-dev/archive/scripts/`; Agent-Legacy-PowerShell (`cleanup_phase3.ps1`, `cleanup_phase4.ps1`, `history_purge_plan.ps1`) gelöscht; .tmp Audit aktualisiert.
- 2025-11-10 08:19: Tool-Registry `settings` Alias wiederhergestellt; targeted pytest `tests/test_tools_registry.py` PASS (AttributeError behoben, R-LINT/R-LOG).
- 2025-11-10 08:08: Ruff-Fixes in `novapolis_agent/app/tools/registry.py`, `novapolis_agent/scripts/append_done.py`, `novapolis_agent/scripts/rerun_failed.py`; moderne Typannotationen, Import-Sortierung und redundante Open-Modi bereinigt; DONELOGs aktualisiert.
- 2025-11-10 07:52: README-Link auf den erweiterten Copilot-Leitfaden ergänzt; `workspace_tree_dirs.txt`, `workspace_tree.txt`, `workspace_tree_full.txt` auf 2025-11-10 07:50 aktualisiert. Folgeanpassungen in `WORKSPACE_STATUS.md` vorgenommen.
- 2025-11-09 22:38: Wrapper-Umstellung: Lange inline `pwsh -NoProfile -Command` Tasks in `/.vscode/tasks.json` wurden auf `-File` Wrapper-Skripte umgestellt. Hinzugefügt: `scripts/checks_linters.ps1`, `scripts/checks_types.ps1`, `scripts/tests_pytest_root.ps1`. Backup-Marker: `Backups/tasks.json.bak`.
- 2025-11-09 22:42: Post-Run Summary: `scripts/checks_linters.ps1` (ruff/black) produced many style/format issues (see linter output summary). `scripts/checks_types.ps1` (pyright+mypy) reported 0 errors and 12 warnings. `scripts/tests_pytest_root.ps1` (`pytest -q`) aborted during collection with multiple ImportErrors (missing package paths / module imports). See `novapolis_agent/docs/DONELOG.txt` for details.

- 2025-11-09 22:55: Tests executed: After installing `novapolis_agent` editable into root `.venv` and running pytest with CWD `novapolis_agent`, the test suite completed successfully (100% collected; run shown as completed). See `novapolis_agent/docs/DONELOG.txt` for the run receipt.

---

Workspace-Status
================

Überblick
---------

- Hinweis: „Grün“ gilt nur bis zur nächsten Abweichung/Unsicherheit - dann STOP, Rückfrage, weiter nach Freigabe. Details: `.github/copilot-instructions.md` → „Unklarheiten-STOP (global, immer gültig)“.

- 2025-11-10 07:50: Tree-Snapshots (`workspace_tree_full.txt`, `workspace_tree.txt`, `workspace_tree_dirs.txt`) regeneriert; README und Status auf den Copilot-Leitfaden verwiesen.
- 2025-11-07 06:30: Alle Markdownlint VS-Code-Tasks & Wrapper-Doku entfernt; Ausführung jetzt ausschließlich manuell via `npx --yes markdownlint-cli2` (Policy npx-only).
- 2025-11-07 02:10: markdownlint-cli2 repo-weit ausgeführt (367× MD003 offen); Skriptprüfung für Markdown-Ausgaben (Chat-Exporter, Reports, todo_gather) vorbereitet.
- 2025-11-07 01:39: TODO aktualisiert (Single-Repo-Reminder; Aufgaben zu Lint-Overrides, Staging-Reports, Metadata-Konsolidierung, Archiv-Ablage).
- 2025-11-07 01:27: Konfliktanalyse durchgeführt (Markdownlint-Overrides, Staging-Reports ohne Frontmatter, doppelte Metadata-Skripte, Chat-Router-Notiz). Maßnahmen in TODO/DONELOG erfasst.
- Mono-Repo bündelt `novapolis_agent`, `novapolis-rp`, `novapolis-dev`, `novapolis-sim`, gemeinsame Pakete unter `packages/`
- Produktiver Code liegt ausschließlich im Agent-Backend; RP-Workspace enthält weiterhin Daten, Workflows, Tools
- Root-Dokumente (`README.md`, `todo.root.md`, `WORKSPACE_STATUS.md`) wurden am 2025-11-02 synchronisiert und liefern Einstieg ohne Projektwechsel
- Kopilot-Anweisungen konsolidiert unter `.github/copilot-instructions.md`
- Struktur-Snapshots (`workspace_tree.txt`, `workspace_tree_dirs.txt`, `workspace_tree_full.txt`) zuletzt am 2025-11-10 07:50 via Tasks `Workspace tree:*` regeneriert; nächste Prüfung nach größeren Strukturänderungen oder spätestens Ende November.
- PowerShell-Standard: Terminal-Profile & VS-Code-Tasks laufen jetzt über `pwsh` 7.5.4; Windows PowerShell bleibt nur noch Fallback.

Aktueller Arbeitsmodus
----------------------

- Modus: General (GPT-5)
- STOP-Gate: an (vor Code-/kanon-kritischen Aktionen explizite Bestätigung erforderlich)
- Erinnerungen: Wechselhinweise bei Code-Triggern aktiv; „Bitte nicht erinnern“ schaltet Hinweise ab bis zur Reaktivierung

Health-Checks & Open Items
---------------------------

- Tests (2025-11-10 08:19 targeted): `pytest tests/test_tools_registry.py` PASS (Tool-Registry Alias-Fix verifiziert); Vorlauf 2025-11-09 22:11 (`pytest` 298 passed, 1 skipped; Coverage 81.66%; Frontmatter-Validator PASS nach Fix an `todo.root.md`).
- Typen: Letzter vollständiger Lauf unverändert grün (pyright/mypy - keine neuen Fehler seit vorherigem Bericht); Folge-Lauf geplant nach nächster Codeänderung.
- TODO-Backlog: siehe `todo.root.md` (Stand 2025-11-07; Fokus Agent: RAG/Tool-Use/Policies, RP: Kurations-Pipeline & Canvas-Pflege, Skriptprüfung für Markdown-Ausgaben)
- Policies & Behaviour: maßgeblich `.github/copilot-instructions.md` (SSOT)
- Risiken kurz:
  - Verzeichnis-Bulk unter `outputs/` (LoRA-Runs) wächst; mittelfristig archivieren oder auslagern
  - RP-Datenpflege erfordert regelmäßigen Sync mit Memory-Bundle (seit 2025-11-02 aktualisiert, siehe `novapolis-rp/database-rp/00-admin/memory-bundle.md`)
  - Tree-Snapshots aktuell Stand 2025-11-10 07:50; Refresh fällig nach der nächsten Strukturinventur oder spätestens Ende November
  - VS-Code-Settings: Nutzer-/Profil-Overrides entfernt, nur Root-Workspace-Config aktiv
  - VS Code Multi-Root (historischer Fall, inzwischen bereinigt): Multi-Root-Workspace-Datei (`*.code-workspace`) entfernt/archiviert; Root wird als Single-Root genutzt. Wrapper-Tasks sind für standardisierte Prüf-/Testläufe wieder erlaubt (R-WRAP), Multi-Root-Fallakte bleibt als Historie (`novapolis-dev/logs/open-case-terminal-multi-root-20251103.md`).

Multi-Root & Wrapper-Status (Stand 2025-11-16 12:00)
----------------------------------------------------

- Workspace: Single-Root (VS Code öffnet den Ordner `Main` direkt; keine aktiven Multi-Root-Workspace-Dateien mehr).
- Wrapper-Policy: Mehrschrittprozesse (Lint/Typen/Tests/Coverage) sollen bevorzugt über Skript-Wrapper laufen:
  - Checks-Wrapper: `python scripts/run_checks_and_report.py` ist der einzige Entry-Point für „Checks: full“.
  - Coverage-Wrapper: `scripts/run_pytest_coverage.ps1` für kombinierte Coverage-Läufe (R-COV), mit Receipt.
- STOP-Gate (R-STOP/R-WRAP):
  - Reine Lese-Operationen (z. B. `tree`, `git status`, `cat`/`Get-Content`) benötigen keinen zusätzlichen Guard.
  - Aktionen mit Seiteneffekt (WRITE/RUN, z. B. Skript-Wrapper, Formatierer, Cleanup) bleiben STOP-pflichtig (kurzer Plan + Receipt).
- Akzeptanzkriterien erfüllt:
  - Keine `*.code-workspace` im Workspace aktiv.
  - Wrapper-Skripte sind im Root verankert (`scripts/run_checks_and_report.py`, `scripts/run_pytest_coverage.ps1`).
  - Dieser Statusblock dokumentiert den Abschluss des Multi-Root-Falls.

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

- Vollständiger Verzeichnisbaum: `workspace_tree_full.txt` (Stand 2025-11-10 07:50; Terminal `tree /A /F`)
- Arbeitsansicht: `workspace_tree.txt` (Stand 2025-11-10 07:50; Terminal `tree /A`) und kompaktes Verzeichnis-Listing `workspace_tree_dirs.txt` (Stand 2025-11-10 07:50; Script `scripts/update_workspace_tree_dirs.ps1`)
- Historische Agent-Dateiinventur (jetzt Root): `WORKSPACE_INDEX.md`
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
- Promotion abgeschlossen: Index liegt als `WORKSPACE_INDEX.md` im Root; nächster Schritt: Tree-Snapshot aktualisieren.
 - Link-Scanner: Nach Index-Anpassungen wurde `scripts/scan_links.py --files WORKSPACE_INDEX.md` am 2025-11-16 03:37 ausgeführt; Report unter `.tmp-results/reports/scan_links_20251116_033738.*`, Postflight in `novapolis-dev/archive/docs/donelogs/scan_links_postflight_20251116_033738.md` dokumentiert (0 kritische Broken-Links im Index).



