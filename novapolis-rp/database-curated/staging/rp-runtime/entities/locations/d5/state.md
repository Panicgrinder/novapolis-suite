---
stand: 2026-05-20 06:28
update: D5-State fuehrt jetzt Koras Pruefzusage und die konservative Hand-/Schubdebatte zur Draisine.
checks: snapshot-lock PASS (2026-05-20 06:28); npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc RP-Runtime-turn13-slice PASS (2026-05-20 06:22); .\.venv\Scripts\python.exe scripts\check_frontmatter.py RP-Runtime-turn13-slice PASS (EXITCODE=0, 2026-05-20 06:22)
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

- summary: D5 traegt im aktuellen Hauptweltpfad weiter die Material-, Freigabe- und Arbeitskante fuer Nordlinie 01. Mit Turn 11 kehrt Ronja zu Jonas und Pahl an die Draisine auf den Bahnsteiggleisen zurueck, nicht in einen abgeschlossenen Werkstattinnenraum. Der Prototyp wird dort auf der Schiene aufgebaut, waehrend Ronja zuerst Baufortschritt, gebundenes Material und Fehlstellen abfragt und erst danach den Tunnelbedarf mit `Schweißgeraet`, `DN60`, Anschlusssicherung und Freiraeumung gegen denselben D5-Arbeitsort spiegelt. T12 zieht daraus zwei offene technische Prueffragen: C6 soll die Schuttkeil-Eignung klaeren, Jonas/Pahl den Antrieb. Turn 13 zieht den Stand enger: Kora bestaetigt aus dem C6-Funkraum, dass sie die Schuttkeil-Frage selbst prueft; zugleich wird die Draisine in D5 nicht mehr nur ueber die leere Motorfrage, sondern ueber konservative Hand-/Schubvarianten diskutiert. Der gebundene Draisine-Bestand liegt weiter in einem eigenen Runtime-Traeger getrennt vom Tunnelbedarf.
- drivers:
  - D5 ist der aktive Werkstatt- und Kontrollkern von Novapolis.
  - Jonas und Pahl beantworten den Nordlinie-Bedarf ueber belastbare Werkstattarbeit statt ueber freie Vollzusagen.
  - Lumen gehoert als Jonas-gekoppelte Begleitinstanz zum aktuellen D5-Arbeitsstand.
  - Die kleine Turn-7-Teilbereitstellung und der ausgeschopfte Turn-8-Rest laufen ueber denselben D5-Ausgabepfad.
  - Turn 9 verdichtet dieselbe Lage zu einer enger formulierten Werkstattanforderung, statt einen neuen improvisierten Hilfssatz zu behaupten.
  - Turn 11 bindet Draisine-Bau und Tunnelbedarf jetzt sichtbar an denselben Bahnsteig-/Gleis-Arbeitsort in D5.
  - Der neue Runtime-Traeger `../../assets/draisine-transportmodul/inventory.md` trennt ab jetzt gebundenen Prototypbestand sauber vom Nordlinie-/Tunnelbedarf.
  - T12 fuehrt Ronjas Schuttkeil-Frage an C6 und ihre Antriebsfrage an Jonas/Pahl als offene Pruef- und Grundlagenfragen, nicht als D5-Freigabe oder Testlauf.
  - Turn 13 bestaetigt Koras eigene Pruefzusage aus `C6` und zieht die D5-seitige Draisine-Debatte auf konservative Hand-/Schubvarianten statt auf eine freie Motorbehauptung.
- blockers:
  - Schweißgeraet und Adapter DN60 fehlen weiter als Hauptblocker.
  - Ueber den kleinen Turn-7-Satz hinaus gibt es keine neue reale D5-Lieferung.
  - Konkrete Folgeabgaenge, Chargenherkunft und weitere Werkstattzusagen bleiben offen.
  - Die verdichtete Anforderung ist noch nicht nach aussen in einen bestaetigten Materialzug gekippt.
  - Der Draisine-Prototyp ist noch nicht so weit, dass er bereits als fertiger Logistikpfad fuer den Tunnelbedarf gelesen werden kann.
  - Weder Hebelbetrieb noch Schubvariante sind als freigegebener Antrieb beantwortet; `Brems-/Stopplogik`, `Not-Aus`, Rueckzugspfad und Lastgrenze bleiben weiter offen.
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
- Runtime: `sessions/d5-c6-nordlinie-sanierung-01/scene-log.md`, Turn 12
- Runtime: `inventory.md`
- Runtime: `../../assets/draisine-transportmodul/inventory.md`
- Runtime: `../../assets/draisine-transportmodul/state.md`

Promotion Notes
---------------

- D5 bleibt fuer den aktuellen Hauptpfad der aktive Werkstatt- und Freigabekern; weitere Fortschreibung erst mit realer neuer Werkstattbewegung, beantworteter Draisine-Antriebsfrage oder klarer Veraenderung der D5-Lastlage.
