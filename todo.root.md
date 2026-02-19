---
stand: 2026-02-18 06:58
update: Optionalpunkt Archivierungs-Feinschliff umgesetzt: Rotations-Dry-Run bewertet, Manifest rekursiv aktualisiert und Outputs->Backups SOP in `Backups/README.md` verankert.
checks: F:/VS-Code-Workspace/Main/.venv/Scripts/python.exe -m scripts.rotate_backups --include-subdirectories DRY-RUN PASS (2026-02-18 06:58, Keep 7 / Delete 75); F:/VS-Code-Workspace/Main/.venv/Scripts/python.exe -m scripts.update_backups_manifest --include-subdirectories PASS (2026-02-18 06:58, Entries 82); F:/VS-Code-Workspace/Main/.venv/Scripts/python.exe -m ruff check . PASS (2026-02-18 06:33); F:/VS-Code-Workspace/Main/.venv/Scripts/python.exe scripts/tests_pytest_root.py PASS (2026-02-18 06:34)
---

TODO-Uebersicht (Novapolis Suite)
=================================

Diese Datei dient als zentrale Sammelstelle fuer alle laufenden Aufgaben. Die vollstaendigen Projekt-Listen sind unten eingebettet, damit sie ohne Kontextwechsel eingesehen werden koennen.

Kurzueberblick
--------------

- 2025-11-18 03:55: Pyright dauerhaft via Wrapper aktiv; Typwarnungen in Agent (`chat.py`, `utils/rag.py`, `utils/eval_utils.py`) entschärft; Full‑Checks PASS (Coverage 83.33%).
- Hinweis: „Grün“ gilt nur bis zur nächsten Abweichung/Unsicherheit - dann STOP, Rückfrage, weiter nach Freigabe. Details: `.github/copilot-instructions.md` → „Unklarheiten-STOP (global, immer gültig)“.
- Hinweis (Temp-Pfade): Legacy `/.tmp-results/` bleibt als Altbestand bestehen; neue Reports/Artefakte liegen unter `/.tmp/results/`.

2026-01-07 03:51 | Copilot | Schritt 3: Temp-Pfade konsolidiert (.tmp-results -> /.tmp/results)


- 2025-11-15 09:27: Frontmatter-Autofix + `--touch` (Stand-Update) in `scripts/check_frontmatter.py` ergänzt; Governance-Hinweis aktualisiert; Validator PASS.
- 2025-11-15 09:00: Dokumentationsstatus aktualisiert (context.local.md Frontmatter repariert, Statusdateien im Abgleich); Frontmatter-Validator PASS.

- 2025-11-10 08:08: Ruff-Backlog Etappe gestartet - targeted Fixes in `novapolis_agent/app/tools/registry.py`, `novapolis_agent/scripts/append_done.py`, `novapolis_agent/scripts/rerun_failed.py`; DONELOG & `WORKSPACE_STATUS.md` aktualisiert (R-LINT, R-LOG).
- 2025-11-09 21:25: Workspace-Analyse durchgeführt (Root/Ordner-Ebene, stichprobenartig Dateien). Befunde ergänzt: Frontmatter-Backlog (R-FM), Multi-Root-Abschluss (R-STOP/R-WRAP), Artefakt-Bereinigung (R-SEC/R-SAFE), Tree-/Status-Snapshots (R-IDX).
- 2025-11-08 23:21: Headings-Extrakt (`.github/copilot-instructions-headings.md`) aktualisiert; Vorschlagsliste neuer Regel-IDs (R-COV, R-IDX, R-COMM, R-RED, R-TODO, R-TIME, R-SAFE) ergänzt. Klärungsbedarf offen: Precedence zwischen abgeschafftem Start-Check (false) und „Semantische Regeln“ (obligatorisch); Anwendung der Default-(true)-Regel bei gleichrangigen Abschnitten.
 - 2025-11-07 21:46: Implementiert: automatisierte Frontmatter-Aktualisierung für veränderte Markdown/Text-Dateien (Backups, scoped validator, DONELOG-Mechanismus). Legacy-Wrapper entfernt.
- 2025-11-07 04:56: Archiv-TODOs (`novapolis-dev/archive/todo.*.archive.md`) auf Setext (H1/H2) umgestellt, Checks/Timestamps aktualisiert; `.github/ISSUE_TEMPLATE/feature_request.md` konsistent gemacht; repo-weites `markdownlint-cli2` PASS (132 Dateien).
- 2025-11-07 02:10: markdownlint-cli2 repo-weit ausgeführt (367× MD003 Setext-Stil offen); Analyse der Markdown-generierenden Skripte (Chat-Exporter, Reports, todo_gather) vorbereitet.
- 2025-11-07 01:27: Workspace-Analyse für widersprüchliche Einstellungen und Alt-Markdown durchgeführt; Kandidaten protokolliert (Lint-Override-Dateien, Staging-Reports ohne Frontmatter, doppelte Metadata-Skripte).
- Reminder Single-Repo: Alle Module (Agent/RP/Dev/Sim) laufen unter `Main/`; zentrale Verwaltung im Root, Archive nach `novapolis-dev/archive/**`, Löschungen erst nach Integration + Freigabe.
- 2025-11-06 15:58: MD003 Setext + YAML-Frontmatter in `novapolis_agent/cleanup_recommendations.md`, `Backups/novapolis-rp-development-archived-20251105/development/README.md`, `novapolis-dev/logs/betriebsmodi-20251103-0341.tmp.md`, `novapolis-rp/.github/ISSUE_TEMPLATE/bug_report.md`, `novapolis_agent/eval/config/context.local.sample.md`; targeted markdownlint PASS (5 Dateien); Logs aktualisiert.
- 2025-11-06 15:22: MD003-Setext-Korrekturen in `novapolis-rp/coding/tools/chat-exporter/README.md`, `novapolis-rp/coding/tools/metadata/README.md`, `novapolis-rp/coding/devcontainer/README.md`; targeted markdownlint PASS (3 Dateien).
- 2025-11-06 15:22: YAML-Frontmatter (stand/update/checks) in denselben 3 Dateien ergänzt; frontmatter-Validator PASS (targeted).
- 2025-11-06 15:30: YAML-Frontmatter ergänzt und MD003-Konformität bestätigt (Setext bereits vorhanden bzw. H1 ergänzt) in `packages/README.md`, `novapolis-sim/README.md`, `novapolis-rp/README.md`, `novapolis-dev/README.md`, `novapolis-rp/coding/tools/validators/README.md`; targeted markdownlint + frontmatter-Validator PASS (5 Dateien).
- 2025-11-06 15:35: MD003 Setext + YAML-Updates in `novapolis-dev/logs/README.md`, `novapolis-dev/integrations/mcp-openai-eval/README.md`, `novapolis-rp/database-curated/staging/README.md`, `novapolis-rp/database-rp/06-scenes/README.md`, `.tmp/results/README.md`; targeted markdownlint + frontmatter-Validator PASS (5 Dateien).
- 2025-11-06 15:44: YAML-Frontmatter ergänzt und MD003/Setext vereinheitlicht in `novapolis-rp/database-curated/README.md`, `novapolis-rp/database-raw/99-exports/README.md`, `.tmp/datasets/README.md`, `novapolis_agent/eval/config/context.notes/README.md`; targeted markdownlint + frontmatter-Validator PASS (4 Dateien).
- 2025-11-06 15:51: MD003 Setext + YAML-Frontmatter (falls fehlend) in `Backups/README.md`, `Backups/AUDIT.md`, `novapolis-dev/logs/log-template.md`, `novapolis_agent/data/logs/README.md`, `eval/config/context.local.md`; targeted markdownlint PASS (5 Dateien).
- 2025-11-06 04:52: MD003-Setext-Korrektur in `novapolis-rp/database-curated/README.md`; targeted markdownlint PASS.
- 2025-11-06 04:50: MD003-Setext-Korrekturen in `packages/README.md`, `novapolis_agent/scripts/README.md`, `novapolis_agent/eval/README.md`, `novapolis_agent/eval/DEPRECATIONS.md`; targeted markdownlint PASS (4 Dateien).
- 2025-11-06 04:40: Demo-Test wieder entfernt (`tests/test_intentional_failure.py`), `pytest -q` via pwsh PASS; Frontmatter-Validator-Demo abgeschlossen.
- 2025-11-06 04:15: Frontmatter-Validator mit Demo-Datei geprüft (`check_frontmatter.py` → Fehlermeldungen bestätigt, nach Fix PASS); absichtlicher pytest-Fail durch `tests/test_intentional_failure.py` dokumentiert.
- 2025-11-06 03:45: Repo-weiter Markdownlint-Lauf zeigte 437× MD003 (Setext-Stil). YAML-Hinweis oben beachten; Bereinigung schrittweise angehen.
- 2025-11-06 03:18: Veraltetes Markdownlint-Skript entfernt (`novapolis-rp/coding/tools/validators/run_lint_markdown.ps1`); README & Copilot-Anweisungen aktualisiert.
- 2025-11-06 03:07: Veralteten Chat-Neustart-Prompt entfernt (`novapolis-dev/docs/prompts/chat-restart.md`); Index/DONELOG aktualisiert; Markdownlint (index/donelog) PASS.
- 2025-11-06 02:57: RP/Sim-Dokumente (`todo.sim.md`, Specs-Batch, Betriebsmodi-Notizen) auf YAML-Frontmatter gebracht und einzeln gelinted - PASS; DONELOG aktualisiert.
- 2025-11-06 02:52: `novapolis-dev/docs/todo.rp.md` auf YAML-Frontmatter gebracht und einzeln gelinted (`markdownlint todo.rp.md`) - PASS; DONELOG aktualisiert.
- 2025-11-06 02:42: `novapolis_agent/docs/training.md` und `docs/reports/overnight-20251022.md` gelinted und mit aktuellem Stand versehen; DONELOG/TODO aktualisiert.
- 2025-11-06 02:35: Agent-Dokumente (`customization.md`, `ARCHIVE_PLAN.md`, `CONTEXT_ARCH.md`, `REPORTS.md`) gelinted; Frontmatter/Checks aktualisiert; dokumentiert in DONELOG.
- 2025-11-06 02:30: `novapolis_agent/docs/DONELOG.txt` auf YAML-Frontmatter/Setext umgestellt; Lint-Einzellauf PASS; Root-DONELOG aktualisiert.
- 2025-11-06 02:23: README (Agent) und `docs/AGENT_BEHAVIOR.md` Heading/Frontmatter angepasst, Lint-Einzelläufe PASS; Zwischenschritt in DONELOG erfasst.

- **novapolis_agent**: Fokus auf Eval-/Tooling-Pflege, RAG-Ausbau, Tool-Use, Policy-Hooks.
- **novapolis-dev / novapolis-rp**: Fokus auf Canvas-Rettung Sprint (Charaktere/Logistik/Systeme) sowie bestehende Datenkurierungs- und Sim-Aufgaben.
- **YAML/Setext-Hinweis**: Bei allen Markdown-Anpassungen Frontmatter (stand/update/checks) synchronisieren und H1/H2 konsequent im Setext-Stil halten; laufender MD003-Backlog (122 Dateien laut letztem Markdownlint-Lauf).
- **Terminal/Tasks (Single-Root)**: VS Code läuft wieder als Single-Root; Wrapper-Tasks/Automationen sind ab Root erlaubt (R-WRAP). Standard-Läufe starten im Repo-Root `F:/VS-Code-Workspace/Main`, Interpreter `.venv` liegt im Root. Multi-Root-Hinweise bleiben lediglich historisch dokumentiert.
  - Historische Fallakte: `novapolis-dev/logs/open-case-terminal-multi-root-20251103.md`
- **Root-Übersicht**: `WORKSPACE_STATUS.md` (Stand 2025-11-02) + `workspace_tree*.txt` (Stand 2025-11-02) liefern Gesamtinventar; nächste Aktualisierung idealerweise bis Mitte November oder nach größeren Umstrukturierungen.
  - [x] Tree-Snapshots (`workspace_tree.txt`, `workspace_tree_dirs.txt`, `workspace_tree_full.txt`) am 2025-11-02 via Tasks `Workspace tree:*` regeneriert.
- 2025-11-01: DONELOG-Heading-Stil auf Setext gemäß MD003 korrigiert; Markdownlint bleibt zentral via npx.
- **Archivierung**: `outputs/`- und `Backups/`-Artefakte sukzessive bündeln (ZIP) und Rotation dokumentieren.
 - **Archivierung**: `outputs/`- und `Backups/`-Artefakte sukzessive bündeln (ZIP) und Rotation dokumentieren; abgeschlossene Dokument-Blöcke nach Review unter `novapolis-dev/archive/` ablegen.
  - Root-Archiv (vollständig erledigte Root-Blöcke): `novapolis-dev/archive/todo.root.archive.md`.
  - [ ] Altbestände nach Runs gruppieren (z. B. `outputs/lora-YYYYMMDD_HHMM` → einzelnes ZIP in `Backups/model-runs/`).
  - [ ] Eval-Resultate aus Vor-Umbenennung auf neue Paketpfade prüfen und Meta-Felder ggf. nachziehen (`eval/results/**/*.jsonl`).
  - [ ] README oder `Backups/`-Manifest um Rotationsplan ergänzen (Aufbewahrungsdauer, Löschkriterien).
  - [ ] Automatisierte Aufgabe/Script prüfen (Cleanup-Phasen, historisch im Archiv) für regelmäßiges Auslagern.
 - **Lokale AI Einbindung (organisch)**: Phasenplan/Go-Kriterien/Metriken in Abschnitt „Lokale AI - Einbindung (organisch)“ unten; Start mit Phase01 möglich (ohne Zeitdruck, mit harten Fallbacks).
 - **Editor-Setup**: Konsolidierung `.vscode` auf Root vorbereiten (siehe Abschnitt „Editor-Setup - .vscode-Konsolidierung (Root-zentriert)“).

- Neu (2025-11-06): Modulstatus → Agent: Gelb-grün, Dev: Grün, RP: Gelb, Sim: Gelb. Konkrete 1-2-Tage-Schritte siehe Abschnitt „Nächstes Vorgehen (1-2 Tage)“.

Wrapper-Migration (.ps1 → .py)
------------------------------

- Ziel: Alle noch relevanten Wrapper von PowerShell (`*.ps1`) schrittweise auf Python-Skripte (`*.py`) umstellen, konsistent mit R-WRAP/R-SEC/R-SAFE.
- Hintergrund:
  - Historische Wrapper (ehemals `*.ps1`, heute `*.py`): `scripts/run_pytest_coverage.py`, `scripts/checks_linters.py`, `scripts/checks_types.py`, `scripts/tests_pytest_root.py`.
  - Aktueller Stand: `python scripts/run_checks_and_report.py` ist der einzige Entry-Point für "Checks: full"; Coverage-Läufe erfolgen via `python scripts/run_pytest_coverage.py --fail-under <threshold>` (PowerShell-Varianten sind nur noch Archiv/Backup).
- Aufgaben (geplant, keine Löschung ohne Freigabe):
  - [x] Bestandsaufnahme aller noch vorhandenen `scripts/*.ps1` Wrapper (inkl. Backups/Archiv-Hinweisen). (2025-12-11: keine aktiven Wrapper mehr im Root; alle 33 `*.ps1`-Dateien liegen ausschließlich unter `novapolis-dev/archive/scripts/scripts.ps1-scripts/`.)
  - [x] Für jeden produktiven Wrapper einen gleichwertigen Python-Einstiegspunkt definieren (z. B. `scripts/run_pytest_coverage.py`), inklusive Args/Exitcodes/Receipts. (Bestätigt 2026-02-17: produktive Entrypoints laufen über `scripts/*.py` und Root-Tasks.)
  - [x] VS-Code-Tasks und Dokumentation (`WORKSPACE_STATUS.md`, `todo.cleaned.md`, README/Docs) auf die Python-Varianten umstellen. (Stand 2026-02-17: aktive Root-Tasks nutzen `.venv\Scripts\python.exe` bzw. `scripts/*.py`.)
  - [x] PowerShell-Wrapper sind nur noch Archiv/Backup; keine aktive Nutzung. Falls jemals reaktiviert, dann ausschließlich als dünne Hülle (nur Aufruf von `python <script.py>`) und klar als Fallback gekennzeichnet. (Stand 2026-02-17)
  - [x] Nach Abschluss: kurzen Statusblock zur Wrapper-Migration in `WORKSPACE_STATUS.md` und DONELOG-Eintrag ergänzen (R-DOKU/R-LOG). (Ergänzt 2026-02-17)

Modulstatus (2025-11-06)
------------------------

- Agent (Backend): Gelb-grün. Tests/Typen zuletzt grün, aber kein dokumentierter Lauf seit 2025-10-31; leichte Driftgefahr bei Scripts/Eval-Artefakten.
- RP (Daten/Canvases): Gelb. Kurations-Pipeline aktiv, einige Review-/Tagging-Schritte offen.
- Dev (Dok-Hub): Grün. Frontmatter-Migration weitgehend durch, Donelog/Index gepflegt.
- Sim (Godot): Gelb. Option A gesetzt, Projektdatei kanonisch; Headless-Lade-Check offen.

Nächstes Vorgehen (1-2 Tage)
 - [x] Korrektur: Checks-Wrapper (damals PowerShell, jetzt `python scripts/run_checks_and_report.py`) - STOP-Fall bei zu vielen Testdateien soll als Fehler/FAIL gemeldet werden (Statuszuordnung anpassen). (erledigt 2025-11-11 00:23, Commit abe6829)
 - [ ] Optional nach Review: Cleanup-Kandidaten (Phase 4) nur mit Freigabe angehen (historisch: `cleanup_phase4` im Archiv).
 - [x] Alt-Analyse `novapolis_agent/analysis_chat_routers.md` ausgewertet; Inhalte in aktiver Doku bestätigt (`novapolis_agent/cleanup_recommendations.md`) und Legacy-Datei nach Freigabe entfernt. (erledigt 2026-02-18 04:00)

Priorisierung (Stand 2026-02-18, aktualisiert)
--------------------------------

### Jetzt

- [x] Skript-Ladefallbacks vereinheitlichen (`scripts/reports/generate_consistency_report.py` ↔ `scripts/audit_workspace.py`) (R-CTX). (erledigt 2026-02-18 04:15)
- [x] Test-/Artefakt-Reste prüfen und `.gitignore`-Abdeckung absichern (R-SEC). (erledigt 2026-02-18 04:15)
- [x] Frontmatter-Backlog in `database-rp` schließen und Validator-Rerun loggen (R-FM). (erledigt 2026-02-18 04:15)
- [x] Root-Tasks Go/No-Go finalisiert: `lint:ruff`, `fix:ruff`, `Tests: pytest (-q) [root]`, `Tests: coverage (fail-under)` erneut grün. (erledigt 2026-02-18 04:50)
- [x] Editor-Setup Etappe 0 abgeschlossen: `.vscode`-Inventur/Diff/Mapping dokumentiert (nur Root-`.vscode` vorhanden: `settings.json`, `tasks.json`, `launch.json`; keine Subfolder-Konflikte). (erledigt 2026-02-18 04:50)
- [x] Snapshot-Frontmatter-Migration Etappe 1 aktiv umgesetzt (dieser Zyklus): geänderte Doku-Dateien mit konsistentem `stand/update/checks` geführt. (laufende Betriebsregel)

### Später

- [x] S1 - Stabilitätsfenster abgeschlossen (Tag 1-2):
  - täglich `lint:ruff`, `Tests: pytest (-q) [root]`, `Tests: coverage (fail-under)` ausführen und PASS in `DONELOG.md`/`WORKSPACE_STATUS.md` nachziehen.
  - Fortschritt: Tag 1 (2026-02-18 05:05) und Tag 2 (2026-02-18 05:13) jeweils grün – `ruff` PASS, Root-Pytest PASS, Coverage PASS (83.02%, `354 passed, 1 skipped`).
  - Gate S1: erfüllt (2 aufeinanderfolgende Läufe ohne rote Root-Gates).
- [x] S2 - Lokale-AI Mindestbasis hergestellt:
  - Schattenmodus-Logging aktivieren, 10-20 Kern-Dokumente indexieren, Flags/Redaction im Stichprobenlauf prüfen.
  - Fortschritt: Index-Stichprobe erstellt (`novapolis_agent/eval/results/rag/s2-core-index-20260218.json`, 11 Dokumente), Schattenmodus-Log aktiv (`.tmp/results/logs/shadow_mode.jsonl`) und gezielte Stichproben-Tests PASS (`tests/test_rag_guards.py`, `tests/test_api_chat_internal_branches.py`).
  - Gate S2: erfüllt (RAG-Minimum + Redaction-Test + Shadow-Log-Artefakt dokumentiert).
- [x] S3 - Operativen Review-Rhythmus fixiert:
  - festen wöchentlichen Slot (30-45 min) setzen und Checkliste „lokale AI“ in `todo.root.md`/`DONELOG.md` verankern.
  - Slot: jeden Mittwoch 09:00-09:45 (lokal) als „Lokale-AI Betriebsreview“.
  - Checkliste (verankert): (1) Shadow-Log vorhanden (`.tmp/results/logs/shadow_mode.jsonl`), (2) RAG-Index aktuell (`novapolis_agent/eval/results/rag/s2-core-index-20260218.json`), (3) Root-Gates grün (`ruff` + Root-`pytest`), (4) offene Risiken/Folgeschritte in `DONELOG.md` notiert.
  - Erster Review-Slot: durchgeführt und protokolliert am 2026-02-18 06:34.
  - Gate S3: erfüllt.
- [x] S4 - Editor-Setup Etappe 1/2 umgesetzt:
  - optionale Task-/Launch-Konsolidierung und Dublettenabbau auf Root-Ebene durchführen.
  - Ergebnis: Keine Subfolder-`.vscode`-Konflikte (nur Root `tasks.json`/`launch.json`), `launch.json` syntaktisch valide, Root-Tasks weiterhin lauffähig (`ruff`, Root-`pytest`).
  - Gate S4: erfüllt.
- [ ] S5 - Snapshot-Frontmatter-Migration Etappe 2/3 freigeben:
  - Sweep + Legacy-Auslauf nur nach 3-5 Tagen stabiler Laufpraxis ohne Beschwerden ausführen.
  - Status: offen wegen Zeit-Gate (früheste Freigabe bei stabiler Laufpraxis ab 2026-02-21).
  - Gate S5 (Migration-Go/No-Go): Freigabevermerk in `WORKSPACE_STATUS.md` + Abschlussblock in `DONELOG.md`.

### Optional

- [x] Cleanup-Kandidaten Phase 4 reviewt (historischer Archivkontext): keine aktiven Zielpfade mehr vorhanden; keine destruktive Aktion ausgeführt. (erledigt 2026-02-18 06:58)
- [x] Archivierungs-Feinschliff umgesetzt (`outputs`/`Backups` Gruppierung, Manifest-Rotationsplan, automatisierte Auslagerung via SOP/Cadence). (erledigt 2026-02-18 06:58; Evidenz: Rotation Dry-Run Keep 7/Delete 75, Manifest 82 Einträge, Regeln in `Backups/README.md`)
- [ ] Etappe-3-Legacy-Ablösung der Snapshot-Frontmatter-Migration erst nach stabiler Laufpraxis (nur falls Etappe 2 abgeschlossen).

### novapolis_agent

- [x] Tests/Typen sequenziell laufen lassen (manuell) und Ergebnis protokollieren: `DONELOG.md` (Root) und `novapolis_agent/docs/DONELOG.txt` (Agent). (erledigt 2026-01-07 10:47)
- [x] 2025-11-10 08:08: Ruff-Fixes in `app/tools/registry.py`, `scripts/append_done.py`, `scripts/rerun_failed.py`; targeted Ruff-Checks PASS, DONELOG & `WORKSPACE_STATUS.md` aktualisiert (R-LINT/R-LOG).
- [x] Ruff-Backlog weiter triagieren (restliche Agent-Skripte/Tools; Volumen >3000 Ruff-Meldungen; R-LINT, R-SEC). (2026-02-17: `lint:ruff` zeigte 1 Treffer in `scripts/merge_todos.py`, per `fix:ruff` behoben; erneuter Lauf PASS.)
- [x] 2025-11-06 04:40: Demo-Test `novapolis_agent/tests/test_intentional_failure.py` entfernt; pytest -q PASS.
- [x] Markdown-Ausgabe der Skripte (todo_gather, summarize_eval_results, map_reduce_summary_llm, Reports) sowie Chat-Exporter auf Setext/YAML-Konformität prüfen und ggf. anpassen. (2025-11-10 04:20)
- [x] Konsistenz-Audit/Report aktualisieren (Sichtprüfung): `novapolis_agent/scripts/reports/generate_consistency_report.py` und Kandidaten aus `novapolis_agent/scripts/audit_workspace.py` prüfen. (2026-02-17: Report neu erzeugt unter `novapolis_agent/eval/results/reports/consistency/20260217_2047`.)
- [x] Optional nach Review: Cleanup-Kandidaten (Phase 4) abgeschlossen; historisches `cleanup_phase4` bleibt archiviert, aktive Zielpfade sind bereits entfernt. (erledigt 2026-02-18 06:58)
- [x] Alt-Analyse `novapolis_agent/analysis_chat_routers.md` ausgewertet; Inhalte in aktiver Doku bestätigt (`novapolis_agent/cleanup_recommendations.md`) und Legacy-Datei nach Freigabe entfernt. (erledigt 2026-02-18 04:00)

#### Tests/Typen/Coverage (Priorität mittel-hoch, R-COV)
 - Akzeptanzkriterien:
   - pytest PASS; pyright PASS; mypy PASS.
   - Coverage ≥ 80 % mit Branch-Erfassung, fail-under aktiv.
   - Receipt mit Zeitstempel, Commit-SHA und getrennten Anteilen (App/Scripts) in `DONELOG.md`; Verweis/Kurzsummary in `WORKSPACE_STATUS.md`.
   - CI-Gate aktiv (nicht nur lokal).
 - Schritte (STOP beachten; Wrapper-Policy gilt):
   - Läufe im Repo-Root (`F:/VS-Code-Workspace/Main`) starten: `python scripts/run_checks_and_report.py --scope full` für den Komplettlauf und `python scripts/run_pytest_coverage.py --fail-under 80` für Coverage. (Falls Spezialpfade nötig sind, `cwd` explizit auf `novapolis_agent/` setzen.)
   - Ergebnisse/Quoten protokollieren (getrennt App/Scripts, Branch-Coverage), Receipts schreiben, CI-Fail-Under prüfen.
 - Receipts/Belege:
   - `DONELOG.md`: „R-COV“ mit PASS/Quoten, Zeitstempel, Commit-SHA.
   - `WORKSPACE_STATUS.md`: kurzer Statusblock „Tests/Typen/Coverage aktuell“ mit Datum/Quote.
 - [x] Skript-Ladefallbacks vereinheitlichen (direkte Imports statt dynamischer Spez): `scripts/reports/generate_consistency_report.py` ↔ `scripts/audit_workspace.py` auf direkten Importpfad vereinheitlicht. (erledigt 2026-02-18 04:15, R-CTX)
 - [x] Test-/Artefakt-Reste geprüft (pyc, test_*_event.meta.json etc.): Funde liegen in `.mypy_cache` und sind via `.gitignore` abgedeckt; keine zusätzlichen Track-Kandidaten. (erledigt 2026-02-18 04:15, R-SEC)

- [x] STOP-Plan 015-010 Write-Run (R-STOP/R-WRAP/R-LOG, erledigt 2025-11-27 22:10)
  - Backups: `Backups/tagging-pipeline/AI-Behavior-Mapping-20251127-220319.{md,json}` erstellt, Snapshot `Backups/tagging-015-010-prewrite.txt` jetzt inkl. SHA256 jeder reviewed Datei.
  - Guard: `python novapolis-rp/coding/tools/curation/tag_chunks_from_yaml.py --range 015-010 --dry-run` PASS (unresolved=[]; Alias-Kollisionen nur Echo/Reflex/Verbindungstunnel/(v1)).
  - Write-Run: identischer Befehl ohne `--dry-run`; `.tagged` 015→010 und `index_review.json`/`lexicon.json`/`unresolved.json` aktualisiert; Log `reports/tagging-20251127T212031Z.log` abgelegt.
  - Validierung: targeted `npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'todo.root.md DONELOG.md novapolis-dev/docs/donelog.md WORKSPACE_STATUS.md .tmp/results/todo.cleaned.md'` PASS; `python scripts/check_frontmatter.py` (Dateien s. checks) PASS.
  - Artefakte sync: `DONELOG.md`, `novapolis-dev/docs/donelog.md`, `.tmp/results/todo.cleaned.md`, `todo.root.md`, `WORKSPACE_STATUS.md`, Tree-Snapshots (`workspace_tree_full.txt`, `workspace_tree.txt`, `workspace_tree_dirs.txt`) und todo-list aktualisiert.

- [x] Export konsolidieren: Offene Aufgabe „`99-exports/chat-export-complete.txt`“ abschließen; Delta-Befunde in SSOT-Canvases spiegeln. (2026-02-17: Konsolidierungslauf `scripts/run_rp_chat_dedupe.py` erneut durchgeführt; `chat-export-consolidated.normalized.txt` + `reports/dedupe-chat-export.md` aktualisiert.)
- [x] Tagging-Pipeline 015-010 vom Dry-Run auf Write gehoben; Lint-Protokoll in `novapolis-dev/docs/donelog.md` vermerkt (2025-11-26 05:35).
  - Umsetzung lt. STOP-Plan (R-STOP/R-WRAP/R-LOG):
    - Backups: `AI-Behavior-Mapping.{md,json}` → `Backups/tagging-pipeline/AI-Behavior-Mapping-20251126-0522.*`, Snapshot `Backups/tagging-015-010-prewrite.txt` für reviewed Outputs.
    - Guard-Lauf: `python coding/tools/curation/tag_chunks_from_yaml.py --yaml-root novapolis-rp/database-rp --chunks-root "novapolis-rp/database-curated/staging/chunks/chat-export (1)" --out-root "novapolis-rp/database-curated/reviewed/chat-export (1)" --range 015-010 --dry-run` PASS (Summaries + Canonicalized N7 total 2 dokumentiert).
    - Write-Run: gleiches Kommando ohne `--dry-run`; erzeugt `part-015.tagged.txt` … `part-010.tagged.txt`, aktualisiert `index_review.json`/`unresolved.json`/`lexicon.json`, Report `reports/tagging-20251126T043409Z.log` mit LOC-only-Hinweisen.
    - Nachbereitung: `npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-dev/docs/donelog.md'` PASS, `python scripts/check_frontmatter.py novapolis-dev/docs/donelog.md` PASS, Einträge in `novapolis-dev/docs/donelog.md` + `DONELOG.md` ergänzt.
    - TODO/Status-Sync (dieser Eintrag + `/.tmp/results/todo.cleaned.md`, `WORKSPACE_STATUS.md`, `workspace_tree*.txt`) läuft mit aktuellem Task; Tree-Snapshots neu auf 2025-11-26 05:36 gesetzt, Postflight folgt nach Abschluss.
- [x] Tagging-Pipeline 015-010 Write-Run Refresh & Doc-Sync (2025-11-27 22:10)
  - Backups + Hash-Snapshot siehe STOP-Plan oben; Dry-Run + Write-Run PASS (alias collisions unverändert, canonicalized N7 total 2) mit Report `reports/tagging-20251127T212031Z.log`.
  - Workspace-Doku aktualisiert (`DONELOG.md`, `novapolis-dev/docs/donelog.md`, `WORKSPACE_STATUS.md`, `.tmp/results/todo.cleaned.md`, `todo.root.md`), Tree-Snapshots regeneriert (`tree /A /F`, `tree /A`, `python scripts/update_workspace_tree_dirs.py`).
  - Targeted markdownlint + Frontmatter-Validator PASS; Folgeaufgabe: Range 009-001 Plan (siehe Dev-Hub) um neue Guard-Checks ergänzen.
 - [x] STOP-Plan 009-001 Write-Run (R-STOP/R-WRAP/R-LOG)
  - Backups: 2025-12-01 08:19 abgeschlossen (`Backups/tagging-pipeline/AI-Behavior-Mapping-20251201-081946.{md,json}` + Snapshot `Backups/tagging-009-001-prewrite.txt` via `git ls-tree -l HEAD -- "novapolis-rp/database-curated/reviewed/chat-export (1)"`).
  - Guard (Dry-Run): `python ... --range 009-001 --dry-run` PASS (`unresolved_dependencies=[]`, Alias-Kollision unverändert `verbindungstunnel-c6-e3` ↔ `verbindungstunnel-d5-c6`), JSON-Summary im Terminal gesichert.
  - Write: gleicher Befehl ohne `--dry-run`; `.tagged` 009→001 + `index_review.json`/`lexicon.json`/`unresolved.json` aktualisiert; Logs aktuell nur via STDOUT verfügbar (Skript erzeugt noch keine Dateien).
  - Nachbereitung (abgeschlossen 2025-12-08 17:55): targeted `markdownlint-cli2` + `python scripts/check_frontmatter.py` (Scope `todo.root.md`, `.tmp/results/todo.cleaned.md`, `DONELOG.md`, `novapolis-dev/docs/donelog.md`, `WORKSPACE_STATUS.md`) erneut laufen lassen, alle genannten Docs synchronisiert und Tree-Snapshots (`workspace_tree_full.txt`, `workspace_tree.txt`, `workspace_tree_dirs.txt`) frisch erzeugt; Postflight-Receipt folgt nach Alias-Fix.
 - [x] Alias-Kollision „Verbindungstunnel" auflösen (Slug-Konvention vs. Doppel-Schreibweise), bevor nächste Range (≤000) geplant wird – `tag_chunks_from_yaml.py` filtert jetzt Stopword-Aliase wie „verbindungstunnel"; Range 009-001 (2025-12-10 17:49) erneut als Dry→Write gelaufen, `lexicon.json`/`unresolved.json` ohne Alias-Kollisionen, betroffene `[LOC]`-Tags (u. a. part-002) bereinigt.
- [x] Markdownlint-Overrides in `database-curated/staging/.markdownlint.json` & `.../reports/.markdownlint.json` geprüft: keine `.markdownlint.json` Dateien vorhanden (Overrides erfolgen zentral oder inline).
- [x] Stabile Staging-Reports migriert nach `novapolis-dev/docs/process/rp-canvas-rescue/` (resolved/uncertainties/plan/sources).
- [x] Verbleibende Staging-Report-Artefakte (z. B. delta/overlap/segment-hash) aufräumen oder als generiert markieren; Altdateien nur nach Freigabe löschen. (2026-02-17: Marker `novapolis-rp/database-curated/staging/reports/generated-artifacts.md` angelegt.)
- [x] Metadata-Initialisierung konsolidiert: `init_metadata.py` als kanonische Variante dokumentiert; `init-metadata.js` entfernt. (erledigt 2026-02-18 04:00)

#### RP-Audit Befunde (2025-12-30)
 - [x] Prozesslücke klären: Workflow-SSOT erwähnt `database-curated/final/`, im Repo fehlt der Ordner → Entscheidung dokumentieren (anlegen vs. Doku anpassen). (erledigt 2025-12-30 06:53)
 - [x] Frontmatter-Duplikate in `novapolis-rp/database-rp/**` bereinigen (Startliste: `00-admin/canon-canvas.draft.md`, `05-projects/Nordlinie-01.md`, `02-characters/Jonas-Merek.md`, `03-locations/C6.md`). (erledigt 2025-12-30 05:32)
 - [x] Linkdrift prüfen/fixen: `05-projects/Nordlinie-01.md` relative Links auf Admin-Dokus (z. B. Missionslog/Logistik). (erledigt 2025-12-30 05:32)
 - [x] README-Stub ergänzen: `novapolis-rp/coding/tools/curation/README.md` (kurzer Einstieg + Verweis auf ingest/tagging + RAW-Policy). (erledigt 2025-12-30 06:53)
 - [x] Nach Fixes: targeted `scripts/check_frontmatter.py` + `markdownlint-cli2` im RP-SSOT-Scope laufen lassen, Receipt in `DONELOG.md` + Kurznotiz in `WORKSPACE_STATUS.md`. (erledigt 2025-12-30 06:53)

#### Frontmatter/Markdown-Sweep (Priorität hoch, R-FM/R-LINT)
 - Akzeptanzkriterien:
   - Frontmatter-Validator PASS im vereinbarten Scope (Zählwerte vor/nach Fix dokumentiert).
   - Markdownlint PASS im definierten Scope; H1/H2 Setext konsistent.
   - „behoben=ja“ mit Zahlen in `DONELOG.md` und zusammengefasst in `WORKSPACE_STATUS.md`.
   - Generatoren, die Markdown erzeugen, schreiben Setext + Pflicht-Frontmatter per Default (kurze Generator-Quittung).
 - Schritte (Reihenfolge strikt: erst Frontmatter, dann MD003):
   - Frontmatter: betroffene Dateien zählen, Pflichtfelder (`---`,`stand`, `update`, `checks`,`---`) ergänzen, Validator erneut laufen lassen, Zählwerte/PASS loggen.
   - Markdown: MD003-Treffer im Scope beheben; Lint erneut laufen lassen; PASS loggen.
 - Receipts/Belege:
   - `DONELOG.md`: „R-FM/R-LINT“ mit Zahlenpaaren (vorher/nachher) und PASS.
   - `WORKSPACE_STATUS.md`: Kurznotiz mit Datum/Scope/Zahlen.
 - [x] Frontmatter-Backlog in `database-rp` geschlossen; Validator-Rerun `scripts/check_frontmatter.py novapolis-rp/database-rp` PASS geloggt. (erledigt 2026-02-18 04:15, R-FM)

### novapolis-dev

 - [x] Tree-Artefakte neu erzeugen (2025-12-08 17:50, manuell): `tree /A /F > workspace_tree_full.txt`, `tree /A > workspace_tree.txt`, `python scripts/update_workspace_tree_dirs.py`; Zeitstempel/Status wird in `WORKSPACE_STATUS.md` + `novapolis-dev/docs/donelog.md` dokumentiert.
  - Kontext: Generations-Cadence dokumentieren (wann „full“ vs. „dirs“ vs. „summary“). (R-IDX)
- [x] Optional: Kurzer Abschnitt „Editor-Setup“ im Root-`README.md` ergänzen (Hinweis auf STOP/Multi-Root, manuelle Terminal-Läufe). (erledigt 2026-02-17 09:16; Abschnitt vorhanden unter „Editor-Setup (Single-Root)“)
- [x] Markdownlint MD003 (aktive Docs): Scope auf essentielle Readmes/Dokus begrenzen, Stichproben-Lint (`markdownlint-cli2`), pro Datei Setext-Stil angleichen und Resttreffer außerhalb des Scopes katalogisieren. (erledigt 2026-02-17 09:18; Scope: `README.md`, `WORKSPACE_INDEX.md`, `novapolis-dev/README.md`, `novapolis-dev/docs/index.md`, `novapolis-dev/docs/readme.hub.md`, `novapolis_agent/README.md`, `novapolis-rp/README.md`; Ergebnis: PASS, 0 Fehler)
- [x] YAML-Frontmatter-Backlog priorisieren: Offene Markdown-Dateien mit `stand/update/checks` nachrüsten (Ausnahme `.github/copilot-instructions.md`), Priorität gemäß zuletzt gemeldeten Lint-Treffern. (erledigt 2026-02-17 09:24; Scope-Scan `novapolis-dev/docs` + `novapolis-rp/database-rp` via `scripts/check_frontmatter.py` = PASS, kein offener Befund)
- [x] Übernahme/Staging-Integration: Inhalte aus `novapolis-rp/database-curated/staging/reports/` nach Review in `novapolis-dev/docs/` spiegeln und Altstände archivieren. (erledigt 2026-02-18 03:57; Altstände unter `novapolis-dev/archive/quarantine/rp-canvas-rescue-presync-20260218_0357`)
  - Priorität A (zuerst spiegeln): `resolved.md`, `uncertainties.md`, `dedupe-chat-export.md`.
  - Priorität B (nachziehen als Referenz/Anhang): `delta-*.md`, `overlap-*.md`.
  - Priorität C (als generiert markieren/archivieren): `segment-hash-*.txt`, `text-stats*.md`, `tagging-*.log`.
  - Stand 2026-02-17 09:26: Inventar des Ordners geprüft; nächste Ausführung soll A-Dateien in `novapolis-dev/docs/process/rp-canvas-rescue/` spiegeln und danach C-Dateien als generierte Artefakte kennzeichnen.
  - Fortschritt 2026-02-17 09:26: A1 umgesetzt — `novapolis-dev/docs/process/rp-canvas-rescue/dedupe-chat-export.md` angelegt (Mirror aus staging/reports).
  - Status 2026-02-17 09:27: Priorität A vollständig im Dev-Hub vorhanden (`resolved.md`, `uncertainties.md`, `dedupe-chat-export.md`).
  - Abschluss 2026-02-18 03:57: A-Dateien aus `staging/reports` frisch gespiegelt; frühere Zielstände vorher in den Quarantänepfad archiviert. Priorität B vollständig gespiegelt (`delta-*.md`, `overlap-*.md`) und Priorität C als generierte Artefakte über Markerdatei `generated-artifacts.md` im Dev-Hub kenntlich gemacht.
 - [x] Docs-Hub aktualisiert: TL;DR/Links/Beispiele ergänzt; Stubs Phase 1 konsolidiert (2025-11-12 01:12).

#### Multi-Root-STOP (abgeschlossen 2025-11-16, R-STOP/R-WRAP)
- Zusammenfassung: `scripts/multi_root_cleanup.py --apply` lief durch (Backups/Move, Wrapper-Test `python scripts/run_checks_and_report.py --whatif`, Receipt in `DONELOG.md`). Alle `*.code-workspace`/`README.md.bak`/`lint.out` Artefakte liegen nun unter `Backups/`.
- Dokumentation: `WORKSPACE_STATUS.md` führt den Block „Single-Root & Wrapper-Status“ + Abschlussnotiz (Zeitstempel 2025-11-16 12:37, Commit-Ref folgt nach Merge). Fallakte bleibt historisch abrufbar (`novapolis-dev/logs/open-case-terminal-multi-root-20251103.md`).
- Nachpflege: `scripts/multi_root_cleanup.py --whatif` kann künftig als Guard laufen, um neue `.code-workspace`- oder Schatten-Dateien früh zu erkennen. Wrapper-Tasks dürfen wieder genutzt werden (R-WRAP); STOP-Gate bleibt für Write-Aktionen aktiv.
- [x] Multi-Root Cleanup-Tasks (README.bak, lint.out, Workspace-Dateien) → verschoben nach `Backups/`. (R-SEC/R-SAFE)  <!-- moved 2025-11-16 12:37 -->

### novapolis-sim

- [x] Headless-Lade-Check des Godot-Projekts `novapolis-sim/project.godot` durchführen; Warnungen/Fehler als Kurznotiz festhalten.

- Risiken (kurz)
--------------

- Tests/Typing nicht tagesaktuell (Agent) → mögliche stille Drift.
- RP: Offene Tagging-/Export-Schritte; Deltas noch nicht vollständig in SSOT gespiegelt.
- Single-Root-Governance: Neu auftauchende `.code-workspace`/`*.bak`-Dateien regelmäßig via `scripts/multi_root_cleanup.py --whatif` prüfen (R-STOP/R-WRAP).

Lokale AI - Einbindung (organisch)
----------------------------------

Kurz: Nicht beschleunigen, sondern sauber einführen. Schattenmodus → kleiner Canary → begrenzte Beta, mit Redaction/Flags/Metriken und klaren Rückfallpfaden.

### Zusammenfassung (Checkliste)

- [x] Inclusion-Ziele definiert (Rollen: RAG, Schattenmodus-Inferenz, Canary, Lernschleife)
- [x] Readiness-Gates je Modul definiert (agent/rp/dev/sim)
- [x] Phasenplan entworfen (Schatten → Canary → Limited Beta → Stabilisierung)
- [x] Daten- & Telemetrieplan (Hygiene, Consent, Redaction, Metriken)
- [x] Immediate next steps checklist (siehe unten) (erledigt 2026-02-17 09:25; Go/No-Go-Checkliste und „Nächste Schritte (sofort)“ sind vorhanden)

### Go-Kriterien je Modul (Beta-Readiness, organisch)

- novapolis_agent
  - Tests/Typen PASS an 2 aufeinanderfolgenden Tagen
  - Policy-/Rewrite-Hooks aktiv, Session-Memory (Basis)
  - RAG-Minimum indexiert (10-50 Kern-Docs, deterministischer Retriever-Test PASS)
  - Logging mit Redaction (keine PII im Klartext)
  - Flags: `RAG_ON`, `SHADOW_ON`, `CANARY_PCT`
- novapolis-rp
  - Canvas-Rettung Sprint1 Kerne abgeschlossen; Memory-Bundle konsistent
  - Sidecars konsistent (tags/dependencies/last_updated)
  - Validator-Pipeline (Behavior/Psymatrix) ohne kritische Findings
  - 200-500 kuratierte Q/A-Paare oder Chat-Turns als Startbasis
- novapolis-dev
  - Tasks/Validatoren laufen; kurzer Leitfaden „Wie wir lokal lernen“ (optional)
- novapolis-sim
  - Für Start nicht erforderlich (später als Szenario-Generator hilfreich)

### Phasenplan (sanft, mit Fallbacks)

- Phase0 - Vorbereitung (ab sofort möglich)
  - Datenquellen fixieren (Canvases, Eval, Policies), Redaction klären, Minimal-Metriken definieren
- Phase1 - Schattenmodus (1-2 Wochen)
  - Lokale AI beantwortet parallel, keine Nutzerwirkung; Stichproben-Review 1-2×/Woche
  - Erfolg: ≥80% Accept in Stichproben, 0 kritische Policy-Verstöße
- Phase2 - RAG-only + Canary-Inferenz (5-10% oder selektive Szenen)
  - Erst RAG aktiv, dann kleine Canary-Quote mit hartem Fallback/Rate-Limit
  - Erfolg: Qualität/Latenz ≥ Status quo; Fallback selten
- Phase3 - Lernschleife v0.1 (1-2-wöchig)
  - Kuratierte Deltas → Train/Val-Pack, LoRA-Mini; Versionierung, einfache A/B-Checks

### Metriken (leichtgewichtig)

- Qualität (Stichprobe): Accept/Revise/Reject-Rate
- Policy: Block/Rewrite-Rate (kritische Verstöße = 0)
- RAG: HitRate@K, Overlap-Score mit Antwort
- Runtime: p50/p95 Latenz, Token-Längen (in/out)
- Lernen: Anteil promoteter Antworten vs. Status quo

### Datenschutz & Datenhygiene

- Redaction: Namen/Orte/IDs durch Platzhalter; Export-Prüfung vor Training
- Consent/Scope markieren (was darf ins Training)
- Retention: Rohlogs kurzlebig, kuratierte Datasets versioniert
- Audit: jede Promotion mit Quelle/Datum/Tests notieren

### Go/No-Go Checkliste (aktiv zu pflegen)

- [ ] Tests/Typen PASS (2 Tage in Folge)
- [ ] RAG-Minimum indexiert, Retriever-Test PASS
- [ ] Redaction aktiv (keine PII in Logs/Datasets)
- [ ] Flags gesetzt: `RAG_ON`, `SHADOW_ON`, `CANARY_PCT`
- [ ] Stichprobe (Schattenmodus) ≥80% „Accept“

### Nächste Schritte (sofort, ohne Codeänderungen)

- [ ] Schattenmodus-Logging mit Redaction intern aktivieren
- [ ] 10-20 Kern-Dokumente (Memory-Bundle + Schlüssel-Canvases) indexieren (RAG-Minimum)
- [ ] Wöchentlichen Review-Slot (30-45 min) für Stichproben + Kurations-Delta einplanen

Editor-Setup - .vscode-Konsolidierung (Root-zentriert)
------------------------------------------------------

Ziel: Ein einziges `.vscode/` im Repo-Root, das Standard-Tasks/Settings bereitstellt, ohne projekt-spezifische Profile (Launch/CWD/ENV) zu beschädigen. Sanft, reversibel, mit Inventur vor Migration.

### Annahmen & Rahmen

- Root verwendet `.venv` (Windows) und zentralen Interpreter (`.vscode/settings.json`).
- `novapolis_agent` ist der einzige Code-Bereich mit Tests/Launch-Profilen; `novapolis-rp` ist primär Daten/Docs/Tools.
- Markdownlint läuft via cli2 in CI; lokale Tasks existieren in Agent-Projekt (bereits erweitert um Root-`TODO.md`/`DONELOG.md`).
- Single-Root ist aktiv; Wrapper-Tasks laufen wieder stabil ab Root. Historische Multi-Root-Hinweise bleiben dokumentiert (siehe `scripts/multi_root_cleanup.py`).

### Akzeptanzkriterien

- Alle Standard-Tasks sind vom Root aus ausführbar: Lint (markdownlint), Fix, `pytest -q`, Coverage (fail-under 80).
- Tasks nutzen korrektes CWD; ENV liegt jetzt zentral im Root: `cwd=novapolis_agent/`, `envFile=.env` (Root), Interpreter aus Root `.venv`.
- Copilot-Workspace-Instructions zentral im Root; keine doppelten, widersprüchlichen Settings.
- Projekt-spezifische Launch-Profile funktionieren unverändert (zunächst im Agent-Ordner belassen).

### Plan (Etappen)

- Etappe0 - Inventur (dieser PR-Teil)
  - [x] Vorab: Multi-Root → Single-Root bereinigen (Workspace aufräumen, eindeutige Root). (Erledigt 2025-11-16 via `scripts/multi_root_cleanup.py --apply`)
  - [x] Liste aller `.vscode`-Dateien erstellen (Root, Agent, RP). (Befund 2026-02-18: nur Root-Dateien vorhanden)
  - [x] Settings/Launch/Tasks diffen und Konflikte notieren. (Befund 2026-02-18: keine Subfolder-Konflikte, Root ist kanonisch)
  - [x] Mapping definieren: was zentralisiert wird, was projekt-spezifisch bleibt. (Befund 2026-02-18: vollständig zentralisiert im Root)
- Etappe1 - Zentralisierung (additiv, ohne Löschen)
  - [x] Root-Tasks ergänzen: `pytest -q` (cwd Agent), `Tests: coverage (fail-under)`, `markdownlint (cli2)`, `markdownlint fix (cli2)` (erledigt 2026-01-07 11:39)
  - [x] Root-Settings um Copilot-Workspace-Instructions aus RP ergänzen (keine Python-Konflikte) - 2025-11-02: User-/Profil-Configs zurückgesetzt, nur Root-Settings aktiv
  - [ ] Agent-Tasks optional auf Root-Tasks verweisen (mittels eindeutiger Labels)
- Etappe2 - Bereinigung (nach 3-5Tagen stabiler Nutzung)
  - [ ] Dubletten entfernen oder Agent-`tasks.json` auf Minimal-Set reduzieren
  - [ ] Launch-Profile optional ins Root migrieren (nur wenn stabil; sonst belassen)
  - [ ] Dokumentation: kurzer Abschnitt „Editor-Setup“ im Root-README

### Aufgabenliste (konkret)

- Inventur
  - [ ] Auflisten: `.vscode/settings.json` (Root, Agent, RP), `.vscode/tasks.json` (Root, Agent), `.vscode/launch.json` (Agent)
  - [ ] Unterschiede festhalten: Interpreter-Pfad, pytestArgs, envFile, Copilot-Instructions
- Root-Tasks
  - [x] Markdownlint: lint/fix (cli2) repo-weit (Root-Tasks vorhanden)
  - [x] Tests: `pytest -q` (cwd=`novapolis_agent`)
  - [x] Tests: Coverage (fail-under=80) (Root-Wrapper `python scripts/run_pytest_coverage.py`)
  - [x] Optional: „Append DONELOG entry“ als Root-Alias mit cwd `novapolis_agent` (2025-11-01 09:05)
    - Änderung: VS Code Task `DONELOG: append entry` in `/.vscode/tasks.json` ergänzt.
    - Prüfungen: keine (reine Task-Erweiterung).
- Root-Settings
  - [x] Copilot-Workspace-Instructions aus `novapolis-rp/.vscode/settings.json` in Root übernehmen/vereinheitlichen
  - [x] Interpreter/pytestArgs zentral lassen; RP-Settings entschlacken (keine Python-Dopplung) - 2025-11-02: Profil-/User-Overrides entfernt, CWD/Interpreter nur noch im Root definiert
- Agent/RP Cleanup (Etappe2)
  - [ ] Agent-`tasks.json` Dubletten entfernen, falls Root-Tasks etabliert
  - [ ] RP-Settings auf Workspace-Instructions beschränken (falls Root diese zentral führt)

### Snapshot-Frontmatter Migration (YAML)

- [ ] Etappe 0 (2025-11-01 09:10): Regel aktiv, Mischbetrieb erlaubt — YAML bevorzugt, `Stand:`/`Letzte Aktualisierung:` weiterhin gültig.
- [x] Etappe 1: Bei Änderungen an Dokus YAML-Frontmatter ergänzen/aktualisieren (`stand`, `update`, `checks`). (laufende Regel, im aktuellen Zyklus eingehalten)
- [ ] Etappe 2: Sweep — bestehende Kopfzeilen migrieren (TODO, README/Index, Policies). Diff klein halten; `checks` kurz.
- [ ] Etappe 3: Legacy-Kopfzeilen auslaufen lassen; Instruktionen aktualisieren (nur YAML erlaubt).
- Fortschritt 2025-11-02 19:11: Root-Dokumente (`README.md`, `todo.root.md`, `single-root-todo.md`, `DONELOG.md`, `WORKSPACE_STATUS.md`) tragen konsolidierte YAML-Frontmatter; markdownlint-cli2 PASS.

### Risiken & Backout

- Risiko: Falsches CWD/ENV führt zu fehlschlagenden Tasks.
  - Mitigation: Jede Task im Root mit `options.cwd=novapolis_agent` + `envFile` testen.
- Risiko: Launch-Profile brechen bei Migration.
  - Mitigation: Launch zunächst im Agent belassen; Migration optional/später.
- Risiko: Regression auf Multi-Root-Konfiguration.
  - Mitigation: `scripts/multi_root_cleanup.py --whatif` regelmäßig ausführen; neue `.code-workspace`-Artefakte sofort in `Backups/` verschieben.
- Backout: Sub-`.vscode` beibehalten bis Etappe2; jederzeit reaktivierbar.

### Betroffene Dateien (geplant)

- `/.vscode/settings.json` (merge Workspace-Instructions)
- `/.vscode/tasks.json` (ergänzte Root-Tasks)
- `/novapolis_agent/.vscode/tasks.json` (später reduzieren)
- `/novapolis_agent/.vscode/launch.json` (vorerst unverändert)
- `/novapolis-rp/.vscode/settings.json` (später verschlanken)

### Go/No-Go für Migration

- [x] Root-Tasks laufen (lint, fix, pytest, coverage) — vollständiger Root-Durchlauf erneut grün verifiziert (2026-02-18 04:50).
- [x] Keine Konflikte in Settings (Interpreter/ENV) — Root-`.vscode` ist kanonisch und konsistent; kein akuter Konfliktbefund (2026-02-18 04:50).
- [ ] 3-5Tage Nutzung ohne Beschwerden → Go für Etappe2

Aktiv vs. Historisch
--------------------

- `todo.root.md` führt nur den aktiven Arbeitsbacklog als offene Checkboxen.
- Historische TODO-Snapshots werden ausschließlich als Referenz im Archiv gehalten und enthalten hier keine offenen Checkboxen.

Historische Referenzen (nur lesend)
-----------------------------------

- Agent-Archiv: `novapolis-dev/archive/todo.agent.archive.md`
- Root-Archiv: `novapolis-dev/archive/todo.root.archive.md`
- Historischer Kontext/Donelog: `novapolis-dev/docs/donelog.md`



