---
stand: 2026-02-23 04:21
update: Frische-Review durchgeführt; Fraktionsrahmen, Wissensmatrix und T0-Abgleich weiterhin gültig (kein Kanon-Delta).
checks: "npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-rp/database-rp/00-admin/Fraktionen-Taxonomie.md' PASS (2026-02-23 04:22); .\\.venv\\Scripts\\python.exe scripts\\check_frontmatter.py 'novapolis-rp/database-rp/00-admin/Fraktionen-Taxonomie.md' PASS (2026-02-23 04:22); npm --prefix novapolis-rp/coding/tools/validators run validate:rp PASS (2026-02-23 04:22)"
slug: fraktionen-taxonomie
category: admin
canvas: fraktionen-taxonomie
status: draft
version: "0.1"
---

Fraktionen-Taxonomie
====================

Zweck
-----

- Stabiler Rahmen für „vier Hauptfraktionen“ vs. weitere Gruppen, ohne Retcons.
- Spielbare Informationskontrolle: Wer weiß was über Tunnel/E3/C6-Nord.
- Schichtentrennung: Core (stabil) → Reference (Objekte/Tabellen) → Narrative (Scenes).

Definitionen
------------

- **Hauptfraktion**: überregionaler Machtblock mit stabiler Identität.
- **Zelle/Cluster**: operative Einheit innerhalb einer Hauptfraktion (kann als eigener Name auftreten).
- **Wissensstufen** (für SL-Steuerung, nicht als harte Lore):
  - **H** (high): verifiziert/operativ bekannt.
  - **M** (medium): teilbekannt, Gerüchte + einzelne Belege.
  - **L** (low): kaum/gar nicht bekannt.

Token-Regel (Stationscodes)
--------------------------

- Einfache Buchstaben-Zahlenkombinationen (z. B. D5, C6, E3, F1) sind **für Stations-/Liniencodes reserviert** und treten nur als solche (historisch/technisch) auf.
- Abgeleitete, lokale Bezeichner dürfen vorkommen, müssen aber **präfixiert** sein (z. B. `C6-N3`) und sind keine eigenständigen Stationen.
- Für Anomalien, Projekte, Personen, Fraktionen und Artefakte werden **sprechende Namen** genutzt.
- Der Legacy-Token „N7“ wird **nicht** als Alias weitergeführt, um Verwechslung mit einer Station auszuschließen.

Taxonomie (aktuell)
-------------------

### Lokal (Novapolis)

- **Novapolis** (D5/C6): lokale Kernfraktion.
  - Referenzen: [memory-bundle](./memory-bundle.md), [Missionslog](./Missionslog.md)

### Externe Hauptfraktionen (Set „4“)

- **Eiserne Enklave** (extern)
  - Referenzen: Inventar [Eiserne-Enklave](../01-factions/eisenkonklave/04-inventory/Eiserne-Enklave-inventar.md)
  - Operative Zellen/Cluster (Default): **Eisenkonklave** als benannte operative Einheit.
    - Referenzen: [Eisenkonklave](../01-factions/eisenkonklave/Eisenkonklave.md), [Relationslog Eisenkonklave](../01-factions/eisenkonklave/06-handel-diplomatie/Relationslog-Eisenkonklave.md)
- **Arkologie** (extern)
  - Referenzen: Inventar [Arkologie](../01-factions/arkologie-a1/04-inventory/Arkologie-inventar.md)
- **Händlerbund** (extern)
  - Referenzen: Inventar [Händlerbund](../01-factions/haendlerbund/04-inventory/Haendlerbund-inventar.md)
- **Schienenbund** (extern)
  - Referenzen: Inventar [Schienenbund](../01-factions/schienenbund/04-inventory/Schienenbund-inventar.md)

### Weitere Gruppen (nicht „Hauptfraktion“)

- **Freie Gruppen** (Sammelkategorie für fraktionslose NPC)
  - Referenzen: Inventar [Freie Gruppen](../04-inventory/Freie-Gruppen-inventar.md)
- **Karawanen-/Splittergruppen**
  - Referenzen: [caravan-moves](../01-factions/haendlerbund/05-projects/caravan-moves.md)

Minimal-Abgleich Basis-/Known-Stationen (T0)
--------------------------------------------

Der folgende Abgleich verbindet Fraktions-Basis/known stations mit der Admin-SSOT fuer Karte/Kontrolle.

| Fraktion | Basis/known stations (T0) | Fraktionsanker | Admin-SSOT |
| --- | --- | --- | --- |
| Novapolis | D5, C6, E3 | [Novapolis](../01-factions/novapolis/Novapolis.md), [D5](../01-factions/novapolis/03-locations/D5.md), [C6](../01-factions/novapolis/03-locations/C6.md), [E3](../01-factions/novapolis/03-locations/E3.md) | [Metrokarte-T0](./Metrokarte-T0.md), [Stationskontroll-Matrix](./Stationskontroll-Matrix.md), [Warenueberblick-T0](./Warenueberblick-T0.md) |
| Arkologie-A1 | A1 | [Arkologie-A1](../01-factions/arkologie-a1/Arkologie-A1.md), [A1](../01-factions/arkologie-a1/03-locations/A1.md) | [Metrokarte-T0](./Metrokarte-T0.md), [Stationskontroll-Matrix](./Stationskontroll-Matrix.md), [Warenueberblick-T0](./Warenueberblick-T0.md) |
| Schienenbund | B2 | [Schienenbund](../01-factions/schienenbund/Schienenbund.md), [B2](../01-factions/schienenbund/03-locations/B2.md) | [Metrokarte-T0](./Metrokarte-T0.md), [Stationskontroll-Matrix](./Stationskontroll-Matrix.md), [Warenueberblick-T0](./Warenueberblick-T0.md) |
| Schattenbund | F9 | [Schattenbund](../01-factions/schattenbund/Schattenbund.md), [F9](../01-factions/schattenbund/03-locations/F9.md) | [Metrokarte-T0](./Metrokarte-T0.md), [Stationskontroll-Matrix](./Stationskontroll-Matrix.md), [Warenueberblick-T0](./Warenueberblick-T0.md) |
| Haendlerbund | G7 | [Haendlerbund](../01-factions/haendlerbund/Haendlerbund.md), [G7](../01-factions/haendlerbund/03-locations/G7.md) | [Metrokarte-T0](./Metrokarte-T0.md), [Stationskontroll-Matrix](./Stationskontroll-Matrix.md), [Warenueberblick-T0](./Warenueberblick-T0.md) |
| Eisenkonklave | H12 | [Eisenkonklave](../01-factions/eisenkonklave/Eisenkonklave.md), [H12](../01-factions/eisenkonklave/03-locations/H12.md) | [Metrokarte-T0](./Metrokarte-T0.md), [Stationskontroll-Matrix](./Stationskontroll-Matrix.md), [Warenueberblick-T0](./Warenueberblick-T0.md) |
| Fluesterkollektiv | K4 | [Fluesterkollektiv](../01-factions/fluesterkollektiv/Fluesterkollektiv.md), [K4](../01-factions/fluesterkollektiv/03-locations/K4.md) | [Metrokarte-T0](./Metrokarte-T0.md), [Stationskontroll-Matrix](./Stationskontroll-Matrix.md), [Warenueberblick-T0](./Warenueberblick-T0.md) |

Wissensmatrix (Default)
-----------------------

Hinweis: Diese Matrix ist ein Default-Startwert für Informationskontrolle. Anpassungen passieren über Scenes/Missionslog; keine stillen Retcons.

### Themen

- **Nordlinie / Tunnel D5↔C6** (Projekt: [Nordlinie-01](../01-factions/novapolis/05-projects/Nordlinie-01.md))
- **E3** (evakuiert; Monitoring/Anomalie offen)
- **C6-Nordanomalie** (Anomalie; versiegelt; siehe [Missionslog](./Missionslog.md))

### Matrix

| Gruppe | Nordlinie (D5↔C6) | E3 | C6-Nordanomalie |
| --- | --- | --- | --- |
| Novapolis | H | H | H |
| Händlerbund | M | L | L |
| Schienenbund | M | L | L |
| Arkologie | L | L | L |
| Eiserne Enklave (inkl. Eisenkonklave-Cluster) | M | L | L |
| Freie Gruppen | L | L | L |

Schichtenregel (Core vs Reference vs Narrative)
-----------------------------------------------

- **Core** (memory-bundle): nur Existenz/Benennung der Hauptfraktionen + 1 Satz „Druck von außen“; keine Matrixwerte.
- **Reference** (dieses Dokument + Inventare + Relationslogs): Details, Tabellen, Zustände, Metriken.
- **Narrative** (Scenes): konkrete Begegnungen, Reveals, Gerüchte, Eskalationen; jede neue harte Info braucht Decision/Beleg.
