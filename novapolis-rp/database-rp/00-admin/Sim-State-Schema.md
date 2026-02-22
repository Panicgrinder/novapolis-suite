---
stand: 2026-02-22 00:17
update: 24x1h Dual-Log-Felder (world_log/pc_log inkl. Sichtbarkeitsmetadaten) im globalen Schema ergänzt.
checks: "npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc '**/*.md' PASS (2026-02-22 00:09); .\\.venv\\Scripts\\python.exe scripts\\check_frontmatter.py 'novapolis-dev/docs/todo.rp.md' 'novapolis-dev/docs/donelog.md' 'novapolis-rp/database-rp/00-admin' 'novapolis-rp/database-rp/01-factions/novapolis/05-projects' 'novapolis-rp/database-rp/01-factions/haendlerbund/05-projects' 'novapolis-rp/database-rp/01-factions/eisenkonklave/05-projects' 'novapolis-rp/database-rp/01-factions/arkologie-a1/05-projects' 'novapolis-rp/database-rp/01-factions/schienenbund/05-projects' 'novapolis-rp/database-rp/01-factions/schattenbund/05-projects' 'novapolis-rp/database-rp/01-factions/fluesterkollektiv/05-projects' PASS (EXITCODE=0, 2026-02-22 00:09)"
slug: sim-state-schema
category: Admin
schemaVersion: 1
language: de
status: draft
tags: [rp, simulation, state, schema]
relatedSlugs: [current-state, process-workflow, logistik, missionslog]
---

Sim-State-Schema (RP)
=====================

Zweck
-----
Maschinenlesbares Schema fuer den Weltzustand (Simulation) im Novapolis-Setting.
Das Schema definiert minimale Pflichtfelder fuer Zeit, Orte, Fraktionen, Ressourcen,
Projekte, Inventare, Beziehungen und Ereignisse.

Leitprinzipien
--------------
- Slug-only: Referenzen nutzen immer `slug`-IDs.
- Keine Retcons: Zustand aendert sich nur mit Belegen (Missionslog/Scenes).
- Minimal, aber eindeutig: Werte, Einheiten, Status und Zeitbezug sind explizit.
- Setting-fokussiert: D5/C6/E3, Nordlinie-01, C6-Nordanomalie, Fraktionslage.

Schema (JSON, v1)
-----------------

```json
{
  "schema_version": "1.0",
  "generated_at": "YYYY-MM-DDTHH:mm:ss+01:00",
  "source": {
    "memory_bundle": "memory-bundle",
    "current_state": "current-state",
    "missionslog": "missionslog",
    "logistik": "logistik"
  },
  "time": {
    "tick": 0,
    "tick_unit": "hour",
    "t0": "YYYY-MM-DD",
    "now": "YYYY-MM-DD"
  },
  "hourly_logs": {
    "world_log": [
      {
        "id": "w-0001",
        "about": "event_key",
        "scope": "allies_only",
        "channel": "log",
        "source": "system",
        "confidence": 1.0,
        "freshness": "YYYY-MM-DDTHH:mm:ss+01:00",
        "notes": ""
      }
    ],
    "pc_log": [
      {
        "id": "p-0001",
        "about": "event_key",
        "scope": "pc",
        "channel": "direct",
        "source": "ally",
        "confidence": 0.8,
        "freshness": "YYYY-MM-DDTHH:mm:ss+01:00",
        "notes": ""
      }
    ]
  },
  "locations": [
    {
      "slug": "d5",
      "status": "aktiv",
      "population_humanoid": 3,
      "connections": ["c6"],
      "risks": ["resource_shortage"],
      "notes": ""
    },
    {
      "slug": "c6",
      "status": "teilaktiv",
      "population_humanoid": 27,
      "connections": ["d5", "e3"],
      "risks": ["anomaly_c6_nord"],
      "notes": ""
    },
    {
      "slug": "e3",
      "status": "evakuiert",
      "population_humanoid": 0,
      "connections": ["c6"],
      "risks": ["anomaly_e3"],
      "notes": ""
    }
  ],
  "factions": [
    {
      "slug": "novapolis",
      "type": "local",
      "stability": "medium",
      "supply": "low",
      "relations": {
        "haendlerbund": "neutral",
        "eisenkonklave": "neutral",
        "arkologie-a1": "unknown",
        "schienenbund": "neutral"
      }
    }
  ],
  "projects": [
    {
      "slug": "nordlinie-01",
      "status": "active",
      "progress": {
        "exploration": 65,
        "securing": 45,
        "operation": 40
      },
      "work_blocks": 0,
      "blockers": ["material_missing"],
      "dependencies": ["novapolis-inventar", "missionslog"]
    },
    {
      "slug": "draisine-transportmodul",
      "status": "prototyping",
      "work_blocks": 0,
      "blockers": ["tunnel_clearance"],
      "dependencies": ["logistik", "missionslog", "nordlinie-01"]
    }
  ],
  "inventory": [
    {
      "slug": "d5-inventar",
      "location": "d5",
      "items": [
        {"item": "energiezelle-standard", "qty": 0, "unit": "stk"},
        {"item": "luftfilter-gasmasken", "qty": 0, "unit": "stk"}
      ]
    },
    {
      "slug": "c6-inventar",
      "location": "c6",
      "items": [
        {"item": "wasserfilter-portabel", "qty": 0, "unit": "stk"}
      ]
    }
  ],
  "logistics": {
    "energy_accounts": {
      "ENERGY_D5_CELLS": {"value": 0, "unit": "pct"},
      "ENERGY_C6_CELLS": {"value": 0, "unit": "pct"},
      "ENERGY_PIPELINE_D5_C6": {"value": "off", "unit": "state"}
    },
    "transfers": []
  },
  "events": [
    {
      "id": "evt-0001",
      "type": "anomaly",
      "location": "c6",
      "status": "active",
      "source": "missionslog"
    }
  ]
}
```

Pflichtfelder (minimal)
-----------------------
- `time.tick`, `time.tick_unit`, `time.t0`, `time.now`
- `hourly_logs.world_log[]`, `hourly_logs.pc_log[]`
- je Logeintrag: `scope`, `channel`, `source`, `confidence`, `freshness`
- `locations[].slug`, `locations[].status`, `locations[].connections`
- `factions[].slug`, `factions[].type`, `factions[].relations`
- `projects[].slug`, `projects[].status`
- `inventory[].slug`, `inventory[].location`, `inventory[].items[]`
- `logistics.energy_accounts`

Validierungsregeln (kurz)
-------------------------
- `slug`-Referenzen muessen in SSOT existieren.
- Prozentwerte: 0-100, ganze Zahlen.
- `tick_unit`: `day` oder `hour` (nur eine Einheit pro Schema).
- `status`-Felder nur aus definierten Enum-Werten.

Enum-Werte (Auszug)
-------------------
- `location.status`: `aktiv`, `teilaktiv`, `evakuiert`, `verlassen`
- `project.status`: `active`, `prototyping`, `paused`, `completed`
- `faction.relations`: `allied`, `cooperative`, `neutral`, `wary`, `hostile`, `unknown`

Erweiterung (v2 geplant)
------------------------
- Fraktions-Subgruppen, Handelsrouten, Kapazitaeten
- Ressourcenverbrauch pro Tick
- Agenten-/NPC-Population mit Rollenprofilen
- Ereignis-Timeline mit Dauer und Triggern
