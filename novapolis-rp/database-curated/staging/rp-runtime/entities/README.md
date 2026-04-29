---
stand: 2026-04-29 03:56
update: Character-Dossiers bleiben aktiv unter `characters/<slug>/`; der alte Runtime-Typordner `../characters/` ist archiviert.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260429_035444.md
---

Runtime Entities
================

Zweck
-----

Dieser Ordner ist die aktive entitaetszentrierte Runtime-Struktur fuer RP im Chat.

- `sessions/` bleibt top-level fuer Szenenlog und Rohspur.
- Entitaetsbezogene Arbeitsdaten liegen unter `entities/<type>/<slug>/`.
- Dossiers enthalten nur belegte Arbeitsflaechen; keine Datei wird nur zur Vollstaendigkeit erfunden.
- Nichts in diesem Ordner ist automatisch RP-SSOT oder Kanon-Promotion.

Namespaces
----------

- `characters/<slug>/` fuer Figuren und handlungsfaehige Einzelentitaeten
- `locations/<slug>/` fuer Orte, Stationen und lokale Roster
- `projects/<slug>/` fuer Projekt- oder Reparaturachsen
- `assets/<slug>/` fuer technische oder materielle Laufzeittraeger
- `factions/<slug>/` fuer aktive Fraktionsoberflaechen

Dossier-Kontrakt
----------------

- `entity.md`: Figuren- oder Entitaetsarbeitsblatt
- `mind.md`: Mind-/Sphaeren-Arbeitsstand und Delta-Kandidaten
- `relationships.md`: gerichtete Beziehungseintraege aus Sicht dieser Entitaet (`observer_id -> target_id`)
- `inventory.md`: Bestand, Transfer, Verbrauch oder Materialbedarf
- `state.md`: Orts-, Projekt-, Fraktions- oder Weltzustand
- `roster.md`: Gruppen-, Bewohner- oder Schichtoberflaeche ohne freie Individualisierung aller Mitglieder

Action Guard
------------

- Vor individuellen Aktionen werden das handelnde Dossier und die relevanten Ziel-Dossiers gemeinsam gelesen.
- Nach der Aktion werden betroffene Dossierdateien im selben Lauf aktualisiert oder bewusst mit `keine neue Mind-Delta`, `keine neue Relationship-Delta` oder `carry_forward_confirmed` stabil gehalten.
- Beziehungen sind keine Einzelkanten-Dateien als Standard; sie stehen in `relationships.md` des jeweiligen Observers.

Legacy-Hinweis
--------------

Die frueheren Typordner `mind/`, `inventories/`, `state/` und `relationships/` enthalten nur noch Redirect- und Migrationshinweise. Der fruehere Typordner `../characters/` ist nach Redirect-Zielpruefung unter `novapolis-dev/archive/quarantine/rp-runtime-characters-legacy-20260429-0229/characters/` archiviert. Aktive Character-Daten liegen in `characters/<slug>/`.
