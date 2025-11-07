---
stand: 2025-11-07 12:56
update: Devcontainer-Verzeichnis physisch gelöscht; DONELOG/TODO aktualisiert.
checks: markdownlint (file) PASS; pytest -q PASS; search (tasks/settings/devcontainer) PASS; Remove-Item PASS
---

<!-- markdownlint-disable MD022 MD041 -->

Single Root TODO (Novapolis Suite)
=================================

Dieses Dokument bietet eine zentrale, lesefreundliche Übersicht über alle laufenden Arbeiten im Monorepo. Die fachlichen Single Sources of Truth (SSOT) bleiben in den Modul-TODOs unter `novapolis-dev/docs/` erhalten.

Hinweise
--------

- SSOT: Modul-TODOs bleiben maßgeblich. Diese Datei dient als komfortabler Root-Einstieg.
- Archivierung: Fertige Blöcke (alle [x]) bitte in die jeweiligen Modul-Archive unter `novapolis-dev/archive/` verschieben.
- Snapshot-Kopf: YAML-Frontmatter oben bei Änderungen aktualisieren (`stand`, `update`, `checks`).
- Lint: Markdownlint läuft repo-weit ausschließlich manuell via `npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc '**/*.md'` (keine VS Code Tasks oder Wrapper). Bei FAIL bitte minimalen Patch anwenden.
- Terminal/Pwsh: Standard ist jetzt PowerShell 7 (`pwsh`). Bei allen manuellen Aufrufen `-NoProfile` verwenden, um Störungen durch Profilskripte zu vermeiden. Die VS Code Tasks (ohne Markdownlint) sind entsprechend konfiguriert (z. B. `pwsh -NoProfile -Command '…'`). Für komplexe/mehrachsige Abläufe sind Skript‑Wrapper via `pwsh -NoProfile -File <script.ps1>` Pflicht; Details siehe `.github/copilot-instructions.md`.
- STOP-Hinweis: „Grün“ gilt nur bis zur nächsten Abweichung/Unsicherheit – dann STOP, Rückfrage, weiter nach Freigabe. Details: `.github/copilot-instructions.md` → Abschnitt „Unklarheiten‑STOP (global, immer gültig)“.

Kurzüberblick (Module & Quellen)
--------------------------------

- Index: `novapolis-dev/docs/todo.index.md`
- Agent: `novapolis-dev/docs/todo.agent.md`
- Dev: `novapolis-dev/docs/todo.dev.md`
- RP: `novapolis-dev/docs/todo.rp.md`
- Sim: `novapolis-dev/docs/todo.sim.md`
- Root-Übersicht (ausführlich): `todo.root.md`

Offene Aufgaben (Root – quer durchs Repo)
----------------------------------------

- [x] Wrapper-Policy präzisiert & gespiegelt (Root/TODO)
  - 2025-11-07: `.github/copilot-instructions.md` vereinheitlicht (Wrapper via `pwsh -NoProfile -File` zwingend); Hinweis in diesem Dokument ergänzt.
  - Lint (focused) PASS.
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
  - 2025-11-07 05:28: Quick‑Fix A umgesetzt (YAML‑Delimiter ergänzt) für `README.md` und `novapolis-dev/docs/index.md`; Validator‑Skip‑Pfade (B) erweitert um `.pytest_cache/` und `.github/ISSUE_TEMPLATE/`. Repo‑weiter Lauf zeigt v. a. `novapolis-rp/database-rp/**` ohne Frontmatter. Option C: breit ergänzen ODER vorübergehend ausschließen (Entscheidung ausstehend).
  - 2025-11-07 05:59: Pre‑commit‑Hook um Frontmatter‑Check erweitert (nur geänderte `.md`‑Dateien). CI: In `markdownlint.yml` zusätzlicher Job „frontmatter (validator)“ für sichere Pfade (`novapolis-dev/docs`, `novapolis_agent/docs`, Root‑Docs). Option C bleibt offen.
- [x] Tree-Snapshots aktualisieren bei Strukturänderungen
  - Tasks: "Workspace tree: full", "Workspace tree: directories", "Workspace tree: summary (dirs)".
- [ ] Backups & Releases (Manifest/Checksums/Rotation) pflegen
- [ ] Markdown-Ausgaben der Skripte (Chat-Exporter, todo_gather, summarize_eval_results, Reports) auf Setext-/Frontmatter-Konformität prüfen und anpassen.
  - [x] Audit dokumentiert: `Backups/AUDIT.md`
  - [x] Skripte ergänzt: `scripts/update_backups_manifest.ps1`, `scripts/rotate_backups.ps1`
  - [x] README + initiales Manifest: `Backups/README.md`, `Backups/manifest.v1.json`
  - [x] Bundles umbenennen (Schema) & Rotation-Läufe dokumentieren (`rotation.log`)
    - 2025-11-03 00:28: `cvn-agent-main.bundle` → `cvn-agent-main-20251103-0028-rev1.bundle` (sha256 protokolliert)
    - 2025-11-03 00:28: `novapolis_agent.bundle` → `novapolis-agent-backup-20251103-0028-rev1.bundle` (sha256 protokolliert)


Modul-Fokus (Auszüge – bitte in den SSOTs pflegen)
-------------------------------------------------

### Agent (Backend)

- Quelle: `novapolis-dev/docs/todo.agent.md`
- [ ] TTS/Coqui – Exporter & Mini-Service (Planung)
  - Implementiere `novapolis_agent/scripts/tts_export_coqui.py` gemäß `novapolis-dev/docs/specs/tts-exporter-coqui.md` (CLI-Nutzung, ohne VS Code Task).
  - Akzeptanz: Referenzinput → OGG-Ausgabe; kurze Run-Notiz im DONELOG.
- [ ] CLI-Fluss/Script für TTS-Export definieren (Planung)
- [ ] Templates `knowledge:/actions:` (nur Doku-Verlinkung)

### Dev (Tooling/Infra)

- Quelle: `novapolis-dev/docs/todo.dev.md`
- [ ] MCP-Server-Prototyp (lokal, Minimal)
- [ ] Annotation-/Scheduler-/TTS-Specs vervollständigen
- [ ] Templates für `knowledge:` und `actions:` bereitstellen
- [ ] Frontmatter-Validator in CI integrieren
  - Akzeptanz: CI-Job failt bei fehlender/inkorrekter YAML-Frontmatter außerhalb der Skip-Pfade (Ausnahme `.github/copilot-instructions.md`).
  - Stand 2025-11-07 05:28: A erledigt (Delimiter‑Quick‑Fix in Kern‑Docs), B erledigt (Skip‑Pfade verfeinert). Option C (RP‑Scope: ergänzen vs. temporär ausschließen) offen.
  - Stand 2025-11-07 05:59: Pre‑commit‑Gate aktiv (staged `.md`), CI‑Frontmatter‑Check in `markdownlint.yml` (scoped). Keine Breaking‑Änderung für RP‑Daten.

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

Pflege & Regeln
---------------

- DONELOG-Pflege: Substanzielle Arbeiten bitte in den passenden DONELOG eintragen (`novapolis-dev/docs/donelog.md` bzw. `novapolis_agent/docs/DONELOG.txt`).
- Minimal-Delta: Kleine, zielgerichtete Patches; Redirect-/Mirror-Stubs erst nach Link-Prüfung entfernen.

Monorepo Single Root – Umstellungsplan (Schritt für Schritt)
-----------------------------------------------------------

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

- [x] Root-Umgebung anlegen/vereinheitlichen: `.venv/` im Root; Dependencies aus `requirements*.txt` installieren
- [x] VS Code: Interpreter im Root setzen (Workspace-Level); alle Ordner-Overrides entfernen
  - Akzeptanz: Python-Interpreter zeigt überall auf `${workspaceFolder}/.venv` (bzw. Python aus dieser venv)
- [x] Entfernen/Neutralisieren von Modul-Interpreter-Hinweisen
  - Dateien prüfen: `novapolis_agent/.vscode/settings.json`, `novapolis-rp/.vscode/settings.json`, `novapolis-sim/.vscode/settings.json`
  - Akzeptanz: Keine interpreterPath-/defaultInterpreterPath-Overrides außerhalb des Root mehr vorhanden

Status (2025-11-07 12:05):
- Skript `scripts/setup_root_venv.ps1` hinzugefügt (idempotent, erstellt/aktualisiert .venv, installiert requirements/base+dev+train).
- Ausführung erfolgreich (Python 3.13.2, pip 25.3). Anforderungen bereits erfüllt (Pakete vorhanden).
- VS Code Settings verweisen auf `${workspaceFolder}/.venv/Scripts/python.exe` (Bestätigung).
- Modul-Settings mit Interpreter-Override außerhalb Root nicht vorhanden.
- Akzeptanzkriterien erfüllt → Etappe 1 abgehakt.

Optionaler manueller Run (Referenz, kein weiterer Bedarf):

```powershell
pwsh -NoProfile -File scripts/setup_root_venv.ps1
```


### Etappe 2 – Tasks zentral, CWD gezielt

- [x] Root `.vscode/tasks.json`: Alle Standard-Tasks zentral (Lint, Types, Full, Coverage, Pytest (-q), Marker-Tests (unit/api+streaming), DONELOG append). Fix-/Format-Tasks bewusst nicht dauerhaft.
  Abschluss (2025-11-07 11:09): Konsolidierung erfolgt; Policy: ruff/black Fix nur ad-hoc manuell.
  Optional (deferred): Marker-Tasks für eval/scripts bei Bedarf nachziehen.

### Etappe 3 – Test-Discovery (Präzisierung)

- [x] Testlauf standardisieren: Root-Task „Tests: pytest (-q)“ mit `cwd=novapolis_agent` (vorhanden)
- [x] Root-Absicherung: `pytest.ini` im Root mit `testpaths = novapolis_agent/tests` ergänzt (migrationsfreundlich für spätere Root-Runs)
- [x] Godot-/Datenordner von Testdiscovery ausschließen (über `norecursedirs`/Ignores in Root-Config abgedeckt)

  Status (2025-11-07 11:16):
  - Aktive Strategie: Kombination aus Variante A (Tasks mit `cwd=novapolis_agent`) und Root-Absicherung via `testpaths` (Variante B) → beides funktionsfähig.
  - Marker wurden im Root gespiegelt, damit Root-Runs ohne UnknownMark-Warnungen funktionieren.
  - Drift-Risiko minimiert: Root-Config ist minimal gehalten; Modul-Config bleibt vorerst bestehen.
- [x] Modul-Tasks deaktivieren/entfernen (nach Verifikation)
  - Status 2025-11-07 12:30: Suche `**/.vscode/tasks.json` zeigt nur Root-Datei; keine modulare Tasks vorhanden → akzeptiert.
  - Akzeptanz: Start aller Prüf-/Test-Tasks aus Root; Modul-Tasks nicht mehr erforderlich (erfüllt)
- [x] ENV bleibt Root: Keine Modul-spezifischen `envFile`/Interpreter-Zuweisungen
  - Status 2025-11-07 12:30: Keine `/.vscode/settings.json` in Modulen gefunden; Root `settings.json` setzt `python.defaultInterpreterPath` und ein zentrales `python.envFile` (Agent-`.env`) → keine Modul-Overrides.

### Etappe 3b – Test-Discovery steuern (nur dort, wo Tests sind)

- [x] Testlauf standardisieren: Root-Task „Tests: pytest (-q)“ mit `cwd=novapolis_agent`
- [x] Exklusion anderer Ordner absichern
  - Variante A (bevorzugt): `cwd` strikt auf `novapolis_agent` (Wrapper: `scripts/run_pytest_quick.ps1`)
  - Variante B: Root-`pytest.ini` mit `testpaths = novapolis_agent/tests` (falls Root-Run ohne cwd genutzt wird)
- [x] Godot-/Datenordner von Testdiscovery ausschließen (falls Root-Discovery aktiv)
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
  - `novapolis_agent/.github/workflows/consistency-report.yml`
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
Notiz (2025-11-07 05:15): Modul-Workflows entfernt (siehe Liste oben); Root-Workflows bleiben die einzige Quelle unter `/.github/workflows/`.

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

Aktueller Stand (geprüft): `novapolis-suite.code-workspace` ist als Single-root konfiguriert (folders: nur `{ "path": "." }`). Der Multi-root-Modus ist entfernt und unterstützt die Single-Root-Umstellung.

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
  
  Notiz (2025-11-07 05:28): Lokale `.markdownlint.json`‑Overrides weiterhin vorhanden (staging/, reports/). Sie werden durch Root‑Ignores neutralisiert; optional später entfernen.
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

Notiz (2025-11-07 12:37): Devcontainer für Agent entfernt/deaktiviert (novapolis_agent/.devcontainer/* auf Stub gesetzt). Single‑Root nutzt lokale `.venv`; keine Container-Abhängigkeit.
Notiz (2025-11-07 12:56): Devcontainer-Ordner physisch gelöscht; keine aktive VS Code Devcontainer-Konfiguration mehr im Repo.

Notiz (2025-11-02 11:35): Root `pyproject.toml` jetzt tools-only (black/ruff/pytest). Packaging verbleibt in Modulen/Paketen.

