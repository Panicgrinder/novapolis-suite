---
stand: 2026-02-04 09:21
update: Verweis auf caravan-moves aktualisiert.
checks: "npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc '**/*.md' PASS (2026-02-04 09:21)"
canvas: Logistik
last_updated: 2025-11-07T04:09:00+01:00
category: admin
slug: logistik
version: 0.9
---

Logistik Novapolis
==================

Hinweis (Scope)
---------------

Dieses Dokument ist eine Admin-/Reference-Sicht (inkl. Tabellen/Constraints). Die fraktionsweite, diegetische Doctrine liegt unter:
[Novapolis - Logistics](../01-factions/novapolis/00-doctrine/novapolis-logistics.md).

System-/Meta-Notizen gehören nach [Ops / Systemnotes](./ops/README.md).

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
- C6-Generator: Status tbd (keine Instandsetzung/Zahlen ohne belegte Einträge)

Leitungen/Schaltzustände
------------------------
- D5↔C6: Status tbd (keine Reparatur/Verfügbarkeit ohne belegte Einträge)
- Einschränkungen definieren (Infrastruktur limitiert reale Versorgung)

T+0: Harte Constraints aus Scenes (keine Retcons)
-----------------------------------------------

- Keine Tunnel-Instandsetzung behaupten, bis ein belegter Schritt vorliegt (u. a. [scene-2025-10-27-j](../06-scenes/scene-2025-10-27-j.md), [scene-2025-10-27-k](../06-scenes/scene-2025-10-27-k.md), [scene-2025-10-27-m](../06-scenes/scene-2025-10-27-m.md)).
- C6-Zustand nicht beschönigen; C6 bleibt „leer/unrepariert“, solange nichts anderes belegt ist (siehe [scene-2025-10-27-m](../06-scenes/scene-2025-10-27-m.md)).
- Inventar-Änderungen nur nach belegten Einträgen nachziehen (z. B. [scene-2025-10-27-l](../06-scenes/scene-2025-10-27-l.md)).

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
- [D5 - Logistik-Policy](../01-factions/novapolis/03-locations/D5-Logistik-Policy.md)
- [C6 - Logistik-Policy](../01-factions/novapolis/03-locations/C6-Logistik-Policy.md)
- [Admin: Day-Switch & Debug](./Canvas-Admin-Day-Switch-Debug.md)
- [Admin: Timeline (T+0)](./Canvas-T+0-Timeline.md)
- [Projekt: Nordlinie 01](../01-factions/novapolis/05-projects/Nordlinie-01.md)
- [Projekt: Karawanenbewegungen](../01-factions/haendlerbund/05-projects/caravan-moves.md)
- [D5](../01-factions/novapolis/03-locations/D5.md), [C6](../01-factions/novapolis/03-locations/C6.md)


