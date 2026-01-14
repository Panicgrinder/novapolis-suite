---
stand: 2026-01-14 12:32
update: "Neu: Metro-Grundstruktur (Stationscodes + Knotenliste) angelegt. Receipts aktualisiert (Gates PASS)."
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-rp/database-rp/**/*.md' PASS (2026-01-14 12:32); & .\\.venv\\Scripts\\python.exe scripts\\check_frontmatter.py novapolis-rp\\database-rp PASS (2026-01-14 12:32); & .\\.venv\\Scripts\\python.exe scripts\\checks_rp_consistency.py --strict PASS (2026-01-14 12:32); npm --prefix novapolis-rp\\coding\\tools\\validators run validate:rp PASS (2026-01-14 12:32); npm --prefix novapolis-rp\\coding\\tools\\validators run validate:crossrefs PASS (2026-01-14 12:32)
slug: metrograph-index
category: Admin
canvas: metrograph
---

Metro (Grundstruktur / Metrograph)
=================================

Ziel
----

Ein überprüfbares Grundgerüst für das Metro-/Stationsnetz nach dem Muster **Buchstabe/Zahl** (z. B. D5, C6, H12).

Stationscodierung (P0)
----------------------

- Format: `Letter + Number` (1–2 Ziffern), intern als Slug klein geschrieben (z. B. `d5`).
- Stationen sind Location-SSOTs.
- Verbindungstunnel sind eigenständige Location-SSOTs.

Fraktionszuordnung (P0)
----------------------

|Fraktion|Primäre Station(en)|Hinweis|
|---|---:|---|
|Novapolis|D5, C6, E3|D5/C6 sind intern; E3 evakuiert|
|Arkologie-A1|A1|Station als Arkologie-Knoten|
|Eisenkonklave|H12|Kommandoknoten|
|Händlerbund|G7|Handels-/Umschlagknoten|
|Schattenbund|F9|Schattentransfer-Knoten|
|Schienenbund|B2|Schienen-/Transitknoten|
|Flüsterkollektiv|K4|Signal-/Info-Knoten|

Knoten (SSOT)
-------------

Verifiziert (bestehend)

- [D5](../01-factions/novapolis/03-locations/D5.md)
- [Verbindungstunnel D5–C6](../01-factions/novapolis/03-locations/Verbindungstunnel-D5-C6.md)
- [C6](../01-factions/novapolis/03-locations/C6.md)
- [Verbindungstunnel C6–E3](../01-factions/novapolis/03-locations/Verbindungstunnel-C6-E3.md)
- [E3](../01-factions/novapolis/03-locations/E3.md)

Zugewiesen (neu, Anbindung tbd)

- [A1](../01-factions/arkologie-a1/03-locations/A1.md)
- [H12](../01-factions/eisenkonklave/03-locations/H12.md)
- [G7](../01-factions/haendlerbund/03-locations/G7.md)
- [F9](../01-factions/schattenbund/03-locations/F9.md)
- [B2](../01-factions/schienenbund/03-locations/B2.md)
- [K4](../01-factions/fluesterkollektiv/03-locations/K4.md)

Kanten (vereinfachtes Modell)
-----------------------------

Verifiziert

- D5 ↔ Verbindungstunnel D5–C6 ↔ C6
- C6 ↔ Verbindungstunnel C6–E3 ↔ E3

Geplant / ungeklärt (tbd)

- (tbd) Anbindung externer Knoten (A1/H12/G7/F9/B2/K4) an das Kernnetz

Regeln (Kanon/Guard)
--------------------

- D5: Keine fraktionsfremden NPCs dauerhaft stationiert.
- C6: Nur Mitglieder von Novapolis dauerhaft stationiert.

Links
-----

- Ortsgraph (minimal) → ./Ortsgraph.md
