---
stand: 2025-11-16 06:52
update: Initial README-Konsolidierungsentscheidungsliste erstellt
checks: n/a
---
README Konsolidierungs-Entscheidungsliste
=========================================

Zweck
-----
Diese Datei dokumentiert, welche der identifizierten 22 README.md-Dateien künftig voll erhalten bleiben, verschlankt (Stub/Redirect) oder archiviert werden. Ziel ist Reduktion von Duplikaten und klare zentrale Navigation über das Hub-README (`novapolis-dev/README.md`).

Kategorien
----------
- KEEP: Bleibt voll mit inhaltlichem Fokus.
- SLIM: Wird auf wenige Kernhinweise + Redirect zum Hub reduziert.
- TOOL: Behält fokussierte technische Instruktionen (nicht verschlanken, aber ggf. Format prüfen).
- ARCHIVE: Inhalt wandert in `novapolis-dev/archive/`; Datei im Quellpfad wird Stub oder entfernt (nach Review).

Entscheidungsmatrix
-------------------
- README.md (Root): KEEP - Einstiegs- und Projektübersicht.
- novapolis_agent/README.md: KEEP - Backend-spezifische Laufzeit/Entwicklung.
- novapolis_agent/scripts/README.md: TOOL - Skriptliste (konsolidieren auf aktuelle Skripte, später evtl. SLIM).
- novapolis_agent/eval/README.md: TOOL - Eval-Prozess, bleibt bis vereinheitlichte Eval-Doku existiert.
- novapolis_agent/eval/config/context.notes/README.md: SLIM - Redirect zu zentraler Kontext-/Prompt-Doku.
- novapolis-dev/README.md: KEEP - Hub.
- novapolis-dev/archive/README.md: SLIM - Kurzer Hinweis, Redirect ins Hub-Archiv-Verzeichnis.
- novapolis-dev/logs/README.md: SLIM - Hinweis auf Log-Policy + Redirect.
- novapolis-dev/integrations/mcp-openai-eval/README.md: TOOL - Spezifische Integration.
- novapolis-rp/README.md: KEEP - RP-Domain, Canvas-Hinweise.
- novapolis-rp/database-rp/06-scenes/README.md: TOOL - Szenenstruktur.
- novapolis-rp/database-curated/README.md: SLIM - Redirect zu zentraler Kurations-Policy.
- novapolis-rp/database-curated/staging/README.md: ARCHIVE - Nach Migration nur Staging-Hinweis.
- novapolis-rp/database-raw/99-exports/README.md: TOOL - Export-Policy (RAW only).
- novapolis-rp/coding/devcontainer/README.md: TOOL - Devcontainer Setup.
- novapolis-rp/coding/tools/chat-exporter/README.md: TOOL - Nutzung Chat-Exporter.
- novapolis-rp/coding/tools/metadata/README.md: TOOL - Metadata-/Validator-Hinweise.
- novapolis-rp/coding/tools/validators/README.md: TOOL - Validatoren (Behalten bis zentrale Validator-Doku erstellt).
- .tmp-results/README.md: SLIM - Temporärbereich, deutlicher Hinweis auf Flüchtigkeit.
- .tmp-datasets/README.md: SLIM - Temporärdaten, Redirect zu Data-Policy.
- novapolis-sim/README.md: KEEP - Simulationsprojekt (Godot, Verifikation).
- packages/README.md: SLIM - Kernhinweis + Redirect zu Shared-Paket-Abschnitt im Hub.

Nächste Schritte
----------------
1. Phase 2 Patches: SLIM/ARCHIVE Kategorien minimal editieren (Stub + Redirect-Link).
2. Markdownlint + Frontmatter nach jedem Patch (MD003 Setext sicherstellen).
3. `WORKSPACE_INDEX.md` nach Abschluss Phase 2 verkürzen (nur Agent-spezifischer Kern + Redirect-Hinweis).
4. DONELOG-Einträge für jede Gruppe (Batch) dokumentieren.
5. Abschluss: Task "Docs/READMEs: Konsolidierung & Leitlinien" abhaken.

Review-Hinweise
---------------
- TOOL-Kategorie nur verschlanken, wenn Inhalte vollständig ins Hub übernommen wurden.
- ARCHIVE-Migration erst nach Bestätigung, dass kein aktiver Prozess auf die Datei verweist.
- Redirect-Format: "Dieser Inhalt wurde konsolidiert. Siehe: <Hub-Pfad>#<Abschnitt>".

Checks (geplant)
----------------
- Batch-Lint vor/ nach SLIM-Patches.
- Frontmatter-Validator gezielt pro geänderte README.

Ende.

