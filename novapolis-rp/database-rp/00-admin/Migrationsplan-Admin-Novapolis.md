---
stand: 2026-02-23 03:01
update: Frische-Review durchgeführt; Template-Scopes/Regeln/Verweise geprüft (kein Inhaltsdelta).
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-rp/database-rp/00-admin/Reference-Campaign-State.md' 'novapolis-rp/database-rp/00-admin/Canvas-T0-Timeline.md' 'novapolis-rp/database-rp/00-admin/Migrationsplan-Admin-Novapolis.md' 'novapolis-dev/docs/donelog.md' PASS (2026-02-23 03:02); .\\.venv\\Scripts\\python.exe scripts\\check_frontmatter.py 'novapolis-rp/database-rp/00-admin/Reference-Campaign-State.md' 'novapolis-rp/database-rp/00-admin/Canvas-T0-Timeline.md' 'novapolis-rp/database-rp/00-admin/Migrationsplan-Admin-Novapolis.md' 'novapolis-dev/docs/donelog.md' PASS (2026-02-23 03:02); npm --prefix novapolis-rp/coding/tools/validators run validate:rp PASS (2026-02-23 03:02)
slug: migrationsplan-admin-template
category: admin
canvas: migration-plan
status: active
version: "0.2"
---

Migrationsplan 00-admin ↔ Fraktionen (Template)
================================================

Ziel
----

Trennung nach Scope:

- `00-admin`: nur allgemein gültige Regeln, Schemata, Prozesse, globale Indizes.
- `01-factions/<fraktion>`: fraktionsspezifische Inhalte (Personen, Orte, Projekte, Missionsstatus, laufende Lage).

Template-Matrix (Dateiebene)
----------------------------

| Quelle (00-admin) | Ziel (Fraktion) | Scope-Klasse | Status | Hinweis |
| --- | --- | --- | --- | --- |
| `Logistik.md` | `01-factions/<fraktion>/00-doctrine/<fraktion>-logistics.md` | `migrate_and_reduce` | in_progress | Admin-Datei bleibt global; operative Details pro Fraktion |
| `Canvas-T0-Timeline.md` | `01-factions/<fraktion>/00-doctrine/<fraktion>-t0-timeline.md` | `migrate_and_reduce` | in_progress | Admin-Datei ist globaler Index; Timeline je Fraktion |
| `Ereignislog-Weltgeschehen.md` | `01-factions/<fraktion>/00-doctrine/<fraktion>-ereignislog.md` | `migrate_and_reduce` | in_progress | Admin-Datei ist globaler Index; Ereignisse je Fraktion |
| `Missionslog.md` | `01-factions/<fraktion>/00-doctrine/<fraktion>-missionslog.md` | `migrate_and_reduce` | in_progress | Admin-Datei ist globaler Rahmen; Missionen je Fraktion |

Harte Regeln
------------

- `00-admin/*` enthält keine stations-/fraktionsspezifischen Fakten.
- Fraktionsinhalte liegen ausschließlich unter `01-factions/<fraktion>/*`.
- Keine Retcons beim Verschieben: Inhalt 1:1 migrieren, erst danach verdichten.
- Nach jeder Mutation: Modul-DONELOG + Lint/FM-Gates.

Migrationsablauf (pro Fraktion)
-------------------------------

1. Quelle in `00-admin` auf globale Regeln/Index reduzieren.
2. Fraktionsdatei unter `01-factions/<fraktion>/00-doctrine/` anlegen oder ergänzen.
3. Inhalte sauber verschieben (kein Duplikat-Drift).
4. Querverweise und ggf. Sidecar-JSON prüfen.
5. `index.json`-Einträge und README-Verweise konsistent halten.

Abnahmekriterien
----------------

- In `00-admin` verbleiben nur globale Rahmeninhalte.
- Fraktionsspezifische Inhalte sind je Fraktion vollständig auffindbar.
- Verweise sind auflösbar, Frontmatter konsistent, Checks grün.

Verlinkungen
------------

- Admin-Logistik: [Logistik](./Logistik.md)
- Admin-Timeline: [Canvas-T0-Timeline](./Canvas-T0-Timeline.md)
- Admin-Ereignislog: [Ereignislog-Weltgeschehen](./Ereignislog-Weltgeschehen.md)
- Fraktions-Doctrine-Ordner: `../01-factions/<fraktion>/00-doctrine/`
