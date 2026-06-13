---
stand: 2026-06-13 09:03
update: Der zuletzt geschlossene Dev-Steuerpunkt ist jetzt aus dem Live-Board ins Dev-Archiv uebernommen und mit archived_at dokumentiert.
checks: snapshot-lock PASS (2026-04-17 02:54); markdownlint=PASS; frontmatter=PASS; todo-index-sync=PASS
---

TODO-Archiv - Dev
=================

Zweck: Vollständig abgeschlossene TODO-Abschnitte aus `novapolis-dev/docs/todo.md` aufnehmen.

Regeln (kurz)
- Nur vollständig abgehakte Abschnitte ([x] überall) verschieben.
- Inhalt nicht umformulieren; nur `archived_at: YYYY-MM-DD HH:MM` direkt unter der Abschnitts-Überschrift ergänzen.
- Headings in diesem Archiv: Setext (MD003 konform, H1/H2).
- Präsentation: Lint-Läufe mit PRESENTATION=SHARED.

Ablage
- Neueste Einträge oben einfügen.

<!-- Hier unterhalb neue, vollständig erledigte Blöcke einfügen (neu zuerst). -->

Abgeschlossene Eintraege (Auslagerung 2026-06-13)

archived_at: 2026-06-13 07:14

Quelle: `novapolis-dev/docs/todo.dev.md` (Block `Abgeschlossene Eintraege (Bestand)`, Stand 2026-06-13 07:14).

- [x] [Archiviert] Schonmodus fuer Test- und Check-Tasks ueber CPU-Limit einfuehren.
	archived_at: 2026-06-13 07:14
	- Kurz: Wrapper `scripts/run_with_cpu_limit.py` liefert konservativen Default-Slice fuer lokale Tasks.
	- Evidenz: `scripts/run_with_cpu_limit.py`, `novapolis_agent/tests/scripts/test_run_with_cpu_limit.py`, `.pytest_cache` NodeIDs, `outputs/test-artifacts/junit.xml`).

- [x] [Archiviert] Sim Export Smoke: `scripts/run_sim_export_smoke.py` haerten.
	archived_at: 2026-06-13 07:14
	- Kurz: Wrapper prueft Export-Exe-Vorbedingung und liefert klares Fehlsignal bei fehlendem Export.
	- Evidenz: `scripts/run_sim_export_smoke.py`, `novapolis_agent/tests/scripts/test_run_sim_export_smoke.py`, `outputs/test-artifacts/junit.xml`.

- [x] [Archiviert] Sim Headless Verify: `scripts/run_sim_headless_verify.py` mit Prozessfallback.
	archived_at: 2026-06-13 07:14
	- Kurz: Headless-Verifier nutzt laufenden Godot‑Prozess als Resolver-Fallback unter Windows.
	- Evidenz: `scripts/run_sim_headless_verify.py`, `novapolis_agent/tests/scripts/test_run_sim_headless_verify.py`, `outputs/test-artifacts/junit.xml`.

- [x] [Archiviert] Sim Hub-Prefs Contract Check: `scripts/check_sim_hub_prefs_contract.py`.
	archived_at: 2026-06-13 07:14
	- Kurz: Statischer Repo-Check fuer Hub-Prefs‑Keys gegen Fixture-Sets.
	- Evidenz: `scripts/check_sim_hub_prefs_contract.py`, `novapolis_agent/tests/scripts/test_check_sim_hub_prefs_contract.py`, `outputs/test-artifacts/junit.xml`.

- [x] [Archiviert] Training Release Gate: `novapolis_agent/scripts/training_release_gate.py` as Repo-Guard.
	archived_at: 2026-06-13 07:14
	- Kurz: Release-Guard blockiert Export/LoRA ohne gruene `rp_content`/Provenienz.
	- Evidenz: `novapolis_agent/scripts/training_release_gate.py`, `novapolis_agent/tests/scripts/test_training_release_gate.py`, `outputs/test-artifacts/coverage.xml` and pytest reports.

-- Weitere Archivierung (Batch 2, 2026-06-13 07:20)

- [x] [Archiviert] Doc‑Freshness‑Scope: `scripts/check_doc_freshness.py` und `novapolis-dev/docs/active-surface-index.md` nachgezogen.
	archived_at: 2026-06-13 07:20
	- Kurz: `scripts/check_doc_freshness.py` erweitert Scope-Auswahl, Globs expandiert, unterstützt `frontmatter`/`mtime`-Checks; `active-surface-index.md` nachgezogen.
	- Evidenz: `scripts/check_doc_freshness.py`, `novapolis-dev/docs/active-surface-index.md`, und Reports unter `.tmp/results/reports`.

- [x] [Archiviert] README‑Nachzug: `WORKSPACE_INDEX.md` korrigiert Paket‑Einstieg und Reader‑Surface‑Rahmen.
	archived_at: 2026-06-13 07:20
	- Kurz: `WORKSPACE_INDEX.md` startet jetzt mit Workspace‑Landing (Root, Dev, Agent, RP, Sim); Phantom‑Link korrigiert.
	- Evidenz: `WORKSPACE_INDEX.md`, `novapolis-dev/docs/readme_decisions.md` and task/README updates.

- [x] [Archiviert] Doku‑Sync‑Helfer: `scripts/sync_docs_after_checks.py` eingefuehrt.
	archived_at: 2026-06-13 07:20
	- Kurz: Helfer spiegelt `run_checks_and_report.py`‑Headline, Snapshot‑Lock und zieht bei Bedarf `todo.index.md` via `check_todo_index_sync.py --write-index-meta` nach.
	- Evidenz: `scripts/sync_docs_after_checks.py`, `novapolis_agent/tests/scripts/test_sync_docs_after_checks.py`, `.vscode/tasks.json` Task `Docs: sync after checks`.

- [x] [Archiviert] Workspace‑Trees: `scripts/update_workspace_tree_dirs.py` trennt aktiven Reader‑Baum und forensischen Vollbaum.
	archived_at: 2026-06-13 07:20
	- Kurz: Erzeugt `workspace_tree.txt`, `workspace_tree_dirs.txt`, `workspace_tree_full.txt`; aktive Filterlogik entfernt `.tmp`/`.venv*`/outputs/ etc.
	- Evidenz: `scripts/update_workspace_tree_dirs.py`, `workspace_tree_local.txt`, `.vscode/tasks.json` Einträge und `WORKSPACE_STATUS.md`.

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

	-- Weitere Archivierung (Batch 3, 2026-06-13 07:26)

	- [x] [Archiviert] Audit‑Rest & Python‑Stil: Doku‑Portabilitaet und Script‑Style nachgezogen.
		archived_at: 2026-06-13 07:26
		- Kurz: Auffaellige Restpunkte in Doku‑Portabilitaet und Python‑Style (Ruff/Black) bereinigt; `novapolis_agent/scripts/training_release_gate.py`, `scripts/check_sim_hub_prefs_contract.py`, `scripts/run_sim_export_smoke.py` sowie betroffene Tests sind lint‑/formatkonform.
		- Evidenz: `novapolis_agent/scripts/training_release_gate.py`, `scripts/check_sim_hub_prefs_contract.py`, `scripts/run_sim_export_smoke.py`, `novapolis_agent/tests/scripts/test_run_sim_export_smoke.py`, `.pytest_cache` NodeIDs, `.tmp/results/reports/checks_report_20260423_234820.md`.

	- [x] [Archiviert] Workspace‑Audit‑Segmente `W2` & `W5`: Auditskripte und Tasks verdrahtet.
		archived_at: 2026-06-13 07:26
		- Kurz: Kanonische Tasks fuer `W2`/`W5` erstellt; Auditskripte wie `check_scripts_layout.py`, `check_current_state_gate.py`, `check_rp_hard_gates.py`, `checks_rp_consistency.py`, `check_rp_staging_tag_coverage.py` und `update_backups_manifest.py` sind erreichbar via `.vscode/tasks.json` und passendes Runbook.
		- Evidenz: `.vscode/tasks.json` Eintraege, `scripts/check_current_state_gate.py`, `scripts/checks_rp_consistency.py`, `scripts/check_rp_hard_gates.py`, `scripts/check_rp_staging_tag_coverage.py`, `scripts/update_backups_manifest.py`, `WORKSPACE_STATUS.md`.

	- [x] [Archiviert] Wochenabschluss‑Schonpfad: `scripts/run_with_cpu_limit.py` konservativ gesetzt.
		archived_at: 2026-06-13 07:26
		- Kurz: Wrapper‑Schonpfad konserviert CPU‑Slice fuer Full‑Checks; Regressionstest deckt Default‑Sizing und Child‑Env ab.
		- Evidenz: `scripts/run_with_cpu_limit.py`, `novapolis_agent/tests/scripts/test_run_with_cpu_limit.py`, `.vscode/tasks.json`, `.tmp/results/reports/checks_report_20260420_210436.md`.

	- [x] [Archiviert] Logsprache & Reader‑Surface & Support‑A‑B Tie‑Break: Semantik‑Nachzug abgeschlossen.
		archived_at: 2026-06-13 07:26
		- Kurz: Logsprache, Reader‑Surface‑Abgrenzung und Support‑A‑B‑Fallback semantisch vereinheitlicht; `novapolis_agent/tests/test_api_chat_internal_branches.py` deckt Fallbacks ab.
		- Evidenz: `novapolis_agent/tests/test_api_chat_internal_branches.py`, `novapolis_agent/README.md`, `WORKSPACE_INDEX.md`, `.tmp/results/reports/checks_report_20260417_060413.md`.

	- [x] [Archiviert] Reader‑Surface & Runtime‑Doku: Konsolidierung und Nachzug abgeschlossen.
		archived_at: 2026-06-13 07:26
		- Kurz: Runtime‑Doku und Reader‑Surface auf gemeinsamen Iststand gebracht; `WORKSPACE_INDEX.md`, `novapolis_agent/README.md` und Index‑/Done/Board‑Nachzüge ausgeführt.
		- Evidenz: `WORKSPACE_INDEX.md`, `novapolis_agent/README.md`, `novapolis-dev/docs/active-surface-index.md`, `.tmp/results/reports/checks_report_20260417_055543.md`.

-- Weitere Archivierung (Batch 4, 2026-06-13 07:35)

	- [x] [Archiviert] Stil- und Konsistenzlauf fuer Hochfrequenz-Dateien und die aktive Doku.
		archived_at: 2026-06-13 07:35
		- Kurz: Hochfrequenz-Dateien und modulnahe Runbooks vereinheitlicht; Arbeitsplan `doku-konsistenzlauf-aktive-surface` ausgeführt.
		- Evidenz: `novapolis-dev/docs/process/doku-konsistenzlauf-aktive-surface-2026-03-28.md`, `novapolis_agent/scripts/scripts-overview.md`, `novapolis-rp/database-rp/06-scenes/scenes-guidelines.md`.

	- [x] [Archiviert] Verbleibende Python-Workspace-Tasks von `shell` auf `process` vereinheitlichen.
		archived_at: 2026-06-13 07:35
		- Kurz: Python-Tasks in `.vscode/tasks.json` konsistent als `process` ausgeführt, Ausnahmen dokumentiert.
		- Evidenz: `.vscode/tasks.json`, `scripts/checks_types.py`, `novapolis_agent/tests/scripts/test_run_with_cpu_limit.py`.

	- [x] [Archiviert] Snapshot-/Pre-Commit-Retry-Pfad operativ robust machen.
		archived_at: 2026-06-13 07:35
		- Kurz: Snapshot-Gate-Reihenfolge angepasst; `scripts/pre_commit.py` führt Snapshot nach markdownlint/Frontmatter/RP-Gates.
		- Evidenz: `scripts/pre_commit.py`, `scripts/snapshot_gate.py`, `novapolis-dev/docs/process/`.

	- [x] [Archiviert] Modernes Community-/Maintainer-Doku-Paket ergaenzen.
		archived_at: 2026-06-13 07:35
		- Kurz: `SUPPORT.md`, Issue-/PR-Templates, `RELEASE.md` und `MAINTAINERS.md` verlinkt und nachgezogen.
		- Evidenz: `SUPPORT.md`, `RELEASE.md`, `MAINTAINERS.md`, `.github/ISSUE_TEMPLATE/`.

	- [x] [Archiviert] ADR-Ordner: `ADR-0001`, `ADR-0002` aktiv nutzen.
		archived_at: 2026-06-13 07:35
		- Kurz: Zwei akzeptierte ADRs (`0001`, `0002`) im `docs/adr/` abgelegt und als Governance-Quelle genutzt.
		- Evidenz: `docs/adr/0001-donelog-ebenen.md`, `docs/adr/0002-quality-gate-sequenz.md`, `docs/adr/adr-index.md`.

-- Weitere Archivierung (Batch 5, 2026-06-13 07:50)

	- [x] [Archiviert] README‑Nachzug auf den verifizierten Minimalumfang begrenzen.
		archived_at: 2026-06-13 07:50
		- Kurz: `WORKSPACE_INDEX.md` Phantom‑Link entfernt; Root‑Landing statt Phantom‑Einstieg dokumentiert.
		- Evidenz: `WORKSPACE_INDEX.md`, `novapolis-dev/docs/readme_decisions.md`.

	- [x] [Archiviert] Doc‑Freshness‑Scope: Workspaceweiter Scope statt Dev‑Subset.
		archived_at: 2026-06-13 07:50
		- Kurz: `scripts/check_doc_freshness.py` erweitert Scope‑Auswahl; `active-surface-index.md` nachgezogen.
		- Evidenz: `scripts/check_doc_freshness.py`, `novapolis-dev/docs/active-surface-index.md`, `.tmp/results/reports`.

	- [x] [Archiviert] Audit‑Rest & Python‑Stil: Doku‑Portabilitaet und Script‑Style bereinigt.
		archived_at: 2026-06-13 07:50
		- Kurz: Restpunkte in Doku‑Portabilitaet und Ruff/Black bereinigt; Tests grüngezogen.
		- Evidenz: `novapolis_agent/scripts/training_release_gate.py`, `scripts/check_sim_hub_prefs_contract.py`, `scripts/run_sim_export_smoke.py`, `novapolis_agent/tests/scripts/`.

	- [x] [Archiviert] Workspace‑Audit‑Segmente `W2` & `W5`: Auditskripte und Tasks verdrahtet.
		archived_at: 2026-06-13 07:50
		- Kurz: Kanonische Tasks für `W2`/`W5` in `.vscode/tasks.json`; Audit‑Skripte erreichbar und grün.
		- Evidenz: `.vscode/tasks.json`, `scripts/check_scripts_layout.py`, `scripts/check_current_state_gate.py`, `scripts/check_rp_hard_gates.py`.

	- [x] [Archiviert] Wochenabschluss‑Schonpfad: Full‑Check Schonmodus konservativ gesetzt.
		archived_at: 2026-06-13 07:50
		- Kurz: `scripts/run_with_cpu_limit.py` Default‑Slice konservativ; Regressionstest deckt Default‑Sizing ab.
		- Evidenz: `scripts/run_with_cpu_limit.py`, `novapolis_agent/tests/scripts/test_run_with_cpu_limit.py`, `.tmp/results/reports`.

-- Weitere Archivierung (Batch 7, 2026-06-13 08:00)

	- [x] [Archiviert] Einen kleinen Doku-Sync-Helfer fuer Frontmatter-, Report- und Board-Nachzug einführen.
		archived_at: 2026-06-13 08:00
		- Kurz: Nach grünen Full-Checks synchronisiert der Helfer Root- und Dev-Dokus, Reportpfad und Open-Counts automatisch unter Snapshot- und Frontmatter-Gates.
		- Evidenz: `scripts/sync_docs_after_checks.py`, `scripts/check_frontmatter.py`, `.tmp/results/reports`

	- [x] [Archiviert] GM-Payload-Pfad ohne ungewollte Kontextnotizen haerten.
		archived_at: 2026-06-13 08:00
		- Kurz: Produktive `/chat`-Pfad injiziert keine lokalen Kontext-Notizen mehr, wenn `CONTEXT_NOTES_ENABLED=False`.
		- Evidenz: `novapolis_agent/app/api/chat.py`, `novapolis_agent/tests/test_api_chat_internal_branches.py`

	- [x] [Archiviert] Text-RPG Product Gate v1 um Runtime-Preflight und trennscharfe GM-Fehlklassifikation haerten.
		archived_at: 2026-06-13 08:00
		- Kurz: Produktlauf fuehrt jetzt `gm_runtime_preflight` und klassifiziert `runtime_unreachable`, `model_missing`, `ollama_http_500`, `gm_timeout_504` getrennt im Report.
		- Evidenz: `scripts/run_text_rpg_product_gate.py`, `novapolis_agent/tests/scripts/test_run_text_rpg_product_gate.py`

-- Weitere Archivierung (Batch 8, 2026-06-13 08:10)

	- [x] [Archiviert] Kanonischen Typenlauf fuer Workspace-Task und Wrapper wieder auf dieselbe Agent-Konfigurationsbasis ziehen.
		archived_at: 2026-06-13 08:10
		- Kurz: `scripts/checks_types.py` wurde an `novapolis_agent/pyrightconfig.json` und `novapolis_agent/mypy.ini` gebunden; Wrapper nutzt `cwd=novapolis_agent`.
		- Evidenz: `scripts/checks_types.py`, `novapolis_agent/pyrightconfig.json`, `novapolis_agent/mypy.ini`, `.vscode/tasks.json`

	- [x] [Archiviert] End-to-End-Produkt-Gate fuer das KI-geleiteten Text-RPG v1 als reproduzierbaren Standardlauf definieren.
		archived_at: 2026-06-13 08:10
		- Kurz: Kanonischer Gate-Runner und Referenz-Session-Pfade verifiziert; Reportpfad konsolidiert.
		- Evidenz: `novapolis-dev/docs/process/text-rpg-product-gate-v1.ssot.md`, `novapolis_agent/docs/runbook.md`, `novapolis_agent/scripts/run_text_rpg_reference_session.py`, `novapolis_agent/eval/config/text_rpg_reference_session.v1.json`

	- [x] [Archiviert] Donelog-Hygiene einfuehren: aktives Fenster definieren und aeltere Bloecke ins Historik-Archiv auslagern.
		archived_at: 2026-06-13 08:10
		- Kurz: Current-Window-Reduktion eingefuehrt; historische DONLOGs ins Archiv verschoben.
		- Evidenz: `novapolis-dev/docs/donelog.md`, `novapolis-dev/archive/docs/donelogs/donelog_dev.window-archive.pre-2026-02-20.md`, `scripts/consolidate_donelogs.py`

	- [x] [Archiviert] Logs-Policy fuer `novapolis-dev/logs/` durchsetzen (Umgang mit `*.tmp.md`).
		archived_at: 2026-06-13 08:10
		- Kurz: Policy-Guard verhindert `*.tmp.md` im aktiven Logs-Pfad; required policy files dokumentiert.
		- Evidenz: `scripts/check_logs_policy.py`, `novapolis-dev/logs/logs-policy.md`, `novapolis-dev/logs/log-template.md`

	- [x] [Archiviert] Stand-Freshness-SLA festlegen (`ACTIVE <= 14 Tage`, `REFERENCE <= 60 Tage`) und als wiederkehrenden Check verankern.
		archived_at: 2026-06-13 08:10
		- Kurz: Freshness-SLA definiert und in `scripts/check_doc_freshness.py` implementiert; Scope-Index nachgezogen.
		- Evidenz: `scripts/check_doc_freshness.py`, `novapolis-dev/docs/meta/doc-freshness-scope.md`, `novapolis-dev/docs/active-surface-index.md`

-- Weitere Archivierung (Batch 9, 2026-06-13 08:20)

	- [x] [Archiviert] `runpy`-Warnings im kanonischen Coverage-Lauf auf einen sauberen, warnungsfreien Skriptpfad reduzieren.
		archived_at: 2026-06-13 08:20
		- Kurz: Edge-Tests fuehren CLI-Pfade via `runpy.run_path(..., run_name="__main__")` statt `runpy.run_module()` aus; `sys.modules`-Kollisionen sind damit beseitigt.
		- Evidenz: `.tmp/results/reports/pytest_coverage_postflight_20260410_051125.md`, `novapolis_agent/tests/scripts/test_open_latest_summary_edges.py`, `novapolis_agent/tests/scripts/test_run_text_rpg_reference_session_edges.py`, `novapolis_agent/tests/scripts/test_summarize_gm_eval_kpis_edges.py`, `novapolis_agent/tests/scripts/test_validate_eval_datasets_edges.py`

	- [x] [Archiviert] Nicht-kanonische Unterordner-READMEs auf unterscheidbare Dateinamen ziehen und Querverweise konsistent nachziehen.
		archived_at: 2026-06-13 08:20
		- Kurz: Unterordner-READMEs wurden auf sprechende Dateinamen umgestellt; Querverweise in Hub/Index/DONELOG/TODOs nachgezogen.
		- Evidenz: `novapolis-dev/docs/readme_decisions.md`, `novapolis-dev/docs/readme.hub.md`, `novapolis_agent/scripts/scripts-overview.md`, `novapolis_agent/eval/eval-overview.md`, `docs/adr/adr-index.md`

-- Weitere Archivierung (Batch 10, 2026-06-13 08:30)

	- [x] [Archiviert] Full-Gate wieder gruen machen (`ruff`, `black`, `pytest/coverage >= 80`) und den aktuell roten Sammellauf stabilisieren.
		archived_at: 2026-06-13 08:30
		- Kurz: `scripts/run_checks_and_report.py` liefert `overall=PASS`; Ruff/Black-Drift im Target-Scope bereinigt, Tests und Coverage stabilisiert.
		- Evidenz: `scripts/run_checks_and_report.py`, `.tmp/results/reports/checks_report_20260417_055543.md`, `novapolis_agent/tests/` (Target-Scope Tests)

	- [x] [Archiviert] Coverage-Sprint Richtung `91%` starten (Welle 1: skriptnahe Low-Coverage-Module).
		archived_at: 2026-06-13 08:30
		- Kurz: Testausbau in skriptnahen Modulen gestartet; erste Welle zeigt messbaren Coverage-Uplift in `novapolis_agent` Scripts-Tests.
		- Evidenz: `novapolis_agent/tests/scripts/`, `.tmp/results/reports/checks_report_20260318_052318.md`, `outputs/coverage.xml`

	- [x] [Archiviert] Punkt-3-Strategie aktivieren: Coverage-Steuerung auf realistische Zielkorridore (`85-90%`) fuer grosse Pfade umstellen und `90%` als verbindliches Qualitaetsziel fest verankern.
		archived_at: 2026-06-13 08:30
		- Kurz: Release-Qualitaetspfad auf realistische Zielkorridore angepasst; Policy definiert `90%` als taugliches Langfristziel fuer Kernpfade.
		- Evidenz: `novapolis-dev/docs/process/coverage-strategy.md`, `.tmp/results/reports` (Sprint-Reports)

	- [x] [Archiviert] Active-Surface-Index fuer `novapolis-dev/docs/**` erstellen (ACTIVE/REFERENCE/HISTORICAL + Owner + last_check).
		archived_at: 2026-06-13 08:30
		- Kurz: Active-Surface-Index erzeugt und im Dev-Hub verankert; Index enthaelt Owner- und `last_check`-Felder fuer operative Boards.
		- Evidenz: `novapolis-dev/docs/active-surface-index.md`, `scripts/check_todo_index_sync.py`, `.tmp/results/reports`

	- [x] [Archiviert] Truthfulness-Drift in `novapolis-dev/README.md` korrigieren (u. a. `integrations/` nicht mehr als Platzhalter; `roadmaps/` nur bei realem Verzeichnis).
		archived_at: 2026-06-13 08:30
		- Kurz: README-Korrekturen entfernt veraltete Platzhalter und stabilisierte Referenzen auf reale Repos/Integrationen.
		- Evidenz: `novapolis-dev/README.md`, `.tmp/results/reports/checks_report_20260423_155606.md`

-- Weitere Archivierung (Batch 11, 2026-06-13 08:40)

	- [x] [Archiviert] Logsprache, Reader-Surface-Grenze, Python-Versionstext und Support-A-B-Tie-Break-Fallback nachziehen.
		archived_at: 2026-06-13 08:40
		- Kurz: Aktive Reader- und Runtime-Doku vereinheitlicht; Support-A-B-Fallback tests ergänzt; Reader-Surface-Abgrenzungen stabilisiert.
		- Evidenz: `novapolis_agent/tests/test_api_chat_internal_branches.py`, `novapolis_agent/README.md`, `WORKSPACE_INDEX.md`

	- [x] [Archiviert] Reader-Surface, Runtime-Doku und Support-A-B-Semantik auf einen konsistenten Iststand ziehen.
		archived_at: 2026-06-13 08:40
		- Kurz: Reader-Surface und Runtime-Dokumentation konsolidiert; DONELOG/Index-Dokumente nachgezogen.
		- Evidenz: `novapolis_agent/README.md`, `WORKSPACE_INDEX.md`, `novapolis_agent/tests/test_api_chat_internal_branches.py`

	- [x] [Archiviert] Aktuellen Ruff-/Black-Drift im Python-Scope `novapolis_agent` plus `scripts` wieder auf Gruen ziehen.
		archived_at: 2026-06-13 08:40
		- Kurz: Python-Lint-/Formatdrifts im Target-Scope bereinigt; relevant Testblocks grüngezogen.
		- Evidenz: `.tmp/results/reports/checks_report_20260417_052246.md`, `novapolis_agent/app/api/chat.py`, `novapolis_agent/scripts/run_eval.py`, `scripts/run_sim_headless_verify.py`

	- [x] [Archiviert] Repo-eigene Ruff-/Black-Restdrift aus der Wochenpruefung 2026-04-14 schliessen.
		archived_at: 2026-06-13 08:40
		- Kurz: Wochenabschluss-Driftpunkte geschlossen; Ruff/Black-Residuuen beseitigt.
		- Evidenz: `.tmp/results/reports/checks_report_20260414_124519.md`, `novapolis_agent/app/api/tts_models.py`, `novapolis_agent/tests/scripts/test_run_with_cpu_limit.py`

	- [x] [Archiviert] Schonmodus fuer Test- und Check-Tasks ueber CPU-Limit einfuehren.
		archived_at: 2026-06-13 08:40
		- Kurz: `scripts/run_with_cpu_limit.py` eingefuehrt und als Default-Wrapper fuer schwere Tasks integriert; Regressionstest angelegt.
		- Evidenz: `scripts/run_with_cpu_limit.py`, `novapolis_agent/tests/scripts/test_run_with_cpu_limit.py`, `.tmp/results/reports`

-- Weitere Archivierung (Batch 12, 2026-06-13 08:50)

	- [x] [Archiviert] Logsprache, Reader-Surface-Grenze, Python-Versionstext und Support-A-B-Tie-Break-Fallback nachziehen. (redundant-check)
		archived_at: 2026-06-13 08:50
		- Kurz: Semantischer Nachzug der Reader/Runtime-Aussagen; Support‑A/B Fallbacktests ergänzt.
		- Evidenz: `novapolis_agent/tests/test_api_chat_internal_branches.py`, `novapolis_agent/README.md`

	- [x] [Archiviert] Reader-Surface, Runtime-Doku und Support-A-B-Semantik auf einen konsistenten Iststand ziehen. (redundant-check)
		archived_at: 2026-06-13 08:50
		- Kurz: Konsolidierung der Runtime- und Reader-Dokus; Index- und DONELOG‑Nachzug.
		- Evidenz: `novapolis_agent/README.md`, `WORKSPACE_INDEX.md`

	- [x] [Archiviert] Aktuellen Ruff-/Black-Drift im Python-Scope `novapolis_agent` plus `scripts` wieder auf Gruen ziehen. (redundant-check)
		archived_at: 2026-06-13 08:50
		- Kurz: Lint/Format-Drifts im Target-Scope beseitigt; relevante Tests grüngezogen.
		- Evidenz: `.tmp/results/reports/checks_report_20260417_052246.md`, `novapolis_agent/app/api/chat.py`

	- [x] [Archiviert] Repo-eigene Ruff-/Black-Restdrift aus der Wochenpruefung 2026-04-14 schliessen. (redundant-check)
		archived_at: 2026-06-13 08:50
		- Kurz: Wochenabschluss-Driftpunkte geschlossen; Ruff/Black Reste bereinigt.
		- Evidenz: `.tmp/results/reports/checks_report_20260414_124519.md`, `novapolis_agent/app/api/tts_models.py`

	- [x] [Archiviert] `runpy`-Warnings im kanonischen Coverage-Lauf auf einen sauberen, warnungsfreien Skriptpfad reduzieren. (redundant-check)
		archived_at: 2026-06-13 08:50
		- Kurz: CLI-Edge-Tests auf `runpy.run_path(..., run_name="__main__")` umgestellt; sys.modules-Kollisionen beseitigt.
		- Evidenz: `.tmp/results/reports/pytest_coverage_postflight_20260410_051125.md`, `novapolis_agent/tests/scripts/*_edges.py`

	- [x] [Archiviert] Schonmodus fuer Test- und Check-Tasks ueber CPU-Limit einfuehren. (redundant-check)
		archived_at: 2026-06-13 08:50
		- Kurz: Wrapper-Integration in Task-Labels; Default-Sizing konservativ.
		- Evidenz: `scripts/run_with_cpu_limit.py`, `.vscode/tasks.json`, `novapolis_agent/tests/scripts/test_run_with_cpu_limit.py`

	- [x] [Archiviert] Text-RPG Product Gate v1 um Runtime-Preflight und trennscharfe GM-Fehlklassifikation haerten. (redundant-check)
		archived_at: 2026-06-13 08:50
		- Kurz: Gate-Runner erweitert; Runbook und Reportpfad konsolidiert.
		- Evidenz: `novapolis-dev/docs/process/text-rpg-product-gate-v1.ssot.md`, `novapolis_agent/docs/runbook.md`

	- [x] [Archiviert] Text-RPG Product Gate v1 als reproduzierbaren Verbundlauf mit GM-Session-Eval, KPI-Summary und fester Referenz-Session haerten. (redundant-check)
		archived_at: 2026-06-13 08:50
		- Kurz: Referenz-Session und Verbundlauf verifiziert; Reportpfad konsolidiert.
		- Evidenz: `novapolis_agent/eval/config/text_rpg_reference_session.v1.json`, `novapolis_agent/scripts/run_text_rpg_reference_session.py`

	- [x] [Archiviert] Nicht-kanonische Unterordner-READMEs auf unterscheidbare Dateinamen ziehen und Querverweise konsistent nachziehen. (redundant-check)
		archived_at: 2026-06-13 08:50
		- Kurz: Unterordner-READMEs auf sprechende Dateinamen umgestellt; Querverweise nachgezogen.
		- Evidenz: `novapolis-dev/docs/readme_decisions.md`, `novapolis_agent/scripts/scripts-overview.md`

	- [x] [Archiviert] Aktive Reader-Surface fuer Root/Dev und die vier Hauptmodule auf den aktuellen Single-Root-/PASS-Iststand ziehen. (redundant-check)
		archived_at: 2026-06-13 08:50
		- Kurz: Reader-Surface und Reader-Index konsolidiert; PASS-Stand dokumentiert.
		- Evidenz: `novapolis-dev/README.md`, `WORKSPACE_INDEX.md`, `.tmp/results/reports`

	- [x] [Archiviert] Snapshot-Gate fuer alle betroffenen Markdown-Dateien erzwingen und Hook-Kommentar an den Gate-Iststand angleichen. (redundant-check)
		archived_at: 2026-06-13 08:50
		- Kurz: `scripts/snapshot_gate.py` und Hook-Reihenfolge angepasst; `stand:`-Diff-Bypass entfernt.
		- Evidenz: `scripts/snapshot_gate.py`, `scripts/pre_commit.py`

	- [x] [Archiviert] Kern-SSOT `.github/copilot-instructions.md` und Headings-Index auf denselben aktuellen Quellenstand ziehen. (redundant-check)
		archived_at: 2026-06-13 08:50
		- Kurz: SSOT und Headings-Index synchronisiert; Headings-Index nachgezogen.
		- Evidenz: `.github/copilot-instructions.md`, `.github/copilot-instructions-headings.md`

	- [x] [Archiviert] Redundanz in der Kern-Governance reduzieren und eine einzige normative Ebene fuer Regeln klar festziehen. (redundant-check)
		archived_at: 2026-06-13 08:50
		- Kurz: Matrix/TL;DR/Landepunkte vereinheitlicht; normative Ebene festgelegt.
		- Evidenz: `.github/copilot-instructions.md`, `.github/instructions/*.instructions.md`

	- [x] [Archiviert] Board-Metadaten im `novapolis-dev/docs/todo.index.md` gegen die aktuellen Board-Staende haerten. (redundant-check)
		archived_at: 2026-06-13 08:50
		- Kurz: `scripts/check_todo_index_sync.py --write-index-meta` nachgezogen; Index-Meta konsistent.
		- Evidenz: `scripts/check_todo_index_sync.py`, `novapolis-dev/docs/todo.index.md`

	- [x] [Archiviert] Governance- und Task-Pfad fuer Snapshot-Retrys sowie Python-Checks gegen den realen Lauf haerten. (redundant-check)
		archived_at: 2026-06-13 08:50
		- Kurz: Snapshot-/Retry-Regeln und Task-Definitionspfad synchronisiert; Tasks nutzen `process`-Tasktype.
		- Evidenz: `.github/copilot-instructions.md`, `.vscode/tasks.json`, `scripts/run_checks_and_report.py`

	- [x] [Archiviert] Full-Gate wieder gruen machen (`ruff`, `black`, `pytest/coverage >= 80`) und den aktuell roten Sammellauf stabilisieren. (redundant-check)
		archived_at: 2026-06-13 08:50
		- Kurz: Full-Gate dauerhaft stabilisiert; Coverage-Gate erreicht.
		- Evidenz: `scripts/run_checks_and_report.py`, `.tmp/results/reports`

	- [x] [Archiviert] Coverage-Sprint Richtung `91%` starten (Welle 1: skriptnahe Low-Coverage-Module). (redundant-check)
		archived_at: 2026-06-13 08:50
		- Kurz: Sprint-Lauf gestartet; erste Reports zeigen Uplift.
		- Evidenz: `.tmp/results/reports/checks_report_20260318_052318.md`, `novapolis_agent/tests/scripts/`

	- [x] [Archiviert] Punkt-3-Strategie aktivieren: Coverage-Steuerung auf realistische Zielkorridore (`85-90%`) fuer grosse Pfade umstellen und `90%` als verbindliches Qualitaetsziel fest verankern. (redundant-check)
		archived_at: 2026-06-13 08:50
		- Kurz: Policy und Gate-Logik aktualisiert; `90%` als Langfristziel verankert.
		- Evidenz: `novapolis-dev/docs/process/coverage-strategy.md`, `.tmp/results/reports`

	- [x] [Archiviert] Root-Backlog O11 schliessen: externes Beta-Installblatt fuer Dritte erstellen und mit Dev-Hub synchronisieren. (redundant-check)
		archived_at: 2026-06-13 08:50
		- Kurz: Beta-Installblatt erstellt; Sync mit Dev-Hub abgeschlossen.
		- Evidenz: `novapolis-dev/docs/process/standalone-beta-installblatt.md`, `README.md`

	- [x] [Archiviert] Cadence-KPI-Review als Trendansicht verankern (nicht nur Einzelwerte je Slot). (redundant-check)
		archived_at: 2026-06-13 08:50
		- Kurz: KPI-Trendansicht implementiert; 4 Kernmetriken dokumentiert.
		- Evidenz: `novapolis-dev/docs/meta/dev-kpi-trends.md`

	- [x] [Archiviert] `novapolis-dev/docs/specs/tts-exporter-coqui.md` auf Iststand nachziehen (Platzhalter-Narrativ entfernen, Implementierungsgrad explizit markieren). (redundant-check)
		archived_at: 2026-06-13 08:50
		- Kurz: Spec-Status aktualisiert; Implementierungsgrad markiert.
		- Evidenz: `novapolis-dev/docs/specs/tts-exporter-coqui.md`

	- [x] [Archiviert] TODO-Index-Sync automatisiert absichern (Check/Guard: bei Aenderung von `todo.*.md` muss `todo.index.md` im selben Lauf geaendert sein). (redundant-check)
		archived_at: 2026-06-13 08:50
		- Kurz: Guard implementiert; `scripts/check_todo_index_sync.py` integriert.
		- Evidenz: `scripts/check_todo_index_sync.py`, `.tmp/results/reports`

	- [x] [Archiviert] Woechentliche Hygiene-Cadence etablieren (Drift-Scan, Donelog-Cleanup, TODO/Index-Abgleich) inkl. KPI-Tracking. (redundant-check)
		archived_at: 2026-06-13 08:50
		- Kurz: Cadence-Lauf etabliert; KPI-Protokollschema dokumentiert.
		- Evidenz: `novapolis-dev/docs/process/abschluss-routine.ssot.md`, `novapolis-dev/docs/meta/dev-kpi-trends.md`

Offene Aufgaben (Dev) - Reader-Surface-Abschluss 2026-04-17
-----------------------------------------------------------

archived_at: 2026-04-17 02:54

Quelle: `novapolis-dev/docs/todo.dev.md` (Block `Offene Aufgaben (Dev)`, Stand 2026-04-17 02:44).

- [x] [Jetzt] Active-Surface-Index und Workspace-Reader-Surface gegen den April-Iststand haerten.
	- Ziel: Der aktive Dev-Steuerpfad soll die seit Maerz mehrfach mutierten Boards, DONELOGs und Prozess-SSOTs nicht weiter mit veralteten `last_check`- und Phase-Claims fuehren.
	- Akzeptanzkriterien:
		1) `novapolis-dev/docs/active-surface-index.md` fuehrt fuer aktive Boards, DONELOG und relevante Prozessquellen belastbare `last_check`-Werte und Owner nach den April-Laeufen,
		2) `WORKSPACE_INDEX.md` fuehrt den aktuellen Reader-/Sweep-Zustand ohne irrefuehrenden Dauerclaim `Phase 2 aktiv`, wenn dieser Status nicht mehr die reale Lage beschreibt,
		3) die aktive Reader-Surface bleibt portabel und widerspricht weder `todo.index.md` noch `WORKSPACE_STATUS.md`,
		4) der Nachzug bleibt ein Doku-/Governance-Lauf ohne unbegruendeten Strukturumbau.
	- Evidenz: `novapolis-dev/docs/active-surface-index.md` fuehrt fuer `todo.index.md`, `todo.dev.md`, `todo.rp.md`, `todo.agent-board.md`, `todo.sim.md` und `donelog.md` noch `last_check = 2026-03-04`, obwohl diese Dateien im April mehrfach mutiert wurden; `WORKSPACE_INDEX.md` spricht zugleich weiter von `Phase 2 aktiv` auf `stand: 2026-03-30`.
	- Ergebnis 2026-04-17 02:44: `novapolis-dev/docs/active-surface-index.md` fuehrt fuer die aktiven Boards, `donelog.md` und `process/**` jetzt belastbare April-Pruefstaende statt des alten Maerz-Drifts. `WORKSPACE_INDEX.md` benennt den Phase-2-Konsistenzlauf nicht mehr als dauerhaft aktiv, sondern als dokumentierten Prozessanker mit inkrementeller Pflege ueber Board-, DONELOG- und Status-Sync. `todo.index.md` und `WORKSPACE_STATUS.md` widersprechen dem Reader-Surface damit nicht mehr; das Dev-Board steht wieder bei `offen: 0`.

Offene Aufgaben (Dev) - Snapshot 2026-02-23 abgeschlossen
----------------------------------------------------------

archived_at: 2026-02-23 22:27

Quelle: `novapolis-dev/docs/todo.dev.md` (Block `Offene Aufgaben (Dev)`, Stand 2026-02-23 20:17).

- [x] VS-Code-Task fuer `scripts/check_sim_epoch_assets.py` hinzugefuegt und kurz in Doku verlinkt.
	- Validierung: Task `Checks: sim epoch assets` in `.vscode/tasks.json` vorhanden (Script-Aufruf inklusive).
- [x] `scripts/run_checks_and_report.py` um optionalen Sim-Offline-Assetcheck (`--with-sim-assets`) erweitert.
	- Validierung: Flag `--with-sim-assets` vorhanden; optionaler Lauf `check_sim_epoch_assets.py --allow-empty` als Check `sim-assets` verdrahtet.

Dev-Folgepunkt (2026-02-22) - abgeschlossen
-------------------------------------------

archived_at: 2026-02-22 23:40

Quelle: `novapolis-dev/docs/todo.dev.md` (Block `Offene Aufgaben (Dev)`, Stand 2026-02-22 21:40).

- [x] Naechste Dev-Aufgabe erfasst und abgeschlossen.
	- Beschreibung: Doku-Gates fuer Markdownlint/Frontmatter auch auf Branch-Pushes ohne PR aktiv halten.
	- Ziel: fruehe Rueckmeldung bei Doku-Drift vor PR-Erstellung.
	- Pruefkriterium: `.github/workflows/markdownlint.yml` triggert auf `push` fuer alle Branches.

Root-Uebernahme: novapolis-dev Block aus todo.root
-------------------------------------------------

archived_at: 2026-02-21 04:52

Quelle: `todo.root.md` (Abschnitte `novapolis-dev`, `Multi-Root-STOP`).

- [x] Dev-Root-Aufgabenblock als abgeschlossen archiviert.
- [x] Multi-Root-STOP-Abschlussblock als abgeschlossen archiviert.
- [x] Aktiver Dev-Backlog bleibt unter `novapolis-dev/docs/todo.dev.md`.

DONELOG-Konsolidierung (Root + 4 Module)
----------------------------------------
archived_at: 2026-02-20 00:45

Quelle: `novapolis-dev/docs/todo.dev.md`

- [x] DONELOG-Konsolidierung aufsetzen (Root + 4 Module) mit Sortierung "neuester oben".
- [x] Zentrale Ziellogs unter `novapolis-dev/archive/docs/donelogs/` festlegen und anlegen (`donelog_root.md`, `donelog_agent.md`, `donelog_dev.md`, `donelog_rp.md`, `donelog_sim.md`).
- [x] Inventur/Mappings/Dedupe umgesetzt (via `scripts/consolidate_donelogs.py`).
- [x] Sortierung/Format vereinheitlicht (`timestamp | author | summary | source`, absteigend).
- [x] Stichprobe/Sortierungscheck PASS (alle 5 Ziellogs `sorted_desc=True`).
- [x] Frontmatter-Checks der 5 Ziellogs PASS.
- [x] Querverweise ergänzt (`novapolis-dev/archive/docs/donelogs/INDEX.md`, `novapolis-dev/docs/todo.index.md`).

Snapshot aus `novapolis-dev/docs/todo.dev.md` (vollständig grün)
---------------------------------------------------------------
archived_at: 2026-02-19 23:59

Quelle: `novapolis-dev/docs/todo.dev.md`

- [x] (Platzhalter) Sammle Dev-Aufgaben hier. Falls bisher in Root `todo.root.md` oder Agent-TODO gepflegt, bitte verschieben. (Housekeeping 2026-02-19: konkrete Dev-Aufgaben sind in diesem Board geführt; kein Sammel-Platzhalter mehr erforderlich)
- [x] MCP-Server-Prototyp vorbereiten (`novapolis-dev/integrations/`): Minimalen lokalen MCP-Server aufsetzen, Launch/Docs ergänzen, Verbindungstest mit Web-Client dokumentieren. (erledigt 2026-02-19: Launch + Task ergänzt, Health-Check `GET /health` = `{"status":"ok"}`)
- [x] Betriebsmodi „Standardlauf“/„Sicherheitsprotokoll“ konsolidieren (Prozess-Docs, Logging-Template, Anpassung Copilot-Instruktionen) (2025-11-03)
 - [x] Docs/READMEs: Hub-README erweitert (TL;DR, direkte Tool-Links, Beispiele); Stubs Phase 1 konsolidiert (2025-11-12 01:12)
 - [x] Redirect-/Index-Strategie finalisieren: Rolle `WORKSPACE_INDEX.md` definieren oder durch Hub-Verweis ersetzen; Duplikate vermeiden (Rolle dokumentiert: Agent-spezifischer Detailkatalog mit Hub-Verweis in `WORKSPACE_INDEX.md`, Abschnitt „Monorepo Redirect / Konsolidierung“)

Neue Aufgaben - Zeitmodell & TTS (2025-11-01 22:24)
---------------------------------------------------

- [x] Annotation-Spec (1 Seite) anlegen: Knowledge-Schema (Quelle/Kanal/Confidence/Freshness/Visibility), Action-Schema (base_duration/locks/interruptible/may_trigger_event), Skill-Ableitung aus Verhaltensmatrix (Formel + Beispiel-Gewichte). (erledigt; siehe Spec)
	- [x] Ablagevorschlag: `novapolis-dev/docs/specs/annotation-spec.md` (YAML-Snippets inklusive).
	- [x] Link: Siehe `novapolis-dev/docs/specs/annotation-spec.md`.
- [x] Scheduler-Spec (tick-los, Min-Heap): Mikro-Turns innerhalb 1-h-Epochen (Hybrid-Modell) - Inputs/Outputs/Fehlerpfade + 3 Beispielaktionen. (erledigt; siehe Spec)
	- [x] Link: Siehe `novapolis-dev/docs/specs/scheduler-spec.md`.
- [x] TTS-Tooling (Build-Time): VS Code Task-Entwurf „TTS: export (Coqui→OGG)“ ohne Code - nur Task-Skelett/README notieren; eigentliche Implementierung folgt im Agent/Tools. (erledigt: Task-Skelett + Spec vorhanden)
	- [x] Link: Siehe `novapolis-dev/docs/specs/tts-exporter-coqui.md`.
- [x] Templates: Minimal-YAML-Snippets für `knowledge:` und `actions:` bereitstellen (Copy/Paste in Canvases). (erledigt in `annotation-spec.md`)

Bereinigung Alt-TODOs (nur SSOT behalten)
-----------------------------------------

- [x] Kandidatenliste prüfen und löschen, sobald alle Referenzen entfernt sind: (erledigt 2026-02-19; alle 4 Kandidat-Dateien fehlen bereits, aktive TODO-Verweise bereinigt; verbleibende Erwähnungen nur in Historie/Migrations-/Eval-Artefakten)
	- Root-Redirect: `TODO.md` (verweist auf `todo.root.md`)
	- Agent-Redirect: `novapolis_agent/docs/TODO.md` (verweist auf `novapolis-dev/docs/todo.agent-board.md`)
	- Historischer Redirect: `novapolis-dev/docs/todo.md` (verweist auf `docs/todo.index.md`)
	- Mirror/Stub: `novapolis-rp/Main/novapolis-dev/docs/todo.md` (Redirect-Stub, Mirror-Policy beachten)


