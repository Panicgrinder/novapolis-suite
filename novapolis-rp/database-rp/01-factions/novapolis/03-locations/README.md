---
stand: 2026-04-23 16:00
update: Ortsindex verweist jetzt zusaetzlich auf den Nordlinie-D5-C6-Fortsetzungsindex fuer den aktiven Tunnelstrang.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp/results/reports/checks_report_20260423_155606.md; snapshot-lock PASS (2026-04-23 16:00)
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
- Nordlinie-D5-C6-Fortsetzungsindex → ../Nordlinie-D5-C6-Index.md
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
