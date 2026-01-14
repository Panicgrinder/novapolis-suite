---
stand: 2026-01-14 07:48
update: "T+0: Scene-Anker um al/am/an ergänzt (Update-Nachlauf; RP-Rückkehr; RP-Intensivierung). Keine neuen Fakten hinzugefügt. Checks PASS."
checks: "npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-rp/database-rp/00-admin/Canvas-T+0-Timeline.md' PASS (2026-01-14 07:48); & .\\.venv\\Scripts\\python.exe scripts\\check_frontmatter.py 'novapolis-rp/database-rp/00-admin/Canvas-T+0-Timeline.md' PASS (2026-01-14 07:48); npm --prefix novapolis-rp\\coding\\tools\\validators run validate:crossrefs PASS (2026-01-14 07:48)"
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
- Ereignis 1: Status-Ping D5/C6/Nordlinie (Links: [scene-2025-10-27-a](../06-scenes/scene-2025-10-27-a.md), [Nordlinie-01](../01-factions/novapolis/05-projects/Nordlinie-01.md))
- Ereignis 2: Logistik-Check (Material/Bedarf/Absprachen, ohne neue Fakten) (Links: [Logistik](./Logistik.md), [Nordlinie-01](../01-factions/novapolis/05-projects/Nordlinie-01.md))
- Ereignis 3: Sicherheits-/Risiko-Check (Tunnel/E3-Status, ohne neue Fakten) (Links: [C6](../01-factions/novapolis/03-locations/C6.md), [E3](../01-factions/novapolis/03-locations/E3.md))
- Ereignis 4: Fokus-Entscheidung (Material-Run vs Laborphase vs Status-Ping) (Links: [scene-2025-10-27-a](../06-scenes/scene-2025-10-27-a.md))
- Ende: [2025-10-27 10:00] - ATSD: A0-T+0-10:00-S1-D:mid

Scene-Anker (T+0, 2025-10-27)
----------------------------

Hinweis: Diese Liste ist eine reine Verweis-/Belegsammlung aus den vorhandenen Scenes; sie ergänzt keine neuen Canon-Fakten.

- D5 (Start/Setup)
  - [scene-2025-10-27-g](../06-scenes/scene-2025-10-27-g.md) (Wartungsauftrag/Wartungsgang; Werkzeugtasche als beobachtetes Objekt)
  - [scene-2025-10-27-h](../06-scenes/scene-2025-10-27-h.md) (Terminal/Port; System-Link als Anker)
  - [scene-2025-10-27-i](../06-scenes/scene-2025-10-27-i.md) (Basispflege; Wurzelgewebe-Motiv; Exoskelett-Idee)
  - [scene-2025-10-27-j](../06-scenes/scene-2025-10-27-j.md) (Jonas eingeführt; Aufbruchplanung; Tunnel-Assessment als Faden)
  - [scene-2025-10-27-ai](../06-scenes/scene-2025-10-27-ai.md) (D5-Pläne/Grundriss als schematische Bauzeichnung; Versionierung + Disclaimer; Bildanalyse-Anker)
  - [scene-2025-10-27-ak](../06-scenes/scene-2025-10-27-ak.md) (D5: Versorgungsmission + Inventar-Transparenz als IC-Problem; Admin-Stop/Prompt-Requirement)

- C6 (Monitoring/Operation)
  - [scene-2025-10-27-b](../06-scenes/scene-2025-10-27-b.md) (Monitoring/Lagebild; Auswertung als Folgeauftrag)
  - [scene-2025-10-27-d](../06-scenes/scene-2025-10-27-d.md) (C6-N3 Sicherung; Artefakt-Markierung „7A“ als Arbeitsanker)
  - [scene-2025-10-27-e](../06-scenes/scene-2025-10-27-e.md) (C6 Abschluss/Übergabe; Echo-Moment als Statusnotiz)
  - [scene-2025-10-27-f](../06-scenes/scene-2025-10-27-f.md) (C6→D5 Statusmeldung/ToDo-Übergabe)
  - [scene-2025-10-27-k](../06-scenes/scene-2025-10-27-k.md) (C6 Funk/Scan; Stationssuche; Monitoring-Splitter als Option)
  - [scene-2025-10-27-am](../06-scenes/scene-2025-10-27-am.md) (RP-Rückkehr: Scannen vor Berührung; TTS-Parameter; Canvas-Reload; Delete/Redo)
  - [scene-2025-10-27-an](../06-scenes/scene-2025-10-27-an.md) (RP-Intensivierung: Trauma-Trigger; Reflex-Überreaktion; Deeskalation)

- Nordlinie/Logistik
  - [scene-2025-10-27-c](../06-scenes/scene-2025-10-27-c.md) (Nordlinie-01: nächster Schritt/Toolliste)
  - [scene-2025-10-27-l](../06-scenes/scene-2025-10-27-l.md) (Tagesabschluss; Nordlinie-01 als Arbeitsauftrag)
  - [scene-2025-10-27-m](../06-scenes/scene-2025-10-27-m.md) (C6 als Puffer-Policy; Händler-Anbahnung via Reflex; keine Reparatur behaupten)

- Admin/Prozess
  - [scene-2025-10-27-n](../06-scenes/scene-2025-10-27-n.md) (Canvas-Drift; Versionierungsstrategie)
  - [scene-2025-10-27-o](../06-scenes/scene-2025-10-27-o.md) (Vollvalidierung; Fraktionsinventare + Händler; 7-Tage-Fraktionszug)
  - [scene-2025-10-27-p](../06-scenes/scene-2025-10-27-p.md) (Sensoren-Status abfragen; Reflex/Ronja-Dynamik als Anker)
  - [scene-2025-10-27-q](../06-scenes/scene-2025-10-27-q.md) (Konsistenzprüfung neuer Canvas; fehlende Logs/Canvas identifizieren)
  - [scene-2025-10-27-r](../06-scenes/scene-2025-10-27-r.md) (Missionsreview C6; Anomalien in Location/Status; Karawane/Fracht als eigene Logs; nacheinander arbeiten)
  - [scene-2025-10-27-s](../06-scenes/scene-2025-10-27-s.md) (Handel/Diplomatie-Canvas; NPC→Canvas-Regel; C6-Generator-Frage als Wunsch, Status tbd)
  - [scene-2025-10-27-t](../06-scenes/scene-2025-10-27-t.md) (Fraktionsreihenfolge; Archiv statt Overwrite; Relationslog soll Logistik berücksichtigen)
  - [scene-2025-10-27-u](../06-scenes/scene-2025-10-27-u.md) (Index/Meta-Index; maschinenoptimierte Canvas; Clusterpflege/Review)
  - [scene-2025-10-27-v](../06-scenes/scene-2025-10-27-v.md) (AI-Behavior Index V1 überarbeiten; Verhaltenscodes/Skalen als System)
  - [scene-2025-10-27-w](../06-scenes/scene-2025-10-27-w.md) (Verhaltensmuster-Kombinationen Reflex/Ronja; Backup/Diff-Check vor Canvas-Updates)
  - [scene-2025-10-27-x](../06-scenes/scene-2025-10-27-x.md) (Inventar-Trennung D5/C6; Stationsinventar-Regel bei nicht aufgehobenen Funden)
  - [scene-2025-10-27-y](../06-scenes/scene-2025-10-27-y.md) (Systemcheck/Canvas-Lücken: Instanz-Canvas, Dialog-Capture, Gruppen-Canvases, C6-Aufteilung)
  - [scene-2025-10-27-z](../06-scenes/scene-2025-10-27-z.md) (Charakter-Canvas-Workflow Jonas/Pahl/Reflex; Kernfrage Schwester-Status)
  - [scene-2025-10-27-aa](../06-scenes/scene-2025-10-27-aa.md) (Karawanen-Anführerin: Konsistenzfix; Archivierungsregel für fehlerhafte Versionen)
  - [scene-2025-10-27-ab](../06-scenes/scene-2025-10-27-ab.md) (Guardrails: nicht vorsimulieren; nichts herbeizaubern; Kontext-Reset/Reset-Prompt)
  - [scene-2025-10-27-ac](../06-scenes/scene-2025-10-27-ac.md) (Reinit-Prompt nach Kontext-Reset: zu ladende Canvases + feste Regeln + Prüf-Checkliste)
  - [scene-2025-10-27-ad](../06-scenes/scene-2025-10-27-ad.md) (C6-N3 Nachprüfung: mögliche Durchgänge; Mess-/Versorgungsmission; Tunnel-/Bewohner-Korrekturen)
  - [scene-2025-10-27-ae](../06-scenes/scene-2025-10-27-ae.md) (Versorgungsmission Richtung D5; Funk-Stabilisierung; Kontext-Priorisierung + Wissenstrennung)
  - [scene-2025-10-27-af](../06-scenes/scene-2025-10-27-af.md) (Händler-Wissensstand-Korrektur: keine direkten Novapolis-Infos; Fehlerhinweis "Energiespitzen"-Begründung)
  - [scene-2025-10-27-ag](../06-scenes/scene-2025-10-27-ag.md) (Kontextprüfung/Doku; Gewichtung ohne Lückenfüllen; Bestandsdaten-Extraktion als Idee)
  - [scene-2025-10-27-ah](../06-scenes/scene-2025-10-27-ah.md) (Reflex-Details + "Reflex-Grid"; Parallel-RP; D5-Layout/Pläne-Idee)
  - [scene-2025-10-27-aj](../06-scenes/scene-2025-10-27-aj.md) (Kontext-Reload + Delete/Redo; Tonalität/Rollen: Ronja leitet; Sicherheitsentscheidung: Kora/Gruppe weg)
  - [scene-2025-10-27-al](../06-scenes/scene-2025-10-27-al.md) (Update-Nachlauf: Kompatibilitätscheck; Liveschaltung-Fragen; Rückkehr ins RP)

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
- [C6 (Ort)](../01-factions/novapolis/03-locations/C6.md)
- [C6 - Logistik-Policy](./C6-Logistik-Policy.md)

Offene Fragen
-------------
- Wann genau ist T+0 (Uhrzeit/Fenster)?
- Welche Mindest-Marker gelten für Tageswechsel?
- Welche Mission(en) sind T+0 relevant?


