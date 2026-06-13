---
stand: 2026-06-13 06:28
update: Der Credits-Plan fuehrt jetzt auch VS-Code-Customization-Surface, Logging-Waechter-Orchestrierung und AI-Credits-Fakten statt Legacy-Request-Annahmen.
checks: snapshot-lock PASS (2026-06-13 06:28); npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc changed-dev-md PASS (2026-06-13 06:24); .\.venv\Scripts\python.exe scripts\check_frontmatter.py changed-dev-md PASS (EXITCODE=0, 2026-06-13 06:24).
---

Model-Credits Optimization Plan (Dev SSOT)
==========================================

Ziel
----

- Governance- und Behavior-Dokumente so nachziehen, dass Modellwahl und Toolnutzung credits-effizient, reproduzierbar und minimalinvasiv erfolgen.
- Arbeitsannahme aus dem aktuellen Lauf: `GPT-5 mini` fuer schnelle Broad-Pass-Analyse, `GPT-5.3-Codex` fuer praezise Umsetzung und Abschlusslaeufe.
- Aktiver Kostenrahmen ist kuenftig AI-Credits-/Token-basiert, nicht primar `premium requests`-basiert.

Scope
-----

- In Scope: Governance-/Behavior-Leittexte, die Agent-Verhalten, Modellwahl, Kontextumfang und Tool-Intensitaet steuern.
- Out of Scope: Fachliche RP-/Sim-Inhalte ohne direkten Bezug zur Modell-/Credits-Policy.

Erfasste betroffene Dateien (Initial)
-------------------------------------

- `.github/agents/novapolis-workspace-navigator.agent.md`
- `.github/agents/novapolis-rp-szenenlabor.agent.md`
- `.github/copilot-instructions.md`
- `novapolis-dev/docs/process/vscode-agent-governance-surface.ssot.md`
- `novapolis-dev/docs/copilot-vscode-usage.md`
- `novapolis-dev/docs/todo.dev.md`
- `novapolis-dev/docs/todo.index.md`
- `novapolis-dev/docs/donelog.md`

Belastbare Grundannahmen (Stand 2026-06-13)
-------------------------------------------

- GitHub Copilot rechnet im aktuellen Modell ueber AI Credits auf Basis von Input-, Output- und Cached Tokens sowie Modellpreis ab.
- `premium requests` und Modell-Multiplikatoren sind fuer Legacy-Jahresplaene weiter dokumentiert, aber nicht der primaere operative Kostenrahmen fuer neue Governance-Entscheidungen.
- VS Code steuert Governance nicht nur ueber `.github/copilot-instructions.md`, sondern ueber eine kombinierte Customization-Surface aus Always-on Instructions, scoped `*.instructions.md`, Custom Agents, Hooks, Prompt Files, MCP-Servern und Workspace-/User-/Org-Einstellungen.
- Der Logging-Waechter ist damit die operative Orchestrierungsinstanz: Credits-Effizienz ist nicht sauber umgesetzt, solange er keine explizite Modell-, Handoff-, Hook- und Kontextbudget-Strategie fuehrt.
- Deutsch bleibt als Arbeitssprache sinnvoll; der primaere Kostentreiber ist nicht "Uebersetzung", sondern Tokenmenge, Kontextgroesse, Reasoning-Level, Modellwahl und Wiederholungsdiagnostik.

Rollout-Phasen
--------------

1. Phase 0 - VS-Code-Governance-Surface absichern

- Vor eigentlichem Policy-Umbau die aktive VS-Code-Customization-Surface explizit als Datensatz pflegen: Instructions, Agents, Hooks, Prompt Files, MCP, relevante Settings und Prioritaeten.
- Sicherstellen, dass kuenftige Governance-Arbeit nicht nur auf Repo-SSOT, sondern auf tatsaechlicher VS-Code-Lade- und Orchestrierungslogik basiert.

2. Phase A - Policy-Klarschnitt

- Credits-Effizienz als explizite Leitplanke in Agent- und Guidance-Texten einfuegen.
- Modell-Eskalation klar benoeten: erst `GPT-5 mini`, bei Komplexitaet/Qualitaetsbedarf auf `GPT-5.3-Codex`.
- Logging-Waechter explizit als Orchestrator benennen: STOP, Handoffs, Kontextbegrenzung, Modellwechsel und Validierungslast werden dort gesteuert.

3. Phase B - Behavior-Haertung

- Toolcall-Budget und Kontext-Budget als feste Guardrails dokumentieren.
- Vollscans nur bei Evidenzbedarf; sonst fokussierte Suchpfade.
- Handoffs standardmaessig reviewbar statt automatisch sendend halten; `send: true` nur mit ausdruecklicher Begruendung.
- Hooks darauf pruefen, ob sie unnoetige Zusatzturns erzeugen oder `Stop`-Schleifen mit weiteren AI-Credit-Kosten verursachen koennen.

4. Phase C - Verifikation

- Konsistenzcheck zwischen Agent-Dateien, Root-Governance und Dev-Guidance.
- Konsistenzcheck gegen VS-Code-Customization-Surface: keine impliziten Konflikte zwischen Repo-SSOT, Agent-Frontmatter, Hooks und Workspace-Settings.
- Doku-Sync in `todo.dev.md`, `todo.index.md` und `novapolis-dev/docs/donelog.md`.

Akzeptanzkriterien
------------------

- Credits- und Modellstrategie ist in allen betroffenen Leitdokumenten konsistent.
- VS-Code-spezifische Governance-Flaechen und Prioritaeten sind in einer eigenen Dev-SSOT dokumentiert und werden nicht still vorausgesetzt.
- Keine widerspruechlichen Modell-Empfehlungen zwischen Agent-Mode und Guidance.
- Keine Rueckfaelle auf Legacy-Annahmen wie `premium requests` als Primaerlogik oder `workspaceInstructions` als alleinigen Governance-Anker.
- Aenderungen bleiben minimal und klar nachvollziehbar geloggt.
