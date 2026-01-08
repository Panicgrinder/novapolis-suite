---
stand: 2026-01-08 09:25
update: "Timeline-Template operationalisiert (ohne neue Fakten): Festlegung-Block ergänzt; Links konsistent gemacht."
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-rp/database-rp/**/*.md' 'DONELOG.md' PASS (2026-01-08 09:25); python scripts/check_frontmatter.py novapolis-rp/database-rp DONELOG.md PASS (2026-01-08 09:25); python scripts/checks_rp_consistency.py --strict PASS (2026-01-08 09:25)
slug: canvas-t-0-timeline
canvas: Timeline T+0
last-updated: 2025-11-07T04:09:00+01:00
category: Admin
version: 0.1
---

Timeline (T+0)
==============

Kurzüberblick: Starttag (T+0) als Anker für Szenen, Logs und Abrechnungen. Dient als Referenz für Reihenfolgen, Tageswechsel und Debug-Marker.

Festlegung (T+0) - Entscheidung erforderlich
-------------------------------------------

- Datum (ISO): tbd (YYYY-MM-DD)
- Startzeit: tbd (hh:mm)
- Endzeit: tbd (hh:mm)
- Auslöser/Trigger für Start: tbd
- Auslöser/Trigger für Ende: tbd
- ATSD-Definition: siehe [Admin: Day-Switch & Debug](./Canvas-Admin-Day-Switch-Debug.md)

Eckpunkte
---------
- Tagesanfang: tbd (Uhrzeit, Auslöser)
- Schlüsselereignisse: tbd (Check-In, Systemmeldungen, Missionen)
- Tagesende: tbd (Abschluss, Persistenz-Speicher, Archivierung)

Sequenz (Tagesablauf)
---------------------
1. Kontext laden (Canvas-Zahl, ATSD-String notieren)
2. Statusmeldungen prüfen (Energie/Inventar/Missionen)
3. Aktionen/Missionen ausführen (Prozess L.1 beachten)
4. Abschluss/Archiv (Inventarabschluss, Verlinkungen, Archiv)

Marker (T+0) - Raster
---------------------
- Beginn: [tbd 19:30] - ATSD: A0-T+0-19:30-S0-D:small
- Ereignis 1: Status-Ping D5/C6/Nordlinie (Links: [scene-2025-10-27-a](../06-scenes/scene-2025-10-27-a.md), [Nordlinie-01](../05-projects/Nordlinie-01.md))
- Ereignis 2: tbd (Links: [Missionslog](./Missionslog.md), [Logistik](./Logistik.md))
- Ende: [tbd 22:00] - ATSD: A{n}-T+0-22:00-S1-D:mid

Debug-Hinweise
--------------
- ATSD-String + Canvas-Zahl bei Beginn/Ende erfassen
- Debug-Mode optional zuschaltbar (siehe „Admin: Day-Switch & Debug“)
- Abweichungen/Drift in einem eigenen Abschnitt dokumentieren

Delta-Log (Abweichungen)
------------------------
- [Zeit] - [Beobachtung] - [Link/Evidenz]

Links
-----
- [Admin: Day-Switch & Debug](./Canvas-Admin-Day-Switch-Debug.md)
- [Missionslog](./Missionslog.md)
- [Logistik (Admin)](./Logistik.md)
- [C6 (Ort)](../03-locations/C6.md)
- [C6 - Logistik-Policy](./C6-Logistik-Policy.md)

Offene Fragen
-------------
- Wann genau ist T+0 (Uhrzeit/Fenster)?
- Welche Mindest-Marker gelten für Tageswechsel?
- Welche Mission(en) sind T+0 relevant?


