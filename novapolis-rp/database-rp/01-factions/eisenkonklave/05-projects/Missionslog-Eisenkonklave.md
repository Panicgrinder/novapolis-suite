---
stand: 2026-04-02 06:27
update: Gelegentliche Handelsfenster mit dem Haendlerbund sind jetzt als belegter Missionsanker der Eisenkonklave verankert.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260402_062604.md
title: Missionslog (Eisenkonklave)
category: project
slug: missionslog-eisenkonklave
version: "0.1"
last_updated: 2026-03-31T18:12:34+02:00
status: active
owners: [eisenkonklave]
authority_chain:
  - "fraktion:eisenkonklave"
  - "fraktions-leitung:varek-solun"
  - "stellv-fraktions-leitung:tbd"
  - "leitung-sicherheit:yara-kest"
  - "leitung-logistik:tbd"
  - "rolle:kaspar-dorn"
  - "stationsleitung:tbd"
tags: [rp, missionen, eisenkonklave]
dependencies: [eisenkonklave]
---

<!-- markdownlint-disable MD025 -->

Missionslog (Eisenkonklave)
===========================

Zentrale Übersicht der fraktionsspezifischen Missionen für den Eisenkonklave.

Hinweis
-------

- Der erste konservative Handels-/Sicherheitsanker der Eisenkonklave ist jetzt verankert.
- Globaler Einstieg bleibt [00-admin/Missionslog](../../../00-admin/Missionslog.md).

### Händlerbund: gelegentliche Handelsfenster unter Sicherheitsfreigabe

- Ziel: begrenzte, kontrollierte Handelsfenster mit dem Haendlerbund offenhalten, ohne die Sicherheitslage der Eisenkonklave aufzuweichen.
- Start: T0 / laufende Fraktionslage
- Ende: offen
- Status: aktiv
- Belege/Quittungen: `../../../database-raw/99-exports/RAW-canvas-2025-10-16T16-55-00-000Z.txt`, [Relationslog-Eisenkonklave](../06-handel-diplomatie/Relationslog-Eisenkonklave.md), [Handelslog-Eisenkonklave](../06-handel-diplomatie/Handelslog-Eisenkonklave.md)
- Verantwortliche: Kaspar Dorn (Handelsleitung), Yara Kest (Sicherheitsfreigaben)
- Inventar-Link: [Eiserne-Enklave-inventar](../04-inventory/Eiserne-Enklave-inventar.md)
- Orte/Projekte: [Handelslog-Eisenkonklave](../06-handel-diplomatie/Handelslog-Eisenkonklave.md), [Relationslog-Eisenkonklave](../06-handel-diplomatie/Relationslog-Eisenkonklave.md)
  Hinweise:
  - Der RAW-Cluster `eisenkonklave_operativ` belegt `Haendlergilde(handel_gelegentlich)` als aktive Diplomatie-/Handelslage.
  - Das Relationslog fuehrt dieselbe Lage als `Haendlerbund -> handel_gelegentlich`.
  - Kaspar Dorn ist als Handelsleitung fuer Tauschfenster und Priorlisten belegt; Yara Kest erteilt die Sicherheitsfreigaben fuer Handelsfenster und Konvois.
  - Konkrete Route, Dealmengen, Tauschliste und einzelne Lieferfenster bleiben bewusst `tbd`.
