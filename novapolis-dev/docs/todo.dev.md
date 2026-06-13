---
stand: 2026-06-13 07:14
update: Das Dev-Board fuehrt jetzt die Mini-first-Regel: GPT-5 mini muss die credits-effiziente Vorarbeit maximal leisten, bevor ein reviewbarer GPT-5.3-Codex-Handoff angeboten wird.
checks: snapshot-lock PASS (2026-06-13 07:10); npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc changed-dev-md PASS (2026-06-13 07:08); C:/Users/FloAu/AppData/Local/Programs/Python/Python313/python.exe scripts/check_frontmatter.py changed-dev-md PASS (EXITCODE=0, 2026-06-13 07:08); C:/Users/FloAu/AppData/Local/Programs/Python/Python313/python.exe scripts/check_todo_index_sync.py PASS (2026-06-13 07:08).
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

- [ ] [Jetzt] Governance- und Behavior-Leitplanken auf credits-optimierte Modellnutzung umstellen.
  - Ziel: Arbeitsmodus fuer die aktuelle Modelltendenz explizit und reproduzierbar in Governance-/Behavior-Dokus verankern: `GPT-5 mini` ist der verpflichtende Default fuer Befund, Planung, Suche, Diff-Review, Check-Auswertung und Handoff-Vorbereitung; `GPT-5.3-Codex` darf erst nach belegter Mini-Ausschoepfung als reviewbarer Handoff fuer praezise Umsetzungs-/Abschlusslaeufe angeboten werden.
  - Akzeptanzkriterien:
    1) Ein Dev-Plan unter `novapolis-dev/docs/process/` fuehrt Scope, Rollout und Guardrails fuer credits-effiziente Modellwahl.
    2) Alle unmittelbar betroffenen Governance-/Behavior-Dateien sind vor Implementierung explizit erfasst.
    3) Die Umstellung bleibt minimalinvasiv (keine fachfremden Nebenbaustellen).
    4) Die Policy erzwingt Mini-first vor Codex: Scope, betroffene Dateien, Risiko, offene Frage und konkrete Codex-Aufgabe muessen mit `GPT-5 mini` vorbereitet sein, bevor ein Codex-Handoff erscheint.
    5) Codex-Handoffs bleiben standardmaessig reviewbar (`send:false`/kein Auto-Submit); `send:true` ist nur mit ausdruecklicher Begruendung erlaubt.
    6) `todo.dev.md`, `todo.index.md` und `novapolis-dev/docs/donelog.md` fuehren denselben Startstand im selben Lauf.
  - Evidenz: Scope- und Befunddateien sind vorhanden und explizit erfasst: `.github/copilot-instructions.md`, `.github/instructions/*.instructions.md`, `.github/agents/novapolis-workspace-navigator.agent.md`, `.github/agents/novapolis-rp-szenenlabor.agent.md`, `.github/hooks/rp-runtime-loop-guard.json`, `.vscode/settings.json`, `novapolis-dev/docs/copilot-vscode-usage.md`, `novapolis-dev/docs/process/model-credits-optimization-plan.ssot.md`, `novapolis-dev/docs/process/vscode-agent-governance-surface.ssot.md`, `novapolis-dev/docs/donelog.md`, `novapolis-dev/docs/todo.dev.md` und `novapolis-dev/docs/todo.index.md`. Online-Faktenlage 2026-06-13: GitHub Copilot usage-based billing rechnet nach Modell plus Input-/Output-/Cached-Tokens; in der offiziellen Preistabelle kostet `GPT-5.3-Codex` gegenueber `GPT-5 mini` je Tokenart rund 7x mehr (`mini`: 0.25/0.025/2.00 USD pro 1M Input/Cached/Output; `Codex`: 1.75/0.175/14.00 USD). Legacy-Multiplikatoren bestaetigen die Richtung (`mini` 0.33, `GPT-5.3-Codex` 6), sind aber nicht die Primaerlogik fuer usage-based billing. VS-Code-Handoffs sind als reviewbare Uebergaenge gedacht; `send:false` laesst den Prompt vorgefuellt, `send:true` sendet automatisch.

  Geplanter, mehrstufiger Umsetzungsplan (zu protokollieren und schrittweise abzuhaken):

  - Phase 0 — Baseline, Hook-Risiko & Befund (Evidenzaufnahme)
    - Aufgabe: Reproduzierbare Ist-Aufnahme erstellen: geladene Instructions/Agents/Hooks/Prompt-Files, `chat`-Settings, Hook-Logs, aktuelle TODO/DONELOG-Eintraege; Hook-Risiken vor Policy-/Settings-Umbau zuerst bewerten.
    - Akzeptanz: Befund-Block in `novapolis-dev/docs/donelog.md` oder `process/*.ssot.md` abgelegt.

  - Phase 1 — Zielvertrag (Dev-SSOT)
    - Aufgabe: Soll-Vertrag in `novapolis-dev/docs/process/model-credits-optimization-plan.ssot.md` erweitern (Logging-Waechter-Rollen, Mini-first-Pflicht, Modell-Eskalation `GPT-5 mini` -> `GPT-5.3-Codex` nur nach belegter Ausschoepfung, Handoff-Policy, Kontextbudget).
    - Akzeptanz: Vertragstext steht, Review-Checklist und Akzeptanzkriterien stehen im Dev-Board.

  - Phase 2 — Logging-Wächter härten (Agent-Datei)
    - Aufgabe: `.github/agents/novapolis-workspace-navigator.agent.md` konkretisieren: `mini-first.required=true`, `model-escalation`, `codex-handoff.requires=escalation-evidence`, `handoff.default=review`, `handoff.send=false`, `max-context-tokens`, `stop-early-rules`, `diagnostics.level`.
    - Akzeptanz: Agent-Frontmatter & Text konkret; Tests: Chat Diagnostics zeigen gewuenschtes Laden/Verhalten; Codex-Handoff erscheint erst nach Mini-Befund mit Scope, Dateien, Risiko, offener Frage und konkreter Codex-Aufgabe.

  - Phase 3 — Root-Governance synchronisieren
    - Aufgabe: Nur notwendige Klarstellungen in `.github/copilot-instructions.md` vornehmen, keine Ausweitung der Scope.
    - Akzeptanz: Keine Widersprueche zwischen Root-SSOT und Agent-Policy.

  - Phase 4 — VS-Code-Settings (wenn nötig)
    - Aufgabe: Optionales Hinzufuegen von `chat.instructionsFilesLocations`, `chat.agentFilesLocations`, `chat.promptFilesLocations` oder `chat.hookFilesLocations` in `.vscode/settings.json` — nur wenn es Drift reduziert.
    - Akzeptanz: Settings-Change dokumentiert, lokal getestet, kein Konflikt mit User/Org-Instructions.

  - Phase 5 — Hooks auditieren
    - Aufgabe: Aus Phase 0 belegte Hook-Befunde fuer `.github/hooks/rp-runtime-loop-guard.json` und weitere Hooks auf `timeout`, `stop-loop`-Risiken und `send:true`-Folgen pruefen; ggf. minimal patchen.
    - Akzeptanz: Hook-Logs zeigen keine Stop-Loops; PreToolUse/PostToolUse verhalten sich erwartbar.

  - Phase 6 — Konsistenz- und Verifikationslauf
    - Aufgabe: Vollständiger Konsistenzcheck: Agent-Dateien vs Root-SSOT vs Dev-SSOT vs TODO/DONELOG vs Settings vs Hook-Logs.
    - Akzeptanz: Alle Checks grün; Abweichungen dokumentiert und priorisiert.

  - Phase 7 — Staged Rollout & Monitoring
    - Aufgabe: Rollout in kleinen Commits; nach jeder Phase: Lint, Frontmatter, TODO-Index-Sync, Snapshot-Lock und prägnanter Postflight-Receipt in DONELOG.
    - Akzeptanz: Rollback-Pfade, Monitoring-Checks, und Board-Status aktualisiert.

  - Sonstige Hinweise
    - Hooks zuerst auditieren; Hooks sind die hauptkritische Credit-Risikoquelle.
    - Mini-first ist Pflicht: breite Suche, Befund, Planung, Diff-Review, Check-Auswertung und Handoff-Prompt werden zuerst mit `GPT-5 mini` erledigt.
    - Zulassige Codex-Eskalationsgruende: konkurrierende Architekturwege, zentrale Governance-/Agent-/Hook-Policy, hohes Regressionsrisiko, widerspruechliche Checkbefunde oder Abschlusspruefung mit besonders hoher Praezisionsanforderung.
    - Nicht ausreichend fuer Codex: viele Dateien allein, reine Zusammenfassung, Board-/Index-/DONELOG-Pflege, Lint-Auswertung oder ein unspezifisches "zur Sicherheit".
    - `send:true` nur mit ausdruecklicher Begruendung; Handoffs standardmaessig `review`/`send:false`.
    - Jede Aenderung einzeln committen und mit Snapshot-Lock/Freshness pruefen.

Abgeschlossene Eintraege (Bestand)
----------------------------------

- [x] [Jetzt] Einen expliziten lokalen Workspace-Baum neben den drei überwachten Tree-Artefakten einfuehren.
  - Ziel: Neben `workspace_tree.txt`, `workspace_tree_dirs.txt` und `workspace_tree_full.txt` soll ein vierter Tree klar den lokalen On-Disk-Zustand abbilden, ohne den Default-Freshness-Gate der drei kanonischen Trees wieder zu verwischen.
  - Akzeptanzkriterien:
    1) `scripts/update_workspace_tree_dirs.py` erzeugt ein separates lokales Tree-Artefakt mit klarem Namen,
    2) der neue lokale Baum ist bewusst nicht Teil des Default-Freshness-Gates,
    3) es gibt einen kanonischen Task und repo-lesbare Doku, die den Unterschied zwischen überwachten Trees und lokalem Baum klar machen,
    4) Board, Index und DONELOG fuehren denselben Abschluss im selben Lauf.
  - Evidenz: Der aktuelle Vierer-Split fehlte noch: `workspace_tree_full.txt` ist inzwischen wieder deterministisch repo-sichtbar und überwacht, bildete aber nicht mehr den echten lokalen Maschinenbaum mit `.snapshot.now`, `.venv`, `.tmp` und ähnlichen lokalen Artefakten ab.
  - Ergebnis 2026-04-28 13:15: `scripts/update_workspace_tree_dirs.py` erzeugt jetzt zusätzlich `workspace_tree_local.txt` als expliziten lokalen Maschinenbaum über den neuen Modus `local-full`. Der neue Baum bleibt bewusst außerhalb von `snapshot_outputs()` und damit außerhalb des Default-Freshness-Gates der drei kanonischen Trees. `.vscode/tasks.json`, `README.md` und `WORKSPACE_INDEX.md` führen denselben Vierer-Split jetzt repo-lesbar, und der vollständige Tree-Testpfad bleibt nach dem Refresh aller Tree-Artefakte grün.

- [x] [Jetzt] `workspace_tree_full.txt` wieder in den Default-Freshness-Gate aufnehmen, ohne Ignore-Drift mitzuschleppen.
  - Ziel: Alle drei Workspace-Trees sollen wieder standardmaessig auf Freshness geprueft werden, aber der Vollbaum darf dabei nicht mehr von `.snapshot.now`, `.venv`, `.tmp` oder anderen ignore-basierten Laufartefakten kippen.
  - Akzeptanzkriterien:
    1) `scripts/update_workspace_tree_dirs.py` erzeugt den Vollbaum deterministisch aus repo-sichtbaren Pfaden statt aus maschinenlokalem Junk,
    2) `stale_snapshot_paths()` prueft standardmaessig wieder `workspace_tree.txt`, `workspace_tree_dirs.txt` und `workspace_tree_full.txt`,
    3) der Testpfad deckt ab, dass `workspace_tree_full.txt` wieder Teil des Default-Gates ist und ignore-basierte Volatilitaet wie `.snapshot.now` nicht in den Vollbaum gelangt,
    4) Board, Index und DONELOG fuehren denselben Abschluss im selben Lauf.
  - Evidenz: Der billige Gegencheck gegen `stale_snapshot_paths(..., include_forensic_full=True)` meldete im aktuellen Stand bereits `workspace_tree_full.txt` als stale; zugleich enthielt der committed Vollbaum maschinenlokale Ignore-Pfade wie `.snapshot.now`, `.tmp`, `.venv` und `coverage.xml`, die den Default-Freshness-Gate instabil machten.
  - Ergebnis 2026-04-28 12:53: `scripts/update_workspace_tree_dirs.py` rendert `workspace_tree_full.txt` jetzt deterministisch aus `git ls-files --cached --others --exclude-standard` statt aus dem rohen Maschinenbaum. Damit bleiben repo-sichtbare Pfade erhalten, waehrend ignore-basierte Volatilitaet wie `.snapshot.now`, `.venv`, `.tmp` und `coverage.xml` aus dem Vollbaum herausfaellt. `stale_snapshot_paths()` prueft standardmaessig wieder alle drei Tree-Artefakte, `novapolis_agent/tests/scripts/test_update_workspace_tree_dirs.py` deckt die Rueckkehr von `workspace_tree_full.txt` in den Default-Gate plus die neue Volatilitaetsregel ab, und `workspace_tree_full.txt` ist mit dem neuen Renderer neu erzeugt.

- [x] [Jetzt] Aktive Workspace-Trees auf tracked Repo-Inhalt statt Reader-Surface-Sonderfiltern zurueckziehen.
  - Ziel: `workspace_tree.txt` und `workspace_tree_dirs.txt` sollen kuenftig alle getrackten Repo-Pfade zeigen und nur noch ignorierte Maschinenartefakte ausblenden.
  - Akzeptanzkriterien:
    1) `scripts/update_workspace_tree_dirs.py` entfernt die zusaetzlichen Reader-Surface-Sonderausschluesse aus der aktiven Tree-Policy,
    2) der Testpfad belegt, dass getrackte Repo-Pfade aus `novapolis-dev/archive`, `novapolis-rp/database-raw` und `novapolis-rp/database-curated` in der aktiven Tree-Surface wieder erscheinen,
    3) ignorierte Artefakte wie `coverage.xml` bleiben weiterhin ausserhalb der aktiven Trees,
    4) Board, Index und DONELOG fuehren denselben Abschluss im selben Lauf.
  - Evidenz: `scripts/update_workspace_tree_dirs.py` fuehrte aktive Reader-Surface-Sonderfilter fuer getrackte Repo-Pfade wie `novapolis-dev/archive`, `novapolis-rp/database-raw` und `novapolis-rp/database-curated`, obwohl die gewuenschte Regel fuer aktive Trees auf "alles Getrackte sichtbar, nur ignorierte Maschinenartefakte ausgeblendet" zielt.
  - Ergebnis 2026-04-28 12:52: `scripts/update_workspace_tree_dirs.py` fuehrt in aktiven Trees nur noch Ignore-basierte Maschinenartefakt-Excludes plus lokale Repo-Metadatenpfade wie `.git` und `.tox`; die Reader-Surface-Sonderfilter sind entfernt. `novapolis_agent/tests/scripts/test_update_workspace_tree_dirs.py` prueft jetzt explizit, dass getrackte Repo-Pfade aus `novapolis-dev/archive`, `novapolis-rp/database-raw` und `novapolis-rp/database-curated` in aktiver Tree- und Directory-Sicht sichtbar bleiben, waehrend ignorierte Artefakte wie `coverage.xml` weiterhin ausgeschlossen sind. `workspace_tree.txt` und `workspace_tree_dirs.txt` sind auf dieser Basis neu erzeugt.

- [x] [Jetzt] Tree-Skip-Policy gegen gitignore spiegeln und feste Drift-Regel verankern.
  - Ziel: Die aktive Tree-Surface soll ignorierte Maschinenpfade nicht still wieder sichtbar machen; gitignore-relevante Skip-Klassen muessen explizit gespiegelt werden, und zusaetzliche Reader-Surface-Ausnahmen muessen als bewusst getrennte Regel statt als implizite Mischliste lesbar sein.
  - Akzeptanzkriterien:
    1) `scripts/update_workspace_tree_dirs.py` trennt gitignore-abgeleitete Skip-Klassen nachvollziehbar von zusaetzlichen Reader-Surface-Ausnahmen,
    2) der Tree-Skript-/Testpfad deckt mindestens die belegten Driftfaelle `novapolis_agent/coverage.xml` und weitere relevante Ignore-Klassen gegen Regression ab,
    3) es gibt eine feste, repo-lesbare Regel, dass aktive Trees gitignore-relevante Maschinenartefakte spiegeln und Reader-Surface-Zusatzfilter explizit getrennt fuehren,
    4) Board, Index und DONELOG fuehren denselben Abschluss im selben Lauf.
  - Evidenz: `workspace_tree.txt` fuehrte `novapolis_agent/coverage.xml`, obwohl Root-`.gitignore` und `novapolis_agent/.gitignore` `coverage.xml` ignorieren; zugleich mischte `scripts/update_workspace_tree_dirs.py` gitignore-nahe Pfade wie `.venv` und `outputs` mit bewusst staerkeren Reader-Surface-Ausnahmen wie `novapolis-dev/archive` oder `novapolis-rp/database-curated`, ohne diese Policy explizit zu trennen.
  - Ergebnis 2026-04-28 12:18: `scripts/update_workspace_tree_dirs.py` trennt die Policy jetzt explizit in `ACTIVE_GITIGNORE_SKIP_*` und `ACTIVE_READER_SURFACE_ONLY_*`. Der Test `novapolis_agent/tests/scripts/test_update_workspace_tree_dirs.py` deckt sowohl den Freshness-Check als auch die Policy-Regel fuer gitignore-gespiegelte Klassen und bewusst getrennte Reader-Surface-Extras ab. `workspace_tree.txt` und `workspace_tree_dirs.txt` sind danach mit der neuen Skip-Policy neu erzeugt; ignorierte Artefakte wie `novapolis_agent/coverage.xml` tauchen damit nicht mehr still in der aktiven Tree-Surface auf.

- [x] [Jetzt] Root-Tree-Artefakte aktualisieren und gegen kuenftige Drift testseitig absichern.
  - Ziel: `workspace_tree.txt`, `workspace_tree_dirs.txt` und `workspace_tree_full.txt` sollen wieder den aktuellen Repo-Stand spiegeln, und die Testsuite soll kuenftig automatisch melden, wenn die committed Trees vom frisch generierten Stand abweichen.
  - Akzeptanzkriterien:
    1) alle drei Root-Tree-Artefakte sind neu erzeugt und enthalten auch die seit dem letzten Lauf hinzugekommenen Dateien,
    2) `scripts/update_workspace_tree_dirs.py` bietet einen testbaren Pfad fuer die inhaltliche Frischepruefung statt nur Side-Effect-Schreiben,
    3) ein neuer pytest-Test faellt bei Tree-Drift reproduzierbar rot und bleibt im frischen Stand gruen,
    4) Board, Index und DONELOG fuehren denselben Abschluss im selben Lauf.
  - Evidenz: Die aktuellen Tree-Artefakte trugen LastWriteTime `2026-04-18 01:47`, waehrend spaeter angelegte Dateien wie `.github/hooks/rp-runtime-loop-guard.json`, `scripts/rp_runtime_loop_guard.py` und `novapolis-rp/database-curated/staging/rp-runtime/mind/README.md` im committed Vollbaum fehlten.
  - Ergebnis 2026-04-28 11:50: `scripts/update_workspace_tree_dirs.py` fuehrt jetzt testbare Render-Helfer und einen Drift-Check ueber `stale_snapshot_paths()`. Der neue pytest-Slice `novapolis_agent/tests/scripts/test_update_workspace_tree_dirs.py` meldet stale Trees reproduzierbar rot und bleibt nach dem echten Refresh gruen. `workspace_tree.txt`, `workspace_tree_dirs.txt` und `workspace_tree_full.txt` sind im selben Lauf neu erzeugt und tragen wieder den aktuellen Workspace-Stand.

- [x] [Als naechstes] README-Nachzug auf den verifizierten Minimalumfang begrenzen.
  - Ziel: Der naechste Arbeitslauf soll nur den belegten kaputten Link im Workspace-Index korrigieren und den veralteten Zukunftssatz in `readme_decisions.md` auf den heutigen Iststand ziehen, ohne die bestehende README-Hierarchie neu umzubauen.
  - Akzeptanzkriterien:
    1) `WORKSPACE_INDEX.md` ersetzt den falschen Verweis `packages/novapolis_common/README.md` durch den realen Einstieg `packages/README.md`,
    2) `novapolis-dev/docs/readme_decisions.md` fuehrt den veralteten Phase-2-Zukunftssatz zu `WORKSPACE_INDEX.md` nicht mehr als offenen Zukunftspunkt,
    3) ein kleiner Root-Skripte-Landing-Block in `WORKSPACE_INDEX.md` wird nur dann aufgenommen, wenn er fuer den operativen Einstieg wirklich einen Mehrwert liefert,
    4) alle anderen README-, Index- und Hub-Strukturen bleiben unangetastet.
  - Evidenz: Der belegte aktive Phantom-Link sitzt in `WORKSPACE_INDEX.md`; die Driftstelle steht in `novapolis-dev/docs/readme_decisions.md`, waehrend `WORKSPACE_INDEX.md` und `novapolis-dev/docs/todo.dev.md` den Reader-Surface-Nachzug bereits als Iststand fuehren.
  - Ergebnis 2026-04-28 08:26: `WORKSPACE_INDEX.md` verweist fuer die gemeinsame Paketlage jetzt auf `packages/README.md`, und `novapolis-dev/docs/readme_decisions.md` fuehrt den Workspace-Index nicht mehr als offenen Phase-2-Verkuerzungspunkt. Ein zusaetzlicher Root-Skripte-Landing-Block wurde bewusst nicht aufgenommen, weil der bestehende Root-Steuerpfad ueber `README.md`, `WORKSPACE_STATUS.md` und `.vscode/tasks.json` bereits den operativen Einstieg abdeckt.

- [x] [Jetzt] Den Doc-Freshness-Scope von einem Dev-Subset auf einen workspaceweiten, moduluebergreifenden Pruefrahmen ziehen.
  - Ziel: Ein gruener Freshness-Lauf soll nicht laenger still nur den Dev-Hub meinen, sondern die fuehrenden Doku- und Navigationspfade aus Root, Governance, Agent, RP, Sim und den Tree-Artefakten abdecken.
  - Evidenz: `scripts/check_doc_freshness.py` leitete den Scope zuvor ausschliesslich aus `novapolis-dev/docs/active-surface-index.md` ab und uebersprang Wildcards bewusst. Der belegte Lauf meldete daher nur `checked_docs=14`, obwohl der Workspace-Audit-Rahmen in `novapolis-dev/docs/process/workspace-audit-segmente.ssot.md` Root, Dev, Agent, RP, Sim und W7-Flaechen explizit fuehrt.
  - Ergebnis 2026-04-28 01:17: `scripts/check_doc_freshness.py` liest den Scope jetzt aus `novapolis-dev/docs/meta/doc-freshness-scope.md`, expandiert die dort hinterlegten Globs zu konkreten Dateien und unterstuetzt `frontmatter`, `legacy-header` und `mtime` als Frischequellen. Der aktuelle Lauf deckt damit `scope_rows=46`, `expanded_glob_rows=12` und `checked_docs=262` ohne Findings ab. `novapolis-dev/docs/active-surface-index.md` bleibt dabei bewusst die Dev-Hub-Klassifikation und nicht mehr die versteckte Workspace-Scope-Quelle.

- [x] [Jetzt] Den kleinen Audit-Rest aus aktiver Doku-Portabilitaet und Python-Stil wieder auf einen gemeinsamen Gruenstand ziehen.
  - Ergebnis 2026-04-23 23:50: `todo.root.md` fuehrt wieder den aktuellen Modulstand statt des veralteten Kurzstatus. `novapolis-dev/docs/todo.sim.md` beschreibt die lokal laufende Godot-Binary jetzt portabel ohne hostgebundenen Pfad. `novapolis_agent/scripts/training_release_gate.py`, `scripts/check_sim_hub_prefs_contract.py`, `scripts/run_sim_export_smoke.py` sowie der betroffene Testsatz unter `novapolis_agent/tests/scripts/` sind wieder Ruff-/Black-konform.
  - Verifikation 2026-04-23 23:50: Der enge Script-Testscope fuer `test_check_sim_hub_prefs_contract.py`, `test_run_sim_export_smoke.py`, `test_run_sim_headless_verify.py` und `test_training_release_gate.py` ist PASS. `scripts/check_portable_paths.py --repo-root .`, `python -m ruff check novapolis_agent scripts`, `python -m black --check novapolis_agent scripts` und der kanonische Voll-Lauf `scripts/run_checks_and_report.py` gegen `.tmp/results/reports/checks_report_20260423_234820.md` sind ebenfalls PASS. Damit steht das Dev-Board wieder bei `offen: 0`.

- [x] [Jetzt] Workspace-Audit-Segmente `W2` und `W5` auf kanonische Task- oder Sammelcheck-Einstiege ziehen.
  - Ziel: Bereits vorhandene Governance- und Audit-Skripte sollen nicht nur lose im Repo liegen, sondern ueber dieselben kanonischen Einstiege erreichbar sein wie die uebrigen Workspace-Checks.
  - Evidenz: Der erste segmentierte Workspace-Auditlauf 2026-04-23 zeigte fuer `W2` und `W5` eine Verdrahtungsluecke: die Skripte `scripts/check_scripts_layout.py`, `scripts/check_current_state_gate.py`, `scripts/check_rp_hard_gates.py`, `scripts/checks_rp_consistency.py`, `scripts/check_rp_staging_tag_coverage.py` und `scripts/update_backups_manifest.py` existierten bereits unter `scripts/`, hatten aber noch keinen kanonischen Einstieg in `.vscode/tasks.json`.
  - Ergebnis 2026-04-23 18:53: `.vscode/tasks.json` fuehrt jetzt die kanonischen Einstiege `Checks: scripts layout`, `Checks: rp current-state gate`, `Checks: rp consistency`, `Checks: rp hard gates`, `Checks: rp staging tag coverage` sowie `Backups: update manifest`. Der direkte Validierungslauf derselben W2/W5-Kommandos ist gruen: `check_current_state_gate.py`, `checks_rp_consistency.py`, `check_rp_hard_gates.py` und `check_rp_staging_tag_coverage.py` sind PASS; `check_scripts_layout.py` bleibt auf sauberem Arbeitsbaum unauffaellig. Der Steuerpunkt ist damit geschlossen.

- [x] [Jetzt] Den Wochenabschluss-Schonpfad fuer `Checks: full` und verwandte Wrapper-Laeufe konservativer ziehen und den verbliebenen Stilrest ohne erneuten Voll-Lastlauf schliessen.
  - Ziel: Der kanonische Full-Check soll auf dem aktuellen lokalen System nicht wieder CPU- und RAM-Spitzen bis an die Systemgrenze verursachen; zugleich soll der bereits vorliegende FAIL-Lauf ohne neuen teuren Vollscan nur noch ueber die verbliebenen Stilreste geschlossen werden.
  - Akzeptanzkriterien:
    1) der Auto-Modus von `scripts/run_with_cpu_limit.py` nutzt fuer schwere lokale Python-Laeufe einen kleineren Standard-Slice als bisher,
    2) der geaenderte Schonpfad ist durch den vorhandenen Regressionstest abgedeckt,
    3) der aktuelle Ruff-/Black-Restscope aus `.tmp/results/reports/checks_run_20260420_204514/{ruff,black}.log` ist gezielt gruen,
    4) Root-/Dev-Statusdokus dokumentieren denselben Abschluss, ohne den problematischen Voll-Lauf blind zu wiederholen.
  - Evidenz: Der Sammelreport `.tmp/results/reports/checks_report_20260420_204514.md` zeigte alle Governance-, Typ- und Test-Gates bereits gruen; offen blieben nur `ruff=FAIL (32)` und `black=FAIL (7)`. Gleichzeitig meldete der lokale Nutzerlauf, dass `Checks: full` kurz vor dem Terminal-Abbruch CPU und RAM auf `99%` getrieben hatte, waehrend der Wrapper auf dem 12-Thread-System noch automatisch `4` logische CPUs nutzte.
  - Ergebnis 2026-04-20 21:07: `scripts/run_with_cpu_limit.py` nutzt im Auto-Modus jetzt nur noch `2` logische CPUs statt `4`; `novapolis_agent/tests/scripts/test_run_with_cpu_limit.py` deckt den konservativeren Standard weiter ab und isoliert den Default-Test jetzt gegen ein aeusseres `NVP_CPU_LIMIT`. Die gezielten Ruff-/Black-Reste in `scripts/run_text_rpg_product_gate.py`, `scripts/sync_docs_after_checks.py`, `scripts/update_workspace_tree_dirs.py` sowie den betroffenen Script-Tests sind bereinigt. Der frische Full-Check `.tmp/results/reports/checks_report_20260420_210436.md` ist im expliziten 1-CPU-Schonmodus wieder vollstaendig PASS; der separate Coverage-Lauf bleibt mit `672 passed` und `96.16%` PASS, und `scripts/check_sim_epoch_assets.py --repo-root . --allow-empty` endet im Clean-Checkout-Profil weiter mit `summary=fail:0,warn:0`.

- [x] [Jetzt] Einen kleinen Doku-Sync-Helfer fuer Frontmatter-, Report- und Board-Nachzug nach grünen Sammellaeufen einfuehren.
  - Ziel: Nach groen Full-Checks sollen Root- und Dev-Dokus nicht mehr rein manuell denselben Reportpfad, denselben Stand und dieselben Open-Counts nachziehen muessen.
  - Akzeptanzkriterien:
    1) Root-/Dev-Dokus und Boards lassen sich nach einem validierten Lauf konsistent mit demselben Reportpfad aktualisieren,
    2) der Helfer respektiert Snapshot-, Frontmatter- und TODO-Index-Gates,
    3) `DONELOG.md`, `WORKSPACE_STATUS.md`, `todo.root.md`, `todo.index.md` und betroffene Boards bleiben danach in einem kleineren Sync-Aufwand,
    4) die Loesung reduziert nur Drift, ersetzt aber nicht die inhaltliche Boardpflege.
  - Evidenz: Die aktiven Root- und Dev-Dokus ziehen nach fast jedem grünen Sammellauf denselben Reportpfad, denselben Boardstand und denselben Checkzustand manuell ueber mehrere Dateien nach.
  - Ergebnis 2026-04-18 02:09: `scripts/sync_docs_after_checks.py` synchronisiert jetzt nach einem belegten Gruenlauf Snapshot-Lock, `stand`-/`checks`-Frontmatter und optional den TODO-Index-Nachzug fuer geaenderte Root-/Dev-Markdownpfade. Der Helfer akzeptiert `--report latest` oder einen konkreten Reportpfad, spiegelt den `run_checks_and_report.py`-Headline plus `snapshot-lock PASS (...)` in die betroffenen Dokus und zieht `novapolis-dev/docs/todo.index.md` via `scripts/check_todo_index_sync.py --write-index-meta` nach, sobald aktive TODO-Boards im Scope liegen. `.vscode/tasks.json` fuehrt dafuer den Task `Docs: sync after checks`, und `novapolis_agent/tests/scripts/test_sync_docs_after_checks.py` deckt Frontmatter-Sync, Latest-Report-Aufloesung und den TODO-Index-Hook ab. Der damalige Steuerpunkt war damit geschlossen.

- [x] [Als naechstes] Die Root-Tree-Artefakte in einen aktiven Reader-Baum und einen forensischen Vollbaum mit klarer Filterlogik aufspalten.
  - Ziel: Die kanonischen Tree-Artefakte sollen fuer aktive Navigation nicht weiter Venv-, Cache- und `.tmp`-Oberflaeche in derselben Form wie den Forensik-Vollstand mischen.
  - Akzeptanzkriterien:
    1) ein aktiver Tree fokussiert navigationsrelevante Surface statt lokaler Artefaktmassen,
    2) ein zweiter Pfad bleibt bewusst forensisch/vollstaendig fuer Audit-Zwecke erhalten,
    3) `WORKSPACE_STATUS.md`, Tree-Tasks und README/Index beschreiben dieselbe Zweiteilung,
    4) der Refresh bleibt automatisierbar ueber denselben Dev-Pfad.
  - Evidenz: `WORKSPACE_STATUS.md` dokumentiert, dass die aktuellen Tree-Artefakte inzwischen auch `.tmp`-Referenz-/Reportpfade sowie lokale Venv-/Cache-Oberflaechen spiegeln; zugleich soll die Reader-Surface laut Index gerade solche Artefaktklassen bewusst abgrenzen.
  - Ergebnis 2026-04-18 01:45: `scripts/update_workspace_tree_dirs.py` erzeugt jetzt drei getrennte Artefakte: `workspace_tree.txt` als aktiven Reader-Baum, `workspace_tree_dirs.txt` als aktive Verzeichnis-Summary und `workspace_tree_full.txt` als forensischen Vollbaum. Die aktive Filterlogik blendet `.tmp`, `.venv*`, `eval/results`, `novapolis-dev/logs`, `novapolis-sim/.godot`, `outputs`, `Backups` sowie weitere grosse Archive-/Raw-/Curated-Pfade aus; `.vscode/tasks.json`, `README.md`, `WORKSPACE_INDEX.md`, `WORKSPACE_STATUS.md`, `DONELOG.md`, `novapolis-dev/docs/donelog.md` und `novapolis-dev/docs/todo.index.md` fuehren denselben Split. Im Dev-Board bleibt damit nur noch der Doku-Sync-Helfer offen.

- [x] [Als naechstes] Den `active-surface-index.md` fuer Referenzdokus mit altem `last_check` vom 2026-03-04 erneut pruefen und sauber neu klassifizieren.
  - Ziel: Der Active-Surface-Index soll nicht nur die Boards und `process/**` frisch fuehren, sondern auch die weiterhin aktiven Referenzquellen belastbar auf April-Stand pruefen oder bewusst als weniger aktiv markieren.
  - Akzeptanzkriterien:
    1) Referenzdokus mit `last_check 2026-03-04` sind entweder frisch geprueft oder als bewusst seltener gepflegt umklassifiziert,
    2) `active-surface-index.md`, `doc-freshness`-Logik und Reader-Surface widersprechen sich nicht,
    3) die Pflege bleibt scanbar und ohne unnötigen Vollscan historischer Quellen,
    4) der Index bleibt kompakt und dient weiter als echte Governance-Hilfe.
  - Evidenz: `novapolis-dev/docs/active-surface-index.md` fuehrt Boards und `process/**` auf April-Stand, waehrend mehrere weiterhin relevante Referenzdokus noch `last_check = 2026-03-04` tragen.
  - Ergebnis 2026-04-18 01:21: Die bislang auf Maerz stehenden Referenzzeilen in `novapolis-dev/docs/active-surface-index.md` sind jetzt auf belegte April-Pruefstaende nachgezogen. Direkt geprueft wurden die Einzelquellen `index.md`, `naming-policy.md`, `tests.md`, `dataset-provenance.md`, `copilot-vscode-usage.md`, `readme_decisions.md`, `readme.hub.md` und `architecture-summary-local-ai.md`; die Gruppenpfade `specs/**` und `meta/**` bleiben REFERENCE, sind aber jetzt als manuell gepruefte Sammelwerte mit explizitem Hinweis auf die Wildcard-Ausnahme in `scripts/check_doc_freshness.py` dokumentiert. Im Dev-Board bleiben damit nur noch zwei offene Steuerpunkte.

- [x] [Jetzt] `WORKSPACE_INDEX.md` von einem agent-lastigen Tiefenkatalog wieder auf eine echte Workspace-Landing-Surface mit klaren Modullinks ausrichten.
  - Ziel: Die aktive Reader-Surface soll zuerst durch Root, Dev, Agent, RP und Sim navigieren und erst danach in Modultiefe gehen, statt weiterhin unter dem Workspace-Titel primär einen Agent-Dateiindex zu fuehren.
  - Akzeptanzkriterien:
    1) `WORKSPACE_INDEX.md` startet mit einer scanbaren Workspace-Landing-Surface ueber Root plus vier Hauptmodule,
    2) agent-lastige Detailtiefe bleibt erreichbar, dominiert aber nicht mehr den Einstieg,
    3) `WORKSPACE_STATUS.md`, `novapolis-dev/README.md` und der Index fuehren denselben Navigationsrahmen,
    4) Reader-Surface-Grenze und aktive Modulwege bleiben portabel und ohne Artefaktdrift.
  - Evidenz: `WORKSPACE_INDEX.md` fuehrt zwar bereits eine Reader-Surface-Grenze, traegt aber weiterhin als fruehen Hauptblock `Vollständiger Index aller Dateien im Agent-Verzeichnis` und bleibt damit fuer einen Workspace-Index noch deutlich agent-zentriert.
  - Ergebnis 2026-04-18 01:03: `WORKSPACE_INDEX.md` startet jetzt mit einer Workspace-Landing-Surface fuer Root, Dev, Agent, RP und Sim sowie den kanonischen Arbeits- und Referenzpfaden. Der tiefe Agent-Dateikatalog bleibt darunter als `Referenzkatalog Agent-Verzeichnis` erhalten, statt weiter den Einstieg zu dominieren; damit fuehren `WORKSPACE_STATUS.md`, `novapolis-dev/README.md` und der Index wieder denselben Navigationsrahmen, und im Dev-Board bleiben nur noch drei offene Steuerpunkte.

- [x] [Jetzt] `Workspace tree:*`-Tasks, Statusclaim und echten Launcher-Pfad wieder auf denselben reproduzierbaren Iststand ziehen.
  - Ziel: Der Workspace soll nicht gleichzeitig aktuelle Prozess-Tasks und einen fortgeschriebenen Statusclaim ueber lokal scheiternde Tree-Tasks tragen; entweder wird der aktuelle Launcherpfad belastbar gruen verifiziert oder die Doku auf den echten Reststand korrigiert.
  - Akzeptanzkriterien:
    1) `.vscode/tasks.json`, `WORKSPACE_STATUS.md` und `novapolis-dev/docs/donelog.md` widersprechen sich danach nicht mehr beim Tree-Task-Verhalten,
    2) `Workspace tree: full` und `Workspace tree: directories` laufen lokal belegbar ueber denselben kanonischen Pfad oder sind bewusst anders dokumentiert,
    3) die Root-Tree-Artefakte lassen sich ohne Terminal-Sonderweg aktualisieren,
    4) der Punkt bleibt auf den technischen Task-/Governance-Pfad begrenzt.
  - Evidenz: `.vscode/tasks.json` fuehrt die Tree-Tasks inzwischen als `process`, waehrend `WORKSPACE_STATUS.md` und `novapolis-dev/docs/donelog.md` weiter den alten lokalen `pwsh /d /c`-Fehlpfad fuer `Workspace tree:*` fortschreiben.
  - Ergebnis 2026-04-18 00:59: Die drei Tasks `Workspace tree: full`, `Workspace tree: directories` und `Workspace tree: summary (dirs)` laufen lokal wieder belegbar ueber denselben aktiven Taskpfad; der kanonische Pfad fuehrt jetzt ueber `scripts/update_workspace_tree_dirs.py` mit den Modi `forensic-full`, `active-tree` und `active-dirs`. `WORKSPACE_STATUS.md` und `novapolis-dev/docs/donelog.md` fuehren den frueheren `pwsh /d /c`-Restclaim fuer diesen aktuellen Pfad nicht mehr fort; offen bleiben im Dev-Board jetzt noch vier Steuerpunkte.

- [x] [Jetzt] Logsprache, Reader-Surface-Grenze, Python-Versionstext und Support-A-B-Tie-Break-Fallback nachziehen.
  - Ziel: Die aktive Reader- und Runtime-Doku soll robuste, nicht vorschnell veraltende Aussagen fuehren; lokale Artefaktklassen sollen nicht mehr als direkte Navigationsziele erscheinen; und der Support-A-B-Pfad soll auch den Gleichstands-Tie-Break bei unbrauchbarer Judge-Antwort explizit testseitig abdecken.
  - Akzeptanzkriterien:
    1) die Formulierung `finale[r] kanonische[r] Sammellauf` ist in den betroffenen aktiven Logs auf eine zeitstabile Formulierung nachgezogen,
    2) `WORKSPACE_INDEX.md` beschreibt lokale/private Artefaktklassen ohne direkte Reader-Links auf diese Einzelpfade,
    3) `novapolis_agent/README.md` fuehrt die Root-Umgebung robust als Python-3.12.x-Referenz mit belegtem Iststand statt als patch-genaues Muss,
    4) `novapolis_agent/tests/test_api_chat_internal_branches.py` deckt zusaetzlich den Fall gleicher heuristischer Scores plus unbrauchbarer Judge-Antwort ab, wobei der Dauer-Tie-Break stabil erhalten bleibt.
  - Ergebnis 2026-04-17 06:04: Die aktiven Logs fuehren keine veraltende `finale`-Formulierung fuer den 05:30-Lauf mehr, `WORKSPACE_INDEX.md` beschreibt lokale/private Artefaktklassen nur noch als Klassenhinweis ohne direkte Reader-Links, `novapolis_agent/README.md` fuehrt die Root-`.venv` robust als Python-3.12.x-Referenz mit zuletzt dokumentiertem Gruenlauf 3.12.10, und `novapolis_agent/tests/test_api_chat_internal_branches.py` deckt jetzt auch den Gleichstandsfall mit unbrauchbarer Judge-Antwort ab. Der Sammellauf `.tmp/results/reports/checks_report_20260417_060413.md` endet vollstaendig mit `overall=PASS`, `639 passed` und `Total coverage: 93.89%`.

- [x] [Jetzt] Reader-Surface, Runtime-Doku und Support-A-B-Semantik auf einen konsistenten Iststand ziehen.
  - Ziel: Die aktive Reader-Oberflaeche soll keine private oder generierte Artefaktliste mehr als primaere Orientierung mischen, die Agent-Runtime-Doku soll den belegten Python- und Modellstand klar trennen, und der Support-A-B-Pfad soll einen explizit abgesicherten Fallback bei ungueltiger Judge-Antwort erhalten.
  - Akzeptanzkriterien:
    1) `novapolis_agent/README.md` beschreibt den belegten Python-Laufzeitstand konsistent und trennt Standard-Chat, Support-A-B und Judge-Modell klar,
    2) `WORKSPACE_INDEX.md` reduziert die aktive Reader-Surface auf navigationstaugliche Inhalte und kapselt private oder generierte Artefakte eindeutig ab,
    3) `novapolis_agent/tests/test_api_chat_internal_branches.py` deckt den Fall ab, dass der Judge keine verwertbare Antwort `A|B` liefert und der heuristische Gewinner bestehen bleibt,
    4) die zugehoerigen DONELOG-/Index-Dokumente sind im selben Lauf nachgezogen.
  - Evidenz: Die aktuelle Workspace-Semantik zeigte drei konkrete Driftpunkte: `novapolis_agent/README.md` forderte Python 3.13, waehrend der belegte Checklauf zuletzt mit Python 3.12.10 verifiziert wurde; `WORKSPACE_INDEX.md` fuehrte lokale Artefakte wie `.env`, `.coverage`, `coverage.xml` und `__pycache__` im aktiven Reader-Surface; und der Support-A-B-Pfad in `novapolis_agent/app/api/chat.py` hatte noch keinen eigenen Test fuer den Fallback bei nicht parsebarer Judge-Antwort.
  - Ergebnis 2026-04-17 05:55: `novapolis_agent/README.md` fuehrt jetzt den belegten Python-3.12.10-Interpreter als Referenzpfad und trennt Standard-Chat, Support-A-B und Judge in einer Profilmatrix. `WORKSPACE_INDEX.md` kapselt private und generierte Artefaktklassen hinter einer eigenen Reader-Surface-Grenze, statt sie als primaere Navigation zu fuehren. `novapolis_agent/tests/test_api_chat_internal_branches.py` sichert den Fall ab, dass ein gesetzter Judge keine verwertbare Antwort `A|B` liefert und der heuristische Gewinner bestehen bleibt. Der kanonische Sammellauf `.tmp/results/reports/checks_report_20260417_055543.md` ist mit `overall=PASS`, `638 passed` und `Total coverage: 93.89%` belegt gruen.

- [x] [Jetzt] Aktuellen Ruff-/Black-Drift im Python-Scope `novapolis_agent` plus `scripts` wieder auf Gruen ziehen.
  - Ziel: Der aktuelle Python-Qualitaetsscope soll wieder ohne Ruff- und Black-Reste laufen, damit der naechste Full-Check nicht an lokalem Stil-/Lint-Drift scheitert.
  - Akzeptanzkriterien:
    1) `python -m ruff check novapolis_agent scripts` liefert `0` Findings,
    2) `python -m black --check novapolis_agent scripts` liefert `0` reformattierbare Dateien,
    3) der Fixlauf fuehrt keine neuen Test- oder Typregressionen ein,
    4) der betroffene Full-Check-Pfad bleibt danach mindestens fuer Docs, Typen, Tests und Coverage gruen und scheitert nicht mehr an neu eingefuehrtem Drift im angefassten Scope.
  - Evidenz: Der Ausgangslauf `.tmp/results/reports/checks_report_20260417_052246.md` meldete `ruff=FAIL` und `black=FAIL`; der direkte Recheck zeigte 13 Ruff-Fundstellen und 9 Black-Reformat-Kandidaten u. a. in `novapolis_agent/app/api/chat.py`, `novapolis_agent/scripts/run_eval.py`, `novapolis_agent/scripts/support_ab_smoke.py`, `novapolis_agent/tests/test_api_chat_internal_branches.py`, `novapolis_agent/tests/test_api_sim_state.py` und `scripts/run_sim_headless_verify.py`.
  - Ergebnis 2026-04-17 05:30: Die gemeldeten Zeilenlaengen-, Import- und Formatdrifts sind im betroffenen Scope bereinigt. Der gezielte Testblock fuer Chat-, Sim- und Script-Pfade ist PASS, `python -m ruff check novapolis_agent scripts` ist PASS, `python -m black --check novapolis_agent scripts` ist PASS, und der damals gezogene kanonische Sammellauf `.tmp/results/reports/checks_report_20260417_053609.md` endet wieder mit `overall=PASS`.

- [x] [Jetzt] Repo-eigene Ruff-/Black-Restdrift aus der Wochenpruefung 2026-04-14 schliessen.
  - Ziel: Der kanonische Full-Check soll nach dem Wochenlauf nicht mehr an Python-Lint-/Formatresten in `novapolis_agent` und `scripts` haengen, nachdem `markdownlint`, `path-portability`, Typen, Tests, Coverage und die Hygiene-Cadence bereits wieder gruen sind.
  - Akzeptanzkriterien:
    1) `python -m ruff check novapolis_agent scripts` liefert `0` Findings,
    2) `python -m black --check novapolis_agent scripts` liefert `0` reformattierbare Dateien,
    3) `scripts/run_checks_and_report.py` endet danach wieder mit `overall=PASS`,
    4) der Fixlauf fuehrt keine neuen Typ- oder Testregressionen ein.
  - Evidenz: `.tmp/results/reports/checks_report_20260414_123622.md` zeigt nach den Root-Cause-Korrekturen fuer `markdownlint` und `path-portability` nur noch `ruff=FAIL (8)` und `black=FAIL (13)` als verbleibende Wochenabschluss-Blocker.
  - Ergebnis 2026-04-14 12:47: `novapolis_agent/app/api/tts_models.py` nutzt fuer `TtsOutputFormat` jetzt `StrEnum`, die betroffenen TTS- und CPU-Limit-Tests sind lint-/formatkonform nachgezogen, und der von `black` gemeldete Restdateisatz in `scripts/` ist formatiert. Der gezielte Pytest-Scope fuer `tests/scripts/test_run_with_cpu_limit.py`, `tests/test_tts_models_validators.py` und `tests/test_tts_provider_edges.py` ist PASS; `ruff check novapolis_agent scripts`, `black --check novapolis_agent scripts` und der Sammellauf `.tmp/results/reports/checks_report_20260414_124519.md` sind ebenfalls PASS. Das Dev-Board steht damit wieder bei `offen: 0`.

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


