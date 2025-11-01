stand: 2025-11-01 18:38
update: Pfadkorrektur archiv→archive (Archiv-Hinweis aktualisiert)
checks: keine
---

<!-- markdownlint-disable MD022 MD041 -->

TODO (Novapolis-Dev)
====================

Hinweis
-------

- Dieses Dokument bündelt Aufgaben für das Dev‑Modul (Tooling, Lint/CI, Validatoren, Doku-Infra).
- RP‑Aufgaben liegen in `docs/todo.rp.md`. Agent‑Aufgaben liegen in `docs/todo.agent.md`.
- Archivierte, vollständig erledigte Abschnitte (H2/H3, alle [x]) bitte manuell nach `novapolis-dev/archive/todo.dev.archive.md` verschieben (neuester oben), mit `archived_at: YYYY-MM-DD HH:MM` unter der Abschnittsüberschrift.

Offene Aufgaben (Dev)
---------------------

- [ ] (Platzhalter) Sammle Dev‑Aufgaben hier. Falls bisher in Root `todo.root.md` oder Agent‑TODO gepflegt, bitte verschieben.

Bereinigung Alt‑TODOs (nur SSOT behalten)
-----------------------------------------

- [ ] Kandidatenliste prüfen und löschen, sobald alle Referenzen entfernt sind:
	- Root‑Redirect: `TODO.md` (verweist auf `todo.root.md`)
	- Agent‑Redirect: `novapolis_agent/docs/TODO.md` (verweist auf `novapolis-dev/docs/todo.agent.md`)
	- Historischer Redirect: `novapolis-dev/docs/todo.md` (verweist auf `docs/todo.index.md`)
	- Mirror/Stub: `novapolis-rp/Main/novapolis-dev/docs/todo.md` (Redirect‑Stub, Mirror‑Policy beachten)
  
Hinweise
--------

- SSOT‑Dateien bleiben: `novapolis-dev/docs/todo.{agent,dev,rp,sim}.md`, `todo.root.md`, `novapolis-dev/docs/todo.index.md` sowie die Archive unter `novapolis-dev/archive/`.
- Redirect/Mirror‑Stubs nach Freigabe entfernen; vorherige Suche nach eingehenden Links durchführen.
