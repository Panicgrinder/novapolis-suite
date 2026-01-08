---
stand: 2026-01-07 18:47
update: Fraktionsnamen (Anzeige) aktualisiert (Händlerbund/Schienenbund).
checks: markdownlint-cli2 PASS; scripts/check_frontmatter.py PASS; scripts/checks_rp_consistency.py --strict PASS (2026-01-07 18:53)
slug: eisenkonklave
category: faction
status: draft
version: "0.1"
---

Eisenkonklave (Fraktion)
========================

Überblick
---------
- Führungsfigur: [Varek Solun](../02-characters/Varek-Solun.md) (Kommandant).
- Primärer Standort: H12 / Sektor_H3 (siehe Cluster-Index).
- Ziele: Zugriff auf Union-Archive, Sicherung eigener Module, Kontrolle der Tunnel.

Diplomatie & Beziehungen
------------------------
- Novapolis: neutral_wachsam → laufende Gespräche über Zugang zu Ressourcen.
- Händlerbund: wechselhaft → einzelne Handelsfenster via `caravan_moves`.
- Schienenbund: feindselig → Konflikt um Tunnelkontrolle.

Systemverknüpfungen
-------------------
- `relationslog_eisenkonklave_v1`
- `ai_behavior_index_v2`
- `cluster_index_v1`
- `handelslog_eisenkonklave_v1` (Pending-Dokument)

ToDo
----
- Missions-/Inventarverknüpfungen ergänzen (z. B. benötigte Module, Sicherheitsauflagen).
- Diplomatieereignisse in `Missionslog` spiegeln.
- Rollenliste erweitern (Second-in-Command, Kontakte zum Händlerbund).
