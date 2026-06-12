---
stand: 2026-06-12 22:56
update: Plan fuer Governance- und Behavior-Umstellung auf credits-optimierte Modellnutzung (GPT-5 mini + GPT-5.3-Codex) angelegt.
checks: snapshot-lock PASS (2026-06-12 22:56); npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc changed-dev-md PASS (2026-06-12 22:50); .\.venv\Scripts\python.exe scripts\check_frontmatter.py changed-dev-md PASS (EXITCODE=0, 2026-06-12 22:50).
---

Model-Credits Optimization Plan (Dev SSOT)
==========================================

Ziel
----

- Governance- und Behavior-Dokumente so nachziehen, dass Modellwahl und Toolnutzung credits-effizient, reproduzierbar und minimalinvasiv erfolgen.
- Arbeitsannahme aus dem aktuellen Lauf: `GPT-5 mini` fuer schnelle Broad-Pass-Analyse, `GPT-5.3-Codex` fuer praezise Umsetzung und Abschlusslaeufe.

Scope
-----

- In Scope: Governance-/Behavior-Leittexte, die Agent-Verhalten, Modellwahl, Kontextumfang und Tool-Intensitaet steuern.
- Out of Scope: Fachliche RP-/Sim-Inhalte ohne direkten Bezug zur Modell-/Credits-Policy.

Erfasste betroffene Dateien (Initial)
-------------------------------------

- `.github/agents/novapolis-workspace-navigator.agent.md`
- `.github/agents/novapolis-rp-szenenlabor.agent.md`
- `.github/copilot-instructions.md`
- `novapolis-dev/docs/copilot-vscode-usage.md`
- `novapolis-dev/docs/todo.dev.md`
- `novapolis-dev/docs/todo.index.md`
- `novapolis-dev/docs/donelog.md`

Rollout-Phasen
--------------

1. Phase A - Policy-Klarschnitt

- Credits-Effizienz als explizite Leitplanke in Agent- und Guidance-Texten einfuegen.
- Modell-Eskalation klar benoeten: erst `GPT-5 mini`, bei Komplexitaet/Qualitaetsbedarf auf `GPT-5.3-Codex`.

2. Phase B - Behavior-Haertung

- Toolcall-Budget und Kontext-Budget als feste Guardrails dokumentieren.
- Vollscans nur bei Evidenzbedarf; sonst fokussierte Suchpfade.

3. Phase C - Verifikation

- Konsistenzcheck zwischen Agent-Dateien, Root-Governance und Dev-Guidance.
- Doku-Sync in `todo.dev.md`, `todo.index.md` und `novapolis-dev/docs/donelog.md`.

Akzeptanzkriterien
------------------

- Credits- und Modellstrategie ist in allen betroffenen Leitdokumenten konsistent.
- Keine widerspruechlichen Modell-Empfehlungen zwischen Agent-Mode und Guidance.
- Aenderungen bleiben minimal und klar nachvollziehbar geloggt.
