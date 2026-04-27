---
stand: 2026-04-27 02:30
update: Novapolis fuehrt jetzt ein konservatives Betriebsmodell T0 fuer D5 als Kernbasis, C6 als Aussenposten und den aktiven D5-C6-Korridor.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260427_022916.md
slug: novapolis-betriebsmodell-t0
category: canon
version: "0.1"
---

Novapolis - Betriebsmodell T0
=============================

Zweck
-----

- Dieser SSOT zieht fuer Novapolis ein konservatives Betriebsmodell T0 nach.
- Er verdichtet `D5` als aktive Kernbasis, `C6` als teilaktiven Aussenposten und den dazwischenliegenden Arbeitskorridor, ohne daraus bereits ein etabliertes Metro-Netz zu machen.

Guardrails
----------

- Novapolis bleibt ein junges lokales Aufbau- und Versorgungsgeflecht.
- `D5` ist der belastbare Kern; `C6` ist derselbe Fraktionsblock im Aussenraum, aber kein gleichwertig stabiler zweiter Kern.
- `E3` bleibt Risiko- und Monitoringraum ohne aktive Ruecknahme in den Betriebsstatus.
- Handelsnormalisierung, Vollmarktlogik und freie Fraktionssummen ueber D5/C6 hinaus bleiben ohne neue Belegkette offen.

Kernlesart T0
-------------

| Bereich | Status | Funktionsprofil | Lesart |
| --- | --- | --- | --- |
| [D5](../03-locations/D5.md) | aktiv | Hauptbasis, Kontrollraum, Versorgung, Werkstatt, Fraktionsleitung | aktiver Novapolis-Kern |
| [C6](../03-locations/C6.md) | teilaktiv | Aussenposten, Monitoring, Staging, lokale Sicherung | aktiver Aussenposten desselben Blocks |
| `D5 <-> C6` | aktiver Projekt- und Versorgungskorridor | Nordlinie, Materiallauf, Rueckmeldung, Freigabe | verletzlicher Arbeits- und Aufbaupfad |

Leitungs- und Freigabekette
---------------------------

- Ronja Kerschner fuehrt D5 als technische und politische Kernlinse.
- Kora Malenkov haelt C6 intern und koppelt lokale Lage an D5 zurueck.
- Jonas Merek traegt Werkstatt-, Material- und Tunnelassessment entlang des Korridors.
- Pahl Brenner setzt Sicherheitsfreigaben, Regelhilfe und Belastungsabwaegung ueber denselben Raum.
- Reflex und Echo filtern Risiko, Signal und Schutz im Kernraum, ohne eigene Fraktionskerne zu bilden.

Betriebsprioritaeten
--------------------

| Prioritaet | Lesart | Guardrail |
| --- | --- | --- |
| Kernstabilitaet | D5 muss bewohnbar, versorgbar und steuerbar bleiben | keine freie Expansion gegen den Kernzustand |
| Aussenpostensicherung | C6 bleibt relevant, aber nur unter enger Freigabe und Monitoringdisziplin | keine Vollsicherheit fuer C6 behaupten |
| Korridorbetrieb | Nordlinie und Materiallauf verbinden die Fraktion real | kein freier Normalverkehr behaupten |
| Aufbau vor Normalisierung | Novapolis ist arbeitsfaehig, aber nicht etabliert | keine Markt- oder Metro-Normalitaet setzen |

Spielbare Konfliktlinien
------------------------

- Kern gegen Peripherie: `D5` fuehrt, aber `C6` bindet Menschen, Material und Aufmerksamkeit in denselben kleinen Pool.
- Versorgung gegen Risiko: Jeder Ausbau des Korridors vergroessert sofort Material-, Sicherheits- und Monitoringdruck.
- Wissen gegen Disziplin: D5 will verstehen, C6 muss filtern; zu fruehe Offenheit kippt die Lage.
- Aufbau gegen Ueberdehnung: Novapolis wirkt nur stabil, solange es D5, C6 und den Korridor nicht ueber seine knappen Reserven hinaus belastet.

Alltagslesart fuer Spiel und Szenen
----------------------------------

- `D5` ist kein bequemer Heimatraum, sondern eine belastbare, aber knappe Arbeitsbasis.
- `C6` ist kein freier Ruecken, sondern ein teilaktiver Vorposten unter Daueranspannung.
- Der Korridor dazwischen ist Projekt-, Transfer- und Freigaberaum, nicht normale Infrastruktur.

Verknuepfte Quellen
-------------------

- [Novapolis](../Novapolis.md)
- [D5](../03-locations/D5.md)
- [C6](../03-locations/C6.md)
- [Novapolis-inventar](../04-inventory/Novapolis-inventar.md)
- [novapolis-nahraum-t0](./novapolis-nahraum-t0.md)
