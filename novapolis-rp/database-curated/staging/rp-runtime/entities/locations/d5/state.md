---
stand: 2026-04-29 03:56
update: In entity-centric Runtime-Dossier migriert; Inhalt bleibt Arbeitsstand ohne Kanon-Promotion.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260429_035444.md
---
Runtime State - D5
==================

Status
------

- slug: d5
- scope: location
- state: Arbeitsstand
- review_state: working

Current State
-------------

- summary: D5 traegt im aktuellen Hauptweltpfad weiter die Material-, Freigabe- und Arbeitskante fuer Nordlinie 01. Mit Turn 11 kehrt Ronja zu Jonas und Pahl an die Draisine auf den Bahnsteiggleisen zurueck, nicht in einen abgeschlossenen Werkstattinnenraum. Der Prototyp wird dort auf der Schiene aufgebaut, waehrend Ronja zuerst Baufortschritt, gebundenes Material und Fehlstellen abfragt und erst danach den Tunnelbedarf mit `Schweißgeraet`, `DN60`, Anschlusssicherung und Freiraeumung gegen denselben D5-Arbeitsort spiegelt; Jonas bleibt dabei mit Lumen im selben Arbeitsfenster. Der gebundene Draisine-Bestand liegt dafuer jetzt nicht mehr nur verteilt in Szene und SSOT, sondern in einem eigenen Runtime-Traeger getrennt vom Tunnelbedarf.
- drivers:
  - D5 ist der aktive Werkstatt- und Kontrollkern von Novapolis.
  - Jonas und Pahl beantworten den Nordlinie-Bedarf ueber belastbare Werkstattarbeit statt ueber freie Vollzusagen.
  - Lumen gehoert als Jonas-gekoppelte Begleitinstanz zum aktuellen D5-Arbeitsstand.
  - Die kleine Turn-7-Teilbereitstellung und der ausgeschopfte Turn-8-Rest laufen ueber denselben D5-Ausgabepfad.
  - Turn 9 verdichtet dieselbe Lage zu einer enger formulierten Werkstattanforderung, statt einen neuen improvisierten Hilfssatz zu behaupten.
  - Turn 11 bindet Draisine-Bau und Tunnelbedarf jetzt sichtbar an denselben Bahnsteig-/Gleis-Arbeitsort in D5.
  - Der neue Runtime-Traeger `../../assets/draisine-transportmodul/inventory.md` trennt ab jetzt gebundenen Prototypbestand sauber vom Nordlinie-/Tunnelbedarf.
- blockers:
  - Schweißgeraet und Adapter DN60 fehlen weiter als Hauptblocker.
  - Ueber den kleinen Turn-7-Satz hinaus gibt es keine neue reale D5-Lieferung.
  - Konkrete Folgeabgaenge, Chargenherkunft und weitere Werkstattzusagen bleiben offen.
  - Die verdichtete Anforderung ist noch nicht nach aussen in einen bestaetigten Materialzug gekippt.
  - Der Draisine-Prototyp ist noch nicht so weit, dass er bereits als fertiger Logistikpfad fuer den Tunnelbedarf gelesen werden kann.
- impacted_entities:
  - D5
  - Jonas Merek
  - Lumen
  - Pahl Brenner
  - Ronja Kerschner
  - Reflex
  - Nordlinie 01

Evidence
--------

- SSOT: `database-rp/01-factions/novapolis/03-locations/D5.md`
- SSOT: `database-rp/01-factions/novapolis/02-characters/Jonas-Merek.md`
- SSOT: `database-rp/01-factions/novapolis/02-characters/Lumen.md`
- Runtime: `sessions/d5-c6-nordlinie-sanierung-01/scene-log.md`, Turn 1, 2, 6, 7
- Runtime: `sessions/d5-c6-nordlinie-sanierung-01/scene-log.md`, Turn 9
- Runtime: `sessions/d5-c6-nordlinie-sanierung-01/scene-log.md`, Turn 11
- Runtime: `inventory.md`
- Runtime: `../../assets/draisine-transportmodul/inventory.md`

Promotion Notes
---------------

- D5 bleibt fuer den aktuellen Hauptpfad der aktive Werkstatt- und Freigabekern; weitere Fortschreibung erst mit realer neuer Werkstattbewegung oder klarer Veraenderung der D5-Lastlage.
