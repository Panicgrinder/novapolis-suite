---
stand: 2026-02-21 08:08
update: Abgeschlossene Agent-Bloecke aus todo.root ueberfuehrt; aktiver Root-Backlog verschlankt.
checks: markdownlint-cli2 PASS; check_frontmatter.py PASS
---

TODO-Archiv - Agent
===================

Zweck: Vollständig abgeschlossene TODO-Abschnitte aus `novapolis_agent/docs/TODO.md` aufnehmen, damit `TODO.md` schlank bleibt.

Regeln (kurz)

- Nur Abschnitte verschieben, deren Checklisten vollständig auf [x] stehen.
- Inhalt unverändert übernehmen. Direkt unter der Abschnitts-Überschrift eine Einzeile ergänzen: `archived_at: YYYY-MM-DD HH:MM`.
- Headings in diesem Archiv: Setext (MD003 konform, H1/H2).
- Präsentation: Lint-Läufe mit PRESENTATION=SHARED.
- DONELOG: Ein Zeilen-Eintrag im Agent-DONELOG genügt (kein Volltext hier).

Ablage

- Neueste Einträge oben einfügen.

<!-- Hier unterhalb neue, vollständig erledigte Blöcke einfügen (neu zuerst). -->

Root-Uebernahme: novapolis_agent Block aus todo.root
---------------------------------------------------

archived_at: 2026-02-21 04:52

Quelle: `todo.root.md` (Abschnitte `novapolis_agent`, `Tests/Typen/Coverage`, `RP-Audit Befunde`, `Frontmatter/Markdown-Sweep`).

- [x] Agent-Root-Aufgabenblock als abgeschlossen archiviert.
- [x] Tests/Typen/Coverage-Teilblock als abgeschlossen archiviert.
- [x] RP-Audit-Befunde-Teilblock als abgeschlossen archiviert.
- [x] Frontmatter/Markdown-Sweep-Teilblock als abgeschlossen archiviert.
- [x] Aktiver Root-Backlog enthaelt diese Detailhistorie nicht mehr; Verweise bleiben in den Archiven.

Kurzfristige Ziele (Heute)
--------------------------

archived_at: 2025-11-01 19:16

- [x] Eval-Profile festziehen
  - Ziel: Reproduzierbare Läufe via `eval/config/profiles.json` (quiet default, temp, optionale Checks).
  - Status: Done (UI lädt Profile; Meta-Header vollständig; kurzer ASGI-Lauf konsistent).
- [x] Eval-UI: Profile-/Quiet-/ASGI-/Guard-Bypass-Integration
  - Ziel: Läufe steuerbar über Profile, reduzierte Logs, In-Process-ASGI, optionaler Vorab-Guard.
  - Status: Done (Menü integriert, Flags wirksam, Trends/Exports ok).
- [x] Synonym-Overlay (privat) einführen und mergen
  - Ziel: `eval/config/synonyms.local.json` (gitignored) automatisch mit `synonyms.json` mergen.
  - Status: Done (Loader-Merge, Sample-Datei, Doku in README & eval/README, .gitignore ergänzt).
- [x] Eval-Pfade harmonisieren & Meta-Header erweitern
  - Ziel: Nutzung von `eval/datasets|results|config`, Meta mit overrides (model/host/temperature).
  - Status: Done (Runner/UI angepasst, Ergebnisse validiert).


