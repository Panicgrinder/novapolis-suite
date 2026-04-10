---
stand: 2026-04-10 13:22
update: Der kanonische Coverage-Lauf ist jetzt wieder warnungsfrei; der `runpy`-Hygiene-Rest ist geschlossen.
checks: scripts/run_checks_and_report.py overall=FAIL; markdownlint=FAIL; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=FAIL; black=FAIL; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260410_131501.md
---

<!-- markdownlint-disable MD022 MD041 -->

TODO (Novapolis-Dev)
====================

Hinweis
-------

- Dieses Dokument buendelt Aufgaben fuer das Dev-Modul (Tooling, Lint/CI, Validatoren, Doku-Infra).
- RP-Aufgaben liegen in `docs/todo.rp.md`. Agent-Aufgaben liegen in `docs/todo.agent-board.md`.
- Vollstaendig erledigte Bloecke werden nach `novapolis-dev/archive/todo.dev.archive.md` verschoben.

Offene Aufgaben (Dev)
---------------------

- [x] [Jetzt] `runpy`-Warnings im kanonischen Coverage-Lauf auf einen sauberen, warnungsfreien Skriptpfad reduzieren.
  - Ziel: Der produktive Coverage- und Script-Testpfad soll keine vermeidbaren Importzustands-Warnings mehr ausgeben, damit echte Runtime-Warnungen nicht hinter bekannten Testartefakten verschwinden.
  - Akzeptanzkriterien:
    1) die aktuellen `RuntimeWarning: ... found in sys.modules after import of package 'scripts'` fuer `open_latest_summary`, `run_text_rpg_reference_session`, `summarize_gm_eval_kpis` und `validate_eval_datasets` verschwinden aus dem kanonischen Coverage-Lauf,
    2) die betroffenen Edge-Tests bleiben in ihrer Modul- bzw. CLI-Absicherung gruen,
    3) die Loesung erklaert nachvollziehbar, ob `runpy`, Importreihenfolge oder Shim-Layout der Root Cause ist, statt die Warnings nur zu unterdruecken,
    4) `.tmp/results/reports/pytest_coverage_postflight_*.md` bleibt danach weiter PASS und fuehrt keine neuen Warnings derselben Klasse.
  - Evidenz: `.tmp/results/reports/pytest_coverage_postflight_20260409_232603.md` endet mit genau vier `runpy`-RuntimeWarnings in `tests/scripts/test_open_latest_summary_edges.py`, `test_run_text_rpg_reference_session_edges.py`, `test_summarize_gm_eval_kpis_edges.py` und `test_validate_eval_datasets_edges.py`.
  - Ergebnis 2026-04-10 05:16: Die vier Edge-Tests fuehren die betroffenen CLI-Pfade nicht mehr via `runpy.run_module()` auf bereits vorimportierten `scripts.*`-Modulen aus, sondern ueber den echten Skriptpfad per `runpy.run_path(..., run_name="__main__")`. Damit verschwindet die `sys.modules`-Kollision an der Ursache statt per Warning-Filter. Der kanonische Wrapper-Lauf `.tmp/results/reports/pytest_coverage_postflight_20260410_051125.md` ist mit `596 passed`, `returncode=0`, `Total coverage: 93.66%` und ohne `found in sys.modules after import of package 'scripts'`-Warnings PASS; das Dev-Board steht damit wieder bei `offen: 0`.

- [x] [Jetzt] Schonmodus fuer Test- und Check-Tasks ueber CPU-Limit einfuehren.
  - Ziel: Workspace-Tasks fuer Tests, Coverage und Sammelchecks sollen auf dem lokalen 6C/12T-Rechner keine unnoetigen CPU-Spitzen mehr verursachen und dadurch den Gesamtzustand des Systems stabiler halten.
  - Akzeptanzkriterien:
    1) ein wiederverwendbarer Wrapper begrenzt Python-Subprozesse auf einen kleinen CPU-Slice statt alle logischen Prozessoren frei zu nutzen,
    2) die relevanten VS-Code-Tasks fuer Tests und Checks laufen ueber denselben Schonpfad,
    3) die Loesung bleibt per Parameter anpassbar und ist nicht hart auf genau eine CPU-Maske verdrahtet,
    4) ein gezielter Testlauf oder Script-Test belegt den Wrapper gegen Regression.
  - Evidenz: Die aktuelle Systemprobe meldet `AMD Ryzen 5 3600X`, `6` physische Kerne, `12` logische Prozessoren und bereits im Leerlauf rund `69%` committed RAM; die bestehenden Tasks in `.vscode/tasks.json` und Root-Wrapper wie `scripts/run_pytest_coverage.py` setzen bislang keine CPU-Grenzen.
  - Ergebnis 2026-04-09 17:34: `scripts/run_with_cpu_limit.py` begrenzt jetzt Windows-Tasklaeufe ueber CPU-Affinität, `below_normal`-Prioritaet und konservative Thread-Umgebungsvariablen; ohne expliziten Override nutzt der Wrapper auf dem lokalen 12-Thread-System automatisch `4` logische CPUs. Die schweren VS-Code-Tasks fuer Root-Pytest, Coverage, Full-Check, Produkt-Gate sowie Eval-/Validierungslaeufe in `.vscode/tasks.json` laufen jetzt ueber denselben Schonpfad. Der neue Regressionstest `novapolis_agent/tests/scripts/test_run_with_cpu_limit.py` ist PASS, und die direkte Env-Probe ueber den Wrapper bestaetigt `NVP_CPU_LIMIT_ACTIVE=4`, `OMP_NUM_THREADS=4` und `TOKENIZERS_PARALLELISM=false` im Kindprozess.

- [x] [Jetzt] GM-Payload-Pfad ohne ungewollte Kontextnotizen haerten.
  - Ziel: Der produktive `/chat`-Pfad soll lokale Kontextnotizen nur dann in GM-Requests injizieren, wenn `CONTEXT_NOTES_ENABLED` explizit aktiv ist, damit der Restpfad nicht durch unbeabsichtigte Zusatzprompts verlangsamt oder verfälscht wird.
  - Akzeptanzkriterien:
    1) `_resolve_context_notes()` liefert bei `CONTEXT_NOTES_ENABLED=False` auch dann `None`, wenn an den konfigurierten Pfaden Notizdateien liegen,
    2) `process_chat_request()` injiziert im deaktivierten Zustand keinen `[Kontext-Notizen]`-Systemturn,
    3) ein gezielter Test deckt den deaktivierten Pfad gegen Regression ab,
    4) die vorhandene Live-Repro bleibt als Evidenz am Board haengen.
  - Evidenz: Der heute extrahierte GM-Payload fuer `gm.session.continuity.v1` enthielt zunaechst drei Nachrichten mit einem zusaetzlichen Systemturn `[Kontext-Notizen]`, obwohl `CONTEXT_NOTES_ENABLED` im aktiven Settings-Stand `False` ist. Die direkte Variantenprobe zeigte ausserdem: `system_user_512` liefert noch eine Antwort, waehrend `full_512`, `full_2048` und `full_10024` im aktuellen Localhost-Lauf in Timeouts kippen.
  - Ergebnis 2026-04-08 23:08: `novapolis_agent/app/api/chat.py` beendet `_resolve_context_notes()` jetzt sofort bei deaktiviertem Flag, statt gefundene Notizen trotzdem durchzureichen. Der neue Test `test_process_chat_request_skips_context_notes_when_disabled` ist PASS, und die Live-Payload-Pruefung fuer `gm.session.continuity.v1` zeigt danach nur noch zwei Nachrichten (`system`, `user`) ohne `[Kontext-Notizen]`-Turn.

- [x] [Jetzt] Text-RPG Product Gate v1 um Runtime-Preflight und trennscharfe GM-Fehlklassifikation haerten.
  - Ziel: Der Produktlauf soll den verbleibenden GM-Restpfad nicht mehr als diffusen Runtime-Haenger melden, sondern fehlende Ollama-Runtime, Ollama-500 und produktive Timeouts vor oder direkt nach dem GM-Schritt explizit unterscheiden.
  - Akzeptanzkriterien:
    1) `scripts/run_text_rpg_product_gate.py` fuehrt vor `gm_session_eval` einen schnellen Runtime-Preflight fuer Host, `/api/tags` und erwartetes Modell aus,
    2) der Produktreport markiert `runtime_unreachable`, `model_missing`, `ollama_http_500` und `gm_timeout_504` als getrennte Fehlerklassen statt nur `step failed: gm_session_eval`,
    3) ein fehlender oder defekter GM-Lauf bleibt weiter summarisiert, aber die Hauptursache ist im Report ohne Logsuche sichtbar,
    4) der neue Pfad ist mit Unit-Tests fuer Preflight-/Klassifikationslogik abgesichert.
  - Evidenz: Der frische Re-Run `process: Eval: suite gm_session (12, asgi)` erzeugt `novapolis_agent/eval/results/results_20260408_2150_gm_session.jsonl`; dabei scheitert `gm.session.continuity.v1` mit `Server error '500 Internal Server Error' for url 'http://localhost:11434/api/chat'`, waehrend `gm.session.reveal-discipline.v1` und `gm.session.option-quality.v1` im Agent-Pfad mit `504 Gateway Timeout` enden. Der lokale Listener selbst ist dagegen live (`127.0.0.1:11434`, Modelle `qwen2.5:7b` und `llama3.1:8b`), sodass der Produktlauf ohne Preflight-/Fehlertrennung aktuell einen zu groben Restblocker meldet.
  - Ergebnis 2026-04-08: `scripts/run_text_rpg_product_gate.py` fuehrt vor `gm_session_eval` jetzt `gm_runtime_preflight` gegen den aktiven Ollama-Host und das erwartete Modell aus und klassifiziert spaetere GM-Resultate nach `runtime_unreachable`, `model_missing`, `ollama_http_500` und `gm_timeout_504`. Der gezielte Testblock `novapolis_agent/tests/scripts/test_run_text_rpg_product_gate.py` ist mit vier Tests PASS, und Ruff sowie `black --check` sind fuer die betroffenen Dateien gruen.

- [x] [Jetzt] Text-RPG Product Gate v1 als reproduzierbaren Verbundlauf mit GM-Session-Eval, KPI-Summary und fester Referenz-Session haerten.
  - Ziel: Der kanonische Produktpfad soll nicht laenger aus getrennten Einzel-Tasks bestehen, sondern denselben Text-RPG-Lauf ueber Full-Check, API-/Streaming-Smoke, Sim-Smoke, GM-Session-Eval und eine feste Referenz-Session reproduzierbar zusammenhalten.
  - Akzeptanzkriterien:
    1) ein kanonischer Runner oder Task fuehrt `Checks: full`, `Tests: pytest (api+streaming)`, `Checks: sim epoch assets`, den `gm_session`-Eval-Lauf und die KPI-Summary in dokumentierter Reihenfolge aus,
    2) Produkt-Gate-SSOT, Runbook und Workspace-Tasking verwenden danach denselben Verbundlauf statt separater, nur lose referenzierter Teilpfade,
    3) eine feste Referenz-Session oder ein aequivalenter Referenz-Case ist fuer denselben Produktpfad als reproduzierbarer Beleg definiert,
    4) der Lauf erzeugt einen kompakten Reportpfad fuer den Produktentscheid statt nur verteilte Einzelartefakte.
  - Evidenz: `novapolis-dev/docs/process/text-rpg-product-gate-v1.ssot.md` und `novapolis_agent/docs/runbook.md` fuehren aktuell nur den Task-Block `Checks: full` -> `Tests: pytest (api+streaming)` -> `Checks: sim epoch assets`; `.vscode/tasks.json` enthaelt zwar bereits `Eval: suite gm_session (12, asgi)` und `Eval: summarize gm session KPIs`, aber noch keinen kanonischen Verbundlauf, der diese Stufen zusammen mit einer festen Referenz-Session als Produkt-Gate ausfuehrt.
  - Ergebnis 2026-04-08: `scripts/run_text_rpg_product_gate.py` und der Task `Checks: text-rpg product gate` fuehren jetzt Full-Check, API-/Streaming-Tests, `Tests: text-rpg reference session`, Sim-Smoke, `gm_session`-Eval und KPI-Summary in einem Reportpfad zusammen. Die feste Referenz-Session liegt unter `novapolis_agent/eval/config/text_rpg_reference_session.v1.json`, laeuft ueber `novapolis_agent/scripts/run_text_rpg_reference_session.py` deterministisch gegen die Session-API und schreibt Savegame-, `world_log`-, `pc_log`- und Replay-Belege. Der reale Verifikationslauf `.tmp/results/reports/text_rpg_reference_session_verify.json` ist PASS; der Wrapper-Gesamtlauf `.tmp/results/reports/text_rpg_product_gate_verify.md` belegt denselben neuen Verbundpfad und zeigt als verbleibende lokale Hard-Fail-Grenze nur noch die nicht erreichbare Modellruntime des `gm_session`-Abschnitts, nicht mehr Gate- oder Task-Drift.

- [x] [Jetzt] Kanonischen Typenlauf fuer Workspace-Task und Wrapper wieder auf dieselbe Agent-Konfigurationsbasis ziehen.
  - Ziel: `Checks: types (pyright+mypy)` soll wieder denselben belastbaren Scope pruefen wie der dokumentierte Agent-Produktpfad, statt wegen Konfigurationspfad-Drift in einen unbeabsichtigten Repo-Weitlauf zu kippen.
  - Akzeptanzkriterien:
    1) `scripts/checks_types.py` verwendet die real vorhandenen Konfigurationen `novapolis_agent/pyrightconfig.json` und `novapolis_agent/mypy.ini` oder setzt den Prozesspfad aequivalent belastbar,
    2) der Workspace-Task `Checks: types (pyright+mypy)` prueft denselben Scope reproduzierbar und scheitert nicht mehr schon an fehlenden Config-Dateien,
    3) Pyright laeuft nicht mehr versehentlich gegen den gesamten Repo-Baum mit fremden Integrations-/Optional-Dependency-Treffern ausserhalb des beabsichtigten Agent-Scopes,
    4) Board, Runbook-Claim und Task-Realitaet widersprechen sich danach nicht mehr.
  - Evidenz: `.vscode/tasks.json` startet `scripts/checks_types.py` zwar fuer `novapolis_agent`, aber der Wrapper loest seinen `ROOT` auf das Repo auf und ruft von dort `pyright -p pyrightconfig.json` sowie `mypy --config-file mypy.ini app scripts` auf. Im Report `.tmp/results/reports/checks_types_20260407_165332.log` meldet Pyright deshalb, dass die Config-Datei am Repo-Root nicht gelesen werden kann, Mypy `Cannot find config file 'mypy.ini'`, und der Task faellt mit `pyright=3`, `mypy=2` um, obwohl der gezielte Slice-Lauf fuer `app/api/{models,chat,sim}.py` plus zugehoerige Tests aktuell PASS liefert.
  - Ergebnis 2026-04-07: `scripts/checks_types.py` bindet Pyright und Mypy jetzt explizit an `novapolis_agent/pyrightconfig.json` und `novapolis_agent/mypy.ini` und fuehrt beide Kommandos mit `cwd=novapolis_agent` aus; `.vscode/tasks.json` startet denselben Wrapper wieder aus dem Repo-Root statt auf implizites CWD-Verhalten zu setzen. Der neue Report `.tmp/results/reports/checks_types_postflight_20260407_170654.md` zeigt `pyright=0` und `mypy=0`, und der anschliessende Full-Check `.tmp/results/reports/checks_report_20260407_171142.md` ist wieder komplett PASS.

- [x] [Jetzt] End-to-End-Produkt-Gate fuer das KI-geleitete Text-RPG v1 als reproduzierbaren Standardlauf definieren.
  - Ziel: Vor spaeteren Implementierungssprints braucht der Workspace einen klaren technischen Freigabepfad vom RP-Quellstand ueber Agent-Session und State-Logs bis zur Sim-/Replay-Sicht statt isolierter Einzelchecks.
  - Akzeptanzkriterien:
    1) ein kanonischer Lauf oder Task-Block baut den benoetigten Projektkontext, prueft den Agent-Session-Vertrag, validiert Log-/Replay-Artefakte und deckt den Sim-Produktpfad zumindest als Smoke ab,
    2) der Gate-Lauf scheitert hart bei OpenAPI-/Schema-Drift, fehlenden `world_log`/`pc_log`-Artefakten, ungueltigen `state_patches` oder Slot-/Replay-Widerspruechen,
    3) Runbook, Tasklabels und Board verwenden denselben Namen fuer diesen Produkt-Gate-Pfad,
    4) der Lauf liefert einen report- und release-tauglichen Kurzbeleg statt verteilter Einzelartefakte ohne Produktkontext.
  - Ergebnis 2026-04-06: `novapolis-dev/docs/process/text-rpg-product-gate-v1.ssot.md` fuehrt jetzt den kanonischen Gate-Namen `Text-RPG Product Gate v1`, die verbindlichen Gate-Stufen und den aktuellen operativen Task-Block `Checks: full` -> `Tests: pytest (api+streaming)` -> `Checks: sim epoch assets`; `novapolis_agent/docs/runbook.md` fuehrt denselben Gate-Block unter demselben Namen.
  - Evidenz: `novapolis_agent/docs/runbook.md` fuehrt Chat/Context-Bridge, Sim-Pruefablauf, TTS und Eval derzeit als getrennte Einzelablaeufe; `novapolis_agent/app/api/sim.py` liefert nur einen Minimalzustand, `novapolis-sim/scripts/Main.gd` erwartet statische Epoch-Logs statt eines geprueften End-to-End-Produktlaufs, und `novapolis-dev/docs/process/text-rpg-product-gate-v1.ssot.md` definiert jetzt den verbindlichen Gate-Rahmen.

- [x] [Jetzt] Nicht-kanonische Unterordner-READMEs auf unterscheidbare Dateinamen ziehen und Querverweise konsistent nachziehen.
  - Ziel: Aktive Unterordner-Dokumente sollen im Editor, in Suchtreffern und in Linklisten nicht mehr als austauschbare `README.md`-Treffer kollidieren, ohne die kanonischen Root-/Modul-Einstiege (`README.md` auf Root- und Modul-Ebene) zu verlieren.
  - Akzeptanzkriterien:
    1) nicht-kanonische aktive README-Dateien in Tool-/Runbook-/Stub-Unterordnern werden auf sprechende, unterscheidbare Dateinamen umgestellt,
    2) Root- und Modul-Einstiege (`README.md`, `novapolis-dev/README.md`, `novapolis_agent/README.md`, `novapolis-rp/README.md`, `novapolis-sim/README.md`) bleiben bewusst unveraendert,
    3) aktive Querverweise in README-Hub, Index, DONELOG, TODOs und betroffenen Fachdokus zeigen danach auf die neuen Dateinamen,
    4) Naming-Gate, Markdownlint und Frontmatter laufen fuer den geaenderten Doku-Scope gruen.
  - Evidenz: `novapolis-dev/docs/readme_decisions.md` und `novapolis-dev/docs/readme.hub.md` fuehren seit Laengerem mehrere Unterordner-READMEs als Stubs/Tool-Dokus, waehrend der aktive Workspace bis vor dem Umbau zahlreiche gleichnamige Dateien wie `novapolis_agent/scripts/scripts-overview.md`, `novapolis_agent/eval/eval-overview.md`, `docs/adr/adr-index.md`, `novapolis-rp/database-rp/06-scenes/scenes-guidelines.md` und `novapolis-rp/coding/tools/validators/validator-suite.md` in ihrer frueheren `README.md`-Form gleichzeitig fuehrte.
  - Abschluss 2026-03-30: Der aktive Stub-/Runbook-/Tool-Scope fuehrt jetzt sprechende Dateinamen (`adr-index.md`, `scripts-overview.md`, `eval-overview.md`, `logs-policy.md`, `validator-suite.md`, `raw-export-policy.md` u. a.); Querverweise in Hub, Index, DONELOG, TODOs, RP-Workflow und `.vscode/settings.json` sind nachgezogen. Bewusst unveraendert blieben die kanonischen Root-/Modul-Einstiege sowie fachliche RP-Landingpages unter `novapolis-rp/database-rp/01-factions/**`.

- [x] [Als naechstes] Stil- und Konsistenzlauf fuer Hochfrequenz-Dateien und die aktive Doku nach dokumentiertem Phasenplan ausfuehren.
  - Ziel: Vor einem breiten Sweep soll die aktive Dokumentoberflaeche mit einem festen Stilrahmen und einer festen Reihenfolge vereinheitlicht werden, statt wieder nur punktuell Drift zu reparieren.
  - Akzeptanzkriterien:
    1) die Hochfrequenz-Dateien werden als eigener Erst-Scope vor der restlichen Doku behandelt,
    2) aktive Doku und modulnahe Runbooks verwenden denselben Stilrahmen fuer Frontmatter, Pfade, Kommandos und Statusbegriffe,
    3) Archive und Quarantaene-Dateien bleiben bewusst ausserhalb des aktiven Sweep-Scope,
    4) der Abschlusslauf zieht TODO, DONELOG und Index im selben Lauf nach.
  - Evidenz: Die letzte Reader-Surface-Welle musste bereits sichtbare Inkonsistenzen in `README.md`, `WORKSPACE_INDEX.md`, `novapolis-dev/README.md`, den Modul-READMEs und `docs/todo.index.md` bereinigen; fuer den naechsten Schritt liegt der Arbeitsplan jetzt in `novapolis-dev/docs/process/doku-konsistenzlauf-aktive-surface-2026-03-28.md`.
  - Abschluss 2026-03-28: Hochfrequenz-Dateien, die zweite Schicht aktiver Dev-Doku sowie die ersten Modul-Runbooks (`novapolis_agent/scripts/scripts-overview.md`, `novapolis-rp/database-rp/06-scenes/scenes-guidelines.md`) fuehren jetzt denselben PASS-/PowerShell-/Root-Wrapper-Stil; beim Restscan blieben nur ignorierte Drittanbieter-READMEs unter `node_modules` ausserhalb des aktiven Scopes uebrig.

- [x] [Jetzt] Aktive Reader-Surface fuer Root/Dev und die vier Hauptmodule auf den aktuellen Single-Root-/PASS-Iststand ziehen.
  - Ziel: Die aktive Dokuoberflaeche soll nach den Maerz-Governance- und Modulfortschritten keine alten FAIL-Receipts, Alt-Kommandos oder Vor-Single-Root-Pfade mehr als aktuellen Stand fuehren.
  - Akzeptanzkriterien:
    1) `novapolis-dev/README.md`, `WORKSPACE_INDEX.md` und die vier Modul-READMEs referenzieren denselben aktiven Single-Root-/`.venv`-Pfad,
    2) aktive Lesedokumente zeigen keinen veralteten Gesamtstatus wie `overall=FAIL` mehr als aktuellen Iststand,
    3) veraltete `venv`-, Sibling- oder Bash-Pfade werden korrigiert oder klar als historische Beispiele markiert,
    4) Root-/Dev-/Modul-Backlogs bleiben danach ohne Truthfulness-Drift.
  - Evidenz: `novapolis-dev/README.md` und `WORKSPACE_INDEX.md` fuehren im Frontmatter noch FAIL-Receipts vom 2026-03-05 bzw. 2026-03-11; `novapolis_agent/README.md` nutzt weiter lokales `venv`, `novapolis-rp/README.md` spricht von `../novapolis_agent/`, und `novapolis-sim/README.md` fuehrt lokale Startpfade, die nicht sauber auf den aktuellen Root-Single-Root-Kontext einzahlen.
  - Abschluss 2026-03-28: Root-/Dev-/Modul-READMEs und `WORKSPACE_INDEX.md` fuehren jetzt durchgaengig den PASS-Kontext ohne alte FAIL-Receipts, nutzen den Root-`.venv`-Pfad konsistent und rahmen die bekannten Sim-Asset-Warnungen nicht mehr als unsichtbaren Widerspruch.

- [x] [Jetzt] Snapshot-Gate fuer alle betroffenen Markdown-Dateien erzwingen und Hook-Kommentar an den Gate-Iststand angleichen.
  - Akzeptanzkriterium: Geaenderte Markdown-Dateien koennen den Snapshot-Check nicht mehr dadurch umgehen, dass nur `stand` unveraendert bleibt; der Pre-Commit-Hook bezeichnet markdownlint nicht mehr als optional.
  - Evidenz: `scripts/snapshot_gate.py` uebersprang bisher Markdown-Dateien ohne `stand:`-Diff, obwohl der Inhalt geaendert wurde; `scripts/pre_commit.py` fuehrte markdownlint bereits als Pflicht-Gate, kommentierte es aber weiter als optional.
  - Abschluss 2026-03-27: Der `stand:`-Diff-Bypass ist entfernt, die Lock-Stand-Toleranz ist als benannte Konstante gefuehrt, der Hook-Kommentar ist bereinigt und ein Regressionstest deckt Gate-Verhalten sowie Hook-Reihenfolge gezielt ab.

- [x] [Jetzt] Kern-SSOT `.github/copilot-instructions.md` und Headings-Index auf denselben aktuellen Quellenstand ziehen.
  - Akzeptanzkriterium: `stand`/Quellenangaben in `.github/copilot-instructions.md` und `.github/copilot-instructions-headings.md` verweisen auf denselben aktuellen Governance-Stand; der Headings-Index ist im selben Lauf nachgezogen und nicht mehr historisch hinterher.
  - Evidenz: Die Kern-SSOT fuehrt weiterhin `Stand: 2026-02-27 10:57`, waehrend seitdem u. a. `R-SNAP` materiell geschaerft wurde; der Headings-Index referenziert noch einen aelteren Quellenstand.
  - Abschluss 2026-03-27: Kopfstand der Kern-SSOT und Quellenstand des Headings-Index zeigen jetzt denselben aktuellen Governance-Zeitanker; die strukturelle Abschnittsliste blieb dabei unveraendert korrekt.

- [x] [Jetzt] Redundanz in der Kern-Governance reduzieren und eine einzige normative Ebene fuer Regeln klar festziehen.
  - Akzeptanzkriterium: TL;DR, Landepunkte und Matrix widersprechen sich nicht mehr und doppeln keine Normtexte unnötig; klar benannt ist, welche Ebene fuer Runtime-Entscheidungen bindend ist.
  - Evidenz: Regeln wie `R-SNAP`, `R-LINT` und `R-LOG` liegen derzeit gleichzeitig in TL;DR, Regelindex, Landepunkten und Matrix vor; genau diese Mehrfachpflege hat schon zu Aktualitaetsdrift gefuehrt.
  - Abschluss 2026-03-27: TL;DR verweist nur noch auf Regel-IDs, die Kerndatei benennt die `Regel-ID-Landepunkte (Kern)` explizit als einzige normative Ebene, und die Matrix ist als abgeleitete Kurzreferenz gekennzeichnet.

- [x] [Als naechstes] Verbleibende Python-Workspace-Tasks systematisch von `shell` auf `process` pruefen und vereinheitlichen.
  - Akzeptanzkriterium: Python-basierte Tasks laufen konsistent ohne den lokalen `pwsh /d /c`-Shellpfad; Ausnahmen sind bewusst dokumentiert und technisch begruendet.
  - Evidenz: Zwar sind die kritischen Checks bereits auf `process` umgestellt, aber mehrere Python-Tasks wie `Checks: linters (all)`, `Tests: pytest (-q) [root]`, `Workspace tree: summary (dirs)` und die Eval-Suites laufen weiter als `shell`.
  - Abschluss 2026-03-27: Alle verbleibenden Python-basierten Workspace-Tasks in `.vscode/tasks.json` laufen jetzt als `process`; reine `pwsh`-Tasks fuer Tree-/HTTP-Aufrufe blieben bewusst als Shell-Tasks bestehen.

- [x] [Als naechstes] Snapshot-/Pre-Commit-Retry-Pfad operativ robust machen, nicht nur dokumentarisch.
  - Akzeptanzkriterium: Ein durch nachgelagerte Gates oder Auto-Fixes abgebrochener Commit fuehrt nicht mehr zu vermeidbarem Freshness-Churn; entweder wird der Retry-Pfad technisch abgefedert oder der Hook-Ablauf entsprechend umgestellt.
  - Evidenz: `scripts/pre_commit.py` startet mit dem Snapshot-Gate vor Markdownlint/Frontmatter/RP-Gates, waehrend `scripts/snapshot_gate.py` weiter auf `±5 min` plus engen Lock-Stand-Abstand prueft; dadurch bleibt Retry-Faelligkeit systemisch moeglich.
  - Abschluss 2026-03-27: `scripts/pre_commit.py` fuehrt das Snapshot-Gate jetzt erst nach markdownlint, Frontmatter-Validator und optionalen RP-Hard-Gates aus; spaete Abbrueche oder Auto-Fixes verbrauchen damit die Freshness nicht mehr vorzeitig.

- [x] [Jetzt] Board-Metadaten im `novapolis-dev/docs/todo.index.md` gegen die aktuellen Board-Staende haerten.
  - Akzeptanzkriterium: `letzte Aenderung`, Open-Counts und `aeltester offener Punkt` spiegeln `todo.dev.md`, `todo.rp.md`, `todo.agent-board.md` und `todo.sim.md` ohne manuelle Nachpflege oder sichtbare Datumsdrift.
  - Evidenz: `novapolis-dev/docs/todo.index.md` zeigt aktuell fuer Agent/Sim/RP noch aeltere `letzte Aenderung`-Werte (`2026-03-11` bzw. `2026-03-05`), obwohl die Boards bereits auf `stand: 2026-03-27 01:16` stehen.
  - Abschluss 2026-03-27: `scripts/check_todo_index_sync.py --write-index-meta` zieht die automationsrelevanten Board-Metadaten jetzt wieder konsistent nach; der offene Driftpunkt ist geschlossen.

- [x] [Jetzt] Governance- und Task-Pfad fuer Snapshot-Retrys sowie Python-Checks gegen den realen Lauf haerten.
  - Akzeptanzkriterium: Snapshot-Regeln benennen die effektive Frischelogik fuer Retry-Faelle explizit und die betroffenen Python-Tasks laufen nicht mehr ueber den fehlerhaften lokalen `pwsh /d /c`-Shellpfad.
  - Evidenz: `.github/copilot-instructions.md` (R-SNAP), `.github/instructions/docs-markdown.instructions.md` (Ausnahme GOV-EX-FM-001), `.vscode/tasks.json` (`process` statt `shell` fuer Python-Checks).
  - Abschluss 2026-03-27: Snapshot-/Retry-Regeln und Task-Definitionspfad sind auf den beobachteten Iststand synchronisiert; Coverage-, TODO-Index- und Logs-Checks koennen lokal wieder ueber die Workspace-Tasks ohne Shell-Wrapping laufen.

- [x] [Jetzt] Full-Gate wieder gruen machen (`ruff`, `black`, `pytest/coverage >= 80`) und den aktuell roten Sammellauf stabilisieren.
  - Akzeptanzkriterium: `scripts/run_checks_and_report.py` liefert `overall=PASS` mit Reportpfad und ohne rote Pflichtchecks.
  - Evidenz: `.tmp/results/reports/checks_report_20260311_072150.md`.
  - Abschluss 2026-03-11: Full-Gate wieder gruen; Coverage-Gate `>=80%` wieder erreicht (aktueller Lauf: `80.45%`).
- [x] [Jetzt] Coverage-Sprint Richtung `91%` starten (Welle 1: skriptnahe Low-Coverage-Module).
  - Akzeptanzkriterium: Nettoanstieg der Gesamt-Coverage gegen Baseline (`76.24%`) ist messbar dokumentiert und die Wellenplanung fuer die naechsten Hauptluecken steht.
  - Evidenz: neue/erweiterte Tests in `novapolis_agent/tests/scripts/` plus Coverage-Report `.tmp/results/reports/checks_report_20260318_052318.md` (`93.69%`; Uplift gegen Baseline `76.24%`).
  - Abschluss 2026-03-18: Der Welle-1-Scope hat den Zielkorridor bereits ueberschritten; verbleibende Testausbauten laufen nicht mehr als akuter Gate-Blocker, sondern als normale Qualitaetshygiene.
- [x] [Als naechstes] Modernes Community-/Maintainer-Doku-Paket ergaenzen (`SUPPORT.md`, Issue-/PR-Templates, `RELEASE.md`, `GOVERNANCE.md` oder `MAINTAINERS.md`).
  - Akzeptanzkriterium: Einstieg, Meldewege und Release-/Maintainer-Prozess sind fuer externe Contributors ohne implizites Wissen auffindbar.
  - Evidenz: `SUPPORT.md`, `RELEASE.md`, `MAINTAINERS.md`, `.github/ISSUE_TEMPLATE/`, `.github/pull_request_template.md`, `README.md`.
  - Abschluss 2026-03-18: Root-Community-Oberflaeche ist jetzt vollstaendig verlinkt; der naechste offene Dev-Punkt bleibt die KPI-Trendansicht.
- [x] [Als naechstes] ADR-Ordner von "bereit" auf "aktiv genutzt" heben (mind. `ADR-0001`, `ADR-0002`).
  - Akzeptanzkriterium: zentrale Entscheidungen (z. B. DONELOG-Ebenen, Quality-Gate-Sequenz) sind als akzeptierte ADRs dokumentiert.
  - Evidenz: `docs/adr/0001-donelog-ebenen.md`, `docs/adr/0002-quality-gate-sequenz.md`, `docs/adr/adr-index.md`.
  - Abschluss 2026-03-18: Der ADR-Ordner enthaelt jetzt zwei akzeptierte Grundsatzentscheidungen und wird aktiv als Governance-Ablage genutzt.
- [x] [Jetzt] Punkt-3-Strategie aktivieren: Coverage-Steuerung auf realistische Zielkorridore (`85-90%`) fuer grosse Pfade umstellen und `90%` als verbindliches Qualitaetsziel fest verankern.
  - Akzeptanzkriterium: dokumentierte Gate-Logik mit Hard-Gate (`>=80%`) plus verbindlichem Qualitaetsziel (`>=90%`) inkl. Nachweispflicht bei Unterschreitung.
  - Evidenz: `novapolis-dev/docs/tests.md` (Abschnitte `Gate-Logik` und `Coverage-Strategie`).
- [x] [Spaeter] Root-Backlog O11 schliessen: externes Beta-Installblatt fuer Dritte erstellen und mit Dev-Hub synchronisieren.
  - Akzeptanzkriterium: ein Dritter kann Setup/Run/Troubleshooting fuer die Standalone-Beta ohne Insiderwissen ausfuehren.
  - Evidenz: `novapolis-dev/docs/process/standalone-beta-installblatt.md`, `README.md`, `todo.root.md`.
  - Abschluss 2026-03-18: Das Installblatt deckt Voraussetzungen, Setup, Start, Verifikation, Go/No-Go und Troubleshooting in externer Leserperspektive ab.
- [x] [Spaeter] Cadence-KPI-Review als Trendansicht verankern (nicht nur Einzelwerte je Slot).
  - Akzeptanzkriterium: KPI-Verlauf (4 Kernmetriken) ist fuer mindestens 4 aufeinanderfolgende Slots vergleichbar dokumentiert.
  - Evidenz: `novapolis-dev/docs/meta/dev-kpi-trends.md`.
  - Abschluss 2026-03-19: Die vier Kernmetriken (`todo_index_drift`, `active_docs_stale`, `placeholder_conflicts`, `logs_policy_violations`) sind ueber vier dokumentierte Slots in einer dedizierten Trendansicht vergleichbar zusammengefuehrt.

- [x] [Jetzt] Active-Surface-Index fuer `novapolis-dev/docs/**` erstellen (ACTIVE/REFERENCE/HISTORICAL + Owner + last_check).
  - Akzeptanzkriterium: Eine scanbare Uebersicht mit klarer Klassifikation aller aktiven Dev-Dokumente liegt vor.
  - Evidenz: `novapolis-dev/docs/active-surface-index.md`.
- [x] [Jetzt] Truthfulness-Drift in `novapolis-dev/README.md` korrigieren (u. a. `integrations/` nicht mehr als Platzhalter; `roadmaps/` nur bei realem Verzeichnis).
  - Akzeptanzkriterium: Strukturabschnitt beschreibt ausschliesslich den Iststand.
  - Evidenz: `novapolis-dev/README.md` (Struktur/Primary-Docs-Abschnitt).
- [x] [Jetzt] `novapolis-dev/docs/specs/tts-exporter-coqui.md` auf Iststand nachziehen (Platzhalter-Narrativ entfernen, Implementierungsgrad explizit markieren).
  - Akzeptanzkriterium: Keine Widersprueche mehr zwischen Spec, Tasking und Modul-Iststand.
  - Evidenz: `novapolis-dev/docs/specs/tts-exporter-coqui.md` (CLI Iststand + Task-Status).
- [x] [Als naechstes] Donelog-Hygiene einfuehren: aktives Fenster definieren (Current-Window) und aeltere Bloecke sauber ins Historik-Archiv auslagern.
  - Akzeptanzkriterium: `novapolis-dev/docs/donelog.md` bleibt fuer operative Arbeit kurz und scanbar; Historie bleibt erhalten.
  - Evidenz: `novapolis-dev/docs/donelog.md` (Current-Window), `novapolis-dev/archive/docs/donelogs/donelog_dev.window-archive.pre-2026-02-20.md` (Archivfenster).
- [x] [Als naechstes] Logs-Policy fuer `novapolis-dev/logs/` durchsetzen (Umgang mit `*.tmp.md` festlegen und konsistent umsetzen).
  - Akzeptanzkriterium: Keine policy-widrigen Rohlogs im aktiven Log-Pfad oder Policy explizit angepasst und dokumentiert.
  - Evidenz: `scripts/check_logs_policy.py`, `novapolis-dev/logs/logs-policy.md`, Verschiebung nach `novapolis-dev/archive/quarantine/logs/`.
- [x] [Als naechstes] Stand-Freshness-SLA festlegen (`ACTIVE <= 14 Tage`, `REFERENCE <= 60 Tage`) und als wiederkehrenden Check im Dev-Modul verankern.
  - Akzeptanzkriterium: Alle aktiven Dev-Dokumente haben frische `stand`-Werte oder dokumentierte Ausnahmen.
  - Evidenz: `scripts/check_doc_freshness.py`, `novapolis-dev/docs/active-surface-index.md`, Integration in `scripts/run_checks_and_report.py`.
- [x] [Spaeter] TODO-Index-Sync automatisiert absichern (Check/Guard: bei Aenderung von `todo.*.md` muss `todo.index.md` im selben Lauf geaendert sein).
  - Akzeptanzkriterium: Drift zwischen Modul-Boards und `todo.index.md` wird technisch verhindert statt nur manuell entdeckt.
  - Evidenz: `scripts/check_todo_index_sync.py`, Integration in `scripts/run_checks_and_report.py`.
- [x] [Spaeter] Woechentliche Hygiene-Cadence etablieren (Drift-Scan, Donelog-Cleanup, TODO/Index-Abgleich) inkl. KPI-Tracking.
  - Akzeptanzkriterium: Fester 60-Minuten-Wochenslot mit dokumentierten KPIs (`todo_index_drift`, `active_docs_stale`, `placeholder_conflicts`, `logs_policy_violations`).
  - Evidenz: `novapolis-dev/docs/process/abschluss-routine.ssot.md` (Abschnitt `Woechentliche Hygiene-Cadence (60 Minuten)` + KPI-Protokollschema).


