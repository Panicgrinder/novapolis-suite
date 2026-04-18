---
stand: 2026-04-18 03:00
update: Der TODO-Index fuehrt fuer Dev nach dem Doku-Sync-Helfer keine offenen Punkte mehr; RP, Agent und Sim bleiben weiter bei je fuenf offenen Folgepunkten, Root bleibt als leere Live-Oberflaeche vorbereitet.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp/results/reports/checks_report_20260417_071110.md; snapshot-lock PASS (2026-04-18 03:00)
---

<!-- markdownlint-disable MD022 MD041 -->

TODO-Index (Novapolis-Dev)
==========================

Übersicht
---------

- RP-Module: `docs/todo.rp.md` — Aufgaben, Kanon-/Canvas-Arbeit, Logs (offen: 5)
- Dev-Module: `docs/todo.dev.md` — Tooling, Lint/CI, Validatoren, Doku-Infra (offen: 0)
- Agent-Module: `docs/todo.agent-board.md` — Backend (FastAPI/Ollama), Tests/Typing, Scripts (offen: 5)
- Sim-Module: `docs/todo.sim.md` — Godot/Visualisierung, API-Polling, Exportprofile (offen: 5)
- Root-Backlog: `todo.root.md` — suiteweiter Querschnitts-Backlog und Meta-Aufgaben (nicht Teil der Modul-Open-Counts oben)

Statushinweise (aktuell)
------------------------

- Root/Meta: `todo.root.md` ist nach der Archivierung des abgeschlossenen April-Blocks wieder als schlanke Live-Oberflaeche vorbereitet und fuehrt aktuell keine offenen suiteweiten Querschnittspunkte. Der zuletzt abgeschlossene Root-Block liegt unter `novapolis-dev/archive/todo.root.archive.md`; der naechste Hygiene-Takt fuer KPI-/Boardpflege bleibt ueber `novapolis-dev/docs/process/abschluss-routine.ssot.md` und die aktuellen Root-Protokolle verankert, waehrend Root bewusst ausserhalb der Modul-Open-Counts bleibt.

- Dev: `novapolis-dev/docs/todo.dev.md` fuehrt nach dem geschlossenen Doku-Sync-Helfer aktuell keine offenen Steuerpunkte mehr. Der neue Helfer `scripts/sync_docs_after_checks.py` zieht nach belegten Gruenlaeufen Snapshot-Lock, Frontmatter und TODO-Index fuer geaenderte Root-/Dev-Dokus nach; die zuvor geschlossene Reader-/Surface-Welle bleibt weiter zusaetzlich unter `novapolis-dev/archive/todo.dev.archive.md` archiviert.

- Agent: `novapolis-dev/docs/todo.agent-board.md` fuehrt jetzt fuenf neue Punkte fuer Coverage-Reste, Referenzpfad-Haertung und `gm_session`-Runtime-Diagnostik; der zuletzt geschlossene Handover-Block bleibt zusaetzlich unter `novapolis-dev/archive/todo.agent.archive.md` archiviert.

- RP: `novapolis-dev/docs/todo.rp.md` fuehrt jetzt fuenf neue Punkte fuer `slot 41-45` und die warenbezogene Evidenzkette von D5/C6 bis Metro-Ebene; der zuletzt geschlossene Folgepfad `slot 36-40` bleibt zusaetzlich unter `novapolis-dev/archive/todo.rp.archive.md` archiviert.

- Sim: `novapolis-dev/docs/todo.sim.md` fuehrt jetzt fuenf neue Punkte fuer Architekturrest, Exportpfad, Export-Smoke, Offline-Vollstand und Persistenzhaertung; der zuletzt geschlossene Sim-Abschlussschnitt bleibt zusaetzlich unter `novapolis-dev/archive/todo.sim.archive.md` archiviert.

- Historische Zwischenstaende und offene Uebergangsphasen bleiben im Dev-DONELOG dokumentiert; der TODO-Index fuehrt absichtlich nur noch den aktuellen Board- und Gate-Stand.

Board-Metadaten (automationsrelevant)
-------------------------------------

| Board | letzte Aenderung | aeltester offener Punkt | Widerspruch "keine offenen" |
| --- | --- | --- | --- |
| Dev (`docs/todo.dev.md`) | 2026-04-17 | keiner (offen: 0) | nein |
| RP (`docs/todo.rp.md`) | 2026-04-17 | - [ ] [Jetzt] Den Folgekorridor hinter `slot 40` als `slot 41-45` unter demselben Slice-2-Handover-Vertrag ausarbeiten. | nein |
| Agent (`docs/todo.agent-board.md`) | 2026-04-17 | - [ ] [Jetzt] `novapolis_agent/scripts/support_ab_smoke.py` vom aktuellen Reststand auf belastbare Produkt- und Testabdeckung ziehen. | nein |
| Sim (`docs/todo.sim.md`) | 2026-04-17 | - [ ] [Jetzt] Den verbliebenen Agent-Studio-/Form-State-Rest aus `Main.gd` in denselben Controller-Schnitt ziehen wie die uebrigen Hub-Pfade. | nein |


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





