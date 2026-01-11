---
stand: 2026-01-09 06:23
update: Narrative erweitert: zwei weitere Chronik-Anker-Scenes (T+0) verlinkt.
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-rp/database-rp/**/*.md' PASS (2026-01-09 06:26); & .\.venv\Scripts\python.exe scripts\check_frontmatter.py novapolis-rp\database-rp PASS (2026-01-09 06:26); & .\.venv\Scripts\python.exe scripts\checks_rp_consistency.py --strict PASS (2026-01-09 06:26)
slug: memory-bundle
category: Admin
canvas: memory-bundle
---

Memory-Bundle (Kanon, kompakt)
==============================

Diese Datei ist der „Wahrheitsspeicher“. Änderungen hier sind kanonisch.

Core-Status (eingefroren)
-------------------------

- Load-Order: Diese Datei ist **immer zuerst zu laden**.
- Scope (Core): Nur stabile, kurze Basisfakten + Regeln. Keine Tabellen/Tracker, keine Detail-Metriken.
- Details gehören in Reference/Narrative:
  - Reference: z. B. Inventare, Relationslogs, Wissensmatrix/Taxonomie.
  - Narrative: Scenes/Chronik; Reveals über Missionslog/Scene, nicht als stiller Retcon.

Kanon
-----
- Setting: Post-Collapse-Metro/Stationen; Novapolis-Sektoren (D5 Hauptbasis, C6 Außenposten).
- Leitmotiv: Technik, Improvisation, Wiederaufbau. Ton: ruhig, fokussiert, cinematisch.
- Regeln: Kontinuität > Stil; keine Retcons ohne Absprache; Vorschläge nur auf Anfrage.
- Spielhilfe: Nach jedem SL-Post kurze interne Gedächtnisnotiz (max. 200 Tokens).

Charaktere
----------
- Ronja Kerschner: Technikerin, Kernfigur der D5-Stabilisierung. (Details: [Ronja-Kerschner](../02-characters/Ronja-Kerschner.md))
- Reflex: emergentes Netz-/Symbiosewesen aus der D5-Reaktor-Stabilisierung; Instanzen/Fragmente möglich (Lumen, Echo). (Details: [Reflex](../02-characters/Reflex.md))
- Jonas Merek: Mechaniker/Logistik; kam über Verbindungstunnel; grundsätzlich vertrauenswürdig, bleibt in Beobachtung. (Details: [Jonas-Merek](../02-characters/Jonas-Merek.md))
- Pahl: Leittechniker; Überlebender des C6-Reaktorereignisses, in Pflege/Reha. (Details: [Pahl](../02-characters/Pahl.md))
- Marei: ehem. Leitung E3; heute C6-Organisation/Logistik (Stellvertretung). (Details: [Marei](../02-characters/Marei.md))

Orte
----
- D5: Hauptbasis. (Details: [D5](../03-locations/D5.md))
- C6: Außenposten/Teilaktiv. (Details: [C6](../03-locations/C6.md))
- E3: evakuiert; Risiko/Anomalie offen. (Details: [E3](../03-locations/E3.md))
- Verbindung D5–C6: Projekt „Nordlinie 01“. (Details: [Verbindungstunnel-D5-C6](../03-locations/Verbindungstunnel-D5-C6.md), [Nordlinie-01](../05-projects/Nordlinie-01.md))
- Verbindung C6–E3: C6-seitig gesichert; Status E3-Ende unklar/risikobehaftet. (Details: [Verbindungstunnel-C6-E3](../03-locations/Verbindungstunnel-C6-E3.md))

Projekte
--------

- Nordlinie 01: Wiederinbetriebnahme des Verbindungstunnels D5–C6; Fortschritt wird getrennt berichtet (Erkundung/Sicherung/Betrieb). (Details: [Nordlinie-01](../05-projects/Nordlinie-01.md))
- E3: Reaktivierung ist offen; Warnmeldungen/Anomalie müssen geklärt werden. (Details: [E3](../03-locations/E3.md))

Offene Fäden (Core-kurz)
------------------------

- Nordlinie 01: Material/Tools für den nächsten Schritt fehlen.
- C6: Monitoring/Überwachung auswerten.
- E3: Risiko klären, bevor Reaktivierung diskutiert wird.

Ausgelagerte Details
--------------------

- Reference (Inventar/Timeline-Skizze/Status): [Reference-Campaign-State](./Reference-Campaign-State.md)
- Narrative (Chronik-Anker):
  - [scene-2025-10-27-a](../06-scenes/scene-2025-10-27-a.md) (Status-Ping)
  - [scene-2025-10-27-b](../06-scenes/scene-2025-10-27-b.md) (C6 Monitoring/Lagebild)
  - [scene-2025-10-27-c](../06-scenes/scene-2025-10-27-c.md) (Nordlinie-01: nächster Schritt)

