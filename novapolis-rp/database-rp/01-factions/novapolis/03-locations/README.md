---
stand: 2026-01-11 06:20
update: Indexdatei für Fraktions-Orte angelegt.
checks: markdownlint-cli2 PASS; frontmatter PASS; rp-consistency PASS
slug: novapolis-locations
category: index
version: "0.1"
---

Orte (Novapolis)
================

Zweck
-----

Ablage aller **Orts-SSOTs**, die primär Novapolis zugeordnet sind.

Nützliche Links
---------------

- Fraktionsordner → ../README.md
- Fraktionen-Taxonomie → ../../../00-admin/Fraktionen-Taxonomie.md

Topologie / Ortsgraph
---------------------

Knoten

- [D5](./D5.md) (Hauptbasis)
- [Verbindungstunnel D5–C6](./Verbindungstunnel-D5-C6.md)
- [C6](./C6.md) (Außenposten)
- [Verbindungstunnel C6–E3](./Verbindungstunnel-C6-E3.md)
- [E3](./E3.md) (evakuiert)

Kanten (vereinfachtes Modell)

- D5 ↔ Verbindungstunnel D5–C6 ↔ C6
- C6 ↔ Verbindungstunnel C6–E3 ↔ E3

Konsistenzregeln
----------------

- Verbindungen sind symmetrisch: Wenn A in `connections:` B nennt, muss B in `connections:` A nennen.
- Tunnel-Dateien sind eigenständige Knoten (nicht nur Text): Verbindungen laufen bevorzugt über Tunnel-Knoten.
- Narrative Details (Szenenverlauf, ad-hoc Status) liegen in `../../../06-scenes/` und werden nur als Link in Locations referenziert.
