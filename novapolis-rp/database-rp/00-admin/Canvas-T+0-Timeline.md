---
stand: 2026-01-09 05:22
update: "T+0 festgelegt (Option A): Morgenfenster 07:00-10:00 am 2025-10-27; Marker-Raster auf 5 Slots erweitert."
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-rp/database-rp/**/*.md' PASS (2026-01-09 05:22); & .\.venv\Scripts\python.exe scripts\check_frontmatter.py novapolis-rp\database-rp PASS (2026-01-09 05:22); & .\.venv\Scripts\python.exe scripts\checks_rp_consistency.py --strict PASS (2026-01-09 05:22)
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

- Datum (ISO): 2025-10-27
- Startzeit: 07:00
- Endzeit: 10:00
- Auslöser/Trigger für Start: Morgen nach der C6-Operation (Statusabgleich/Planung)
- Auslöser/Trigger für Ende: Fokus-Entscheidung + Plan (Material-Run vs Laborphase vs Status-Ping)
- ATSD-Definition: siehe [Admin: Day-Switch & Debug](./Canvas-Admin-Day-Switch-Debug.md)

Eckpunkte
---------
- Tagesanfang: 07:00 (T+0 Start)
- Schlüsselereignisse: Status-Ping + Planung/Entscheidung (ohne neue Fakten)
- Tagesende: 10:00 (T+0 Ende)

Sequenz (Tagesablauf)
---------------------
1. Kontext laden (Canvas-Zahl, ATSD-String notieren)
2. Statusmeldungen prüfen (Energie/Inventar/Missionen)
3. Aktionen/Missionen ausführen (Prozess L.1 beachten)
4. Abschluss/Archiv (Inventarabschluss, Verlinkungen, Archiv)

Marker (T+0) - Raster
---------------------
- Beginn: [2025-10-27 07:00] - ATSD: A0-T+0-07:00-S0-D:small
- Ereignis 1: Status-Ping D5/C6/Nordlinie (Links: [scene-2025-10-27-a](../06-scenes/scene-2025-10-27-a.md), [Nordlinie-01](../05-projects/Nordlinie-01.md))
- Ereignis 2: Logistik-Check (Material/Bedarf/Absprachen, ohne neue Fakten) (Links: [Logistik](./Logistik.md), [Nordlinie-01](../05-projects/Nordlinie-01.md))
- Ereignis 3: Sicherheits-/Risiko-Check (Tunnel/E3-Status, ohne neue Fakten) (Links: [C6](../03-locations/C6.md), [E3](../03-locations/E3.md))
- Ereignis 4: Fokus-Entscheidung (Material-Run vs Laborphase vs Status-Ping) (Links: [scene-2025-10-27-a](../06-scenes/scene-2025-10-27-a.md))
- Ende: [2025-10-27 10:00] - ATSD: A0-T+0-10:00-S1-D:mid

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
- [Reference: Campaign State](./Reference-Campaign-State.md)
- [Missionslog](./Missionslog.md)
- [Logistik (Admin)](./Logistik.md)
- [C6 (Ort)](../03-locations/C6.md)
- [C6 - Logistik-Policy](./C6-Logistik-Policy.md)

Offene Fragen
-------------
- Wann genau ist T+0 (Uhrzeit/Fenster)?
- Welche Mindest-Marker gelten für Tageswechsel?
- Welche Mission(en) sind T+0 relevant?


