---
stand: 2026-02-22 04:16
update: T0-Gesamtbild-Referenzen (Metrokarte, Stationskontroll-Matrix, Warenueberblick) ergänzt.
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc '**/*.md' PASS (2026-02-22 02:26); .\\.venv\\Scripts\\python.exe scripts\\check_frontmatter.py 'novapolis-rp/database-rp/00-admin/index-rules.md' 'novapolis-rp/database-rp/00-admin/Current-State.md' 'novapolis-rp/database-rp/00-admin/Logistik.md' 'novapolis-rp/database-rp/00-admin/Metrograph.md' 'novapolis-rp/database-rp/00-admin/Ortsgraph.md' 'novapolis-rp/database-rp/00-admin/Canvas-Admin-Day-Switch-Debug.md' 'novapolis-rp/database-rp/00-admin/Kernkonversationen.md' 'novapolis-rp/database-rp/00-admin/Metrokarte-T0.md' 'novapolis-rp/database-rp/00-admin/Stationskontroll-Matrix.md' 'novapolis-rp/database-rp/00-admin/Warenueberblick-T0.md' 'novapolis-dev/docs/donelog.md' PASS (2026-02-22 02:27)
slug: current-state
category: Admin
canvas: current-state
---

Current State
=============

Zweck
-----

Dieser Eintrag ist der **Single Entry Point** für den aktuellen, spielrelevanten Stand.
Er verweist bewusst auf die SSOT-Dokumente (Canon-Core + veränderliche Referenzen), statt Inhalte zu duplizieren.

Kurzstart (Start here)
----------------------

- Canon-Core (stabil, sparsam): [memory-bundle.md](memory-bundle.md)
- Laufender Stand (bewusst veränderlich): [Reference-Campaign-State.md](Reference-Campaign-State.md)
- Timeline/Entscheidungen/Verlauf: [Missionslog.md](Missionslog.md) und [Ereignislog-Weltgeschehen.md](Ereignislog-Weltgeschehen.md)
- Orte & Verbindungen: [Ortsgraph.md](Ortsgraph.md)

Snapshot (kurz, abgeleitet)
---------------------------

Hinweis: Fraktionsspezifische Snapshots werden in den jeweiligen Fraktions-SSOTs gepflegt.

- Novapolis-Snapshot: [Novapolis](../01-factions/novapolis/Novapolis.md)

Snapshot-Quellen (Gate-Pflicht)
------------------------------

Jede Fraktion muss im Current-State über **Missionslog + Inventar** referenziert sein.

- Arkologie-A1: [Missionslog](../01-factions/arkologie-a1/05-projects/Missionslog-Arkologie-A1.md), [Inventar](../01-factions/arkologie-a1/04-inventory/README.md)
- Eisenkonklave: [Missionslog](../01-factions/eisenkonklave/05-projects/Missionslog-Eisenkonklave.md), [Inventar](../01-factions/eisenkonklave/04-inventory/README.md)
- Flüsterkollektiv: [Missionslog](../01-factions/fluesterkollektiv/05-projects/Missionslog-Fluesterkollektiv.md), [Inventar](../01-factions/fluesterkollektiv/04-inventory/README.md)
- Händlerbund: [Missionslog](../01-factions/haendlerbund/05-projects/Missionslog-Haendlerbund.md), [Inventar](../01-factions/haendlerbund/04-inventory/README.md)
- Novapolis: [Missionslog](../01-factions/novapolis/05-projects/Missionslog-Novapolis.md), [Inventar](../01-factions/novapolis/04-inventory/README.md)
- Schattenbund: [Missionslog](../01-factions/schattenbund/05-projects/Missionslog-Schattenbund.md), [Inventar](../01-factions/schattenbund/04-inventory/README.md)
- Schienenbund: [Missionslog](../01-factions/schienenbund/05-projects/Missionslog-Schienenbund.md), [Inventar](../01-factions/schienenbund/04-inventory/README.md)

Aktive Projekte (Kurzliste)
---------------------------

Fraktionsspezifische Projekte werden in den Fraktionsordnern geführt:

- Novapolis-Projekte: [Ordner](../01-factions/novapolis/05-projects/)

Hauptorte (Kurzstatus)
----------------------

Fraktionsspezifische Ortszustände werden in den Fraktionsordnern geführt:

- Novapolis-Orte: [Orte (Novapolis)](../01-factions/novapolis/03-locations/README.md)

Chronik-Anker (Startpunkte)
---------------------------

- [scene-2025-10-27-a.md](../06-scenes/scene-2025-10-27-a.md)
- [scene-2025-10-27-b.md](../06-scenes/scene-2025-10-27-b.md)
- [scene-2025-10-27-c.md](../06-scenes/scene-2025-10-27-c.md)

Namensdrift (separat behandeln)
------------------------------

Namens-/Alias-Regeln sind global in `index-rules.md` dokumentiert.

Stationen D5/C6 (v1.0)
----------------------

- Ziel: Mit vorhandenen Daten D5 und C6 vollständig pflegen (Struktur/Abschnitte/Links), ohne neue Fakten zu erfinden.
- Praxis: Fehlende Details als offene Aufgaben markieren (statt zu raten) und über Missionslog/Scenes belegen, bevor sie in Core wandern.

T0-Gesamtbild (operativ)
------------------------

- Metrokarte (T0): [Metrokarte-T0.md](Metrokarte-T0.md)
- Stationskontrolle (T0): [Stationskontroll-Matrix.md](Stationskontroll-Matrix.md)
- Warenueberblick (T0): [Warenueberblick-T0.md](Warenueberblick-T0.md)

Arbeitsfluss (SSOT/RAW/curated)
-------------------------------

- **SSOT (RP):** [database-rp/](..) (dieser Bereich)
- **RAW-Exporte:** [database-raw/99-exports](../../database-raw/99-exports/README.md) (ungefiltert, nur dort)
- **Curated:** [database-curated](../../database-curated/README.md) (staging/reviewed/final)

Regel: Neue Fakten gehen nicht direkt in den Canon-Core, solange sie noch volatil sind. Nutze dafür zuerst die Reference-Ebene.

Validatoren (Gates)
-------------------

- Slug-Unique + Kategorie-Schema: `npm --prefix novapolis-rp\coding\tools\validators run validate:rp`
- Crossrefs (slug-only): `npm --prefix novapolis-rp\coding\tools\validators run validate:crossrefs`
- Current-State-Gate (Snapshot-Ableitung): `& .\.venv\Scripts\python.exe scripts\check_current_state_gate.py`

Hinweis: Referenzen zwischen SSOT-Dokumenten laufen technisch über **`slug`** (nicht Dateinamen).

Referenzstandard und Validator-Gates sind global im [index-rules.md](./index-rules.md) hinterlegt.

Wenn du etwas suchst
--------------------

- Personen/Charaktere: 01-factions/<faction>/02-characters/
- Orte: 01-factions/<faction>/03-locations/
- Inventar: 01-factions/<faction>/04-inventory/
- Projekte: 01-factions/<faction>/05-projects/
- Szenen/Chronik: [06-scenes/](../06-scenes/)
