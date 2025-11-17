---
stand: 2025-11-16 06:52
update: Archivkopie (Stand/Checks ergänzt)
checks: geprüft (Frontmatter-Validator)
---

LLM-Dokumentenheader (nicht löschen)
====================================
- Type: Copilot Instruction Set / Project Governance
- Scope: Novapolis-Suite (VS Code Workspace Main)
- Language: Deutsch
- Encoding: UTF-8 / Unix-EOL
- Purpose: Legt alle verbindlichen Regeln, STOP-Gates, Policies und Ablaufprotokolle für Copilot-gestützte Aktionen im Projekt fest.
- Structure: Markdown (H1/H2 = Setext, H3+ = ATX) - hierarchisch eingerückt; jede Regel mit semantischem Kontext.
- Priority: Dieses Dokument ist SSOT (Single Source of Truth) für Copilot-Verhalten - es überschreibt lokale oder temporäre Session-Prompts.
- Precedence: Immer zuerst laden → alle Aktionen, Tests und Änderungen müssen den hier definierten Regeln folgen.
- Compliance: Wrapper-Policy, STOP-Gate, Frontmatter-Policy, Lint-Policy, Security-Checks, Logging-Receipt, Meta-/Systeminfo-Protokollierung.
- Audit: Jede Antwort oder Änderung endet mit einem Postflight-Block nach Abschnitt „Meta-/Systeminfo-Protokollierung“.
- Timestamp: 2025-11-14 14:50
- Änderung: Frühere Start-Checks abgeschafft; Postflight bleibt einzig verpflichtendes Gate, Wrapper-Guards übernehmen alle vorbereitenden Prüfungen.
<!-- markdownlint-disable MD022 MD032 MD036 -->

Kurzreferenz aller Überschriften dieser Anleitung
---
`.github/copilot-instructions-headings.md` (Extrakt der H1/H2/H3-Überschriften).


Dateipfad & Geltungsbereich
---
### Kanonischer Speicherort
- `.github/copilot-instructions.md` im Repo-Root. Nur hier abgelegte Inhalte gelten als verbindlich; Kopien/Backups dienen ausschließlich der Historie.
### Geltungsbereich
- Regeln gelten für Copilot Chat in VS Code, Inline-Completions, Apply-Patch-Befehle und agentische Funktionen (z. B. Tasks, Run-Code-Snippets). Bei Tools mit begrenztem Kontext immer die Kernregeln priorisieren und Details bei Bedarf im Chat referenzieren.
### Pfad-Disziplin
- Tippfehler oder abweichende Verzeichnisse (z. B. `.github/copilot-instuctions.md`, absichtliches Beispiel) werden ignoriert. Vor Änderungen prüfen, dass die editierte Datei exakt den kanonischen Pfad besitzt.

Primäre Behaviour-Quellen
---
### SSOT: Dieses Dokument ist die zentrale Verhaltens-/Arbeitsrichtlinie. Modul-/Domänenreferenzen
- Konsolidiert: Frühere Modulkopien (Agent/Dev-Hub) wurden in dieses Dokument überführt und entfernt.
- `novapolis-rp/database-rp/00-admin/AI-Behavior-Mapping.{md,json}`: Rollenspiel-spezifische Verhaltenshooks und Rollenmatrix (SSOT in RP).
- `novapolis-rp/development/docs/` enthielt Legacy-Stubs und wurde entfernt (2025-11-05). Verwende ausschließlich die oben genannte RP-Quelle und dieses Dokument.
#### Priorität
- 1. Dieses Dokument (global)
- 2. `novapolis-rp/database-rp/00-admin/AI-Behavior-Mapping.*` (RP-spezifisch)
- 3. `novapolis_agent/docs/DONELOG.txt` + Agent-Essentials (Backend-spezifisch)
   Bei Konflikten gilt die niedrigere Zahl.

Gemeinsamer Arbeitsstil
---
### Für verschiedene Optionen gibt es einen "Zustand", definiert als
- "(true)" Eintrag muss umgesetzt/befolgt werden.
- "(false)" Eintrag hat aktuell keine Gültigkeit. Muss mit `yyyy-MM-dd HH:mm` und `name` und kurze info z.b. Grund: & Aufgabe: usw. versehen.
- Einträge, die weder mit "(true)" noch mit "(false)" versehen sind, gelten als "(true)".
- Es gilt:
   - Übergeordnete Einträge gelten über alleinstehende und referenzierte Einträge.
- Standard-Antwortsprache ist Deutsch (Erklärungen, Beispiele, Fehlermeldungen).
### Arbeite iterativ, halte Tests und Typprüfungen grün, dokumentiere substanzielle Änderungen
- Root: `DONELOG.md`, `todo.root.md`.
- Agent: `novapolis_agent/docs/DONELOG.txt` (und projektinterne TODOs, falls vorhanden).
- Dev-Hub: `novapolis-dev/docs/donelog.md`, `novapolis-dev/docs/todo.*.md`.
- Weitere Projekt-TODOs nur, wenn tatsächlich vorhanden; ansonsten Root/Dev-Hub nutzen.
- Prägnanter Output: skimmbar, keine überladenen Blockzitate; bei großen Aufgaben Plan in betreffende todo eintragen.
- Root-Statusdateien `WORKSPACE_STATUS.md`, `workspace_tree_full.txt` und `workspace_tree_dirs.txt` als globalen Kontext heranziehen und nach größeren Umstrukturierungen oder mindestens monatlich aktualisieren. (zuletzt aktualisiert: 2025-11-08 21:18)

Onboarding & Setup
---
- Schnell-Index (häufig genutzte Themen)

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

Kanonische Prüfabläufe (pwsh)
---
### Empfohlen (Wrapper, Copilot/GPT)

```powershell
pwsh -File scripts\run_pytest_coverage.ps1
```

- `$maxTestFiles` (Standard 40) stellt sicher, dass nicht versehentlich zu viele Testdateien im Lauf landen. Bei Überschreitung stoppt der Befehl mit einer roten STOP-Notiz.
 
Hinweis (2025-11-12 06:45): Der konsolidierte Prüflauf erfolgt jetzt über `python scripts/run_checks_and_report.py`. STOP-Gate-Fehlerbehandlung und Exitcode-Regeln aus der früheren PowerShell-Variante wurden übernommen; der Wrapper erstellt weiterhin Postflight-Reports und setzt das `R-STOP`-Flag korrekt.
Modus (bei Review): GPT-5 mini (Agent-review), Postflight erforderlich; ToDo wurde erfüllt und in `.tmp-results/todo.cleaned.md` markiert.
Hinweis (2025-11-12 06:45): Das Python-Skript protokolliert alle Teilprüfungen (markdownlint, Frontmatter, Ruff/Black, Pyright, Mypy, Pytest) und generiert Markdown-/JSON-Reports unter `.tmp-results/reports/`. Die frühere PowerShell-Integration von `PSScriptAnalyzer` ist archiviert; bei Bedarf läuft der Analyzer separat über `scripts/`.
- Details und Begründung siehe Abschnitt „Kanonische Prüfabläufe (pwsh)“ weiter unten.
- Einmalig `& .\.venv\Scripts\python.exe -m pip install --upgrade pip` ausführen, falls Pip veraltet ist.
- Erste Validierung: Sequenz aus Lint (`ruff`, `black --check`), Typen (`pyright`, `mypy`) und Tests mit Coverage (Pytest ≥ 80 %) jeweils manuell via `pwsh -Command "& { ... }"` oder direkt in der aktiven pwsh-Session ausführen; Beispielbefehle siehe Abschnitt „Kanonische Prüfabläufe (pwsh)“.
 - Vor dokumentationsbezogenen Sessions mit Copilot bzw. GPT-5 zwingend `npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc '**/*.md'` ausführen (Achtung: Glob stets in einfachen Anführungszeichen, keine abschließenden Escape-Zeichen), um falsche Positivmeldungen in nachfolgenden Tests zu vermeiden. Den Befehl unverändert direkt im Terminal eingeben - keine `pwsh -Command`-Hülle verwenden.

### VS Code Tasks ausführen.(true)
- Grundlage: Die gleichnamigen VS Code Tasks dienen nur als Referenz. Copilot/GPT erstellt keine neuen VS Code Tasks.
- Copilot/GPT startet komplexe/mehrschrittige Abläufe nicht als Inline `-Command`, sondern bevorzugt über Skript-Wrapper via `pwsh -File <script.ps1>` (Profil erlaubt). Die nachfolgenden Inline-Beispiele sind dokumentarisch und für manuelle Human-Runs gedacht; Inline `-Command` bleibt nur für echte Einzeiler zulässig.

### Lint (Ruff + Black, keine Auto-Fixes)(true)
Hinweis: Für agentische Ausführung NICHT die nachfolgenden Inline-Muster verwenden:

```powershell
pwsh -Command "& { $ErrorActionPreference = 'Stop'; $root = '${workspaceFolder}'; Set-Location $root; $python = Join-Path $root '.venv\\Scripts\\python.exe'; if (-not (Test-Path -LiteralPath $python)) { $python = 'python'; }; & $python -m ruff check .; $ruffExit = $LASTEXITCODE; & $python -m black --check .; if ($ruffExit -ne 0 -or $LASTEXITCODE -ne 0) { exit 1 } }"
```

#### Typen (Pyright + Mypy)

```powershell
pwsh -Command "& { $ErrorActionPreference = 'Stop'; $root = '${workspaceFolder}'; $agent = Join-Path $root 'novapolis_agent'; Set-Location $agent; $pyright = Join-Path $root '.venv\\Scripts\\pyright.exe'; if (-not (Test-Path -LiteralPath $pyright)) { $pyright = 'pyright'; }; & $pyright -p pyrightconfig.json; if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }; $python = Join-Path $root '.venv\\Scripts\\python.exe'; if (-not (Test-Path -LiteralPath $python)) { $python = 'python'; }; & $python -m mypy --config-file mypy.ini app scripts; exit $LASTEXITCODE }"
```

#### Tests (Pytest Coverage ≥ 80 %)

```powershell
pwsh -Command "& { $ErrorActionPreference = 'Stop'; $root = '${workspaceFolder}'; $python = Join-Path $root '.venv\\Scripts\\python.exe'; if (-not (Test-Path -LiteralPath $python)) { $python = 'python'; }; $cover = Join-Path $root 'novapolis_agent'; $cover = Join-Path $cover '.coveragerc'; $cwd = Join-Path $root 'novapolis_agent'; Set-Location $cwd; $maxTestFiles = 40; $collectOutput = & $python -m pytest --collect-only 2>&1; $collectedFiles = $collectOutput | Where-Object { ``$_ -match '::' } | ForEach-Object { (``$_ -split '::')[0] }; $uniqueFiles = $collectedFiles | Sort-Object -Unique; $fileCount = $uniqueFiles.Count; if ($fileCount -gt $maxTestFiles) { Write-Host 'STOP: Zu viele Testdateien gesammelt (' + $fileCount + ' > ' + $maxTestFiles + '). Bitte Scope prüfen.'; exit 2 }; & $python -m pytest --cov --cov-report=term-missing --cov-branch --cov-config $cover --cov-fail-under=80; exit $LASTEXITCODE }"
if ($LASTEXITCODE -eq 0) { Write-Host 'Pytest PASS' } else { Write-Host "Pytest FAIL ($LASTEXITCODE)" }
```
> `$maxTestFiles` kann bei Bedarf angepasst werden; die STOP-Meldung verhindert, dass ungewollt große Testmengen laufen.
> Coverage-Gate ≥ 80 % (dynamischer Wert). Aktueller Prozentwert wird nicht hier festgeschrieben; führende Quelle: `WORKSPACE_STATUS.md`.

### Aggregierte Prüfung (`Checks: full`)
   - obige Befehle in der Reihenfolge Lint → Typen → Tests ausführen und Ergebnisse dokumentieren.

### Zusatz (pwsh)
   - Für Python-Befehle den Interpreter aus `.venv` verwenden (Fallback `python`), wie in den Beispielen gezeigt.
   - Bei Pfaden mit Leerzeichen `${workspaceFolder}` und `Join-Path` einsetzen.
   - Wrapper-Richtlinie: Wenn ein Befehl mehr als ~120 Zeichen umfasst, Artefakte schreibt (z. B. JUnit/Coverage/XML) oder mehrere logische Schritte enthält (Collect-Guard, Ausführung, Summary), als eigenes Skript unter `scripts/` ablegen und ausschließlich über `pwsh -File` starten. Keine mehrstufigen Inline-Blöcke mit verschachtelten `& { ... }` für solche Fälle.

### Update-Logistik
   - Zeitquelle: Bei jeder Angabe von Zeitstempeln muss die aktuelle lokale Systemzeit zum Zeitpunkt der Ausgabe frisch eingeholt werden (keine gecachten Werte, keine Vorausberechnung). Die Referenz ist der direkte Aufruf über PowerShell:
     - `Get-Date`
     - Gilt für alle Kontexte in diesem Dokument (z. B. Frontmatter `stand`, Logs/DONELOG, Postflight/Abort, Statusnotizen, Release-Einträge) und ist zwingend pro Ereignis erneut auszuführen.
   - Timestamp: Änderungen im Format `YYYY-MM-DD HH:mm` erfassen (aktuell) - gilt für Kopfzeilen („Stand“, „Letzte Aktualisierung“), DONELOG-Einträge und kurze Statusnotizen. Standard ist die lokale Systemzeit. Wer mit abweichender Zeitzone arbeitet, ergänzt im `update`-Feld den Offset (z. B. `UTC+02`) oder weist ihn im Text aus. Eine Umstellung auf `Z`/UTC erfolgt erst nach Anpassung des Validators.
   - Systemzeit (lokal, kanonisch): `Get-Date`.
   - PowerShell-Version (lokal): `Get-Host`.
   - Kurznotiz: 1-2 Sätze oder Bullet, was angepasst wurde (analog zu `novapolis-rp/database-rp/02-*`). Bei komplexeren Tasks optional Primärpfad referenzieren (`app/...`, `scripts/...`).
   - Prüfungen: Relevante Checks nennen (z. B. `pytest -q`, `pyright`, `markdownlint-cli2`) inkl. Ergebnis/Exit-Status; bei Bedarf Link/Dateipfad zur Ausgabe ergänzen.
   - Markdownlint-Läufe protokollieren: Lauf/Command + PASS/FAIL direkt nach dem Lauf im Status erwähnen.

### Workspace-Tree-Artefakte (Zuordnung)
 - „Workspace tree: full“ → `workspace_tree_full.txt`
 - „Workspace tree: directories“ → `workspace_tree.txt`
 - „Workspace tree: summary (dirs)“ → `workspace_tree_dirs.txt`
 - Dokumentpflege: Betroffene Artefakte synchron halten (Root: `todo.root.md`, `DONELOG.md`; Agent: `novapolis_agent/docs/DONELOG.txt`; Dev-Hub: `novapolis-dev/docs/todo.*.md`, `novapolis-dev/docs/donelog.md`; außerdem `WORKSPACE_INDEX.md`, `WORKSPACE_STATUS.md`, README/Index-Seiten). Strukturänderungen → zusätzlich Tree-Snapshots aktualisieren; Behaviour-Änderungen → dieses Dokument aktualisieren und Verweise prüfen.
 - Referenzen: Wenn vorhanden Issue-/PR-Links, Commit-Hash oder Kontextnotizen angeben (Inline oder als Fußnote). Für wiederkehrende Schritte Templates/Tasks im Root `.vscode/` ergänzen.
 - Nicht-triviale Änderungen → in zugehörige TODO oder DONELOG.

Markdownlint (zentral)
---
MD003 = `setext_with_atx` (H1/H2 im Setext-Stil, H3+ im ATX-Stil; je Level konsistent innerhalb der Datei). Keine gemischten Stile für dasselbe Level in einer Datei.
### Konfiguration erfolgt zentral über `.markdownlint-cli2.jsonc`; projektlokale Overrides nur nach Review und dokumentierter Ausnahme.
`ignores` in der CLI2-Config decken generierte/kuratierte Bereiche ab (u. a. `novapolis_agent/eval/results/**`, `novapolis_agent/outputs/**`, `outputs/**`, `novapolis-rp/.pytest_cache/**`).
### Vor Arbeiten mit Copilot/GPT-5 Pflichtlauf im bestehenden Terminal
`npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc '**/*.md'` (ohne zusätzliche `pwsh -Command`-Hülle).
- Auto-Fix optional: `npx --yes markdownlint-cli2-fix --config .markdownlint-cli2.jsonc '**/*.md'`.
### Grundsatz
Keine globalen CLI-Installationen und keine Wrapper-Skripte für Markdownlint verwenden; ausschließlich `npx --yes`.
### Optionaler Zusatz: Für einen schnellen Dokumentations-Lint direkt im Terminal ausführen
`npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-dev/docs/**/*.md' 'novapolis_agent/docs/**/*.md'`

YAML-Frontmatter (kompakt & LLM-freundlich)
---
   - Jede Datei mit Snapshot-Kopfzeile und eine YAML-Frontmatter am Dokumentanfang einpflegen.
   - Empfohlene Schlüssel (kurz und stabil):
     - `stand`: `YYYY-MM-DD HH:mm` (lokale Zeit (immer aktuell))
     - `update`: 1-2 Stichpunkte zur Änderung
     - `checks`: kurz zu den relevanten Prüfungen/Ergebnissen (z. B. „pytest -q PASS“)
   - Optional: `refs` (Issue/PR/Commit), `affected` (betroffene Dateien/Pfade)

   Beispiel:
     ---
     stand: 2025-11-01 09:05
     update: Task „DONELOG: append entry“ ergänzt.
     checks: keine
     ---

### Hinweise
   - Bei jedem Schreibvorgang Frontmatter-Zeitstempel und `update`/`checks` aktualisieren.
   - Ausnahme: Für dieses Dokument (`.github/copilot-instructions.md`) keine YAML-Frontmatter verwenden (Parser-Einschränkung). Snapshot hier weiterhin per `Stand:`-Zeile pflegen.
   - Fallback (allgemein): Wenn YAML-Frontmatter technisch nicht einsetzbar ist (Parser/Format-Einschränkung), nutze am Dokumentanfang eine kompakte Kopfzeile im Klartext:
     - Erste Zeile: `Stand: 2025-11-01 09:28 - Abschnitt X präzisiert.`
     - Optional darunter: `Checks: pytest -q PASS`
   - Beispiel:
     - `Stand: 2025-11-01 09:28 - Abschnitt X präzisiert.`
     - `Checks: pytest -q PASS`
 - Migrationsstatus & Historie: Siehe Archiv `novapolis-dev/archive/copilot-instructions-update-tode.archive.md`.

Frontmatter-Schutz (true)(robust gegen Delimiter-Verlust)
---
   - Ziel: Verhindern, dass die erste/letzte Frontmatter-Zeile (`---`) versehentlich entfernt oder verändert wird.
   - Editor-Policy (Markdown):
     - Format On Save für Markdown deaktivieren; Auto-Fixer/Prettier für Markdown nicht einsetzen.
     - Änderungen in der Frontmatter nur an Schlüsseln/Values (z. B. `stand`, `update`, `checks`) vornehmen - die Delimiter `---` oben/unten nie anfassen. Sollten diese fehlen und nichts im betrefenden Dokument spricht dagegen, füge die erste Zeile `---` wieder hinzu (yaml fix).
   - Validator-Gates:
     - Pre-commit: `scripts/check_frontmatter.py` verpflichtend ausführen; Commit bei Fehlern blocken.
     - Zusätzliche Sofort-Checks: erste Zeile exakt `---`, schließender Delimiter vorhanden, kein BOM vor dem öffnenden Delimiter.
     - CI: Frontmatter-Validator als Schritt im Root-Workflow (fail-fast außerhalb der Skip-Pfade).
   - Skip-Pfade (siehe `scripts/check_frontmatter.py`): `.venv/`, `Backups/`, `outputs/`, `novapolis_agent/eval/results/`, `novapolis_agent/outputs/`, `novapolis-rp/database-raw/`, `.pytest_cache/` (inkl. Varianten), `.tmp-results/`, `eval/results/tmp_summaries/`, `novapolis_agent/.tmp-results/` sowie diese Datei selbst.
   - Der Validator ist ein hartes Gate: Sowohl Pre-Commit als auch CI brechen bei Verstößen ab; ohne Fix gibt es keinen Push/kein Merge.

Dateiformat & EOL
---
Frontmatter-Policy (Konsolidiert)
---
Standard: Alle Markdown-Dokumente (außer Ausnahme GOV-EX-FM-001 für diese Datei) führen YAML-Frontmatter mit Schlüsseln `stand`, `update`, `checks`. Schutz: Erste und letzte `---` niemals automatisch modifizieren; Validator (`scripts/check_frontmatter.py`) erzwingt Gültigkeit und Skip-Pfade. Ausnahme GOV-EX-FM-001: Diese Governance-Datei behält nur Kopfzeile + „Stand“-Zeile, keine Frontmatter. Frühere Einzelabschnitte bleiben bis vollständiger Merge zur Referenz bestehen.
   - Referenzblock (immer exakt so belassen, nur Werte aktualisieren):

```
---
stand: YYYY-MM-DD HH:mm
update: Kurznotiz
checks: Kontext (z. B. pytest -q PASS)
---
```

   - Automatischer Fix: `scripts/check_frontmatter.py` ergänzt fehlende Start-Delimiter (`---`) sofort, sobald eine Frontmatter erkannt wird. Beim Speichern (z. B. via VS Code `runOnSave`) wird dadurch jede Datei wieder in den korrekten Zustand gebracht, auch wenn Copilot/GPT die erste Zeile versehentlich entfernt hat.
   - Stand-Aktualisierung: `python scripts/check_frontmatter.py --touch <datei.md>` setzt den `stand`-Wert auf die lokale Systemzeit (`Get-Date -Format 'yyyy-MM-dd HH:mm'`). Empfehlung: Als manuellen Schritt nach größeren Änderungen oder über eine lokale `runOnSave`-Regel ausführen.
   - Markdown-Dateien stets als UTF-8 ohne BOM speichern; der Validator schlägt bei BOM im ersten Zeichen fehl.
   - Genau eine abschließende Newline am Dateiende belassen (MD047), keine zusätzlichen Leerzeilen anhängen.
   - Git kümmert sich um Zeilenendungen (LF) im Repo; lokale CRLF-Konvertierungen sind erlaubt, solange der Commit wieder LF enthält. Bei Unsicherheiten `.gitattributes` respektieren und keinen Auto-Formatter einsetzen, der Frontmatter anfasst.

Definition of Done (Code & Docs)
---
   - **Code:** `pytest -q` PASS, `pyright -p pyrightconfig.json` PASS, `python -m mypy --config-file mypy.ini app scripts` PASS, Coverage ≥ 80 % (Task `Tests: coverage (fail-under)`), relevante DONELOG/TODO-Einträge aktualisiert, keine neuen TODO-Reste.
   - **Docs:** Frontmatter aktualisiert (`stand`/`update`/`checks`), Markdownlint PASS, Stilvorgaben (MD003) eingehalten, keine überzähligen Leerzeilen, Kontext-Referenzen (z. B. Primärpfade) ergänzt.

Security & Dependencies
---
   - Monatlich (mindestens) `pip-audit` oder vergleichbares Tool ausführen; Findings vor Merge/Release auflösen.
   - Abhängigkeiten pinnen (`requirements*.txt`, `pyproject.toml`); Versionssprünge dokumentieren (DONELOG + kurze Notiz).
   - Keine Secrets ins Repo commiten (`.env` bleibt lokal). Vor Uploads/Exports prüfen, ob sensible Daten sanitisiert sind.

Historisch (veraltet)
---
- Der vorangestellte Start-Check wurde am 2025-11-12 abgeschafft. Wrapper-Guards übernehmen seither alle vorbereitenden Prüfungen; neue Beiträge dürfen keine alten Bezeichner oder Parameter für diesen Schritt mehr einführen.
- Legacy-Receipts oder Archive mit entsprechenden Alt-Begriffen bleiben nur zur Nachvollziehbarkeit bestehen. Aktive Dokumente, Skripte und Beispiele müssen ausschließlich Postflight + Guard-Notation verwenden.

Meta- / Systeminfo-Protokollierung (Postflight & kompakter Meta-Block)
---
### Zweck
   - Revisionssichere Dokumentation aller Änderungen und Skriptausführungen über einen abschließenden Postflight-Block.
   - Kompakter Meta-Block nur für rein lesende / erklärende Antworten (ohne Dateimutationen oder Skriptläufe).

### Postflight (aktiv)
   - Nach jedem logisch abgeschlossenen Vorgang mit Dateimutationen oder Skript-/Testausführungen genau EIN Postflight-Block - dieser steht immer als letzter Block am Ende der ausgegebenen Nachricht.
   - Keine Zwischen-Postflights für Teilaktionen; Ergebnisse gesammelt ausgeben.
   - Abort-Fall: Meta: Modus=Abort, Modell=<GPT-5|GPT-5 Codex|GPT-5 mini>, Grund=<Kurzbeschreibung>, Zeitpunkt=<yyyy-MM-dd HH:mm>.
#### Format Postflight (erfolgreich)
   - Meta: Modus=Postflight, Modell=<GPT-5|GPT-5 Codex|GPT-5 mini>, Arbeitsverzeichnis=<Pfad>, RepoRoot=<Pfad>, PSScriptRoot=<Pfad>, PSVersion=<x.y.z>, Aufruf=pwsh -File <Pfad.zum.Skript.ps1>, SHA256=<Hash.der.Skriptdatei>, STOP-Gate=<aktiv/deaktiv>, Wrapper-Policy=<erfüllt/verletzt>, Wrapper-Guards=<GuardA:PASS|GuardB:PASS>, Quellen=<.github/copilot-instructions.md;README.md;...>, Aktion=<Kurzbeschreibung>
     - Prüfung: markdownlint=<PASS/FAIL>, ExitcodeLint=<N>, behobenLint=<ja/nein>, Frontmatter-Validator=<PASS/FAIL>, ExitcodeFM=<N>, behobenFM=<ja/nein>, Cleanup-WhatIf-Exit=<N>, behobenWhatIf=<ja/nein>, Cleanup-Real-Exit=<N>, behobenReal=<ja/nein>, WorkspaceScanRoot=<Zahl>, WorkspaceScanRecurse=<Zahl>
     - Regeln: IDs=<R-WRAP,R-STOP,R-FM,R-LINT,R-SCAN,R-CTX,R-SEC,R-LOG>, Details=R-WRAP über -File erzwungen; R-STOP aktiv vor Real; R-FM geprüft; R-LINT ausgeführt; R-SCAN Root-only; R-CTX Quellen geladen; R-SEC geprüft; R-LOG Receipt erstellt
     - Todos: offen=<Anzahl>, BeispielFix=<Kurzbeschreibung>, ReRun=<Testname>, Fällig=<Datum/Zeit>
       - Beispiel (Dummy):

          ```
         Meta: Modus=Postflight, Modell=GPT-5 Codex, Arbeitsverzeichnis=F:\VS Code Workspace\Main, RepoRoot=F:\VS Code Workspace\Main, PSScriptRoot=F:\VS Code Workspace\Main\scripts, PSVersion=7.4.1, Aufruf=pwsh -File scripts\run_linters.ps1, SHA256=..., STOP-Gate=aktiv, Wrapper-Policy=erfüllt, Wrapper-Guards=PfadCheck:PASS|StopGate:PASS, Quellen=.github/copilot-instructions.md;README.md, Aktion=Lint-Checks aktualisiert
         Prüfung: markdownlint=PASS, ExitcodeLint=0, behobenLint=nein, Frontmatter-Validator=PASS, ExitcodeFM=0, behobenFM=nein, Cleanup-WhatIf-Exit=0, behobenWhatIf=nein, Cleanup-Real-Exit=0, behobenReal=nein, WorkspaceScanRoot=0, WorkspaceScanRecurse=0
          Regeln: IDs=R-WRAP,R-STOP,R-FM,R-LINT,R-SCAN,R-CTX,R-SEC,R-LOG, Details=R-WRAP über -File erzwungen; R-STOP aktiv bestätigt; R-FM geprüft; R-LINT ausgeführt; R-SCAN Root-only; R-CTX Quellen geladen; R-SEC geprüft; R-LOG Receipt erstellt
          Todos: offen=12, BeispielFix=Markdownlint-Report verlinkt, ReRun=pytest -q, Fällig=2025-11-12 17:00
          Ende: Timestamp=2025-11-12 04:00
          ```
     - Ende: Timestamp=<yyyy-MM-dd HH:mm>

### Kompakter Meta-Block (rein lesend)
   - Format (einzeilig, komma-separiert): Meta: Modus=General, Modell=<GPT-5|GPT-5 Codex|GPT-5 mini|optional>, Aktion=<Kurzbeschreibung>, Timestamp=<yyyy-MM-dd HH:mm>[, Arbeitsverzeichnis=<Pfad>]
   - Minimalbeispiel: Meta: Modus=General
   - Keine sensitiven Daten; nur verwenden, wenn kein Postflight nötig ist.

Semantische Regeln (Agent-spezifisch, kuratiert)
---
Zweck: Präzise, maschinen- und agentenfreundliche Auslegung zentraler Arbeitsregeln. Zustandsfelder verwenden normierte Bedeutungen (siehe Tabelle „Regelzustände“).

Regelzustände (Normativ)
 - aktiv / true / an: Regel ist verbindlich und muss eingehalten werden.
 - aus / false / off: Regel ist temporär deaktiviert; Verstöße führen nicht zum Abbruch, aber sollen optional dokumentiert werden, falls "test" nicht gesetzt.
 - scharf / ready / strikt: Regel löst vor auslösenden Aktionen zwingend ein STOP-Gate aus (Bestätigungspflicht). Kombination mit "aktiv" → höchste Strenge.
 - test / testing / beobachtung: Regel wird nicht erzwungen, aber Verstöße werden gemeldet (Log / Hinweis im Receipt) und können zur Aktivierung führen.

A. Postflight Logik
 1. Wrapper-Guards (aktiv): Vor jeder Dateiänderung oder skriptgestützten Mutation definierte Guard-Prüfungen ausführen (Pfad-Check, STOP-Gate-Bewertung, Kontextquellen). Guards ersetzen sämtliche vormals vorgeschalteten Start-Prüfungen und dienen ausschließlich als Abbruchkriterium vor dem eigentlichen Schritt.
 2. Postflight (aktiv): Nach jeder Dateiänderung oder Skript-/Testausführung genau EIN Postflight am Ende des vollständigen Vorgangs.
 3. Keine Dateimutationen ohne nachfolgenden Postflight-Receipt.
 4. "behoben=ja" nur, wenn ein Prüfschritt im selben Lauf erst FAIL und dann PASS war; bei sofortigem PASS "behoben=nein".

B. Quellen / Kontext
 5. Quellenpfade in Guard-Checks und Postflights als absolute Pfade aufführen (aktiv): Mindestens `.github/copilot-instructions.md` und alle unmittelbar betroffenen Arbeitsdateien.
 6. TODO-Propagation (test): Automatische Übernahme von neu erkannten TODOs in `todo.root.md` ist optional; bis zur expliziten Aktivierung nur dokumentieren.

C. Zeit / Timestamps
 7. Timestamp-Format (aktiv): `YYYY-MM-DD HH:mm` lokale Zeit (Europe/Berlin); pro Ereignis frisch via `Get-Date` ermittelt.
 8. Kein Reuse früherer Zeitstempel (aktiv): Jeder Postflight holt Zeit erneut.

D. STOP-Gate Interaktion
 9. STOP-Gate Vorrang (aktiv, scharf): Bei Unsicherheit/Abweichung ruht jede ausführende Aktion bis Bestätigung. Auslöser: Regelfehler, widersprüchliche Prioritäten, fehlende Quellen, unklare Moduswahl.

E. Modus / Profile
 10. Moduswahl heuristisch (test): Empfehlung gemäß Mapping (siehe Tabelle unter „Modell-Profile & Moduswechsel“), aber Nutzerentscheidung hat Vorrang.

F. Receipt Felder
 11. Todos: offen=<Anzahl> zählt verbleibende offene Items aus dem relevanten Kontext (aktiv). Bei fehlender Ermittlung test.
 12. BeispielFix: Kurzbeschreibung einer einzelnen konkreten Korrektur (aktiv) - leer lassen, wenn keine Korrektur stattfand.

G. Validierung
 13. Reihenfolge der Prüfungen (aktiv): Lint → Typen → Tests → Coverage (falls umfassend). Abweichungen dokumentieren.
 14. Minimale Datenerfassung (aktiv): Keine sensiblen Daten (Secrets/PII) in Meta-Blöcken.

Hinweis (Konsolidierung): Die früheren Einträge Sem01-Sem07 wurden in strukturierter Form abgelöst; Sem06 unklar formuliert → nun als TODO-Propagation (test) präzisiert.

Definition der Regel-IDs (zur Verwendung im Feld „Regeln: IDs=…“)
-----------------------------------------------------------------
 - Regelkennungen (IDs) sind standardisierte Kurzbezeichner, die in der gesamten Arbeitsumgebung und in allen automatisierten Ausgaben konsistent verwendet werden müssen.
 - Sie dienen der Verkürzung, Maschinenlesbarkeit und Querverweiskontrolle zwischen Prüf-, Skript- und Log-Systemen.
 - Dieser Abschnitt gilt als verbindlicher Bestandteil der SSOT (Single Source of Truth) für alle Automatisierungen innerhalb der Novapolis-Suite.
 - Alle Agenten, Skripte und Copilot-Instanzen müssen diese Struktur respektieren, bevor eine Änderung ausgeführt oder ein Receipt erstellt wird.
 - Abweichungen sind nur mit expliziter Freigabe im STOP-Gate zulässig.

### aktuell vergebene Regel-IDs
   - ID R-WRAP: Wrapper-Policy - Skripte und Mehrschritt-Prozesse dürfen ausschließlich über „pwsh -File“ mit absolutem Pfad ausgeführt werden. Inline „-Command“ ist nur für echte Einzeiler erlaubt.
   - ID R-STOP: STOP-Gate - Jede modusrelevante oder sicherheitskritische Aktion muss vor Ausführung explizit bestätigt werden.
   - ID R-FM: Frontmatter-Policy - Dokumente müssen gültige YAML-Frontmatter-Blöcke mit definierten Schlüsseln (stand, update, checks) enthalten. Fehlende oder beschädigte Frontmatter werden durch den Validator erkannt und gemeldet.
   - ID R-LINT: Markdownlint-Policy - Dokumente müssen die Style-Regeln MD001-MD050 einhalten; insbesondere MD003 (Setext für H1/H2, ATX ab H3).
   - ID R-SCAN: Workspace-Scan - Definiert, ob der Workspace-Scan nur auf Root-Ebene oder rekursiv erfolgen darf. Standard ist Root-only by design.
   - ID R-CTX: Kontextquelle - Stellt sicher, dass alle relevanten Steuerdateien (.github/copilot-instructions.md, README.md, single-root-todo.md usw.) vor einer Aktion geladen und im Kontext referenziert wurden.
   - ID R-SEC: Sicherheitsprinzip - Keine destruktiven Änderungen ohne vorherige WhatIf-Phase, minimalinvasive Diffs, keine automatischen Löschungen außerhalb des Skriptkontextes.
   - ID R-LOG: Receipt-Pflicht - Nach jedem abgeschlossenen Vorgang muss ein vollständiger, formalisierter Postflight-Log (Receipt) im DONELOG.md angelegt oder ergänzt werden.
   - ID R-COV: Coverage-Gate (Mindest-Coverage ≥80% vor Merge durchsetzen)
   - ID R-IDX: Headings-Index-Pflege (Aktualisierung bei strukturrelevanten Änderungen)
   - ID R-COMM: Kommunikationsstil (prägnant, deutsch, keine Füllphrasen)
   - ID R-RED: Redundanz-Handling (Duplikate nur mit Freigabe entfernen, vorher melden)
   - ID R-TODO: Konsistenz von TODO/DONELOG-Einträgen (Format, Pflichtfelder)
   - ID R-TIME: Timestamp-Konvention (lokales Format yyyy-MM-dd HH:mm; Quelle pwsh Get-Date)
   - ID R-SAFE: Minimaländerungen ohne semantischen Eingriff (nur Orthografie/Lint, wenn eingeschränkt erlaubt)

Ergänzende Präzisierungen (Determinismus & Prozessanker)
---
- Determinismus: Bei Generator-Runs werden zwei Läufe verglichen; Zeitanteile (Frontmatter-Timestamps, datumsbasierte Dateinamen) werden ignoriert; Bodies müssen textgleich sein, sonst STOP.
- R-IDX Pflege: Headings-Index wird derzeit manuell aktualisiert (`.github/copilot-instructions-headings.md`); Script kann später ergänzt werden.
- R-TODO Quelle: SSOT für Zählung `Todos: offen` ist `todo.root.md`; modulare TODO-Dateien sind optional und nicht Teil der Kennzahl.
- R-WRAP Schwelle: Ein Einzeiler umfasst max. einen Prozessaufruf und höchstens einen Pipe-Schritt; darüber Wrapper via `pwsh -File` zwingend.
- R-SCAN: Live-Scans nur Root-Ebene (aktiv); Artefakt-Skripte dürfen rekursiv Snapshots erzeugen (aktiv). Terminologie vereinheitlicht auf „aktiv“ / „deaktiviert“.
- Security-Takt: Monatlicher `pip-audit` Lauf; Ergebnis (PASS/Findings) wird als Kurzzeile in `WORKSPACE_STATUS.md` dokumentiert.

STOP-Gates & Modi
---
### STOP-Gate (Hard & Soft, aktiv)
Klassen:
- Hard-Trigger (Mutation/Sicherheit): Code-/Script-Änderungen, Validator-/Testläufe mit Seiteneffekten, Policy-/SSOT-Anpassungen. Ablauf: Empfehlung Moduswahl, explizite Bestätigung zwingend, keine Ausführung vor Freigabe.
- Soft-Trigger (Mehrdeutigkeit/Konflikt): Unklare Quellen, widersprüchliche Regeln, Moduskonflikte, unspezifizierte Pfade. Ablauf: Kurzstatus + 1-2 Handlungsoptionen; Bestätigung vor Fortsetzung.
Gemeinsame Regeln: Beidseitig (Code & Redaktion), triviale Gespräche ausgenommen, keine automatische Task-Kaskade während STOP. Hard hat Vorrang bei gleichzeitigem Auftreten. RAW/noisy/staging Bereiche: nur Soft solange keine Mutation.

Modell-Profile & Moduswechsel (GPT-5, GPT-5 Codex, GPT-5 mini)
---
### General (GPT-5)
   - Zweck: Hochwertiger redaktioneller und Analyse-Modus für Policy-Kurierung, Quellenabgleich, strukturierte Reviews, semantische Validierung und präzise Zusammenfassungen.
### Codex (GPT-5 Codex)
   - Zweck: Code-, Test-, Build-/CI- und Refactor-orientierter Modus für technische Skripte, Parser, Typ-/Lint-kritische Änderungen und Implementierungen.
### Mini (GPT-5 mini)
   - Zweck: Schneller, kosteneffizienter Tagesmodus mit großem Lesekontext; ideal für breite Datei-Reviews, Dokumentationspflege, Massentriage von TODO/Logs, konservative Low-Risk-Fixes und umfangreiche Übersichtsausgaben. Nicht erste Wahl für heikle Refactors, migrationskritische Schritte oder SSOT-Neufassung.
#### Standardmodus
   - Standard: General (GPT-5) für redaktionelle Arbeiten und initialen Kontext. Wechsel zu Codex bei Code-/Test-/CI-Schwerpunkt; Wechsel zu Mini bei großflächigen Review-/Pflegeaufgaben.
#### Heuristische Trigger
   - Codex-Trigger: Edits in `novapolis_agent/app/**`, `novapolis_agent/scripts/**`, `novapolis_agent/utils/**`, `novapolis_agent/tests/**`, `packages/**`, `novapolis-rp/coding/**`; Anforderungen wie „Validator bauen“, „API anpassen“, „Pytest fixen“.
   - Mini-Trigger: Viele Dateien gleichzeitig lesen, Bulk-Dokumentationspflege, Log-/TODO-Massentriage, konservative Streu-Fixes ohne tiefen Codeeingriff.
   - General-Trigger: Policy-/Prozess-Anpassungen, SSOT-Abgleich, semantische Strukturierung.
#### Mapping-Tabelle (Agent-orientiert)
| Aktion/Signal | Empfohlener Modus | Primäre Gründe | STOP-Risiko |
|---------------|-------------------|----------------|-------------|
| Patch/Code-Refactor (app/, scripts/) | Codex | Präzise Codeanalyse, Typsicherheit | Mittel |
| Tests/Typen/Coverage Lauf | Codex | Sequenz Lint→Typen→Tests | Niedrig |
| Große Doku-Sweeps (>10 Dateien) | Mini | Performance, breiter Lesekontext | Niedrig |
| Einzelne Policy-/Governance-Anpassung | General | Semantische Präzision | Hoch |
| Mehrfachanalyse Logs/Reports (read-only) | Mini | Breite Sicht, kein Codeeingriff | Niedrig |
| Modulstrategie / Roadmap-Neuordnung | General | Priorisierung, semantische Struktur | Mittel |
| Ambigue Moduswahl / Konflikt | General (Fallback) | Neutraler Review | Hoch |
#### Zustands-Annotation (optional)
"aktiv" = Mapping anwenden; "test" = Empfehlung loggen aber freie Wahl; "scharf" = STOP vor Abweichung von empfohlenem Modus.
#### Prompting-Policy
   - Bei erkanntem Trigger Hinweis auf empfohlenen Moduswechsel; Nutzerentscheidung ist maßgeblich.
   - Explizite Wahl („Modus Codex“, „Modus General“, „Modus Mini“) setzt sofort um.

Essentials (konzentriert)
---
### Agent (Backend) - Essentials
   - Aktiver Codepfad: `novapolis_agent/app/**`, Hilfsskripte unter `novapolis_agent/scripts/`.
   - Grüne Gates: `pytest -q`, `pyright -p pyrightconfig.json`, `python -m mypy --config-file mypy.ini app scripts`, Coverage ≥ 80 % (`scripts/run_pytest_coverage.ps1`).
   - DONELOG-Pflicht: Änderungen in `app/`, `scripts/`, `utils/` im `novapolis_agent/docs/DONELOG.txt` protokollieren.
   - Streaming- und Rate-Limit-Checks berücksichtigen (`tests/test_app_*`, SSE-Events `meta`/`delta`/`done`).

### Dev-Hub - Essentials
   - Arbeitsdokumentation lebt unter `novapolis-dev/docs/**` (todo, donelog, index, naming-policy).
   - Redirect-Stubs in `novapolis-rp/development/...` bleiben unverändert; echte Inhalte ausschließlich im Dev-Hub pflegen.
   - Struktur- oder Regeländerungen im `novapolis-dev/docs/donelog.md` und im Root-DONELOG festhalten; betroffene Tree-Artefakte aktualisieren.

### RP - AI Behavior Mapping (Canvas) - Überblick
   - Zweck: Domänen-Canvas für Verhaltensmatrix (Cluster O/E/M/N/C/S/L/T, Intensität 01-99, Modifikatoren wie k/a/z/p/r/s/h).
   - Signaturformat: `<Anchor>=<Cluster><Intensität>-…-<Modifier>` (z. B. `R4=O82-T79-L70-E60-…-kpr`).
   - Anker-Register und Beispiele: Siehe `novapolis-rp/database-rp/00-admin/AI-Behavior-Mapping.{md,json}`.
   - Anwendung: Leitplanken für Charakter-Canvas, KI-Interaktion, Missionsplanung; Validatoren/Reports sind in Arbeit.
   - Hinweis: Das Canvas bleibt in RP als SSOT bestehen; hier erfolgt nur die Kurzreferenz.

Repositoryweiter Rahmen
---
- Gemeinsamer Code gehört nach `packages/novapolis_common`; doppelte Module aus den Teilprojekten nach Migration entfernen.
- Konfigurationen bleiben projektspezifisch; Produktions- und API-Code verbleibt im jeweiligen Projektordner, Utilities werden über das Shared-Package re-exportiert.
- Doppelte Modulpfade (z. B. parallele `novapolis_agent/novapolis_agent/**` und `novapolis_agent/app/**`) sind als Legacy zu behandeln; Neu-Anpassungen bitte nur unter den aktiven Pfaden vornehmen (siehe `WORKSPACE_INDEX.md`).
- Secrets (`.env`) bleiben lokal; ungefilterte Exporte ausschließlich unter `novapolis-rp/database-raw/99-exports/` ablegen.
- Working docs (Projektweit) leben in `novapolis-dev/docs/` (todo, donelog, tests, naming-policy, copilot-behavior, index); `novapolis-rp/development/...` sind Redirect-Stubs.
- Backups/Altstände gehören zentral nach `Backups/` (keine tool-lesbaren Backups neben aktiven Configs).
- Godot (Sim): Kanonische Projektdatei ist `novapolis-sim/project.godot` (Option A). Das frühere, verschachtelte Projekt wurde nach `Backups/novapolis-sim-archived-20251104/` verschoben.

Prüf- und Release-Checks
------------------------
- Vor Commits relevante Tests/Skripte ausführen (Root-basiert): `novapolis_agent/scripts/run_tests.py` (cwd=`novapolis_agent`), Validatoren unter `novapolis-rp/coding/tools/validators/`.
- Bei Änderungen an Behaviour-/Policy-Dokumenten zusätzlich den Test `novapolis_agent/tests/test_content_policy_profiles.py` laufen lassen und Changelogs prüfen. Diese Regel ist im Single-Root-TODO verlinkt.
- Coverage-Gate: Task `Tests: coverage (fail-under)` muss ≥ 80 % liefern; bei Unterschreitung erfolgt kein Merge/Push ohne Freigabe.
- Bei Unsicherheiten/Unklarheiten: STOP-Gate setzen (Rückfrage einholen), dann mit Minimal-Delta fortfahren; transparente Diffs mit Dateiliste/Diffstat, keine Shell-Kommandos oder History-Rewrites.

Release & Versionierung
-----------------------
- Versionierung über `pyproject.toml`; Versionssprung + Git-Tag `vX.Y.Z` gehören in denselben PR.
- `DONELOG.md` bzw. projektspezifische DONELOGs um einen Eintrag ergänzen (Wer/Was/Wann, kurzer Kontext).
- Kein Release ohne grüne Gates (Tests, Types, Coverage, Frontmatter-Validator, Markdownlint bei Docs).

- Hinweis (CI-Workflows): Nur Workflows unter `.github/workflows/` am Repo-Root sind wirksam. Kopien/Spiegel in Unterordnern (z. B. `novapolis_agent/.github/workflows/`) gelten als Stubs/Archiv und werden von GitHub Actions nicht ausgeführt. Cleanup als eigener Task vorschlagen (vorher eingehende Verweise prüfen).

Doku-Update (true)
---
Bedeutung: Wenn aktiv, hält Copilot alle relevanten Arbeitsdokumente synchron, sobald eine Änderung fachlich oder strukturell wirksam ist.
Trigger (auslösend, nicht optional): neue/verschobene/umbenannte Dateien, geänderte Tests/Lints/Validatoren, Behaviour-Änderungen, Release-Schritte, aktualisierte Skripte oder Workflows.
Pflichtschritte pro Änderungsfall:
- TODOs aktualisieren: erledigte Punkte abhaken/verschieben, neue Nacharbeiten erfassen (Root `todo.root.md`, Dev-Hub `novapolis-dev/docs/todo.*.md`, projektspezifische TODOs nur wenn vorhanden).
- DONELOG ergänzen: kurzer, prüfbarer Receipt mit Wer/Was/Wann/Kontext (Root `DONELOG.md`, Agent `novapolis_agent/docs/DONELOG.txt`, Dev-Hub `novapolis-dev/docs/donelog.md`).
- READMEs/Indexseiten synchronisieren: betroffene Abschnitte, Links, Anker und Zählungen nachziehen (insb. `novapolis-dev/docs/index.md`, `WORKSPACE_INDEX.md`).
- Frontmatter pflegen: `stand` mit lokaler Systemzeit `yyyy-MM-dd HH:mm`, `update` kurz, `checks` mit relevanten Ergebnissen; keine Delimiter anfassen.
- Lint/Validator laufen lassen und Ergebnis notieren: `markdownlint-cli2` für Docs, Frontmatter-Validator; nur grüne Zustände gelten als abgeschlossen.
- Strukturänderungen dokumentieren: bei Verschiebungen/Neuordnung Arbeitsbaum-Artefakte aktualisieren (`workspace_tree_full.txt`, `workspace_tree_dirs.txt`) und in den Statusdateien vermerken (`WORKSPACE_STATUS.md`).
### Grenzen: rein orthografische Mikro-Fixes ohne semantische Wirkung dürfen gebündelt werden, solange Frontmatter, Lint und Status grün bleiben.
### STOP-Gate: Unklarheit über Geltungsbereich, kollidierende Quellen oder rote Checks erzwingen STOP; erst nach Klärung fortfahren.

Die Hauptmodule
---
### Novapolis Agent (Backend)
#### Arbeitskontext
- Repo: `novapolis_agent` (Branch `main`), Stack: FastAPI + Ollama, Kern: `app/main.py`, `app/api/models.py`, `app/core/settings.py`, `app/core/prompts.py`.
#### Schnellziele bei Codeänderungen
- CI grün halten: Tests (`pytest`), Typen (Pyright/Mypy). CI prüft `docs/DONELOG.txt`.
- Nach jedem Edit Tests/Typen sequentiell ausführen und Ergebnisse abwarten (`pytest -q` → `pyright -p pyrightconfig.json` → `python -m mypy --config-file mypy.ini app scripts`). Keine Vorab-Statusmeldungen.
#### PR-/Push-Checks
- Tests lokal: `pytest -q` oder passende Marker.
- Typechecks: `pyright -p pyrightconfig.json`, `python -m mypy --config-file mypy.ini app scripts`; optional Task „Tests: coverage (fail-under 80%)“.
- Änderungen an `app/`, `scripts/`, `utils/` → DONELOG-Update (Push auf main erfordert Eintrag; PR-Befreiung via Label `skip-donelog`).
#### Pytest-Marker & Selektiver Lauf
- Unit: `pytest -q -m unit`.
- API/Streaming: `pytest -q -m "api or streaming"`.
- Selektiv: `pytest -q -k test_rate_limit_headers_on_success`.
#### API & Integration
- Endpunkte: `/`, `/health`, `/version`, `POST /chat`, `POST /chat/stream` (SSE).
- Prompts zentral in `app/core/prompts.py`; Kontext-Notizen via ENV `CONTEXT_NOTES_ENABLED=true`, Pfade in Settings.
- Synonyme: Basis `eval/config/synonyms.json`, Overlay `eval/config/synonyms.local.json` (optional, Merge).
#### Konventionen
- Modelle ausschließlich über `app/api/models.py` importieren (nicht `app/schemas.py`).
- Middleware setzt `X-Request-ID` auch bei Fehlern; HTTPException-Header werden gemergt.
- Rate-Limit per ENV; Tests nutzen `monkeypatch.setenv(...)` und Module-Reload.
#### Häufige Fehlerquellen
- Streaming/SSE: Generator liefert Events; Tests erwarten `event: meta` mit `"policy_post"`, `event: delta` mit `"text"`, `event: done`.
- Rate-Limit-Header: Bei Erfolg `X-RateLimit-{Limit,Remaining,Window}`, bei 429 zusätzlich `Retry-After`.
- CORS-ENV `BACKEND_CORS_ORIGINS` akzeptiert JSON-Liste oder Komma-Liste (Validator in `settings`).
#### Workflows & Artefakte
- Lokal starten: `uvicorn app.main:app --reload` (Swagger `/docs`).
- Finetune-Export/Prepare: Tasks „Finetune: export (latest)“ → `scripts/export_finetune.py`, „Finetune: prepare (split)“ → `scripts/prepare_finetune_pack.py` (Outputs `eval/results/finetune/`).
#### Nachschlagen & Meta
- CI/Workflows: `.github/workflows/ci.yml`, `.github/workflows/enforce-donelog.yml`.
- Tests siehe `tests/` (u. a. `test_app_*` für Health/Request-ID/Rate-Limit; Streaming-/Policy-Tests definieren Format).
- Skripte: `scripts/` (Eval/Export/Train/Reports) - vorhandene CLI-Optionen nutzen.
- Beim Aktualisieren dieser Datei Hinweise aus den Agent-Essentials oben beachten (Progress-Cadence, DONELOG, Shell-Hinweise); nach Änderungen Checks abwarten. Manuelle Reihenfolge für Vollprüfungen: erst `pytest -q`, dann `pyright -p pyrightconfig.json`, danach `python -m mypy --config-file mypy.ini app scripts`.
- Feedbackbedarf (Marker, Tasks, Troubleshooting) kurz melden.

### Novapolis-RP
#### Working Rules (Novapolis)
- SSOT: **/Main/novapolis-dev/**.
- Minimal und transparent: Diffs klein halten, betroffene Dateien und Diffstat nennen.
- Keine Shell-Kommandos, keine History-Rewrites.
- Working Docs liegen in `novapolis-dev/docs/` (todo, donelog, tests, naming-policy, copilot-behavior, index).
- `novapolis-rp/development/...` sind Redirect-Stubs - nicht hineinschreiben.
- Vor APPLY nach verbliebenen `development/docs`-Referenzen suchen (nur in Redirect-README und `meta.origin` erlaubt).
- Nach APPLY sicherstellen, dass verschobene Docs Sidecars mit `source`, `origin`, `migrated_at` besitzen.

Workspace-Instructions (kompakt)
---
### Primärer Kontext
- Dev-Hub: Siehe dieses Dokument (Essentials) sowie `novapolis-dev/docs/index.md` für Navigation & Prozess.
- `novapolis-dev/docs/index.md` - Navigation & Prozessreferenz.
- `novapolis-rp/database-raw/99-exports/README.md` - RAW-Policy (keine ungefilterten Daten nach `database-rp/`).

### Wichtige Regeln
- Sprache: Deutsch (Erklärungen, Beispiele, Fehlermeldungen).
- RAW-Only: Ungefilterte Exporte ausschließlich unter `database-raw/99-exports/` speichern.
- Curation-Flow: Für RP-Nutzung stets Ingest/Curation verwenden (`coding/tools/curation/`).
- Minimal-Delta: Änderungen klein halten; `novapolis-dev/docs/donelog.md` pflegen.
- Sicherheit & Privacy: Keine Secrets; offline bevorzugen.

### Antworten & Format
- Prägnant, skimmbar; kurze Sätze, Bullet-Listen ok, keine überladenen Blockzitate.
- Bei größeren Aufgaben ToDo-Liste des betroffenen Moduls oder `Main/todo-root.md` ergänzen.


### Temporäre Aufgaben-Daten (.tmp-results)
- Zweck: Schneller, kuratierter Arbeitsauszug für Copilot/GPT ohne die SSOT zu verändern. SSOT bleibt `todo.root.md`.
- Dateien: `/.tmp-results/todo.cleaned.md` (menschlich lesbar) und `/.tmp-results/todo.cleaned.json` (maschinenlesbar, priorisiert).
- Nutzung (Copilot/GPT):
   - Bei ToDo-/Planungsaufgaben zuerst `todo.cleaned.json` laden und verwenden; bei Abweichungen zu `todo.root.md` → STOP und Rückfrage.
   - Änderungen an Aufgabenlisten niemals direkt in `.tmp-results` als Quelle beginnen; stattdessen in `todo.root.md` pflegen und anschließend die temporären Dateien aktualisieren.
- Pflege (Doku-Update=true): Aktualisierung der temporären Dateien erfolgt bei relevanten Änderungen an `todo.root.md` oder nach Sprint-Planungen. Frontmatter (`stand/update/checks`) in `.tmp-results/*.md` pflegen; Markdownlint/Frontmatter-Validator ausführen und Status notieren.
- Lebenszyklus: `.tmp-results` ist flüchtig (kein langfristiges Archiv). Inhalte können ohne Vorwarnung rotiert/ersetzt werden; keine sensiblen Daten ablegen.

### Diagnose-Playbook bei Lint-FAIL (pwsh, konservativ)
- Ziel: Lint-Fehler reproduzierbar erfassen, schnell auswerten und mit minimalem Risiko beheben.
- Ausführung (repo-weit, Konfiguration aus Root):
- Bestehendes Terminal (PowerShell 7, Profil aktiviert) verwenden.
- Vollständige Ausgabe in Datei sichern:
- Beispiel: `npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc '**/*.md' 2>&1 | Tee-Object -FilePath lint_fail.out`
- Analyse (PowerShell-only, Python via Here-String in `python -` pipen):
- Hintergrund: Kein Bash, keine Backticks; UTF-8 sicher; kein Multi-Line `python -c`.
- Muster (Interpreter anpassen, z. B. auf Workspace-Venv):

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

### Typische Befunde und Fixes
- MD012/no-multiple-blank-lines: Doppelte Leerzeilen entfernen (konservativ, nur überzählige Leerzeilen).
- MD047/single-trailing-newline: Fehlende Abschluss-Zeile am Dateiende hinzufügen (genau eine).
#### Akzeptanzchecks
   - Nach Fix: optional enger Bereich erneut mit obigem npx-Aufruf prüfen.
   - Voller Lauf mit `'**/*.md'` kann weiterhin FAIL sein, bis alle betroffenen Dateien bereinigt sind.
   - Ergebnisse kurz protokollieren (PASS/FAIL, ggf. Pfad zur Ausgabe z. B. `lint_fail.out`).

#### Mirrors/Redirect-Stubs
 - Unter `novapolis-rp/Main/novapolis-dev/docs/` liegen nur noch Redirect-Stubs; Single Source of Truth ist `novapolis-dev/docs/**`.
 - Änderungen an Arbeitsregeln/Dokumentation ausschließlich in den Live-Quellen vornehmen; Stubs nicht bearbeiten.

### Export/Importer
 - Export: `coding/tools/chat-exporter/` (Auto-Scroll, Inaktivitäts-Stop, speicherschonend).
 - Ingest: `coding/tools/curation/ingest_jsonl.py` (streamend, chunked, sanftes Cleaning).
 
Ziele
---
 - Stabiles Gedächtnis (Admin: system-prompt/memory-bundle) und reibungsloser Szenenstart.
 - Reproduzierbare, nachvollziehbare Schritte (Dokumentation & kleine Commits).
 
Hinweis (Terminal/Pwsh)
---
### Standard ist PowerShell 7 (`pwsh`) mit aktivem Profil.
 Direkte Eingaben erfolgen in der laufenden Session (kein erneutes `pwsh` nötig). Für komplexe oder mehrzeilige Abläufe (Coverage, Artefakt-Erzeugung, umfangreiche Prüf-Sequenzen) Skript-Wrapper nutzen: `pwsh -File <script.ps1>`. Inline `pwsh -Command "..."` ist ausschließlich für echte Einzeiler oder externe Launcher (CI/Task) zulässig. Kein zusammengesetztes Mehrzeilen-Here-String über `-Command`; stattdessen Skript anlegen. Achte auf sauberes Quoting (`${workspaceFolder}`, `Join-Path`).
#### Ausnahme (Systemzeit)
 Einfache Ausgabe direkt: `Get-Date -Format 'yyyy-MM-dd HH:mm'`.

Postflight: STOP-Gate dedupliziert, Modell-Profile konsolidiert, Prüfabläufe und Module korrekt gerelevelt, Markdownlint-Sektion vereinheitlicht, Meta-Block harmonisiert, Heading-Interpunktion und -Einzug bereinigt, Whitespace normalisiert; Lint-Ziele MD001/MD003/MD007/MD009/MD012/MD023/MD025/MD031/MD032/MD047 erfüllt.
