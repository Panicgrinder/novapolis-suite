---
stand: 2026-01-09 03:33
update: Energie-/Verbrauchsmodell konkretisiert (Konten, Tagesabschluss, spielbar vs Hintergrund); last_updated Key vereinheitlicht.
checks: markdownlint-cli2 PASS (targeted) (2026-01-09 03:33); scripts/check_frontmatter.py PASS (targeted) (2026-01-09 03:33)
canvas: Logistik
last_updated: 2025-11-07T04:09:00+01:00
category: admin
slug: logistik
version: 0.9
---

Logistik Novapolis
==================

Fokus: Energie-Konten, Generatoren, Leitungen, Ladefenster, Prioritäten, Transportketten, Beleg-Fluss, Materialien/Bestände.

Energie-Konten
--------------

- D5: Produktion/Verbrauch (kWh, Zellen-%)
- C6: Verbrauch (Teilversorgung über D5 + lokaler Generator)

Tagesabschluss (Buchungen, minimal)
----------------------------------

- Konten (spielbar)
  - `ENERGY_D5_CELLS` (Zellen-%)
  - `ENERGY_C6_CELLS` (Zellen-%)
  - `ENERGY_PIPELINE_D5_C6` (Leitung aktiv/limitiert/aus)
- Konten (Hintergrund/Meta)
  - `ENERGY_D5_BASELOAD_KWH` (Lebenserhalt + Grundlast)
  - `ENERGY_C6_BASELOAD_KWH` (Grundlast + Monitoring)

- Tagesabschluss-Regel (einfach):
  - 1) Grundlast buchen (D5/C6)
  - 2) Projekt-/Mission-Lasten buchen (z. B. Nordlinie-Reparaturtag)
  - 3) Transfer buchen (D5 → C6), wenn Leitung aktiv und Zellen vorhanden
  - 4) Ergebnis als Kurzzeile protokollieren (Bilanz + 1 Satz Ursache)

Beispielbuchung
--------------

- Tag X: D5 −8 (Grundlast), C6 −12 (Grundlast + Monitoring), Transfer D5→C6 +10 ⇒ Netto D5 −18, C6 −2

Generatoren
-----------
- D5-Reaktor: Status 100%, lädt Zellen (Regeln verlinken)
- C6-Generator: repariert, Kapazität/Verbrauch verknüpfen

Leitungen/Schaltzustände
------------------------
- D5↔C6: aktiv, in Reparatur
- Einschränkungen definieren (Infrastruktur limitiert reale Versorgung)

Ladefenster / Prioritäten
-------------------------
- Ladefenster pro Tag (Start/Ende)
- Prioritätenmatrix: Lebenserhalt > Sicherheit > Produktion > Komfort

Transportketten
---------------
- Quelle → Transport → Ziel; Kapazitäten/Wege; Engpässe

Beleg-/Quittungsfluss
---------------------
- Standardfluss: Entnahme (Quelle/Canvas) → Transport → Ankunft (Ziel/Canvas) → Belege/Quittungen → Verantwortliche

Materialien / Bestände
----------------------
- Bestandsliste mit Einheiten (kg/t, m, m², m³, kWh, Zellen-%)
- Trigger für Skalierung (SUPPLY) - Low/Med/High Stufen

Verlinkungen
------------
- [Missionslog](./Missionslog.md)
- [C6 - Logistik-Policy](./C6-Logistik-Policy.md)
- [Admin: Day-Switch & Debug](./Canvas-Admin-Day-Switch-Debug.md)
- [Admin: Timeline (T+0)](./Canvas-T+0-Timeline.md)
- [Projekt: Nordlinie 01](../05-projects/Nordlinie-01.md)
- [Projekt: Karawanenbewegungen](../05-projects/caravan_moves.md)
- [D5](../03-locations/D5.md), [C6](../03-locations/C6.md)


