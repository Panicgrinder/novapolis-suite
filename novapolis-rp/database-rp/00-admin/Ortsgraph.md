---
stand: 2026-01-09 05:12
update: P0: Ortsgraph als minimalen Index definiert (D5↔C6↔E3 via Tunnel-Knoten).
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-rp/database-rp/**/*.md' PASS (2026-01-09 05:12); & .\.venv\Scripts\python.exe scripts\check_frontmatter.py novapolis-rp\database-rp PASS (2026-01-09 05:12); & .\.venv\Scripts\python.exe scripts\checks_rp_consistency.py --strict PASS (2026-01-09 05:12)
slug: ortsgraph-index
category: Admin
canvas: ortsgraph
---

Ortsgraph (Index, minimal)
=========================

Ziel: Ein kleines, überprüfbares Ortsnetz als Basis für Konsistenz-Checks und Querverlinkungen.

Graph (Knoten und Kanten)
-------------------------

Knoten (SSOT)

- [D5](../01-factions/novapolis/03-locations/D5.md) (Hauptbasis)
- [Verbindungstunnel D5–C6](../01-factions/novapolis/03-locations/Verbindungstunnel-D5-C6.md)
- [C6](../01-factions/novapolis/03-locations/C6.md) (Außenposten)
- [Verbindungstunnel C6–E3](../01-factions/novapolis/03-locations/Verbindungstunnel-C6-E3.md)
- [E3](../01-factions/novapolis/03-locations/E3.md) (evakuiert)

Kanten (vereinfachtes Modell)

- D5 ↔ Verbindungstunnel D5–C6 ↔ C6
- C6 ↔ Verbindungstunnel C6–E3 ↔ E3

Pflichtfelder pro Ort (P0)
--------------------------

Jede Location-Datei unter `../03-locations/` soll mindestens enthalten:

- Status
- Bevölkerung (falls relevant; bei „keine“ explizit so markieren)
- Infrastruktur / Zugänge
- Risiken
- Offene Aufgaben

Konsistenzregeln
----------------

- Verbindungen sind symmetrisch: Wenn A in `connections:` B nennt, muss B in `connections:` A nennen.
- Tunnel-Dateien sind eigenständige Knoten (nicht nur Text): Verbindungen laufen bevorzugt über Tunnel-Knoten.
- Narrative Details (Szenenverlauf, ad-hoc Status) liegen in `../06-scenes/` und werden nur als Link in Locations referenziert.

Links
-----
- Canon-Core → ../00-admin/memory-bundle.md
- Timeline (T+0) → ../00-admin/Canvas-T+0-Timeline.md
