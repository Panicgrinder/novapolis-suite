---
stand: 2026-04-27 02:30
update: Novapolis fuehrt jetzt ein konservatives Betriebs- und Nahraummodell T0 fuer D5 als Kernbasis, C6 als Aussenposten und den aktiven D5-C6-Korridor.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260427_022916.md
slug: novapolis
category: faction
status: active
version: "0.1"
tags: [fraktion]
---

Novapolis (Fraktion)
====================

Ueberblick
----------
- Status: aktiv
- Rolle im Setting: junges lokales Versorgungs-, Sicherungs- und Aufbaugeflecht mit einer belastbaren Kernbasis in D5 und einem teilaktiven Aussenposten in C6.

Kerngebiet
----------

- [D5](./03-locations/D5.md): aktive Hauptbasis und sicherster Betriebskern von Novapolis.
- [C6](./03-locations/C6.md): teilaktiver Aussenposten mit begrenzter Kernzone, Monitoringdruck und laufender Rueckkopplung nach D5.

Betriebskorridor T0
-------------------

- `D5` bleibt der einzige voll aktive Fraktionskern von Novapolis.
- Der Korridor `D5 <-> C6` bildet mit [Nordlinie 01](./05-projects/Nordlinie-01.md) den unmittelbaren Arbeits-, Versorgungs- und Sicherheitsraum der Fraktion.
- `C6` bleibt ein teilaktiver Aussenposten desselben Blocks und kein zweiter voll stabiler Kern.
- `E3` bleibt historisch und evakuiert; der Raum wirkt als Risiko- und Monitoringdruck, aber nicht als aktiver Novapolis-Kern.

Rollenlesart T0
---------------

- Ronja Kerschner fuehrt D5 als technische und politische Startlinse des Fraktionskerns.
- Kora Malenkov haelt C6 intern, koppelt Logistik und Rueckmeldung an D5 und filtert lokale Risiken.
- Jonas Merek und Pahl Brenner tragen Werkstatt-, Freigabe- und Sicherheitslogik ueber denselben Korridor.
- Reflex und Echo bleiben keine eigene Bevoelkerung, aber operative Schutz- und Sensorinstanzen im Kernraum.

Betriebsmodell T0
-----------------

- Das konservative Arbeitsmodell fuer Kernbasis, Aussenposten und innere Konfliktlinien liegt in [novapolis-betriebsmodell-t0](./00-doctrine/novapolis-betriebsmodell-t0.md).
- Kernlesart: `D5` fuehrt; `C6` und der dazwischenliegende Korridor bestimmen, wie weit Novapolis praktisch sichern, versorgen und expandieren kann.

Nahraum T0
----------

- Der unmittelbare Novapolis-Nahraum ist jetzt konservativ in [novapolis-nahraum-t0](./00-doctrine/novapolis-nahraum-t0.md) verdichtet.
- Darin sind `D5`, `C6`, der aktive D5-C6-Korridor und die naechsten Druckachsen zusammengezogen.

Assets in diesem Ordner
-----------------------
- Charaktere → ./02-characters/
- Orte → ./03-locations/
- Inventar → ./04-inventory/Novapolis-inventar.md
- Doctrine → ./00-doctrine/
- Projekte → ./05-projects/

Kernfiguren
-----------

- Ronja Kerschner: Technikerin, Kernfigur der D5-Stabilisierung.
- Reflex: emergentes Netz-/Symbiosewesen aus der D5-Reaktor-Stabilisierung; Instanzen/Fragmente möglich (Lumen, Echo).
- Jonas Merek: Mechaniker/Logistik; kam über Verbindungstunnel; grundsätzlich vertrauenswürdig, bleibt in Beobachtung.
- Pahl Brenner: Leittechniker; Überlebender des C6-Reaktorereignisses, in Pflege/Reha.
- Marei Falk: ehem. Leitung E3; heute C6-Organisation/Logistik (Stellvertretung).

Kernorte
--------

- D5: Hauptbasis.
- C6: Aussenposten/teilaktiv.
- E3: evakuiert; Risiko/Anomalie offen.
- Verbindung D5-C6: Projekt Nordlinie 01.
- Verbindung C6-E3: C6-seitig gesichert; Status E3-Ende unklar/risikobehaftet.

Aktueller Stand (Snapshot)
--------------------------

- Bevoelkerung (humanoid, gesamt): ~29 (E3-Evakuierte 20, Karawane 6, Kernteam 3).
- Aktiv: Nordlinie 01 und Draisine-/Transportmodul.
- Hauptorte: D5 (Basis), C6 (Außenposten), E3 (evakuiert/offen).

Offene Fäden
------------

- Nordlinie 01: Material/Tools für den nächsten Schritt fehlen.
- C6: Monitoring/Überwachung auswerten.
- E3: Risiko klären, bevor Reaktivierung diskutiert wird.

Fuehrung & Rollen
-----------------
- **Leitung (Novapolis; Standortleitung D5)**: [Ronja Kerschner](./02-characters/Ronja-Kerschner.md) (Diplomatie, Technik)
- **Stellvertretung (Novapolis; Leitung C6)**: [Kora Malenkov](./02-characters/Kora-Malenkov.md) (Handel ueber C6, Logistikkoordination)
- **Quartiermeisterin (D5)**: [Nika Perez](./02-characters/Nika-Perez.md) (Inventar, Ausgabe, Priorisierung)
- **Sicherheitsoffizier (Novapolis)**: [Pahl Brenner](./02-characters/Pahl-Brenner.md) (Freigaben, Sicherheitslage, Einsatzkoordination)

Offene Punkte
-------------
- [x] Führungs-/Rollenliste ergänzen
- [ ] Diplomatie-Status zu anderen Fraktionen aus `Relationslog-*` spiegeln
- [ ] E3 nur nach neuer Evidenz aus Risiko- in Betriebslogik ueberfuehren

Weiterführend
-------------

- Missionsstatus: [Missionslog-Novapolis](./05-projects/Missionslog-Novapolis.md)
- Campaign-State (fraktionsspezifisch): [novapolis-campaign-state](./00-doctrine/novapolis-campaign-state.md)
- Globales Regelwerk: [Reference-Campaign-State](../../00-admin/Reference-Campaign-State.md)
