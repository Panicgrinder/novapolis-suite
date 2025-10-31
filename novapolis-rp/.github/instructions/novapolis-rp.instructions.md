# Novapolis‑RP – Workspace‑Instructions (Kompakt)

Diese Datei kann in Copilot Chat als Instruktionen angehängt werden (siehe VS Code Einstellung „Chat: Instructions Files Locations“). Sie liefert einen kompakten, team‑weiten Kontext.

## Primärer Kontext (bitte bevorzugen)

- novapolis-dev/docs/copilot-behavior.md – Arbeitsweise, Stil, Sicherheit
- novapolis-dev/docs/index.md – Navigations-/Prozessreferenz
- database-raw/99-exports/README.md – RAW‑Policy (keine ungefilterten Daten nach `database-rp/`)

## Wichtige Regeln

- Sprache: Deutsch (Erklärungen, Beispiele, Fehlermeldungen)
- RAW‑Only: Ungefilterte Exporte ausschließlich unter `database-raw/99-exports/` speichern.
- Curation‑Flow: Für Nutzung im RP stets Ingest/Curation verwenden (siehe `coding/tools/curation/`).
- Minimal‑Delta: Änderungen klein halten; `novapolis-dev/docs/donelog.md` pflegen.
- Sicherheit & Privacy: Keine Secrets; offline bevorzugen.

## Antworten & Format

- Prägnant, skimmbar; kurze Sätze, Bullet‑Listen ok, keine überladenen Blockzitate.
- Wenn Codeänderungen nötig sind: minimaler Patch, mit kurzer Begründung und Prüfung.
- Bei großen Aufgaben: ToDo‑Liste (Plan) sichtbar führen und aktualisieren.

## Export/Importer

- Export: `coding/tools/chat-exporter/` (Auto‑Scroll, Inaktivitäts‑Stop, speicherschonend)
- Ingest: `coding/tools/curation/ingest_jsonl.py` (streamend, chunked, sanftes Cleaning)

## Ziele

- Stabiles Gedächtnis (Admin: system‑prompt/memory‑bundle) und reibungsloser Szenenstart.
- Reproduzierbare, nachvollziehbare Schritte (Dokumentation & kleine Commits).
