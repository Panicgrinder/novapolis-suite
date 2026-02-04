---
stand: 2026-02-04 09:08
update: Index-Links auf relative Pfade umgestellt.
checks: "npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc '**/*.md' PASS (2026-02-04 09:08)"
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
- Synchronisiert mit [caravan_moves](../05-projects/caravan_moves.md), [Handel-Diplomatie-Haendlergilde](./Handel-Diplomatie-Haendlergilde.md), [Personenindex Novapolis](../../novapolis/02-characters/person-index-np.md).
- Hub/Übersicht (Handel/Diplomatie): [Index-Handel-Diplomatie](../../../00-admin/Index-Handel-Diplomatie.md)
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
