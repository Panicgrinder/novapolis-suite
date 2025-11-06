stand: 2025-11-06 15:58
update: MD003 + YAML Frontmatter (weitere 5 Dateien, templates+logs-2); targeted lint PASS; Logs aktualisiert.
checks: markdownlint-cli2 PASS (targeted, 5 Dateien); check_frontmatter.py n/a; repo-weit MD003 offen; pytest -q n/a
---

<!-- markdownlint-disable MD003 -->

# TODO-Uebersicht (Novapolis Suite)

Diese Datei dient als zentrale Sammelstelle fuer alle laufenden Aufgaben. Die vollstaendigen Projekt-Listen sind unten eingebettet, damit sie ohne Kontextwechsel eingesehen werden koennen.

## Kurzueberblick

- Hinweis: „Grün“ gilt nur bis zur nächsten Abweichung/Unsicherheit – dann STOP, Rückfrage, weiter nach Freigabe. Details: `.github/copilot-instructions.md` → „Unklarheiten‑STOP (global, immer gültig)“.

- 2025-11-06 15:58: MD003 Setext + YAML-Frontmatter in `novapolis_agent/cleanup_recommendations.md`, `Backups/novapolis-rp-development-archived-20251105/development/README.md`, `novapolis-dev/logs/betriebsmodi-20251103-0341.tmp.md`, `novapolis-rp/.github/ISSUE_TEMPLATE/bug_report.md`, `novapolis_agent/eval/config/context.local.sample.md`; targeted markdownlint PASS (5 Dateien); Logs aktualisiert.
- 2025-11-06 15:22: MD003-Setext-Korrekturen in `novapolis-rp/coding/tools/chat-exporter/README.md`, `novapolis-rp/coding/tools/metadata/README.md`, `novapolis-rp/coding/devcontainer/README.md`; targeted markdownlint PASS (3 Dateien).
- 2025-11-06 15:22: YAML-Frontmatter (stand/update/checks) in denselben 3 Dateien ergänzt; frontmatter-Validator PASS (targeted).
- 2025-11-06 15:30: YAML-Frontmatter ergänzt und MD003-Konformität bestätigt (Setext bereits vorhanden bzw. H1 ergänzt) in `packages/README.md`, `novapolis-sim/README.md`, `novapolis-rp/README.md`, `novapolis-dev/README.md`, `novapolis-rp/coding/tools/validators/README.md`; targeted markdownlint + frontmatter-Validator PASS (5 Dateien).
- 2025-11-06 15:35: MD003 Setext + YAML‑Updates in `novapolis-dev/logs/README.md`, `novapolis-dev/integrations/mcp-openai-eval/README.md`, `novapolis-rp/database-curated/staging/README.md`, `novapolis-rp/database-rp/06-scenes/README.md`, `.tmp-results/README.md`; targeted markdownlint + frontmatter-Validator PASS (5 Dateien).
- 2025-11-06 15:44: YAML-Frontmatter ergänzt und MD003/Setext vereinheitlicht in `novapolis-rp/database-curated/README.md`, `novapolis-rp/database-raw/99-exports/README.md`, `.tmp-datasets/README.md`, `novapolis_agent/eval/config/context.notes/README.md`; targeted markdownlint + frontmatter-Validator PASS (4 Dateien).
- 2025-11-06 15:51: MD003 Setext + YAML-Frontmatter (falls fehlend) in `Backups/README.md`, `Backups/AUDIT.md`, `novapolis-dev/logs/log-template.md`, `novapolis_agent/data/logs/README.md`, `eval/config/context.local.md`; targeted markdownlint PASS (5 Dateien).
- 2025-11-06 04:52: MD003-Setext-Korrektur in `novapolis-rp/database-curated/README.md`; targeted markdownlint PASS.
- 2025-11-06 04:50: MD003-Setext-Korrekturen in `packages/README.md`, `novapolis_agent/scripts/README.md`, `novapolis_agent/eval/README.md`, `novapolis_agent/eval/DEPRECATIONS.md`; targeted markdownlint PASS (4 Dateien).
- 2025-11-06 04:40: Demo-Test wieder entfernt (`tests/test_intentional_failure.py`), `pytest -q` via pwsh PASS; Frontmatter-Validator-Demo abgeschlossen.
- 2025-11-06 04:15: Frontmatter-Validator mit Demo-Datei geprüft (`check_frontmatter.py` → Fehlermeldungen bestätigt, nach Fix PASS); absichtlicher pytest-Fail durch `tests/test_intentional_failure.py` dokumentiert.
- 2025-11-06 03:45: Repo-weiter Markdownlint-Lauf zeigte 437× MD003 (Setext-Stil). YAML-Hinweis oben beachten; Bereinigung schrittweise angehen.
- 2025-11-06 03:18: Veraltetes Markdownlint-Skript entfernt (`novapolis-rp/coding/tools/validators/run_lint_markdown.ps1`); README & Copilot-Anweisungen aktualisiert.
- 2025-11-06 03:07: Veralteten Chat-Neustart-Prompt entfernt (`novapolis-dev/docs/prompts/chat-restart.md`); Index/DONELOG aktualisiert; Markdownlint (index/donelog) PASS.
- 2025-11-06 02:57: RP/Sim-Dokumente (`todo.sim.md`, Specs-Batch, Betriebsmodi-Notizen) auf YAML-Frontmatter gebracht und einzeln gelinted – PASS; DONELOG aktualisiert.
- 2025-11-06 02:52: `novapolis-dev/docs/todo.rp.md` auf YAML-Frontmatter gebracht und einzeln gelinted (`markdownlint todo.rp.md`) – PASS; DONELOG aktualisiert.
- 2025-11-06 02:42: `novapolis_agent/docs/training.md` und `docs/reports/overnight-20251022.md` gelinted und mit aktuellem Stand versehen; DONELOG/TODO aktualisiert.
- 2025-11-06 02:35: Agent-Dokumente (`customization.md`, `ARCHIVE_PLAN.md`, `CONTEXT_ARCH.md`, `REPORTS.md`) gelinted; Frontmatter/Checks aktualisiert; dokumentiert in DONELOG.
- 2025-11-06 02:30: `novapolis_agent/docs/DONELOG.txt` auf YAML-Frontmatter/Setext umgestellt; Lint-Einzellauf PASS; Root-DONELOG aktualisiert.
- 2025-11-06 02:23: README (Agent) und `docs/AGENT_BEHAVIOR.md` Heading/Frontmatter angepasst, Lint-Einzelläufe PASS; Zwischenschritt in DONELOG erfasst.

- **novapolis_agent**: Fokus auf Eval-/Tooling-Pflege, RAG-Ausbau, Tool-Use, Policy-Hooks.
- **novapolis-dev / novapolis-rp**: Fokus auf Canvas-Rettung Sprint (Charaktere/Logistik/Systeme) sowie bestehende Datenkurierungs- und Sim-Aufgaben.
- **YAML/Setext-Hinweis**: Bei allen Markdown-Anpassungen Frontmatter (stand/update/checks) synchronisieren und H1/H2 konsequent im Setext-Stil halten; laufender MD003-Backlog (122 Dateien laut letztem Markdownlint-Lauf).
- **Terminal/Tasks (STOP)**: VS Code markiert den Workspace aktuell fälschlich als Multi‑Root; Wrapper‑Tasks/Automationen sind unzuverlässig. Bis zur Bereinigung: KEINE WRAPPER, TERMINAL NUR MANUELL NUTZEN. Lösung erst nach Aufräumen (Single‑Root‑Struktur).
  - Open Case: Terminal/Tasks Multi‑Root → `novapolis-dev/logs/open-case-terminal-multi-root-20251103.md`
- **Root-Übersicht**: `WORKSPACE_STATUS.md` (Stand 2025-11-02) + `workspace_tree*.txt` (Stand 2025-11-02) liefern Gesamtinventar; nächste Aktualisierung idealerweise bis Mitte November oder nach größeren Umstrukturierungen.
  - [x] Tree-Snapshots (`workspace_tree.txt`, `workspace_tree_dirs.txt`, `workspace_tree_full.txt`) am 2025-11-02 via Tasks `Workspace tree:*` regeneriert.
- 2025-11-01: DONELOG-Heading-Stil auf Setext gemäß MD003 korrigiert; Markdownlint bleibt zentral via npx.
- **Archivierung**: `outputs/`- und `Backups/`-Artefakte sukzessive bündeln (ZIP) und Rotation dokumentieren.
  - Root-Archiv (vollständig erledigte Root-Blöcke): `novapolis-dev/archive/todo.root.archive.md`.
  - [ ] Altbestände nach Runs gruppieren (z. B. `outputs/lora-YYYYMMDD_HHMM` → einzelnes ZIP in `Backups/model-runs/`).
  - [ ] Eval-Resultate aus Vor-Umbenennung auf neue Paketpfade prüfen und Meta-Felder ggf. nachziehen (`eval/results/**/*.jsonl`).
  - [ ] README oder `Backups/`-Manifest um Rotationsplan ergänzen (Aufbewahrungsdauer, Löschkriterien).
  - [ ] Automatisierte Aufgabe/Script prüfen (`scripts/cleanup_phase*.ps1`) für regelmäßiges Auslagern.
 - **Lokale AI Einbindung (organisch)**: Phasenplan/Go‑Kriterien/Metriken in Abschnitt „Lokale AI – Einbindung (organisch)“ unten; Start mit Phase01 möglich (ohne Zeitdruck, mit harten Fallbacks).
 - **Editor‑Setup**: Konsolidierung `.vscode` auf Root vorbereiten (siehe Abschnitt „Editor‑Setup – .vscode‑Konsolidierung (Root‑zentriert)“).

- Neu (2025-11-06): Modulstatus → Agent: Gelb‑grün, Dev: Grün, RP: Gelb, Sim: Gelb. Konkrete 1–2‑Tage‑Schritte siehe Abschnitt „Nächstes Vorgehen (1–2 Tage)“.

## Modulstatus (2025-11-06)

- Agent (Backend): Gelb‑grün. Tests/Typen zuletzt grün, aber kein dokumentierter Lauf seit 2025‑10‑31; leichte Driftgefahr bei Scripts/Eval‑Artefakten.
- RP (Daten/Canvases): Gelb. Kurations‑Pipeline aktiv, einige Review-/Tagging‑Schritte offen.
- Dev (Dok‑Hub): Grün. Frontmatter‑Migration weitgehend durch, Donelog/Index gepflegt.
- Sim (Godot): Gelb. Option A gesetzt, Projektdatei kanonisch; Headless‑Lade‑Check offen.

## Nächstes Vorgehen (1–2 Tage)

Hinweis: Aufgrund des Multi‑Root‑STOPs keine Wrapper‑Tasks verwenden; bei Bedarf Befehle manuell im Terminal ausführen und Ergebnisse kurz dokumentieren.

### novapolis_agent

- [ ] Tests/Typen sequenziell laufen lassen (manuell) und Ergebnis protokollieren: `DONELOG.md` (Root) und `novapolis_agent/docs/DONELOG.txt` (Agent).
- [x] 2025-11-06 04:40: Demo-Test `novapolis_agent/tests/test_intentional_failure.py` entfernt; pytest -q PASS.
- [ ] Konsistenz‑Audit/Report aktualisieren (Sichtprüfung): `novapolis_agent/scripts/reports/generate_consistency_report.py` und Kandidaten aus `novapolis_agent/scripts/audit_workspace.py` prüfen.
- [ ] Optional nach Review: Cleanup‑Kandidaten (Phase 4) nur mit Freigabe angehen (`novapolis_agent/scripts/cleanup_phase4.ps1`).

### novapolis-rp

- [ ] Export konsolidieren: Offene Aufgabe „`99-exports/chat-export-complete.txt`“ abschließen; Delta‑Befunde in SSOT‑Canvases spiegeln.
- [ ] Tagging‑Pipeline 015–010 vom Dry‑Run auf Write heben; anschließend kurzem Lint‑Protokoll in `novapolis-dev/docs/donelog.md` vermerken.

### novapolis-dev

- [ ] Tree‑Artefakte neu erzeugen (manuell): `workspace_tree_full.txt`, `workspace_tree.txt`, `workspace_tree_dirs.txt`; Zeitstempel/Status in `WORKSPACE_STATUS.md` und `novapolis-dev/docs/donelog.md` aktualisieren.
- [ ] Optional: Kurzer Abschnitt „Editor‑Setup“ im Root‑`README.md` ergänzen (Hinweis auf STOP/Multi‑Root, manuelle Terminal‑Läufe).
- [ ] Markdownlint MD003 (aktive Docs): Scope auf essentielle Readmes/Dokus begrenzen, Stichproben-Lint (`markdownlint-cli2`), pro Datei Setext-Stil angleichen und Resttreffer außerhalb des Scopes katalogisieren.

### novapolis-sim

- [ ] Headless‑Lade‑Check des Godot‑Projekts `novapolis-sim/project.godot` durchführen; Warnungen/Fehler als Kurznotiz festhalten.

## Risiken (kurz)

- Tests/Typing nicht tagesaktuell (Agent) → mögliche stille Drift.
- RP: Offene Tagging-/Export‑Schritte; Deltas noch nicht vollständig in SSOT gespiegelt.
- Multi‑Root‑Markierung stört Tasks → bis zur Bereinigung ausschließlich manuelle Läufe.

## Lokale AI – Einbindung (organisch)

Kurz: Nicht beschleunigen, sondern sauber einführen. Schattenmodus → kleiner Canary → begrenzte Beta, mit Redaction/Flags/Metriken und klaren Rückfallpfaden.

### Zusammenfassung (Checkliste)

- [x] Inclusion‑Ziele definiert (Rollen: RAG, Schattenmodus‑Inferenz, Canary, Lernschleife)
- [x] Readiness‑Gates je Modul definiert (agent/rp/dev/sim)
- [x] Phasenplan entworfen (Schatten → Canary → Limited Beta → Stabilisierung)
- [x] Daten‑ & Telemetrieplan (Hygiene, Consent, Redaction, Metriken)
- [ ] Immediate next steps checklist (siehe unten)

### Go‑Kriterien je Modul (Beta‑Readiness, organisch)

- novapolis_agent
  - Tests/Typen PASS an 2 aufeinanderfolgenden Tagen
  - Policy‑/Rewrite‑Hooks aktiv, Session‑Memory (Basis)
  - RAG‑Minimum indexiert (10–50 Kern‑Docs, deterministischer Retriever‑Test PASS)
  - Logging mit Redaction (keine PII im Klartext)
  - Flags: `RAG_ON`, `SHADOW_ON`, `CANARY_PCT`
- novapolis-rp
  - Canvas‑Rettung Sprint1 Kerne abgeschlossen; Memory‑Bundle konsistent
  - Sidecars konsistent (tags/dependencies/last_updated)
  - Validator‑Pipeline (Behavior/Psymatrix) ohne kritische Findings
  - 200–500 kuratierte Q/A‑Paare oder Chat‑Turns als Startbasis
- novapolis-dev
  - Tasks/Validatoren laufen; kurzer Leitfaden „Wie wir lokal lernen“ (optional)
- novapolis-sim
  - Für Start nicht erforderlich (später als Szenario‑Generator hilfreich)

### Phasenplan (sanft, mit Fallbacks)

- Phase0 – Vorbereitung (ab sofort möglich)
  - Datenquellen fixieren (Canvases, Eval, Policies), Redaction klären, Minimal‑Metriken definieren
- Phase1 – Schattenmodus (1–2 Wochen)
  - Lokale AI beantwortet parallel, keine Nutzerwirkung; Stichproben‑Review 1–2×/Woche
  - Erfolg: ≥80% Accept in Stichproben, 0 kritische Policy‑Verstöße
- Phase2 – RAG‑only + Canary‑Inferenz (5–10% oder selektive Szenen)
  - Erst RAG aktiv, dann kleine Canary‑Quote mit hartem Fallback/Rate‑Limit
  - Erfolg: Qualität/Latenz ≥ Status quo; Fallback selten
- Phase3 – Lernschleife v0.1 (1–2‑wöchig)
  - Kuratierte Deltas → Train/Val‑Pack, LoRA‑Mini; Versionierung, einfache A/B‑Checks

### Metriken (leichtgewichtig)

- Qualität (Stichprobe): Accept/Revise/Reject‑Rate
- Policy: Block/Rewrite‑Rate (kritische Verstöße = 0)
- RAG: HitRate@K, Overlap‑Score mit Antwort
- Runtime: p50/p95 Latenz, Token‑Längen (in/out)
- Lernen: Anteil promoteter Antworten vs. Status quo

### Datenschutz & Datenhygiene

- Redaction: Namen/Orte/IDs durch Platzhalter; Export‑Prüfung vor Training
- Consent/Scope markieren (was darf ins Training)
- Retention: Rohlogs kurzlebig, kuratierte Datasets versioniert
- Audit: jede Promotion mit Quelle/Datum/Tests notieren

### Go/No‑Go Checkliste (aktiv zu pflegen)

- [ ] Tests/Typen PASS (2 Tage in Folge)
- [ ] RAG‑Minimum indexiert, Retriever‑Test PASS
- [ ] Redaction aktiv (keine PII in Logs/Datasets)
- [ ] Flags gesetzt: `RAG_ON`, `SHADOW_ON`, `CANARY_PCT`
- [ ] Stichprobe (Schattenmodus) ≥80% „Accept“

### Nächste Schritte (sofort, ohne Codeänderungen)

- [ ] Schattenmodus‑Logging mit Redaction intern aktivieren
- [ ] 10–20 Kern‑Dokumente (Memory‑Bundle + Schlüssel‑Canvases) indexieren (RAG‑Minimum)
- [ ] Wöchentlichen Review‑Slot (30–45 min) für Stichproben + Kurations‑Delta einplanen

## Editor‑Setup – .vscode‑Konsolidierung (Root‑zentriert)

Ziel: Ein einziges `.vscode/` im Repo‑Root, das Standard‑Tasks/Settings bereitstellt, ohne projekt‑spezifische Profile (Launch/CWD/ENV) zu beschädigen. Sanft, reversibel, mit Inventur vor Migration.

### Annahmen & Rahmen

- Root verwendet `.venv` (Windows) und zentralen Interpreter (`.vscode/settings.json`).
- `novapolis_agent` ist der einzige Code‑Bereich mit Tests/Launch‑Profilen; `novapolis-rp` ist primär Daten/Docs/Tools.
- Markdownlint läuft via cli2 in CI; lokale Tasks existieren in Agent‑Projekt (bereits erweitert um Root‑`TODO.md`/`DONELOG.md`).
- Aktueller Blocker: VS Code erkennt den Workspace als Multi‑Root; Wrapper‑Tasks laufen unzuverlässig. Vorgabe bis zur Bereinigung: KEINE WRAPPER – Terminal ausschließlich manuell nutzen.

### Akzeptanzkriterien

- Alle Standard‑Tasks sind vom Root aus ausführbar: Lint (markdownlint), Fix, `pytest -q`, Coverage (fail‑under 80).
- Tasks nutzen korrektes CWD und ENV: `cwd=novapolis_agent/`, `envFile=novapolis_agent/.env`, Interpreter aus Root `.venv`.
- Copilot‑Workspace‑Instructions zentral im Root; keine doppelten, widersprüchlichen Settings.
- Projekt‑spezifische Launch‑Profile funktionieren unverändert (zunächst im Agent‑Ordner belassen).

### Plan (Etappen)

- Etappe0 – Inventur (dieser PR‑Teil)
  - [ ] Vorab: Multi‑Root → Single‑Root bereinigen (Workspace aufräumen, eindeutige Root). Erst danach Wrapper‑Tasks reaktivieren.
  - [ ] Liste aller `.vscode`‑Dateien erstellen (Root, Agent, RP)
  - [ ] Settings/Launch/Tasks diffen und Konflikte notieren
  - [ ] Mapping definieren: was zentralisiert wird, was projekt‑spezifisch bleibt
- Etappe1 – Zentralisierung (additiv, ohne Löschen)
  - [ ] Root‑Tasks ergänzen: `pytest -q` (cwd Agent), `Tests: coverage (fail‑under)`, `markdownlint (cli2)`, `markdownlint fix (cli2)` (erledigt)
  - [x] Root‑Settings um Copilot‑Workspace‑Instructions aus RP ergänzen (keine Python‑Konflikte) - 2025-11-02: User-/Profil-Configs zurückgesetzt, nur Root-Settings aktiv
  - [ ] Agent‑Tasks optional auf Root‑Tasks verweisen (mittels eindeutiger Labels)
- Etappe2 – Bereinigung (nach 3–5Tagen stabiler Nutzung)
  - [ ] Dubletten entfernen oder Agent‑`tasks.json` auf Minimal‑Set reduzieren
  - [ ] Launch‑Profile optional ins Root migrieren (nur wenn stabil; sonst belassen)
  - [ ] Dokumentation: kurzer Abschnitt „Editor‑Setup“ im Root‑README

### Aufgabenliste (konkret)

- Inventur
  - [ ] Auflisten: `.vscode/settings.json` (Root, Agent, RP), `.vscode/tasks.json` (Root, Agent), `.vscode/launch.json` (Agent)
  - [ ] Unterschiede festhalten: Interpreter‑Pfad, pytestArgs, envFile, Copilot‑Instructions
- Root‑Tasks
  - [x] Markdownlint: lint/fix (cli2) repo‑weit (Root‑Tasks vorhanden)
  - [x] Tests: `pytest -q` (cwd=`novapolis_agent`)
  - [x] Tests: Coverage (fail-under=80) (cwd=`novapolis_agent`)
  - [x] Optional: „Append DONELOG entry“ als Root-Alias mit cwd `novapolis_agent` (2025-11-01 09:05)
    - Änderung: VS Code Task `DONELOG: append entry` in `/.vscode/tasks.json` ergänzt.
    - Prüfungen: keine (reine Task-Erweiterung).
- Root‑Settings
  - [x] Copilot-Workspace-Instructions aus `novapolis-rp/.vscode/settings.json` in Root übernehmen/vereinheitlichen
  - [x] Interpreter/pytestArgs zentral lassen; RP‑Settings entschlacken (keine Python‑Dopplung) - 2025-11-02: Profil-/User-Overrides entfernt, CWD/Interpreter nur noch im Root definiert
- Agent/RP Cleanup (Etappe2)
  - [ ] Agent‑`tasks.json` Dubletten entfernen, falls Root‑Tasks etabliert
  - [ ] RP‑Settings auf Workspace‑Instructions beschränken (falls Root diese zentral führt)

### Snapshot‑Frontmatter Migration (YAML)

- [ ] Etappe 0 (2025-11-01 09:10): Regel aktiv, Mischbetrieb erlaubt — YAML bevorzugt, `Stand:`/`Letzte Aktualisierung:` weiterhin gültig.
- [ ] Etappe 1: Bei Änderungen an Dokus YAML-Frontmatter ergänzen/aktualisieren (`stand`, `update`, `checks`).
- [ ] Etappe 2: Sweep — bestehende Kopfzeilen migrieren (TODO, README/Index, Policies). Diff klein halten; `checks` kurz.
- [ ] Etappe 3: Legacy-Kopfzeilen auslaufen lassen; Instruktionen aktualisieren (nur YAML erlaubt).
- Fortschritt 2025-11-02 19:11: Root-Dokumente (`README.md`, `todo.root.md`, `single-root-todo.md`, `DONELOG.md`, `WORKSPACE_STATUS.md`) tragen konsolidierte YAML-Frontmatter; markdownlint-cli2 PASS.

### Risiken & Backout

- Risiko: Falsches CWD/ENV führt zu fehlschlagenden Tasks.
  - Mitigation: Jede Task im Root mit `options.cwd=novapolis_agent` + `envFile` testen.
- Risiko: Launch‑Profile brechen bei Migration.
  - Mitigation: Launch zunächst im Agent belassen; Migration optional/später.
- Risiko: VS Code Multi‑Root‑Markierung verhindert stabile Task‑Ausführung.
  - Mitigation: Wrapper‑Tasks deaktivieren; bis zur Single‑Root‑Bereinigung ausschließlich manuelle Terminal‑Läufe.
- Backout: Sub‑`.vscode` beibehalten bis Etappe2; jederzeit reaktivierbar.

### Betroffene Dateien (geplant)

- `/.vscode/settings.json` (merge Workspace‑Instructions)
- `/.vscode/tasks.json` (ergänzte Root‑Tasks)
- `/novapolis_agent/.vscode/tasks.json` (später reduzieren)
- `/novapolis_agent/.vscode/launch.json` (vorerst unverändert)
- `/novapolis-rp/.vscode/settings.json` (später verschlanken)

### Go/No‑Go für Migration

- [ ] Root‑Tasks laufen (lint, fix, pytest, coverage)
- [ ] Keine Konflikte in Settings (Interpreter/ENV)
- [ ] 3–5Tage Nutzung ohne Beschwerden → Go für Etappe2

## Volltexte

<details>
<summary>Historischer Snapshot (Agent TODO, archiviert)</summary>

Autoritativer Stand:
- SSOT: `novapolis-dev/docs/todo.agent.md`
- Archiv: `novapolis-dev/archive/todo.agent.archive.md`

```markdown
<!-- markdownlint-disable MD013 -->
# Novapolis Agent – ToDo & Roadmap

Kurzfristige Ziele (Heute)

- [x] Eval-Profile festziehen
  - Ziel: Reproduzierbare Läufe via `eval/config/profiles.json` (quiet default, temp, optionale Checks).
  - Status: Done (UI lädt Profile; Meta-Header vollständig; kurzer ASGI-Lauf konsistent).
- [x] Eval-UI: Profile-/Quiet-/ASGI-/Skip-Preflight-Integration
  - Ziel: Läufe steuerbar über Profile, reduzierte Logs, In-Process-ASGI, Preflight optional.
  - Status: Done (Menü integriert, Flags wirksam, Trends/Exports ok).
- [x] Synonym-Overlay (privat) einführen und mergen
  - Ziel: `eval/config/synonyms.local.json` (gitignored) automatisch mit `synonyms.json` mergen.
  - Status: Done (Loader-Merge, Sample-Datei, Doku in README & eval/README, .gitignore ergänzt).
- [x] Eval-Pfade harmonisieren & Meta-Header erweitern
  - Ziel: Nutzung von `eval/datasets|results|config`, Meta mit overrides (model/host/temperature).
  - Status: Done (Runner/UI angepasst, Ergebnisse validiert).
- [x] Altlasten entfernen
  - Ziel: `app/routers/*`, redundante Prompt-Dateien, alte Helpers entfernen; Doku/Index bereinigen.
  - Status: Done (Bereinigt, Referenzen aktualisiert, Smoke-Eval grün).
- [x] Prompt-Schalter robust machen
  - Ziel: Klare Priorität DEFAULT > UNRESTRICTED > EVAL; saubere Systemprompt-Injektion.
  - Status: Done (Unit-Tests für Default/Unrestricted/Eval hinzugefügt und grün).
- [x] HTTP/Client-Reuse & Timeouts
  - Ziel: Wiederverwendbarer AsyncClient auch im HTTP-Modus + zentrale Timeouts.
  - Status: Done (process_chat_request akzeptiert geteilten AsyncClient; zentraler Timeout bleibt aktiv).
- [x] Unit-Tests: Synonym-Overlay-Merge
  - Ziel: Test, dass `synonyms.local.json` korrekt gemerged wird und fehlende Datei still ignoriert wird.
  - Status: Done (zwei Tests hinzugefügt, beide grün).

- [x] Pyright-Upgrade & Typwarnungen bereinigt
  - Status: Done (Pyright 1.1.406; 0 Fehler, 0 Warnungen im App-Bereich; Tests grün; tests/ & scripts/ vorerst aus Pyright-Analyse ausgeschlossen – schrittweise Reaktivierung geplant)

- [x] Markdownlint-Konfiguration & Tasks
  - Status: Done (Root `.markdownlint-cli2.jsonc` aktiv; VS Code Tasks für Lint/Fix; README/TODO/Customization bereinigt; Legacy `.markdownlint.json` entfernt)

1–2 Tage

- [x] Qualitäts-Heuristiken fürs RPG (stilistische Checks)
  - Status: Done (rpg_style-Score + Check; Unit-Tests hinzugefügt; per Checks-Liste aktivierbar)
- [x] Parameter-Sweeps (temperature, top_p, max_tokens)
  - Status: Done (Runner unterstützt Sweeps + Overrides; Tagging/Meta;
    Trends zeigt kompakte Aggregation; top_p end-to-end sichtbar)
- [x] Beobachtbarkeit (Korrelation-ID, JSON-Logs, Trunkierung)
  - Status: Done (Request-ID-Middleware; JSON-Logs für Requests/Errors;
    Trunkierung in Chat-Logs; RID-Weitergabe an Modell; strukturierte Model-Logs)
- [x] Rate-Limits/Schutzschalter Feintuning
  - Status: Done (Fenster/Limit/Burst konfigurierbar; Exempt Paths & Trusted IPs; informative Rate-Limit-Header; Tests grün)
- [x] Streaming-Antworten (optional)
  - Status: Done (POST /chat/stream liefert text/event-stream;
    serverseitige Chunk-Ausgabe via Ollama-Stream; Logs & Fehler-Ereignisse;
    kompatibel zu bestehender /chat API)

- [x] DONELOG-Disziplin auch für Agent-Änderungen
  - Ziel: Sicherstellen, dass direkte Pushes auf `main` ebenfalls einen DONELOG-Eintrag erfordern; bequemer Editor-Flow.
  - Status: Done (CI-Workflow prüft jetzt auch Push auf `main`;
    PR-Bypass via Label bleibt; VS Code Task "Append DONELOG entry" hinzugefügt.)

- [x] Mypy-Enforcement für weitere Skripte ausweiten
  - Ziel: Schrittweises Reduzieren von `[mypy-scripts.*] ignore_errors = True`;
    per Datei auf `check_untyped_defs = True` heben.
  - Kandidaten: `scripts/run_eval.py`, `scripts/eval_ui.py`,
    `scripts/curate_dataset_from_latest.py`, `scripts/openai_finetune.py`,
    `scripts/train_lora.py`.
  - Status: Done — Alle genannten Skripte sind jetzt auf `check_untyped_defs=True`
    gestellt und mypy-clean.

- Ziel: Mehr Edge- und Fehlerpfade testen (Streaming-Fehler, Timeout/Rate-Limit, dependency_check-Sonderfälle, Export/Prepare-Interop).
  - Hinweis: Windows-Pfade beachten (keine Laufwerks-Mismatches; projektwurzelnahe Temp-Verzeichnisse nutzen).
  - Gruppierung: pytest-Marker eingerichtet (unit, api, streaming, eval, scripts);
    VS Code Tasks für "Tests: unit" und "Tests: api+streaming" hinzugefügt.
  - Fortschritt:
    - Neue Tests für Rate-Limit/Timeout, Prompt-/Options-Parsing, Context-Notes,
      Settings-Validatoren, LLM-Service, Summaries.
    - Skript-Smokes erweitert (neu hinzugefügt):
      - `tests/scripts/test_todo_gather_smoke.py` → scripts/todo_gather.py (jetzt ~88%)
      - `tests/scripts/test_customize_prompts_smoke.py` → scripts/customize_prompts.py (jetzt ~48%)
      - `tests/scripts/test_map_reduce_summary_llm_smoke.py` → scripts/map_reduce_summary_llm.py (jetzt ~62%)
      - `tests/scripts/test_open_latest_summary_smoke.py` → scripts/open_latest_summary.py (Happy-Path, Print)
      - `tests/scripts/test_fine_tune_pipeline_smoke.py` → scripts/fine_tune_pipeline.py (Free‑Modell, --no-check, kurzer Pfad)
    - Ergebnis: Scripts-Zeilenabdeckung zuletzt ~67% (vorher ~60–65%);
      weitere Runden erhöht (letzte Messung 69% mit Branch-Coverage,
      erneute Messung steht an).
    - Zusätzlich: Beispiel‑Test `tests/test_chai_checks.py` prüft `check_term_inclusion`
      inkl. Synonym‑Erkennung.
  - Nächste Schritte:
    - [x] Integrationstest: alpaca Export→Prepare
      - Test: `tests/scripts/test_export_and_prepare_pipeline_alpaca.py` (Export alpaca → Prepare-Pack; Train/Val erzeugt)
    - [x] Weitere Edge-Tests ergänzt (export_finetune, open_context_notes, rerun_failed, fine_tune_pipeline)
    - [x] 3+1 Testrunde (customize_prompts, map_reduce_summary, fine_tune_pipeline + /health Header)
      - Resultat: Suite grün; Scripts-Coverage ~75% (Branch-Coverage aktiv)
    - [x] 3+1 Testrunde (map_reduce_summary Python/JSON, rerun_failed JSON-Array, export_finetune Fallback + /404 Header)
      - Resultat: Suite grün; Scripts-Coverage ~78%
    - [x] 3+1 Testrunde (fine_tune_pipeline fp16/KeyboardInterrupt, export_finetune openai_chat include_failures, /chat/stream Fehler-SSE)
      - Resultat: Suite grün; Scripts-Coverage stabil ~78%
    - [x] 3+1 Testrunde (migrate_dataset_schemas Happy-Path, openai_ft_status Snapshot+Follow, [App-Test bereits enthalten])
      - Resultat: Suite grün; Scripts-Coverage ~79%
    - [x] 3+1 Testrunde (audit_workspace Fallback, curate_dataset_from_latest Minimal, open_context_notes Happy, /chat Fehlerpfad)
      - Resultat: Suite grün; Scripts-Coverage stabil ~79%
    - [x] Scripts-Coverage erneut messen und gezielt ≥80% anstreben
      - Erreicht: 80% (Branch-Coverage aktiv)
      - Neu hinzugefügt:
        - tests/scripts/test_curate_dataset_filters_empty.py (Filter führen zu Exit 5)
        - tests/test_audit_workspace_references.py (scan_text_references findet Referenzen)
        - tests/test_app_root_request_id.py (X-Request-ID Header auf /)
      - Messung: vollständige Suite mit --cov=scripts --cov-branch

- [x] Pre-commit-Hook für DONELOG
  - Ziel: Commit verhindern, wenn Code unter `app/|scripts/|utils/` geändert wurde,
    aber kein aktueller DONELOG-Eintrag vorliegt (Jahres-/Datumscheck).
  - Optional: Interaktiv `scripts/append_done.py` aufrufen.
  - Optional (lokal vorbereitet): `.githooks/pre-commit` + VS Code Tasks
    - Installieren: Task "Git hooks: install local pre-commit"
    - Prüfen: Task "Git hooks: verify pre-commit"
    - Manuell ausführen: Task "Pre-commit: run check"
  - Status: Done (Hook aktiv; erweitert um markdownlint-Prüfung mit Auto-Fix für geänderte .md)

- [x] VS Code Tasks normalisieren (Portabilität)
  - Ziel: Harte `F:/`-Pfade durch `${workspaceFolder}` & `${config:python.interpreterPath}` ersetzen; konsistente CWD-Optionen.
  - Bonus: Tasks für `mypy`, `pyright`, `pytest -q`, `scripts/dependency_check.py` hinzufügen.
  - Status: Done (Tasks portabel; Pyright/Mypy ProblemMatcher; Markdownlint
    Lint/Fix Tasks ergänzt; Windows-Optimierungen für Hook-Tasks und
    Markdownlint-Fallback)

## Coverage-Ziele & Tasks

- Ziele (vereinbart):
  - App: ≥85% Zeilen, ≥75–80% Branches (inkrementell anziehen)
  - Scripts: ≥60% Zeilen (Basis, später anheben)
  - Kombiniert: Fail-Under=80 (angezogen)
- VS Code Tasks:
  - "Tests: coverage app (≥85%)"
  - "Tests: coverage scripts (≥60%)"
  - "Tests: coverage (fail-under)" (kombiniert, 80)

### Zusätzliche kurzfristige Abschlüsse (2025-10-21)

Hinweis: Abschnitt am 2025-11-02 08:38 in `novapolis-dev/archive/todo.root.archive.md` archiviert.

### Zusätzliche kurzfristige Abschlüsse (2025-10-22)

Hinweis: Abschnitt am 2025-11-02 08:40 in `novapolis-dev/archive/todo.root.archive.md` archiviert.

### Kurz-Update (2025-10-25)

Hinweis: Abschnitt am 2025-11-02 08:36 in `novapolis-dev/archive/todo.root.archive.md` archiviert.

Hinweise:

- Branch-Coverage ist in `.coveragerc` aktiviert; schwere/interactive Skripte sind ausgeschlossen.
- Zielwerte werden sukzessive angehoben, sobald Teilbereiche stabil darüber liegen.

### 3–7 Tage

#### Datensatzkurierung aus Logs (Train/Val-Pack)

- [ ] Datensatzkurierung (gesamt)
- [x] Skript `scripts/curate_dataset_from_latest.py` erstellt
- [x] Export (openai_chat/alpaca) möglich
- [x] Dedupe & Train/Val‑Split umgesetzt
- [x] VS Code Task „Curate dataset (latest)“ vorhanden
- [x] `app/core/settings.py`: `EVAL_FILE_PATTERN` auf `eval-*.json*` erweitert
- [x] `scripts/export_finetune.py`: nutzt `source_file` aus Results zur zuverlässigen Zuordnung
- [ ] Kurze Kuratierungs‑Doku/Kochrezept ergänzen (Ablauf, Parameter, Outputs)

#### Fine-Tuning/LoRA Mini-Pipeline

- [x] Smoke‑Run (Mini‑LoRA) durchgeführt
  - 10 Schritte (TinyLlama), Artefakte unter `outputs/lora-chai-mini-0937/` dokumentiert.
- [x] Trainings‑Doku (Minimalablauf) vorhanden
  - Verweis: `novapolis_agent/docs/training.md` (Basisablauf, Optionen, Hinweise).
- [ ] Reproduzierbarer Task/Profil (VS Code/CLI)
  - Ziel: Standard‑Task oder klarer CLI‑Befehl mit Parametern; stabile Pfade/ENV.
- [ ] Qualitätsgatter & Artefakte
  - Ziel: Mindestmetrik(en) definieren (z. B. loss‑Trend/val‑score) und Ausgabe standardisieren.

#### Caching/Memoization für Eval-Reruns

- [x] Eval-Caching (Basis) per `--cache`
  - Hinweis: Antworten werden optional in `eval/results/cache_eval.jsonl` persistiert; Key = messages+options+model+eval_mode.
- [ ] Memoization für Eval-Reruns (Wiederholungen überspringen)
  - Ziel: Wiederholte Ausführungen per persistentem Index/Map vermeiden (über Session/Run-Grenzen hinaus); CLI-Optionen + Tests.

#### Rerun-Failed mit Profil/Meta-Rekonstruktion

- [x] Rerun-Failed mit Profil/Meta-Rekonstruktion
  - `scripts/rerun_from_results.py` rekonstruiert Model/Host/Temperature/Checks aus Meta
  - ASGI/HTTP unterstützt
  - Smoke-Test vorhanden

- [x] Mini-Eval → Export → Split → LoRA (Smoke)
  - Ziel: 10–20 Items evaluieren (quiet/ASGI), `openai_chat` exportieren, Split erzeugen,
    kurze LoRA-Trainingsprobe (max 10 Steps) mit `--only-free` oder lokalem Modell.
  - Output: Artefakte in `eval/results/finetune/`, Trainingslogs und Metriken festhalten.
  - Status: Done (chai-Profil)
    - Eval: 15 Items (ASGI/quiet) aus `eval/datasets/chai-ai_small_v1.jsonl` → `eval/results/results_20251016_0930.jsonl`
    - Kuratierung: `openai_chat` Export + Split → Train (13) / Val (2)
    - Validation: `scripts/openai_finetune.py ... --validate-only` → VALIDATION_OK
    - LoRA Mini: 10 Schritte (TinyLlama), Output: `outputs/lora-chai-mini-0937/`
    - Begleitende Verbesserungen: Checks vereinfacht; Synonyms‑Overlay erweitert; Test `tests/test_chai_checks.py` hinzugefügt.

- [x] Eval-Caching (Basis)
  - Status: Done — Optional per `--cache`
    - Speichert Antworten in `eval/results/cache_eval.jsonl`
    - Key: messages+options+model+eval_mode
    - Reruns folgen separat

- [x] Dedupe/Heuristiken für Trainingsdaten schärfen (Basis)
  - Status: Done — `prepare_finetune_pack.py` unterstützt `--near-dup-threshold` (Token‑Jaccard) zusätzlich zur Instruktions‑Dedupe.

- [x] Dokumentation Training/Feinabstimmung
  - Status: Done — `docs/training.md` (Minimalablauf, Optionen, Hinweise).

### Kurzfristig (nächste Iterationen)

Hinweis: Abschnitt am 2025-11-02 08:07 in `novapolis-dev/archive/todo.root.archive.md` archiviert.

### Neu (Backups & Releases)

- [x] Backup-Repo (Release-Assets) erstellt und initial befüllt
  - Neues GitHub-Repo; Snapshot als Release-Assets (ZIPs, gesplittete .venv-Parts).
- [x] Checksums & Restore-Doku ergänzt
  - MANIFEST mit SHA-256; README mit Restore-Anleitung (Parts zusammenfügen, Verifikation).
- [ ] Optional: Verschlüsselung (7‑Zip AES‑256) für sensible Artefakte vorbereiten

### Kurz-Update (2025-10-20)

Hinweis: Abschnitt am 2025-11-02 08:34 in `novapolis-dev/archive/todo.root.archive.md` archiviert.

### Offene Punkte (Kurzfristig)

Hinweis: Abschnitt am 2025-11-02 09:00 in `novapolis-dev/archive/todo.root.archive.md` archiviert.

### Neu: Reports‑Standard

Hinweis: Abschnitt am 2025-11-02 08:45 in `novapolis-dev/archive/todo.root.archive.md` archiviert.

Später

- Narrativspeicher (Session Memory)
- Formale Stil-Guidelines + Tests
- Tooling (pre-commit, ruff/black, pins)

- CI/Qualitätstore
  - Ziel: Optionales Coverage-Minimum in CI (z. B. Zeilen/Branches), Linting (ruff/black)
    und Format-Checks per Pre-commit & CI.

- Packaging & Deployability
  - Ziel: Healthchecks und Produktionshinweise.

### Mittelfristig

- [~] Tool‑Use/Function‑Calling (Basis)
  - Ziel: 2–3 sichere Tools (Rechnen, lokale Datei‑Sandbox, einfache Korpus‑Suche) per ReAct‑Prompting,
    Policy‑basiert freischaltbar; Protokollierung.
  - Fortschritt: Basis‑Scaffold umgesetzt
    - Settings: `TOOLS_ENABLED` (bool), `TOOLS_WHITELIST` (Liste) hinzugefügt.
    - Registry: `app/tools/registry.py` mit `register_tool/list_tools/is_allowed/call_tool`.
    - Built‑in Tool: `calc_add` (Addition mit Float‑Coercion).
    - Tests: `tests/test_tools_basic.py` (unit) prüft Deny by default, Allow per Whitelist, Unknown Tool.
  - Nächste Schritte:
    - Logging/Protokollierung der Tool‑Aufrufe (RID, Dauer, Args‑Redaktion) ergänzen.
    - Optional: Weitere Tools (z. B. `safe_eval_math`, `sandbox_ls` mit strikten Pfaden) + Policy‑Bindung.
    - Chat‑Integration (ReAct‑Stil) hinter Flag verdrahten.

- [ ] RAG (lokal)
  - Ziel: FAISS oder Qdrant; Indexer für Markdown/Text; Query‑Augmentation; konfigurierbar offline.
  - Akzeptanz: Indexer‑Script + Retrieval‑Hook; deterministische Tests (Treffer/Kein‑Treffer).

- [ ] Profile/Personas
  - Ziel: Profile/JSON (Prompts/Policies/Options), Auswahl via Header/Token/Session.
  - Akzeptanz: Validierung + Anwendungslogik; Tests: Profilwechsel wirkt.

- [ ] Evaluierung & Telemetrie
  - Ziel: Policy‑Coverage‑Tests; Metriken (Latenz p50/p95, Länge, RAG‑HitRate); strukturierte Logs.
  - Akzeptanz: Berichte in `eval/results/reports/metrics/` mit Zeitstempel (z. B. `YYYYMMDD_HHMM`); mind. 3 Kennzahlen.

### Langfristig

- [ ] Admin‑UI/Settings
  - Ziel: UI zur Steuerung von Policies/Profilen/Sessions; Live‑Logs/Health; Schutz (AuthN/Z optional).
  - Akzeptanz: Minimal‑UI mit 2–3 Screens; Read/Write Policies; Tests (smoke).

- [ ] Persistenter Memory‑Store & DSGVO‑Löschung
  - Ziel: SQLite/Postgres Speicherung + „Right to be forgotten“‑Routinen; Export/Pruning.
  - Akzeptanz: CRUD + Purge; Tests für Löschpfade.

- [ ] Skalierung/Resilienz
  - Ziel: Worker/Queue, Retry/Timeout‑Policies, Backpressure; Limits observabel.
  - Akzeptanz: Stresstest‑Skript + Metriken.

### Kleine Auffälligkeiten / Verbesserungen

- [x] Einheitliches Message‑Schema
  - Ziel: `ChatRequest.messages` akzeptiert `ChatMessage` und dicts; Validator normalisiert Einträge.
  - Status: Done — Pydantic‑Validator ergänzt; Tests hinzugefügt (`tests/test_messages_schema.py`); Flow bleibt rückwärtskompatibel.

- [x] Streaming‑Meta/Fehler-Modell
  - Ziel: Ersten SSE‑Meta‑Event (Params/Mode/RID) senden; Fehler zusätzlich protokollieren.
  - Status: Done — Erster `event: meta` mit `{params: {mode, request_id, model, options}}` wird zu Beginn des Streams gesendet; bestehendes Policy‑Meta/Delta am Ende bleibt erhalten.
  - Akzeptanz: Tests prüfen Meta‑Event + Error‑Event (neu: `tests/test_streaming_initial_meta.py`; bestehende Error‑/Policy‑Tests grün).

- [ ] Settings/Options erweitern
  - Ziel: Mehr Ollama‑Optionen exponieren, klar dokumentieren; Defaults in Settings.
  - Akzeptanz: Doku + Validation‑Tests.

- [x] AGENT_BEHAVIOR.md: DONELOG Autoren‑Definition präzisieren
  - Ziel: In `AGENT_BEHAVIOR.md` ergänzen, dass der Autor in `docs/DONELOG.txt` die Herkunft des Vorschlags widerspiegelt (z. B. „Panicgrinder“ für Benutzer‑/Owner‑Vorschläge; „Copilot“ für automatisch initiierte/umgesetzte Vorschläge).
  - Akzeptanz: Abschnitt „Regel: Abgeschlossene Arbeiten dokumentieren (DONELOG)“ erweitert; konkrete Beispiele hinzugefügt.

</details>

Metriken

- Eval-Erfolgsrate ↑ (gesamt/paketweise)
- Latenz p95 ↓
- 0 RPG-Erkennungen im Eval-Modus; konsistenter RP-Stil im UNRESTRICTED
- Trainingspacks: dedupliziert, ausgewogene Längen
- Logs strukturiert, korrelierbar, ohne sensible Leaks

- Abdeckung: inkrementelle Erhöhung (z. B. +5–10 Prozentpunkte über mehrere Iterationen); Gate optional.

---

Regel: Abgeschlossene Arbeiten dokumentieren (DONELOG)

- Jede nicht-triviale, abgeschlossene Änderung bitte in `docs/DONELOG.txt` erfassen.
- Format je Zeile: `YYYY-MM-DD HH:MM | Author | Kurzbeschreibung` (keine sensiblen Inhalte!).
- Helferskript: `python scripts/append_done.py "Kurzbeschreibung..."` hängt automatisch Zeitstempel und Autor an.
- CI: PRs mit Code-Änderungen (app/, scripts/, utils/) erfordern einen DONELOG-Eintrag; Bypass via Label `skip-donelog` möglich.
- Zusätzlich: Pushes auf `main` werden ebenfalls geprüft. Für Push-Events gibt es keinen
  Label-Bypass. Falls nötig, zuvor `docs/DONELOG.txt` aktualisieren.
- VS Code Task: "Append DONELOG entry" fragt nach einer Kurzbeschreibung und ruft
  `scripts/append_done.py` mit dem aktiven Python-Interpreter auf.

## Roadmap Nächste Schritte (Agent-Funktionen)

- [ ] Session‑Memory (Kurz/Mittelfrist)
  - Ziel: Gesprächskontext je `session_id` persistieren (In‑Memory + optional JSONL/SQLite),
    Fenster/Trunkierung (Token/Chars), konfigurierbar über Settings.
  - Akzeptanzkriterien:
    - `ChatRequest.options.session_id` wird akzeptiert.
    - Vorherige Turns werden geladen und in die Messages eingebettet (Budget‑basiert).
    - Tests: Happy‑Path + Trunkierung + „No Memory“ Fallback.

- [ ] Policy/Rules‑Engine („eigene Regeln statt externer“)
  - Ziel: Pre‑/Post‑Prompt‑Hook mit Policies (ENV/policy.json), Umschaltung per Modus/Profil
    (eval/unrestricted/profile_id).
  - Akzeptanzkriterien:
    - Hook in `process_chat_request`/`stream_chat_request` aktiv.
    - Policies anwendbar (Allow‑All/Rewrite/Verbote); Ereignisse werden geloggt.
    - Tests: Policy wirkt (Rewrite/Block), Protokollierung vorhanden.

- [ ] Tool‑Use/Function‑Calling (Basis)
  - Ziel: 2–3 sichere Tools (z. B. Rechnen, lokale Datei‑Lesen in Sandbox, einfache Suche im Korpus)
    mit ReAct‑Prompting, per Policy freischaltbar.
  - Akzeptanzkriterien:
    - Tool‑Katalog (registriert, Whitelist), Aufrufe werden protokolliert.
    - Tests: mindestens ein Tool End‑to‑End (Stub/Offline), Policy Off/On.

- [ ] RAG (lokal, optional)
  - Ziel: Einfaches Retrieval (zunächst TF‑IDF; perspektivisch FAISS/Qdrant), Indizierung für Markdown/Text, Query‑Augmentation.
  - Akzeptanzkriterien:
    - Indexer‑Script + Retrieval‑Hook; deterministische Tests (Treffer/Kein‑Treffer).

- [ ] Profile/Personas
  - Ziel: Profile als JSON (Prompts/Policies/Options), Auswahl via Header/Token/Session.
  - Akzeptanzkriterien:
    - Profile werden geladen, validiert und angewandt.
    - Tests: Profilwechsel beeinflusst Prompt/Optionen/Policy.

- [ ] Evaluierung & Telemetrie
  - Ziel: Policy‑Coverage‑Tests; Metriken (Latenz p50/p95, Länge, RAG‑HitRate); strukturierte Logs.
  - Akzeptanzkriterien:
    - Berichte in `eval/results/reports/metrics/` mit Zeitstempel (z. B. `YYYYMMDD_HHMM`); mind. 3 Kennzahlen.

### Langfristig

- [ ] Admin‑UI/Settings
  - Ziel: UI zur Steuerung von Policies/Profilen/Sessions; Live‑Logs/Health; Schutz (AuthN/Z optional).
  - Akzeptanz: Minimal‑UI mit 2–3 Screens; Read/Write Policies; Tests (smoke).

- [ ] Persistenter Memory‑Store & DSGVO‑Löschung
  - Ziel: SQLite/Postgres Speicherung + „Right to be forgotten“‑Routinen; Export/Pruning.
  - Akzeptanz: CRUD + Purge; Tests für Löschpfade.

- [ ] Skalierung/Resilienz
  - Ziel: Worker/Queue, Retry/Timeout‑Policies, Backpressure; Limits observabel.
  - Akzeptanz: Stresstest‑Skript + Metriken.

### Kleine Auffälligkeiten / Verbesserungen

- [x] Einheitliches Message‑Schema
  - Ziel: `ChatRequest.messages` akzeptiert `ChatMessage` und dicts; Validator normalisiert Einträge.
  - Status: Done — Pydantic‑Validator ergänzt; Tests hinzugefügt (`tests/test_messages_schema.py`); Flow bleibt rückwärtskompatibel.

- [x] Streaming‑Meta/Fehler-Modell
  - Ziel: Ersten SSE‑Meta‑Event (Params/Mode/RID) senden; Fehler zusätzlich protokollieren.
  - Status: Done — Erster `event: meta` mit `{params: {mode, request_id, model, options}}` wird zu Beginn des Streams gesendet; bestehendes Policy‑Meta/Delta am Ende bleibt erhalten.
  - Akzeptanz: Tests prüfen Meta‑Event + Error‑Event (neu: `tests/test_streaming_initial_meta.py`; bestehende Error‑/Policy‑Tests grün).

- [ ] Settings/Options erweitern
  - Ziel: Mehr Ollama‑Optionen exponieren, klar dokumentieren; Defaults in Settings.
  - Akzeptanz: Doku + Validation‑Tests.

