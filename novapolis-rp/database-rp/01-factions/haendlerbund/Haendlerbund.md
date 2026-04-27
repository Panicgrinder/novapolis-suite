---
stand: 2026-04-27 02:30
update: Haendlerbund fuehrt jetzt ein konservatives Betriebs- und Nahraummodell T0 fuer G7 als externe Zentrale und C6 als eingebettete Niederlassung.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260427_022916.md
slug: haendlerbund
category: faction
status: active
version: "0.1"
tags: [fraktion]
---

Haendlerbund (Fraktion)
=======================

Überblick
---------
- Status: aktiv
- Rolle im Setting: mobiler Handels- und Versorgungsblock mit einer konservativen externen Zentrale in [G7](./03-locations/G7.md) und eingebetteten Niederlassungen bei Partnerfraktionen.

Kerngebiet
----------

- [G7](./03-locations/G7.md): externe Zentrale des Haendlerbunds mit Leitstelle, Handels- und Routenleitstand sowie Sicherheitsfreigabe.

Betriebskorridor T0
-------------------

- `G7` bleibt der einzige klar aktive Eigenkern des Haendlerbunds.
- [C6](../novapolis/03-locations/C6.md) ist die belastbar belegte eingebettete Niederlassung des Haendlerbunds in Novapolis und kein zweiter externer Fraktionskern.
- Der primaere Arbeitskorridor des aktuellen T0-Rahmens bleibt `G7 <-> C6`; weitere Niederlassungen bleiben ohne neue Evidenz offen.

Rollenlesart T0
---------------

- Mara Quell fuehrt Ziele, Freigaben und Krisenentscheidungen aus der Leitstelle in `G7`.
- Tovin Rek steuert Handelsfenster, Konvoiplanung und Lieferprioritaeten von `G7` aus.
- Runa Fehr bindet Zutritt, Begleitschutz und Transitfreigaben an denselben Kern.

Betriebsmodell T0
-----------------

- Das konservative Arbeitsmodell fuer Zentrale, Niederlassungslogik und innere Konfliktlinien liegt in [haendlerbund-betriebsmodell-t0](./00-doctrine/haendlerbund-betriebsmodell-t0.md).
- Kernlesart: `G7` fuehrt als externe Zentrale; `C6` ist der wichtigste eingebettete Aussenposten im Novapolis-Raum.

Nahraum T0
----------

- Der unmittelbare Haendlerbund-Nahraum ist jetzt konservativ in [haendlerbund-nahraum-t0](./00-doctrine/haendlerbund-nahraum-t0.md) verdichtet.
- Darin sind `G7`, der Korridor `G7 <-> C6` und die Spannungen zwischen Versorgung, Verhandlung und Sicherheitsfreigabe zusammengezogen.

Assets in diesem Ordner
-----------------------
- Charaktere → ./02-characters/
- Orte → ./03-locations/
- Inventar → ./04-inventory/Haendlerbund-inventar.md
- Doctrine → ./00-doctrine/
- Projekte → ./05-projects/caravan-moves.md

Offene Punkte
-------------
- [ ] Weitere Niederlassungen nur nach neuer Evidenz als eigene Fraktionsanker verdichten
- [ ] Handelsfenster und Protokolle zwischen G7 und Partnerfraktionen weiter schaerfen
