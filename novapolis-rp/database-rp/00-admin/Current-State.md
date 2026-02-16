---
stand: 2026-02-08 22:51
update: Platzhalter-Links bereinigt; curated Pfad korrigiert.
checks: "not run (link fix)"
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

Hinweis: Referenzen zwischen SSOT-Dokumenten laufen technisch über **`slug`** (nicht Dateinamen).

Referenzstandard und Validator-Gates sind global im [index-rules.md](./index-rules.md) hinterlegt.

Wenn du etwas suchst
--------------------

- Personen/Charaktere: 01-factions/<faction>/02-characters/
- Orte: 01-factions/<faction>/03-locations/
- Inventar: 01-factions/<faction>/04-inventory/
- Projekte: 01-factions/<faction>/05-projects/
- Szenen/Chronik: [06-scenes/](../06-scenes/)
