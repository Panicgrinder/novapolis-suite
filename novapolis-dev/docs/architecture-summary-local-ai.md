---
stand: 2026-03-28 06:51
update: Phase-2-Konsistenzlauf harmonisiert die Architektur-Notiz auf aktuelle Root-Wrapper und den aktiven Single-Root-Betriebsrahmen.
checks: markdownlint PASS; frontmatter PASS; path-portability PASS; logs-policy PASS (2026-03-28 01:31)
---
Architektur-Notiz: Monorepo & Single-Root (lokale AI)
====================================================

Kurzfassung
-----------

- Workspace: Monorepo mit Single-Root (`Main/`), alle Teilmodule (Agent, RP, Dev, Sim) laufen unter diesem Root.
- Steuerung: Root fungiert als "Control Plane" (Skripte, Checks, Policies); Module sind Domänen-Unterbäume statt isolierter Produkte.
- Zielbild: Ein "biologisch" wachsender Workspace, der von einer lokalen AI möglichst einfach genutzt werden kann (Navigation, Refactoring, Audits, Tools).

Wichtige Prinzipien
-------------------

- Single-Root als Norm: VS Code wird immer mit dem Root-Ordner geöffnet, Multi-Root-Workspaces sind historische Sonderfälle und werden über `scripts/multi_root_cleanup.py` überwacht.
- Wrapper-Policy (R-WRAP): Mehrschrittprozesse (Lint/Typen/Tests/Coverage/Cleanup) laufen über Python-Skripte unter `scripts/` statt über adhoc Shell-Kommandos.
- Governance im Repo: Behaviour-/Sicherheitsregeln liegen in `.github/copilot-instructions.md` und werden von Root-Dokumenten (`README.md`, `WORKSPACE_STATUS.md`, `todo.root.md`, `DONELOG.md`) gespiegelt.
- Meta-Schicht für AI: Index/Status/TODO/DONELOG bilden gemeinsam eine leicht auswertbare Übersichtsschicht für Menschen und Tools.

Vergleich zu "klassischen" Setups
---------------------------------

- Multi-Repo-Ansatz (pro Produkt ein Repo) wäre hier hinderlich: die Domänen greifen stark ineinander, und AI-gestützte Aufgaben würden durch Kontextwechsel erschwert.
- Strenger Monorepo-Ansatz (Bazel/Pants) ist Overkill; stattdessen: klare Paketgrenzen (z. B. `novapolis_agent`, `novapolis-rp`, `packages/novapolis_common`) mit leichtgewichtiger Orchestrierung über Python-Skripte.
- Das Projekt ähnelt eher einem Framework- und Tooling-Monorepo: Kernpaket(e), Daten/Stories, Simulation, Dokumentation und Dev-Tools in einem Workspace.

Standard-Workflows (Root-basiert)
---------------------------------

- Checks/Lint/Typen/Tests: `& .\.venv\Scripts\python.exe scripts/run_checks_and_report.py`
- Coverage-Gate (R-COV): `& .\.venv\Scripts\python.exe scripts/run_pytest_coverage.py --fail-under 80`
- Multi-Root-Guard: `& .\.venv\Scripts\python.exe scripts/multi_root_cleanup.py --whatif`

Diese Kommandos sind die bevorzugte Oberfläche für Menschen und für die lokale AI.

Hinweis
-------

Diese Notiz dient als Kurzreferenz für die Architektur-Entscheidung "Single-Root-Monorepo mit AI-freundlicher Meta-Schicht". Für Details und laufende Aufgaben verweisen die Root-Dokumente (`README.md`, `WORKSPACE_STATUS.md`, `todo.root.md`, `DONELOG.md`) und die Governance-Datei `.github/copilot-instructions.md`.
