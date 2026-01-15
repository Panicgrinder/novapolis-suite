---
title: "Scenes: Definition & Template"
date: 2025-11-12 08:59
tags: [doc]
stand: 2026-01-15 06:52
update: "Scene-XREFs: Klarstellung auf slug-only + Validierungstext aktualisiert. Checks PASS."
checks: "& .\\.venv\\Scripts\\python.exe scripts\\run_checks_and_report.py PASS"
slug: scenes-konventionen-stub
---

Scenes: Definition & Template
-----------------------------

Ziel: Szenen sind die **Narrative-Schicht**. Sie dokumentieren Entscheidungen und Konsequenzen nachvollziehbar, ohne den Canon-Core aufzublähen.

Grundregeln
-----------

- Keine Retcons ohne Decision/Absprache.
- Änderungen an Orten/Inventar/Projekten passieren als **Konsequenz** (und werden verlinkt).
- Wenn eine Szene neue Fakten setzt, muss sie auf die betroffenen SSOT-Dateien verweisen.

Frontmatter (Empfehlung)
------------------------

Pflichtfelder für `06-scenes/*.md`:

- `id`, `slug`, `date`, `category: scene`
- `characters`, `locations`, `inventoryRefs` (Listen; dürfen leer sein)
- `stand`, `update`, `checks`, `last_updated`

Hinweis: `scripts/checks_rp_consistency.py` prüft, dass `characters/locations/inventoryRefs` auf existierende SSOT-**Slugs** zeigen (d. h. auf das `slug:`-Feld der Ziel-Datei).

Pflichtabschnitte im Body
-------------------------

Jede Scene soll mindestens enthalten:

- **Kurzbeschreibung** (2–4 Sätze)
- **Kernentscheidungen** (Bulletliste)
- **Konsequenzen / Statusänderungen** (Bulletliste; verlinkt auf Orte/Projekte/Inventar/Logistik/Missionslog)
- **Offene Fäden** (Bulletliste)
- **Links** (Querverweise; mindestens Timeline + relevante Orte/Projekte)

Template
--------

```markdown
---
stand: YYYY-MM-DD HH:mm
update: Kurznotiz
checks: PENDING
last_updated: YYYY-MM-DDTHH:mm:ss+01:00
slug: scene-YYYY-MM-DD-x
id: scene-YYYY-MM-DD-x
category: scene
date: YYYY-MM-DD
characters: []
locations: []
inventoryRefs: []
version: "1.0"
tags: []
---

Szene: <Titel>
==============

Kurzbeschreibung: <2-4 Sätze>

Kernentscheidungen
------------------
- <Entscheidung>

Konsequenzen / Statusänderungen
-------------------------------
- <Konsequenz> (Link: <SSOT-Datei>)

Offene Fäden
------------
- <Faden>

Links
-----
- Timeline (T+0) → ../00-admin/Canvas-T+0-Timeline.md
- Missionslog → ../00-admin/Missionslog.md
- Logistik → ../00-admin/Logistik.md
```

Validierung (Gates)
-------------------

- `npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-rp/database-rp/**/*.md'`
- `python scripts/check_frontmatter.py novapolis-rp/database-rp`
- `python scripts/checks_rp_consistency.py --strict`


