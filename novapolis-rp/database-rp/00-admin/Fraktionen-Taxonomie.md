---
stand: 2026-01-13 02:03
update: N7-Benennung als Alias standardisiert (C6-Nordanomalie); Postflight-Receipt ergänzt.
checks: "run_checks_and_report.py PASS (2026-01-13 02:01); npm validate:rp PASS (2026-01-13 02:03); npm validate:crossrefs PASS (2026-01-13 02:03); checks_rp_consistency.py --strict PASS (2026-01-13 02:03)"
slug: fraktionen-taxonomie
category: admin
canvas: fraktionen-taxonomie
status: draft
version: "0.1"
---

Fraktionen (Taxonomie & Wissensmatrix)
=====================================

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

- **Freie Gruppen** (Sammelkategorie)
  - Referenzen: Inventar [Freie Gruppen](../04-inventory/Freie-Gruppen-inventar.md)
- **Karawanen-/Splittergruppen**
  - Referenzen: [caravan_moves](../01-factions/haendlerbund/05-projects/caravan_moves.md)

Wissensmatrix (Default)
-----------------------

Hinweis: Diese Matrix ist ein Default-Startwert für Informationskontrolle. Anpassungen passieren über Scenes/Missionslog; keine stillen Retcons.

### Themen

- **Nordlinie / Tunnel D5↔C6** (Projekt: [Nordlinie-01](../01-factions/novapolis/05-projects/Nordlinie-01.md))
- **E3** (evakuiert; Monitoring/Anomalie offen)
- **C6-Nordanomalie** (Anomalie; versiegelt; Alias: N7; siehe [Missionslog](./Missionslog.md))

### Matrix

| Gruppe | Nordlinie (D5↔C6) | E3 | C6-Nordanomalie (Alias: N7) |
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
