---
stand: 2026-02-22 14:21
update: Pfadnotation auf kanonische RP-Zielpfade vereinheitlicht (`novapolis-rp/...`) und CWD-Mehrdeutigkeit reduziert.
checks: "npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-dev/docs/index.md' PASS (2026-02-22 11:24); .\\.venv\\Scripts\\python.exe scripts\\check_frontmatter.py 'novapolis-dev/docs/index.md' PASS (2026-02-22 11:24)"
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
  - `docs/todo.agent-board.md` — Agent-Aufgaben (Backend, Tests/Typing, Scripts)
  - `.github/copilot-instructions.md` — verbindliche Arbeitsweise & Sicherheitsregeln (SSOT)
- `docs/naming-policy.md` — Dateibenennung fuer alle Novapolis-Repos
- `docs/tests.md` — Testabdeckung, Sim-/Client-Checks
- Meta-Sidecars: `novapolis-dev/docs/meta/*.json` (Quelle, Ursprung, Migrationsstempel)

Betriebsnotiz (temporär)
------------------------

- Workspace ist Single-Root (Repo-Root). Mehrschrittige Abläufe laufen bevorzugt über Python-Wrapper (`scripts/*.py`) statt über komplexe Inline-Shell-Blöcke.

Specs
-----

- `docs/specs/annotation-spec.md` — Knowledge/Actions/Skill-Ableitung (YAML-Snippets)
- `docs/specs/scheduler-spec.md` — Tickloser Min-Heap Scheduler (24×1h, Events/Locks/Interrupts)
- `docs/specs/tts-exporter-coqui.md` — Build-Time Export (Coqui→OGG), Task-Skelett & Kontrakt

> [!NOTE]
> Legacy-Kopien im ehemaligen RP-Development-Verzeichnis bleiben nur temporaer als Verweis bestehen und werden nach Downstream-Sign-off entfernt.

Kernprinzipien:

- Aenderungen an Code oder signifikanten Dateien kurz in `novapolis-dev/docs/donelog.md` dokumentieren.
- Aufgabenpflege und Priorisierung im Modul: `docs/todo.rp.md`, `docs/todo.dev.md`, `docs/todo.agent-board.md`; Index: `docs/todo.index.md`.
- Tooling liegt weiterhin in `novapolis-rp/coding/tools/`; dieses Index liefert nur Verweise.

Dokumentierte Datenpfade
------------------------

- Rohdaten verbleiben unter `novapolis-rp/database-raw/`.
- Kuratierte Daten liegen unter `novapolis-rp/database-curated/staging/` und `novapolis-rp/database-curated/final/`.
- Finale RP-Struktur (`00-admin`, `01-factions`, `04-inventory`, `06-scenes`, …) bleibt produktiv unter `novapolis-rp/database-rp/`.

Tooling & Skripte
-----------------

- `novapolis-rp/coding/tools/validators/` — Daten-Validierungen (Schema, Cross-Refs, Co-Occurrence, Name-Check)
- `novapolis-rp/coding/tools/curation/` — Ingest-/Curation-Skripte fuer RAW → RP
- `novapolis-rp/coding/devcontainer/` — Entwicklungscontainer (Node 22; markdownlint-Setup)
- `novapolis-rp/coding/tools/metadata/` — Front-Matter- und Metadaten-Hilfen

Nutzungshinweise (lokal)
------------------------

```powershell
# Self-Test der Tagging-Pipeline
python "novapolis-rp/coding/tools/curation/tag_chunks_from_yaml.py" --self-test

# Dry-Run (keine Dateien schreiben)
python "novapolis-rp/coding/tools/curation/tag_chunks_from_yaml.py" --yaml-root "novapolis-rp/database-rp" --chunks-root "novapolis-rp/database-curated/staging/chunks/chat-export (1)" --out-root "novapolis-rp/database-curated/reviewed/chat-export (1)" --range 019-016 --dry-run

# Schreiben (Outputs aktualisieren)
python "novapolis-rp/coding/tools/curation/tag_chunks_from_yaml.py" --yaml-root "novapolis-rp/database-rp" --chunks-root "novapolis-rp/database-curated/staging/chunks/chat-export (1)" --out-root "novapolis-rp/database-curated/reviewed/chat-export (1)" --range 019-016

# Retag-Modus (nur Teil-Heuristiken a/b/c)
python "novapolis-rp/coding/tools/curation/tag_chunks_from_yaml.py" --yaml-root "novapolis-rp/database-rp" --chunks-root "novapolis-rp/database-curated/staging/chunks/chat-export (1)" --out-root "novapolis-rp/database-curated/reviewed/chat-export (1)" --retag-in "novapolis-rp/database-curated/reviewed/chat-export (1)" --retag-out "novapolis-rp/database-curated/reviewed/chat-export (1)" --range 019-016
```

Validierung & Tasks
-------------------

- CI fuehrt automatisch aus: Daten-Validierung (`novapolis-rp/coding/tools/validators`) und Markdown-Lint.
- Lokale VS Code Tasks (Docker bevorzugt, sonst Node):
  - "validate:data (auto)" - Validatoren (Schema, Cross-Refs, Co-Occurrence)
  - "lint:names (auto)" - Benennung nach `novapolis-dev/docs/naming-policy.md`
  - "system:check (windows)" - Umgebung pruefen

Hinweise:

- Tasks sind im Workspace vorkonfiguriert; CI bleibt massgeblich.
- Bei Quoting-/Shell-Problemen die Validatoren direkt gemäß Hub-Doku ausfuehren (siehe `novapolis-dev/docs/readme.hub.md`, Abschnitt "Validator Tools").
- Markdown-Lint lokal: ausschließlich direkt im Terminal via `npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc '**/*.md'` (keine Wrapper/Tasks).



