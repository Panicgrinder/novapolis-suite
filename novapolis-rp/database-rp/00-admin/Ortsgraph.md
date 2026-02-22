---
stand: 2026-02-22 04:16
update: Veralteten Timeline-Link auf kanonisches Canvas-T0-Timeline-Ziel korrigiert.
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc '**/*.md' PASS (2026-02-22 02:26); .\\.venv\\Scripts\\python.exe scripts\\check_frontmatter.py 'novapolis-rp/database-rp/00-admin/index-rules.md' 'novapolis-rp/database-rp/00-admin/Current-State.md' 'novapolis-rp/database-rp/00-admin/Logistik.md' 'novapolis-rp/database-rp/00-admin/Metrograph.md' 'novapolis-rp/database-rp/00-admin/Ortsgraph.md' 'novapolis-rp/database-rp/00-admin/Canvas-Admin-Day-Switch-Debug.md' 'novapolis-rp/database-rp/00-admin/Kernkonversationen.md' 'novapolis-rp/database-rp/00-admin/Metrokarte-T0.md' 'novapolis-rp/database-rp/00-admin/Stationskontroll-Matrix.md' 'novapolis-rp/database-rp/00-admin/Warenueberblick-T0.md' 'novapolis-dev/docs/donelog.md' PASS (2026-02-22 02:27)
slug: ortsgraph-index
category: Admin
canvas: ortsgraph
---

Ortsgraph (Index, minimal)
=========================

Ziel: Ein kleines, überprüfbares Ortsnetz als Basis für Konsistenz-Checks und Querverlinkungen.

Hinweis: Fraktionsspezifische Ortsgraphen liegen bei den Fraktionen (z. B. Novapolis unter `01-factions/novapolis/03-locations/README.md`).

Graph (Knoten und Kanten)
-------------------------

Knoten (SSOT)

- Beispiel (Novapolis): [Orte (Novapolis)](../01-factions/novapolis/03-locations/README.md)

Kanten (vereinfachtes Modell)

- Fraktionslokal definieren (siehe Fraktions-Ortsgraphen).

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
- Timeline (T+0) → ../00-admin/Canvas-T0-Timeline.md
