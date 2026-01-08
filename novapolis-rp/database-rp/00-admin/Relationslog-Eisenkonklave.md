---
stand: 2026-01-07 18:47
update: Fraktionsnamen (Anzeige) aktualisiert (Händlerbund/Schienenbund).
checks: markdownlint-cli2 PASS; scripts/check_frontmatter.py PASS; scripts/checks_rp_consistency.py --strict PASS (2026-01-07 18:53)
slug: relationslog_eisenkonklave_v1
category: admin
status: draft
version: "0.1"
---

Relationslog Eisenkonklave (v1)
===============================

Kontext
-------
- Quelle: `database-raw/99-exports/RAW-canvas-2025-10-16T16-55-00-000Z.txt` (Cluster `eisenkonklave_operativ`).
- Zweck: Nachverfolgung aller diplomatischen Zustände der Eisenkonklave (Novapolis, Händlerbund, Schienenbund, Arkologie).
- Verknüpft mit `cluster_index_v1`, `ai_behavior_index_v2`, `handelslog_eisenkonklave_v1`.

Aktuelle Bewertungen
--------------------
- Novapolis → neutral_wachsam (Konfliktpotenzial 0.47).
- Händlerbund → handel_gelegentlich.
- Schienenbund → feindselig.
- Arkologie → umkämpft.

Arbeitsnotizen
--------------
- Diplomatie-Skalen (0-1) aufnehmen und mit Missionslog-Incidents verlinken.
- Handels-/Relationslog-Trennung dokumentieren (wer pflegt welches Artefakt?).
- Letzte Validierung: offen (siehe TODO in Cluster-Index).
