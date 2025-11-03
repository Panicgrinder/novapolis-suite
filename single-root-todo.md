---
stand: 2025-11-03 23:22
update: Frontmatter (YAML) korrigiert; Checks in YAML verschoben.
checks: keine
---

<!-- markdownlint-disable MD022 MD041 -->

# Single Root TODO (Novapolis Suite)

Dieses Dokument bietet eine zentrale, lesefreundliche Übersicht über alle laufenden Arbeiten im Monorepo. Die fachlichen Single Sources of Truth (SSOT) bleiben in den Modul-TODOs unter `novapolis-dev/docs/` erhalten.

## Hinweise

- SSOT: Modul-TODOs bleiben maßgeblich. Diese Datei dient als komfortabler Root-Einstieg.
- Archivierung: Fertige Blöcke (alle [x]) bitte in die jeweiligen Modul-Archive unter `novapolis-dev/archive/` verschieben.
- Snapshot-Kopf: YAML-Frontmatter oben bei Änderungen aktualisieren (`stand`, `update`, `checks`).
- Lint: Markdownlint läuft repo-weit via npx/Task. Bei FAIL bitte minimalen Patch anwenden.
- Terminal/Pwsh: Standard ist jetzt PowerShell 7 (`pwsh`). Bei allen manuellen Aufrufen `-NoProfile` verwenden, um Störungen durch Profilskripte zu vermeiden. Die VS Code Tasks sind bereits entsprechend konfiguriert (z. B. `pwsh -NoProfile -Command '…'`).
- STOP-Hinweis: „Grün“ gilt nur bis zur nächsten Abweichung/Unsicherheit – dann STOP, Rückfrage, weiter nach Freigabe. Details: `.github/copilot-instructions.md` → Abschnitt „Unklarheiten‑STOP (global, immer gültig)“.

## Kurzüberblick (Module & Quellen)

- Index: `novapolis-dev/docs/todo.index.md`
- Agent: `novapolis-dev/docs/todo.agent.md`
- Dev: `novapolis-dev/docs/todo.dev.md`
- RP: `novapolis-dev/docs/todo.rp.md`
- Sim: `novapolis-dev/docs/todo.sim.md`
- Root-Übersicht (ausführlich): `todo.root.md`

## Offene Aufgaben (Root – quer durchs Repo)

- [x] .vscode-Konsolidierung (Root-zentriert) weiterführen (Etappen 0–2)
  - Referenz: Abschnitt "Editor‑Setup – .vscode‑Konsolidierung (Root‑zentriert)" in `todo.root.md`.
  - 2025-11-02: User- und Profil-Settings bereinigt; nur `/.vscode/settings.json` bleibt maßgeblich.
- [x] Snapshot-Frontmatter-Migration vorantreiben (Etappen 1–3)
  - YAML-Frontmatter sukzessive ergänzen; bei Sweeps Diff klein halten.
  - Scope (Dateien/Pfade): Root-Dokumente (`README.md`, `todo.root.md`, `single-root-todo.md`, `WORKSPACE_STATUS.md`), `novapolis-dev/docs/**/*.md`, `novapolis_agent/docs/**/*.md`, ausgewählte `novapolis-rp/**/docs/**/*.md`. Ausnahmen beibehalten: `.github/copilot-instructions.md` ohne YAML-Frontmatter.
  - Root-Dokumente abgeschlossen am 2025-11-02 19:11; nächster Sweep: `novapolis-dev/docs/**/*.md`.
  - Vorgehen:
    1. Scan: Markdown-Dateien ohne YAML-Frontmatter oder mit Legacy-Header (`Stand:`, `Letzte Aktualisierung:`) identifizieren.
    2. Migration: YAML-Frontmatter am Dokumentanfang einfügen (Schlüssel: `stand`, `update`, `checks`). Legacy-Kopfzeilen nach YAML überführen, bestehende MD-Lint-Disable-Kommentare unterhalb der Frontmatter belassen.
    3. Validierung: `markdownlint-cli2` laufen lassen; einheitlicher Heading-Stil je Datei (MD003=consistent) sichern.
    4. Sonderfälle: Dateien mit Parser-Einschränkungen im Fallback-Format belassen (Klartext-Kopfzeile), generierte/kuratierte Bereiche gemäß CLI2-Ignores ausnehmen.
    5. Batch-Strategie: In kleinen Sweeps (10–20 Dateien) migrieren; Minimal-Delta, semantisch neutrale Änderungen, jeweils DONELOG-Notiz.
  - Akzeptanzkriterien (Migration):
    - YAML-Frontmatter vorhanden und korrekt befüllt; keine doppelten Kopfzeilen.
    - Lint PASS (markdownlint-cli2), keine neuen Regelverstöße.
    - Interne Anker/Links unverändert funktionsfähig.
    - Snapshot-Zeitstempel (`stand`) und Kurznotiz (`update`) pro Commit aktualisiert.
  - 2025-11-02: README.md auf YAML-Frontmatter migriert (lint PASS).
  - 2025-11-02: WORKSPACE_STATUS.md aktualisiert (PowerShell 7.5.4 via VS Code Extension).
  - 2025-11-02: Tasks & Hooks auf `pwsh`-Standard umgestellt (Settings, Tasks, pre-commit, Snapshot-Gate).
  - 2025-11-02: `.gitignore` erweitert – Godot-Editor-Binaries (`novapolis-sim/Godot_v*.exe`) bleiben lokal.
  - 2025-11-02: `novapolis-dev/docs/todo.{index,dev,sim}.md` auf YAML-Frontmatter (mit `---`-Delimiter) gebracht; Lint docs focused PASS.
  - 2025-11-02: `novapolis-dev/docs/donelog.md` und `novapolis-dev/docs/tests.md` mit YAML-Frontmatter versehen; Lint docs focused PASS.
  - 2025-11-02: `novapolis_agent/docs/*` (7 Dateien) mit YAML-Frontmatter versehen; Lint docs focused PASS.
  - 2025-11-02: RP‑Docs unter `novapolis-rp/**/docs/**` sind Redirect-/Mirror‑Stubs → keine Migration nötig.
- [x] Tree-Snapshots aktualisieren bei Strukturänderungen
  - Tasks: "Workspace tree: full", "Workspace tree: directories", "Workspace tree: summary (dirs)".
- [ ] Backups & Releases (Manifest/Checksums/Rotation) pflegen
  - [x] Audit dokumentiert: `Backups/AUDIT.md`
  - [x] Skripte ergänzt: `scripts/update_backups_manifest.ps1`, `scripts/rotate_backups.ps1`
  - [x] README + initiales Manifest: `Backups/README.md`, `Backups/manifest.v1.json`
  - [x] Bundles umbenennen (Schema) & Rotation-Läufe dokumentieren (`rotation.log`)
    - 2025-11-03 00:28: `cvn-agent-main.bundle` → `cvn-agent-main-20251103-0028-rev1.bundle` (sha256 protokolliert)
    - 2025-11-03 00:28: `novapolis_agent.bundle` → `novapolis-agent-backup-20251103-0028-rev1.bundle` (sha256 protokolliert)

## Modul-Fokus (Auszüge – bitte in den SSOTs pflegen)

### Agent (Backend)

- Quelle: `novapolis-dev/docs/todo.agent.md`
- [ ] TTS/Coqui – Exporter & Mini-Service (Planung)
- [ ] VS Code Tasks für TTS-Fluss (Planung)
- [ ] Templates `knowledge:/actions:` (nur Doku-Verlinkung)

### Dev (Tooling/Infra)

- Quelle: `novapolis-dev/docs/todo.dev.md`
- [ ] MCP-Server-Prototyp (lokal, Minimal)
- [ ] Annotation-/Scheduler-/TTS-Specs vervollständigen
- [ ] Templates für `knowledge:` und `actions:` bereitstellen

### RP (Kanon/Canvas)

- Quelle: `novapolis-dev/docs/todo.rp.md`
- [ ] Canvas-Rettung Sprint 1 – nächste Charaktere/Blöcke
- [ ] Logistik/Inventar konsolidieren (C6/D5)
- [ ] Validatoren/Indexe nachziehen (Behavior/Psymatrix)

### Sim (Godot)

- Quelle: `novapolis-dev/docs/todo.sim.md`
- [ ] Epoch-Loader (24×1h) + OGG-Playback
- [ ] Event-Signals (on_action_start/end, ...)
- [ ] Scheduler-Hook vorbereiten

## Pflege & Regeln

- DONELOG-Pflege: Substanzielle Arbeiten bitte in den passenden DONELOG eintragen (`novapolis-dev/docs/donelog.md` bzw. `novapolis_agent/docs/DONELOG.txt`).
- Minimal-Delta: Kleine, zielgerichtete Patches; Redirect-/Mirror-Stubs erst nach Link-Prüfung entfernen.

## Monorepo Single Root – Umstellungsplan (Schritt für Schritt)

Zielbild: Eine Wahrheit im Root (`/Main`), eine Python-Umgebung im Root (`.venv`), zentrale Tasks/Settings. Module sind „dumme“ Unterordner ohne eigene Interpreter/Tasks. Tests werden nur dort entdeckt/ausgeführt, wo sie hingehören.

### Etappe 0 – Inventur & Freeze

- [ ] Liste aller abweichenden Interpreter-/Tasks-/Launch-Settings erfassen
  - Orte: `**/.vscode/settings.json`, `**/.vscode/tasks.json`, `**/.vscode/launch.json`
  - Akzeptanz: Tabelle mit Pfad → Abweichung → Entscheidung (behalten/zentralisieren/entfernen)
- [ ] Soft-Freeze: Keine neuen Modul-Tasks/Interpreter-Overrides bis Abschluss Etappe 2
- [ ] Kommunikation: Kurznotiz im Root-README und im Dev-Hub-Index

Inventur-Status (2025-11-02 12:05):

- Gefunden:
  - `/.vscode/settings.json` → Interpreter zentral (`.venv`) und CWD/Env für Agent gesetzt – behalten
  - `/.vscode/launch.json` → CWD=`novapolis_agent`, keine Modul-Interpreter – behalten
  - `/novapolis-rp/.vscode/settings.json` → kein Interpreter-Override – behalten
- Nicht gefunden: modulare `tasks.json`-Overrides (Stand jetzt keine vorhanden)

### Etappe 1 – Eine venv im Root, Interpreter zentral

- [ ] Root-Umgebung anlegen/vereinheitlichen: `.venv/` im Root; Dependencies aus `requirements*.txt` installieren
- [ ] VS Code: Interpreter im Root setzen (Workspace-Level); alle Ordner-Overrides entfernen
  - Akzeptanz: Python-Interpreter zeigt überall auf `${workspaceFolder}/.venv` (bzw. Python aus dieser venv)
- [ ] Entfernen/Neutralisieren von Modul-Interpreter-Hinweisen
  - Dateien prüfen: `novapolis_agent/.vscode/settings.json`, `novapolis-rp/.vscode/settings.json`, `novapolis-sim/.vscode/settings.json`
  - Akzeptanz: Keine interpreterPath-/defaultInterpreterPath-Overrides außerhalb des Root mehr vorhanden

Optionale Befehle (Pwsh):

```powershell
# Root venv erstellen (Windows, pwsh)
py -3 -m venv .venv
\.venv\Scripts\Activate.ps1
pip install -U pip
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

### Etappe 2 – Tasks zentral, CWD gezielt

- [ ] Root `.vscode/tasks.json`: Alle Standard-Tasks hier definieren
  - Lint: `markdownlint-cli2` (repo-weit)
  - Tests: `pytest -q` (cwd=`novapolis_agent`), Coverage (cwd=`novapolis_agent`)
  - DONELOG-Append (cwd=`novapolis_agent`)
  - Optional: `ruff` (lint/fix), `black` (format)
- [ ] Modul-Tasks deaktivieren/entfernen (nach Verifikation)
  - Akzeptanz: Start aller Prüf-/Test-Tasks aus Root; Modul-Tasks nicht mehr erforderlich
- [ ] ENV bleibt Root: Keine Modul-spezifischen `envFile`/Interpreter-Zuweisungen

### Etappe 3 – Test-Discovery steuern (nur dort, wo Tests sind)

- [ ] Testlauf standardisieren: Root-Task „Tests: pytest (-q)“ mit `cwd=novapolis_agent`
- [ ] Exklusion anderer Ordner absichern
  - Variante A (bevorzugt): `cwd` strikt auf `novapolis_agent`
  - Variante B: Root-`pytest.ini` mit `testpaths = novapolis_agent/tests` (falls Root-Run ohne cwd genutzt wird)
- [ ] Godot-/Datenordner von Testdiscovery ausschließen (falls Root-Discovery aktiv)
  - Akzeptanz: `pytest -q` findet ausschließlich Agent-Tests

### Etappe 4 – Lint/Format global vereinheitlichen

- [ ] Markdownlint: eine zentrale Config (`.markdownlint-cli2.jsonc`) – bereits vorhanden
- [ ] Python: `ruff` (Lint/Fix) und `black` (Format) zentral konfigurieren (Root `pyproject.toml`)
  - Tasks ergänzen: `lint:ruff`, `fix:ruff`, `format:black`
  - Akzeptanz: Ein Satz Regeln, keine Modul-Sonderwege
- [ ] Optional: Pre-commit-Hooks auf Root-venv umstellen

### Etappe 5 – Aufräumen & CI-Angleichung

- [ ] Entfernte/neutralisierte Modul-Settings final löschen (nach 3–5 Tagen stabiler Nutzung)
- [x] CI-Workflows prüfen und auf Root-Tasks/Configs mappen
  - Lint → markdownlint-cli2, ruff/black
  - Tests → pytest (cwd=novapolis_agent)
  - Akzeptanz: CI spiegelt lokalen Root-Flow

Notiz (2025-11-02 11:35): CI im Root ergänzt:
- `.github/workflows/ci.yml` (Python): pyright+mypy+pytest mit `working-directory=novapolis_agent`.
- `.github/workflows/validate-rp.yml` (RP-Validatoren): Node/PS1-Varianten auf Rootpfade umgestellt.
- `.github/workflows/enforce-donelog.yml` (DONELOG-Prüfung): Pfade auf `novapolis_agent/docs/DONELOG.txt` angepasst.

### Workflows (Root-only Zielbild)

- [x] Modul-Workflows entfernen oder migrieren (Root-only):
  - `novapolis_agent/.github/workflows/ci.yml`
  - `novapolis_agent/.github/workflows/enforce-donelog.yml`
  - `novapolis-rp/.github/workflows/validate.yml`
- [x] Root-Workflows finalisieren (nur unter `/.github/workflows/*.yml`):
  - `ci.yml` (Python, cwd `novapolis_agent`)
  - `validate-rp.yml` (RP-Validatoren)
  - `markdownlint.yml` (global)
  - `enforce-donelog.yml` (global)
- [x] Betriebsmodi „Standardlauf“/„Sicherheitsprotokoll“ beschreiben und in Anleitungen verankern (2025-11-03)
- [ ] Trigger/Paths prüfen: nur relevante Pfade bauen/testen (Performance)
- [ ] README Hinweis: Workflows liegen ausschließlich im Root

Notiz (2025-11-02 11:52): Modul-Workflows entfernt; Root-Workflows aktiv. Nächster Schritt: Trigger/Paths justieren und README-Hinweis ergänzen.
Notiz (2025-11-02 12:08): Root `pyproject.toml` konsolidiert (tools-only: black/ruff); README „Editable“ auf `packages/novapolis_common` umgestellt.
Notiz (2025-11-02 12:41): Prüf-/Release-Checks aktualisiert (Root-cwd, STOP‑Gate bei Unsicherheiten); Behaviour/Policy‑Änderungen erfordern Test `test_content_policy_profiles.py` + Changelogs.

### Prüf-/Release-Checks (konkret)

- [ ] Vor Commits: `novapolis_agent/scripts/run_tests.py` (cwd=`novapolis_agent`), Validatoren unter `novapolis-rp/coding/tools/validators/`.
- [ ] Behaviour-/Policy‑Änderungen: `novapolis_agent/tests/test_content_policy_profiles.py` laufen lassen; Changelogs prüfen.

### Akzeptanzkriterien (gesamt)

- [ ] Ein Interpreter (Root `.venv`), keine Modul-Interpreter
- [ ] Alle Dev-Tasks startbar aus Root; CWD pro Task korrekt gesetzt
- [ ] `pytest -q` läuft nur für Agent-Tests
- [ ] Lint/Format global konsistent (eine Config je Tool)
- [ ] Dokumentation aktualisiert (README/Index, dieser Plan abgehakt)

### VS Code Workspace (Multi-root → Single-root)

Aktueller Stand (geprüft): `novapolis-suite.code-workspace` ist als Multi-root konfiguriert (folders: `Main`, `novapolis_agent`, `novapolis-dev`, `novapolis-rp`, `novapolis-sim`, `packages`). Das hält den Multi-root-Modus am Leben und konterkariert die Single-Root-Umstellung.

- [x] Entscheidung: `.code-workspace` entfernen ODER auf Single-root reduzieren (nur `{ "path": "." }`).
- [x] Falls behalten: `folders` auf nur Root setzen; modulare Einträge entfernen.
- [x] Godot-Setting (`godotTools.editorPath.godot3`) in Root-`.vscode/settings.json` überführen.
- [x] README-Hinweis: Workspace künftig über den Root-Ordner öffnen (nicht Multi-root `.code-workspace`).

Notiz (2025-11-02 10:27): `.code-workspace` wurde auf Single-root reduziert (nur `{"path": "."}`); `godotTools.editorPath.godot3` ins Root `/.vscode/settings.json` migriert.

### Konflikt-Konfigurationen (Scan/Status)

- Markdownlint (lokale Overrides gefunden):
  - `novapolis-rp/database-curated/staging/.markdownlint.json`
  - `novapolis-rp/database-curated/staging/reports/.markdownlint.json`
  - Maßnahme: Root-CLI2-Ignores ergänzt, damit diese Bereiche nicht lint-blocken. Weitere Konsolidierung optional (Dateien später entfernen).
- EditorConfig (potentielle Override-Gefahr):
  - `novapolis-sim/novapolis-sim/.editorconfig` hatte `root = true` → entfernt. Defer jetzt zur Root-.editorconfig.
- Pyproject (Fragmentierung):
  - `novapolis_agent/pyproject.toml` (Modul-spezifisch)
  - `novapolis-dev/integrations/mcp-openai-eval/pyproject.toml` (Mini-Projekt)
  - Root `pyproject.toml` enthält doppelte/inkonsistente Sektionen → Konsolidierung nötig.

- [x] Markdownlint-Ignores in `.markdownlint-cli2.jsonc` ergänzt (staging/*, reports/*)
- [x] `novapolis-sim/.editorconfig` „root = true“ entfernt
- [x] Root `pyproject.toml` bereinigen (doppelte [project]/[build-system] entfernen, einheitliche Tools/Config)
- [ ] Modul-`pyproject.toml` konsolidieren oder isolieren (Tests/Lint steuern via CWD/paths)

Notiz (2025-11-02 11:35): Root `pyproject.toml` jetzt tools-only (black/ruff/pytest). Packaging verbleibt in Modulen/Paketen.


