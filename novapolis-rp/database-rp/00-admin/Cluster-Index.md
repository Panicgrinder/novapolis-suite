---
stand: 2025-11-27 03:25
update: Stub angelegt; cluster_index_v1 für Lexikon registriert
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc '**/*.md' PASS (2025-11-27 03:20)
slug: cluster_index_v1
title: Cluster-Index v1
category: admin
status: draft
version: "0.1"
---

Cluster-Index (v1)
==================

Zweck
-----
- Referenz für Fraktions- und Cluster-Signaturen (Eisenkonklave, Arkologie, Händlergilde, Schattenbund).
- Liefert die Diplomatie-/Prioritätswerte aus `database-raw/99-exports/RAW-canvas-2025-10-16T16-55-00-000Z.txt`.
- Ergänzt `AI-Behavior-Mapping.md` um Cluster-spezifische Kontextdaten (z. B. Konfliktpotenziale, Führungen, aktive Systeme).

Aktueller Stand
---------------
- Cluster `eisenkonklave_operativ`: Priorität mittel, Systeme `relationslog_eisenkonklave_v1`, `handelslog_eisenkonklave_v1`.
- Cluster `arkologie_a1`: Priorität mittel, Systeme `relationslog_arkologie_v1`.
- Cluster `schattenbund_feld`: Priorität mittel, Systeme `relationslog_schattenbund_v1`.
- Cluster `haendlergilde_extern`: Priorität niedrig, Systeme `relationslog_haendlergilde_v1`, `handelslog_haendlergilde_v1`.

ToDo
----
- Detailaufschlüsselung pro Cluster (Mitglieder, Orte, Diplomatie) in Tabellenform übernehmen.
- Schnittstellen zu Missionslog/Logistik referenzieren.
- Versionierung aus dem RAW-Canvas übernehmen und Validierungsintervall ergänzen.
