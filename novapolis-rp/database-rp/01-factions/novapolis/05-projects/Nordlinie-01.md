---
stand: 2026-04-05 19:43
update: Nordlinie 01 fuehrt jetzt ein startkorridor-taugliches Knowledge-Set und Kernactions fuer den Scheduler-Pfad.
checks: snapshot-lock PASS (2026-04-05 08:10); markdownlint PASS; frontmatter PASS; validate:rp PASS
title: Nordlinie 01 (Tunnel D5-C6)
category: project
slug: nordlinie-01
status: active
locations: ["d5", "c6", "verbindungstunnel-d5-c6"]
dependencies: ["novapolis-inventar", "missionslog"]
version: "1.0"
last_updated: 2026-02-02T18:40:54+01:00
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

Knowledge (24x1h Starter)
-------------------------

```yaml
knowledge:
  - id: know-nordlinie-esb-status-2026-04-05-01
    about: nordlinie_esb_status
    channel: log
    source: projektstatus
    scope: allies_only
    confidence: 0.88
    freshness: 2026-04-05T08:10:00+02:00
    visibility_to: [ronja-kerschner, jonas-merek, pahl-brenner, kora-malenkov]
    attachments: [doc:./Nordlinie-01.md]
  - id: know-nordlinie-c6-fruehwarnung-2026-04-05-01
    about: nordlinie_c6_warning
    channel: reflex_link
    source: c6_monitoring
    scope: allies_only
    confidence: 0.73
    freshness: 2026-04-05T08:10:00+02:00
    visibility_to: [ronja-kerschner, reflex, kora-malenkov]
    attachments: [doc:../03-locations/C6.md]
```

Actions (24x1h Starter)
-----------------------

```yaml
actions:
  - id: act-nordlinie-abschnitt-a-sichern-2026-04-05-01
    verb: sichern
    base_duration_min: 60
    effort: 4
    interruptible: true
    locks: [abschnitt_a]
    may_trigger_event: true
    resources: [stuetzen, markierungskit]
    prerequisites: [know-nordlinie-esb-status-2026-04-05-01]
    outputs: [abschnitt_a_stabil]
    risks: [altschacht_instabilitaet]
  - id: act-nordlinie-trasse-ziehen-b-2026-04-05-01
    verb: reparatur
    base_duration_min: 90
    effort: 4
    interruptible: true
    locks: [abschnitt_b]
    may_trigger_event: true
    resources: [adapter_dn60, werkzeugkit]
    prerequisites: []
    outputs: [trasse_abschnitt_b]
    risks: [materialmangel]
  - id: act-nordlinie-probefahrt-2026-04-05-01
    verb: test
    base_duration_min: 45
    effort: 3
    interruptible: false
    locks: [tunnelkorridor]
    may_trigger_event: true
    resources: [draisine_modul, funkterminal]
    prerequisites: [know-nordlinie-esb-status-2026-04-05-01]
    outputs: [betriebscheck]
    risks: [streckenausfall]
```

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

Tagesleistung (skalierbar)
--------------------------

Wir führen zusätzlich **Arbeitsblöcke** als gemeinsame Basis, damit die Umrechnung in „m/Tag“ nicht driftet.
- 1 Arbeitsblock = 1 Person fokussiert am Tunnel (inkl. Sicherheit/Setup) für einen halben Tag.
- Missionslog-Reporting nutzt: Arbeitsblöcke + betroffene Kennzahl (E/S/B) + Blocker + Beleg/Quittung.
- „m/Tag“ ist abgeleitet (Abschnitt/Material/Blocker-abhängig) und wird nur als Zusatz geführt.

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

- Tagesleistung: Arbeitsblöcke + optional m/Tag (abgeleitet, siehe „Tagesleistung (skalierbar)“)
- Blocker: Instabilitäten, Materialmangel, Fraktionsaktivität
- Personal: Teamliste inkl. Rollen (Leitung/Technik/Logistik/Med)
- Material: Stückliste, Verbrauch/Restbestände (Einheiten)
- Events: Störungen/Unfälle/Entscheidungen (mit Zeitstempel)
- Links: [Logistik](../../../00-admin/Logistik.md), [Missionslog](./Missionslog-Novapolis.md)


