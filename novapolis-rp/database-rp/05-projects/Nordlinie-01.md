---
stand: 2026-01-09 03:33
update: "Fortschritts-Methodik ergänzt (Erkundung/Sicherung/Betrieb), um 40% vs >60% konsistent zu berichten."
checks: scripts/checks_rp_consistency.py PASS (targeted); scripts/check_frontmatter.py PASS (targeted); markdownlint-cli2 PASS (targeted) (2026-01-09 03:33)
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

- Tagesleistung: m/Tag/Team; skaliert mit Teamgröße/Erschöpfung
- Blocker: Instabilitäten, Materialmangel, Fraktionsaktivität
- Personal: Teamliste inkl. Rollen (Leitung/Technik/Logistik/Med)
- Material: Stückliste, Verbrauch/Restbestände (Einheiten)
- Events: Störungen/Unfälle/Entscheidungen (mit Zeitstempel)
- Links: [Logistik](../00-admin/Logistik.md), [Missionslog](../00-admin/Missionslog.md)


