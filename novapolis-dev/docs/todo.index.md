---
stand: 2026-03-27 15:47
update: Letzter Governance-Folgepunkt geschlossen: Snapshot-/Pre-Commit-Retry-Pfad ist jetzt operativ gehaertet; Index-Metadaten nachgezogen.
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc '.github/copilot-instructions.md' '.github/copilot-instructions-headings.md' 'novapolis-dev/docs/todo.index.md' 'novapolis-dev/docs/todo.dev.md' 'novapolis-dev/docs/donelog.md' 'DONELOG.md' PASS (2026-03-27 15:47); .\.venv\Scripts\python.exe scripts/check_frontmatter.py '.github/copilot-instructions-headings.md' 'novapolis-dev/docs/todo.index.md' 'novapolis-dev/docs/todo.dev.md' 'novapolis-dev/docs/donelog.md' 'DONELOG.md' PASS (2026-03-27 15:47); .\.venv\Scripts\python.exe scripts/check_todo_index_sync.py --repo-root . --write-index-meta PASS (2026-03-27 15:47); .\.venv\Scripts\python.exe scripts/check_logs_policy.py --repo-root . PASS (2026-03-27 15:47)
---

<!-- markdownlint-disable MD022 MD041 -->

TODO-Index (Novapolis-Dev)
==========================

Übersicht
---------

- RP-Module: `docs/todo.rp.md` — Aufgaben, Kanon-/Canvas-Arbeit, Logs (offen: 6)
- Dev-Module: `docs/todo.dev.md` — Tooling, Lint/CI, Validatoren, Doku-Infra (offen: 0)
- Agent-Module: `docs/todo.agent-board.md` — Backend (FastAPI/Ollama), Tests/Typing, Scripts (offen: 0)
- Sim-Module: `docs/todo.sim.md` — Godot/Visualisierung, API-Polling, Exportprofile (offen: 1)

Statushinweise (aktuell)
------------------------

- Index v2.1: Neue Folgepunkte sind jetzt explizit verankert: RP wurde vom Sammelpunkt auf Transferkette/Delta-Struktur/Realabgleich aufgefaechert, Sim fuehrt die bekannten Asset-Warnungen erstmals als aktiven Punkt, Dev den sichtbaren Metadaten-Drift im Index selbst.

- RP v5.18: Der RAW-Rettungsstand vor manueller Verteilung ist jetzt explizit dokumentiert. Hart rettbar bleiben C6-Startsnapshot, D5-Teilanker, generische Transferpfade und einzelne Tagesdeltas; weich rettbar sind Rollen- und Prozesslogik. Aktuelle Fraktionssummen, Restbestaende und konkrete Verbrauchsreihen bleiben weiter Handarbeit.

- RP v5.17: Die C6-Zielseite hat jetzt einen semiformellen Logistikanker: `logistik_novapolis_v2` fuehrt `D5 -> C6 (Bauteile, Werkzeuge, Versorgungsgueter)` als aktive Fracht, `logistik_c6_v2` benennt Primaer-/Sekundaerlager in C6. Definierbar ist damit ein missionierter Versorgungslauf mit bestaetigtem Empfang und Weiterverteilung, nicht aber eine harte Lagerbuchung oder Inventarmenge.

- RP v5.16: C6-Zielseite fuer die Transferkette gegen RAW nachgeschaerft. Bestaetigt sind jetzt nicht nur `Ankunft/Bestandsaufnahme`, sondern auch ein expliziter Empfangsanker plus anschliessende Verteilung an die Baustellen; unbelegt bleiben aber weiter Schleusen-/Lagerbuchung, Charge und Quittungszeile im Inventarlog.

- RP v5.15: D5-Quellorte fuer die Transferkette gegen RAW nachgeschaerft. Bestaetigt sind jetzt ein physischer Quellort `Materiallager unter Bahnsteig` sowie Werkstatt-/Transportmodul-Kontext in D5; unbelegt bleiben aber weiter Entnahmezeile, Zielbuchung in Schleuse/Lagerhalle und Quittung.

- RP v5.14: Transferkette `D5 -> C6` erneut gegen Umfeld und RAW gegengeprueft. Bestaetigt sind jetzt der generische Frachtanker in `logistik_novapolis_v2` sowie der Prozessrahmen `Abmeldung in D5 -> Ankunft/Bestandsaufnahme in C6`; unbelegt bleiben aber weiter Entnahmezeile, Zielbuchung in Schleuse/Lagerhalle und Quittung.

- RP v5.13: Das RP-Board fuehrt jetzt die feste Promotionskette `Charakter -> Team/POI -> Station -> Fraktion -> Metro` sowie die Pflicht-Deltas `Transfer`, `Verbrauch`, `Handel`, `Bilanz`; der offene Backfill ist damit als Gesamtprozess statt als lose Inventarsammlung beschrieben.
- RP v5.10: Transfer- und Verbrauchskette fuer Novapolis gegen RAW, Staging, Logistik und Missionslog geprueft; belastbar sind Bilanz- und Frachtanker, aber nicht die Item-Kette `Entnahme -> Transport -> Ankunft -> Quittung`.
- RP v5.11: Die Guetermission `D5 -> C6` ist jetzt im aktiven Missionslog als Transferanker verankert; fuer harte Fraktionssummen fehlen aber weiter Mengen-, Zielbuchungs- und Quittungszeilen.
- RP v5.12: D5- und C6-Teilinventare fuehren denselben Materiallauf jetzt als lokale Review-Anker; der Gap ist standortscharf dokumentiert, aber weiter nicht quantifiziert.
- RP v5.9: D5-Startsnapshot aus `RAW-canvas-2025-10-16T12-00-00-000Z` nachgezogen; mit C6 liegen jetzt zwei lokale Fruehanker vor, aber noch keine harte Fraktionssumme.
- RP v5.8: C6-Startsnapshot mit exakten Stueckzahlen aus `inventar_c6_v2` und `logistik_c6_v2` nachgezogen; D5 und Fraktionssummen bleiben ohne Gegenbeleg bewusst offen.
- RP v5.7: Skill-Mapping-V1 im Spec um eine zweite Referenzreihe fuer `Pahl`, `Reflex`, `Lumen` und `Echo` erweitert; RP offen bleibt `3`.
- RP v5.6: Skill-Mapping-V1 fuer `reparieren`, `wache`, `funk` und `wahrnehmung` im Spec verankert; RP offen `5 -> 3`.
- RP v5.5: Material-Delta Tag 12->13 fuer Tunnelarbeiten nachgezogen; Verbrauch ist belegt, aber Rest- und Standortmengen bleiben bewusst offen.
- RP v5.4: Energie-Tagesabschluss Tag 12->13 fuer D5/C6/Novapolis aus Staging plus Logistik nachgezogen; absolute Zellstaende bleiben bewusst `tbd`.
- RP v5.3: Erster konservativer Inventar-Abgleich fuer D5/C6/Novapolis abgeschlossen; D5 fuehrt keine C6-Bestaende mehr als lokalen Bestand.
- RP v5.2: Eigentlicher Inventar-Abgleich fuer D5/C6/Novapolis gestartet; erster harter Driftpunkt ist die fruehere Vermischung von C6-Bestaenden im D5-Inventar.
- RP v5.1: Pilotpaket fuer D5/C6/Novapolis-Backfill vorbereitet; RP offen bleibt `5`, aber der Start-Scope ist jetzt konkret dokumentiert.
- Dev v5.9: KPI-Trendansicht fuer die Hygiene-Cadence angelegt; Dev offen `1 -> 0`.
- Dev v5.10: Snapshot-/Retry-Governance gegen den realen Hook-Iststand geschaerft und die betroffenen Python-Tasks von `shell` auf `process` umgestellt; der lokale `pwsh /d /c`-Fehlpfad ist fuer Coverage-, TODO-Index- und Logs-Checks entfernt.
- Dev v5.11: Governance erneut gegen Aktualitaet, Redundanz und operatives Verhalten geprueft. Neu im Board stehen jetzt: Headings-/Quellenstand der Kern-SSOT nachziehen, Regelduplikate in der Kern-Governance reduzieren, verbleibende Python-Tasks auf `process` pruefen und den Snapshot-Retry-Pfad operativ haerten.
- Dev v5.12: Kern-SSOT `.github/copilot-instructions.md` und `.github/copilot-instructions-headings.md` wieder auf denselben aktuellen Quellenstand gezogen; der erste Governance-Folgepunkt ist damit geschlossen (`offen: 4 -> 3`).
- Dev v5.13: Kern-Governance normativ gestrafft. TL;DR verweist nur noch auf Regel-IDs, die `Regel-ID-Landepunkte (Kern)` sind explizit als bindende Ebene markiert, und die Matrix ist jetzt nur noch Kurzreferenz (`offen: 3 -> 2`).
- Dev v5.14: Verbleibende Python-Workspace-Tasks in `.vscode/tasks.json` von `shell` auf `process` vereinheitlicht; bewusste Shell-Ausnahmen bleiben nur fuer `pwsh`-Aufrufe (`offen: 2 -> 1`).
- Dev v5.15: Snapshot-/Pre-Commit-Retry-Pfad operativ gehaertet. Das Snapshot-Gate laeuft in `scripts/pre_commit.py` jetzt erst nach markdownlint, Frontmatter und RP-Hard-Gates; der Dev-Governance-Block ist damit komplett geschlossen (`offen: 1 -> 0`).
- Dev v5.8: O11 geschlossen; externes Standalone-Beta-Installblatt fuer Dritte dokumentiert (`offen: 2 -> 1`).
- Dev v5.7: Community-/Maintainer-Paket umgesetzt (`SUPPORT.md`, `RELEASE.md`, `MAINTAINERS.md`, Root-Issue-/PR-Templates); Dev offen `3 -> 2`.
- Dev v5.6: ADR-Ordner aktiv genutzt; `ADR-0001` und `ADR-0002` als akzeptierte Governance-Entscheidungen aufgenommen (`offen: 4 -> 3`).
- Dev v5.5: Coverage-Sprint Richtung `91%` abgeschlossen und deutlich ueberschritten (`76.24% -> 93.69%`, `offen: 5 -> 4`).
- Dev v5.3: Coverage-Punkt 3 gestartet; 90%-Qualitaetsziel jetzt verbindlich in Dev-Tests/Abschlussprozess verankert.
- Dev v5.4: Punkt 1 (Full-Gate) geschlossen; Coverage-Welle 1 Richtung `91%` gestartet (`76.24% -> 80.45%`).
- Dev v5.2: Folgezyklus fuer Gate-Stabilisierung und modernes Doku-Basispaket gestartet (`offen: 0 -> 5`).
- Dev v5.1: Woechentliche Hygiene-Cadence mit KPI-Tracking verbindlich dokumentiert (`offen: 1 -> 0`).
- Sim v5.0: Sim-Board konsolidiert, verbleibende Mikrodrift geschlossen (`offen: 1 -> 0`).
- Index v2.0: Operative Anzeige erweitert um Board-Metadaten (letzte Aenderung, aeltester offener Punkt, Widerspruchscheck).

Board-Metadaten (automationsrelevant)
-------------------------------------

| Board | letzte Aenderung | aeltester offener Punkt | Widerspruch "keine offenen" |
| --- | --- | --- | --- |
| Dev (`docs/todo.dev.md`) | 2026-03-27 | keiner (offen: 0) | nein |
| RP (`docs/todo.rp.md`) | 2026-03-27 | - [ ] [Als naechstes] Danach erst Mengen-Backfill in Inventaren (D5/C6/Fraktionen) starten. | nein |
| Agent (`docs/todo.agent-board.md`) | 2026-03-27 | keiner (offen: 0) | nein |
| Sim (`docs/todo.sim.md`) | 2026-03-27 | - [ ] [Als naechstes] Sim-Asset-Warnungen aus `scripts/check_sim_epoch_assets.py` aufloesen oder bewusst kanonisch ausnehmen. | nein |


Hinweise (Index)
----------------

- Vollständig erledigte Abschnitte (H2/H3, alle [x]) bitte manuell in `novapolis-dev/archive/todo.<modul>.archive.md` verschieben; unter der Abschnittsüberschrift `archived_at: YYYY-MM-DD HH:MM` ergänzen. Übersicht aller Archive: `novapolis-dev/archive/README.md`.
- Validierung bei Änderungen: markdownlint via `npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc` und Frontmatter-Check via `scripts/check_frontmatter.py`.
- Automationscheck: `scripts/check_todo_index_sync.py` liefert zusaetzlich Metadaten zu letzter Board-Aenderung, aeltestem offenen Punkt und Widerspruchen.

Verweise
--------

- Root-Übersicht: `todo.root.md` (Kurzüberblick, Meta-Aufgaben, Links)
- DONELOG-Zentralstruktur: `novapolis-dev/archive/docs/donelogs/INDEX.md`





