---
stand: 2026-02-21 22:11
update: Delta-zum-Missionslog ergänzt und C6-Inventarstände/Offenpunkte evidenzgebunden konsolidiert.
checks: ausstehend (nach Mutation neu ausführen)
title: Inventar - C6
last_updated: 2026-01-11T07:14:00+01:00
category: inventory
slug: c6-inventar
owner: novapolis
scope: location
location: c6
version: "0.1"
tags: []
---

<!-- markdownlint-disable MD025 -->

C6 - Inventar
=============

Policy
------
- Inventare bleiben getrennt; Transfers nur via Mission/Logistik.
- Buchungen mit Quelle/Ziel in [Logistik](../../../00-admin/Logistik.md) dokumentieren.

Bestände (verbucht)
-------------------
- Filter (C6) - belegt, Menge tbd
- Energiezellen (C6) - belegt, Menge tbd
- Werkzeuge (C6) - belegt, Menge/Typen tbd

Potenziale
----------
- Hydrofilter-Behälter (Reserve) - Potenzial vorhanden, Einbindung offen
- Mechanik-Werkzeug (priorisiert, ohne Stückzahlen)

Fehlend / Offen
---------------
- Adapter/Fittings DN60 (kritisch)
- Schweißausrüstung (kritisch)
- Lagerplätze/Containerstruktur für C6-Inventar

Bewegungen (Log)
----------------
- 2026-01-16 [FACT?] Prioritätenliste für C6-Inventar benannt (Filter, Energiezellen, Adapter/Fittings DN60, Schweißausrüstung, Mechanik-Werkzeug; ohne Stückzahlen). Quelle: scene-2026-01-16-a.
- 2026-02-10 17:09 [FACT?] Artefakt 7A im C6-Kontext markiert; Details erst nach Inventarisierung. Quelle: scene-2025-10-27-d.
- 2026-02-10 17:09 [FACT?] Datenkern (tragbar) am Fundort C6 belassen; nicht aufgenommen. Quelle: scene-2025-10-27-x.

Delta zum Missionslog
---------------------

- Delta 1 (belegt): C6-Fund-/Sicherungsanker (Artefakt 7A, Datenkern am Fundort belassen) sind im Missionslog referenziert und im Inventar als offen markiert.
  - Quelle: [Missionslog-Novapolis - C6: Sicherung/Markierung (C6-N3) & Artefakt „7A“](../05-projects/Missionslog-Novapolis.md#c6-sicherungmarkierung-c6-n3--artefakt-7a), [scene-2025-10-27-d](../../../06-scenes/scene-2025-10-27-d.md), [scene-2025-10-27-x](../../../06-scenes/scene-2025-10-27-x.md)
- Delta 2 (belegt/offen): C6-Monitoring/Funk-Abschnitte sind als aktive Missionen geführt; daraus resultierende Material-/Transferdetails bleiben bis Belegzeile offen.
  - Quelle: [Missionslog-Novapolis - C6: Funk/Scan & Stationssuche](../05-projects/Missionslog-Novapolis.md#c6-funkscan--stationssuche), [Missionslog-Novapolis - Monitoring: C6-Überwachung](../05-projects/Missionslog-Novapolis.md#monitoring-c6-überwachung-auswertung)

Aktionen
--------
- [ ] Lagerplätze/Container definieren
- [ ] Verbrauchslog anlegen
