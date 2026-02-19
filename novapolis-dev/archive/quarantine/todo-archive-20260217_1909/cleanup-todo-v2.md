---
stand: 2026-01-07 10:02
update: Prioritaet 1 umgesetzt (scripts.agent Wrapper/Kompatibilitaet, Tests migriert, Deprecation-Hinweise, Drift-Check).
checks: pwsh -NoProfile -File scripts\checks_types.ps1 PASS (2026-01-07); pwsh -NoProfile -File scripts\tests_pytest_root.ps1 PASS (2026-01-07)
---

Cleanup TODO v2 (Root .tmp)
===========================

Hinweis:
- Dieses Dokument bündelt besprochene Punkte. Neuere Entscheidungen haben Vorrang.
- Temporäre Artefakte liegen ab sofort unter `/.tmp/…`. Altpfade (`.tmp-results`, `.tmp-datasets`) werden schrittweise ausgerollt/migriert.

Priorität 0 — Temp-Pfade konsolidieren (aktiv)
----------------------------------------------
- Schreiben: Alle Root-Skripte nutzen `/.tmp/results/reports` statt `/.tmp-results/reports`.
- Lesen: Tools akzeptieren vorerst beide Pfade (Bestandsschutz in Tests/Docs).
- Follow-up: Legacy-Verweise in Doku (`DONELOG.md`, `WORKSPACE_STATUS.md`, `novapolis-dev/**`) auf `/.tmp` drehen.
- Stand 2026-01-07: Referenzen auf das Temp-TODO wurden auf `/.tmp/results/todo.cleaned.md` normalisiert; Archive/Tree-Snapshots bleiben historisch.
- Option: Symlinks/Junctions für Windows (`.tmp-results` → `.tmp/results`, `.tmp-datasets` → `.tmp/datasets`) — erst nach Review (Admin-/DevMode nötig).

Priorität 1 — Root als kanonische Skript-Ebene
----------------------------------------------
- Wrapper-Paket `scripts/agent/` anlegen (Import-Wrapper für Agent-CLIs), Guard stellt CWD=Root & PYTHONPATH sicher.
- Tests: Importe von `novapolis_agent.scripts.*` auf `scripts.agent.*` migrieren.
- Agent-CLIs: Im `__main__` deprecate-Hinweis „Bitte Root-Wrapper nutzen“.
- Drift-Check: `scripts/check_scripts_layout.py` (CI/Pre-commit) verhindert neue Skripte außerhalb `scripts/`+`scripts/agent/`.
	- Stand 2026-01-07: umgesetzt und nach `main` gepusht (Commit: b8746bf).

Priorität 2 — App/Eval-Struktur bereinigen
------------------------------------------
- Root `app/` abbauen: Importe auf `novapolis_agent.app.*` umstellen; `app/` anschließend löschen.
- `eval/` bleibt im Root (workspace-weit). Modul-interne eval-Artefakte nach Root migrieren; Modul behält Code.

Priorität 3 — Tests/Deps Stabilität
-----------------------------------
- Dev-Dependencies sicherstellen (`requirements-dev.txt`), inkl. `fastapi`, `uvicorn`, `pytest-timeout`.
- Option: `pip install -e novapolis_agent` (Importpfade stabil), alternativ PYTHONPATH-Guard im Wrapper.
- Coverage-Gate: erneuter Lauf via `python scripts/run_pytest_coverage.py --fail-under 80` nach Deps-Fix.

Priorität 4 — Prompt/Qualität (erledigt)
----------------------------------------
- Systemmeldung ergänzt: „Canvas geladen: N“ (aus `request.options.canvas_count`) — injected als zweite System-Nachricht.
- Synonyme dedupliziert (`novapolis_agent/eval/config/synonyms.json`).

Governance/Policies (Reminder)
------------------------------
- STOP-Gate vor WRITE/RUN (R-STOP); Wrapper-Pflicht (R-WRAP).
- Frontmatter in MD (R-FM, Setext H1/H2, MD003) — auch für dieses Dokument.
- Doku-Update-Pflicht bei relevanten Änderungen (R-DOKU).

Offene Fragen
-------------
- Symlink/Junction Rollout für Altpfade (`.tmp-results`, `.tmp-datasets`) — technisch möglich, aber Freigabe/WhatIf empfohlen.
- Umfang Root-Wrapper (erste Tranche 6–8 häufige CLIs vs. kompletter Satz).