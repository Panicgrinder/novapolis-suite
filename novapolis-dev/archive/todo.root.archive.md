---
stand: 2026-02-22 14:21
update: Vollsnapshot aus `todo.root.md` archiviert und Root-TODO auf neue Arbeitsvorlage umgestellt.
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-dev/archive/todo.root.archive.md' 'todo.root.md' 'DONELOG.md' 'WORKSPACE_STATUS.md' 'novapolis-dev/docs/donelog.md' PASS (2026-02-22 12:35); .\.venv\Scripts\python.exe scripts\check_frontmatter.py 'novapolis-dev/archive/todo.root.archive.md' 'todo.root.md' 'DONELOG.md' 'WORKSPACE_STATUS.md' 'novapolis-dev/docs/donelog.md' PASS (2026-02-22 12:35)
---

TODO-Archiv (Root)
==================

Hinweis
-------

- Dieses Archiv sammelt vollständig erledigte Abschnitte (H2/H3) aus `todo.root.md`.
- Bitte nur Blöcke verschieben, deren Checklisten vollständig abgehakt sind ([x] überall).
- Direkt unter der Abschnitts-Überschrift im Archiv eine Zeile ergänzen: `archived_at: YYYY-MM-DD HH:MM`.

Archivierte Einträge

README-Gesamtlauf (73/73) - abgeschlossen
-----------------------------------------

archived_at: 2026-02-22 16:27

Quelle: `todo.root.md` (Punkt "Alle README*.md im Workspace inhaltlich auf Aktualitaet/Wahrheit pruefen").

- [x] Umfangreiche READMEs einzeln geprüft; kompakte READMEs in 4er-Batches plus Restmenge per Einmal-Durchlauf verifiziert.
- [x] Identifizierte Driftpunkte wurden in den betroffenen Dateien korrigiert (`README.md`, `novapolis-sim/README.md`, `novapolis-rp/README.md`, `packages/README.md`, `novapolis_agent/README.md`).
- [x] Finaler Voll-Rescan über alle 73 README-Dateien durchgeführt: `.tmp/results/reports/readme_full_rescan_20260222_1627.md`.
- [x] Abschlussbefund: `missing_link_count=0`, `flag_count=0`.

Root-Backlog Vollsnapshot aus `todo.root.md` (2026-02-22)
--------------------------------------------------------

archived_at: 2026-02-22 12:35

Quelle: `novapolis-dev/archive/quarantine/todo-root-snapshot-20260222_1234.md` (vollstaendiger Stand vor Neustart der Root-TODO-Datei).

- [x] Vollinhalt von `todo.root.md` als Snapshot in den Quarantänepfad verschoben.
- [x] `todo.root.md` danach auf schlanke neue Arbeitsvorlage fuer frische Punkte zurueckgesetzt.

Single-Root Archivpflege & Verifikationsfix (2026-02-20)
---------------------------------------------------------

archived_at: 2026-02-20 16:26

Quelle: `novapolis-dev/archive/quarantine/single-root-todo.md` (Archivkopie, verifiziert gegen aktuellen Workspace-Stand).

- [x] Veralteten Archivpfad-Hinweis korrigiert (historischer Zielpfad `novapolis-dev/archive/2025/2025-11-09-single-root-todo.md` war nicht mehr auflösbar).
- [x] Dev-SSOT-Verweis im Kurzüberblick korrigiert (`novapolis-dev/docs/todo.dev.md` statt Archivdatei).
- [x] Root-Single-Root-Kernclaims erneut verifiziert: zentrale Root-Workflows aktiv, keine Modul-`.github/workflows`, nur Root-`.vscode`, keine aktive `*.code-workspace`.

Single-Root Umstellungsplan (validiert aus Archivkopie)
------------------------------------------------------

archived_at: 2026-02-21 04:01

Quelle: `novapolis-dev/archive/quarantine/single-root-todo.md` (Abschnitt `Monorepo Single Root - Umstellungsplan`).

- [x] Etappen 0-5 (Inventur, Root-venv, Task-Zentralisierung, Test-Discovery, Lint/Format, CI-Angleichung) als abgeschlossen verifiziert und archiviert.
- [x] Workflows Root-only verifiziert: nur `/.github/workflows/*.yml`, keine Modul-Workflows.
- [x] VS-Code-Workspace-Zielbild verifiziert: keine aktive `*.code-workspace`, nur Root-`.vscode`.
- [x] Konfliktkonfigurations-Abschluss verifiziert: kein aktiver Agent-Devcontainer, Root-`pyproject.toml` tools-only, lokale Markdownlint-Overrides durch Root-Ignores neutralisiert.
- [x] Prüf-/Release-Checks sowie Akzeptanzkriterien aus dem abgeschlossenen Block in dieses Archiv uebernommen.

Modul-Fokus (Agent/Dev/RP/Sim) - validiert aus Archivkopie
----------------------------------------------------------

archived_at: 2026-02-21 04:05

Quelle: `novapolis-dev/archive/quarantine/single-root-todo.md` (Abschnitt `Modul-Fokus (Auszuege - bitte in den SSOTs pflegen)`).

- [x] Agent-Block (TTS/Tools-Planung) als abgeschlossen markiert und auf aktives Board `novapolis-dev/docs/todo.agent-board.md` referenziert.
- [x] Dev-Block (Tooling/Infra) als abgeschlossen markiert und auf Archiv `novapolis-dev/archive/todo.dev.archive.md` referenziert.
- [x] RP-Block (Kanon/Canvas) als abgeschlossen markiert und auf aktives Board `novapolis-dev/docs/todo.rp.md` referenziert.
- [x] Sim-Block (Godot) als abgeschlossen markiert und auf aktives Board `novapolis-dev/docs/todo.sim.md` referenziert.

Offene Aufgaben (Root - quer durchs Repo) - validiert aus Archivkopie
---------------------------------------------------------------------

archived_at: 2026-02-21 04:07

Quelle: `novapolis-dev/archive/quarantine/single-root-todo.md` (Abschnitt `Offene Aufgaben (Root - quer durchs Repo)`).

- [x] Wrapper-Policy/Root-Hinweise als abgeschlossen markiert und mit Root-Governance abgeglichen.
- [x] `.vscode`-Konsolidierung im Root als abgeschlossen verifiziert (nur Root-Konfiguration aktiv).
- [x] Snapshot-Frontmatter-Migrationsblock (historisch abgeschlossen) als abgeschlossen archiviert.
- [x] Tree-Snapshot-Taskblock als abgeschlossen archiviert.
- [x] Backups-/Manifest-Block als abgeschlossen archiviert; Artefakte (`Backups/AUDIT.md`, `Backups/README.md`, `Backups/manifest.v1.json`) vorhanden.
- [x] Zugehoerige Skript-Referenzen (`scripts/update_backups_manifest.py`, `scripts/rotate_backups.py`) vorhanden.

Wrapper-Migration (.ps1 -> .py) - validiert aus Root-Backlog
------------------------------------------------------------

archived_at: 2026-02-21 04:18

Quelle: `todo.root.md` (Abschnitt `Wrapper-Migration (.ps1 -> .py)`).

- [x] Keine aktiven `scripts/*.ps1` Wrapper mehr im Root vorhanden.
- [x] Produktive Python-Einstiegspunkte vorhanden und dokumentiert (`scripts/run_pytest_coverage.py`, `scripts/checks_linters.py`, `scripts/checks_types.py`, `scripts/tests_pytest_root.py`).
- [x] Historische PowerShell-Wrapper liegen ausschließlich im Archivpfad `novapolis-dev/archive/scripts/scripts.ps1-scripts/`.
- [x] Migrationsstatus in Doku/Status (DONELOG + WORKSPACE_STATUS) als abgeschlossen dokumentiert.

Priorisierung (Stand 2026-02-18) - Block "Jetzt" validiert aus Root-Backlog
----------------------------------------------------------------------------

archived_at: 2026-02-21 04:21

Quelle: `todo.root.md` (Abschnitt `Priorisierung -> Jetzt`).

- [x] Skript-Ladefallbacks validiert: `novapolis_agent/scripts/reports/generate_consistency_report.py` und `novapolis_agent/scripts/audit_workspace.py` vorhanden.
- [x] RP-Backlog-Marker validiert: `novapolis-rp/database-curated/staging/reports/generated-artifacts.md` vorhanden.
- [x] Root-Task-Zentralisierung validiert: `.vscode/tasks.json` vorhanden.
- [x] Block insgesamt als abgeschlossen verifiziert und in das Root-Archiv überführt.

Lokale AI - Zusammenfassung (Checkliste) validiert aus Root-Backlog
------------------------------------------------------------------

archived_at: 2026-02-21 04:28

Quelle: `todo.root.md` (Abschnitt `Lokale AI - Einbindung (organisch) -> Zusammenfassung (Checkliste)`).

- [x] Inclusion-Ziele definiert (RAG/Schattenmodus/Canary/Lernschleife).
- [x] Readiness-Gates je Modul dokumentiert.
- [x] Phasenplan, Daten-/Telemetrieplan und Immediate-Checklist als abgeschlossen markiert.
- [x] Evidenz-Verankerung bleibt aktiv im Root-Backlog über die Unterabschnitte `Go/No-Go Checkliste` und `Naechste Schritte (sofort)`.

Priorisierung (Stand 2026-02-18) - Block "Spaeter: S1-S4" validiert aus Root-Backlog
----------------------------------------------------------------------------------------

archived_at: 2026-02-21 04:31

Quelle: `todo.root.md` (Abschnitt `Priorisierung -> Spaeter`, Teilblock `S1-S4`).

- [x] S1 Stabilitaetsfenster als abgeschlossen verifiziert (2 gruene Root-Gate-Laeufe dokumentiert).
- [x] S2 Mindestbasis als abgeschlossen verifiziert (RAG-Index + Shadow-Log + Tests dokumentiert).
- [x] S3 Review-Rhythmus als abgeschlossen verifiziert (Slot/Checkliste dokumentiert).
- [x] S4 Editor-Setup Etappe 1/2 als abgeschlossen verifiziert (Root-`.vscode` konsistent).
- [x] Offener Punkt S5 explizit im aktiven Root-Backlog belassen.

Naechstes Vorgehen (1-2 Tage) - validiert aus Root-Backlog
----------------------------------------------------------

archived_at: 2026-02-21 04:52

Quelle: `todo.root.md` (Abschnitt `Naechstes Vorgehen (1-2 Tage)`).

- [x] Checks-Wrapper-Statuszuordnung auf FAIL bei STOP-Fall als erledigt dokumentiert.
- [x] Cleanup-Kandidaten Phase 4 als reviewt/geschlossen dokumentiert.
- [x] Alt-Analyse `analysis_chat_routers.md` in aktive Doku ueberfuehrt und Legacy entfernt.

Priorisierung (Stand 2026-02-18) - Block "Optional" (abgeschlossene Teilpunkte)
---------------------------------------------------------------------------------

archived_at: 2026-02-21 04:52

Quelle: `todo.root.md` (Abschnitt `Priorisierung -> Optional`, erledigte Teilpunkte).

- [x] Cleanup-Kandidaten Phase 4 reviewt/geschlossen (historischer Kontext, keine destruktive Aktion).
- [x] Archivierungs-Feinschliff umgesetzt (Rotation-Dry-Run/Manifest/SOP dokumentiert).
- [x] Offener Optional-Punkt `Etappe-3-Legacy-Ablösung` bleibt aktiv im Root-Backlog.


Snapshot-Gate v1 (Root)
-----------------------

archived_at: 2025-11-01 18:38

- [x] Timestamp-Task etabliert (Windows PowerShell, `Get-Date -Format 'yyyy-MM-dd HH:mm'`).
- [x] YAML-Frontmatter-Regel definiert (`stand`, `update`, `checks`).
- [x] Disziplin: Vor Änderungen Frontmatter-Zeitstempel aktualisieren.

Anhang
------

- Leitdokument: `.github/copilot-instructions.md` (Terminal-Policy & Snapshot-Gate).
- Status-Quellen: `WORKSPACE_STATUS.md`, `workspace_tree*.txt` (Tree-Snapshots).

Cleanup-Kandidaten (aus Konsistenz-Report 20251021_1446)
--------------------------------------------------------

archived_at: 2025-11-02 08:01

Quelle: `eval/results/reports/consistency/20251021_1446/report.md`.

Ziel: Offensichtliche Altlasten/Beispiele sichten, entweder (a) einbinden, (b) nach `examples/` verschieben/archivieren oder (c) entfernen. Bitte jeweils kurz verifizieren (Referenzen/Tests) und mit DONELOG erfassen.

API/Nahbereich:

- [x] `app/schemas.py` — Legacy-Schema entfernt. Modelle liegen zentral unter `app/api/models.py`.
- [x] `app/api/chat_helpers.py` — Geprüft: wird produktiv genutzt (z. B. `normalize_ollama_options` in `app/api/chat.py` und Tests). Behalten.
- [x] `app/core/content_management.py` — Wird aktiv aus `app/api/chat.py` genutzt (optional via Flags, Pre/Post/Prompt-Modifikationen). Behalten; später gezielt verdrahten/abdecken (Tests vorhanden, z. B. Post-Hooks via Monkeypatch).
- [x] `app/utils/convlog.py` — Aktuell nur in `app/utils/examples/*` referenziert. Als Beispiel/Utility belassen; ggf. später in `examples/` verschieben.
- [x] `app/utils/summarize.py` — Wird von Tests und Beispielen genutzt; belassen.
- [x] `app/utils/session_memory.py` — Wird in `app/api/chat.py` genutzt (optional via Settings). Belassen; Folgeaufgabe: Basis-Tests/Trunkierung.
- [x] `app/utils/examples/**` — Beispiele belassen; ggf. später konsolidieren.
- [x] `examples/rpg/*` — Beispiel-RPG belassen; später separat dokumentieren/archivieren.

Skripte (CLI/Tools - teils „potenziell ungenutzt“ aus App-Perspektive):

- [x] `scripts/customize_prompts.py`, `scripts/estimate_tokens.py`, `scripts/open_context_notes.py` — behalten oder als „optional tools“ markieren; README-Hinweis ergänzen.
  - Status: Done — README-Abschnitt „Optionale CLI-Tools“ ergänzt; Tools aufgeführt; `--help` verfügbar.
- [x] `scripts/openai_finetune.py`, `scripts/openai_ft_status.py`, `scripts/train_lora.py`, `scripts/fine_tune_pipeline.py` — CLI-Only; behalten, aber in Doku referenzieren; ggf. mit `--help`-Tests absichern.
  - Status: Done — In README „Optionale CLI-Tools“ verlinkt; vorhandene Smokes/Tests abdecken Grundpfade (fine_tune_pipeline, openai_ft_status).
- [x] `scripts/reports/generate_*` — jetzt repariert; behalten. Optional: Task/README ergänzen (siehe unten).
  - Status: Done — README „Neuigkeiten“ beschreibt Reports; Generatoren gelistet; CI lädt Artefakte hoch.
- [x] `scripts/audit_workspace.py` — behalten (liefert diese Liste); README-Querverweis setzen.
  - Status: Done — In README „Optionale CLI-Tools“ erwähnt.

Nicht-Python-Artefakte (Referenzen vorhanden, aber Pflege prüfen):

- [x] `eval/config/profiles.json` — aktuell; Doku konsolidieren.
  - Status: Done — `eval/README.md` Abschnitt „Profile & Synonyme“ ergänzt.
- [x] `eval/config/synonyms.json` (+ `synonyms.local.json`) — gepflegt; README aktualisieren.
  - Status: Done — `eval/README.md` (Overlay erklärt) und README Synonym-Hinweis vorhanden.
- [x] `app/prompt/system.txt` — Altlast; zentrale Prompts sind `app/core/prompts.py`. Entfernen, wenn nicht mehr referenziert.
  - Status: Done — Datei entfernt; `WORKSPACE_INDEX.md` und `docs/DONELOG.txt` aktualisiert.

Kurzfristig (nächste Iterationen)
---------------------------------

archived_at: 2025-11-02 08:07

- [x] Policy-Hook & Content-Management verdrahten
  - Ziel: `core/content_management.py` im Chat-Flow aktivieren (Pre-/Post-Prompt),
    Policies aus ENV/policy.json, Modus-Schalter (eval/unrestricted/profile).
  - Akzeptanz: Hook in `process_chat_request` und `stream_chat_request`; Log/Audit pro Eingriff;
    Tests: Rewrite/Allow-All/Block.

- [x] Session-Memory (Basis)
  - Ziel: `session_id` unterstützen, In-Memory Store + Trunkierungs-Heuristik (Token/Chars).
  - Akzeptanz: Einbettung relevanter Turns in Messages; Settings für Limits; Tests: Happy-Path, Trunkierung, Fallback.

- [x] Erweiterte LLM-Options
  - Schema/Validierung in `ChatRequest.options` ergänzt (`ChatOptions`), Pass-Through bis zum Client; Smoke-Tests hinzugefügt.
  - Ziel: num_ctx, repeat_penalty, presence/frequency_penalty etc. via `ChatRequest.options` validiert durchreichen.
  - Akzeptanz: Pydantic-Schema/Validation, Payload-Durchreichung, Smoke-Tests.

Rerun-Failed mit Profil/Meta-Rekonstruktion (3-7 Tage)
------------------------------------------------------

archived_at: 2025-11-02 08:21

- [x] Rerun-Failed mit Profil/Meta-Rekonstruktion
  - `scripts/rerun_from_results.py` rekonstruiert Model/Host/Temperature/Checks aus Meta
  - ASGI/HTTP unterstützt
  - Smoke-Test vorhanden

Kurz-Update (2025-10-20)
------------------------

archived_at: 2025-11-02 08:34

- [x] Reruns vereinheitlicht (Profile-aware)
  - Skript: [`scripts/rerun_from_results.py`](scripts/rerun_from_results.py)
  - Task: VS Code „Eval: rerun from results“
- [x] Checksums & Restore
  - Skript: [`scripts/generate_checksums.py`](scripts/generate_checksums.py)
  - Doku: [`docs/RESTORE.md`](docs/RESTORE.md)
- [x] Workspace-Index/Tasks konsolidiert
  - Datei: [`WORKSPACE_INDEX.md`](WORKSPACE_INDEX.md)
  - Tasks: normalisiert

Kurz-Update (2025-10-25)
------------------------

archived_at: 2025-11-02 08:36

- [x] Kontext-Notizen: lokale Dateien priorisiert
  - Änderung: `CONTEXT_NOTES_PATHS` so angepasst, dass `context.local.*` vor `context.notes/` eingelesen wird.
  - Ergebnis: Tests wieder grün; Injektion enthält lokale Notizen zuverlässig (vor Trunkierung).
- [x] Pyright-Konfiguration bereinigt
  - Änderung: Ungültige Keys entfernt; Analysebereich auf `app/` und `utils/` fokussiert.
  - Ergebnis: 0 Fehler/0 Warnungen im App-Scope; Nacharbeit: tests/ & scripts/ später wieder einbeziehen und Warnungen abbauen.

Zusätzliche kurzfristige Abschlüsse (2025-10-21)
------------------------------------------------

archived_at: 2025-11-02 08:38

- [x] CI Stabilisierung (Linux/Windows)
  - `os.startfile` guard + plattformneutrale Open-Logik (webbrowser/open/xdg-open)
  - `rich` optional (Console/Table/Progress Fallbacks in run_eval)
  - `openai` optional in openai_ft_status (Nutzung prüft installierte Lib)
  - `workflow_dispatch` für manuelle CI-Runs

- [x] Synonym-Overlay erweitert (Empathie)
  - `empathisch`: [einfühlsam, zugewandt, mitfühlend, verständnisvoll, empathie]

Zusätzliche kurzfristige Abschlüsse (2025-10-22)
------------------------------------------------

archived_at: 2025-11-02 08:40

- [x] Docs konsolidiert: `AGENT_PROMPT.md` + `BEHAVIOR.md` → `AGENT_BEHAVIOR.md`
  - Inhalte zusammengeführt (System-Prompt, Richtlinien, System-Infos)
  - Verweise aktualisiert (Index, Training, Copilot-Instructions, VS Code Task)
  - Hinweis aufgenommen, wie das Dokument via `CONTEXT_NOTES_*` in den Agent-Kontext geladen wird
  - Kontext-Notizen Defaults unverändert belassen; Aktivierung/Erweiterung per ENV dokumentiert

- [x] Kontext-Setup & Logs (heute/gestern)
  - `eval/config/context.local.md`: 2-Tage-Digest (heute+gestern) + klare Feststellung (Defaults unverändert; ENV nutzen)
  - Platzhalter-Logs angelegt: `data/logs/2025-10-22.jsonl`, `data/logs/2025-10-21.jsonl` (gitignored)
  - Hinweis in `AGENT_BEHAVIOR.md` Historie präzisiert

Neu: Reports-Standard
---------------------

archived_at: 2025-11-02 08:45

- [x] Bericht-Ordner festlegen
  - Struktur: `eval/results/reports/<topic>/<YYYYMMDD_HHMM>/`
  - Inhalte pro Run:
    - `report.md` (Ergebnisse)
    - `params.txt` (Testparameter/Scope)
  - Vorteil: reproduzierbare Audits; klare Trennung von Artefakten

Hinweise:

- Die Heuristik meldet auch legitime CLI-Skripte als „potenziell ungenutzt“, da sie nicht von `app/main.py` referenziert werden. Diese bitte nicht vorschnell löschen, sondern als Tools dokumentieren und ggf. mit leichten Smoke-Tests abdecken.
- Vollständige Liste siehe Report unter obigem Pfad.

Offene Punkte (Kurzfristig)
---------------------------

archived_at: 2025-11-02 09:00

- [x] Integrationstest „alpaca Export→Prepare“
  - Ziel: End-to-End (Results → Export alpaca → Prepare-Pack)
  - Status: Done — Test vorhanden: [`tests/scripts/test_export_and_prepare_pipeline_alpaca.py`](../tests/scripts/test_export_and_prepare_pipeline_alpaca.py)
    sowie ergänzend: [`tests/scripts/test_export_finetune_more_edges.py`](../tests/scripts/test_export_finetune_more_edges.py),
    [`../tests/test_prepare_finetune_pack_nodedupe.py`](../tests/test_prepare_finetune_pack_nodedupe.py)
- [x] Cleanup: harte Laufwerks-Pfade entfernen
  - Status: Done — [`scripts/cleanup_phase3.ps1`](../scripts/cleanup_phase3.ps1)
    verwendet `Join-Path $ProjectRoot` (keine festen F:\-Pfade mehr)
- [x] Doku-Drift bereinigen
  - Status: Done — `cleanup_recommendations.md` und `README.md` sind konsistent;
    zentrale Endpunkte in [`app/main.py`](../app/main.py): `/`, `/health`, `/version`,
    `POST /chat`, `POST /chat/stream`



