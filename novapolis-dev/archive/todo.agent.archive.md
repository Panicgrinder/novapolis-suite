---
stand: 2025-11-12 04:42
update: Archivtext auf Guard-Check-Terminologie angepasst
checks: markdownlint-cli2 PASS
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


