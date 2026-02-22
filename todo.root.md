---
stand: 2026-02-21 08:08
update: Abgeschlossene Root- und Modulbloecke in die passenden Archive ueberfuehrt; aktiver Backlog in todo.root weiter verschlankt.
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
  - [x] Altbestände nach Runs gruppieren (z. B. `outputs/lora-YYYYMMDD_HHMM` → einzelnes ZIP in `Backups/model-runs/`). (2026-02-19: `Backups/model-runs/lora-runs-batch-20260219.zip` erstellt)
  - [x] Eval-Resultate aus Vor-Umbenennung auf neue Paketpfade prüfen und Meta-Felder ggf. nachziehen (`eval/results/**/*.jsonl`). (2026-02-19 Audit: `jsonl_scanned=1346`, `files_with_path_hits=0`)
  - [x] README oder `Backups/`-Manifest um Rotationsplan ergänzen (Aufbewahrungsdauer, Löschkriterien). (erledigt: `Backups/README.md`, Stand 2026-02-18)
  - [x] Automatisierte Aufgabe/Script prüfen (Cleanup-Phasen, historisch im Archiv) für regelmäßiges Auslagern. (2026-02-19: `scripts.rotate_backups` Dry-Run PASS; `scripts.update_backups_manifest --include-subdirectories` ausgeführt)
 - **Lokale AI Einbindung (organisch)**: Phasenplan/Go-Kriterien/Metriken in Abschnitt „Lokale AI - Einbindung (organisch)“ unten; Start mit Phase01 möglich (ohne Zeitdruck, mit harten Fallbacks).
 - **Editor-Setup**: Konsolidierung `.vscode` auf Root vorbereiten (siehe Abschnitt „Editor-Setup - .vscode-Konsolidierung (Root-zentriert)“).

- Neu (2025-11-06): Modulstatus → Agent: Gelb-grün, Dev: Grün, RP: Gelb, Sim: Gelb. Konkrete 1-2-Tage-Schritte siehe Abschnitt „Nächstes Vorgehen (1-2 Tage)“.

Wrapper-Migration (.ps1 → .py)
------------------------------

- Vollstaendig abgeschlossener Block wurde inhaltlich nach `novapolis-dev/archive/todo.root.archive.md` verschoben.
- Validiert vor Verschiebung:
  - keine aktiven `scripts/*.ps1` im Root,
  - produktive Python-Einstiegspunkte vorhanden (`scripts/run_pytest_coverage.py`, `scripts/checks_linters.py`, `scripts/checks_types.py`, `scripts/tests_pytest_root.py`),
  - historische `.ps1`-Wrapper liegen im Archivpfad `novapolis-dev/archive/scripts/scripts.ps1-scripts/`.

Modulstatus (2025-11-06)
------------------------

- Agent (Backend): Gelb-grün. Tests/Typen zuletzt grün, aber kein dokumentierter Lauf seit 2025-10-31; leichte Driftgefahr bei Scripts/Eval-Artefakten.
- RP (Daten/Canvases): Gelb. Kurations-Pipeline aktiv, einige Review-/Tagging-Schritte offen.
- Dev (Dok-Hub): Grün. Frontmatter-Migration weitgehend durch, Donelog/Index gepflegt.
- Sim (Godot): Gelb. Option A gesetzt, Projektdatei kanonisch; Headless-Lade-Check offen.

Nächstes Vorgehen (1-2 Tage)
- Vollstaendig abgeschlossener Block wurde inhaltlich nach `novapolis-dev/archive/todo.root.archive.md` verschoben.
- Validiert vor Verschiebung:
  - alle Punkte abgeschlossen,
  - Details und Evidenz bleiben im Root-Archiv nachvollziehbar.

Priorisierung (Stand 2026-02-18, aktualisiert)
--------------------------------

### Jetzt

- Vollstaendig abgeschlossener Block wurde inhaltlich nach `novapolis-dev/archive/todo.root.archive.md` verschoben.
- Validiert vor Verschiebung:
  - relevante Skripte vorhanden (`novapolis_agent/scripts/reports/generate_consistency_report.py`, `novapolis_agent/scripts/audit_workspace.py`),
  - RP-Backlog-Marker vorhanden (`novapolis-rp/database-curated/staging/reports/generated-artifacts.md`),
  - Root-Task-Konfiguration weiterhin zentral vorhanden (`.vscode/tasks.json`).

### Später

- Vollstaendig abgeschlossener Teilblock `S1-S4` wurde inhaltlich nach `novapolis-dev/archive/todo.root.archive.md` verschoben.
- Validiert vor Verschiebung:
  - S2-Evidenzdateien vorhanden (`novapolis_agent/eval/results/rag/s2-core-index-20260218.json`, `.tmp/results/logs/shadow_mode.jsonl`),
  - Root-Editor-Setup weiterhin konsistent (`.vscode/tasks.json`, `.vscode/launch.json`),
  - S5 bleibt aktiv offen und verbleibt hier unveraendert.
- [ ] S5 - Snapshot-Frontmatter-Migration Etappe 2/3 freigeben:
  - Sweep + Legacy-Auslauf nur nach 3-5 Tagen stabiler Laufpraxis ohne Beschwerden ausführen.
  - Status: offen wegen Zeit-Gate (früheste Freigabe bei stabiler Laufpraxis ab 2026-02-21).
  - Vorprüfung 2026-02-19: Legacy-Header-Scan (`^(Stand|Letzte Aktualisierung):`) ergab `360` Treffer bei `490` gescannten Markdown-Dateien (ohne Archiv/.venv/node_modules) - Etappe 2 bleibt ein geplanter Sweep nach Freigabe.
  - Prework 2026-02-19 (ausführungsreif): Etappe-2-Sweep in Wellen vorbereiten, Reihenfolge:
    1) Root-Kerndokus (`README.md`, `todo.root.md`, `DONELOG.md`, `WORKSPACE_STATUS.md`, `WORKSPACE_INDEX.md`, `PR_DESCRIPTION.md`) + Archivkopie `novapolis-dev/archive/quarantine/single-root-todo.md`
    2) `novapolis-dev/docs/**` und `novapolis_agent/docs/**`
    3) `novapolis-rp/database-rp/**` + Rest-README-Dateien
    4) Backups-/historische Referenzen nur nach separater Freigabe
  - Baseline-Update 2026-02-19: `scripts/scan_legacy_markdown_headers.py` erzeugte `.tmp/results/reports/legacy_header_scan_20260219_230710.md` (`files_scanned=490`, `legacy_hits=3`; Wellen: `0/1/1/1`).
  - Gate S5 (Migration-Go/No-Go): Freigabevermerk in `WORKSPACE_STATUS.md` + Abschlussblock in `DONELOG.md`.

### Optional

- Abgeschlossene Teilpunkte wurden inhaltlich nach `novapolis-dev/archive/todo.root.archive.md` verschoben.
- [ ] Etappe-3-Legacy-Ablösung der Snapshot-Frontmatter-Migration erst nach stabiler Laufpraxis (nur falls Etappe 2 abgeschlossen).

### novapolis_agent
- Vollstaendig abgeschlossene Modulbloecke wurden inhaltlich in die Modularchive ueberfuehrt:
  - Agent: `novapolis-dev/archive/todo.agent.archive.md`
  - Dev: `novapolis-dev/archive/todo.dev.archive.md`
  - Sim: `novapolis-dev/archive/todo.sim.archive.md`
- Aktiver Root-Backlog verbleibt hier bewusst nur mit offenen/querschnittlichen Punkten.

- Risiken (kurz)
--------------

- Tests/Typing nicht tagesaktuell (Agent) → mögliche stille Drift.
- RP: Offene Tagging-/Export-Schritte; Deltas noch nicht vollständig in SSOT gespiegelt.
- Single-Root-Governance: Neu auftauchende `.code-workspace`/`*.bak`-Dateien regelmäßig via `scripts/multi_root_cleanup.py --whatif` prüfen (R-STOP/R-WRAP).

Lokale AI - Einbindung (organisch)
----------------------------------

Kurz: Nicht beschleunigen, sondern sauber einführen. Schattenmodus → kleiner Canary → begrenzte Beta, mit Redaction/Flags/Metriken und klaren Rückfallpfaden.

### Zusammenfassung (Checkliste)

- Vollstaendig abgeschlossener Block wurde inhaltlich nach `novapolis-dev/archive/todo.root.archive.md` verschoben.
- Validiert vor Verschiebung:
  - Go/No-Go-Checkliste im selben Abschnitt ist weiterhin grün geführt,
  - Schattenmodus-/RAG-Evidenzen bleiben in den Folgeunterabschnitten (`Go/No-Go Checkliste`, `Naechste Schritte (sofort)`) erhalten.

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

- [x] Tests/Typen PASS (2 Tage in Folge) (S1 erfüllt 2026-02-18)
- [x] RAG-Minimum indexiert, Retriever-Test PASS (S2 erfüllt 2026-02-18)
- [x] Redaction aktiv (keine PII in Logs/Datasets) (S2 Stichproben-Tests PASS 2026-02-18)
- [x] Flags gesetzt: `RAG_ON`, `SHADOW_ON`, `CANARY_PCT` (Alias-Flags in Settings/.env.example verankert; Mapping auf Runtime-Flags aktiv)
- [x] Stichprobe (Schattenmodus) ≥80% „Accept“ (Review-Lauf 2026-02-19: `8/8` Accept = `100.00%`; Report `.tmp/results/reports/shadow_accept_report_20260219_223752.md`; Review-Dataset `.tmp/results/reviews/shadow_review_sample.reviewed.jsonl`)
  - Historie 2026-02-19: Frühere Proxy-Messung (`--mode policy-proxy`) ergab `6/8` Accept = `75.00%` (FAIL); anschließender Review-Lauf erreichte `8/8` = `100.00%` (PASS).
  - KI-Workflow bereit: `scripts/build_shadow_review_sample.py` erzeugt `.tmp/results/reviews/shadow_review_sample.jsonl` (redacted previews + `suggested_verdict` + leeres `verdict`), Gate unterstützt `--mode review-file` sowie `--fallback-suggested` für Bootstrap-Läufe.

### Nächste Schritte (sofort, ohne Codeänderungen)

- [x] Schattenmodus-Logging mit Redaction intern aktivieren (abgeschlossen 2026-02-18)
- [x] 10-20 Kern-Dokumente (Memory-Bundle + Schlüssel-Canvases) indexieren (RAG-Minimum) (abgeschlossen 2026-02-18)
- [x] Wöchentlichen Review-Slot (30-45 min) für Stichproben + Kurations-Delta einplanen (S3 abgeschlossen 2026-02-18)

Editor-Setup - .vscode-Konsolidierung (Root-zentriert)
------------------------------------------------------

Ziel: Ein einziges `.vscode/` im Repo-Root, das Standard-Tasks/Settings bereitstellt, ohne projekt-spezifische Profile (Launch/CWD/ENV) zu beschädigen. Sanft, reversibel, mit Inventur vor Migration.

### Annahmen & Rahmen

- Root verwendet `.venv` (Windows) und zentralen Interpreter (`.vscode/settings.json`).
- `novapolis_agent` ist der einzige Code-Bereich mit Tests/Launch-Profilen; `novapolis-rp` ist primär Daten/Docs/Tools.
- Markdownlint läuft via cli2 in CI; lokale Tasks existieren in Agent-Projekt (bereits erweitert um Root-`todo.root.md`/`DONELOG.md`).
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
  - [x] Agent-Tasks optional auf Root-Tasks verweisen (mittels eindeutiger Labels) (entfallen: keine Agent-Subfolder-Tasks vorhanden; Root ist kanonisch)
- Etappe2 - Bereinigung (nach 3-5Tagen stabiler Nutzung)
  - [x] Dubletten entfernen oder Agent-`tasks.json` auf Minimal-Set reduzieren (entfallen: keine Agent-`tasks.json` vorhanden)
  - [x] Launch-Profile optional ins Root migrieren (nur wenn stabil; sonst belassen) (entfallen: nur Root-`launch.json` vorhanden)
  - [x] Dokumentation: kurzer Abschnitt „Editor-Setup“ im Root-README (abgeschlossen 2026-02-17; siehe `README.md`)

### Aufgabenliste (konkret)

- Inventur
  - [x] Auflisten: `.vscode/settings.json` (Root, Agent, RP), `.vscode/tasks.json` (Root, Agent), `.vscode/launch.json` (Agent) (Befund 2026-02-18: nur Root-`.vscode` vorhanden)
  - [x] Unterschiede festhalten: Interpreter-Pfad, pytestArgs, envFile, Copilot-Instructions (Befund 2026-02-18 dokumentiert)
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
  - [x] Agent-`tasks.json` Dubletten entfernen, falls Root-Tasks etabliert (entfallen: keine Agent-`tasks.json` vorhanden)
  - [x] RP-Settings auf Workspace-Instructions beschränken (falls Root diese zentral führt) (entfallen: keine RP-Subfolder-`.vscode`-Settings vorhanden)

### Snapshot-Frontmatter Migration (YAML)

- [x] Etappe 0 (2025-11-01 09:10): Regel aktiv, Mischbetrieb erlaubt — YAML bevorzugt, `Stand:`/`Letzte Aktualisierung:` weiterhin gültig. (aktiv/bestätigt)
- [x] Etappe 1: Bei Änderungen an Dokus YAML-Frontmatter ergänzen/aktualisieren (`stand`, `update`, `checks`). (laufende Regel, im aktuellen Zyklus eingehalten)
- [ ] Etappe 2: Sweep — bestehende Kopfzeilen migrieren (TODO, README/Index, Policies). Diff klein halten; `checks` kurz.
- [ ] Etappe 3: Legacy-Kopfzeilen auslaufen lassen; Instruktionen aktualisieren (nur YAML erlaubt).
- Fortschritt 2025-11-02 19:11: Root-Dokumente (`README.md`, `todo.root.md`, `DONELOG.md`, `WORKSPACE_STATUS.md`) tragen konsolidierte YAML-Frontmatter; Archivkopie unter `novapolis-dev/archive/quarantine/single-root-todo.md`; markdownlint-cli2 PASS.

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



