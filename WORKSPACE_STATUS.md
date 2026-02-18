---
stand: 2026-02-18 06:35
update: S3/S4 abgeschlossen (Review-Rhythmus gesetzt, Editor-Setup Etappe 1/2 verifiziert); S5 bleibt bis zum 3-5-Tage-Stabilitätsfenster offen.
checks: F:/VS-Code-Workspace/Main/.venv/Scripts/python.exe -m ruff check . PASS (2026-02-18 06:33); F:/VS-Code-Workspace/Main/.venv/Scripts/python.exe scripts/tests_pytest_root.py PASS (2026-02-18 06:34); F:/VS-Code-Workspace/Main/.venv/Scripts/python.exe -c "import json, pathlib; json.loads(pathlib.Path('.vscode/launch.json').read_text(encoding='utf-8')); print('launch.json: valid')" PASS (2026-02-18 06:32); file_search '**/.vscode/tasks.json' und '**/.vscode/launch.json' je 1 Root-Treffer (2026-02-18 06:32)
---
- 2026-02-18 06:34: S3 abgeschlossen: fester Betriebsreview-Slot gesetzt (Mittwoch 09:00-09:45, lokal), Checkliste für lokale AI verankert und erster Slot protokolliert.
- 2026-02-18 06:34: S4 abgeschlossen: keine Subfolder-`.vscode`-Konflikte (nur Root `tasks.json`/`launch.json`), `launch.json` valide, Root-Tasks (`ruff`, Root-`pytest`) lauffähig.
- 2026-02-18 06:34: S5 bleibt offen wegen Zeit-Gate; früheste Freigabe Etappe 2/3 bei weiter stabiler Laufpraxis ab 2026-02-21.
- 2026-02-18 05:27: Später-Block S2 abgeschlossen. Shadow-Logging aktiv über `SHADOW_MODE_LOGGING_ENABLED` (hash-basiertes JSONL), Artefaktpfad `.tmp/results/logs/shadow_mode.jsonl` bestätigt; RAG-Basisindex (`novapolis_agent/eval/results/rag/s2-core-index-20260218.json`) und Redaction/Flags-Stichprobe (`tests/test_api_chat_internal_branches.py`, `tests/test_rag_guards.py`) PASS.
- 2026-02-18 05:16: Nächster offener Punkt S2 gestartet. RAG-Minimum-Stichprobe erzeugt (`novapolis_agent/eval/results/rag/s2-core-index-20260218.json`, 11 Kern-Dokumente) und gezielte Flags/Redaction-Stichprobe erfolgreich (`tests/test_rag_guards.py`, `tests/test_api_chat_internal_branches.py` PASS). S2 bleibt offen bis Schattenmodus-Logging aktiv dokumentiert ist.
- 2026-02-18 05:13: Später-Block S1 abgeschlossen (Tag 2/2 erfolgreich). Root-Gates erneut grün: `lint:ruff` PASS, Root-Pytest PASS, Coverage PASS (`83.02%`, `354 passed, 1 skipped`). Damit ist das 2-Tage-Stabilitätsgate erfüllt.
- 2026-02-18 05:05: Später-Block S1 (Tag 1/2) operativ gelaufen. Root-Gates erneut grün: `lint:ruff` PASS, Root-Pytest PASS, Coverage PASS (`83.02%`, `354 passed, 1 skipped`). Für S1 verbleibt Tag 2 als Abschluss gegen das 2-Tage-Stabilitätsgate.
- 2026-02-18 04:50: Root-Go/No-Go erneut komplett verifiziert: `lint:ruff`, `fix:ruff`, Root-Pytest und Coverage-Wrapper laufen grün; Coverage steht bei 83.02%. Zusätzlich Editor-Setup Etappe 0 abgeschlossen (nur Root-`.vscode` vorhanden: `settings.json`, `tasks.json`, `launch.json`; keine Subfolder-Konflikte).
- 2026-02-18 04:35: Coverage-Gate neu verifiziert: `scripts/run_pytest_coverage.py` läuft ohne Import-/Dependency-Fehler, scheitert aber korrekt am Fail-Under (`76.07% < 80%`, 354 passed, 1 skipped). Root-Go/No-Go bleibt damit fachlich offen (kein Environment-Blocker mehr).
- 2026-02-18 04:15: Jetzt-Block-Umsetzung: Import-Fallbacks in Consistency/Audit vereinheitlicht, Artefakt-/Gitignore-Prüfung erledigt, Frontmatter-Rerun für `novapolis-rp/database-rp` PASS. Root-Go/No-Go bleibt offen, da Coverage-/pytest-Läufe im aktuellen Environment auf fehlende Pakete (`fastapi`, `uvicorn`) laufen.
- 2026-02-18 04:12: Priorisierung der offenen aktiven TODOs abgeschlossen. Triageliste (`Jetzt`, `Später`, `Optional`) ist in `todo.root.md` ergänzt und dient als Reihenfolge für Folgeumsetzungen.
- 2026-02-18 04:12: `todo.root.md` bereinigt: Historischer Volltext in Referenzblock überführt, sodass offene Checkboxen nur noch im aktiven Backlog liegen.
- 2026-02-18 04:00: Metadata-Init konsolidiert: `novapolis-rp/coding/tools/metadata/init_metadata.py` ist kanonisch dokumentiert, die frühere JS-Variante `init-metadata.js` wurde entfernt.
- 2026-02-18 04:00: Alt-Analyse chat_routers abgeschlossen: Inhalt war bereits in `novapolis_agent/cleanup_recommendations.md` enthalten; `WORKSPACE_INDEX.md`-Verweis auf `novapolis_agent/analysis_chat_routers.md` entfernt und die Legacy-Datei gelöscht.
- 2026-02-18 03:57: Staging-Integration abgeschlossen: `resolved.md`, `uncertainties.md`, `dedupe-chat-export.md` aktualisiert gespiegelt; `delta-*.md` und `overlap-*.md` als Referenzanhang in `novapolis-dev/docs/process/rp-canvas-rescue/` übernommen; Marker `generated-artifacts.md` dort ergänzt. Vorversionen der A-Dateien liegen in `novapolis-dev/archive/quarantine/rp-canvas-rescue-presync-20260218_0357`.
- 2026-02-17 23:38: Verifikation bestätigt: Alle 5 priorisierten Schritte sind korrekt umgesetzt. Nächste offenen TODOs: Staging-Integration (A/B/C) in `novapolis-dev/docs` finalisieren, `analysis_chat_routers.md` in aktive Doku überführen/entscheiden, Metadata-Init (`init-metadata.js` vs. `init_metadata.py`) konsolidieren, Import-Fallbacks in Consistency/Audit-Skripten vereinheitlichen.
- 2026-02-17 20:49: Wrapper-Migration abgeschlossen – aktive Entrypoints/Tasks laufen über Python (`scripts/*.py`, `.venv\Scripts\python.exe`); PowerShell-Wrapper verbleiben ausschließlich im Archiv.
- 2026-02-17 20:49: Ruff-Triage aktualisiert – initial 1 Treffer (`scripts/merge_todos.py`, Import-Order), per `fix:ruff` behoben; Re-Run `lint:ruff` PASS.
- 2026-02-17 20:49: RP-Export-Konsolidierung erneuert – `scripts/run_rp_chat_dedupe.py` schrieb `database-curated/staging/chat-export-consolidated.normalized.txt` und aktualisierte `staging/reports/dedupe-chat-export.md`.
- 2026-02-17 20:49: Staging-Reports als generiert markiert – Markerdatei `novapolis-rp/database-curated/staging/reports/generated-artifacts.md` ergänzt (keine Löschungen).
- 2026-02-17 20:49: Konsistenz-Report erneuert – `novapolis_agent/scripts/reports/generate_consistency_report.py` erzeugte `novapolis_agent/eval/results/reports/consistency/20260217_2047`.
- 2026-01-05 19:07: Unified Runner erneut verifiziert – `scripts/checks_rp_consistency.py` Ruff/Black gruen gemacht; `python scripts/run_checks_and_report.py` overall PASS (Report: `checks_report_20260105_190519.json`).
- 2026-01-07 03:57: Schritt 3: Doku-Verweise fuer Temp-Artefakte konsolidiert (`/.tmp-results/` -> `/.tmp/results/`).
- 2025-12-30 05:32: RP-SSOT bereinigt – Frontmatter-Duplikate entfernt in `database-rp/00-admin/canon-canvas.draft.md`, `05-projects/Nordlinie-01.md`, `02-characters/Jonas-Merek.md`, `03-locations/C6.md`; in `Nordlinie-01.md` zusätzlich relative Links auf Admin-Dokus korrigiert; targeted markdownlint/frontmatter PASS.
- 2025-12-30 06:53: RP-SSOT Slugs nachgezogen (10 Dateien) – `scripts/checks_rp_consistency.py` jetzt ohne missing_slug/warnings; targeted Frontmatter-Validator + markdownlint PASS.
- 2025-12-30 21:02: Frontmatter-Validator repo-weit repariert – `.tmp/` und `.tmp-results/` werden nun geskippt; Frontmatter ergänzt in `PR_DESCRIPTION.md` und `context.local.md` (2×); `python scripts/check_frontmatter.py` PASS.
- 2025-12-10 17:49: RP Alias-Stopword Fix & Tagging 009-001 Refresh – `tag_chunks_from_yaml.py` ignoriert jetzt generische Aliase („verbindungstunnel“), Range 009-001 erneut als Dry→Write gelaufen, `lexicon.json`/`unresolved.json` kollisionsfrei und `part-002.tagged.txt` ohne Doppel-[LOC]; targeted markdownlint + `python scripts/check_frontmatter.py` (TODO/DONELOG/Status/Temp-TODO) PASS.
- 2025-12-08 17:55: STOP-Plan 009-001 Nachbereitung abgeschlossen – Tree-Artefakte (`workspace_tree_full.txt`, `workspace_tree.txt`, `workspace_tree_dirs.txt`) via `tree /A /F`, `tree /A` und `python scripts/update_workspace_tree_dirs.py` erneut erzeugt; targeted `npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'todo.root.md DONELOG.md novapolis-dev/docs/donelog.md WORKSPACE_STATUS.md .tmp/results/todo.cleaned.md'` + `python scripts/check_frontmatter.py` PASS; `todo.root.md`, `.tmp/results/todo.cleaned.md`, DONELOGs und WORKSPACE_STATUS synchronisiert (damaliger Stand: Alias-Follow-up „Verbindungstunnel“ noch offen, inzwischen behoben).
- 2025-12-01 08:47: Tagging-Pipeline (novapolis-rp) Range 009-001 (Dry→Write) ausgeführt – Backups `AI-Behavior-Mapping-20251201-081946.{md,json}` vorab erstellt, Snapshot `Backups/tagging-009-001-prewrite.txt` aus HEAD-Liste abgelegt, Dry-Run meldete keine `unresolved_dependencies` (nur Alias-Kollision `verbindungstunnel`), Write-Run erzeugte `.tagged` 009→001 + aktualisierte `index_review.json`/`lexicon.json`/`unresolved.json`; targeted markdownlint + `python scripts/check_frontmatter.py` (Scope: Root/Dev TODO/DONELOG/Status) am 2025-12-01 PASS, Tree-Snapshots folgen separat.
- 2025-11-30 08:13: Doku-/Statussync nach dem 015-010 Refresh (Root/Dev TODOs, DONELOGs, WORKSPACE_STATUS, Temp-TODO) abgeschlossen; STOP-Plan 009-001 mit Backups/Dry-Run/Write/Nachbereitung dokumentiert (keine neuen Skriptläufe).
- 2025-11-27 22:10: Tagging-Pipeline (novapolis-rp) Range 015-010 erfolgreich erneut ausgeführt – Backups (`AI-Behavior-Mapping-20251127-220319.*`, `Backups/tagging-015-010-prewrite.txt`), Report `reports/tagging-20251127T212031Z.log`, Tree-Snapshots & Status-Doku synchronisiert, targeted markdownlint/frontmatter PASS.
- 2025-11-27 03:25: RP-Lexikon bereinigt – fehlende Slugs (ai_behavior_index_v2, logistik, missionslog, Wissenstands-Canvas) ergänzt, neue Admin/Faktions-Stubs (`cluster_index_v1`, `relationslog_eisenkonklave_v1`, `handel_diplomatie_haendlergilde_v1`, `index_haendlergilde_v1`, `eisenkonklave`) angelegt, `caravan_moves`-Slug vereinheitlicht. `tag_chunks_from_yaml.py` aktualisiert (alias-Kollisionen C6 vs. C6-Nord beseitigt, Redirects erweitert). Dry-Run (015-010) bestätigt: `unresolved_dependencies` leer, verbleibende Alias-Kollisionen nur bei Mehrfach-Titeln (Echo/Reflex Wissenstands-Canvas). Plan für Range 009-001 im Dev-Hub notiert.

Recent Changes
--------------

- 2026-02-18 03:57: Offenes TODO „Übernahme/Staging-Integration" abgeschlossen: A/B-Dateien aus `staging/reports` nach `novapolis-dev/docs/process/rp-canvas-rescue/` gespiegelt; C-Artefakte per Marker dokumentiert; Altstände revisionssicher im Quarantänepfad archiviert.
- 2026-02-17 23:38: Verifikation der Umsetzung „5→3→1→2→4“ abgeschlossen (dokumentarisch + Artefakte + Live-Ruff). Folgeprioritäten aus `todo.root.md` gezogen: Staging-Integration finalisieren, Alt-Analyse Router-Doku entscheiden, Metadata-Init konsolidieren, Consistency/Audit-Importpfade vereinheitlichen.
- 2025-12-10 17:49: RP Alias-Stopword Fix & Tagging 009-001 Refresh – Skript filtert nun generische Aliase, Dry→Write-Lauf (009-001) aktualisierte `.tagged` 009→001 sowie `lexicon.json`/`unresolved.json`, part-002-Tabellen enthalten keine `[LOC:verbindungstunnel-c6-e3]` mehr; targeted markdownlint + `python scripts/check_frontmatter.py` für TODO/DONELOG/Status/Temp-TODO PASS.
- 2025-12-08 17:55: STOP-Plan 009-001 Nachbereitung – Tree-Artefakte (`workspace_tree_full.txt`, `workspace_tree.txt`, `workspace_tree_dirs.txt`) via `tree /A /F`, `tree /A` und `python scripts/update_workspace_tree_dirs.py` aktualisiert, targeted markdownlint + `python scripts/check_frontmatter.py` im üblichen Scope PASS, Doc/TODO/DONELOG/Status synchronisiert (Alias-Follow-up zu diesem Zeitpunkt noch offen, s. 2025-12-10).
- 2025-12-01 08:47: novapolis-rp Tagging-Pipeline Range 009-001 (Dry→Write) durchgeführt – Backups/Snapshot dokumentiert, `.tagged` 009→001 + Index/Lexicon/Unresolved aktualisiert; targeted markdownlint + `python scripts/check_frontmatter.py` (Scope: Root/Dev TODO/DONELOG/Status) am 2025-12-01 PASS, Tree-Snapshots folgen separat.
- 2025-11-30 08:13: Root-/Hub-Dokumente und Temp-TODO nach dem 015-010 Refresh synchronisiert; neue STOP-Plan-Details für Range 009-001 (Backups/Dry-Run/Write/Nachbereitung) hinzugefügt. Keine neuen Skriptläufe.
- 2025-11-27 22:10: novapolis-rp Tagging-Pipeline Range 015-010 (Dry→Write) erneut ausgeführt – Backups & Hash-Snapshot erstellt, Report `reports/tagging-20251127T212031Z.log`, Tree-Snapshots/DONELOG/TODO/Status synchronisiert, targeted markdownlint und `scripts/check_frontmatter.py` PASS.
- 2025-11-17 04:55: `novapolis_agent/app/routers` und `app/services/llm.py` endgültig entfernt (inkl. Mirror-Pakete + LLM-Tests); `WORKSPACE_INDEX.md`, `cleanup_recommendations.md` und DONELOGs aktualisiert.
 - 2025-11-17 09:40: Archivierung abgeschlossen: `novapolis_agent/app`-Stubs nach `novapolis_agent/archive/app/` verschoben; Live-Stubs durch explizite Import-Marker ersetzt; `app/__init__.py` Shim im Repo-Root hinzugefügt; Tests und Index aktualisiert. Commits: `1df7561`, `6191a5d`.
- 2025-11-15 09:27: Frontmatter-Autofix + `--touch` (Stand-Aktualisierung) in `scripts/check_frontmatter.py` ergänzt; Governance-Referenzblock erweitert; Validator PASS (`python scripts/check_frontmatter.py`).
- 2025-11-15 09:20: Dokumentationssweep (context.local.md Frontmatter repariert, todo/Status/Index aktualisiert); Frontmatter-Validator PASS (`python scripts/check_frontmatter.py`).
- 2025-11-15 09:00: Dokumentationssweep (context.local.md Frontmatter repariert, todo/Status/Index aktualisiert); Frontmatter-Validator PASS (`python scripts/check_frontmatter.py`).
- 2025-11-12 03:37: Checks: full Review abgeschlossen (damals PowerShell-Runner, inzwischen durch `python scripts/run_checks_and_report.py` ersetzt; PSScriptAnalyzer-Phase verifiziert, Receipt-Struktur JSON + Postflight-Vorlage bestätigt). Link-Scanner Rescan nun 0 defekte Verweise.
 - 2025-11-16 04:54: Sim headless verification: `novapolis-sim/project.godot` loaded headless with Godot Engine `v4.5.1.stable.official.f62fdbde1` — PASS. Log: `.tmp/results/logs/godot_headless_20251116_045407.log`. Postflight Donelog entry added to `novapolis-dev/docs/donelog.md`.
- 2025-11-12 02:46: Governance: Vorangestellte Start-Checks entfernt aus `.github/copilot-instructions.md`; Postflight-Formulierung präzisiert (finaler Block am Ende der Nachricht); Headings-Extrakt aktualisiert & veraltete Regel-ID-Vorschläge gestrichen; Lint PASS (`.github/copilot-instructions-headings.md`).
- 2025-11-26 05:35: novapolis-rp Tagging-Pipeline Range 015-010 (Dry→Write) abgeschlossen – Backups (AI-Behavior-Mapping, Tree-Snapshot) erstellt, neue `part-015.tagged.txt` … `part-010.tagged.txt` + aktualisierte `index_review.json`/`unresolved.json`/`lexicon.json` unter `novapolis-rp/database-curated/reviewed/chat-export (1)/`, Report `reports/tagging-20251126T043409Z.log` abgelegt. Targeted markdownlint/frontmatter PASS, weitere Dokumentation (DONELOG/TODO/Status) in Arbeit.
- 2025-11-26 05:36: Tree-Artefakte (`workspace_tree_full.txt`, `workspace_tree.txt`, `workspace_tree_dirs.txt`) neu generiert (`tree /A /F` + `python scripts/update_workspace_tree_dirs.py`). Snapshot-Stand jetzt 2025-11-26 05:36; Status-/Index-Dokumente werden gleichgezogen.


 - 2025-11-16 07:50: Root-Postflight: `python scripts/run_checks_and_report.py` + `python scripts/run_pytest_coverage.py --fail-under 80` ausgeführt.
  - Ergebnis: Checks-Wrapper JSON/MD: `.tmp/results/reports/checks_report_20251116_074933.{json,md}` — Gesamtstatus: **FAIL** (Lint/Format/Markdown-Checks)
   - Coverage: **83.96%** (Fail-Under 80) — Gate: PASS
   - Offene Befunde: `markdownlint` (28 Treffer), `ruff` (35 Treffer), `black` (2 Dateien würden formatiert)
  - Logs/Details: `.tmp/results/reports/checks_run_20251116_074933/`
   - Aktionsempfehlung: `npx markdownlint-cli2` → `ruff --fix` → `black .` → `pyright` installieren und erneut prüfen.

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
- Hinweis (2026-01-08): Ältere Einträge können noch `.ps1` referenzieren (historisch). Aktive Wrapper/Entry-Points laufen über `scripts/*.py`; PowerShell-Wrapper liegen nur noch im Archiv.

- 2025-12-08 17:50: Tree-Snapshots (`workspace_tree_full.txt`, `workspace_tree.txt`, `workspace_tree_dirs.txt`) erneut generiert (`tree /A /F`, `tree /A`, `python scripts/update_workspace_tree_dirs.py`); nächster Pflichtlauf nach relevanter Strukturänderung oder spätestens Ende Dezember.
- 2025-11-07 06:30: Alle Markdownlint VS-Code-Tasks & Wrapper-Doku entfernt; Ausführung jetzt ausschließlich manuell via `npx --yes markdownlint-cli2` (Policy npx-only).
- 2025-11-07 02:10: markdownlint-cli2 repo-weit ausgeführt (367× MD003 offen); Skriptprüfung für Markdown-Ausgaben (Chat-Exporter, Reports, todo_gather) vorbereitet.
- 2025-11-07 01:39: TODO aktualisiert (Single-Repo-Reminder; Aufgaben zu Lint-Overrides, Staging-Reports, Metadata-Konsolidierung, Archiv-Ablage).
- 2025-11-07 01:27: Konfliktanalyse durchgeführt (Markdownlint-Overrides, Staging-Reports ohne Frontmatter, doppelte Metadata-Skripte, Chat-Router-Notiz). Maßnahmen in TODO/DONELOG erfasst.
- Mono-Repo bündelt `novapolis_agent`, `novapolis-rp`, `novapolis-dev`, `novapolis-sim`, gemeinsame Pakete unter `packages/`
- Produktiver Code liegt ausschließlich im Agent-Backend; RP-Workspace enthält weiterhin Daten, Workflows, Tools
- Root-Dokumente (`README.md`, `todo.root.md`, `WORKSPACE_STATUS.md`) wurden am 2025-11-02 synchronisiert und liefern Einstieg ohne Projektwechsel
- Kopilot-Anweisungen konsolidiert unter `.github/copilot-instructions.md`
- Struktur-Snapshots (`workspace_tree.txt`, `workspace_tree_dirs.txt`, `workspace_tree_full.txt`) zuletzt am 2025-11-27 22:12 via `tree /A /F`, `tree /A` und `python scripts/update_workspace_tree_dirs.py` regeneriert; nächste Prüfung nach größeren Strukturänderungen oder spätestens Mitte Dezember.
- PowerShell-Standard: Terminal-Profile & VS-Code-Tasks laufen jetzt über `pwsh` 7.5.4; Windows PowerShell bleibt nur noch Fallback.

Aktueller Arbeitsmodus
----------------------

- Modus: General (GPT-5)
- STOP-Gate: an (vor Code-/kanon-kritischen Aktionen explizite Bestätigung erforderlich)
- Erinnerungen: Wechselhinweise bei Code-Triggern aktiv; „Bitte nicht erinnern“ schaltet Hinweise ab bis zur Reaktivierung

Aktueller Arbeitsmodus (Single-Root, Python @ Root)
--------------------------------------------------

- Workspace & Interpreter: `F:/VS-Code-Workspace/Main` ist der einzige VS-Code-Root; `.venv` (Python 3.11/3.12+) und `.env` liegen im Root.
- Standard-Wrappers: `python scripts/run_checks_and_report.py --scope full` (Lint/Typen/Tests) und `python scripts/run_pytest_coverage.py --fail-under 80` (Coverage) laufen aus dem Root; PowerShell-Wrapper sind nur noch archiviert.
- Tasks setzen `options.cwd` gezielt (z. B. `novapolis_agent/` für pytest), bleiben aber über das Root-`.vscode/tasks.json` steuerbar.
- Guard-Check: `python scripts/multi_root_cleanup.py --whatif` prüft regelmäßig auf neue `*.code-workspace`-/Schatten-Dateien; Auffälligkeiten sofort nach `Backups/` verschieben.

Health-Checks & Open Items
---------------------------

- Tests (2025-11-10 08:19 targeted): `pytest tests/test_tools_registry.py` PASS (Tool-Registry Alias-Fix verifiziert); Vorlauf 2025-11-09 22:11 (`pytest` 298 passed, 1 skipped; Coverage 81.66%; Frontmatter-Validator PASS nach Fix an `todo.root.md`).
- Typen: Letzter vollständiger Lauf unverändert grün (pyright/mypy - keine neuen Fehler seit vorherigem Bericht); Folge-Lauf geplant nach nächster Codeänderung.
- TODO-Backlog: siehe `todo.root.md` (Stand 2025-11-07; Fokus Agent: RAG/Tool-Use/Policies, RP: Kurations-Pipeline & Canvas-Pflege, Skriptprüfung für Markdown-Ausgaben)
- Policies & Behaviour: maßgeblich `.github/copilot-instructions.md` (SSOT)
- Risiken kurz:
  - Verzeichnis-Bulk unter `outputs/` (LoRA-Runs) wächst; mittelfristig archivieren oder auslagern
  - RP-Datenpflege erfordert regelmäßigen Sync mit Memory-Bundle (seit 2025-11-02 aktualisiert, siehe `novapolis-rp/database-rp/00-admin/memory-bundle.md`)
  - Tree-Snapshots aktuell Stand 2025-12-08 17:50; nächster Refresh nach der nächsten Strukturinventur oder spätestens Ende Dezember
  - VS-Code-Settings: Nutzer-/Profil-Overrides entfernt, nur Root-Workspace-Config aktiv
  - VS Code Multi-Root (historischer Fall, inzwischen bereinigt): Multi-Root-Workspace-Datei (`*.code-workspace`) entfernt/archiviert; Root wird als Single-Root genutzt. Wrapper-Tasks sind für standardisierte Prüf-/Testläufe wieder erlaubt (R-WRAP), Multi-Root-Fallakte bleibt als Historie (`novapolis-dev/logs/open-case-terminal-multi-root-20251103.md`).

Single-Root & Wrapper-Status (ehemals Multi-Root, Stand 2025-11-16 12:00)
-------------------------------------------------------------------------

- Workspace: Single-Root (VS Code öffnet den Ordner `Main` direkt; keine aktiven Multi-Root-Workspace-Dateien mehr; frühere Multi-Root-Konfiguration nur noch historisch relevant).
- Wrapper-Policy: Mehrschrittprozesse (Lint/Typen/Tests/Coverage) sollen bevorzugt über Skript-Wrapper laufen:
  - Checks-Wrapper: `python scripts/run_checks_and_report.py` ist der einzige Entry-Point für „Checks: full“.
  - Coverage-Wrapper: `python scripts/run_pytest_coverage.py --fail-under <threshold>` für kombinierte Coverage-Läufe (R-COV); PowerShell-Fallback nur archiviert.
- STOP-Gate (R-STOP/R-WRAP):
  - Reine Lese-Operationen (z. B. `tree`, `git status`, `cat`/`Get-Content`) benötigen keinen zusätzlichen Guard.
  - Aktionen mit Seiteneffekt (WRITE/RUN, z. B. Skript-Wrapper, Formatierer, Cleanup) bleiben STOP-pflichtig (kurzer Plan + Receipt).
- Akzeptanzkriterien erfüllt:
  - Keine `*.code-workspace` im Workspace aktiv.
  - Wrapper-Skripte sind im Root verankert (`scripts/run_checks_and_report.py`, `scripts/run_pytest_coverage.py`).
  - Dieser Statusblock dokumentiert den Abschluss des Multi-Root-Falls.

Status-Update (Multi-Root Abschluss)
-----------------------------------
- Multi-Root abgeschlossen: Zeitstempel: 2025-11-16 12:37, Commit: <git-short-hash>, Gefundene `*.code-workspace`=1, Verschoben nach `Backups/`=1, Weitere Artefakte (`README.md.bak`,`lint.out`)=2 verschoben. Wrapper-Test: `python scripts/run_checks_and_report.py --whatif` (ExitCode=0, Output="WhatIf: no changes made"). Receipt in `DONELOG.md`.

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

- Vollständiger Verzeichnisbaum: `workspace_tree_full.txt` (Stand 2025-11-27 22:12; Terminal `tree /A /F`)
- Arbeitsansicht: `workspace_tree.txt` (Stand 2025-11-27 22:12; Terminal `tree /A`) und kompaktes Verzeichnis-Listing `workspace_tree_dirs.txt` (Stand 2025-11-27 22:12; `python scripts/update_workspace_tree_dirs.py`)
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
 - Link-Scanner: Nach Index-Anpassungen wurde `scripts/scan_links.py --files WORKSPACE_INDEX.md` am 2025-11-16 03:37 ausgeführt; Report unter `.tmp/results/reports/scan_links_20251116_033738.*`, Postflight in `novapolis-dev/archive/docs/donelogs/scan_links_postflight_20251116_033738.md` dokumentiert (0 kritische Broken-Links im Index).



