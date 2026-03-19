---
stand: 2026-03-19 11:09
update: Dev-Board nach KPI-Trendansicht erneut synchronisiert; es sind keine offenen Dev-Punkte mehr vorhanden.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260318_052318.md
---

<!-- markdownlint-disable MD022 MD041 -->

TODO-Index (Novapolis-Dev)
==========================

Übersicht
---------

- RP-Module: `docs/todo.rp.md` — Aufgaben, Kanon-/Canvas-Arbeit, Logs (offen: 5)
- Dev-Module: `docs/todo.dev.md` — Tooling, Lint/CI, Validatoren, Doku-Infra (offen: 0)
- Agent-Module: `docs/todo.agent-board.md` — Backend (FastAPI/Ollama), Tests/Typing, Scripts (offen: 0)
- Sim-Module: `docs/todo.sim.md` — Godot/Visualisierung, API-Polling, Exportprofile (offen: 0)

Statushinweise (aktuell)
------------------------

- Dev v5.9: KPI-Trendansicht fuer die Hygiene-Cadence angelegt; Dev offen `1 -> 0`.
- Dev v5.8: O11 geschlossen; externes Standalone-Beta-Installblatt fuer Dritte dokumentiert (`offen: 2 -> 1`).
- Dev v5.7: Community-/Maintainer-Paket umgesetzt (`SUPPORT.md`, `RELEASE.md`, `MAINTAINERS.md`, Root-Issue-/PR-Templates); Dev offen `3 -> 2`.
- Dev v5.6: ADR-Ordner aktiv genutzt; `ADR-0001` und `ADR-0002` als akzeptierte Governance-Entscheidungen aufgenommen (`offen: 4 -> 3`).
- Dev v5.5: Coverage-Sprint Richtung `91%` abgeschlossen und deutlich ueberschritten (`76.24% -> 93.69%`, `offen: 5 -> 4`).
- Dev v5.3: Coverage-Punkt 3 gestartet; 90%-Qualitaetsziel jetzt verbindlich in Dev-Tests/Abschlussprozess verankert.
- Dev v5.4: Punkt 1 (Full-Gate) geschlossen; Coverage-Welle 1 Richtung `91%` gestartet (`76.24% -> 80.45%`).
- Dev v5.2: Folgezyklus fuer Gate-Stabilisierung und modernes Doku-Basispaket gestartet (`offen: 0 -> 5`).
- Dev v5.1: Woechentliche Hygiene-Cadence mit KPI-Tracking verbindlich dokumentiert (`offen: 1 -> 0`).
- Sim v5.0: Sim-Board konsolidiert, verbleibende Mikrodrift geschlossen (`offen: 1 -> 0`).
- Index v2.0: Operative Anzeige erweitert um Board-Metadaten (letzte Aenderung, aeltester offener Punkt, Widerspruchscheck).

Board-Metadaten (automationsrelevant)
-------------------------------------

| Board | letzte Aenderung | aeltester offener Punkt | Widerspruch "keine offenen" |
| --- | --- | --- | --- |
| Dev (`docs/todo.dev.md`) | 2026-03-19 | keiner (offen: 0) | nein |
| RP (`docs/todo.rp.md`) | 2026-03-05 | - [ ] [Als naechstes] Danach erst Mengen-Backfill in Inventaren (D5/C6/Fraktionen) starten. | nein |
| Agent (`docs/todo.agent-board.md`) | 2026-03-11 | keiner (offen: 0) | nein |
| Sim (`docs/todo.sim.md`) | 2026-03-11 | keiner (offen: 0) | nein |


Hinweise (Index)
----------------

- Vollständig erledigte Abschnitte (H2/H3, alle [x]) bitte manuell in `novapolis-dev/archive/todo.<modul>.archive.md` verschieben; unter der Abschnittsüberschrift `archived_at: YYYY-MM-DD HH:MM` ergänzen. Übersicht aller Archive: `novapolis-dev/archive/README.md`.
- Validierung bei Änderungen: markdownlint via `npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc` und Frontmatter-Check via `scripts/check_frontmatter.py`.
- Automationscheck: `scripts/check_todo_index_sync.py` liefert zusaetzlich Metadaten zu letzter Board-Aenderung, aeltestem offenen Punkt und Widerspruchen.

Verweise
--------

- Root-Übersicht: `todo.root.md` (Kurzüberblick, Meta-Aufgaben, Links)
- DONELOG-Zentralstruktur: `novapolis-dev/archive/docs/donelogs/INDEX.md`





