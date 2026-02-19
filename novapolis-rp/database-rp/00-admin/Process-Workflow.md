---
stand: 2026-02-16 12:32
update: README-Sidecar-Policy festgelegt (READMEs ohne Sidecar).
checks: "& .\\.venv\\Scripts\\python.exe scripts\\run_checks_and_report.py PASS (2026-02-16 12:33)"
slug: process-workflow
category: Admin
schemaVersion: 1
language: de
status: active
owners: [admin-novapolis]
tags: [rp, workflow, curation, validation, simulation]
relatedSlugs: [index-rules, memory-bundle, system-prompt]
---

Process-Workflow (RP)
=====================

Zweck
-----
Zentrale Prozess- und Workflow-Referenz fuer RP-Daten, Kuratierung, Validierung und Simulation.
Diese Seite konsolidiert die Arbeitsablaeufe, die zuvor im Dev-Hub dokumentiert waren.

Geltungsbereich
---------------
- RP-SSOT: `database-rp/`
- RAW: `database-raw/99-exports/`
- Curated: `database-curated/` (staging/reviewed/final)
- Tools: `novapolis-rp/coding/tools/`

Datenfluss (RAW -> Staging -> Final -> RP)
------------------------------------------
1. Exporte (RAW) nach `database-raw/99-exports/` ablegen (ungefiltert, keine Bearbeitung).
2. Staging-Aufbereitung in `database-curated/staging/` (Normalize, Tagging, Review-Tags).
3. Review/Approval -> `database-curated/final/` (geplant; derzeit Platzhalter).
4. Relevante Fakten/Szenen/Canvas nach `database-rp/` uebernehmen.
5. DONELOG/TODO aktualisieren (Root + Dev-Hub), optional Metadata-Sidecars refreshen.

Review-Tags (Staging)
---------------------
- `[SCENE|FACT|CHAR|LOC|PROJ|INV|OPEN]`
- Keine RAW-Daten direkt in `database-rp/` einpflegen.

Validatoren (Suite)
-------------------
- Schema-Validierung: `coding/tools/validators/src/validate-curated.js` (staging/manifest.json)
- RP-Markdown-Checks: `coding/tools/validators/src/validate-rp.js`
- Cross-Refs: `coding/tools/validators/src/check-crossrefs.js` (slug-only Referenzen)
- Behavior-Matrix: `coding/tools/validators/behavior_matrix_check.py`
- Aggregation: `coding/tools/validators/src/validate-all.js`

Export & Ingest
---------------
- Chat-Exporter: `novapolis-rp/coding/tools/chat-exporter/` (Browser Auto-Scroll)
- Ziel: immer `database-raw/99-exports/`
- Ingest: `novapolis-rp/coding/tools/curation/ingest_jsonl.py`
- Tagging (YAML/SSOT -> Chunks): `novapolis-rp/coding/tools/curation/tag_chunks_from_yaml.py`

Metadata Layer (Sidecar JSON)
-----------------------------
- Pro Markdown optionales Companion JSON (Struktur/Tags, kein Content-Eingriff).
- Beispiel-Felder: chapter, characters, location, tags, source.
- Flags: `--dry-run`, `--overwrite`, `--glob`.

README-Sidecar-Policy
---------------------
- **README.md-Dateien benoetigen keine JSON-Sidecars.**
- Bestehende `README.json`-Dateien gelten als Legacy und sollen entfernt werden.
- Sidecars sind fuer kanonische Entities (z. B. character/location/project/inventory/scene) oder Indizes sinnvoll; READMEs sind Navigations-/Stub-Seiten.

Temporare Bereiche
------------------
- `.tmp/results/` fuer Reports/Scanner-Ausgaben.
- `.tmp/datasets/` fuer fluechtige Zwischenartefakte.
- Rotation (empfohlen): letzte 7 Tage oder letzte 5 Artefakte je Serie; Zielbudget 500 MB.

Stubbing-Policy
--------------
- Unterordner-READMEs sind Stubs und verweisen auf diese Prozess-Seite.
- Stubs enthalten Frontmatter, Kurz-Zweck, Link auf den relevanten Abschnitt.
- Stubs nicht wieder aufblaehen; Details bleiben hier.

Stub-Mapping (Auszug)
---------------------

| Pfad | Abschnitt | Typ |
| ---- | --------- | ---- |
| novapolis-rp/coding/tools/validators/README.md | Validatoren | stub |
| novapolis-rp/coding/tools/chat-exporter/README.md | Export & Ingest | stub |
| novapolis-rp/coding/tools/metadata/README.md | Metadata Layer | stub |
| novapolis-rp/database-curated/README.md | Curation Workflow | stub |
| novapolis-rp/database-curated/staging/README.md | Curation Workflow | stub |
| novapolis-rp/database-raw/99-exports/README.md | Export & Ingest | stub |
| novapolis-rp/database-rp/06-scenes/README.md | Scenes Guidelines | stub |

Naming-Policy (database-rp)
---------------------------
- Zeichensatz: A-Z, a-z, 0-9, Bindestrich `-`, Punkt `.`.
- Umlaute: ae/oe/ue, ss.
- Keine Leerzeichen, Unterstriche, Klammern.
- Endungen klein (`.md`, `.txt`).
- Durchsetzung: `coding/tools/validators/src/check-names.js` (Dry-Run; `--apply` fuer Umbenennungen).

Schreibstil (RP-Antworten)
--------------------------
- Keine Zitatbloecke.
- Cinematisch, fokussiert, 250-400 Woerter je Antwort.
- Vorschlaege/Optionen nur auf Anfrage.

Simulation & Tests (novapolis-sim)
----------------------------------
- API: `GET /world/state`, `POST /world/step` (Agent: `novapolis_agent`).
- Godot pollt alle 0.2s mit `{dt:0.1}`; visualisiert Tick und Zeit.
- Startfolge: Agent starten -> Godot `Main.tscn` oeffnen -> Play.

Empfohlene Prueflaeufe (manuell)
--------------------------------
- Vollcheck Runner (Lint/Typen/Tests/Coverage): `python scripts/run_checks_and_report.py`
- Coverage-Only: `python scripts/run_pytest_coverage.py`
- Link-Scan Dry-Run: `python scripts/scan_links.py --dry-run`

Mini-Prequel-Testplan
---------------------
1. Startzustand abrufen: `GET /world/state` mit `tick` und `time`/`timestamp`.
2. Intro-Overlay: Tick + Zeit anzeigen; Intro-Text aus freigegebenem Kanon.
3. Sequenz: Intro ca. 5s, dann ausblenden; Polling bleibt aktiv.
4. Statuspanel: `Verbindung` + `Letztes Update` (timestamp, Fallback "-").

Offline-Verhalten
-----------------
- Bei Fehlern: Status `Offline`, Step-Requests pausieren, Retry mit Backoff.
- Hinweistext: "Agent nicht erreichbar - Anzeige pausiert".
- Reconnect: Status auf `Verbunden`, Intro bleibt deaktiviert.

Scenes Guidelines (Kurzfassung)
-------------------------------
- Szenen liegen unter `database-rp/06-scenes/` mit Frontmatter (`id`, `characters`, `locations`, `inventoryRefs`).
- Co-Occurrence-Regeln beachten; Validierung ueber Validatoren.

Beispiel-Frontmatter
--------------------

```yaml
---
id: scene-0123
title: Begegnung am Fluss
characters: [ava, bram]
locations: [flussufer]
inventoryRefs: [lanterne]
tags: [SCENE, pivotal]
---
```

FinalGate-Hinweis (Curated)
---------------------------
- `database-curated/staging/*.finalgate.md` dient als Promotion-Checkliste/Decision Record pro Export.

Governance & Tracking
---------------------
- Governance: `.github/copilot-instructions.md`
- DONELOGs: Root `DONELOG.md`, Dev-Hub `novapolis-dev/docs/donelog.md`
- TODOs: `todo.root.md`, RP-Board `novapolis-dev/docs/todo.rp.md`
- Status: `WORKSPACE_STATUS.md`

Canvas-Rescue (Kurzfassung)
---------------------------
- Roh-Canvas aus `database-raw/99-exports/` nach `database-rp/` ueberfuehren.
- Flags (`vorsichtig_behandeln`, `korrupt`) beachten; Drift kommentieren.
- Quellenblock pro Canvas: RAW-Datei + `resolved.md`-Referenzen.
- Nach Migration Validatoren laufen lassen (RP + Crossrefs).

Pflegepflichten
---------------
- Aenderungen in DONELOGs festhalten (Root + Dev-Hub).
- Aufgaben im RP-Board `novapolis-dev/docs/todo.rp.md` pflegen.
- Nach groesseren Updates Validatoren laufen lassen (RP + Crossrefs).
