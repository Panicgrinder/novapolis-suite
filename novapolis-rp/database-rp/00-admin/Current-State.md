---
stand: 2026-02-04 13:10
update: Links auf relative Pfade normalisiert.
checks: "npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc '**/*.md' PASS (2026-02-04 13:10)"
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

Hinweis: Dieser Snapshot ist **nur eine Kurzliste** und verweist auf die SSOT-Quelle. Wenn etwas unklar/konfliktär ist: erst im Missionslog/Scenes verorten, dann als Decision festnageln.

- Bevölkerung (humanoid, gesamt): ~29 (Quelle: [resolved.md](../../database-curated/staging/reports/resolved.md), FACT [POP])
  - Breakdown (kurz): Evakuierte aus E3 = 20; Karawane = 6; Kernteam (Ronja/Jonas/Pahl) = 3
  - Reflex-Instanzen (Reflex/Echo/Lumen) sind zusätzlich und zählen nicht zur humanoiden Zahl

Aktive Projekte (Kurzliste)
---------------------------

- Nordlinie 01 (D5↔C6): [Nordlinie-01.md](../01-factions/novapolis/05-projects/Nordlinie-01.md)
- Draisine-/Transportmodul (D5): [Draisine-Transportmodul.md](../01-factions/novapolis/05-projects/Draisine-Transportmodul.md)

Hauptorte (Kurzstatus)
----------------------

- D5 (Hauptbasis): [D5.md](../01-factions/novapolis/03-locations/D5.md)
- C6 (Außenposten/teilaktiv): [C6.md](../01-factions/novapolis/03-locations/C6.md)
- E3 (evakuiert; Risiko/Anomalie offen): [E3.md](../01-factions/novapolis/03-locations/E3.md)
- Tunnel D5↔C6: [Verbindungstunnel-D5-C6.md](../01-factions/novapolis/03-locations/Verbindungstunnel-D5-C6.md)
- Tunnel C6↔E3: [Verbindungstunnel-C6-E3.md](../01-factions/novapolis/03-locations/Verbindungstunnel-C6-E3.md)

Chronik-Anker (Startpunkte)
---------------------------

- [scene-2025-10-27-a.md](../06-scenes/scene-2025-10-27-a.md)
- [scene-2025-10-27-b.md](../06-scenes/scene-2025-10-27-b.md)
- [scene-2025-10-27-c.md](../06-scenes/scene-2025-10-27-c.md)

Namensdrift (separat behandeln)
------------------------------

- Keine stillen Umbenennungen in SSOT. Namens-/Alias-Entscheidungen werden separat dokumentiert und dann konsistent nachgezogen.
- Token-Regel: Einfache Buchstaben-Zahlenkombinationen (z. B. D5, C6, E3, F1) sind **für Stations-/Liniencodes reserviert**.
- Legacy-Token wie „N7“ werden **nicht** als Alias weitergeführt (Verwechslungsgefahr mit Stationen); stattdessen werden sprechende Namen verwendet (z. B. „C6-Nordanomalie“).

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

Referenzstandard (slug-only)
----------------------------

- **ID ist immer `slug`** (auch in Listen wie `characters`, `locations`, `dependencies`, `owners`).
- Dateiname/Ordnername ist nur Ablageform und darf **nie** als Referenz-Token benutzt werden.
- Markdown-Links dienen der Navigation; semantische Zuordnung/Validierung läuft über `slug`.

Wenn du etwas suchst
--------------------

- Personen/Charaktere: [01-factions/<faction>/02-characters/](../01-factions/<faction>/02-characters/)
- Orte: [01-factions/<faction>/03-locations/](../01-factions/<faction>/03-locations/)
- Inventar: [01-factions/<faction>/04-inventory/](../01-factions/<faction>/04-inventory/)
- Projekte: [01-factions/<faction>/05-projects/](../01-factions/<faction>/05-projects/)
- Szenen/Chronik: [06-scenes/](../06-scenes/)
