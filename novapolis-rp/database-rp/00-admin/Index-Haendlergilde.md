---
stand: 2026-01-11 05:18
update: Handel/Diplomatie-Hub verlinkt.
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-rp/database-rp/**/*.md' PASS (2026-01-11 05:18); & .\.venv\Scripts\python.exe scripts\check_frontmatter.py --touch novapolis-rp\database-rp\00-admin\Index-Handel-Diplomatie.md novapolis-rp\database-rp\00-admin\Handel-Diplomatie-Haendlergilde.md novapolis-rp\database-rp\00-admin\Relationslog-Novapolis.md novapolis-rp\database-rp\00-admin\Index-Haendlergilde.md DONELOG.md PASS (2026-01-11 05:18); & .\.venv\Scripts\python.exe scripts\checks_rp_consistency.py --strict PASS (2026-01-11 05:18)
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
- Synchronisiert mit `caravan_moves.md`, `database-rp/01-factions/haendlerbund/06-handel-diplomatie/Handel-Diplomatie-Haendlergilde.md`, `person_index_np.md`.
- Hub/Übersicht (Handel/Diplomatie): `database-rp/00-admin/Index-Handel-Diplomatie.md`
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
