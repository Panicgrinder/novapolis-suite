---
stand: 2026-01-07 18:47
update: Fraktionsnamen (Anzeige) aktualisiert (Händlerbund/Schienenbund).
checks: markdownlint-cli2 PASS; scripts/check_frontmatter.py PASS; scripts/checks_rp_consistency.py --strict PASS (2026-01-07 18:53)
slug: cluster_index_v1
category: admin
status: draft
version: "0.1"
---

Cluster-Index (v1)
==================

Zweck
-----
- Referenz für Fraktions- und Cluster-Signaturen (Eisenkonklave, Arkologie, Händlerbund, Schienenbund).
- Liefert die Diplomatie-/Prioritätswerte aus `database-raw/99-exports/RAW-canvas-2025-10-16T16-55-00-000Z.txt`.
- Ergänzt `AI-Behavior-Mapping.md` um Cluster-spezifische Kontextdaten (z. B. Konfliktpotenziale, Führungen, aktive Systeme).

Aktueller Stand
---------------
- Cluster `eisenkonklave_operativ`: Priorität mittel, Systeme `relationslog_eisenkonklave_v1`, `handelslog_eisenkonklave_v1`.
- Cluster `arkologie_a1`: Priorität mittel, Systeme `relationslog_arkologie_v1`.
- Cluster `schattenbund_feld` (Schienenbund): Priorität mittel, Systeme `relationslog_schattenbund_v1`.
- Cluster `haendlergilde_extern` (Händlerbund): Priorität niedrig, Systeme `relationslog_haendlergilde_v1`, `handelslog_haendlergilde_v1`.

ToDo
----
- Detailaufschlüsselung pro Cluster (Mitglieder, Orte, Diplomatie) in Tabellenform übernehmen.
- Schnittstellen zu Missionslog/Logistik referenzieren.
- Versionierung aus dem RAW-Canvas übernehmen und Validierungsintervall ergänzen.
