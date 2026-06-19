---
stand: 2026-06-19 15:17
update: Der TODO-Index fuehrt den Dev-Plan jetzt mit abgeschlossenen Phasen 0/1/2/3 konsistent bei offen: 0 und behaelt die technische Enforcement-Integration weiterhin offen. Phase 4 (Read-only-Audit der VS-Code-Settings) abgeschlossen: kein Drift; keine Settings-Mutation erforderlich. Root-Kurzstatus ist im selben Lauf auf `RP=1` synchronisiert.
checks: snapshot-lock PASS (2026-06-14 01:54); npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc novapolis-dev/docs/todo.index.md PASS; .\.venv\Scripts\python.exe scripts\check_frontmatter.py novapolis-dev/docs/todo.index.md PASS (EXITCODE=0); .\.venv\Scripts\python.exe scripts\check_todo_index_sync.py --repo-root . PASS

---

<!-- markdownlint-disable MD022 MD041 -->

TODO-Index (Novapolis-Dev)
==========================

Übersicht
---------

- RP-Module: `docs/todo.rp.md` — Aufgaben, Kanon-/Canvas-Arbeit, Logs (offen: 2)
- Dev-Module: `docs/todo.dev.md` — Tooling, Lint/CI, Validatoren, Doku-Infra (offen: 4)
- Agent-Module: `docs/todo.agent-board.md` — Backend (FastAPI/Ollama), Tests/Typing, Scripts (offen: 1)
- Sim-Module: `docs/todo.sim.md` — Godot/Visualisierung, API-Polling, Exportprofile (offen: 1)
- Root-Backlog: `todo.root.md` — suiteweiter Querschnitts-Backlog und Meta-Aufgaben (nicht Teil der Modul-Open-Counts oben)

Statushinweise (aktuell)
------------------------

- Root/Meta: `todo.root.md` fuehrt jetzt drei offene Querschnittspunkte (GOV-STRANG-01 bis GOV-STRANG-03) fuer den beschlossenen Governance-Umbau und bleibt bewusst ausserhalb der Modul-Open-Counts.

- Dev: `novapolis-dev/docs/todo.dev.md` fuehrt jetzt vier offene Governance-Umbaupunkte (GOV-STRANG-04 bis GOV-STRANG-07) als aktive Umsetzungsarbeit fuer technische Projektion, Hook-Evidenz, Freshness-Harmonisierung und Mini-Lamas-Vertragskonsolidierung.

- Agent: `novapolis-dev/docs/todo.agent-board.md` fuehrt jetzt einen offenen Governance-Umbaupunkt (GOV-STRANG-08) fuer die operative Agent-Runtime-Projektion inklusive mini-first/Handoff/Gate-Nachweis.

- RP: `novapolis-dev/docs/todo.rp.md` fuehrt jetzt zwei offene Punkte: den laufenden Nordlinie-Fachpunkt plus den Governance-Umbaupunkt GOV-STRANG-09 fuer die RP-SSOT-to-Runtime-Projektion.

- Sim: `novapolis-dev/docs/todo.sim.md` fuehrt jetzt einen offenen Governance-Umbaupunkt (GOV-STRANG-02) als Sim-Bruecke in die Root-/Dev-Planlandschaft.

- Historische Zwischenstaende und offene Uebergangsphasen bleiben im Dev-DONELOG dokumentiert; der TODO-Index fuehrt absichtlich nur noch den aktuellen Board- und Gate-Stand.

Board-Metadaten (automationsrelevant)
-------------------------------------

| Board | letzte Aenderung | aeltester offener Punkt | Widerspruch "keine offenen" |
| --- | --- | --- | --- |
| Dev (`docs/todo.dev.md`) | 2026-06-19 | - [ ] [Jetzt] GOV-STRANG-04: Phase-5-Verifikation vom Vertragsstand auf technische Runtime-Projektion heben. | nein |
| RP (`docs/todo.rp.md`) | 2026-06-19 | - [ ] [Jetzt] Nordlinie-Folgepaket in drei Zuegen schliessen und Reflex-Herkunft gegen Datenrettung pruefen. | nein |
| Agent (`docs/todo.agent-board.md`) | 2026-06-19 | - [ ] [Als naechstes] GOV-STRANG-08: Agent-Runtime-Projektion fuer den Governance-Umbau als belegten Umsetzungsstrang fuehren. | nein |
| Sim (`docs/todo.sim.md`) | 2026-06-19 | - [ ] [Als naechstes] GOV-STRANG-02: Sim-Governance-Bruecke fuer den Umbau als explizite Planarbeit fuehren. | nein |


Hinweise (Index)
----------------

- Aktive TODO-Quellen sind `todo.root.md` plus die vier Modul-Boards in `novapolis-dev/docs/`; gleichnamige Dateien unter `novapolis-dev/archive/**` oder `novapolis-dev/archive/quarantine/**` sind Historie, Snapshots oder Arbeitsquarantäne.
- Detaillierte Zwischenhistorie und Board-Uebergangsphasen bleiben in `novapolis-dev/docs/donelog.md`; dieser Index spiegelt nur den aktuellen Board- und Gate-Stand.
- Vollständig erledigte Abschnitte (H2/H3, alle [x]) bitte manuell in `novapolis-dev/archive/todo.<modul>.archive.md` verschieben; unter der Abschnittsüberschrift `archived_at: YYYY-MM-DD HH:MM` ergänzen. Übersicht aller Archive: `novapolis-dev/archive/README.md`.
- Validierung bei Änderungen: markdownlint via `npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc` und Frontmatter-Check via `scripts/check_frontmatter.py`.
- Automationscheck: `scripts/check_todo_index_sync.py` liefert zusaetzlich Metadaten zu letzter Board-Aenderung, aeltestem offenen Punkt und Widerspruchen.

Verweise
--------

- Root-Übersicht: `todo.root.md` (Kurzüberblick, Meta-Aufgaben, Links)
- DONELOG-Zentralstruktur: `novapolis-dev/archive/docs/donelogs/INDEX.md`





