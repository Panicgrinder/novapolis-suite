# PR: Archivierung von App-Stubs, Root-`app`-Shim und Formatierungsfixes

Kurz (Deutsch):
- Archiviert: Teile des `novapolis_agent/app`-Pakets in `novapolis_agent/archive/app/` verschoben; Live-Stubs durch klare Import-Fehlermarker ersetzt.
- Kompatibilität: Ein Root-`app/__init__.py`-Shim wurde hinzugefügt, damit Tests vom Repo-Root aus laufen (verhindert ImportError beim Root-CWD).
- Tests: Betroffene Tests aktualisiert; fokussierter Import-Test (`novapolis_agent/tests/test_module_exports.py`) und gesamte Test-Suite wurden erfolgreich ausgeführt.
- Formatierung: `ruff --fix` + `black` auf Repository angewendet; formattierte Dateien committed.
- Prüfstand: Voller Testlauf + Coverage report: Coverage insgesamt 80.0% (siehe `coverage report` output). Keine Test-Fails.

Details / Motivation (Kurz):
- Ziel: Repo aufräumen (geparkte/legacy-Module archivieren) ohne stille Regressionen; Tests sollen weiterhin aus Root CWD laufen.
- Vorgehen: Archiv statt löschen; ersetze live-Modul-Inhalte durch explizite Import-Fehler mit Hinweis auf das Archiv; passe Tests, die vorher still importiert hätten.
- Ergebnis: Sauberere Trennung, reproduzierbare Importe, Root-Shim stellt Abwärtskompatibilität für Root-CWD-Tests her.

Änderungen (high-level):
- Dateien/Ordner: `novapolis_agent/archive/app/...` (neue Archivkopien)
- Neue Datei: `app/__init__.py` (Repo-Root Shim)
- Tests aktualisiert: `novapolis_agent/tests/*` (mehrere)
- Style: diverse Dateien formatiert (ruff/black)

Nächste empfohlene Schritte:
1. (Optional) Kleine Unit-Tests hinzufügen für `scripts/run_eval.py` und `app/api/chat.py` um Coverage-Lücken zu schließen (ich kann das in 10er-Batches machen).
2. Lint-Remediation: verbleibende Ruff-Findings prüfen (`ruff check .`) und gezielt fixen.
3. Falls gewünscht: Erstelle den Pull Request auf GitHub (ich kann das Commit in einen Topic-Branch verschieben und PR-Text dort anlegen).

Commits in diesem PR:
- `a0167eb` — docs: document archival of app stubs + add root app shim (entries for DONELOG/WORKSPACE_INDEX/WORKSPACE_STATUS)
- `f25fcfc` — style: apply ruff/black formatting fixes

---
Bitte prüfen und sagen, ob ich den nächsten Schritt machen soll: (1) Branch & PR erstellen, (2) weitere Lint-Fixes, (3) Coverage-Targeting (10er-Batches), oder (4) nichts weiter.