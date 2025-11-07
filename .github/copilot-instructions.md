Copilot-Projektanweisungen (Novapolis Suite)
============================================

Stand: 2025-11-07 02:51 – H1/H2 auf Setext umgestellt (MD003).
Hinweis: Single‑Root, pwsh 7, Godot Option A aktiv (kanonisch: `novapolis-sim/project.godot`)

<!-- markdownlint-disable MD022 MD032 MD036 -->

> Hinweis (Terminal/Pwsh): Standard ist jetzt PowerShell 7 (`pwsh`). Bei allen manuellen Aufrufen `-NoProfile` verwenden, um Störungen durch Profilskripte zu vermeiden. Tasks verwenden wieder `-Command`; achte auf sauberes Quoting (`${workspaceFolder}`, `Join-Path`), damit Leerzeichen in Pfaden keine Fehler auslösen.
> Ausnahme (Systemzeit): Für einfache, pfadfreie Einzeiler ist `-Command` erlaubt und kanonisch. Systemzeit immer so ermitteln: `pwsh -NoProfile -Command "Get-Date -Format 'yyyy-MM-dd HH:mm'"`.
>
> Hinweis (STOP): „Grün“ gilt nur bis zur nächsten Abweichung/Unsicherheit – dann STOP, Rückfrage, weiter nach Freigabe.

Primäre Behaviour-Quellen
-------------------------

- `novapolis_agent/docs/AGENT_BEHAVIOR.md`: maßgeblicher System-Prompt, Sicherheitsrichtlinien, Arbeitsablauf.
- `novapolis-dev/docs/copilot-behavior.md`: redigierte Kopie für den Dokumentations-Hub; folgt denselben Regeln.
- `novapolis-rp/database-rp/00-admin/AI-Behavior-Mapping.{md,json}`: Rollenspiel-spezifische Verhaltenshooks und Rollenmatrix.
- `novapolis-rp/development/docs/` enthielt Legacy-Stubs und wurde entfernt (2025-11-05). Verwende ausschließlich die oben genannten Live‑Quellen im Dev‑Hub.

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

### Tippfehler-/Benennungshygiene

- Proaktiv auf offensichtliche Tippfehler und inkonsistente Benennungen hinweisen (z. B. „archiv“ → „archive“ bei Ordnernamen/Dateien).
- Bei Korrekturen mit Minimal‑Delta vorgehen: Redirects/Stubs belassen bis alle Verweise umverdrahtet sind, dann aufräumen.
- Vor dem Entfernen von Redirect-/Mirror‑Stubs eingehende Links per Suche prüfen und erst danach löschen.

### Copilot vs. Mensch (Verantwortungsmatrix)

- Copilot: dokumentiert PASS/FAIL-Ergebnisse und aktualisiert `checks` nach realen Läufen.
- Copilot: pflegt Task-Definitionen und fordert bei fehlenden Tasks Freigabe ein.
- Mensch: nutzt das User-Terminal für ad-hoc Shell-Kommandos und Explorationsläufe.
- Mensch: bestätigt Moduswechsel (STOP‑Gate) und gibt neue Tasks oder Anpassungen frei.
- Mensch: sorgt dafür, dass das User-Terminal frei ist, wenn Copilot Tasks starten soll.

### Kanonische Tasks (Referenz)

- Checks: *lint+pytest* (Task ruft zuerst `Lint: markdownlint-cli2 (all md)` und danach `Tests: pytest (-q)` sequenziell auf).
- Git: *commit+push* (Commit-Message per Prompt, dann Push).
- Lint: *markdownlint-cli2 (all md)*.
- Hinweis: Labels müssen exakt den Einträgen in `.vscode/tasks.json` entsprechen; bei Abweichung **nicht starten**, sondern Rückfrage.
- Gates können jederzeit durch die Formulierung „STOP‑Gate aus (Session)“ deaktivieren und mit „STOP‑Gate an“ wieder aktivieren.

Zusatz (pwsh):
- Für Tasks mit Python-Nutzung wird per `-Command` direkt der Interpreter aus `.venv` (Fallback `python`) aufgerufen; CWD/Coverage-Pfade sind im Task hinterlegt.
- Bei Pfaden mit Leerzeichen bitte `${workspaceFolder}` und `Join-Path` verwenden.

### Update-Logistik

- Timestamp: Änderungen mit `YYYY-MM-DD HH:mm` (lokale Zeit) vermerken – gilt für Kopfzeilen („Stand“, „Letzte Aktualisierung“), DONELOG-Einträge und kurze Statusnotizen.
- Systemzeit (kanonisch): `pwsh -NoProfile -Command "Get-Date -Format 'yyyy-MM-dd HH:mm'"`.
- Kurznotiz: 1–2 Sätze oder Bullet, was angepasst wurde (analog zu `novapolis-rp/database-rp/02-*`). Bei komplexeren Tasks optional Primärpfad referenzieren (`app/...`, `scripts/...`).
- Prüfungen: Relevante Checks nennen (z. B. `pytest -q`, `pyright`, `markdownlint-cli2`) inkl. Ergebnis/Exit-Status; bei Bedarf Link/Dateipfad zur Ausgabe ergänzen.
- Markdownlint-Läufe protokollieren: Lauf/Command + PASS/FAIL direkt nach dem Lauf im Status erwähnen.

#### Workspace‑Tree‑Artefakte (Zuordnung)

- „Workspace tree: full“ → `workspace_tree_full.txt`
- „Workspace tree: directories“ → `workspace_tree.txt`
- „Workspace tree: summary (dirs)“ → `workspace_tree_dirs.txt`
- Dokumentpflege: Betroffene Artefakte synchron halten (Root: `todo.root.md`, `DONELOG.md`; Agent: `novapolis_agent/docs/DONELOG.txt`; Dev‑Hub: `novapolis-dev/docs/todo.*.md`, `novapolis-dev/docs/donelog.md`; außerdem `WORKSPACE_INDEX.md`, `WORKSPACE_STATUS.md`, README/Index-Seiten). Strukturänderungen → zusätzlich Tree-Snapshots aktualisieren; Behaviour-Änderungen → `AGENT_BEHAVIOR.md` & Kopien prüfen.
- Referenzen: Wenn vorhanden Issue-/PR-Links, Commit-Hash oder Kontextnotizen angeben (Inline oder als Fußnote). Für wiederkehrende Schritte Templates/Tasks im Root `.vscode/` ergänzen.
- Nicht-triviale Änderungen → in zugehörige TODO oder DONELOG.

#### YAML-Frontmatter (kompakt & LLM-freundlich)

- Ab sofort bevorzugt jede Datei mit Snapshot-Kopfzeile eine YAML-Frontmatter am Dokumentanfang.
- Übergangsphase: Legacy-Kopfzeilen mit `Stand:`/`Letzte Aktualisierung:` bleiben gültig; neue Änderungen bevorzugt als YAML einpflegen. Mischbetrieb kurzfristig erlaubt; Ziel ist vollständige Migration.
- Empfohlene Schlüssel (kurz und stabil):
  - `stand`: `YYYY-MM-DD HH:mm` (lokale Zeit)
  - `update`: 1–2 Stichpunkte zur Änderung
  - `checks`: kurz zu den relevanten Prüfungen/Ergebnissen (z. B. „pytest -q PASS“)
  - Optional: `refs` (Issue/PR/Commit), `affected` (betroffene Dateien/Pfade)

Beispiel:

```markdown
---
stand: 2025-11-01 09:05
update: Task „DONELOG: append entry“ ergänzt.
checks: keine
---
```

- Hinweise:
 - Tokens sparsam halten (kurze Schlüssel, 1–2 Stichpunkte).
 - Bei jedem Schreibvorgang Frontmatter-Zeitstempel und `update`/`checks` aktualisieren.
 - Für Tools/Parsing ist YAML robuster als Freitext-Kopfzeilen.
 - Ausnahme: Für dieses Dokument (`.github/copilot-instructions.md`) keine YAML-Frontmatter verwenden (Parser-Einschränkung). Snapshot hier weiterhin per `Stand:`-Zeile pflegen.
 - Fallback (allgemein): Wenn YAML-Frontmatter technisch nicht einsetzbar ist (Parser/Format-Einschränkung), nutze am Dokumentanfang eine kompakte Kopfzeile im Klartext:
  - Erste Zeile: `Stand: YYYY-MM-DD HH:mm – <Kurznotiz>`
  - Optional darunter: `Checks: <kurz>`
  - Beispiel:
    - `Stand: 2025-11-01 09:28 – Abschnitt X präzisiert.`
    - `Checks: pytest -q PASS`

### STOP‑Gate (beidseitig, vor Modus‑relevanten Aktionen)

- Vor potenziell modus‑relevanten Aktionen – code‑schwer (z. B. Dateiedits unter Codepfaden, Skript-/Validator‑Neubau, Test-/Typecheck‑Runs, API/Service‑Änderungen) ODER redaktionell/kanon‑kritisch (z. B. Behaviour-/Policy‑Dokumente, Kanon-/SSOT‑Änderungen) – wird ein hartes STOP‑Gate gesetzt.
- Ablauf:
  1) Ausgabe „STOP: Moduswechsel empfohlen. Bitte Modus wählen.“
  2) Warten auf explizite Bestätigung:
     - „Wechsel: Modus Codex“ → sofort auf Codex wechseln und fortfahren.
     - „Wechsel: Modus General“ → sofort auf General wechseln und fortfahren.
     - „Weiter: aktueller Modus“ → ohne Moduswechsel fortfahren.
  3) Ohne Bestätigung keine auslösenden Aktionen starten.
- Hinweise:
  - Das STOP‑Gate gilt beidseitig (Code ↔ Redaktion). Reine triviale Konversationen sind nicht betroffen.
  - Während STOP gilt „Debug/Analyse vor Ausführung“: Keine neuen Build/Test/Run‑Tasks automatisch starten. Laufende Task‑Wünsche werden in eine interne Queue gelegt und erst nach Freigabe gestartet.
  - Test‑Ergebnis‑Heuristik (Plausibilität): Wenn ein vollständiger Testlauf quasi sofort (< 1 s) mit PASS zurückkommt, ist das verdächtig (möglicher Fehlaufruf/Scope‑Fehler). In diesem Fall Tests manuell im Terminal mit gesetztem cwd ausführen und die Laufzeit/Ergebnisse im Log vermerken.
  - Manuell‑ausführen‑Pflicht (kritische Läufe): Bei Coverage‑Gates oder Fehlersuche im Terminal mit gesetztem cwd=`novapolis_agent` arbeiten und Befehle mit `Join-Path` sauber quoten.

### Unklarheiten‑STOP (global, immer gültig)

- „Grün“ gilt nur bis zum nächsten unerwarteten Ereignis. Sobald etwas außerhalb des Plans liegt, sofort STOP – unabhängig vom aktiven Modus.
- Unerwartet = mindestens eins davon:
  - Abweichung vom Plan/Ergebnis oder Modul‑Erwartung
  - Widerspruch (Quellen/Regeln/Invarianten/SSOT)
  - Unsicherheit über Bedeutung/Wirkung/Reichweite
  - Sicherheits-/Privacy‑Bedenken
  - Falscher/unklarer Modus (General ↔ Codex)
- Ausnahmen (kein STOP): Bereiche, die explizit als „RAW“, „noisy“ oder „staging/experimentell“ gekennzeichnet sind.
- Vorgehen bei STOP:
  1) Kurzstatus: Was ist abweichend/unklar (1–2 Sätze)?
  2) 1–2 Vorschläge (inkl. „keine Aktion“) zur Auswahl darlegen.
  3) Auf Freigabe warten – keine Folgeaktionen bis Bestätigung.
- Priorität: Dieses STOP hat Vorrang vor dem Moduswechsel‑Gate. Falls eine Lösung Code erfordert, danach Moduswechsel vorschlagen und bestätigen lassen.

### Modell-Profile & Moduswechsel (GPT‑5 ↔ GPT‑5 Codex)

- Kurzdefinition: General = redaktionelle/Analyse‑Arbeiten; Codex = Code/Tests/Build‑/CI‑Arbeiten.
- Standardmodus: GPT‑5 (General) für redaktionelle Arbeiten, Kanon-/Quellenabgleich, `[FACT]`↔`[FACT?]`‑Revalidierung, Policy-/Prozess‑Checks und Textkurierung.
- Codex-Modus (umschalten bei Bedarf): Für Code‑schwere Aufgaben wie Skripte/Validatoren, Tests/CI, API‑/Service‑Änderungen, Parser/RegEx, Datentransformationen.
- Heuristische Trigger für Wechselvorschlag (nicht automatisch, nur Hinweis):
  - Edits in Quellcodepfaden: `novapolis_agent/app/**`, `novapolis_agent/scripts/**`, `novapolis_agent/utils/**`, `novapolis_agent/tests/**`, `packages/**`, `novapolis-rp/coding/**`.
  - Anforderung: „Bitte Skript/Validator/Test bauen“, „API anpassen“, „Pytest/Typing fixen“.
  - Geplante Ausführung technischer Tasks: Pytest/Mypy/Pyright, Linter-/Build‑Themen.
- Erinnerung/Prompting‑Policy:
  - Wenn aktueller Modus = GPT‑5 und ein Trigger erkannt wird: „Hinweis: Moduswechsel zu Codex empfohlen für Code‑schwere Aufgaben. Bitte bestätigen.“
  - Wenn aktueller Modus = Codex und redaktionelle Arbeit erkannt wird: „Hinweis: Moduswechsel zu General empfohlen für redaktionelle Aufgaben. Bitte bestätigen.“
  - Nutzerentscheid respektieren; bei „nein“ weiter im aktuellen Modus arbeiten. Auf Wunsch „Bitte nicht erinnern“ stelle ich Erinnerungen ein, bis du wieder grünes Licht gibst.
  - Explizite Nutzerwahl überschreibt Heuristik: „Modus Codex“/„Modus General“ setzt sofort um.
  - Transparenz: Den aktiven Modus im nächsten Status‑Update kurz erwähnen (z. B. „Modus: General“), wenn ein Wechsel stattfand oder Code‑Arbeit ansteht.

### Betriebsmodi (Standardlauf & Sicherheitsprotokoll)

- **Standardlauf:** Default nach Freigabe eines STOP‑Gates. Vor jedem Task einen Expected-State-Block festhalten (Ziel, Nicht-Ziele, Invarianten, Scope, Budgets, Akzeptanzchecks, Risiken) und reguläre Dokumentationspflichten erfüllen.
– **Sicherheitsprotokoll:** Aktiv bei STOP-Auslösern, Drift außerhalb Budgets oder manueller Anforderung. In Paketen zu 3–5 Operationen arbeiten, nach jedem Paket IST/SOLL abgleichen und Driftbewertung melden.
– **Expected State & Logging:** Vorlage siehe `novapolis-dev/docs/process/betriebsmodi-sicherheitsprotokoll-notizen.md`. Rohlogs lokal in `novapolis-dev/logs/betriebsmodi-*.tmp.md` führen, verdichtete Zusammenfassungen optional committen (Vorlage `novapolis-dev/logs/log-template.md`).
– **Ausstieg:** Sicherheitsprotokoll erst verlassen, wenn Ursache behoben ist und zwei Pakete ohne neue Drift außerhalb Budgets verlaufen oder der Nutzer explizit freigibt. Abschlussbericht (Befund, Checks, Rest-Risiken) bereitstellen.

Repositoryweiter Rahmen
-----------------------
- Gemeinsamer Code gehört nach `packages/novapolis_common`; doppelte Module aus den Teilprojekten nach Migration entfernen.
- Konfigurationen bleiben projektspezifisch; Produktions- und API-Code verbleibt im jeweiligen Projektordner, Utilities werden über das Shared-Package re-exportiert.
- Doppelte Modulpfade (z. B. parallele `novapolis_agent/novapolis_agent/**` und `novapolis_agent/app/**`) sind als Legacy zu behandeln; Neu‑Anpassungen bitte nur unter den aktiven Pfaden vornehmen (siehe `novapolis_agent/WORKSPACE_INDEX.md`).
- Secrets (`.env`) bleiben lokal; ungefilterte Exporte ausschließlich unter `novapolis-rp/database-raw/99-exports/` ablegen.
- Working docs leben in `novapolis-dev/docs/` (todo, donelog, tests, naming-policy, copilot-behavior, index); `novapolis-rp/development/...` sind Redirect-Stubs.
 - Backups/Altstände gehören zentral nach `Backups/` (keine tool‑lesbaren Backups neben aktiven Configs).
 - Godot (Sim): Kanonische Projektdatei ist `novapolis-sim/project.godot` (Option A). Das frühere, verschachtelte Projekt wurde nach `Backups/novapolis-sim-archived-20251104/` verschoben.

Prüf- und Release-Checks
------------------------
- Vor Commits relevante Tests/Skripte ausführen (Root‑basiert): `novapolis_agent/scripts/run_tests.py` (cwd=`novapolis_agent`), Validatoren unter `novapolis-rp/coding/tools/validators/`.
- Bei Änderungen an Behaviour-/Policy‑Dokumenten zusätzlich den Test `novapolis_agent/tests/test_content_policy_profiles.py` laufen lassen und Changelogs prüfen. Diese Regel ist im Single‑Root‑TODO verlinkt.
- Bei Unsicherheiten/Unklarheiten: STOP‑Gate setzen (Rückfrage einholen), dann mit Minimal‑Delta fortfahren; transparente Diffs mit Dateiliste/Diffstat, keine Shell‑Kommandos oder History‑Rewrites.

Hinweis (CI‑Workflows): Nur Workflows unter `.github/workflows/` am Repo‑Root sind wirksam. Kopien/Spiegel in Unterordnern (z. B. `novapolis_agent/.github/workflows/`) gelten als Stubs/Archiv und werden von GitHub Actions nicht ausgeführt. Cleanup als eigener Task vorschlagen (vorher eingehende Verweise prüfen).

Novapolis Agent (Backend)
-------------------------

### Arbeitskontext
- Repo: `novapolis_agent` (Branch `main`), Stack: FastAPI + Ollama, Kern: `app/main.py`, `app/api/models.py`, `app/core/settings.py`, `app/core/prompts.py`.

### Schnellziele bei Codeänderungen
- CI grün halten: Tests (`pytest`), Typen (Pyright/Mypy). CI prüft `docs/DONELOG.txt`.

- Nach jedem Edit Tests/Typen sequentiell ausführen und Ergebnisse abwarten (`pytest -q` → `pyright -p pyrightconfig.json` → `python -m mypy --config-file mypy.ini app scripts`). Keine Vorab-Statusmeldungen.

### PR-/Push-Checks
- Tests lokal: `pytest -q` oder passende Marker.
- Typechecks: `pyright -p pyrightconfig.json`, `python -m mypy --config-file mypy.ini app scripts`; optional Task „Tests: coverage (fail-under 80%)“.
- Änderungen an `app/`, `scripts/`, `utils/` → DONELOG-Update (Push auf main erfordert Eintrag; PR-Befreiung via Label `skip-donelog`).

### Pytest-Marker & Selektiver Lauf
- Unit: `pytest -q -m unit`.
- API/Streaming: `pytest -q -m "api or streaming"`.
- Selektiv: `pytest -q -k test_rate_limit_headers_on_success`.

### API & Integration
- Endpunkte: `/`, `/health`, `/version`, `POST /chat`, `POST /chat/stream` (SSE).
- Prompts zentral in `app/core/prompts.py`; Kontext-Notizen via ENV `CONTEXT_NOTES_ENABLED=true`, Pfade in Settings.
- Synonyme: Basis `eval/config/synonyms.json`, Overlay `eval/config/synonyms.local.json` (optional, Merge).

### Konventionen
- Modelle ausschließlich über `app/api/models.py` importieren (nicht `app/schemas.py`).
- Middleware setzt `X-Request-ID` auch bei Fehlern; HTTPException-Header werden gemergt.
- Rate-Limit per ENV; Tests nutzen `monkeypatch.setenv(...)` und Module-Reload.

### Häufige Fehlerquellen
- Streaming/SSE: Generator liefert Events; Tests erwarten `event: meta` mit `"policy_post"`, `event: delta` mit `"text"`, `event: done`.
- Rate-Limit-Header: Bei Erfolg `X-RateLimit-{Limit,Remaining,Window}`, bei 429 zusätzlich `Retry-After`.
- CORS-ENV `BACKEND_CORS_ORIGINS` akzeptiert JSON-Liste oder Komma-Liste (Validator in `settings`).

### Workflows & Artefakte
- Lokal starten: `uvicorn app.main:app --reload` (Swagger `/docs`).
- Finetune-Export/Prepare: Tasks „Finetune: export (latest)“ → `scripts/export_finetune.py`, „Finetune: prepare (split)“ → `scripts/prepare_finetune_pack.py` (Outputs `eval/results/finetune/`).

### Nachschlagen & Meta
- CI/Workflows: `.github/workflows/ci.yml`, `.github/workflows/enforce-donelog.yml`.
- Tests siehe `tests/` (u. a. `test_app_*` für Health/Request-ID/Rate-Limit; Streaming-/Policy-Tests definieren Format).
- Skripte: `scripts/` (Eval/Export/Train/Reports) – vorhandene CLI-Optionen nutzen.
- Beim Aktualisieren dieser Datei Hinweise aus `docs/AGENT_BEHAVIOR.md` beachten (Progress-Cadence, DONELOG, Shell-Hinweise); nach Änderungen Checks abwarten. Manuelle Reihenfolge für Vollprüfungen: erst `pytest -q`, dann `pyright -p pyrightconfig.json`, danach `python -m mypy --config-file mypy.ini app scripts`.
- Feedbackbedarf (Marker, Tasks, Troubleshooting) kurz melden.

Novapolis-RP
------------

### Working Rules (Novapolis)
- SSOT: **/Main/novapolis-dev/**.
- Minimal und transparent: Diffs klein halten, betroffene Dateien und Diffstat nennen.
- Keine Shell-Kommandos, keine History-Rewrites.
- Working Docs liegen in `novapolis-dev/docs/` (todo, donelog, tests, naming-policy, copilot-behavior, index).
- `novapolis-rp/development/...` sind Redirect-Stubs – nicht hineinschreiben.
- Vor APPLY nach verbliebenen `development/docs`-Referenzen suchen (nur in Redirect-README und `meta.origin` erlaubt).
- Nach APPLY sicherstellen, dass verschobene Docs Sidecars mit `source`, `origin`, `migrated_at` besitzen.

### Workspace-Instructions (kompakt)

**Primärer Kontext**
- `novapolis-dev/docs/copilot-behavior.md` – Arbeitsweise, Stil, Sicherheit.
- `novapolis-dev/docs/index.md` – Navigation & Prozessreferenz.
- `novapolis-rp/database-raw/99-exports/README.md` – RAW-Policy (keine ungefilterten Daten nach `database-rp/`).

**Wichtige Regeln**
- Sprache: Deutsch (Erklärungen, Beispiele, Fehlermeldungen).
- RAW-Only: Ungefilterte Exporte ausschließlich unter `database-raw/99-exports/` speichern.
- Curation-Flow: Für RP-Nutzung stets Ingest/Curation verwenden (`coding/tools/curation/`).
- Minimal-Delta: Änderungen klein halten; `novapolis-dev/docs/donelog.md` pflegen.
- Sicherheit & Privacy: Keine Secrets; offline bevorzugen.

**Antworten & Format**
- Prägnant, skimmbar; kurze Sätze, Bullet-Listen ok, keine überladenen Blockzitate.
- Bei Codeänderungen minimaler Patch mit kurzer Begründung und Prüfung.
- Bei größeren Aufgaben ToDo-Liste (Plan) sichtbar führen und aktualisieren.

### Markdownlint (zentral)

  - MD003 = `setext_with_atx` (H1/H2 im Setext‑Stil, H3+ im ATX‑Stil; je Level konsistent innerhalb der Datei). Keine gemischten Stile für dasselbe Level in einer Datei.
  - `ignores` in der CLI2‑Config decken generierte/kuratierte Bereiche ab (u. a. `novapolis_agent/eval/results/**`, `novapolis_agent/outputs/**`, `outputs/**`, `novapolis-rp/.pytest_cache/**`).
- Lokaler Lauf (nur im bestehenden Terminal, unter pwsh -NoProfile): `npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc "**/*.md"`.
  - Wrapper/Tasks: Nicht benötigt; Lint läuft direkt via Task (Exit‑Code wird durchgereicht).
- Auto‑Fix optional: `npx --yes markdownlint-cli2-fix --config .markdownlint-cli2.jsonc "**/*.md"`.

Optionaler Zusatz: „Lint: markdownlint-cli2 (docs focused)“ kann für einen schnellen Dokumentations‑Lint genutzt werden (`novapolis-dev/docs/**`, `novapolis_agent/docs/**`).

#### Diagnose‑Playbook bei Lint‑FAIL (pwsh, konservativ)

Ziel: Lint‑Fehler reproduzierbar erfassen, schnell auswerten und mit minimalem Risiko beheben.

- Ausführung (repo‑weit, Konfiguration aus Root):
  - Bestehendes Terminal (PowerShell 7, `-NoProfile`) verwenden.
  - Vollständige Ausgabe in Datei sichern:
    - Beispiel: `npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc "**/*.md" 2>&1 | Tee-Object -FilePath lint_fail.out`
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
  - Nach Fix: „Lint: markdownlint-cli2 (docs focused)“ optional zur schnellen Verifikation.
  - Voller Lauf „Lint: markdownlint-cli2 (all md)“ kann weiterhin FAIL sein, bis alle betroffenen Dateien bereinigt sind.
  - Ergebnisse kurz protokollieren (PASS/FAIL, ggf. Pfad zur Ausgabe z. B. `lint_fail.out`).

### Mirrors/Redirect‑Stubs

- Unter `novapolis-rp/Main/novapolis-dev/docs/` liegen nur noch Redirect‑Stubs; Single Source of Truth ist `novapolis-dev/docs/**`.
- Änderungen an Arbeitsregeln/Dokumentation ausschließlich in den Live‑Quellen vornehmen; Stubs nicht bearbeiten.

**Export/Importer**
- Export: `coding/tools/chat-exporter/` (Auto-Scroll, Inaktivitäts-Stop, speicherschonend).
- Ingest: `coding/tools/curation/ingest_jsonl.py` (streamend, chunked, sanftes Cleaning).

**Ziele**
- Stabiles Gedächtnis (Admin: system-prompt/memory-bundle) und reibungsloser Szenenstart.
- Reproduzierbare, nachvollziehbare Schritte (Dokumentation & kleine Commits).

