---
stand: 2026-06-19 09:07
update: Dev-Wochenbericht (Dev-Fokus) erstellt und validatorisch eingepflegt
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp/results/reports/checks_report_20260619_090547.md; snapshot-lock PASS (2026-06-19 09:07)

---
Wochenbericht (Dev-Fokus) — 2026-06-14
====================================

Kurzüberblick
- Zeitraum / Snapshot: 2026-06-14 14:37 (Snapshot-Lock im Postflight-Lauf).
- Gesamtstatus: Workspace-Grün; Root‑ und Modul‑Boards synchronisiert (siehe Links unten).

Dev‑Highlights (vollständige Sektion)
- Phasenstatus
  - Phase 0 — Baseline & Hook‑Audit: Abgeschlossen. Evidenz: `novapolis-dev/docs/process/vscode-agent-governance-surface.ssot.md`, `.github/hooks/rp-runtime-loop-guard.json`.
  - Phase 1 — Zielvertrag (Credits/Modelle): Abgeschlossen. Evidenz: `novapolis-dev/docs/process/model-credits-optimization-plan.ssot.md`.
  - Phase 2 — Logging‑Wächter (Agent‑Policy): Abgeschlossen (Agent-Body normativ). Evidenz: `.github/agents/novapolis-workspace-navigator.agent.md`.
  - Phase 3 — Root‑Governance‑Sync: Abgeschlossen. Evidenz: `.github/copilot-instructions.md`.
  - Phase 4 — VS‑Code Settings (Read‑only Audit): Abgeschlossen; keine Settings‑Mutation nötig.
  - Phase 5 — Konsistenz‑/Verifikationslauf: Teilweise ausgeführt (Validatoren laufen, Full‑Check-Report PASS steht in `novapolis-dev/docs/donelog.md`).
  - Phase 6 — Staged Rollout & Monitoring: Plan vorbereitet; Rollout-Checkliste in `novapolis-dev/docs/process/model-credits-optimization-plan.ssot.md`.

- Archiv‑Batches (Kurz)
  - Mehrere Archiv‑Batches (Batch 2..12) wurden konsolidiert und nach `novapolis-dev/archive/todo.dev.archive.md` verschoben; betroffene Einträge: diverse Hygiene-, Coverage- und Prozesspunkte. (Beleg: `novapolis-dev/docs/donelog.md`).

- Validatoren & Checks
  - `markdownlint`, `scripts/check_frontmatter.py`, `scripts/check_todo_index_sync.py` wurden in den beteiligten Läufen ausgeführt und meldeten PASS (siehe Frontmatter-Header oben und `novapolis-dev/docs/donelog.md`).

Dev‑Board / offene Aufgaben
- Aktueller Stand: `offen: 0` für Dev (Board‑Metadaten). Der Dev‑Plan ist heute ein Governance‑/Implementationsplan (Phasen 0‑6), keine operativen Checkbox‑Tasks.

Risiken / Beobachtungen (Dev‑relevant)
- Hooks sind Risikoquelle (Hook‑Risk Ampel: gelb); Empfehlung: Hook‑Ereignisstrom in `novapolis-dev/logs/**` als Quelle verifizierbar machen.
- Sim‑Verifikationen können hostabhängig blockieren (Godot Binary). Falls Sim‑Smoke automatisiert werden soll, bitte Godot‑Binary‑Resolver in CI definieren.

Konkrete nächste Schritte (empfohlen)
- Offener Punkt: Vollständiger Phase‑5 Lauf (Full‑Check‑Wrapper inkl. Snapshot‑Lock + Postflight Receipt) für alle Dev‑Mutationen ausführen.
- Hooks‑Monitoring: `novapolis-dev/logs/` optional anlegen und Hook‑Events dort spiegeln.
- Falls gewünscht: dieses Wochenformat als permanentes Artefakt an `novapolis-dev/docs/process/wochenbericht-<YYYY-MM-DD>-dev.md` automatisieren.

Wichtige Quellen / Links
- Root DONELOG: [DONELOG.md](../../DONELOG.md)
- Workspace Status: [WORKSPACE_STATUS.md](../../WORKSPACE_STATUS.md)
- Dev TODO Board: [novapolis-dev/docs/todo.dev.md](../todo.dev.md)
- Dev DONelog: [novapolis-dev/docs/donelog.md](../donelog.md)
- Model Credits SSOT: [novapolis-dev/docs/process/model-credits-optimization-plan.ssot.md](model-credits-optimization-plan.ssot.md)

---
Kurz: Diese Datei fasst die Dev-relevanten Phasen, Archiv‑Batches und Validator‑Belege zusammen. Sie wurde automatisch aus den aktuellen SSOTs und `novapolis-dev/docs/donelog.md` konstruiert.
