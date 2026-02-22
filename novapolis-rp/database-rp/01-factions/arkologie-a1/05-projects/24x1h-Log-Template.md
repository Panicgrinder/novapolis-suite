---
stand: 2026-02-22 00:17
update: Fraktionsvorlage für 24x1h world_log/pc_log nach globalem 00-admin-Standard angelegt.
checks: "npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc '**/*.md' PASS (2026-02-22 00:09); .\\.venv\\Scripts\\python.exe scripts\\check_frontmatter.py 'novapolis-dev/docs/todo.rp.md' 'novapolis-dev/docs/donelog.md' 'novapolis-rp/database-rp/00-admin' 'novapolis-rp/database-rp/01-factions/novapolis/05-projects' 'novapolis-rp/database-rp/01-factions/haendlerbund/05-projects' 'novapolis-rp/database-rp/01-factions/eisenkonklave/05-projects' 'novapolis-rp/database-rp/01-factions/arkologie-a1/05-projects' 'novapolis-rp/database-rp/01-factions/schienenbund/05-projects' 'novapolis-rp/database-rp/01-factions/schattenbund/05-projects' 'novapolis-rp/database-rp/01-factions/fluesterkollektiv/05-projects' PASS (EXITCODE=0, 2026-02-22 00:09)"
title: 24x1h Log-Template (Arkologie-A1)
category: project
slug: 24x1h-log-template-arkologie-a1
version: "0.1"
status: planned
last_updated: "2026-02-22"
owners: [arkologie-a1]
tags: [rp, template, 24x1h, logs]
relatedSlugs: [missionslog-arkologie-a1, tick-regeln-simulation, sim-state-schema]
---

<!-- markdownlint-disable MD025 -->

24x1h Log-Template (Arkologie-A1)
=================================

Zweck
-----
Diese Vorlage setzt den globalen 24x1h-Standard aus `00-admin` fraktionslokal um.
Sie ist neutral strukturiert; Inhalte werden pro Tick aus Arkologie-A1-Sicht befüllt.

Slot-Header (pro Stunde)
------------------------
- Datum:
- `tick_of_day` (1-24):
- `tick_global`:
- Ort/Segment:
- Verantwortliche Instanz:

world_log (intern, vollständig)
--------------------------------

```yaml
world_log:
  - id: w-YYYYMMDD-HH-01
    about: event_key
    scope: allies_only
    channel: log
    source: system
    confidence: 1.0
    freshness: YYYY-MM-DDTHH:mm:ss+01:00
    notes: ""
```

pc_log (spielerrelevant)
------------------------

```yaml
pc_log:
  - id: p-YYYYMMDD-HH-01
    about: event_key
    scope: pc
    channel: direct
    source: ally
    confidence: 0.8
    freshness: YYYY-MM-DDTHH:mm:ss+01:00
    notes: ""
```

Sichtbarkeitsübergabe
---------------------
- Zulässige Scope-Werte: `private`, `allies_only`, `pc`, `public`, optional `redacted`.
- Rückblende nur als Sichtbarkeitsänderung (`allies_only`/`hidden` -> `pc`), keine Retcons.

Actions-Mini-Template (optional)
--------------------------------

```yaml
actions:
  - id: action-YYYYMMDD-HH-01
    verb: analysieren
    base_duration_min: 60
    effort: 2
    interruptible: true
    locks: []
    may_trigger_event: true
    resources: []
```

Verweise
--------
- Globalregeln: [Tick-Regeln-Simulation](../../../00-admin/Tick-Regeln-Simulation.md)
- Globalschema: [Sim-State-Schema](../../../00-admin/Sim-State-Schema.md)
- Fraktions-Missionslog: [Missionslog-Arkologie-A1](./Missionslog-Arkologie-A1.md)
