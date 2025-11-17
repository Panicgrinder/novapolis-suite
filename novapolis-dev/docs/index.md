---
stand: 2025-11-16 06:52
update: Frontmatter-Delimiter ergänzt; Snapshot aktualisiert (keine inhaltlichen Änderungen)
checks: markdownlint-cli2 PASS (single file)
---

<!-- markdownlint-disable MD041 -->

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
- `docs/todo.index.md` — Index für Aufgaben (Module)
  - `docs/todo.rp.md` — RP-Aufgaben (Kanon/Canvas/Projekte)
  - `docs/todo.dev.md` — Dev-Aufgaben (Tooling, Lint/CI, Validatoren)
  - `docs/todo.agent.md` — Agent-Aufgaben (Backend, Tests/Typing, Scripts)
  - `.github/copilot-instructions.md` — verbindliche Arbeitsweise & Sicherheitsregeln (SSOT)
- `docs/naming-policy.md` — Dateibenennung fuer alle Novapolis-Repos
- `docs/tests.md` — Testabdeckung, Sim-/Client-Checks
- Meta-Sidecars: `novapolis-dev/docs/meta/*.json` (Quelle, Ursprung, Migrationsstempel)

Betriebsnotiz (temporär)
------------------------

- VS Code markiert den Workspace aktuell als Multi-Root. Wrapper-Tasks/Automationen sind unzuverlässig (CWD/Quoting). Bis zur Bereinigung auf Single-Root gilt: KEINE WRAPPER, Terminal ausschließlich manuell nutzen.
  - Fallakte: `novapolis-dev/logs/open-case-terminal-multi-root-20251103.md`

Specs
-----

- `docs/specs/annotation-spec.md` — Knowledge/Actions/Skill-Ableitung (YAML-Snippets)
- `docs/specs/scheduler-spec.md` — Tickloser Min-Heap Scheduler (24×1h, Events/Locks/Interrupts)
- `docs/specs/tts-exporter-coqui.md` — Build-Time Export (Coqui→OGG), Task-Skelett & Kontrakt

> [!NOTE]
> Legacy-Kopien im ehemaligen RP-Development-Verzeichnis bleiben nur temporaer als Verweis bestehen und werden nach Downstream-Sign-off entfernt.

Kernprinzipien:

- Aenderungen an Code oder signifikanten Dateien kurz in `novapolis-dev/docs/donelog.md` dokumentieren.
- Aufgabenpflege und Priorisierung im Modul: `docs/todo.rp.md`, `docs/todo.dev.md`, `docs/todo.agent.md`; Index: `docs/todo.index.md`.
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
  - "validate:data (auto)" - Validatoren (Schema, Cross-Refs, Co-Occurrence)
  - "lint:names (auto)" - Benennung nach `novapolis-dev/docs/naming-policy.md`
  - "system:check (windows)" - Umgebung pruefen

Hinweise:

- Tasks sind im Workspace vorkonfiguriert; CI bleibt massgeblich.
- Bei PowerShell-Quoting-Problemen (Unexpected token) statt des Tasks direkt ausfuehren:
  - `powershell -ExecutionPolicy Bypass -File coding/tools/validators/run_check_names.ps1`
- Markdown-Lint lokal: ausschließlich direkt im Terminal via `npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc '**/*.md'` (keine Wrapper/Tasks).



