---
stand: 2026-02-23 04:15
update: Frische-Review durchgeführt; Ortsgraph-Regeln, Pflichtfelder und Verweise weiterhin gültig (kein Kanon-Delta).
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-rp/database-rp/00-admin/Ortsgraph.md' PASS (2026-02-23 04:15); .\\.venv\\Scripts\\python.exe scripts\\check_frontmatter.py 'novapolis-rp/database-rp/00-admin/Ortsgraph.md' PASS (2026-02-23 04:15); npm --prefix novapolis-rp/coding/tools/validators run validate:rp PASS (2026-02-23 04:15)
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
