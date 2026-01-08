---
stand: 2026-01-07 18:47
update: Anzeige-Name: Händlerbund (IDs/Slugs unverändert).
checks: markdownlint-cli2 PASS; scripts/check_frontmatter.py PASS; scripts/checks_rp_consistency.py --strict PASS (2026-01-07 18:53)
slug: index_haendlergilde_v1
category: admin
status: draft
version: "0.1"
---

Index Händlerbund (Händlergilde-ID, v1)
======================================

Beschreibung
------------
- Akteurs- und Strukturverzeichnis des Händlerbunds (Führung, Komitees, mobile Einheiten).
- Synchronisiert mit `caravan_moves.md`, `Handel-Diplomatie-Haendlergilde.md`, `person_index_np.md`.
- Herkunft: RAW-Cluster `haendlergilde_extern` (16.10.2025 16:55Z).

Geplanter Inhalt
----------------
- Abschnitt Personen (Arlen, Marven, Unterstützer:innen) mit Rollen/Signals.
- Abschnitt Systeme (Konvoi-Tracker, Diplomatie-Board, Handelslogbuch).
- Abschnitt Abhängigkeiten (Energie, Schutzteams, Novapolis-Eintrittspunkte).

ToDo
----
- Tabellenstruktur übernehmen, `dependencies`-Feld für relevante Canvas setzen.
- Validierungszyklus definieren (z. B. pro Missionseintrag im `Missionslog`).
