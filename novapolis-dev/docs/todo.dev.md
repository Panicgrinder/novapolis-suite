---
stand: 2026-06-19 15:17
update: Phase 3 ist abgeschlossen: Die Root-Governance ist minimal auf KI-operative Framework-Semantik und die Phase-2-Abgrenzung synchronisiert. Phase 4 (Read-only-Audit der VS-Code-Settings) abgeschlossen: kein Drift; keine Settings-Mutation erforderlich.
checks: snapshot-lock PASS (2026-06-13 21:52); npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc novapolis-dev/docs/todo.dev.md PASS; .\.venv\Scripts\python.exe scripts\check_frontmatter.py novapolis-dev/docs/todo.dev.md PASS (EXITCODE=0); .\.venv\Scripts\python.exe scripts\check_todo_index_sync.py --repo-root . PASS

---

<!-- markdownlint-disable MD022 MD041 -->

TODO (Novapolis-Dev)
====================

Hinweis




Offene Aufgaben (Dev)


  - Ziel: Der bestehende Governance-Plan fuehrt nicht nur Soll-Regeln, sondern belegte technische Ausleitung fuer mini-first, Codex-Eskalation, Hook-Budget und Nachweisfluss.
  - Akzeptanzkriterien:
    1) fuer die offenen Phase-5-Punkte liegen explizite technische Zielpfade vor,
    2) die Ausleitung bleibt konsistent zu `.github/copilot-instructions.md` und `.github/agents/novapolis-workspace-navigator.agent.md`,
    3) kein stiller Scope-Sprung in RP-/Sim-Fachdaten.
  - Evidenz: `novapolis-dev/docs/process/model-credits-optimization-plan.ssot.md`, `.github/agents/novapolis-workspace-navigator.agent.md`.

  - Ziel: Hook-Entscheidungen (`allow/ask/deny`) werden fuer Governance-Audits reproduzierbar als Dev-Evidenz lesbar.
  - Akzeptanzkriterien:
    1) Loggingpfad und Pflichtfelder sind festgezogen,
    2) Nachweise lassen sich in Dev-DONELOG und Auditlaeufen referenzieren,
    3) keine Kollision mit bestehender Hook-/Pre-Commit-Logik.
  - Evidenz: `novapolis-dev/docs/process/vscode-agent-governance-surface.ssot.md`, `.github/hooks/rp-runtime-loop-guard.json`, `scripts/rp_runtime_loop_guard.py`.

  - Ziel: Aktive Flaechen fuehren keinen divergierenden Check-/Freshness-Stand.
  - Akzeptanzkriterien:
    1) Root- und Modulboards verweisen auf denselben gueltigen Laufstand,
    2) `novapolis-dev/docs/todo.index.md` bleibt synchron,
    3) stale Claims werden explizit nachgezogen statt implizit toleriert.
  - Evidenz: `todo.root.md`, `novapolis-dev/docs/todo.index.md`, `novapolis-dev/docs/todo.agent-board.md`, `novapolis-dev/docs/todo.rp.md`, `novapolis-dev/docs/todo.sim.md`.

  - Ziel: Die Mini-Lamas-SSOT bleibt als Architekturquelle aktiv, aber ihre Ausfuehrungskette und ihr Validierungsstatus sind gegen Root-/Dev-Governance eindeutig gespiegelt.
  - Akzeptanzkriterien:
    1) Rollenabgrenzung kollidiert nicht mit mini-first/Codex-Policy,
    2) offene Validierungs-/Projektionsthemen sind als klare Folgearbeit markiert,
    3) keine Umwandlung in Instructions ohne belegten Bedarf.
  - Evidenz: `novapolis-dev/docs/process/mini-lamas-architecture.ssot.md`, `novapolis-dev/docs/process/model-credits-optimization-plan.ssot.md`.

Geplanter, mehrstufiger Umsetzungsplan (Kurzfassung)

  - Aufgabe: Reproduzierbare Ist-Aufnahme erstellen: geladene Instructions/Agents/Hooks/Prompt-Files, `chat`-Settings, Hook-Logs, aktuelle TODO/DONELOG-Eintraege.
  - Akzeptanzkriterium: Startbefund enthaelt Prioritaetenpfad (Always-on Instructions -> scoped Instructions -> Agents/Hooks/Prompts/MCP -> Workspace/User/Org-Settings) und Hook-Risikoampel.
  - Status: Abgeschlossen (2026-06-13 09:57).
  - Evidenz: `.github/copilot-instructions.md`, `.github/instructions/*.instructions.md`, `.github/agents/*.agent.md`, `.github/hooks/rp-runtime-loop-guard.json`, `scripts/rp_runtime_loop_guard.py`, `scripts/pre_commit.py`, `.vscode/settings.json`, `novapolis-dev/docs/process/vscode-agent-governance-surface.ssot.md`, `novapolis-dev/docs/todo.index.md`, `novapolis-dev/docs/donelog.md`.

  - Aufgabe: Soll-Vertrag in `novapolis-dev/docs/process/model-credits-optimization-plan.ssot.md` auf AI-Credits-Logik und Mini-first-Eskalation schaerfen.
  - Akzeptanzkriterium: Klarer Eskalationspfad (`GPT-5 mini` zuerst, `GPT-5.3-Codex` nur mit belegter Begruendung und reviewbarem Handoff).
  - Status: Abgeschlossen (2026-06-13 10:51).
  - Evidenz: `novapolis-dev/docs/process/model-credits-optimization-plan.ssot.md` fuehrt jetzt einen verbindlichen Phase-1-Zielvertrag mit Mini-first-Pflicht, Eskalationskriterien, Handoff-Standard (`send:false`) und Rueckfuehrungspflicht in den Mini-Flow.

  - Aufgabe: `.github/agents/novapolis-workspace-navigator.agent.md` konkretisieren (`mini-first.required`, `codex-handoff.requires`, `diagnostics.level`, `hook-budget-guard`).
  - Akzeptanzkriterium: Keine widerspruechlichen Modell-/Handoff-Regeln mehr zwischen Dev-SSOT, Agent-Datei und Root-Governance.
  - Status: Abgeschlossen als Agent-Policy-Schicht (2026-06-13 11:25).
  - Evidenz: `.github/agents/novapolis-workspace-navigator.agent.md` fuehrt die normativen Policy-Felder im Agent-Body.
  - Abgrenzung: Noch nicht abgeschlossen ist die technische Enforcement-Integration (keine automatische VS-Code-Frontmatter-Auswertung, keine Runtime-Hook-Enforcement-Implementierung in diesem Schritt).

  - Aufgabe: Nur notwendige Klarstellungen in `.github/copilot-instructions.md` vornehmen; keine Scope-Ausweitung.
  - Akzeptanzkriterium: Root-Regeln bleiben minimal, aber deckungsgleich zum gehaerteten Agent- und Dev-Plan.
  - Status: Abgeschlossen (2026-06-13 13:23).
  - Evidenz: `.github/copilot-instructions.md` fuehrt KI-operative Steuersemantik fuer aktive Normtexte und die Phase-2-Abgrenzung (Agent-Body normativ, keine automatische Frontmatter-/Runtime-Enforcement).

  - Aufgabe: Settings ausschliesslich dann nachziehen, wenn aus Phase 0 Drift-Reduktion belegbar wird.
  - Akzeptanzkriterium: Keine hostgebundenen Pfade in aktiven SSOT-/Policy-Texten; Settings-Aenderungen sind direkt evidenzverknuepft.
  - Status: Abgeschlossen — Read‑only Settings‑Audit ergab keine notwendige Settings‑Mutation.
  - Evidenz: novapolis-dev/docs/donelog.md (DONELOG‑Eintrag, 2026-06-13 15:20).
  - Abgrenzung: Ergebnisnotiz; spaetere Mutationen benötigen frischen Snapshot‑Lock, reguläre Checks und einen Eintrag in novapolis-dev/docs/donelog.md im selben Änderungslauf.

  - Aufgabe: Vollstaendiger Konsistenzcheck: Agent-Dateien vs Root-SSOT vs Dev-SSOT vs TODO/DONELOG vs Settings vs Hook-Logs.
  - Akzeptanzkriterium: `markdownlint`, `check_frontmatter.py`, `check_todo_index_sync.py` und Full-Check-Report ohne Governance-Widerspruch.

  - Aufgabe: Rollout in kleinen Commits; nach jeder Phase: Lint, Frontmatter, TODO-Index-Sync, Snapshot-Lock und Postflight-Receipt in DONELOG.
  - Akzeptanzkriterium: Jede Mutation ist minimal, rueckverfolgbar und im passenden DONELOG dokumentiert.

Sonstige Hinweise


Abgeschlossene Eintraege


Hinweis zu Validatoren


---

