---
stand: 2026-02-27 06:06
update: Donelog-Hygiene auf Wochenfenster umgesetzt (Current-Window aktiv, Historik ins Dev-Archiv ausgelagert).
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc "WORKSPACE_STATUS.md" "DONELOG.md" "novapolis-dev/docs/donelog.md" "novapolis-dev/docs/todo.dev.md" "novapolis-dev/docs/todo.index.md" "novapolis-dev/archive/docs/others/workspace-status.archive.pre-2026-02-20.md" "novapolis-dev/archive/docs/donelogs/donelog_dev.window-archive.pre-2026-02-20.md" PASS (2026-02-27 00:06); f:/VS-Code-Workspace/Main/.venv/Scripts/python.exe scripts/check_frontmatter.py "WORKSPACE_STATUS.md" "DONELOG.md" "novapolis-dev/docs/donelog.md" "novapolis-dev/docs/todo.dev.md" "novapolis-dev/docs/todo.index.md" "novapolis-dev/archive/docs/others/workspace-status.archive.pre-2026-02-20.md" "novapolis-dev/archive/docs/donelogs/donelog_dev.window-archive.pre-2026-02-20.md" PASS (EXITCODE=0, 2026-02-27 00:06)
---

<!-- markdownlint-disable MD022 MD041 -->

TODO (Novapolis-Dev)
====================

Hinweis
-------

- Dieses Dokument buendelt Aufgaben fuer das Dev-Modul (Tooling, Lint/CI, Validatoren, Doku-Infra).
- RP-Aufgaben liegen in `docs/todo.rp.md`. Agent-Aufgaben liegen in `docs/todo.agent-board.md`.
- Vollstaendig erledigte Bloecke werden nach `novapolis-dev/archive/todo.dev.archive.md` verschoben.

Offene Aufgaben (Dev)
---------------------

- [ ] [Jetzt] Active-Surface-Index fuer `novapolis-dev/docs/**` erstellen (ACTIVE/REFERENCE/HISTORICAL + Owner + last_check).
  - Akzeptanzkriterium: Eine scanbare Uebersicht mit klarer Klassifikation aller aktiven Dev-Dokumente liegt vor.
- [ ] [Jetzt] Truthfulness-Drift in `novapolis-dev/README.md` korrigieren (u. a. `integrations/` nicht mehr als Platzhalter; `roadmaps/` nur bei realem Verzeichnis).
  - Akzeptanzkriterium: Strukturabschnitt beschreibt ausschliesslich den Iststand.
- [ ] [Jetzt] `novapolis-dev/docs/specs/tts-exporter-coqui.md` auf Iststand nachziehen (Platzhalter-Narrativ entfernen, Implementierungsgrad explizit markieren).
  - Akzeptanzkriterium: Keine Widersprueche mehr zwischen Spec, Tasking und Modul-Iststand.
- [x] [Als naechstes] Donelog-Hygiene einfuehren: aktives Fenster definieren (Current-Window) und aeltere Bloecke sauber ins Historik-Archiv auslagern.
  - Akzeptanzkriterium: `novapolis-dev/docs/donelog.md` bleibt fuer operative Arbeit kurz und scanbar; Historie bleibt erhalten.
  - Evidenz: `novapolis-dev/docs/donelog.md` (Current-Window), `novapolis-dev/archive/docs/donelogs/donelog_dev.window-archive.pre-2026-02-20.md` (Archivfenster).
- [ ] [Als naechstes] Logs-Policy fuer `novapolis-dev/logs/` durchsetzen (Umgang mit `*.tmp.md` festlegen und konsistent umsetzen).
  - Akzeptanzkriterium: Keine policy-widrigen Rohlogs im aktiven Log-Pfad oder Policy explizit angepasst und dokumentiert.
- [ ] [Als naechstes] Stand-Freshness-SLA festlegen (`ACTIVE <= 14 Tage`, `REFERENCE <= 60 Tage`) und als wiederkehrenden Check im Dev-Modul verankern.
  - Akzeptanzkriterium: Alle aktiven Dev-Dokumente haben frische `stand`-Werte oder dokumentierte Ausnahmen.
- [ ] [Spaeter] TODO-Index-Sync automatisiert absichern (Check/Guard: bei Aenderung von `todo.*.md` muss `todo.index.md` im selben Lauf geaendert sein).
  - Akzeptanzkriterium: Drift zwischen Modul-Boards und `todo.index.md` wird technisch verhindert statt nur manuell entdeckt.
- [ ] [Spaeter] Woechentliche Hygiene-Cadence etablieren (Drift-Scan, Donelog-Cleanup, TODO/Index-Abgleich) inkl. KPI-Tracking.
  - Akzeptanzkriterium: Fester 60-Minuten-Wochenslot mit dokumentierten KPIs (`todo_index_drift`, `active_docs_stale`, `placeholder_conflicts`, `logs_policy_violations`).
