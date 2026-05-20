---
stand: 2026-05-20 17:42
update: Der TODO-Index spiegelt den ausgespielten Reflex-Wahrnehmungszug aus Turn 15; offen bleibt 1.
checks: snapshot-lock PASS (2026-05-20 17:42); npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc '**/*.md' PASS (2026-05-20 17:42); .\.venv\Scripts\python.exe scripts\check_frontmatter.py changed-md PASS (EXITCODE=0, 2026-05-20 17:42); .\.venv\Scripts\python.exe scripts\check_todo_index_sync.py PASS (2026-05-20 17:42); npm --prefix novapolis-rp/coding/tools/validators run validate:rp PASS (2026-05-20 17:42); git diff --check PASS (CRLF warnings only, 2026-05-20 17:42).
---

<!-- markdownlint-disable MD022 MD041 -->

TODO-Index (Novapolis-Dev)
==========================

Übersicht
---------

- RP-Module: `docs/todo.rp.md` — Aufgaben, Kanon-/Canvas-Arbeit, Logs (offen: 1)
- Dev-Module: `docs/todo.dev.md` — Tooling, Lint/CI, Validatoren, Doku-Infra (offen: 0)
- Agent-Module: `docs/todo.agent-board.md` — Backend (FastAPI/Ollama), Tests/Typing, Scripts (offen: 0)
- Sim-Module: `docs/todo.sim.md` — Godot/Visualisierung, API-Polling, Exportprofile (offen: 0)
- Root-Backlog: `todo.root.md` — suiteweiter Querschnitts-Backlog und Meta-Aufgaben (nicht Teil der Modul-Open-Counts oben)

Statushinweise (aktuell)
------------------------

- Root/Meta: `todo.root.md` bleibt die schlanke Live-Oberflaeche ohne offene suiteweite Querschnittspunkte. Der Wochenabschluss 2026-05-18 ist gruen belegt: `.tmp\results\reports\checks_report_20260518_222833.md` ist PASS, `Checks: sim epoch assets` bleibt PASS (`summary=fail:0,warn:0`), `Tests: coverage (fail-under)` bleibt bei `92.19%` und `709 passed`, und Root bleibt bewusst ausserhalb der Modul-Open-Counts. Der initiale Vollcheck `.tmp\results\reports\checks_report_20260518_222210.md` fiel nur an Freshness-/Tree-Drift und ist im selben Lauf geschlossen.

- Dev: `novapolis-dev/docs/todo.dev.md` fuehrt aktuell wieder keine offenen Punkte mehr. Der Vierer-Split ist jetzt klar gezogen: `workspace_tree.txt`, `workspace_tree_dirs.txt` und `workspace_tree_full.txt` bleiben die überwachten kanonischen Trees, waehrend `workspace_tree_local.txt` den echten lokalen On-Disk-Zustand getrennt davon abbildet.

- Agent: `novapolis-dev/docs/todo.agent-board.md` fuehrt weiter keine offenen Punkte. Der Wochenabschlusslauf hat hier nur den Freshness-Stand nachgezogen; inhaltlich bleibt der gemeinsame Release-Gate-Pfad `novapolis_agent/scripts/training_release_gate.py` unveraendert der harte Vorlauf vor `export+pack` und LoRA.

- RP: `novapolis-dev/docs/todo.rp.md` fuehrt weiter genau einen offenen Punkt. Zug A des aktiven Folgekorridors fuer `d5-c6-nordlinie-sanierung-01` ist mit Turn 14 und Turn 15 belegt: Die Ronja/Reflex-Geste ist als bestaetigendes Naehesignal dokumentiert, und Reflex' Wahrnehmung bleibt unter D5-/C6-Weltendruck kantig, ohne Kokon, Kontrolle, technische Freigabe oder neue Symbiose-Stufe. Als Einschub sind der SSOT-Schnitt gegen unbelegte formale Stop-/Freigabe-/Request-Kommandos sowie die freigegebene Reflex-Profilkante dokumentiert: Bindungs-/Regulationslesart glaettet Reflex nicht; Weltendruck und `CRISIS`-Kokon/Vollschutz bleiben Teil seiner Wahrnehmungs- und Schutzlogik. Offen bleiben Zug B zur konservativen Draisine-Entscheidung mit `Jonas/Pahl/Lumen`, Zug C zu Koras/Echos Schuttkeil-Rueckmeldung sowie das Herkunftsaudit fuer Reflex, weil aktive SSOT aktuell nur `D5-Reaktor-Stabilisierung` fuehrt, waehrend die Datenrettung noch Drift wie `Jonas' Werkstatt (Geburtsort Reflex)` traegt.

- Sim: `novapolis-dev/docs/todo.sim.md` fuehrt aktuell keine offenen Punkte mehr. `scripts/run_sim_headless_verify.py` loest im aktuellen Windows-Kontext jetzt auch den Pfad eines laufenden lokalen Godot-Prozesses auf; `Checks: sim headless verify` endet damit wieder mit `SIM_VERIFY: OK` statt am frueheren Exit `2`.

- Historische Zwischenstaende und offene Uebergangsphasen bleiben im Dev-DONELOG dokumentiert; der TODO-Index fuehrt absichtlich nur noch den aktuellen Board- und Gate-Stand.

Board-Metadaten (automationsrelevant)
-------------------------------------

| Board | letzte Aenderung | aeltester offener Punkt | Widerspruch "keine offenen" |
| --- | --- | --- | --- |
| Dev (`docs/todo.dev.md`) | 2026-04-28 | keiner (offen: 0) | nein |
| RP (`docs/todo.rp.md`) | 2026-05-20 | Nordlinie-Folgepaket in drei Zuegen schliessen und Reflex-Herkunft gegen Datenrettung pruefen (offen: 1) | nein |
| Agent (`docs/todo.agent-board.md`) | 2026-05-11 | keiner (offen: 0) | nein |
| Sim (`docs/todo.sim.md`) | 2026-04-26 | keiner (offen: 0) | nein |


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





