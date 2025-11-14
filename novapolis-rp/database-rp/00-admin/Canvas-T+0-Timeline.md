---
stand: 2025-11-07 04:09
update: frontmatter INIT
checks: pending
canvas: Timeline T+0
last-updated: 2025-11-07T04:09:00+01:00
category: Admin
version: 0.1
---
canvas: Timeline T+0
last-updated: 2025-11-07T04:09:00+01:00
category: Admin
version: 0.1
---

Timeline (T+0)
==============

Kurzüberblick: Starttag (T+0) als Anker für Szenen, Logs und Abrechnungen. Dient als Referenz für Reihenfolgen, Tageswechsel und Debug-Marker.

Eckpunkte
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
- Ereignis 1: Status-Ping D5/C6/Nordlinie - Link: ../06-scenes/scene-2025-10-27-a.md, ../05-projects/Nordlinie-01.md
- Ereignis 2: tbd - Link: [Missionslog/Ort/Projekt]
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
- Admin: Day-Switch & Debug → ./Canvas-Admin-Day-Switch-Debug.md
- Missionslog → ./Missionslog.md
- Logistik (Admin) → ./Logistik.md
- C6 (Ort) → ../03-locations/C6.md
- C6 - Logistik-Policy → ./C6-Logistik-Policy.md

Offene Fragen
-------------
- Wann genau ist T+0 (Uhrzeit/Fenster)?
- Welche Mindest-Marker gelten für Tageswechsel?
- Welche Mission(en) sind T+0 relevant?


