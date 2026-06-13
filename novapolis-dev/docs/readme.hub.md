---
stand: 2026-06-13 09:34
update: Phase-2-Konsistenzlauf aktualisiert den Hub-Header und die manuellen Pruefbeispiele auf den aktuellen Root-Wrapper-Stil.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260613_093323.md
---

Novapolis Dokumentations-Hub
============================

Zweck
-----
Zentrale, kanonische Bündelung aller querliegenden Workflows (Curation, Validation, Export, Scenes, Tooling) und Ersatz ausführlicher Unterordner-READMEs durch schlanke Stubs. Dieses Dokument ist Ergänzung zu `novapolis-dev/README.md` (organisatorischer Fokus) und verweist auf operative Pipelines.

Kurzüberblick (TL;DR)
---------------------
- Core: Dieses Hub-Dokument ist SSOT für Prozesse; Unterordner-READMEs sind Stubs mit Verweisen hierher.
- Fluss: RAW → Staging → Final → RP; Validatoren sichern Konsistenz entlang des Pfads.
- Werkzeuge: Validatoren, Chat-Exporter, Metadata-Sidecars - alle relevanten Dateien sind unten direkt verlinkt.
- Pflege: Änderungen immer in DONELOG/TODO spiegeln; Frontmatter und Markdownlint (MD003) einhalten.
- Cleanup: `.tmp-*` Inhalte regelmäßig rotieren; Kriterien siehe Abschnitt Temporäre Bereiche.

Inhalt & Navigationsmatrix
--------------------------
- Datenfluss (RAW → Staging → Final → RP) - siehe Abschnitt Curation Workflow.
- Validator Suite (Schemas, Cross-Refs, Behavior Matrix) - Abschnitt Validator Tools.
- Export / Import (Browser Chat-Exporter, Ingest/Curation) - Abschnitt Export & Ingest.
- Szenen & Referenzen (Frontmatter, Co-Occurrence) - Abschnitt Scenes Guidelines.
- Metadata Companion JSON (Hybrid Metadata Tool) - Abschnitt Metadata Layer.
- Temporäre Artefakte (`.tmp/results/`, `.tmp/datasets/`) - Abschnitt Temporäre Bereiche.
- Stub-Policy & Migrationsstatus - Abschnitt Stubbing Policy.

Curation Workflow
-----------------
1. Export (RAW) nach `novapolis-rp/database-raw/99-exports/` nur ungefiltert.
2. Staging-Aufbereitung in `novapolis-rp/database-curated/staging/` (Normalize, Tagging, Review Tags `[SCENE|FACT|CHAR|LOC|PROJ|INV|OPEN]`).
3. Review & Approval → Kopie nach `novapolis-rp/database-curated/final/` (geplant; derzeit `final/` Platzhalter).
4. Übernahme relevanter Artefakte (Memory-Bundle Updates, Facts, Scenes) nach `novapolis-rp/database-rp/*` Strukturen.
5. Aktualisierung DONELOG / TODO (Dev Hub, RP Board) + optional Metadata JSON Refresh.

Validator Tools
---------------
Pfad: `novapolis-rp/coding/tools/validators/`
- Schema Validation ([`src/validate-curated.js`](../../novapolis-rp/coding/tools/validators/src/validate-curated.js)): `staging/manifest.json`.
- RP Markdown Checks ([`src/validate-rp.js`](../../novapolis-rp/coding/tools/validators/src/validate-rp.js)): Slug-Unique, Kategorie-Schema, H1 (ATX/Setext), Frontmatter-Typen.
- Cross-Reference Check ([`src/check-crossrefs.js`](../../novapolis-rp/coding/tools/validators/src/check-crossrefs.js)): slug-only Referenzen (Characters/Locations/Inventory/Projects).
- Behavior Matrix ([`behavior_matrix_check.py`](../../novapolis-rp/coding/tools/validators/behavior_matrix_check.py)): Signaturen & Intensitäten.
- Aggregation ([`src/validate-all.js`](../../novapolis-rp/coding/tools/validators/src/validate-all.js)).

Export & Ingest
---------------
Chat-Exporter ([Ordner](../../novapolis-rp/coding/tools/chat-exporter/)): Auto-Scroll, dedupliziert, speicherschonend (Streaming/Chunks) - schreibt nur nach RAW ([`database-raw/99-exports/`](../../novapolis-rp/database-raw/99-exports/)).
Metadata & Ingest ([Ordner](../../novapolis-rp/coding/tools/metadata/)): Erzeugt pro Markdown JSON-Sidecars (kein Content-Eingriff). Curation/Ingest-Skripte (separat, s. Validator Tools) transformieren Exporte in kuratierte Form.

Empfohlene Prüfläufe (manuell):

```powershell
# Validierungen (Wrapper bevorzugen; Beispiele)
# Vollcheck Runner (Lint/Typen/Tests/Coverage):
& .\.venv\Scripts\python.exe scripts/run_checks_and_report.py
# Nur Coverage (mit Fail-Under-Gate):
& .\.venv\Scripts\python.exe scripts/run_pytest_coverage.py --fail-under 80
# Link-Scanner Dry-Run / Reports:
& .\.venv\Scripts\python.exe scripts/scan_links.py --dry-run
```

Scenes Guidelines
-----------------
Szenen liegen unter [`database-rp/06-scenes/`](../../novapolis-rp/database-rp/06-scenes/) mit validierter Frontmatter (id, characters, locations, inventoryRefs). Co-Occurrence-Regeln erzwingen bestimmte Charakterpaarungen. Validation via Validators.

### Beispiel-Frontmatter

```yaml
---
id: scene-0123
title: Begegnung am Fluss
characters: [ava, bram]
locations: [flussufer]
inventoryRefs: [lanterne]
tags: [SCENE, pivotal]
---

Kurzer Einstiegsabsatz der Szene …
```

Validierung (scoped Beispiel):

```powershell
npm --prefix novapolis-rp/coding/tools/validators run validate:rp
```

Metadata Layer
--------------
[`coding/tools/metadata/`](../../novapolis-rp/coding/tools/metadata/) legt strukturierte JSON-Files neben Markdown an (Felder: chapter, characters, location, tags, source). Dry-Run / Overwrite Flags ermöglichen sichere Aktualisierung.

### Beispiel-Sidecar (`.meta.json`)

```json
{
  "chapter": 3,
  "characters": ["ava", "bram"],
  "location": "flussufer",
  "tags": ["SCENE", "quiet"],
  "source": "chat-export-2025-11-10.jsonl"
}
```

### Flags (Konvention)
- `--dry-run`: Nur diffen, keine Files schreiben.
- `--overwrite`: Existierende Sidecars aktualisieren.
- `--glob`: Zielmenge einschränken (z. B. `**/*.md`).

Temporäre Bereiche
------------------
- `.tmp/results/`: Nicht versionierte Zwischenstände (Reports, Scanner Ergebnisse).
- `.tmp/datasets/`: Flüchtige Dataset-Zwischenartefakte. Beide Verzeichnisse werden regelmäßig bereinigt; zentraler Inhalt gehört nicht hinein.

Rotation/Policy (empfohlen):
- Aufbewahrung: letzte 7 Tage oder die letzten 5 Artefakte je Serie (je nachdem, was größer ist).
- Größenlimit: Zielbudget 500 MB für `.tmp-*` insgesamt; ältere Artefakte zuerst entfernen.
- Werkzeuge: [`scripts/cleanup_workspace_files.py`](../../scripts/cleanup_workspace_files.py), [`scripts/rotate_backups.py`](../../scripts/rotate_backups.py).
- Reports: Link-Scanner-Berichte unter [`/.tmp/results/reports/scan_links_reports/`](../../.tmp/results/reports/scan_links_reports/).

Stubbing Policy
---------------
Ausführliche Unterordner-READMEs wurden verkürzt (Stub) und zeigen auf dieses Hub-Dokument. Stubs enthalten: Frontmatter (aktueller `stand`), `update: Stub → Hub`, kurze Zweckzeile, Link auf relevanten Abschnitt. Ursprünglicher Inhalt bleibt über Git-Historie auffindbar.

Stub-Mapping (Phase 1)
----------------------

| Pfad | Abschnitt | Typ |
| ---- | --------- | ---- |
| novapolis-rp/coding/tools/validators/validator-suite.md | Validator Tools | stub |
| novapolis-rp/coding/tools/chat-exporter/chat-exporter-guide.md | Export & Ingest | stub |
| novapolis-rp/coding/tools/metadata/metadata-tools.md | Metadata Layer | stub |
| novapolis-rp/coding/devcontainer/README.md | Tooling (Lint Env) | stub |
| novapolis-rp/database-curated/curation-workflow.md | Curation Workflow | stub |
| novapolis-rp/database-curated/staging/staging-workflow.md | Curation Workflow | stub |
| novapolis-rp/database-raw/99-exports/raw-export-policy.md | Export & Ingest | stub |
| novapolis-rp/database-rp/06-scenes/scenes-guidelines.md | Scenes Guidelines | stub |
| novapolis_agent/eval/config/context.notes/context-notes-guide.md | Metadata Layer | stub |
| novapolis-dev/integrations/mcp-openai-eval/mcp-openai-eval-guide.md | Integrations (Future) | stub |

| .tmp/results/README.md | Temporäre Bereiche | stub |
| .tmp/datasets/README.md | Temporäre Bereiche | stub |

Kern-READMEs (bleiben ausführlich)
----------------------------------
Root `README.md`, `novapolis-dev/README.md`, `novapolis_agent/README.md`, `novapolis-rp/README.md`, `novapolis-sim/README.md`, `packages/README.md`, plus Prozess-/Log-Dokumente (`novapolis-dev/logs/logs-policy.md`, Archive Übersicht, `novapolis_agent/eval/eval-overview.md`, `novapolis_agent/scripts/scripts-overview.md`).

Migrationsstatus
----------------
Phase 1 abgeschlossen (Stub-Ersetzung). Nachverfolgung in TODO (Docs/READMEs Konsolidierung). Nächste Phase: Prüfung redundanter Details in Kern-READMEs & Querverlinkungen vereinheitlichen.

Qualität & Pflege
-----------------
Bei Ergänzungen zuerst prüfen, ob Abschnitt schon existiert; ansonsten neuen Unterabschnitt hinzufügen und Stubs NICHT wieder aufblähen. Änderungen an Workflows → DONELOG & TODO aktualisieren.

Governance & Tracking
----------------------
- Governance (SSOT): [`.github/copilot-instructions.md`](../../.github/copilot-instructions.md)
- DONELOGs: Root [`DONELOG.md`](../../DONELOG.md), Agent [`novapolis_agent/docs/DONELOG.txt`](../../novapolis_agent/docs/DONELOG.txt), Dev-Hub [`novapolis-dev/docs/donelog.md`](../../novapolis-dev/docs/donelog.md)
- TODOs: [`todo.root.md`](../../todo.root.md) und kuratierter Auszug [`/.tmp/results/todo.cleaned.md`](../../.tmp/results/todo.cleaned.md)
- Status: [`WORKSPACE_STATUS.md`](../../WORKSPACE_STATUS.md)

Änderungshistorie
-----------------
2025-11-12 01:12 TL;DR, direkte Link-Verweise, Beispiele (Scenes/Metadata), Governance-Bezüge, Rotations-Policy ergänzt.
2025-11-12 01:03 Initiale Erstellung (Konsolidierung, Stub-Matrix).


