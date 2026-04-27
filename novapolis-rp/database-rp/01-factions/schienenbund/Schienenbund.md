---
stand: 2026-04-27 02:30
update: Schienenbund fuehrt jetzt ein konservatives Betriebs- und Nahraummodell T0 fuer B2 und den Korridor B1-B2-C3.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260427_022916.md
slug: schienenbund
category: faction
status: active
version: "0.1"
tags: [fraktion]
---

Schienenbund (Fraktion)
=======================

Überblick
---------
- Status: aktiv
- Rolle im Setting: kontrollierter Trassen-, Reparatur- und Freigabeblock mit einem aktiven Kernknoten in B2.

Kerngebiet
----------

- [B2](./03-locations/B2.md): aktiver Kommandoknoten fuer Netzhoheit, Reparaturprioritaeten, Freigabefenster und Sperrlogik.

Betriebskorridor T0
-------------------

- [B1](../../03-locations/B1.md) bleibt der neutrale Vorpuffer vor dem partiellen Zulauf in den Schienenbund-Kern.
- [B2](./03-locations/B2.md) ist der einzige klar aktive Schienenbund-Kernknoten.
- [C3](../../03-locations/C3.md) bleibt der teilaktive Nachpuffer hinter B2 und fuehrt den Weiterlauf unter Anschluss- und Hazard-Druck.

Rollenlesart T0
---------------

- Der Schienenbund arbeitet nicht als breit verteiltes Fraktionsnetz, sondern als eng gefuehrter Korridorblock um `B2`.
- Netzhoheit, Reparatur und kontrollierter Durchsatz gehen vor Expansion oder offene Diplomatie.
- Helia Vorn priorisiert den Betrieb, Rian Kord steuert Freigabefenster und Transitvorteile, Tera Solm haelt Sperr- und Sicherheitslogik.

Betriebsmodell T0
-----------------

- Das konservative Arbeitsmodell fuer Kernknoten, Freigabekette und innere Konfliktlinien liegt in [schienenbund-betriebsmodell-t0](./00-doctrine/schienenbund-betriebsmodell-t0.md).
- Kernlesart: `B2` fuehrt, `B1` puffert den Zulauf, `C3` traegt den verletzlichen Weiterlauf.
- Der Schienenbund bleibt damit als kleiner, harter Infrastrukturblock lesbar und nicht als flaechig kontrolliertes Stationsreich.

Nahraum T0
----------

- Der unmittelbare Schienenbund-Nahraum ist jetzt konservativ in [schienenbund-nahraum-t0](./00-doctrine/schienenbund-nahraum-t0.md) verdichtet.
- Darin sind Kernknoten `B2`, Vorpuffer `B1`, Nachpuffer `C3`, die beiden Hauptrichtungen des Korridors und die naechsten Belastungsachsen zusammengezogen.

Assets in diesem Ordner
-----------------------
- Charaktere → ./02-characters/
- Orte → ./03-locations/
- Inventar → ./04-inventory/Schienenbund-inventar.md
- Doctrine → ./00-doctrine/
- Projekte → ./05-projects/

Offene Punkte
-------------
- [ ] Beziehungsstatus zu Novapolis/Eisenkonklave weiter konsolidieren
