# LLM-Dokumentenheader (nicht löschen)
 Type: Copilot Instruction Set / Project Governance  
 Scope: Novapolis-Suite (VS Code Workspace Main)  
 Language: Deutsch  
 Encoding: UTF-8 / Unix-EOL  
 Purpose: Legt alle verbindlichen Regeln, STOP-Gates, Policies und Ablaufprotokolle für Copilot-gestützte Aktionen im Projekt fest.  
 Structure: Markdown (H1/H2 = Setext, H3+ = ATX) – hierarchisch eingerückt; jede Regel mit semantischem Kontext.  
 Priority: Dieses Dokument ist SSOT (Single Source of Truth) für Copilot-Verhalten – es überschreibt lokale oder temporäre Session-Prompts.  
 Precedence: Immer zuerst laden → alle Aktionen, Tests und Änderungen müssen den hier definierten Regeln folgen.  
 Compliance: Wrapper-Policy, STOP-Gate, Frontmatter-Policy, Lint-Policy, Security-Checks, Logging-Receipt, Meta-/Systeminfo-Protokollierung.  
 Audit: Jede Antwort oder Änderung endet mit einem Postflight-Block nach Abschnitt „Meta-/Systeminfo-Protokollierung“.  
 Timestamp: 2025-11-08 20:22
============================
<!-- markdownlint-disable MD022 MD032 MD036 -->

Kurzreferenz aller Überschriften dieser Anleitung
-------------------------------------------------
 -  `.github/copilot-instructions-headings.md` (Extrakt der H1/H2/H3-Überschriften).

 - Hinweis (Terminal/Pwsh): Standard ist jetzt PowerShell 7 (`pwsh`). Bei allen manuellen Aufrufen `-NoProfile` verwenden, um Störungen durch Profilskripte zu vermeiden. Für einfache, kurze Einzeiler weiterhin `-Command` Inline nutzen; für komplexe oder mehrzeilige Abläufe (Coverage, Artefakt-Erzeugung, umfangreiche Prüf-Sequenzen) zwingend Skript-Wrapper nutzen: `pwsh -NoProfile -File <script.ps1>`. Wrapper sind nur in dieser Form erlaubt (kein indirektes Aufrufen per `-Command` mit Here-Strings). Achte auf sauberes Quoting (`${workspaceFolder}`, `Join-Path`) bei allen Inline-Kommandos.
 - Ausnahme (Systemzeit): Für einfache, pfadfreie Einzeiler ist `-Command` erlaubt und kanonisch. Systemzeit immer so ermitteln: `pwsh -NoProfile -Command "Get-Date -Format 'yyyy-MM-dd HH:mm'"`.

Dateipfad & Geltungsbereich
---------------------------
 - **Kanonischer Speicherort:** `.github/copilot-instructions.md` im Repo-Root. Nur hier abgelegte Inhalte gelten als verbindlich; Kopien/Backups dienen ausschließlich der Historie.
 - **Geltungsbereich:** Regeln gelten für Copilot Chat in VS Code, Inline-Completions, Apply-Patch-Befehle und agentische Funktionen (z. B. Tasks, Run-Code-Snippets). Bei Tools mit begrenztem Kontext immer die Kernregeln priorisieren und Details bei Bedarf im Chat referenzieren.
 - **Pfad-Disziplin:** Tippfehler oder abweichende Verzeichnisse (z. B. `.github/copilot-instuctions.md`) werden ignoriert. Vor Änderungen prüfen, dass die editierte Datei exakt den kanonischen Pfad besitzt.

Primäre Behaviour-Quellen
-------------------------
 ### SSOT: Dieses Dokument ist die zentrale Verhaltens‑/Arbeitsrichtlinie. Modul‑/Domänenreferenzen:
   - Konsolidiert: Frühere Modulkopien (Agent/Dev‑Hub) wurden in dieses Dokument überführt und entfernt.
   - `novapolis-rp/database-rp/00-admin/AI-Behavior-Mapping.{md,json}`: Rollenspiel-spezifische Verhaltenshooks und Rollenmatrix (SSOT in RP).
   - `novapolis-rp/development/docs/` enthielt Legacy-Stubs und wurde entfernt (2025-11-05). Verwende ausschließlich die oben genannte RP‑Quelle und dieses Dokument.
   - Priorität: 11 Dieses Dokument (global), 2. `novapolis-rp/database-rp/00-admin/AI-Behavior-Mapping.*` (RP-spezifisch), 3. `novapolis_agent/docs/DONELOG.txt` + Agent-Essentials (Backend-spezifisch). Bei Konflikten gilt die niedrigere Zahl.

Gemeinsamer Arbeitsstil
-----------------------
 - Standard-Antwortsprache ist Deutsch (Erklärungen, Beispiele, Fehlermeldungen).
 - Arbeite iterativ, halte Tests und Typprüfungen grün, dokumentiere substanzielle Änderungen:
   - Root: `DONELOG.md`, `todo.root.md`.
   - Agent: `novapolis_agent/docs/DONELOG.txt` (und projektinterne TODOs, falls vorhanden).
   - Dev‑Hub: `novapolis-dev/docs/donelog.md`, `novapolis-dev/docs/todo.*.md`.
   - Weitere Projekt‑TODOs nur, wenn tatsächlich vorhanden; ansonsten Root/Dev‑Hub nutzen.
 - Prägnanter Output: skimmbar, keine überladenen Blockzitate; bei großen Aufgaben Plan in betreffende todo eintragen.
 - Sicherheit & Privacy: Keine Secrets, offline bevorzugen, keine harten Pfade zu externen Repositories übernehmen.
 - Root-Statusdateien `WORKSPACE_STATUS.md`, `workspace_tree_full.txt` und `workspace_tree_dirs.txt` als globalen Kontext heranziehen und nach größeren Umstrukturierungen oder mindestens monatlich aktualisieren.

Onboarding & Setup
------------------
 - Schnell‑Index (häufig genutzte Themen)

 | Thema        | Vorkommen |
 | ---          | ---:      |
 | DONELOG      | 27        |
 | pyright      | 22        |
 | pytest       | 20        |
 | STOP         | 20        |
 | markdownlint | 19        |
 | pwsh         | 17        |
 | mypy         | 16        |
 | Frontmatter  | 14        |
 | TODO         | 14        |
 | Tasks        | 14        |
 | .venv        | 11        |
 | Coverage     | 10        |

 - Hinweis: Aus dieser Datei automatisch ermittelt (Stoppwörter/Plural nicht normalisiert). Dient als Navigationshilfe, nicht als strikte Metrik.

Cheat Sheet (pwsh‑Kommandos)
-----------------------------
 - ACHTUNG: Rein dokumentarische Referenz für Menschen. Copilot/GPT verwendet für komplexe oder mehrschrittige Prüfungen ausschließlich Skript-Wrapper über `pwsh -NoProfile -File <script.ps1>`. Inline `-Command` ist nur für echte, kurze Einzeiler erlaubt.
 - Kurzformen für die drei wichtigsten lokalen Prüfungen (identisch mit den ausführlichen Befehlen weiter unten für manuelle Runs; Wrapper-Alternative siehe Hinweis unter Tests):
 - ACHTUNG: Copilot erstellt keine neuen VS Code Tasks. Bereits vorhandene Tasks dürfen genutzt werden, wenn sie einen `pwsh -NoProfile -File <script.ps1>`-Wrapper einsetzen und damit vollständige Ausgaben liefern.

 ### Lint (Ruff + Black, keine Auto‑Fixes)
   ```powershell
   pwsh -NoProfile -Command "& { $ErrorActionPreference = 'Stop'; $root = '${workspaceFolder}'; Set-Location $root; $python = Join-Path $root '.venv\\Scripts\\python.exe'; if (-not (Test-Path -LiteralPath $python)) { $python = 'python'; }; & $python -m ruff check .; $ruffExit = $LASTEXITCODE; & $python -m black --check .; if ($ruffExit -ne 0 -or $LASTEXITCODE -ne 0) { exit 1 } }"
   ```

 ### Typen (Pyright + Mypy)
   ```powershell
   pwsh -NoProfile -Command "& { $ErrorActionPreference = 'Stop'; $root = '${workspaceFolder}'; $agent = Join-Path $root 'novapolis_agent'; Set-Location $agent; $pyright = Join-Path $root '.venv\\Scripts\\pyright.exe'; if (-not (Test-Path -LiteralPath $pyright)) { $pyright = 'pyright'; }; & $pyright -p pyrightconfig.json; if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }; $python = Join-Path $root '.venv\\Scripts\\python.exe'; if (-not (Test-Path -LiteralPath $python)) { $python = 'python'; }; & $python -m mypy --config-file mypy.ini app scripts; exit $LASTEXITCODE }"
   ```

 ### Tests (Pytest mit Coverage ≥ 80 %)
   ```powershell
   pwsh -NoProfile -Command "& { $ErrorActionPreference = 'Stop'; $root = '${workspaceFolder}'; $python = Join-Path $root '.venv\\Scripts\\python.exe'; if (-not (Test-Path -LiteralPath $python)) { $python = 'python'; }; $cover = Join-Path $root 'novapolis_agent'; $cover = Join-Path $cover '.coveragerc'; $cwd = Join-Path $root 'novapolis_agent'; Set-Location $cwd; $maxTestFiles = 40; $collectOutput = & $python -m pytest --collect-only 2>&1; $collectedFiles = $collectOutput | Where-Object { `$_ -match '::' } | ForEach-Object { (`$_ -split '::')[0] }; $uniqueFiles = $collectedFiles | Sort-Object -Unique; $fileCount = $uniqueFiles.Count; if ($fileCount -gt $maxTestFiles) { Write-Host \"STOP: Zu viele Testdateien gesammelt ($fileCount > $maxTestFiles). Bitte Scope prüfen.\"; exit 2 }; & $python -m pytest --cov --cov-report=term-missing --cov-branch --cov-config $cover --cov-fail-under=80; exit $LASTEXITCODE }"
   if ($LASTEXITCODE -eq 0) { Write-Host 'Pytest PASS' } else { Write-Host "Pytest FAIL ($LASTEXITCODE)" }
   ```

 ## Empfohlen (Wrapper, Copilot/GPT):
   ```powershell
   pwsh -NoProfile -File scripts\run_pytest_coverage.ps1
   ```

   - `$maxTestFiles` (Standard 40) stellt sicher, dass nicht versehentlich zu viele Testdateien im Lauf landen. Bei Überschreitung stoppt der Befehl mit einer roten STOP-Notiz.
   - Details und Begründung siehe Abschnitt „Kanonische Prüfabläufe (pwsh)“ weiter unten.
   - Einmalig `pwsh -NoProfile -Command "& .\.venv\Scripts\python.exe -m pip install --upgrade pip"` ausführen, falls Pip veraltet ist.
   - Erste Validierung: Sequenz aus Lint (`ruff`, `black --check`), Typen (`pyright`, `mypy`) und Tests mit Coverage (Pytest ≥ 80 %) jeweils manuell via `pwsh -NoProfile -Command "& { ... }"` ausführen; Beispielbefehle siehe Abschnitt „Kanonische Prüfabläufe (pwsh)“.
   - Vor dokumentationsbezogenen Sessions mit Copilot bzw. GPT‑5 zwingend `npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc '**/*.md'` ausführen (Achtung: Glob stets in einfachen Anführungszeichen, keine abschließenden Escape-Zeichen), um falsche Positivmeldungen in nachfolgenden Tests zu vermeiden. Den Befehl unverändert direkt im Terminal eingeben – keine `pwsh -NoProfile -Command`-Hülle verwenden.

Kanonische Prüfabläufe (pwsh)
-----------------------------
 - Grundlage: Die gleichnamigen VS Code Tasks dienen nur als Referenz. Copilot/GPT startet komplexe/mehrschrittige Abläufe nicht als Inline `-Command`, sondern ausschließlich über Skript-Wrapper via `pwsh -NoProfile -File <script.ps1>`. Copilot erstellt keine neuen Tasks; vorhandene Tasks dürfen laufen, sofern sie diesen Wrapper beibehalten. Die nachfolgenden Inline-Beispiele sind dokumentarisch und für manuelle Human-Runs gedacht; Inline `-Command` bleibt nur für echte Einzeiler zulässig.

 ## Lint (Ruff + Black, keine Auto-Fixes)
 ```powershell
 pwsh -NoProfile -Command "& { $ErrorActionPreference = 'Stop'; $root = '${workspaceFolder}'; Set-Location $root; $python = Join-Path $root '.venv\\Scripts\\python.exe'; if (-not (Test-Path -LiteralPath $python)) { $python = 'python'; }; & $python -m ruff check .; $ruffExit = $LASTEXITCODE; & $python -m black --check .; if ($ruffExit -ne 0 -or $LASTEXITCODE -ne 0) { exit 1 } }"
 ```

 ## Typen (Pyright + Mypy)
 ```powershell
 pwsh -NoProfile -Command "& { $ErrorActionPreference = 'Stop'; $root = '${workspaceFolder}'; $agent = Join-Path $root 'novapolis_agent'; Set-Location $agent; $pyright = Join-Path $root '.venv\\Scripts\\pyright.exe'; if (-not (Test-Path -LiteralPath $pyright)) { $pyright = 'pyright'; }; & $pyright -p pyrightconfig.json; if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }; $python = Join-Path $root '.venv\\Scripts\\python.exe'; if (-not (Test-Path -LiteralPath $python)) { $python = 'python'; }; & $python -m mypy --config-file mypy.ini app scripts; exit $LASTEXITCODE }"
 ```

 ## Tests (Pytest Coverage ≥ 80 %)
  ```powershell
  pwsh -NoProfile -Command "& { $ErrorActionPreference = 'Stop'; $root = '${workspaceFolder}'; $python = Join-Path $root '.venv\\Scripts\\python.exe'; if (-not (Test-Path -LiteralPath $python)) { $python = 'python'; }; $cover = Join-Path $root 'novapolis_agent'; $cover = Join-Path $cover '.coveragerc'; $cwd = Join-Path $root 'novapolis_agent'; Set-Location $cwd; $maxTestFiles = 40; $collectOutput = & $python -m pytest --collect-only 2>&1; $collectedFiles = $collectOutput | Where-Object { `$_ -match '::' } | ForEach-Object { (`$_ -split '::')[0] }; $uniqueFiles = $collectedFiles | Sort-Object -Unique; $fileCount = $uniqueFiles.Count; if ($fileCount -gt $maxTestFiles) { Write-Host "STOP: Zu viele Testdateien gesammelt ($fileCount > $maxTestFiles). Bitte Scope prüfen."; exit 2 }; & $python -m pytest --cov --cov-report=term-missing --cov-branch --cov-config $cover --cov-fail-under=80; exit $LASTEXITCODE }"
  if ($LASTEXITCODE -eq 0) { Write-Host 'Pytest PASS' } else { Write-Host "Pytest FAIL ($LASTEXITCODE)" }
  > `$maxTestFiles` kann bei Bedarf angepasst werden; die STOP-Meldung verhindert, dass ungewollt große Testmengen laufen.
  ```

 ## Aggregierte Prüfung (`Checks: full`): 
   - obige Befehle in der Reihenfolge Lint → Typen → Tests ausführen und Ergebnisse dokumentieren.

 ## Zusatz (pwsh):
   - Für Python-Befehle den Interpreter aus `.venv` verwenden (Fallback `python`), wie in den Beispielen gezeigt.
   - Bei Pfaden mit Leerzeichen `${workspaceFolder}` und `Join-Path` einsetzen.
   - Wrapper-Richtlinie: Wenn ein Befehl mehr als ~120 Zeichen umfasst, Artefakte schreibt (z. B. JUnit/Coverage/XML) oder mehrere logische Schritte enthält (Collect-Guard, Ausführung, Summary), als eigenes Skript unter `scripts/` ablegen und ausschließlich über `pwsh -NoProfile -File` starten. Keine mehrstufigen Inline-Blöcke mit verschachtelten `& { ... }` für solche Fälle.

 ## Update-Logistik
   - Timestamp: Änderungen im Format `YYYY-MM-DD HH:mm` erfassen (aktuell) – gilt für Kopfzeilen („Stand“, „Letzte Aktualisierung“), DONELOG-Einträge und kurze Statusnotizen. Standard ist die lokale Systemzeit. Wer mit abweichender Zeitzone arbeitet, ergänzt im `update`-Feld den Offset (z. B. `UTC+02`) oder weist ihn im Text aus. Eine Umstellung auf `Z`/UTC erfolgt erst nach Anpassung des Validators.
   - Systemzeit (lokal, kanonisch): `pwsh -NoProfile -Command "Get-Date -Format 'yyyy-MM-dd HH:mm'"`.
   - Kurznotiz: 1–2 Sätze oder Bullet, was angepasst wurde (analog zu `novapolis-rp/database-rp/02-*`). Bei komplexeren Tasks optional Primärpfad referenzieren (`app/...`, `scripts/...`).
   - Prüfungen: Relevante Checks nennen (z. B. `pytest -q`, `pyright`, `markdownlint-cli2`) inkl. Ergebnis/Exit-Status; bei Bedarf Link/Dateipfad zur Ausgabe ergänzen.
   - Markdownlint-Läufe protokollieren: Lauf/Command + PASS/FAIL direkt nach dem Lauf im Status erwähnen.

 ## Workspace‑Tree‑Artefakte (Zuordnung)
   - „Workspace tree: full“ → `workspace_tree_full.txt`
   - „Workspace tree: directories“ → `workspace_tree.txt`
   - „Workspace tree: summary (dirs)“ → `workspace_tree_dirs.txt`
   - Dokumentpflege: Betroffene Artefakte synchron halten (Root: `todo.root.md`, `DONELOG.md`; Agent: `novapolis_agent/docs/DONELOG.txt`; Dev‑Hub: `novapolis-dev/docs/todo.*.md`, `novapolis-dev/docs/donelog.md`; außerdem `WORKSPACE_INDEX.md`, `WORKSPACE_STATUS.md`, README/Index-Seiten). Strukturänderungen → zusätzlich Tree-Snapshots aktualisieren; Behaviour-Änderungen → dieses Dokument aktualisieren und Verweise prüfen.
   - Referenzen: Wenn vorhanden Issue-/PR-Links, Commit-Hash oder Kontextnotizen angeben (Inline oder als Fußnote). Für wiederkehrende Schritte Templates/Tasks im Root `.vscode/` ergänzen.
   - Nicht-triviale Änderungen → in zugehörige TODO oder DONELOG.

 ## YAML-Frontmatter (kompakt & LLM-freundlich)
   - Jede Datei mit Snapshot-Kopfzeile und eine YAML-Frontmatter am Dokumentanfang einpflegen.
   - Empfohlene Schlüssel (kurz und stabil):
     - `stand`: `YYYY-MM-DD HH:mm` (lokale Zeit (immer aktuell))
     - `update`: 1–2 Stichpunkte zur Änderung
     - `checks`: kurz zu den relevanten Prüfungen/Ergebnissen (z. B. „pytest -q PASS“)
   - Optional: `refs` (Issue/PR/Commit), `affected` (betroffene Dateien/Pfade)

   Beispiel:
     ---
     stand: 2025-11-01 09:05
     update: Task „DONELOG: append entry“ ergänzt.
     checks: keine
     ---

 - Hinweise:
   - Bei jedem Schreibvorgang Frontmatter-Zeitstempel und `update`/`checks` aktualisieren.
   - Ausnahme: Für dieses Dokument (`.github/copilot-instructions.md`) keine YAML-Frontmatter verwenden (Parser-Einschränkung). Snapshot hier weiterhin per `Stand:`-Zeile pflegen.
   - Fallback (allgemein): Wenn YAML-Frontmatter technisch nicht einsetzbar ist (Parser/Format-Einschränkung), nutze am Dokumentanfang eine kompakte Kopfzeile im Klartext:
     - Erste Zeile: `Stand: YYYY-MM-DD HH:mm – <Kurznotiz>` (aktuelle Systemzeit)
     - Optional darunter: `Checks: <kurz>`
   - Beispiel:
     - `Stand: 2025-11-01 09:28 – Abschnitt X präzisiert.`
     - `Checks: pytest -q PASS`
 - Migrationsstatus & Historie: Siehe Archiv `novapolis-dev/archive/copilot-instructions-update-tode.archive.md`.

 ## Frontmatter‑Schutz (robust gegen Delimiter‑Verlust)
   - Ziel: Verhindern, dass die erste/letzte Frontmatter‑Zeile (`---`) versehentlich entfernt oder verändert wird.
   - Editor‑Policy (Markdown):
     - Format On Save für Markdown deaktivieren; Auto‑Fixer/Prettier für Markdown nicht einsetzen.
     - Änderungen in der Frontmatter nur an Schlüsseln/Values (z. B. `stand`, `update`, `checks`) vornehmen – die Delimiter `---` oben/unten nie anfassen.
   - Validator‑Gates:
     - Pre‑commit: `scripts/check_frontmatter.py` verpflichtend ausführen; Commit bei Fehlern blocken.
     - Zusätzliche Sofort‑Checks: erste Zeile exakt `---`, schließender Delimiter vorhanden, kein BOM vor dem öffnenden Delimiter.
     - CI: Frontmatter‑Validator als Schritt im Root‑Workflow (fail‑fast außerhalb der Skip‑Pfade).
     - Skip-Pfade (siehe `scripts/check_frontmatter.py`): `.venv/`, `Backups/`, `outputs/`, `novapolis_agent/eval/results/`, `novapolis_agent/outputs/`, `novapolis-rp/database-raw/`, `.pytest_cache/` (inkl. projektspezifischer Varianten), `.github/ISSUE_TEMPLATE/` sowie diese Datei selbst.
   - Der Validator ist ein hartes Gate: Sowohl Pre-Commit als auch CI brechen bei Verstößen ab; ohne Fix gibt es keinen Push/kein Merge.

Dateiformat & EOL
-----------------
   - Markdown-Dateien stets als UTF-8 ohne BOM speichern; der Validator schlägt bei BOM im ersten Zeichen fehl.
   - Genau eine abschließende Newline am Dateiende belassen (MD047), keine zusätzlichen Leerzeilen anhängen.
   - Git kümmert sich um Zeilenendungen (LF) im Repo; lokale CRLF-Konvertierungen sind erlaubt, solange der Commit wieder LF enthält. Bei Unsicherheiten `.gitattributes` respektieren und keinen Auto-Formatter einsetzen, der Frontmatter anfasst.

Definition of Done (Code & Docs)
--------------------------------
   - **Code:** `pytest -q` PASS, `pyright -p pyrightconfig.json` PASS, `python -m mypy --config-file mypy.ini app scripts` PASS, Coverage ≥ 80 % (Task `Tests: coverage (fail-under)`), relevante DONELOG/TODO-Einträge aktualisiert, keine neuen TODO-Reste.
   - **Docs:** Frontmatter aktualisiert (`stand`/`update`/`checks`), Markdownlint PASS, Stilvorgaben (MD003) eingehalten, keine überzähligen Leerzeilen, Kontext-Referenzen (z. B. Primärpfade) ergänzt.

Security & Dependencies
-----------------------
   - Monatlich (mindestens) `pip-audit` oder vergleichbares Tool ausführen; Findings vor Merge/Release auflösen.
   - Abhängigkeiten pinnen (`requirements*.txt`, `pyproject.toml`); Versionssprünge dokumentieren (DONELOG + kurze Notiz).
   - Keine Secrets ins Repo commiten (`.env` bleibt lokal). Vor Uploads/Exports prüfen, ob sensible Daten sanitisiert sind.

Meta- / Systeminfo-Protokollierung (Preflight & Postflight, kompakt)
--------------------------------------------------------------------
 - Zweck:
   - Dieser Abschnitt definiert, wann und wie Copilot automatisch Meta- und Systeminformationen ausgibt, um jede Aktion revisionssicher zu dokumentieren.
   - Das Format ist minimalistisch, maschinenlesbar und tokenoptimiert.
   - Er ist verpflichtend für jede Änderung oder Erstellung von Dateien, Prüf- und Validierungsvorgänge sowie komplexe Abläufe mit Mehrschritt-Logik.

 ### Preflight (deaktiviert 08.11.2025 20:58 Panicgrinder)(vor jeder Änderung)
   - Vor jeder Aktion, die Dateien verändert oder generiert, muss Copilot einen Preflight-Block ausgeben, bevor irgendetwas ausgeführt wird.
   - Dieser Block dient der Vorschau und Bestätigung, dass alle Regeln, Pfade, STOP-Gates und Policies korrekt geladen sind.

   - Format (Pflichtfelder fett, optionale Angaben in Klammern):
     - Meta: Modus=Preflight, **Arbeitsverzeichnis=<Pfad>**, **RepoRoot=<Pfad>**, (PSScriptRoot=<Pfad>), (PSVersion=<x.y.z>), Aufruf=pwsh -NoProfile -File <Pfad.zum.Skript.ps1>, (SHA256=<Hash.der.Skriptdatei>), STOP-Gate=<aktiv/deaktiv>, Wrapper-Policy=<erfüllt/verletzt>, Quellen=<.github/copilot-instructions.md;README.md;...>, Aktion=<Kurzbeschreibung>

 - Verhalten:
   - Keine Änderungen, kein Schreiben, keine Commits.
   - Dient ausschließlich der Kontexterkennung und Validierung.
   - Wird bei aktivem STOP-Gate durch eine manuelle Freigabe fortgesetzt.
   - Darf nicht übersprungen werden.

 ### Postflight (scharf)(nach Abschluss eines vollständigen Arbeitsvorgangs)
   - Nach Abschluss eines vollständigen, logisch abgeschlossenen Vorgangs (z. B. Vereinheitlichung mehrerer Dokumente, Ausführung aller Tests, Erstellung eines Skripts) muss Copilot genau einen Postflight-Block ausgeben.
   - Es dürfen keine Zwischenblöcke bei Mehrfachdateien oder Schleifen erzeugt werden.
   - Ergebnisse sind gesammelt und am Ende auszugeben.

   - Falls ein Vorgang unerwartet abgebrochen wird oder ein STOP-Gate ausgelöst wurde:
     - Meta: Modus=Abort, Grund=<Kurzbeschreibung>, Zeitpunkt=<yyyy-MM-dd HH:mm>

   - Format für erfolgreiche Postflight-Ausgabe:
     - Meta: Modus=Postflight, Arbeitsverzeichnis=<Pfad>, RepoRoot=<Pfad>, PSScriptRoot=<Pfad>, PSVersion=<x.y.z>, Aufruf=pwsh -NoProfile -File <Pfad.zum.Skript.ps1>, SHA256=<Hash.der.Skriptdatei>, STOP-Gate=<aktiv/deaktiv>, Wrapper-Policy=<erfüllt/verletzt>, Quellen=<.github/copilot-instructions.md;README.md;...>, Aktion=<Kurzbeschreibung>
     - Prüfung: markdownlint=<PASS/FAIL>, ExitcodeLint=<N>, behobenLint=<ja/nein>, Frontmatter-Validator=<PASS/FAIL>, ExitcodeFM=<N>, behobenFM=<ja/nein>, Cleanup-WhatIf-Exit=<N>, behobenWhatIf=<ja/nein>, Cleanup-Real-Exit=<N>, behobenReal=<ja/nein>, WorkspaceScanRoot=<Zahl>, WorkspaceScanRecurse=<Zahl>
     - Regeln: IDs=<R-WRAP,R-STOP,R-FM,R-LINT,R-SCAN,R-CTX,R-SEC,R-LOG>, Details=R-WRAP über -File erzwungen; R-STOP aktiv vor Real; R-FM geprüft; R-LINT ausgeführt; R-SCAN Root-only; R-CTX Quellen geladen; R-SEC geprüft; R-LOG Receipt erstellt
     - Todos: offen=<Anzahl>, BeispielFix=<Kurzbeschreibung>, ReRun=<Testname>, Fällig=<Datum/Zeit>
     - Ende: Timestamp=<yyyy-MM-dd HH:mm> (jedesmal aktuelle Systemzeit über pwsh einholen.)

 ## Semantische Regeln
   - Preflight ist obligatorisch vor jedem Schreib-, Erstell- oder Löschvorgang.
   - Ohne Preflight darf keine Dateiänderung stattfinden.
   - Postflight wird genau einmal pro abgeschlossenem Vorgang erzeugt, nicht pro Datei.
   - behoben=ja nur, wenn derselbe Prüfschritt im selben Lauf erneut ausgeführt wurde und PASS ergibt.
   - Quellen müssen als absolute Pfade angegeben werden.
   - Todos wird automatisch in die todo.md übernommen, falls vorhanden.
   - Timestamp verwendet lokales Format yyyy-MM-dd HH:mm, Zeitzone Europe/Berlin.

  Kompakter Meta-Block für normale Antworten
  -----------------------------------------
   - Zweck: Für alltägliche, nicht-ausführende Antworten (keine Dateiänderung, keine Task-Starts) ist ein sehr kompakter, maschinenlesbarer Meta-Block am Ende der Nachricht erlaubt und erwünscht. Er erleichtert automatisches Parsing und dokumentiert kurz Kontext/Absicht ohne die Preflight/Postflight-Pflicht zu ersetzen.
   - Format (einzeilig, komma-separiert):
     - Meta: Modus=General, Arbeitsverzeichnis=<Pfad|optional>, RepoRoot=<Pfad|optional>, PSScriptRoot=<Pfad|optional>, PSVersion=<x.y.z|optional>, Aufruf=<Aufruf|none>, Aktion=<Kurzbeschreibung>, Timestamp=<yyyy-MM-dd HH:mm>
   - Minimalbeispiel (sehr kurz):
     - Meta: Modus=General
   - Beispiel (empfohlen, wenn etwas Kontext nützlich ist):
     - Meta: Modus=General, Arbeitsverzeichnis=F:\\VS Code Workspace\\Main, RepoRoot=F:\\VS Code Workspace\\Main, PSScriptRoot=scripts, PSVersion=pwsh 7.3, Aufruf=none, Aktion=Antwort auf Coverage-Summary, Timestamp=2025-11-08 17:00
   - Regeln:
     - Dieser kompakte Meta-Block ersetzt nicht die Preflight- oder Postflight-Blöcke, wenn Dateien verändert oder Skripte ausgeführt werden. Für jede auszuführende Aktion ist weiterhin ein Preflight (vorher) und ein Postflight (nachher) erforderlich.
     - Der kompakte Block soll eine einzelne Zeile bleiben, sparsam verwendet werden und keine sensiblen Informationen enthalten.
     - Felder sind optional; wenn nur der Modus angegeben wird, genügt `Meta: Modus=General`.

Definition der Regel-IDs (zur Verwendung im Feld „Regeln: IDs=…“)
-----------------------------------------------------------------
 - Regelkennungen (IDs) sind standardisierte Kurzbezeichner, die in der gesamten Arbeitsumgebung und in allen automatisierten Ausgaben konsistent verwendet werden müssen.
 - Sie dienen der Verkürzung, Maschinenlesbarkeit und Querverweiskontrolle zwischen Prüf-, Skript- und Log-Systemen.
 - Dieser Abschnitt gilt als verbindlicher Bestandteil der SSOT (Single Source of Truth) für alle Automatisierungen innerhalb der Novapolis-Suite.
 - Alle Agenten, Skripte und Copilot-Instanzen müssen diese Struktur respektieren, bevor eine Änderung ausgeführt oder ein Receipt erstellt wird.
 - Abweichungen sind nur mit expliziter Freigabe im STOP-Gate zulässig.

 ### aktuell vergebene Regel-IDs
   - ID R-WRAP: Wrapper-Policy – Skripte und Mehrschritt-Prozesse dürfen ausschließlich über „pwsh -NoProfile -File“ mit absolutem Pfad ausgeführt werden. Inline „-Command“ ist nur für echte Einzeiler erlaubt.
   - ID R-STOP: STOP-Gate – Jede modusrelevante oder sicherheitskritische Aktion muss vor Ausführung explizit bestätigt werden.
   - ID R-FM: Frontmatter-Policy – Dokumente müssen gültige YAML-Frontmatter-Blöcke mit definierten Schlüsseln (stand, update, checks) enthalten. Fehlende oder beschädigte Frontmatter werden durch den Validator erkannt und gemeldet.
   - ID R-LINT: Markdownlint-Policy – Dokumente müssen die Style-Regeln MD001–MD050 einhalten; insbesondere MD003 (Setext für H1/H2, ATX ab H3).
   - ID R-SCAN: Workspace-Scan – Definiert, ob der Workspace-Scan nur auf Root-Ebene oder rekursiv erfolgen darf. Standard ist Root-only by design.
   - ID R-CTX: Kontextquelle – Stellt sicher, dass alle relevanten Steuerdateien (.github/copilot-instructions.md, README.md, single-root-todo.md usw.) vor einer Aktion geladen und im Preflight bestätigt wurden.
   - ID R-SEC: Sicherheitsprinzip – Keine destruktiven Änderungen ohne vorherige WhatIf-Phase, minimalinvasive Diffs, keine automatischen Löschungen außerhalb des Skriptkontextes.
   - ID R-LOG: Receipt-Pflicht – Nach jedem abgeschlossenen Vorgang muss ein vollständiger, formalisierter Postflight-Log (Receipt) im DONELOG.md angelegt oder ergänzt werden.

STOP-Gates & Modi
-----------------
 ## STOP‑Gate (scharf)(beidseitig, vor Modus‑relevanten Aktionen)
   - Vor potenziell modus‑relevanten Aktionen – code‑schwer (z. B. Dateiedits unter Codepfaden, Skript-/Validator‑Neubau, Test-/Typecheck‑Runs, API/Service‑Änderungen) ODER redaktionell/kanon‑kritisch (z. B. Behaviour-/Policy‑Dokumente, Kanon-/SSOT‑Änderungen) – wird ein hartes STOP‑Gate gesetzt.
   - Ablauf:
     1) Ausgabe „STOP: Moduswechsel empfohlen <GPT-Modus>. Bitte Modus wählen.“
     2) Warten auf explizite Bestätigung:
       - „Wechsel: Modus Codex“ → sofort auf Codex wechseln und fortfahren.
       - „Wechsel: Modus General“ → sofort auf General wechseln und fortfahren.
       - „Weiter: aktueller Modus“ → ohne Moduswechsel fortfahren.
     3) Ohne Bestätigung keine auslösenden Aktionen starten.
   - Hinweise:
   - Das STOP‑Gate gilt beidseitig (Code ↔ Redaktion). Reine triviale Konversationen sind nicht betroffen.
   - Während STOP gilt „Debug/Analyse vor Ausführung“: Keine neuen Build/Test/Run‑Tasks automatisch starten
   - Laufende Task‑Wünsche werden in eine interne Queue gelegt und erst nach Freigabe gestartet.
   - Manuell‑ausführen‑Pflicht (kritische Läufe): 
     - Bei Coverage‑Gates oder Fehlersuche im Terminal mit gesetztem cwd=`/Main` arbeiten und Befehle mit `Join-Path` sauber quoten (mit -NoProfile -Command).

  ## Unklarheiten‑STOP (scharf)(global, immer gültig)
   - „Grün“ gilt nur bis zum nächsten unerwarteten Ereignis. Sobald etwas außerhalb des Plans liegt, sofort STOP. (unabhängig vom aktiven Modus).
   - Unerwartet = mindestens eins davon:
     - Abweichung vom Plan/Ergebnis oder Modul‑Erwartung
     - Widerspruch (Quellen/Regeln/Invarianten/SSOT)
     - Unsicherheit über Bedeutung/Wirkung/Reichweite
     - Sicherheits-/Privacy‑Bedenken
     - Falscher/unklarer Modus (General ↔ Codex)
     - Ausnahmen (kein STOP): Bereiche, die explizit als „RAW“, „noisy“ oder „staging/experimentell“ gekennzeichnet sind.
   - Vorgehen bei STOP:
     1. Kurzstatus: Was ist abweichend/unklar (1–2 Sätze)?
     2. 1–2 Vorschläge (inkl. „keine Aktion“) zur Auswahl darlegen.
     3. Auf Freigabe warten – keine Folgeaktionen bis Bestätigung.
   - Priorität: Dieses STOP hat Vorrang vor dem Moduswechsel‑Gate. Falls eine Lösung Code erfordert, danach Moduswechsel vorschlagen und bestätigen lassen.

 ## Modell-Profile & Moduswechsel (GPT‑5 ↔ GPT‑5 Codex)
 - Kurzdefinition: General = redaktionelle/Analyse‑Arbeiten; Codex = Code/Tests/Build‑/CI‑Arbeiten.
 - Standardmodus: GPT‑5 (General) für redaktionelle Arbeiten, Kanon-/Quellenabgleich, `[FACT]`↔`[FACT?]`‑Revalidierung, Policy-/Prozess‑Checks und Textkurierung.
 - Aktiver Modus wird zu Sitzungsbeginn sowie bei STOP-Gates im Chat bestätigt; dieser Abschnitt dokumentiert ausschließlich die Wechselheuristiken.
 - Codex-Modus (umschalten bei Bedarf): Für Code‑schwere Aufgaben wie Skripte/Validatoren, Tests/CI, API‑/Service‑Änderungen, Parser/RegEx, Datentransformationen.
 - Heuristische Trigger für Wechselvorschlag (nicht automatisch, nur Hinweis):
   - Edits in Quellcodepfaden: `novapolis_agent/app/**`, `novapolis_agent/scripts/**`, `novapolis_agent/utils/**`, `novapolis_agent/tests/**`, `packages/**`, `novapolis-rp/coding/**`.
   - Anforderung: „Bitte Skript/Validator/Test bauen“, „API anpassen“, „Pytest/Typing fixen“.
   - Geplante Ausführung technischer Tasks: Pytest/Mypy/Pyright, Linter-/Build‑Themen.
 - Erinnerung/Prompting‑Policy:
   - Wenn aktueller Modus = GPT‑5 und ein Trigger erkannt wird: „Hinweis: Moduswechsel zu Codex empfohlen für Code‑schwere Aufgaben. Bitte bestätigen.“
   - Wenn aktueller Modus = Codex und redaktionelle Arbeit erkannt wird: „Hinweis: Moduswechsel zu General empfohlen für redaktionelle Aufgaben. Bitte bestätigen.“
   - Nutzerentscheid respektieren; bei „nein“ weiter im aktuellen Modus arbeiten.
   - Explizite Nutzerwahl überschreibt Heuristik: „Modus Codex“/„Modus General“ setzt sofort um.

Essentials (konzentriert)
-------------------------
 ## Agent (Backend) – Essentials
   - Aktiver Codepfad: `novapolis_agent/app/**`, Hilfsskripte unter `novapolis_agent/scripts/`.
   - Grüne Gates: `pytest -q`, `pyright -p pyrightconfig.json`, `python -m mypy --config-file mypy.ini app scripts`, Coverage ≥ 80 % (`scripts/run_pytest_coverage.ps1`).
   - DONELOG-Pflicht: Änderungen in `app/`, `scripts/`, `utils/` im `novapolis_agent/docs/DONELOG.txt` protokollieren.
   - Streaming- und Rate-Limit-Checks berücksichtigen (`tests/test_app_*`, SSE-Events `meta`/`delta`/`done`).

 ## Dev‑Hub – Essentials
   - Arbeitsdokumentation lebt unter `novapolis-dev/docs/**` (todo, donelog, index, naming-policy).
   - Redirect-Stubs in `novapolis-rp/development/...` bleiben unverändert; echte Inhalte ausschließlich im Dev-Hub pflegen.
   - Struktur- oder Regeländerungen im `novapolis-dev/docs/donelog.md` und im Root-DONELOG festhalten; betroffene Tree-Artefakte aktualisieren.

 ## RP – AI Behavior Mapping (Canvas) – Überblick
   - Zweck: Domänen‑Canvas für Verhaltensmatrix (Cluster O/E/M/N/C/S/L/T, Intensität 01–99, Modifikatoren wie k/a/z/p/r/s/h).
   - Signaturformat: `<Anchor>=<Cluster><Intensität>-…-<Modifier>` (z. B. `R4=O82-T79-L70-E60-…-kpr`).
   - Anker‑Register und Beispiele: Siehe `novapolis-rp/database-rp/00-admin/AI-Behavior-Mapping.{md,json}`.
   - Anwendung: Leitplanken für Charakter‑Canvas, KI‑Interaktion, Missionsplanung; Validatoren/Reports sind in Arbeit.
   - Hinweis: Das Canvas bleibt in RP als SSOT bestehen; hier erfolgt nur die Kurzreferenz.

Repositoryweiter Rahmen
-----------------------
 - Gemeinsamer Code gehört nach `packages/novapolis_common`; doppelte Module aus den Teilprojekten nach Migration entfernen.
 - Konfigurationen bleiben projektspezifisch; Produktions- und API-Code verbleibt im jeweiligen Projektordner, Utilities werden über das Shared-Package re-exportiert.
 - Doppelte Modulpfade (z. B. parallele `novapolis_agent/novapolis_agent/**` und `novapolis_agent/app/**`) sind als Legacy zu behandeln; Neu‑Anpassungen bitte nur unter den aktiven Pfaden vornehmen (siehe `novapolis_agent/WORKSPACE_INDEX.md`).
 - Secrets (`.env`) bleiben lokal; ungefilterte Exporte ausschließlich unter `novapolis-rp/database-raw/99-exports/` ablegen.
 - Working docs (Projektweit) leben in `novapolis-dev/docs/` (todo, donelog, tests, naming-policy, copilot-behavior, index); `novapolis-rp/development/...` sind Redirect-Stubs.
 - Backups/Altstände gehören zentral nach `Backups/` (keine tool‑lesbaren Backups neben aktiven Configs).
 - Godot (Sim): Kanonische Projektdatei ist `novapolis-sim/project.godot` (Option A). Das frühere, verschachtelte Projekt wurde nach `Backups/novapolis-sim-archived-20251104/` verschoben.

Prüf- und Release-Checks
------------------------
 - Vor Commits relevante Tests/Skripte ausführen (Root‑basiert): `novapolis_agent/scripts/run_tests.py` (cwd=`novapolis_agent`), Validatoren unter `novapolis-rp/coding/tools/validators/`.
 - Bei Änderungen an Behaviour-/Policy‑Dokumenten zusätzlich den Test `novapolis_agent/tests/test_content_policy_profiles.py` laufen lassen und Changelogs prüfen. Diese Regel ist im Single‑Root‑TODO verlinkt.
 - Coverage-Gate: Task `Tests: coverage (fail-under)` muss ≥ 80 % liefern; bei Unterschreitung erfolgt kein Merge/Push ohne Freigabe.
 - Bei Unsicherheiten/Unklarheiten: STOP‑Gate setzen (Rückfrage einholen), dann mit Minimal‑Delta fortfahren; transparente Diffs mit Dateiliste/Diffstat, keine Shell‑Kommandos oder History‑Rewrites.

Release & Versionierung
-----------------------
 - Versionierung über `pyproject.toml`; Versionssprung + Git-Tag `vX.Y.Z` gehören in denselben PR.
 - `DONELOG.md` bzw. projektspezifische DONELOGs um einen Eintrag ergänzen (Wer/Was/Wann, kurzer Kontext).
 - Kein Release ohne grüne Gates (Tests, Types, Coverage, Frontmatter-Validator, Markdownlint bei Docs).

 - Hinweis (CI‑Workflows): Nur Workflows unter `.github/workflows/` am Repo‑Root sind wirksam. Kopien/Spiegel in Unterordnern (z. B. `novapolis_agent/.github/workflows/`) gelten als Stubs/Archiv und werden von GitHub Actions nicht ausgeführt. Cleanup als eigener Task vorschlagen (vorher eingehende Verweise prüfen).

Novapolis Agent (Backend)
-------------------------
 ## Arbeitskontext
   - Repo: `novapolis_agent` (Branch `main`), Stack: FastAPI + Ollama, Kern: `app/main.py`, `app/api/models.py`, `app/core/settings.py`, `app/core/prompts.py`.

 ## Schnellziele bei Codeänderungen
   - CI grün halten: Tests (`pytest`), Typen (Pyright/Mypy). CI prüft `docs/DONELOG.txt`.

   - Nach jedem Edit Tests/Typen sequentiell ausführen und Ergebnisse abwarten (`pytest -q` → `pyright -p pyrightconfig.json` → `python -m mypy --config-file mypy.ini app scripts`). Keine Vorab-Statusmeldungen.

 ## PR-/Push-Checks
   - Tests lokal: `pytest -q` oder passende Marker.
   - Typechecks: `pyright -p pyrightconfig.json`, `python -m mypy --config-file mypy.ini app scripts`; optional Task „Tests: coverage (fail-under 80%)“.
   - Änderungen an `app/`, `scripts/`, `utils/` → DONELOG-Update (Push auf main erfordert Eintrag; PR-Befreiung via Label `skip-donelog`).

 ## Pytest-Marker & Selektiver Lauf
   - Unit: `pytest -q -m unit`.
   - API/Streaming: `pytest -q -m "api or streaming"`.
   - Selektiv: `pytest -q -k test_rate_limit_headers_on_success`.

 ## API & Integration
   - Endpunkte: `/`, `/health`, `/version`, `POST /chat`, `POST /chat/stream` (SSE).
   - Prompts zentral in `app/core/prompts.py`; Kontext-Notizen via ENV `CONTEXT_NOTES_ENABLED=true`, Pfade in Settings.
   - Synonyme: Basis `eval/config/synonyms.json`, Overlay `eval/config/synonyms.local.json` (optional, Merge).

 ## Konventionen
   - Modelle ausschließlich über `app/api/models.py` importieren (nicht `app/schemas.py`).
   - Middleware setzt `X-Request-ID` auch bei Fehlern; HTTPException-Header werden gemergt.
   - Rate-Limit per ENV; Tests nutzen `monkeypatch.setenv(...)` und Module-Reload.

 ## Häufige Fehlerquellen
   - Streaming/SSE: Generator liefert Events; Tests erwarten `event: meta` mit `"policy_post"`, `event: delta` mit `"text"`, `event: done`.
   - Rate-Limit-Header: Bei Erfolg `X-RateLimit-{Limit,Remaining,Window}`, bei 429 zusätzlich `Retry-After`.
   - CORS-ENV `BACKEND_CORS_ORIGINS` akzeptiert JSON-Liste oder Komma-Liste (Validator in `settings`).

 ## Workflows & Artefakte
   - Lokal starten: `uvicorn app.main:app --reload` (Swagger `/docs`).
   - Finetune-Export/Prepare: Tasks „Finetune: export (latest)“ → `scripts/export_finetune.py`, „Finetune: prepare (split)“ → `scripts/prepare_finetune_pack.py` (Outputs `eval/results/finetune/`).

 ## Nachschlagen & Meta
 - CI/Workflows: `.github/workflows/ci.yml`, `.github/workflows/enforce-donelog.yml`.
   - Tests siehe `tests/` (u. a. `test_app_*` für Health/Request-ID/Rate-Limit; Streaming-/Policy-Tests definieren Format).
   - Skripte: `scripts/` (Eval/Export/Train/Reports) – vorhandene CLI-Optionen nutzen.
   - Beim Aktualisieren dieser Datei Hinweise aus den Agent‑Essentials oben beachten (Progress-Cadence, DONELOG, Shell-Hinweise); nach Änderungen Checks abwarten. Manuelle Reihenfolge für Vollprüfungen: erst `pytest -q`, dann `pyright -p pyrightconfig.json`, danach `python -m mypy --config-file mypy.ini app scripts`.
 - Feedbackbedarf (Marker, Tasks, Troubleshooting) kurz melden.

Novapolis-RP
------------
 ## Working Rules (Novapolis)
   - SSOT: **/Main/novapolis-dev/**.
   - Minimal und transparent: Diffs klein halten, betroffene Dateien und Diffstat nennen.
   - Keine Shell-Kommandos, keine History-Rewrites.
   - Working Docs liegen in `novapolis-dev/docs/` (todo, donelog, tests, naming-policy, copilot-behavior, index).
   - `novapolis-rp/development/...` sind Redirect-Stubs – nicht hineinschreiben.
   - Vor APPLY nach verbliebenen `development/docs`-Referenzen suchen (nur in Redirect-README und `meta.origin` erlaubt).
   - Nach APPLY sicherstellen, dass verschobene Docs Sidecars mit `source`, `origin`, `migrated_at` besitzen.

Workspace-Instructions (kompakt)
--------------------------------
 ## Primärer Kontext
   - Dev‑Hub: Siehe dieses Dokument (Essentials) sowie `novapolis-dev/docs/index.md` für Navigation & Prozess.
   - `novapolis-dev/docs/index.md` – Navigation & Prozessreferenz.
   - `novapolis-rp/database-raw/99-exports/README.md` – RAW-Policy (keine ungefilterten Daten nach `database-rp/`).

 ## Wichtige Regeln
   - Sprache: Deutsch (Erklärungen, Beispiele, Fehlermeldungen).
   - RAW-Only: Ungefilterte Exporte ausschließlich unter `database-raw/99-exports/` speichern.
   - Curation-Flow: Für RP-Nutzung stets Ingest/Curation verwenden (`coding/tools/curation/`).
   - Minimal-Delta: Änderungen klein halten; `novapolis-dev/docs/donelog.md` pflegen.
   - Sicherheit & Privacy: Keine Secrets; offline bevorzugen.

 ## Antworten & Format
   - Prägnant, skimmbar; kurze Sätze, Bullet-Listen ok, keine überladenen Blockzitate.
   - Bei größeren Aufgaben ToDo-Liste des betroffenen Moduls oder `Main/todo-root.md` ergänzen.

 ## Markdownlint (zentral)
   - MD003 = `setext_with_atx` (H1/H2 im Setext‑Stil, H3+ im ATX‑Stil; je Level konsistent innerhalb der Datei). Keine gemischten Stile für dasselbe Level in einer Datei.
   - Konfiguration erfolgt zentral über `.markdownlint-cli2.jsonc`; projektlokale Overrides nur nach Review und dokumentierter Ausnahme.
   - `ignores` in der CLI2‑Config decken generierte/kuratierte Bereiche ab (u. a. `novapolis_agent/eval/results/**`, `novapolis_agent/outputs/**`, `outputs/**`, `novapolis-rp/.pytest_cache/**`).
   - Vor Arbeiten mit Copilot/GPT‑5 Pflichtlauf im bestehenden Terminal: `npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc '**/*.md'` (ohne zusätzliche `pwsh -NoProfile -Command`-Hülle).
   - Auto‑Fix optional: `npx --yes markdownlint-cli2-fix --config .markdownlint-cli2.jsonc '**/*.md'`.
   - Grundsatz: Keine globalen CLI‑Installationen und keine Wrapper‑Skripte für Markdownlint verwenden; ausschließlich `npx --yes`.
   - Optionaler Zusatz: Für einen schnellen Dokumentations‑Lint direkt im Terminal ausführen:
     `npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-dev/docs/**/*.md' 'novapolis_agent/docs/**/*.md'`

 ## Diagnose‑Playbook bei Lint‑FAIL (pwsh, konservativ)
   - Ziel: Lint‑Fehler reproduzierbar erfassen, schnell auswerten und mit minimalem Risiko beheben.
   - Ausführung (repo‑weit, Konfiguration aus Root):
   - Bestehendes Terminal (PowerShell 7, `-NoProfile`) verwenden.
   - Vollständige Ausgabe in Datei sichern:
   - Beispiel: `npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc '**/*.md' 2>&1 | Tee-Object -FilePath lint_fail.out`
   - Analyse (PowerShell‑only, Python via Here‑String in `python -` pipen):
   - Hintergrund: Kein Bash, keine Backticks; UTF‑8 sicher; kein Multi‑Line `python -c`.
   - Muster (Interpreter anpassen, z. B. auf Workspace‑Venv):

  ```powershell
  $python = 'F:\VS Code Workspace\Main\.venv\Scripts\python.exe'  # ggf. anpassen
  $script = @"
  import pathlib, re
  from collections import defaultdict

  p = pathlib.Path('lint_fail.out')
  text = p.read_text(encoding='utf-8', errors='ignore')
  by_rule = defaultdict(list)
  for line in text.splitlines():
     # Erwartetes Format (markdownlint-cli2): path:line MDxxx/…
     m = re.match(r'^(.*?):\d+\s+(MD\d+)\b', line)
     if m:
         by_rule[m.group(2)].append(m.group(1))

  for rule, files in sorted(by_rule.items()):
     uniq = sorted(set(files))
     print(f"{rule}: {len(files)} Treffer in {len(uniq)} Dateien")
  "@
  $script | & $python -
  ```

 - Typische Befunde und Fixes:
   - MD012/no-multiple-blank-lines: Doppelte Leerzeilen entfernen (konservativ, nur überzählige Leerzeilen).
   - MD047/single-trailing-newline: Fehlende Abschluss‑Zeile am Dateiende hinzufügen (genau eine).
   - Akzeptanzchecks:
     - Nach Fix: optional enger Bereich erneut mit obigem npx‑Aufruf prüfen.
     - Voller Lauf mit `'**/*.md'` kann weiterhin FAIL sein, bis alle betroffenen Dateien bereinigt sind.
     - Ergebnisse kurz protokollieren (PASS/FAIL, ggf. Pfad zur Ausgabe z. B. `lint_fail.out`).

## Mirrors/Redirect‑Stubs
 - Unter `novapolis-rp/Main/novapolis-dev/docs/` liegen nur noch Redirect‑Stubs; Single Source of Truth ist `novapolis-dev/docs/**`.
 - Änderungen an Arbeitsregeln/Dokumentation ausschließlich in den Live‑Quellen vornehmen; Stubs nicht bearbeiten.

## Export/Importer
 - Export: `coding/tools/chat-exporter/` (Auto-Scroll, Inaktivitäts-Stop, speicherschonend).
 - Ingest: `coding/tools/curation/ingest_jsonl.py` (streamend, chunked, sanftes Cleaning).

## Ziele
 - Stabiles Gedächtnis (Admin: system-prompt/memory-bundle) und reibungsloser Szenenstart.
 - Reproduzierbare, nachvollziehbare Schritte (Dokumentation & kleine Commits).

