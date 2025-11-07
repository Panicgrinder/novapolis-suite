---
canvas: Logistik
last-updated: 2025-11-07T04:09:00+01:00
category: A
version: 0.9
---

Logistik Novapolis
==================

Fokus: Energie‑Konten, Generatoren, Leitungen, Ladefenster, Prioritäten, Transportketten, Beleg‑Fluss, Materialien/Bestände.

Energie‑Konten
--------------
- D5: Produktion/Verbrauch (kWh, Zellen %)
- C6: Verbrauch (Teilversorgung über D5)
- Darstellung: Tagesbilanz je Knoten (z. B. „D5 −8 / C6 −12 = −20; D5 +10 ⇒ Netto −10 Zellen“)

Generatoren
-----------
- D5‑Reaktor: Status 100%, lädt Zellen (Regeln verlinken)
- C6‑Generator: repariert, Kapazität/Verbrauch verknüpfen

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

Beleg‑/Quittungsfluss
---------------------
- Standardfluss: Entnahme (Quelle/Canvas) → Transport → Ankunft (Ziel/Canvas) → Belege/Quittungen → Verantwortliche

Materialien / Bestände
----------------------
- Bestandsliste mit Einheiten (kg/t, m, m², m³, kWh, Zellen‑%)
- Trigger für Skalierung (SUPPLY) – Low/Med/High Stufen

Verlinkungen
------------
- [Missionslog](./Missionslog.md)
- [C6 – Logistik‑Policy](./C6-Logistik-Policy.md)
- [Admin: Day‑Switch & Debug](./Canvas-Admin-Day-Switch-Debug.md)
- [Admin: Timeline (T+0)](./Canvas-T+0-Timeline.md)
- [Projekt: Nordlinie 01](../05-projects/Nordlinie-01.md)
- [Projekt: Karawanenbewegungen](../05-projects/caravan_moves.md)
- [D5](../03-locations/D5.md), [C6](../03-locations/C6.md)
