---
stand: 2026-02-23 02:31
update: Frische-Review durchgeführt; Core-Regeln und Verlinkungen gegen aktuelle Admin-/Fraktions-SSOT geprüft (kein Kanon-Delta).
checks: "npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-rp/database-rp/00-admin/AI-Behavior-Mapping.md' 'novapolis-rp/database-rp/00-admin/memory-bundle.md' 'novapolis-rp/database-rp/00-admin/system-prompt.md' 'novapolis-dev/docs/donelog.md' PASS (2026-02-23 02:33); .\\.venv\\Scripts\\python.exe scripts\\check_frontmatter.py 'novapolis-rp/database-rp/00-admin/AI-Behavior-Mapping.md' 'novapolis-rp/database-rp/00-admin/memory-bundle.md' 'novapolis-rp/database-rp/00-admin/system-prompt.md' 'novapolis-dev/docs/donelog.md' PASS (2026-02-23 02:33); npm --prefix novapolis-rp/coding/tools/validators run validate:rp PASS (2026-02-23 02:33)"
slug: memory-bundle
category: Admin
canvas: memory-bundle
---

Memory-Bundle (Kanon, kompakt)
==============================

Diese Datei ist der „Wahrheitsspeicher“. Änderungen hier sind kanonisch.

Start here: [Current-State.md](./Current-State.md)

Core-Status (eingefroren)
-------------------------

- Load-Order: Diese Datei ist **immer zuerst zu laden**.
- Scope (Core): Nur stabile, kurze Basisfakten + Regeln. Keine Tabellen/Tracker, keine Detail-Metriken.
- Details gehören in Reference/Narrative:
  - Reference: z. B. Inventare, Relationslogs, Wissensmatrix/Taxonomie.
  - Narrative: Scenes/Chronik; Reveals über Missionslog/Scene, nicht als stiller Retcon.

Referenzstandard (slug-only)
----------------------------

- **Semantische ID ist immer `slug`** (Frontmatter-Felder wie `characters`, `locations`, `dependencies` etc.).
- Dateiname/Ordnername ist nur Ablageform.
- Links im Text sind Navigation; Validierung läuft über `slug` (Gates: `validate:rp`, `validate:crossrefs`).

Kanon
-----
- Setting: Post-Collapse-Metro/Stationen; Novapolis-Sektoren (D5 Hauptbasis, C6 Außenposten).
- Leitmotiv: Technik, Improvisation, Wiederaufbau. Ton: ruhig, fokussiert, cinematisch.
- Regeln: Kontinuität > Stil; keine Retcons ohne Absprache; Vorschläge nur auf Anfrage.
- Spielhilfe: Nach jedem SL-Post kurze interne Gedächtnisnotiz (max. 200 Tokens).

Charaktere
----------

Fraktionsspezifische Charakterdetails liegen in den Fraktions-SSOTs:

- Novapolis: [Novapolis](../01-factions/novapolis/Novapolis.md)

Orte
----

Fraktionsspezifische Ortsdetails liegen in den Fraktions-SSOTs:

- Novapolis: [Orte (Novapolis)](../01-factions/novapolis/03-locations/README.md)

Projekte
--------

Fraktionsspezifische Projekte liegen in den Fraktions-SSOTs:

- Novapolis: [Projekte (Ordner)](../01-factions/novapolis/05-projects/)

Offene Fäden (Core-kurz)
------------------------

Offene Fäden werden fraktionslokal geführt, z. B. in:

- [Novapolis](../01-factions/novapolis/Novapolis.md)
- [Missionslog-Novapolis](../01-factions/novapolis/05-projects/Missionslog-Novapolis.md)

Ausgelagerte Details
--------------------

- Reference (Inventar/Timeline-Skizze/Status): [Reference-Campaign-State](./Reference-Campaign-State.md)
- Narrative (Chronik-Anker):
  - [scene-2025-10-27-a](../06-scenes/scene-2025-10-27-a.md) (Status-Ping)
  - [scene-2025-10-27-b](../06-scenes/scene-2025-10-27-b.md) (C6 Monitoring/Lagebild)
  - [scene-2025-10-27-c](../06-scenes/scene-2025-10-27-c.md) (Nordlinie-01: nächster Schritt)

