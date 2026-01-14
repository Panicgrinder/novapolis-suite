---
stand: 2026-01-13 02:03
update: Team-/Arbeitsmodus ergänzt (40% Betrieb; Teamwechsel wegen Draisine; Reflex-Last als Frage); Postflight-Receipt ergänzt.
checks: "run_checks_and_report.py PASS (2026-01-13 02:01); npm validate:rp PASS (2026-01-13 02:03); npm validate:crossrefs PASS (2026-01-13 02:03); checks_rp_consistency.py --strict PASS (2026-01-13 02:03)"
title: Nordlinie 01 (Tunnel D5-C6)
category: project
slug: nordlinie-01
status: active
locations: ["d5", "c6", "verbindungstunnel-d5-c6"]
dependencies: ["novapolis-inventar", "missionslog"]
version: "1.0"
last_updated: 2025-11-07T03:32:00+01:00
tags: []
---

Projekt: Nordlinie 01 (Tunnel D5-C6)
-------------------------------------

Ziel
----
Wiederinbetriebnahme des Verbindungstunnels zwischen D5 und C6.

Phasen
------
1) Aufnahme & Kartierung ✓
2) Materialbeschaffung (Schweißgerät, Adapter DN60, Stützen)
3) Abschnittsweise Reparatur (Sicherung → Trassen → Tests)
4) Betriebsaufnahme (Probefahrt/Lasttest)

Aufgabenliste
-------------
- [ ] Stückliste finalisieren
- [ ] Schweißgerät beschaffen/bauen
- [ ] Adapter DN60 fertigen/beschaffen
- [ ] Abschnitt A sichern
- [ ] Abschnitt B Trassen ziehen
- [ ] Abschlussprüfung/Protokoll

Risiken
-------
- Instabilitäten in Altschächten
- Fraktionsaktivität/Diebstahl

Notizen
-------
- Überwachungs-Splitter an C6 liefert Frühwarnungen.

---

Mission Tunnel - Monitoring
---------------------------

- Abschnitte: A/B/C/D (Definition und Länge je Abschnitt)

Fortschritt-Methodik (gegen Drift)
---------------------------------

Wir führen drei getrennte Kennzahlen (0-100%). Dadurch können alte Aussagen („>60%“) und aktuelle Betriebsfähigkeit („40%“) koexistieren, ohne Retcon.

- Erkundungsgrad: Wie viel vom Tunnel ist kartiert/verstanden?
- Sicherungsgrad: Wie viel ist statisch gesichert (Stützen, Gefahrstellen markiert)?
- Betriebsgrad: Wie viel ist für regelmäßige Nutzung freigegeben (Begehbarkeit/Trasse/Tests)?

Reporting-Regel
--------------

- Missionslog/Scenes dürfen verkürzt sprechen (z. B. „wir sind über 60%“), müssen aber klar machen, welche Kennzahl gemeint ist.
- Projektstatus nutzt immer die 3er-Zeile (E/S/B).

Aktueller Stand (Startwerte)
---------------------------

- Erkundung: 65%
- Sicherung: 45%
- Betrieb: 40%

Arbeitsmodus (Teams)
--------------------

- Grundsatz: Es arbeiten kleine Trupps von beiden Seiten (D5 und C6).
- Aktuell (D5-Seite): Ronja und Reflex arbeiten weiter am Tunnel; Jonas und Pahl fokussieren die Werkstattarbeit am Projekt [Draisine-Transportmodul](./Draisine-Transportmodul.md).

Offene Frage (Reflex-Last)
--------------------------

- Wenn D5-seitig primär Ronja+Reflex arbeiten, wird die Frage nach Reflex' Effektivität und Energieverbrauch relevant (Mechanik/Heuristik siehe [Reference-Campaign-State](../../../00-admin/Reference-Campaign-State.md)).

- Tagesleistung: m/Tag/Team; skaliert mit Teamgröße/Erschöpfung
- Blocker: Instabilitäten, Materialmangel, Fraktionsaktivität
- Personal: Teamliste inkl. Rollen (Leitung/Technik/Logistik/Med)
- Material: Stückliste, Verbrauch/Restbestände (Einheiten)
- Events: Störungen/Unfälle/Entscheidungen (mit Zeitstempel)
- Links: [Logistik](../../../00-admin/Logistik.md), [Missionslog](../../../00-admin/Missionslog.md)


