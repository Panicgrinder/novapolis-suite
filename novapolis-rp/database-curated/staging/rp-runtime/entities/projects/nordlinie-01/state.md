---
stand: 2026-04-29 03:56
update: In entity-centric Runtime-Dossier migriert; Inhalt bleibt Arbeitsstand ohne Kanon-Promotion.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260429_035444.md
---
Runtime State - Nordlinie 01
============================

Status
------

- slug: nordlinie-01
- scope: project
- state: Probe
- review_state: working

Current State
-------------

- summary: Ronja und Reflex fuehren die Markierungs- und Fehlerarbeit am D5-seitigen Tunnelabschnitt nicht endlos linear fort, sondern ziehen den Folgeanker in Turn 11 wieder nach `D5`. Dort trifft Ronja Jonas, Pahl und Lumen an der Draisine auf den Bahnsteiggleisen, klaert zuerst Baufortschritt, gebundenes Material und Fehlstellen des Prototyps und spiegelt erst danach den beidseitigen Tunnelbedarf gegen denselben Arbeitsort. Parallel bleibt `C6` getrennt lesbar: `Kora` haelt die Station und verarbeitet den Bericht des `C6-Tunneltrupps` als eigene Innenaufgabe. Der gebundene Draisine-Bestand wird dafuer in `../../assets/draisine-transportmodul/inventory.md` gefuehrt, waehrend der eigentliche Nordlinie-Reparaturbedarf jetzt in `inventory.md` als eigener Runtime-Inventartraeger steht.
- drivers:
  - belegt Nordlinie-01 als aktives Tunnelprojekt zwischen D5 und C6
  - belegt Arbeitsteilung Ronja und Reflex im Tunnel, Jonas und Pahl in der D5-Werkstatt; Jonas laeuft dabei nicht allein, sondern mit der gekoppelten Begleitinstanz Lumen
  - Session-Arbeitslesart: Sicherung vor Tempo, Meldung vor Materialdrift
  - Session-Arbeitslesart: D5 beantwortet Bedarf belastbar, aber ohne sofortige Entspannung des Engpasses
  - Session-Arbeitslesart: C6 arbeitet weiter, aber ebenfalls ohne Durchbruch oder freie Materialentlastung
  - Session-Arbeitslesart: Kein Ereignis zwingt eine eigene Zwischenszene vor der naechsten Zusammenfassung
  - Admin-Lesart: Der Wechsel in den SSOT-/Lore-Agenten ist bereits vollzogen; die naechste Szene schliesst direkt an diesen Handover an
  - Session-Arbeitslesart: Der Folgeabschnitt liegt jetzt mit erster Materialerfassung und markierten Schwachzonen lesbarer vor
  - Session-Arbeitslesart: D5 hat die schmale Werkstattvorbereitung fuer Stuetzelemente in einen kleinen realen Turn-7-Satz ueberfuehrt, ohne Schweißgeraet oder DN60 frei zu behaupten
  - Session-Arbeitslesart: Reflex traegt und setzt die improvisierten Sicherungen koerpernah als Ronjas Exoskelett; auch die praktische Assistenz verletzt die Detachment-Lesart nicht
  - Session-Arbeitslesart: Ein kleiner Behelfssatz aus D5 ist im Tunnelzug wirksam geworden und verbessert Sicherung, nicht aber Reparaturgrad
  - Session-Arbeitslesart: Turn 8 fuehrt den Tunnel nur mit dem real verbliebenen Rest des Turn-7-Satzes weiter; weitere Materialfortschreibung braucht ab hier wieder eine explizite D5-Lieferung
  - Session-Arbeitslesart: Der naechste Fehlerkorridor ist jetzt als `Schottertasche Nordkante`, `Haltepunktpaar Leitungszug` und `Uebergang Engbogen` getrennt benannt
  - Session-Arbeitslesart: `Schottertasche Nordkante` ist mit lokaler Baukasten-Nachsicherung als `Band M` eingegrenzt; `Uebergang Engbogen` bleibt mit Schweißgeraet und DN60 ein `Band H`-Blocker
  - Session-Arbeitslesart: Turn 9 verdichtet denselben Hauptpfad jetzt offen ueber `D5`, `C6` und den bilateralen Tunnelkontakt, ohne neue Materialbewegung zu behaupten
  - Session-Arbeitslesart: `D5` fuehrt jetzt eine belastbar knappe Werkstattanforderung fuer `Schweißgeraet`, `DN60`, Anschlusssicherung und vorgelagerte Freiraeumung
  - Session-Arbeitslesart: `C6` arbeitet am Tunnel und haelt zugleich unter `Kora` den Innenbetrieb des Aussenpostens stabil
  - Session-Arbeitslesart: Die nicht eingesetzten Gefluechteten tragen Wasser-, Lager-, Hygiene-, Kuechen-, Wache- und Entlastungsarbeit des laufenden Stationsbetriebs
  - Session-Arbeitslesart: `Mara Quell` bleibt in `C6`; `G7` bleibt ohne Meldung auf altem Wissensstand
  - Session-Arbeitslesart: Ronja erreicht den C6-Trupp jetzt an einem schmalen, behelfshaft sicheren Kontaktpunkt und gleicht die Lage direkt ab
  - Session-Arbeitslesart: Der C6-Tunneltrupp bringt jetzt eigene melderelevante Befunde seiner Haelfte ein und steht nicht nur als bestaetigende Gegenstimme von Ronjas Seite im Raum
  - Session-Arbeitslesart: Neben `Schottertasche Nordkante`, `Haltepunktpaar Leitungszug` und `Uebergang Engbogen` liegen jetzt auch die C6-seitigen Arbeitsstellen `Schuttkeil Kontaktseite`, `Randauflage Suedlauf` und `Leitungsaufnahme C6-Vorlauf` als Folgeanker vor
  - Session-Arbeitslesart: Fuer den Folgezug liegt jetzt eine gemeinsame Bedarfskalkulation mit `Schweißgeraet`, `DN60`, Anschlusssicherung, Verbindungsmaterial, Baukasten-Nachsicherung, C6-seitiger Raeumung und Freiraeumung vor
  - Session-Arbeitslesart: Turn 11 fuehrt Jonas und Pahl nicht in einem stillen Werkstattraum, sondern an der Draisine auf den D5-Bahnsteiggleisen.
  - Session-Arbeitslesart: Ronja klaert zuerst den realen Draisine-Bau- und Materialstand und erst danach den Tunnelbedarf.
  - Session-Arbeitslesart: `Kora` verarbeitet in `C6` denselben Bericht als Stations- und Verteilungsaufgabe; ihre Ebene wird nicht mit Ronjas D5-Rueckkehr vermischt.
  - Session-Arbeitslesart: Der aktuelle Draisine-Eigenbestand liegt jetzt in `../../assets/draisine-transportmodul/inventory.md` getrennt vom Nordlinie-/Tunnelbedarf.
  - Session-Arbeitslesart: Der Nordlinie-Reparaturbedarf liegt jetzt in `inventory.md` als eigener Projekttraeger statt nur verteilt in Szene, State und D5-Bedarfsnotiz.
- blockers:
  - Schweißgeraet fehlt
  - Adapter DN60 fehlen
  - Teilbereitstellung und Tunnelrest reichen nur fuer begrenzte Sicherung einzelner Schwachzonen, nicht fuer eigentliche Reparatur oder Leitungsabschluss
  - keine weitere sofortige Werkstatt- oder Lieferfreigabe aus D5 ueber den kleinen Turn-7-Satz hinaus
  - naechster Materialfortschritt muss als reale D5-Lieferung belegt werden; aus dem ausgeschopften Tunnelrest laesst sich kein weiterer Satz ableiten
  - kein beidseitiger Durchbruch aus C6-Sicht; Fortschritt bleibt vorbereitend statt freigegeben
  - ueber den kleinen Turn-7-Stuetzsatz hinaus bleiben weitere Materialmengen, chargenscharfe Herkunft und jede Folge-Werkstattzusage weiter offen
  - die verdichtete D5-Anforderung ist noch keine reale Freigabe, sondern erst die enge Form eines moeglichen Folgezugs
  - auch der neue Kontaktpunkt der Trupps ist noch kein freier Durchgang oder Materialkorridor
  - C6 fuehrt noch keinen neuen Materialeingang; Innenbetrieb und Tunnelarbeit laufen parallel unter Druck
  - die C6-Haelfte ist nicht reparaturfrei; ihr eigener Befund ist nur noch nicht so tief technisch ausformuliert wie Ronjas D5-seitige Hauptcluster
  - G7 bleibt ohne Meldung blind fuer den frischen Laufstand
- impacted_entities:
  - Nordlinie 01
  - Ronja Kerschner
  - Reflex
  - Jonas Merek
  - Lumen
  - Pahl Brenner
  - Kora Malenkov
  - Echo
  - Mara Quell
  - D5
  - C6
  - Verbindungstunnel D5-C6

Named Problem Clusters (Turn 8)
-------------------------------

- `Schottertasche Nordkante`: seitliche Kante mit ausgespueltem Unterbau; provisorisch beruhigt, voll belastbare Reparaturfolge mit lokaler Unterfuetterung und Baukasten-Nachsicherung jetzt auf `Band M` eingegrenzt.
- `Haltepunktpaar Leitungszug`: zwei noch sitzende, aber nur vorlaeufig tragende Haltepunkte; Anschluss- und Lastbild noch nicht voll freigelegt, Kostenklasse deshalb bewusst offen.
- `Uebergang Engbogen`: verzogener Uebergang vor dem engeren Bogen; belastbare Reparatur erst mit Schweißgeraet, DN60-Adapter und nachgelagerter Sicherung, deshalb `Band H`.

Evidence
--------

- SSOT: `database-rp/01-factions/novapolis/05-projects/Nordlinie-01.md`
- SSOT: `database-rp/01-factions/novapolis/05-projects/Draisine-Transportmodul.md`
- SSOT: `database-rp/01-factions/novapolis/03-locations/Verbindungstunnel-D5-C6.md`
- Runtime: `sessions/d5-c6-nordlinie-sanierung-01/scene-log.md`, Turn 1-3
- Runtime: `sessions/d5-c6-nordlinie-sanierung-01/scene-log.md`, Turn 4
- Runtime: `sessions/d5-c6-nordlinie-sanierung-01/scene-log.md`, Turn 5
- Runtime: `sessions/d5-c6-nordlinie-sanierung-01/scene-log.md`, Turn 6
- Runtime: `sessions/d5-c6-nordlinie-sanierung-01/scene-log.md`, Turn 7
- Runtime: `sessions/d5-c6-nordlinie-sanierung-01/scene-log.md`, Turn 8
- Runtime: `sessions/d5-c6-nordlinie-sanierung-01/scene-log.md`, Turn 9
- Runtime: `sessions/d5-c6-nordlinie-sanierung-01/scene-log.md`, Turn 10
- Runtime: `sessions/d5-c6-nordlinie-sanierung-01/scene-log.md`, Turn 11
- Runtime: `../../assets/draisine-transportmodul/inventory.md`
- Runtime: `inventory.md`

Promotion Notes
---------------

- Kleiner Turn-7-Satz ist mit Turn 8 restseitig ausgeschopft; weitere Promotion oder Materialfortschreibung erst, wenn eine neue Lieferung aus D5 explizit real im Runtime-Zug angekommen ist und die offenen Problemherde weiter technisch geschlossen werden koennen
