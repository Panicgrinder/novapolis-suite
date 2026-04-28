---
stand: 2026-04-28 11:26
update: Die README-Entscheidungsliste fuehrt den Workspace-Index nicht mehr als offenen Phase-2-Verkuerzungspunkt, sondern nur noch als zielgerichtete Driftfix-Flaeche.
checks: snapshot-lock PASS (2026-04-28 11:26); markdownlint=PASS; frontmatter=PASS; path-portability=PASS
---
README Konsolidierungs-Entscheidungsliste
=========================================

Zweck
-----
Diese Datei dokumentiert, welche der ehemals identifizierten 22 README-basierten Doku-Dateien künftig voll erhalten bleiben, verschlankt (Stub/Redirect) oder archiviert werden. Ziel ist Reduktion von Duplikaten und klare zentrale Navigation über das Hub-README (`novapolis-dev/README.md`). Der Scope betrifft bewusst Hub-, Stub-, Tool- und Runbook-Dokus; fachliche Inhaltsindizes unter `novapolis-rp/database-rp/01-factions/**` bleiben eigene Landingpages und sind nicht Teil dieses Renaming-Laufs.

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
- novapolis_agent/scripts/scripts-overview.md: TOOL - Skriptliste (konsolidieren auf aktuelle Skripte, später evtl. SLIM).
- novapolis_agent/eval/eval-overview.md: TOOL - Eval-Prozess, bleibt bis vereinheitlichte Eval-Doku existiert.
- novapolis_agent/eval/config/context.notes/context-notes-guide.md: SLIM - Redirect zu zentraler Kontext-/Prompt-Doku.
- novapolis-dev/README.md: KEEP - Hub.
- novapolis-dev/archive/README.md: SLIM - Kurzer Hinweis, Redirect ins Hub-Archiv-Verzeichnis.
- novapolis-dev/logs/logs-policy.md: SLIM - Hinweis auf Log-Policy + Redirect.
- novapolis-dev/integrations/mcp-openai-eval/mcp-openai-eval-guide.md: TOOL - Spezifische Integration.
- novapolis-rp/README.md: KEEP - RP-Domain, Canvas-Hinweise.
- novapolis-rp/database-rp/06-scenes/scenes-guidelines.md: TOOL - Szenenstruktur.
- novapolis-rp/database-curated/curation-workflow.md: SLIM - Redirect zu zentraler Kurations-Policy.
- novapolis-rp/database-curated/staging/staging-workflow.md: ARCHIVE - Nach Migration nur Staging-Hinweis.
- novapolis-rp/database-raw/99-exports/raw-export-policy.md: TOOL - Export-Policy (RAW only).
- novapolis-rp/coding/devcontainer/README.md: TOOL - Devcontainer Setup.
- novapolis-rp/coding/tools/chat-exporter/chat-exporter-guide.md: TOOL - Nutzung Chat-Exporter.
- novapolis-rp/coding/tools/metadata/metadata-tools.md: TOOL - Metadata-/Validator-Hinweise.
- novapolis-rp/coding/tools/validators/validator-suite.md: TOOL - Validatoren (Behalten bis zentrale Validator-Doku erstellt).
- .tmp/results/README.md: SLIM - Temporärbereich, deutlicher Hinweis auf Flüchtigkeit.

- .tmp-datasets/README.md: SLIM - Temporärdaten, Redirect zu Data-Policy.
- novapolis-sim/README.md: KEEP - Simulationsprojekt (Godot, Verifikation).
- packages/README.md: SLIM - Kernhinweis + Redirect zu Shared-Paket-Abschnitt im Hub.

Nächste Schritte
----------------
1. Phase 2 Patches: SLIM/ARCHIVE Kategorien minimal editieren (Stub + Redirect-Link).
2. Markdownlint + Frontmatter nach jedem Patch (MD003 Setext sicherstellen).
3. `WORKSPACE_INDEX.md` nur noch punktuell per belegtem Link- oder Driftfix anpassen; kein weiterer Strukturabbau als eigener Phase-2-Punkt.
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

