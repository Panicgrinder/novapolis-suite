---
stand: 2026-04-27 05:33
update: Nordlinie 01 beschreibt den D5-C6-Korridor jetzt klar als bereits genutzten Arbeitsweg, dessen Belastbarkeit und Materialfuehrung ausgebaut werden.
checks: snapshot-lock PASS (2026-04-27 04:18); npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-rp/database-rp/01-factions/novapolis/05-projects/Nordlinie-01.md' 'novapolis-rp/database-rp/01-factions/novapolis/03-locations/Verbindungstunnel-C6-E3.md' 'novapolis-rp/database-rp/01-factions/novapolis/03-locations/C6.md' 'novapolis-dev/docs/donelog.md' PASS (2026-04-27 04:26); .venv-py313-backup-20260409_1832/Scripts/python.exe scripts/check_frontmatter.py 'novapolis-rp/database-rp/01-factions/novapolis/05-projects/Nordlinie-01.md' 'novapolis-rp/database-rp/01-factions/novapolis/03-locations/Verbindungstunnel-C6-E3.md' 'novapolis-rp/database-rp/01-factions/novapolis/03-locations/C6.md' 'novapolis-dev/docs/donelog.md' PASS (2026-04-27 04:26); npm --prefix novapolis-rp/coding/tools/validators run validate:rp PASS (2026-04-27 04:26)
title: Nordlinie 01 (Tunnel D5-C6)
category: project
slug: nordlinie-01
status: active
locations: ["d5", "c6", "verbindungstunnel-d5-c6"]
dependencies: ["novapolis-inventar", "missionslog"]
version: "1.0"
last_updated: 2026-04-27T04:18:00+02:00
tags: []
---

Projekt: Nordlinie 01 (Tunnel D5-C6)
-------------------------------------

Ziel
----
Belastbarkeitsausbau des bereits genutzten Verbindungstunnels zwischen D5 und C6 fuer sichereren Arbeits-, Material- und spaeteren Trassenbetrieb.

Phasen
------
1) Aufnahme & Kartierung ✓
2) Materialbeschaffung (Schweißgerät, Adapter DN60, Stuetzbaukasten)
3) Abschnittsweise Sicherung und Reparatur (Sicherung → Trassen → Tests)
4) Belastbarkeitsausbau (Probefahrt/Lasttest ohne freie Vollinstandsetzung zu behaupten)

Aufgabenliste
-------------
- [ ] Stückliste finalisieren
- [ ] Stuetzbaukasten zaehlbar fuehren
- [ ] Schweißgerät beschaffen/bauen
- [ ] Adapter DN60 fertigen/beschaffen
- [ ] Abschnitt A sichern
- [ ] Abschnitt B Trassen ziehen
- [ ] Abschlussprüfung/Protokoll

Material- und Buchungsstand (kleiner Turn-7-Satz)
-------------------------------------------------

| Klasse | Transfer aus D5 | im D5-seitigen Tunnel eingesetzt | Rest vor Ort | Notiz |
| --- | --- | --- | --- | --- |
| Metallprofil (mittel) | `2` | `2` | `0` | fuer die tragfaehigeren der zwei beruhigten Stellen |
| Metallprofil (kurz) | `4` | `3` | `1` | Versteifung und Unterfuetterung |
| Stuetzklemme | `4` | `4` | `0` | direkte Fixierung an markierten Schwachzonen |
| Lasche / Knotenblech | `2` | `2` | `0` | Lastverteilung der improvisierten Baugruppen |
| Ausgleichsplatte | `2` | `1` | `1` | eine Platte als kleiner Tunnelrest fuer die naechste enge Stelle |
| Schraubensatz (mittel) | `4 Sets` | `3 Sets` | `1 Set` | kontrollierbare Verbindung statt freier Notloesung |
| Bolzen-Mutter-Satz (stark) | `1 Set` | `1 Set` | `0` | nur fuer den staerkeren Punkt eingesetzt |
| Klebmasse (schwach) | `1 Kartusche` | `1 Kartusche` | `0` | nur ausrichtend/fixierend, nicht tragend |

Hinweise

- Nordlinie 01 bedeutet nicht, den ersten Fussweg zwischen `D5` und `C6` ueberhaupt erst herzustellen; der Korridor ist bereits als Arbeitsweg genutzt, das Projekt zieht vor allem Sicherheit, Stuetzung, Materialfuehrung und spaetere Lastfaehigkeit nach.

- Der Satz bleibt bewusst klein: genug fuer zwei beruhigte Schwachzonen, nicht genug fuer Reparaturdurchbruch oder Leitungsabschluss.
- `Schweißgeraet` und `Adapter DN60` bleiben weiterhin die eigentlichen Hauptblocker; die Buchung hier schliesst nur die kleine Turn-7-Teilbereitstellung.

Risiken
-------
- Instabilitäten in Altschächten
- Fraktionsaktivität/Diebstahl

Notizen
-------
- Überwachungs-Splitter an C6 liefert Frühwarnungen.
- `Stuetzen` meint fuer Nordlinie 01 ab jetzt den komponentenbasierten Baukasten aus Profilen, Formteilen und Verbindungsmitteln; siehe [Nordlinie-01-Stuetzbaukasten](./Nordlinie-01-Stuetzbaukasten.md).
- Im Actions-Block bleibt `stuetzen` vorerst als Legacy-Kurzform stehen, bis Folgesysteme auf `stuetzbaukasten` umgestellt sind.
- Der kleine Turn-7-Satz ist jetzt konservativ klassenweise gebucht; offen bleiben weitere Folgeabgaenge, Ruecklaeufe und eine vollstaendige chargenscharfe Historie.

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
- Betriebsgrad: Wie viel ist fuer regelmaessigere Nutzung ueber den bereits moeglichen Fussbetrieb hinaus freigegeben (Trasse/Tests/Belastbarkeit)?

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


