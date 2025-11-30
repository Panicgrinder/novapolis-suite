---
stand: 2025-11-27 03:25
update: Stub angelegt; relationslog_eisenkonklave_v1 dokumentiert
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc '**/*.md' PASS (2025-11-27 03:20)
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
- Zweck: Nachverfolgung aller diplomatischen Zustände der Eisenkonklave (Novapolis, Händlergilde, Schattenbund, Arkologie).
- Verknüpft mit `cluster_index_v1`, `ai_behavior_index_v2`, `handelslog_eisenkonklave_v1`.

Aktuelle Bewertungen
--------------------
- Novapolis → neutral_wachsam (Konfliktpotenzial 0.47).
- Händlergilde → handel_gelegentlich.
- Schattenbund → feindselig.
- Arkologie → umkämpft.

Arbeitsnotizen
--------------
- Diplomatie-Skalen (0-1) aufnehmen und mit Missionslog-Incidents verlinken.
- Handels-/Relationslog-Trennung dokumentieren (wer pflegt welches Artefakt?).
- Letzte Validierung: offen (siehe TODO in Cluster-Index).
