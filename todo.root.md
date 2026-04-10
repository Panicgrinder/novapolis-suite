---
stand: 2026-04-10 13:22
update: Root-Backlog verankert den Folgepfad hinter slot 30 jetzt als gemeinsame SSOT `Text-RPG Slice 2 Handover v1`.
checks: scripts/run_checks_and_report.py overall=FAIL; markdownlint=FAIL; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=FAIL; black=FAIL; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260410_131501.md
---

TODO-Uebersicht (Novapolis Suite)
=================================

Kurzstatus
----------

- Der aktuelle Referenzlauf vom 2026-04-08 ist gruen (`overall=PASS`); der kanonische Beleg liegt unter `.tmp/results/reports/checks_report_20260408_131224.md`.
- Der separate Coverage-Lauf `scripts/run_pytest_coverage.py --fail-under 80` ist ebenfalls PASS (`90.14%`, `518 passed, 1 warning`); der Sim-Offline-Check im Clean-Checkout-Profil endet mit `summary=fail:0,warn:0`.
- Die woechentliche Hygiene-Cadence bleibt gruen (`todo_index_drift=0`, `active_docs_stale=0`, `placeholder_conflicts=0`, `logs_policy_violations=0`).
- Der erste Text-RPG-Slice, der interne Pfad `Slice -> MVP -> Beta` und die Prioritaet `spielbarer Kern vor Komfort` sind auf Root-Ebene gegen den belegten Modul-Iststand geschlossen; die Detailfuehrung liegt jetzt in den Modul-Boards und Gate-SSOTs.
- Vorheriger Vollinhalt wurde archiviert unter `novapolis-dev/archive/quarantine/todo-root-snapshot-20260222_1234.md`.
- Historische Sammelbasis: `novapolis-dev/archive/todo.root.archive.md`.
- Diese Datei ist jetzt die aktive Arbeitsliste fuer neue Punkte.
- README-Pruefpunkt (73/73) wurde nach finalem Doppelcheck archiviert: `novapolis-dev/archive/todo.root.archive.md` (Abschnitt "README-Gesamtlauf (73/73) - abgeschlossen").

Neue Punkte (Backlog)
---------------------

- [x] Zweiten Text-RPG-Produktslice hinter `slot 30` suiteweit auf dieselbe kanonische Kette ziehen.
  - Ziel: Nach dem geschlossenen ersten Slice sollen Root, RP, Agent und Sim denselben Anschluss hinter `slot 30` fuehren, statt den naechsten Produktschritt nur implizit aus RP- oder Runtime-Resten abzuleiten.
  - Akzeptanzkriterien:
    1) Root-, Dev-, Agent-, RP- und Sim-Board benennen denselben Folgepfad hinter `slot 30` ohne abweichende Slice-Namen,
    2) der RP-Pfad fuehrt einen belastbaren Anschluss fuer `slot 31-35` oder eine gleichwertige modulare Episode,
    3) Agent-Produkt-Gate, Referenz-Session und Runbook benennen denselben Handover statt nur den Stand bis `slot 30`,
    4) Sim- und Replay-Pfad koennen den Episodenuebergang ohne ad-hoc-Annahmen ueber Resume-/Checkpoint-Logik tragen.
  - Evidenz: `novapolis-dev/docs/process/text-rpg-product-gate-v1.ssot.md` fuehrt den kanonischen Produktpfad derzeit nur bis `rp-folgekorridor-slot-26-30.ssot.md`; derselbe RP-Folgekorridor nennt im Abschnitt `Weiterer Ausbau` explizit `slot 31-35` oder einen modularen Episodenpfad als naechsten Ausbau.
  - Ergebnis 2026-04-10 00:11: `novapolis-dev/docs/process/text-rpg-slice-2-handover-v1.ssot.md` fixiert jetzt den gemeinsamen Namen, den Session-/Artefaktvertrag und die Modulrollen fuer den Folgepfad hinter `slot 30`. `text-rpg-product-gate-v1.ssot.md` und `novapolis_agent/docs/runbook.md` verweisen im selben Lauf auf dieselbe SSOT; die offenen RP- und Sim-Folgepunkte fuehren damit keinen freien Folgepfad mehr, sondern denselben gemeinsamen Handover.

- [x] Vertikalen Slice `Spielstart Novapolis` als kanonische Produktkette vom Prompt bis zur spielbaren Rueckmeldung festziehen.
  - Ziel: Der erste echte Produktpfad soll nicht mehr nur aus getrennten Chat-, RP-, TTS- und Sim-Bausteinen bestehen, sondern einen zusammenhaengenden Slice `Spielerinput -> KI-Spielleitung -> Weltmutation -> PC-Rueckmeldung -> Logs/Audio/UI` definieren.
  - Akzeptanzkriterien:
    1) Root-, Agent-, RP-, Sim- und Dev-Board benennen denselben Slice ohne widerspruechliche Scope-Grenzen,
    2) der Slice hat einen klaren Startpunkt mit Startslot, Startzustand und erstem Entscheidungsraum,
    3) Weltwahrheit, PC-Sicht und Debug-/Operator-Sicht sind als getrennte Ebenen beschrieben,
    4) der Pfad ist bis Save/Replay/Checks als zusammenhaengende Produktkette nachverfolgbar.
  - Evidenz: `novapolis_agent/README.md` fuehrt stabilen Chat-, TTS- und Eval-Betrieb, `novapolis_agent/app/api/sim.py` aber nur einen Minimalzustand ohne Spielschleife; `novapolis-dev/docs/specs/annotation-spec.md` und `novapolis-dev/docs/specs/scheduler-spec.md` definieren Daten- und Zeitmodell, `novapolis-sim/scripts/Main.gd` konsumiert derzeit statische `world_log`/`pc_log`-Artefakte.
  - Abschluss 2026-04-07: Der Root-Slice ist jetzt ueber dieselben aktiven Quellen zusammengezogen: `novapolis-dev/docs/process/rp-start-chooser.ssot.md` und die Folgekorridore fuehren Startpunkt, Startslot und ersten Entscheidungsraum; `novapolis-dev/docs/specs/text-rpg-session-contract-v1.md` trennt Weltwahrheit, PC-Sicht und Log-Kanaele; `novapolis_agent/docs/runbook.md`, `novapolis-dev/docs/process/text-rpg-product-gate-v1.ssot.md`, `novapolis_agent/app/api/sim.py` und `novapolis-sim/scripts/Main.gd` fuehren denselben Pfad bis Save/Replay/Checks und Sim-Hub ohne widerspruechliche Modulsicht.

- [x] Ersten internen Releasepfad `Slice -> spielbarer MVP -> betreibbare Beta` moduluebergreifend absichern.
  - Ziel: Der Weg bis zum fertigen Produkt soll nicht beim ersten spielbaren Prototyp enden, sondern bereits jetzt die Stufen bis zu einem betreibbaren, testbaren und nachvollziehbar freigabefaehigen Build beschreiben.
  - Akzeptanzkriterien:
    1) MVP-, Beta- und spaeterer Produktstatus sind ueber klare DoD-/Gate-Kriterien getrennt,
    2) technische Folgepunkte liegen in Dev/Agent/Sim, inhaltliche Folgepunkte in RP, die Root-Sicht verknuepft nur noch,
    3) Save/Replay, Operator-Runbook, Eval- und Release-Gates sind vor einer Beta nicht mehr implizit, sondern eigene Arbeitspakete,
    4) der Produktpfad bleibt im Root sichtbar, ohne Modul-Detailarbeit doppelt zu fuehren.
  - Evidenz: `novapolis-dev/docs/process/project-context-bridge.ssot.md` fuehrt bisher nur den projektbewussten Chatmodus bis Phase 4, `novapolis_agent/docs/runbook.md` trennt Chat, Sim, TTS und Eval noch als Einzelablaeufe, und `novapolis-dev/docs/todo.index.md` fuehrte bis jetzt keinen zusammenhaengenden Text-RPG-Produktpfad.
  - Abschluss 2026-04-07: Der interne Releasepfad ist jetzt ueber `novapolis-dev/docs/process/text-rpg-product-gate-v1.ssot.md`, `novapolis-dev/docs/process/standalone-beta-gates.ssot.md`, `novapolis_agent/docs/runbook.md` und `novapolis-dev/docs/todo.index.md` sauber getrennt. `Text-RPG Product Gate v1` deckt den spielbaren Slice/MVP-Pfad ab, die Standalone-Beta-Gates fixieren den betreibbaren Beta-Go/No-Go, und Root verweist nur noch auf diese kanonischen Modul- und Gate-SSOTs statt dieselbe Detailarbeit doppelt zu fuehren.

- [x] Inhalts- und Technikskalen nach dem ersten Slice sauber trennen: `spielbarer Kern` zuerst, `Weltbreite und Komfort` danach.
  - Ziel: Das Produkt soll zuerst eine belastbare, KI-geleitete Kernrunde koennen, bevor breitere Weltabdeckung, TTS-Komfort, Asset-Ausbau und spaetere Erweiterungen dieselbe Prioritaet bekommen.
  - Akzeptanzkriterien:
    1) Pflichtarbeit fuer den ersten Slice ist als `Jetzt/Als naechstes` von spaeterem Welt- und Komfortausbau getrennt,
    2) RP priorisiert Startkorridor, Sphaeren-/Mind-Cluster-SSOT und Reveal-Regeln vor spaeterem Flavour-Ausbau,
    3) Agent priorisiert Session-/State-/Eval-Pfade vor weiterem Komforttraining,
    4) Sim priorisiert Live-Spielclient und Replay-Bridge vor Atmosphaere-/Asset-Breite.
  - Evidenz: `novapolis-dev/docs/todo.rp.md` hielt zuletzt nur Restarbeit fuer TTS offen, `novapolis-dev/docs/todo.agent-board.md` stand bei offen `0`, und `novapolis-dev/docs/todo.sim.md` fuehrte nur Hygiene-/Assetpunkte statt eines produktnahen Spielerloops.
  - Abschluss 2026-04-07: Die Prioritaet `spielbarer Kern vor Weltbreite/Komfort` ist jetzt belegter Modul-Iststand statt Root-Absicht. RP fuehrte Startkorridor, Reveal-Matrizen, Folgekorridore und OGG-Kandidaten zuerst; Agent fuehrte Session-/State-/Eval-/TTS-Vertrag zuerst; Sim zog Live-Spielclient, Replay-Bridge und erst danach Asset-/Bootstrap-Klarheit nach. `novapolis-dev/docs/todo.index.md` zeigt den Produktpfad dadurch moduluebergreifend ohne offene Komfort- oder Breitenpflicht fuer den ersten Slice.

- [x] Verbleibenden Root-eval-Rest auf den Modulpfad umziehen und danach aus dem aktiven Root-Surface entfernen.
  - Ziel: Der letzte noch aktive Root-Verweis `eval/config/context.local.md` soll auf den kanonischen Modulpfad unter `novapolis_agent/eval/config/` umgestellt werden, damit der verbliebene Root-eval-Rest nicht weiter technisch live bleibt.
  - Akzeptanzkriterien:
    1) Runtime-Defaults und Hilfsskripte nutzen fuer lokale Kontext-Notizen den Modulpfad statt `eval/config/...`,
    2) aktive Doku verweist auf `novapolis_agent/eval/config/context.local.sample.md` und den Modulpfad in `CONTEXT_NOTES_PATHS`,
    3) der verbliebene Root-eval-Rest wird nachvollziehbar nach Quarantaene ueberfuehrt statt still geloescht,
    4) Root-/Agent-DONELOG, Status und TODO-Index dokumentieren den Schritt im selben Lauf.
  - Evidenz: `novapolis_agent/app/core/settings.py` fuehrt `CONTEXT_NOTES_PATHS` noch mit `eval/config/context.local.md`, `novapolis_agent/scripts/open_context_notes.py` faellt ebenfalls auf den Root-Pfad zurueck, und `eval/results/tmp_summaries/` hat im aktiven Scope keine belegten Referenzen mehr.
  - Abschluss 2026-03-28: `app/core/settings.py`, `app/api/chat.py`, `scripts/open_context_notes.py` und die Agent-README nutzen jetzt durchgaengig `novapolis_agent/eval/...`; der urspruengliche Root-Ordner `eval/` liegt nachvollziehbar unter `novapolis-dev/archive/quarantine/root-cleanup-20260328_0501-root-eval-rest/eval`, ein nach den Nachweisen erneut entstandener lokaler Stub `eval/config/context.local.md` wurde zusaetzlich nach `novapolis-dev/archive/quarantine/root-cleanup-20260328_0632-root-eval-rest-postchecks/eval` ueberfuehrt, und die Root-Tree-Artefakte wurden danach erneut neu erzeugt.

- [x] Lokale Editor-/Host-Snapshots aus dem Main-Root in Quarantaene ueberfuehren.
  - Ziel: Root-Dateien ohne aktive Repo-Funktion, die nur den lokalen VS-Code-/Host-Stand spiegeln, sollen nicht im produktiven Single-Root-Surface liegen.
  - Akzeptanzkriterien:
    1) `extensions.installed.txt`, `extensions.status.txt` und `desktop.ini` liegen nicht mehr im Root,
    2) die Dateien sind in einem nachvollziehbaren Quarantaenepfad abgelegt statt still geloescht,
    3) aktive Root-Pfade wie Shims, Tree-Artefakte und Governance-Dokumente bleiben unangetastet,
    4) Root-Backlog, DONELOGs und Workspace-Status dokumentieren den Schritt im selben Lauf.
  - Evidenz: `extensions.installed.txt` listet lokale VS-Code-Erweiterungen, `extensions.status.txt` ist ein lokaler `code --status`-Snapshot, und `desktop.ini` taucht nur noch im alten Tree-Artefakt auf, nicht als aktive Repo-Referenz.
  - Abschluss 2026-03-28: Die drei Dateien liegen jetzt unter `novapolis-dev/archive/quarantine/root-cleanup-20260328_0330-local-snapshots/`; die Root-Tree-Artefakte wurden danach direkt per Terminal neu erzeugt, weil die vorhandenen Shell-Tasks lokal weiter am bekannten `pwsh /d /c`-Fehlpfad scheitern.

- [x] Sichere Root-Altartefakte aus dem aktiven Single-Root-Surface in Quarantaene ueberfuehren.
  - Evidenz: `combined.json`, `lint.out`, `md003_scan.out`, `.tmp-datasets/` und `reports/` lagen als historische oder temporare Restartefakte direkt im Repo-Root, obwohl der aktive Betriebsrahmen diese Inhalte heute unter `.tmp/`, Modulpfaden oder Archiv-/Quarantaenepfaden fuehrt.
  - Abschluss 2026-03-28: Die Kandidaten liegen gesammelt unter `novapolis-dev/archive/quarantine/root-cleanup-20260328_0238/`; die gleichnamigen Root-Pfade sind entfernt und tauchen im aktiven Root nicht mehr auf.
  - Bewusste Nicht-Ziele: Die aktiven Kompatibilitaetsshims `app/__init__.py` und `utils/__init__.py` sowie der noch referenzierte Hinweis `eval/config/context.local.md` blieben unveraendert.

- [x] Einheitlichen Stil- und Konsistenzlauf fuer Hochfrequenz-Dateien und aktive Doku nach dokumentiertem Phasenplan durchziehen.
  - Evidenz: `README.md`, `WORKSPACE_INDEX.md`, `novapolis-dev/README.md`, die Modul-READMEs und `novapolis-dev/docs/todo.index.md` mussten gerade erst sichtbare Drift bei Status-Headern, Pfaden, Kommandos und aktiven Verweisen nachgezogen bekommen.
  - Arbeitsplan: `novapolis-dev/docs/process/doku-konsistenzlauf-aktive-surface-2026-03-28.md`.
  - Abschluss 2026-03-28: Hochfrequenz-Dateien, aktive Dev-SSOTs und die ersten Modul-Runbooks fuehren jetzt durchgaengig den PASS-/Root-Wrapper-Stil; im aktiven Scope blieb beim Restscan nur noch ignorierte Drittanbieter-Doku unter `node_modules` ausserhalb des Arbeitsbereichs uebrig.

- [x] Aktive Reader-Surface fuer Root/Dev und die vier Hauptmodule auf den aktuellen Single-Root-/PASS-Iststand ziehen.
  - Evidenz: `novapolis-dev/README.md`, `WORKSPACE_INDEX.md`, `novapolis_agent/README.md`, `novapolis-rp/README.md`, `novapolis-sim/README.md` fuehren teils noch Vor-Maerz-Receipts, Altpfade oder lokale `venv`-/Sibling-Hinweise statt des aktuellen Root-`.venv`- und PASS-Kontexts.
  - Abschluss 2026-03-28: Die aktiven Lesedokumente fuehren jetzt keinen veralteten FAIL-Header mehr, nutzen den Single-Root-/`.venv`-Pfad konsistent und trennen im Sim-Modul UI-Start sauber von optionalen Asset-Warnungen.

- [x] Agent-Export-/Pack-Pfad gegen Null-Exports aus historischem Results-Drift haerten.
  - Evidenz: `novapolis-dev/docs/todo.agent-board.md`, `novapolis_agent/docs/DONELOG.txt` (historischer Laufbeleg 2026-02-27 mit `0` Export-Eintraegen wegen Source-Path-Drift).
  - Abschluss 2026-03-30: `novapolis_agent/scripts/export_finetune.py` leitet Dataset-Kandidaten jetzt aus Results-Metadaten und `source_file` ab, `novapolis_agent/scripts/curate_dataset_from_latest.py` waehlt nicht mehr blind den Dateinamen-Toptreffer, sondern das neueste exportierbare Resultset, und Null-Exports brechen mit Diagnostik (`successful_rows`, `exportable_count`, `unmapped_item_ids`) explizit ab. Gezielte Pytests sind gruen; ein temp-basierter Real-Lauf gegen `novapolis_agent/eval/results/` hat fuer `results_20260226_0306_quality_de_round7b_repeat3.jsonl` wieder `20` Export-Eintraege und einen Pack-Split `train=18`, `val=2` erzeugt.

- [x] RP-Inventar-Backfill in die belegte Transferkette ueberfuehren (`D5 -> C6` mit Entnahme, Zielbuchung, Quittung) und `Novapolis-inventar.md` auf Delta-Format umstellen.
  - Evidenz: `novapolis-dev/docs/todo.rp.md`, `novapolis-dev/docs/process/rp-inventory-backfill-pilot-2026-03-20.md`, `novapolis-rp/database-rp/01-factions/novapolis/04-inventory/Novapolis-inventar.md`.
  - Abschluss 2026-03-31: Der Warenlauf fuehrt jetzt in `Missionslog-Novapolis.md`, `D5-inventar.md`, `C6-inventar.md` und `Novapolis-inventar.md` dieselbe konservativ belegte Prozesskette mit Pack-/Entnahmeanker in D5, Transport durch Ronja plus ReflexAssist, Eintreffen/Bestandsaufnahme/Empfang in C6 und anschliessender Baustellenverteilung; `Novapolis-inventar.md` fuehrt die Fraktionslage parallel im Delta-/Bilanzformat mit Bedarfsblock statt Sammelfreitext.

- [x] RP-Finalzuteilung aus der fraktionsscharfen Matrix in ein operatives Arbeitsledger ueberfuehren.
  - Evidenz: `novapolis-dev/docs/process/rp-metro-warenzuteilung-matrix-2026-03-27.md`, `novapolis-dev/docs/process/rp-metro-warenzuteilung-arbeitsledger-2026-03-30.md`, `novapolis-dev/docs/todo.rp.md`.
  - Abschluss 2026-03-30: Das neue Arbeitsledger trennt jetzt den fixen Sockel, konservative Rahmenwerte und echte Handentscheidungen mit sichtbaren Zielpfaden; damit ist der Uebergang von der Matrix in ein operatives Verteilungsblatt geschlossen.

- [x] Sim-Asset-Warnungen aus dem Wochenabschluss entscheiden: entweder beheben oder als bewusste Ausnahme dokumentieren.
  - Evidenz: `novapolis-dev/docs/todo.sim.md`, `WORKSPACE_STATUS.md` (Wochenabschluss 2026-03-27, `summary=fail:0,warn:2`).
  - Abschluss 2026-04-07: `scripts/check_sim_epoch_assets.py` behandelt `--allow-empty` jetzt als kanonisches Clean-Checkout-Profil statt als Warnpfad; der Lauf `--repo-root . --allow-empty --check-slot-consistency` endet im aktuellen Repo-Stand mit `summary=fail:0,warn:0`.

- [x] Sim-Minimalprofil fuer Epoch-/Audio-Assets festlegen, damit Clean-Checkout und Vollstand getrennte Erwartungswerte haben.
  - Evidenz: `novapolis-dev/docs/todo.sim.md`, `novapolis-sim/README.md`, `WORKSPACE_STATUS.md` (weiter `warn:2` trotz sonst gruener Sim-Verifikation).
  - Abschluss 2026-04-07: `novapolis-sim/data/epochs/` und `novapolis-sim/assets/audio/` sind als Bootstrap-Zielorte angelegt; `novapolis-sim/README.md` und der Checker unterscheiden jetzt explizit zwischen warnungsfreiem `Clean-Checkout` mit `--allow-empty` und artefaktbelegtem Vollstand ohne dieses Flag.

- [x] Wochenabschluss 2026-03-27 nach SSOT komplett ausgefuehrt (Full-Gate, Coverage-Gate, Hygiene-KPIs, Abschluss-Sync).
  - Evidenz: `.tmp/results/reports/checks_report_20260327_011507.md`, `WORKSPACE_STATUS.md`, `DONELOG.md`, `novapolis-dev/docs/donelog.md`, `novapolis-dev/docs/meta/dev-kpi-trends.md`, `novapolis-dev/docs/todo.agent-board.md`, `novapolis-dev/docs/todo.sim.md`.

- [x] Wochenabschluss 2026-03-10 nach SSOT ausgefuehrt (Checks, Tree-Artefakte, Abschluss-Sync).
  - Evidenz: `.tmp/results/reports/checks_report_20260310_153947.md`, `workspace_tree_full.txt`, `workspace_tree.txt`, `workspace_tree_dirs.txt`, `WORKSPACE_STATUS.md`, `DONELOG.md`, `novapolis-dev/docs/donelog.md`.

- [x] Tunnel-Check als VS-Code-Task ergänzen (`Checks: sim epoch assets`) und im README kurz dokumentieren.
  - Evidenz: `/.vscode/tasks.json`, `README.md`.
- [x] Aktive TODO-Boards (Agent/Sim/RP) auf Prioritätstags `Jetzt/Als naechstes/Später` harmonisieren.
  - Evidenz: `novapolis-dev/docs/todo.agent-board.md`, `novapolis-dev/docs/todo.sim.md`, `novapolis-dev/docs/todo.rp.md`.
- [x] Wochenabschluss-Routine standardisieren: Reihenfolge und Artefaktablage für Tests/Checks/Status-Update verbindlich notieren.
  - Evidenz: `README.md` (Abschnitt „Wochenabschluss-Routine“).
- [x] [Jetzt] `TTS/` nur als temporaere Entnahmequelle behandeln: benoetigte Teile nach `novapolis_agent/` ueberfuehren und das Root-Verzeichnis `TTS/` danach entfernen.
  - Akzeptanzkriterien: (1) Entnommene Dateien/Pfade in `novapolis_agent/` dokumentiert, (2) `TTS/` aus Root entfernt, (3) README/Status/DONELOG synchronisiert.
  - Evidenz: `novapolis_agent/scripts/tts_coqui_export.py` (`--help` verifiziert), Root-Pfad `TTS/` entfernt, Sync in `README.md`/`WORKSPACE_STATUS.md`/`DONELOG.md`.

Standalone-Beta Exit-Checkliste (v0, geordnet)
-----------------------------------------------

Ziel: Eine lokal reproduzierbare Standalone-Beta mit stabilen Gates, dokumentierter Bedienung und klaren No-Go-Kriterien.

- [x] [Blocker B1] Root-TTS-Migration abschliessen: benoetigte Inhalte aus `TTS/` in `novapolis_agent/` ueberfuehren und Root-`TTS/` entfernen.
  - Akzeptanz: `todo.root.md`-Punkt erledigt; README/Status/DONELOG synchron; kein Root-`TTS/` mehr im aktiven Baum.
- [x] [Blocker B2] Sim-Restpunkte schliessen: in `novapolis-dev/docs/todo.sim.md` den Platzhalter konkretisieren und den offenen DoD-Punkt evidenzbasiert auf erledigt setzen.
  - Akzeptanz: `offen: 0` fuer Sim im `novapolis-dev/docs/todo.index.md`.
- [x] [Blocker B3] RP-P0-DoD schliessen: T0-Warenueberblick je Fraktion + D5/C6-Aufbauphase konsistent finalisieren.
  - Akzeptanz: offene `[Jetzt]`-Punkte in `novapolis-dev/docs/todo.rp.md` fuer P0 erledigt, Evidenzpfade gesetzt.
- [x] [Blocker B4] Dev-Truthfulness korrigieren: offene Driftpunkte in `novapolis-dev/docs/todo.dev.md` fuer aktive Dokuoberflaeche beheben.
  - Akzeptanz: README/spec claims spiegeln ausschliesslich Iststand.
- [x] [Blocker B5] Stabilen Full-Check als Beta-Gate einfrieren: ein aktueller kompletter Lauf (`Checks: full`) mit gruenem Ergebnisbeleg.
  - Akzeptanz: verlinkter Report in `.tmp/results/reports/` plus Eintrag in `novapolis-dev/docs/donelog.md` und `DONELOG.md`.
- [x] [Blocker B6] Standalone-Startpfad dokumentieren: ein kanonischer Startablauf fuer API + Sim-Hub + Checklauf.
  - Akzeptanz: reproduzierbarer Abschnitt in `README.md` oder Runbook mit 1:1-Kommandos und erwarteten Ergebnissen.
- [x] [Blocker B7] Release-Go/No-Go Kriterien festschreiben: minimale Schwellwerte fuer Tests/Typen/Coverage/Runtime.
  - Akzeptanz: schriftliche Gate-Definition in Dev-Doku; Entscheidung pro Lauf nachvollziehbar protokolliert.
- [x] [Optional O8] TODO-Index-Guard automatisieren: Aenderungen an `todo.*.md` erzwingen Sync von `novapolis-dev/docs/todo.index.md`.
  - Akzeptanz: technischer Check vorhanden und im Standardlauf eingebunden.
  - Evidenz: `scripts/check_todo_index_sync.py`, `scripts/run_checks_and_report.py`, `/.vscode/tasks.json` (`Checks: todo index sync`).
- [x] [Optional O9] Freshness-SLA durchsetzen: aktive Dokus nach Altersgrenze pruefen (`stand`).
  - Akzeptanz: dokumentierter Checklauf ohne ungekennzeichnete Ausnahmen.
  - Evidenz: `scripts/check_doc_freshness.py` (ACTIVE `<=14`, REFERENCE `<=60`), `scripts/run_checks_and_report.py`, `/.vscode/tasks.json` (`Checks: doc freshness`).
- [x] [Optional O10] Logs-Policy haerten: klare Regeln fuer `novapolis-dev/logs/` inkl. `*.tmp.md` konsistent umsetzen.
  - Akzeptanz: keine policy-widrigen Artefakte im aktiven Logpfad.
  - Evidenz: `scripts/check_logs_policy.py`, `novapolis-dev/logs/logs-policy.md`, verschobener Rohlog nach `novapolis-dev/archive/quarantine/logs/betriebsmodi-20251103-0341.tmp.md`.
- [x] [Optional O11] Beta-Installblatt fuer Dritte erstellen: minimale Voraussetzungen, Setup, Troubleshooting.
  - Akzeptanz: eine externe Person kann lokal ohne implizites Vorwissen starten.
  - Evidenz: `novapolis-dev/docs/process/standalone-beta-installblatt.md`, Root-README-Verweis im Abschnitt `Standalone-Beta Startpfad (kanonisch)`.
- [x] [Optional O12] Beta-Tagging vorbereiten: einheitliches Namensschema fuer Beta-Builds und Ergebnisreports.
  - Akzeptanz: run-/artefaktnahe Labels sind in Doku und DONELOG konsistent.
  - Evidenz: `novapolis-dev/docs/process/standalone-beta-gates.ssot.md` (Abschnitt `Beta-Tagging-Konvention`), Eintragsformat in `novapolis-dev/docs/donelog.md` und `DONELOG.md`.

Definition of Ready fuer "Standalone Beta"
-------------------------------------------

- [x] Alle Blocker B1-B7 erledigt.
- [x] Ein finaler Referenzlauf (Checks + Startpfad) ist reproduzierbar dokumentiert.
- [x] Offene Punkte sind nur noch als `[Optional]` markiert.

Hinweise
--------

- Abgeschlossene oder historisierte Bloecke in `novapolis-dev/archive/todo.root.archive.md` verschieben.
- Bei jeder Mutation TODO/DONELOG/WORKSPACE_STATUS synchron halten.






