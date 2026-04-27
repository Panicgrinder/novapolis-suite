---
stand: 2026-04-27 06:11
update: Der Novapolis-Ortsindex ist jetzt ausdruecklich nur noch Graphanker; Detailorte bleiben in ihren eigenen Dateien und der Weltkarte.
checks: snapshot-lock PASS (2026-04-27 06:11)
slug: novapolis-locations
category: index
version: "0.1"
---

Orte (Novapolis)
================

Zweck
-----

Dieser Index bleibt bewusst ein reiner Graphanker fuer den Novapolis-Kernraum.

- Er fuehrt nur den lokalen Knoten- und Korridorzusammenhang der Hauptorte und Tunnelknoten.
- Detailorte und Kompatibilitaetsstubs bleiben in ihren eigenen Dateien.
- Breitere Topologie- und Stationsdetails liegen in der Weltkarte bzw. den jeweiligen Orts-SSOTs.

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
