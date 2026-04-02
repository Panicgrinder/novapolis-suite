---
stand: 2026-04-02 06:27
update: Der RP-Realabgleich fuer Skill-Mapping-V1 ist dokumentiert; der RP-Open-Count sinkt auf 2.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260402_062604.md
---

<!-- markdownlint-disable MD022 MD041 -->

TODO-Index (Novapolis-Dev)
==========================

Übersicht
---------

- RP-Module: `docs/todo.rp.md` — Aufgaben, Kanon-/Canvas-Arbeit, Logs (offen: 2)
- Dev-Module: `docs/todo.dev.md` — Tooling, Lint/CI, Validatoren, Doku-Infra (offen: 0)
- Agent-Module: `docs/todo.agent-board.md` — Backend (FastAPI/Ollama), Tests/Typing, Scripts (offen: 0)
- Sim-Module: `docs/todo.sim.md` — Godot/Visualisierung, API-Polling, Exportprofile (offen: 2)
- Root-Backlog: `todo.root.md` — suiteweiter Querschnitts-Backlog und Meta-Aufgaben (nicht Teil der Modul-Open-Counts oben)

Statushinweise (aktuell)
------------------------

- Root v1.2: Der letzte aktive Root-eval-Rest ist final geschlossen. Lokale Kontext-Notizen-Defaults, Eval-Standardpfade und die RAG-Fallbacks laufen jetzt ueber `novapolis_agent/eval/...`; der ehemalige Root-Ordner `eval/` liegt nachvollziehbar unter `novapolis-dev/archive/quarantine/root-cleanup-20260328_0501-root-eval-rest/eval`, ein nach den Abschluss-Checks erneut erzeugter lokaler Stub wurde zusaetzlich unter `novapolis-dev/archive/quarantine/root-cleanup-20260328_0632-root-eval-rest-postchecks/eval` abgelegt, und die Tree-Artefakte wurden danach erneut neu erzeugt (`offen: unveraendert`).

- Dev v5.21: Der aktive Stub-/Runbook-/Tool-Scope fuehrt jetzt unterscheidbare Dateinamen statt austauschbarer Unterordner-READMEs. Umbenannt wurden u. a. `docs/adr/adr-index.md`, `novapolis_agent/scripts/scripts-overview.md`, `novapolis_agent/eval/eval-overview.md`, `novapolis-dev/logs/logs-policy.md`, `novapolis-rp/coding/tools/validators/validator-suite.md` und `novapolis-rp/database-raw/99-exports/raw-export-policy.md`; aktive Querverweise sind im selben Lauf nachgezogen. Bewusst unveraendert blieben die kanonischen Root-/Modul-Einstiege sowie fachliche RP-Landingpages unter `novapolis-rp/database-rp/01-factions/**` (`offen: 1 -> 0`).

- Agent v5.3: Der historische Null-Export-Drift im Export-/Kurationspfad ist geschlossen. `export_finetune.py` liefert jetzt laute Diagnostik statt stiller `0`-Exports, `curate_dataset_from_latest.py` nimmt das neueste exportierbare Resultset statt blind des neuesten Dateinamens, und ein temp-basierter Real-Lauf erzeugte fuer `results_20260226_0306_quality_de_round7b_repeat3.jsonl` wieder `20` Export-Eintraege plus Pack-Split `18/2` (`offen: 1 -> 0`).

- Agent v5.2: Der Artefakt-Cleanup gruppiert Retention jetzt auf Run-/Artefaktgruppen-Ebene statt pro Datei. `outputs/` bleibt im Dry-Run als ganze Laufgruppen zusammen, und fuer `novapolis_agent/eval/results` werden nur noch ganze Cluster statt gemischter Dateireste markiert; als einziger offener Agent-Punkt bleibt damit wieder der Export-/Kurationspfad gegen historische Results-Drift (`offen: 1 -> 1`).

- Agent v5.1: Die Kontext-Notizen-Migration ist abgeschlossen. `CONTEXT_NOTES_PATHS`, `open_context_notes.py`, `README.md` und die Eval-/RAG-Defaults fuehren jetzt konsistent auf `novapolis_agent/eval/...`, womit das Agent-Board wieder nur den historischen Export-/Kurationspfad offen fuehrt (`offen: 2 -> 1`).

- Root v1.1: Der zweite kleine Root-Cleanup ist abgeschlossen. `extensions.installed.txt`, `extensions.status.txt` und `desktop.ini` liegen jetzt gesammelt unter `novapolis-dev/archive/quarantine/root-cleanup-20260328_0330-local-snapshots/`; die Root-Tree-Artefakte wurden direkt per Terminal regeneriert, weil die vorhandenen Shell-Tasks lokal weiter am bekannten `pwsh /d /c`-Fehlpfad scheitern (`offen: unveraendert`).

- Root v1.0: Der sichere Root-Cleanup ist vollzogen. `combined.json`, `lint.out`, `md003_scan.out`, `.tmp-datasets/` und `reports/` liegen jetzt gesammelt unter `novapolis-dev/archive/quarantine/root-cleanup-20260328_0238/`; aktive Shims und der noch referenzierte Hinweis `eval/config/context.local.md` blieben bewusst im Root-Scope (`offen: unveraendert`).

- Dev v5.20: Der dokumentierte Stil- und Konsistenzlauf ist abgeschlossen. Hochfrequenz-Dateien, aktive Dev-SSOTs und die ersten Modul-Runbooks fuehren jetzt denselben PASS-/PowerShell-/Root-Wrapper-Stil; im aktiven Scope blieben beim Restscan nur ignorierte Drittanbieter-READMEs unter `node_modules` ausserhalb des Arbeitsbereichs uebrig (`offen: 1 -> 0`).

- Dev v5.19: Der naechste Doku-Hygienelauf ist vor seinem Start als eigener Phasenplan dokumentiert. Hochfrequenz-Dateien gehen zuerst, danach aktive Dev- und Modul-Doku; Archive und Quarantaene bleiben bewusst ausserhalb des Sweep-Scope (`offen: 0 -> 1`).

- Index v2.2: `todo.root.md` steht jetzt explizit in der Uebersicht; weitere `todo*.md` unter `novapolis-dev/archive/**` und `novapolis-dev/archive/quarantine/**` bleiben historische bzw. quarantänisierte Nebenpfade und zaehlen nicht zum aktiven Backlog.

- Index v2.1: Neue Folgepunkte sind jetzt explizit verankert: RP wurde vom Sammelpunkt auf Transferkette/Delta-Struktur/Realabgleich aufgefaechert, Sim fuehrt die bekannten Asset-Warnungen erstmals als aktiven Punkt, Dev den sichtbaren Metadaten-Drift im Index selbst.

- RP v5.29: Skill-Mapping-V1 ist jetzt gegen reale RP-Pfade dokumentiert. `annotation-spec.md` fuehrt den Realabgleich fuer `Ronja/Reflex` im Materiallauf `D5 -> C6`, fuer `Pahl` als faktisches D5-Kommando und fuer `Kora/Echo` im C6-Schutz-/Logistikkontext; die Baselines bleiben konservativ, nur fuer `Pahl` ist ein szenengebundener Kontext-Lift `funk/wache +1` statt eines Rollenwechsels festgehalten (`offen: 3 -> 2`).

- RP v5.27: Der Schattenbund fuehrt jetzt erstmals einen belegten Relations- und Beschaffungsrahmen statt nur T0-Abschirmhuelle. `Relationslog-Schattenbund.md`, `Handelslog-Schattenbund.md`, `Missionslog-Schattenbund.md` und `Schattenbund-inventar.md` dokumentieren nun den konservativen Rahmen `Novapolis = unbekannt`, `Eisenkonklave = feindselig`, `Arkologie = verdeckt` samt verdeckter Kette `Jarek Voan -> Sera Nol -> Nyra Vehl`; Mengen, Routen und benannte Gegenparteien bleiben bewusst offen (`offen: 3 -> 3`).

- RP v5.28: Das Fluesterkollektiv fuehrt jetzt erstmals einen belegten Minimalrahmen jenseits der reinen T0-Huelle. `Relationslog-Fluesterkollektiv.md`, `Handelslog-Fluesterkollektiv.md`, `Missionslog-Fluesterkollektiv.md` und `Fluesterkollektiv-inventar.md` dokumentieren nun den konservativen Rahmen `Novapolis = unbekannt` samt indirekter Kette `Corin Mael -> Sera Kaal -> Iris Vey`; benannte Gegenparteien, Routen und Mengen bleiben bewusst offen (`offen: 3 -> 3`).

- RP v5.26: Arkologie-A1 fuehrt jetzt erstmals einen belegten Aussenrahmen statt nur T0-Versorgungshuelle. `Relationslog-Arkologie-A1.md`, `Handelslog-Arkologie-A1.md`, `Missionslog-Arkologie-A1.md` und `Arkologie-inventar.md` dokumentieren nun den konservativen Rahmen `Haendlerbund = beschraenkt`, `Eisenkonklave = umkaempft`, `Novapolis = unbekannt` samt Handels-, Sicherheits- und Biosicherheitskette `Nera Vossen -> Borin Khade -> Liora Navesh`; Mengen, Routen und Einzeldeals bleiben bewusst offen (`offen: 3 -> 3`).

- RP v5.25: Die Eisenkonklave fuehrt jetzt erstmals einen belegten Handelsanker statt nur Rohrahmen. `Missionslog-Eisenkonklave.md`, `Handelslog-Eisenkonklave.md` und `Eiserne-Enklave-inventar.md` dokumentieren nun den konservativen Rahmen `Haendlerbund = handel_gelegentlich` samt Freigabekette `Kaspar Dorn -> Yara Kest`; konkrete Dealmengen, Routen und Tauschlisten bleiben bewusst offen (`offen: 3 -> 3`).

- RP v5.24: Der Haendlerbund ist von der reinen Rahmenwert-Huelle auf einen belegten Aufbaupfad gezogen. `Missionslog-Haendlerbund.md`, `caravan-moves.md` und `Haendlerbund-inventar.md` fuehren jetzt `H-47`, `C6 als Handelsstuetzpunkt`, `G7 als externer Kontaktpunkt` und die ersten Austauschklassen `Energie/Reparaturen/Kommunikationszugang <-> Nahrungsmittel/Filter/Grundbedarfsgueter`; Mengen und Manifeste bleiben bewusst offen (`offen: 3 -> 3`).

- RP v5.23: Die externen Fraktionsinventare fuehren jetzt denselben konservativen `rahmenwert`-Stand wie Matrix, Arbeitsledger und `Warenueberblick-T0.md`. Arkologie-A1, Schienenbund, Haendlerbund, Eisenkonklave, Schattenbund und Fluesterkollektiv zeigen jetzt explizite T0-Rahmen, Herkunftslogik und dokumentierte `RAHMENWERT`-Logs statt leerer `tbd`-Huellen; neue Mengen wurden bewusst nicht gesetzt (`offen: 3 -> 3`).

- RP v5.22: Der offene Warenlauf ist jetzt konservativ geschlossen. `Missionslog-Novapolis.md`, `D5-inventar.md`, `C6-inventar.md` und `Novapolis-inventar.md` fuehren dieselbe belegte Prozessspur `Entnahme/Packen in D5 -> Abmeldung -> Transport mit ReflexAssist -> Eintreffen/Bestandsaufnahme/Empfang in C6`; parallel fuehrt `Novapolis-inventar.md` jetzt das geforderte Delta-/Bilanzformat mit Bedarfsblock statt generischer Sammelnotizen (`offen: 6 -> 3`).

- RP v5.21: Das operative Arbeitsledger fuer die finale Metro-Warenzuteilung ist jetzt als eigenes Arbeitsblatt angelegt. Die Matrix ist damit in `fix`, `rahmenwert` und `handentscheidung` mit sichtbaren Zielpfaden, Stationsbezug und Updatepfad fuer die Zielinventare ueberfuehrt; als offene RP-Reste bleiben Transferkette, Delta-/Bilanzformat und der spaetere Realabgleich (`offen: 7 -> 6`).

- RP v5.18: Der RAW-Rettungsstand vor manueller Verteilung ist jetzt explizit dokumentiert. Hart rettbar bleiben C6-Startsnapshot, D5-Teilanker, generische Transferpfade und einzelne Tagesdeltas; weich rettbar sind Rollen- und Prozesslogik. Aktuelle Fraktionssummen, Restbestaende und konkrete Verbrauchsreihen bleiben weiter Handarbeit.
- RP v5.19: Die operative Zuteilungsmatrix fuer die finale Metro-Warenverteilung liegt jetzt als eigenes Arbeitsblatt vor und ist im Recheck auf alle aktiven Fraktionen ausdifferenziert. Novapolis bleibt darin ausdruecklich getrennt, weil die aktive SSOT nur eine lokale Kernfraktion in frueher Aufbauphase belegt; die externen Fraktionen werden einzeln ueber ihre T0-Warenbilder und Inventarklassen gerahmt (`offen: 6 -> 6`).
- RP v5.20: Nach der fraktionsscharfen Matrix ist jetzt auch der direkte Folgepfad verankert: Die finale Handverteilung soll erst ueber ein explizites Arbeitsledger laufen, bevor D5/C6/Fraktionsinventare weitergezogen werden (`offen: 6 -> 7`).

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
- Dev v5.16: Review-Nachlauf behoben. `scripts/snapshot_gate.py` prueft Freshness jetzt fuer alle betroffenen Markdown-Dateien statt nur bei `stand:`-Diff, und `scripts/pre_commit.py` kommentiert markdownlint nicht mehr irrefuehrend als optional (`offen: 0 -> 0`).
- Dev v5.17: Die aktive Reader-Surface ist wieder als Folgepunkt offen. Root-/Dev-/Modul-READMEs fuehren teils noch Vor-Maerz-Receipts, Altpfade oder Vor-Single-Root-Onboarding und sollen auf den aktuellen PASS-/`.venv`-Stand gezogen werden (`offen: 0 -> 1`).
- Dev v5.18: Reader-Surface-Sync abgeschlossen. Root-/Dev-/Modul-READMEs und `WORKSPACE_INDEX.md` fuehren jetzt den aktuellen Single-Root-/PASS-Kontext ohne alte FAIL-Header, lokale `venv`-Altpfade oder Sibling-Verweise (`offen: 1 -> 0`).
- Agent v5.0: Der dokumentierte Export-/Pack-Standardpfad fuehrt noch einen historischen Null-Export-Fall mit Source-Path-Drift; als neuer Folgepunkt ist jetzt ein lauter Fail oder ein nichtleerer aktueller Export statt stiller `0`-Records verankert (`offen: 0 -> 1`).
- Dev v5.8: O11 geschlossen; externes Standalone-Beta-Installblatt fuer Dritte dokumentiert (`offen: 2 -> 1`).
- Dev v5.7: Community-/Maintainer-Paket umgesetzt (`SUPPORT.md`, `RELEASE.md`, `MAINTAINERS.md`, Root-Issue-/PR-Templates); Dev offen `3 -> 2`.
- Dev v5.6: ADR-Ordner aktiv genutzt; `ADR-0001` und `ADR-0002` als akzeptierte Governance-Entscheidungen aufgenommen (`offen: 4 -> 3`).
- Dev v5.5: Coverage-Sprint Richtung `91%` abgeschlossen und deutlich ueberschritten (`76.24% -> 93.69%`, `offen: 5 -> 4`).
- Dev v5.3: Coverage-Punkt 3 gestartet; 90%-Qualitaetsziel jetzt verbindlich in Dev-Tests/Abschlussprozess verankert.
- Dev v5.4: Punkt 1 (Full-Gate) geschlossen; Coverage-Welle 1 Richtung `91%` gestartet (`76.24% -> 80.45%`).
- Dev v5.2: Folgezyklus fuer Gate-Stabilisierung und modernes Doku-Basispaket gestartet (`offen: 0 -> 5`).
- Dev v5.1: Woechentliche Hygiene-Cadence mit KPI-Tracking verbindlich dokumentiert (`offen: 1 -> 0`).
- Sim v5.0: Sim-Board konsolidiert, verbleibende Mikrodrift geschlossen (`offen: 1 -> 0`).
- Sim v5.1: Der verbleibende Sim-Restpunkt ist jetzt in Problem und Folgepfad getrennt: neben der Warnungsentscheidung liegt ein eigener Bootstrap-Punkt fuer Clean-Checkout vs. Vollstand auf dem Board (`offen: 1 -> 2`).
- Index v2.0: Operative Anzeige erweitert um Board-Metadaten (letzte Aenderung, aeltester offener Punkt, Widerspruchscheck).

Board-Metadaten (automationsrelevant)
-------------------------------------

| Board | letzte Aenderung | aeltester offener Punkt | Widerspruch "keine offenen" |
| --- | --- | --- | --- |
| Dev (`docs/todo.dev.md`) | 2026-03-30 | keiner (offen: 0) | nein |
| RP (`docs/todo.rp.md`) | 2026-03-30 | - [ ] [Spaeter] Vorproduzierte OGG-Summaries je Stunde (world/pc) - Kandidaten markieren. | nein |
| Agent (`docs/todo.agent-board.md`) | 2026-03-30 | keiner (offen: 0) | nein |
| Sim (`docs/todo.sim.md`) | 2026-03-28 | - [ ] [Als naechstes] Sim-Asset-Warnungen aus `scripts/check_sim_epoch_assets.py` aufloesen oder bewusst kanonisch ausnehmen. | nein |


Hinweise (Index)
----------------

- Aktive TODO-Quellen sind `todo.root.md` plus die vier Modul-Boards in `novapolis-dev/docs/`; gleichnamige Dateien unter `novapolis-dev/archive/**` oder `novapolis-dev/archive/quarantine/**` sind Historie, Snapshots oder Arbeitsquarantäne.
- Vollständig erledigte Abschnitte (H2/H3, alle [x]) bitte manuell in `novapolis-dev/archive/todo.<modul>.archive.md` verschieben; unter der Abschnittsüberschrift `archived_at: YYYY-MM-DD HH:MM` ergänzen. Übersicht aller Archive: `novapolis-dev/archive/README.md`.
- Validierung bei Änderungen: markdownlint via `npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc` und Frontmatter-Check via `scripts/check_frontmatter.py`.
- Automationscheck: `scripts/check_todo_index_sync.py` liefert zusaetzlich Metadaten zu letzter Board-Aenderung, aeltestem offenen Punkt und Widerspruchen.

Verweise
--------

- Root-Übersicht: `todo.root.md` (Kurzüberblick, Meta-Aufgaben, Links)
- DONELOG-Zentralstruktur: `novapolis-dev/archive/docs/donelogs/INDEX.md`





