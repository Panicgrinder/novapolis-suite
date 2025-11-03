stand: 2025-11-02 09:00
update: Archiv ergänzt: „Offene Punkte (Kurzfristig)“ aus todo.root.md verschoben.
checks: keine
---

TODO-Archiv (Root)
==================

Hinweis
-------

- Dieses Archiv sammelt vollständig erledigte Abschnitte (H2/H3) aus `todo.root.md`.
- Bitte nur Blöcke verschieben, deren Checklisten vollständig abgehakt sind ([x] überall).
- Direkt unter der Abschnitts-Überschrift im Archiv eine Zeile ergänzen: `archived_at: YYYY-MM-DD HH:MM`.

Archivierte Einträge
--------------------

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
- [x] `app/core/content_management.py` — Wird aktiv aus `app/api/chat.py` genutzt (optional via Flags, Pre/Post/Prompt‑Modifikationen). Behalten; später gezielt verdrahten/abdecken (Tests vorhanden, z. B. Post‑Hooks via Monkeypatch).
- [x] `app/utils/convlog.py` — Aktuell nur in `app/utils/examples/*` referenziert. Als Beispiel/Utility belassen; ggf. später in `examples/` verschieben.
- [x] `app/utils/summarize.py` — Wird von Tests und Beispielen genutzt; belassen.
- [x] `app/utils/session_memory.py` — Wird in `app/api/chat.py` genutzt (optional via Settings). Belassen; Folgeaufgabe: Basis‑Tests/Trunkierung.
- [x] `app/utils/examples/**` — Beispiele belassen; ggf. später konsolidieren.
- [x] `examples/rpg/*` — Beispiel‑RPG belassen; später separat dokumentieren/archivieren.

Skripte (CLI/Tools – teils „potenziell ungenutzt“ aus App-Perspektive):

- [x] `scripts/customize_prompts.py`, `scripts/estimate_tokens.py`, `scripts/open_context_notes.py` — behalten oder als „optional tools“ markieren; README-Hinweis ergänzen.
  - Status: Done — README-Abschnitt „Optionale CLI-Tools“ ergänzt; Tools aufgeführt; `--help` verfügbar.
- [x] `scripts/openai_finetune.py`, `scripts/openai_ft_status.py`, `scripts/train_lora.py`, `scripts/fine_tune_pipeline.py` — CLI-Only; behalten, aber in Doku referenzieren; ggf. mit `--help`-Tests absichern.
  - Status: Done — In README „Optionale CLI-Tools“ verlinkt; vorhandene Smokes/Tests abdecken Grundpfade (fine_tune_pipeline, openai_ft_status).
- [x] `scripts/reports/generate_*` — jetzt repariert; behalten. Optional: Task/README ergänzen (siehe unten).
  - Status: Done — README „Neuigkeiten“ beschreibt Reports; Generatoren gelistet; CI lädt Artefakte hoch.
- [x] `scripts/audit_workspace.py` — behalten (liefert diese Liste); README-Querverweis setzen.
  - Status: Done — In README „Optionale CLI-Tools“ erwähnt.

Nicht‑Python‑Artefakte (Referenzen vorhanden, aber Pflege prüfen):

- [x] `eval/config/profiles.json` — aktuell; Doku konsolidieren.
  - Status: Done — `eval/README.md` Abschnitt „Profile & Synonyme“ ergänzt.
- [x] `eval/config/synonyms.json` (+ `synonyms.local.json`) — gepflegt; README aktualisieren.
  - Status: Done — `eval/README.md` (Overlay erklärt) und README Synonym-Hinweis vorhanden.
- [x] `app/prompt/system.txt` — Altlast; zentrale Prompts sind `app/core/prompts.py`. Entfernen, wenn nicht mehr referenziert.
  - Status: Done — Datei entfernt; `WORKSPACE_INDEX.md` und `docs/DONELOG.txt` aktualisiert.

Kurzfristig (nächste Iterationen)
---------------------------------

archived_at: 2025-11-02 08:07

- [x] Policy‑Hook & Content‑Management verdrahten
  - Ziel: `core/content_management.py` im Chat‑Flow aktivieren (Pre‑/Post‑Prompt),
    Policies aus ENV/policy.json, Modus‑Schalter (eval/unrestricted/profile).
  - Akzeptanz: Hook in `process_chat_request` und `stream_chat_request`; Log/Audit pro Eingriff;
    Tests: Rewrite/Allow‑All/Block.

- [x] Session‑Memory (Basis)
  - Ziel: `session_id` unterstützen, In‑Memory Store + Trunkierungs‑Heuristik (Token/Chars).
  - Akzeptanz: Einbettung relevanter Turns in Messages; Settings für Limits; Tests: Happy‑Path, Trunkierung, Fallback.

- [x] Erweiterte LLM‑Options
  - Schema/Validierung in `ChatRequest.options` ergänzt (`ChatOptions`), Pass‑Through bis zum Client; Smoke‑Tests hinzugefügt.
  - Ziel: num_ctx, repeat_penalty, presence/frequency_penalty etc. via `ChatRequest.options` validiert durchreichen.
  - Akzeptanz: Pydantic‑Schema/Validation, Payload‑Durchreichung, Smoke‑Tests.

Rerun-Failed mit Profil/Meta-Rekonstruktion (3–7 Tage)
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

- [x] Kontext‑Notizen: lokale Dateien priorisiert
  - Änderung: `CONTEXT_NOTES_PATHS` so angepasst, dass `context.local.*` vor `context.notes/` eingelesen wird.
  - Ergebnis: Tests wieder grün; Injektion enthält lokale Notizen zuverlässig (vor Trunkierung).
- [x] Pyright‑Konfiguration bereinigt
  - Änderung: Ungültige Keys entfernt; Analysebereich auf `app/` und `utils/` fokussiert.
  - Ergebnis: 0 Fehler/0 Warnungen im App‑Scope; Nacharbeit: tests/ & scripts/ später wieder einbeziehen und Warnungen abbauen.

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
  - Inhalte zusammengeführt (System‑Prompt, Richtlinien, System‑Infos)
  - Verweise aktualisiert (Index, Training, Copilot‑Instructions, VS Code Task)
  - Hinweis aufgenommen, wie das Dokument via `CONTEXT_NOTES_*` in den Agent‑Kontext geladen wird
  - Kontext‑Notizen Defaults unverändert belassen; Aktivierung/Erweiterung per ENV dokumentiert

- [x] Kontext-Setup & Logs (heute/gestern)
  - `eval/config/context.local.md`: 2‑Tage‑Digest (heute+gestern) + klare Feststellung (Defaults unverändert; ENV nutzen)
  - Platzhalter-Logs angelegt: `data/logs/2025-10-22.jsonl`, `data/logs/2025-10-21.jsonl` (gitignored)
  - Hinweis in `AGENT_BEHAVIOR.md` Historie präzisiert

Neu: Reports‑Standard
---------------------

archived_at: 2025-11-02 08:45

- [x] Bericht-Ordner festlegen
  - Struktur: `eval/results/reports/<topic>/<YYYYMMDD_HHMM>/`
  - Inhalte pro Run:
    - `report.md` (Ergebnisse)
    - `params.txt` (Testparameter/Scope)
  - Vorteil: reproduzierbare Audits; klare Trennung von Artefakten

Hinweise:

- Die Heuristik meldet auch legitime CLI‑Skripte als „potenziell ungenutzt“, da sie nicht von `app/main.py` referenziert werden. Diese bitte nicht vorschnell löschen, sondern als Tools dokumentieren und ggf. mit leichten Smoke‑Tests abdecken.
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

