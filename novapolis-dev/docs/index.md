<!-- markdownlint-disable MD041 -->
last-updated: 2025-10-29T16:30:00+01:00
---

<!-- context-core: true; context-id: novapolis-rp; priority: high -->
> [!IMPORTANT]
> Kontext-Kerndokument: Dieses Index dient als Navigations- und Prozessreferenz fuer alle Arbeitsunterlagen.

Index: novapolis-dev/docs
=========================

<!-- Migration: Quelle aus dem frueheren coding-Hub, uebernommen am 2025-10-29 -->
<!-- Relocated vom alten Novapolis-RP Development-Hub nach `novapolis-dev/docs/index.md` am 2025-10-29 -->

Dieses Index-Dokument buendelt das Arbeitsmaterial fuer Agent-, Sim- und RP-Streams in `novapolis-dev/docs/`. Der Dev Hub ersetzt die frueheren `novapolis-rp/development/docs/*`-Bestände und fungiert als gemeinsames Sprungbrett fuer teamweite Policies, Reviews und Integrationen.

Primary Docs
------------

- `docs/donelog.md` — laufende Fortschritte und Beschluesse
- `docs/todo.md` — offene Aufgaben, Prioritaeten, Follow-ups
- `docs/copilot-behavior.md` — verbindliche Arbeitsweise & Sicherheitsregeln
- `docs/naming-policy.md` — Dateibenennung fuer alle Novapolis-Repos
- `docs/tests.md` — Testabdeckung, Sim-/Client-Checks
- Meta-Sidecars: `novapolis-dev/docs/meta/*.json` (Quelle, Ursprung, Migrationsstempel)

> [!NOTE]
> Legacy-Kopien im ehemaligen RP-Development-Verzeichnis bleiben nur temporaer als Verweis bestehen und werden nach Downstream-Sign-off entfernt.


Kernprinzipien:

- Aenderungen an Code oder signifikanten Dateien kurz in `novapolis-dev/docs/donelog.md` dokumentieren.
- Aufgabenpflege und Priorisierung in `novapolis-dev/docs/todo.md`.
- Tooling liegt weiterhin in `coding/tools/`; dieses Index liefert nur Verweise.


Dokumentierte Datenpfade
------------------------

- Rohdaten verbleiben unter `database-raw/`; geplante Spiegelung nach `novapolis-dev/raw/` (Mapping folgt in kuenftigen Migrationen).
- Kuratierte Daten (`database-curated/staging/`, `database-curated/final/`) werden perspektivisch nach `novapolis-dev/curated/` gespiegelt; derzeit nur Referenzierung.
- Finale RP-Struktur (`00-admin`, `01-canon`, …) bleibt produktiv und enthaelt ausschliesslich freigegebene Inhalte.

Tooling & Skripte
-----------------

- `coding/tools/validators/` — Daten-Validierungen (Schema, Cross-Refs, Co-Occurrence, Name-Check)
- `coding/tools/curation/` — Ingest-/Curation-Skripte fuer RAW → RP
- `coding/devcontainer/` — Entwicklungscontainer (Node 22; markdownlint-Setup)
- `coding/tools/metadata/` — Front-Matter- und Metadaten-Hilfen

Nutzungshinweise (lokal)
------------------------

```powershell
# Self-Test der Tagging-Pipeline
python "coding/tools/curation/tag_chunks_from_yaml.py" --self-test

# Dry-Run (keine Dateien schreiben)
python "coding/tools/curation/tag_chunks_from_yaml.py" --yaml-root "database-rp" --chunks-root "database-curated/staging/chunks/chat-export (1)" --out-root "database-curated/reviewed/chat-export (1)" --range 019-016 --dry-run

# Schreiben (Outputs aktualisieren)
python "coding/tools/curation/tag_chunks_from_yaml.py" --yaml-root "database-rp" --chunks-root "database-curated/staging/chunks/chat-export (1)" --out-root "database-curated/reviewed/chat-export (1)" --range 019-016

# Retag-Modus (nur Teil-Heuristiken a/b/c)
python "coding/tools/curation/tag_chunks_from_yaml.py" --yaml-root "database-rp" --chunks-root "database-curated/staging/chunks/chat-export (1)" --out-root "database-curated/reviewed/chat-export (1)" --retag-in "database-curated/reviewed/chat-export (1)" --retag-out "database-curated/reviewed/chat-export (1)" --range 019-016
```

Validierung & Tasks
-------------------

- CI fuehrt automatisch aus: Daten-Validierung (`coding/tools/validators`) und Markdown-Lint.
- Lokale VS Code Tasks (Docker bevorzugt, sonst Node):
  - "validate:data (auto)" – Validatoren (Schema, Cross-Refs, Co-Occurrence)
  - "lint:names (auto)" – Benennung nach `novapolis-dev/docs/naming-policy.md`
  - "lint:markdown (auto)" – Markdown-Lint
  - "system:check (windows)" – Umgebung pruefen

Hinweise:

- Tasks sind im Workspace vorkonfiguriert; CI bleibt massgeblich.
- Bei PowerShell-Quoting-Problemen (Unexpected token) statt des Tasks direkt ausfuehren:
  - `powershell -ExecutionPolicy Bypass -File coding/tools/validators/run_check_names.ps1`
- Alternativ stehen PS1-Tasks ohne Inline-Command bereit:
  - "lint:names (ps1)" / "validate:data (ps1)" / "lint:markdown (ps1)"
