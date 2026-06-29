---
stand: 2026-06-29 16:07
update: Die Architektur-Notiz beschreibt jetzt zusaetzlich den append-only RP-Chattranskriptpfad als Rohsignal vor jeder Promotion.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp/results/reports/checks_report_20260629_155310.md; snapshot-lock PASS (2026-06-29 16:07)
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
- Wahrheit vor Training: RP-SSOT unter `novapolis-rp/database-rp/**` bleibt der redaktionelle Truth-Layer; trainierbare Pakete unter `novapolis_agent/eval/datasets/training/**` entstehen nur als dokumentierte Ableitung daraus.
- Promotionsgrenze: Session-, Replay- und Savegame-Artefakte bleiben Laufzeitsignal, bis sie explizit in RP-SSOT oder ein freigegebenes Curation-Pack uebernommen werden.

Vergleich zu "klassischen" Setups
---------------------------------

- Multi-Repo-Ansatz (pro Produkt ein Repo) wäre hier hinderlich: die Domänen greifen stark ineinander, und AI-gestützte Aufgaben würden durch Kontextwechsel erschwert.
- Strenger Monorepo-Ansatz (Bazel/Pants) ist Overkill; stattdessen: klare Paketgrenzen (z. B. `novapolis_agent`, `novapolis-rp`, `packages/novapolis_common`) mit leichtgewichtiger Orchestrierung über Python-Skripte.
- Das Projekt ähnelt eher einem Framework- und Tooling-Monorepo: Kernpaket(e), Daten/Stories, Simulation, Dokumentation und Dev-Tools in einem Workspace.

Kontrolliertes Simulationssystem
--------------------------------

- Novapolis ist kein freier Chatbot, sondern ein kontrolliertes Simulationssystem.
- Das Optimierungsziel ist nicht maximale Kreativitaet, sondern maximale Konsistenz gegen SSOT, Runtime, Gates und belegte Arbeitsstaende.
- Die aktuelle Modellarbeit ist bewusst in Rollen getrennt:
  - `llama3.1:8b` fuer stabile Erstantwort, Dokuarbeit, Governance-nahe Routine und Turn-Formulierung,
  - `qwen3.5:4b` fuer Gegenpruefung, Widerspruch, Semantik- und Scope-Kontrolle,
  - `qwen2.5:7b` als opt-in Judge fuer Tie-Break, Konfliktbewertung, Priorisierung und Freigabeempfehlung.
- Verbindlich wird hier nichts durch ein Modell allein. Verbindlich wird nur, was durch SSOT, DONELOG, STOP-Gates, Runtime-Artefakte, Frontmatter und Validatoren getragen ist.
- Die operative Modellmatrix fuer den Agent-Pfad bleibt in `novapolis_agent/README.md`; dieser Abschnitt fixiert nur die uebergeordnete Systemlesart.

Standard-Workflows (Root-basiert)
---------------------------------

- Checks/Lint/Typen/Tests: `& .\.venv\Scripts\python.exe scripts/run_checks_and_report.py`
- Coverage-Gate (R-COV): `& .\.venv\Scripts\python.exe scripts/run_pytest_coverage.py --fail-under 80`
- Multi-Root-Guard: `& .\.venv\Scripts\python.exe scripts/multi_root_cleanup.py --whatif`

Diese Kommandos sind die bevorzugte Oberfläche für Menschen und für die lokale AI.

RP-zu-Training (aktueller Umsetzungsschnitt)
-------------------------------------------

- RP-Eval bleibt ueber `novapolis_agent/scripts/build_eval_from_rp.py` an den Suite-Pfad `rp_content` gekoppelt.
- Der erste RP-Train-Schnitt laeuft jetzt ueber `novapolis_agent/scripts/build_training_from_rp.py` und erzeugt getrennte Seed-Pakete fuer `lore` und `ops` unter `novapolis_agent/eval/datasets/training/`.
- Der zweite Promotionsschnitt laeuft jetzt getrennt ueber `novapolis_agent/scripts/build_session_promotion_pack.py` und schreibt reviewpflichtige Curation-Records unter `novapolis_agent/eval/datasets/curation/session_promotions.v1.jsonl` aus dem kanonischen Session-Artefaktquartett.
- RP-Runtime-Sessions koennen jetzt zusaetzlich ein append-only `transcript.jsonl` unter `novapolis-rp/database-curated/staging/rp-runtime/sessions/<session-id>/` fuehren; diese Rohspur dient Nachvollziehbarkeit und spaeterer Review-Arbeit, ist aber weder SSOT noch direkter Builder-Input.
- Die RP-Train-Pakete bleiben bewusst Vorstufen mit Provenienz- und Promotionsfeldern, nicht freie Rohimports aus Session- oder Replay-Daten.
- Der operative Pfad verzweigt damit sauber: `RP-SSOT -> RP-Eval/RP-Training-Seeds -> Export/Pack -> LoRA` und getrennt `Runtime Session -> Session Promotion Pack -> RP-SSOT oder freigegebene Trainingsableitung`; RP-Markdown und Laufzeitlogs gehen weiterhin nicht direkt in Trainingsjobs.

Hinweis
-------

Diese Notiz dient als Kurzreferenz für die Architektur-Entscheidung "Single-Root-Monorepo mit AI-freundlicher Meta-Schicht". Für Details und laufende Aufgaben verweisen die Root-Dokumente (`README.md`, `WORKSPACE_STATUS.md`, `todo.root.md`, `DONELOG.md`) und die Governance-Datei `.github/copilot-instructions.md`.
