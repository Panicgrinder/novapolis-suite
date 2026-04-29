---
stand: 2026-04-29 03:56
update: In entity-centric Runtime-Dossier migriert; Inhalt bleibt Arbeitsstand ohne Kanon-Promotion.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260429_035444.md
---
Runtime State - Novapolis
=========================

Status
------

- slug: novapolis
- scope: faction
- state: Arbeitsstand
- review_state: working

Current State
-------------

- summary: Novapolis ist im aktuellen Hauptpfad kein diffuser Sammelraum mehr, sondern ein aktiv belasteter Fraktionsblock mit klarer Binnenaufteilung. `D5` bleibt der Werkstatt-, Material- und Freigabekern; `C6` bleibt teilaktiver Aussenposten unter Tunnel-, Stations- und Versorgungslast; `Nordlinie 01` bindet beide Orte ueber denselben Reparatur- und Materialkorridor; das `Draisine-Transportmodul` laeuft als noch nicht fertiger, aber bereits materiell gebundener Logistikkoerper auf den Bahnsteiggleisen von `D5` mit.
- drivers:
  - `D5` bleibt aktiver Werkstatt- und Kontrollkern von Novapolis.
  - `C6` bleibt teilaktiver Vorposten mit eigener Tunnelkante, Stationsbetrieb und laufender Ruecklaufrolle.
  - `Nordlinie 01` ist aktuell der groeßte materielle und operative Projektverbrauch der Fraktion.
  - Das `Draisine-Transportmodul` bindet bereits Technikposten in D5, ist aber noch kein fertiger Logistikpfad.
  - Der Fraktionsverbrauch verteilt sich aktuell asymmetrisch: D5 langsam-stabil, C6 angespannt, Nordlinie hoch, Draisine klein aber stetig.
- blockers:
  - `Schweißgeraet` und `Adapter / Fitting (DN60)` fehlen weiter als harte Projektblocker.
  - Konkrete Fraktionsrestmengen ueber alle offenen Projekte bleiben weiter `tbd`.
  - `C6` arbeitet ohne neuen realen Materialeingang weiter unter Druck.
  - Der Nordlinie-Kontaktpunkt ist noch kein freier Material- oder Personalkorridor.
- impacted_entities:
  - Novapolis
  - D5
  - C6
  - Nordlinie 01
  - Draisine-Transportmodul
  - Ronja Kerschner
  - Reflex
  - Jonas Merek
  - Pahl Brenner
  - Lumen
  - Kora Malenkov
  - Echo

Active Runtime Axes
-------------------

- Ortsachsen:
  - `D5` als Werkstatt-, Material- und Freigabekern
  - `C6` als teilaktiver Aussenposten mit getrennter Tunnel- und Stationslesart
- Projektachsen:
  - `Nordlinie 01` als akuter Reparatur- und Materialkorridor
  - `Draisine-Transportmodul` als lokaler Logistik- und Werkstattpfad in D5
- Inventarachsen:
  - `../../locations/d5/inventory.md` fuer ortsgebundenen Bedarf und reale Altbewegungen
  - `../../projects/nordlinie-01/inventory.md` fuer den Projekt-Reparaturbedarf
  - `../../assets/draisine-transportmodul/inventory.md` fuer Prototypbestand und Projektumgebung

Evidence
--------

- SSOT: `database-rp/01-factions/novapolis/04-inventory/Novapolis-inventar.md`
- SSOT: `database-rp/01-factions/novapolis/05-projects/Nordlinie-01.md`
- SSOT: `database-rp/01-factions/novapolis/05-projects/Draisine-Transportmodul.md`
- Runtime: `../../locations/d5/state.md`
- Runtime: `../../locations/c6/state.md`
- Runtime: `../../projects/nordlinie-01/state.md`
- Runtime: `../../locations/d5/inventory.md`
- Runtime: `../../projects/nordlinie-01/inventory.md`
- Runtime: `../../assets/draisine-transportmodul/inventory.md`

Promotion Notes
---------------

- Dieser Fraktionsstatus aggregiert nur die im aktuellen Hauptpfad wirklich aktiven Novapolis-Achsen.
- Weitere Fraktionsflaechen erst dann nachziehen, wenn sie im Runtime-Zug selbst material- oder handlungsrelevant werden.
