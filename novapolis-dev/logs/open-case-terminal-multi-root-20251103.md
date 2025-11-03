---
stand: 2025-11-03 04:23
update: Status-Notiz ergänzt: letztes Commit+Push vor VS Code Neustart; Case bleibt bis Mono-Workspace-Umstellung geschlossen (Hint).
checks: keine (STOP – keine automatisierten Läufe)

Open Case: VS Code Multi-Root & unzuverlässige Tasks/Terminal
=============================================================

Kurz: VS Code markiert den Workspace aktuell als Multi-Root. Wrapper-Tasks verhalten sich inkonsistent (z. B. Snapshot-Task Quoting-Fail), während manuelle Terminalläufe funktionieren. Bis zur Bereinigung gilt: KEINE WRAPPER, Terminal nur manuell.

Zusammenfassung
---------------

- Symptome:
  - Snapshot-Task lief einmal mit Quote-Konflikt fehl (Exit 1), manuell mit doppelten Quotes ok.
  - Tests über Task: PASS; manuell: PASS. Coverage manuell: FAIL (Total ≈66% < 80%).
  - Workspace wird als Multi-Root erkannt → Tasks/Wrapper teils mit falschem Kontext.
- Impact:
  - Potenzielle False-Positives oder -Negatives bei automatisierten Tasks.
  - Zeitverlust und Verunsicherung bei Diagnose.
- Status: Offener Fall (Sicherheitsprotokoll aktiv). Evidenz unten verlinkt.

Status-Update (2025-11-03 04:23)
--------------------------------

- Letzte durchgeführte Aktion im Zusammenhang mit diesem Fall: finales Committen und Pushen der Dateien im Workspace, im Zuge eines Neustarts von VS Code, um keinen korrupten Kontext mitzuschleppen.
- Anschließend wurde die Sitzung neugestartet. Der Case bleibt bis zur Umstellung auf „Mono-Workspace“ geschlossen und dient nur als Hinweis (Hint).

Evidenz
-------

- TMP-Log: `novapolis-dev/logs/betriebsmodi-20251103-0341.tmp.md`
- Screenshots (Ablage):
  - `novapolis-dev/logs/screenshots/Screenshot 2025-11-03 033435.png`
  - `novapolis-dev/logs/screenshots/Screenshot 2025-11-03 034248.png`
  - `novapolis-dev/logs/screenshots/Screenshot 2025-11-03 034642.png`
  - `novapolis-dev/logs/screenshots/Screenshot 2025-11-03 034741.png`
  - `novapolis-dev/logs/screenshots/Screenshot 2025-11-03 034851.png`

Reproduktion (beobachtet)
-------------------------

1) Snapshot (Task):
   - Befehl: `pwsh -NoProfile -Command 'Get-Date -Format 'yyyy-MM-dd HH:mm''` → FAIL (Exit 1, Quote-Konflikt)
   - Manuell: `pwsh -NoProfile -Command "Get-Date -Format 'yyyy-MM-dd HH:mm' | Write-Output"` → PASS
2) Tests (Task): `pytest -q` → PASS (Exit 0), cwd: `novapolis_agent`
3) Coverage (Task/Manuell): manuell mit `--cov --cov-branch --cov-fail-under=80` → FAIL; Total ≈66%

Analyse
-------

- Hauptursache: Multi-Root-Markierung führt zu instabilen Wrapper-Tasks (CWD/ENV/Quoting). Manuelle Läufe sind stabil.
- Sekundäre Beobachtung: Coverage-Gate scheitert vor allem wegen Lücken in 0%-Modulen (`app/api/api.py`, `app/core/mode.py`, `app/utils/convlog.py`) und hohem Anteil `scripts/**`.

Maßnahmen (sofort)
-------------------

- Policy bis zur Bereinigung: KEINE WRAPPER – Terminal ausschließlich manuell nutzen.
- STOP-Gate: Automatisierte Tasks in die Queue, manuell verifizieren (Heuristik: <1s PASS = verdächtig).

Maßnahmen (nächste Schritte)
----------------------------

- Workspace bereinigen → Single-Root sicherstellen; danach Wrapper reaktivieren.
- Optional kurzfristig für Stabilität:
  1) Snapshot-Task-Quoting auf doppelte Quotes vereinheitlichen (Dokumentation/Hinweis, kein Wrapper-Zwang).
  2) Coverage-Scope vorübergehend auf `app/**` beschränken (nur wenn notwendig, dokumentieren).
  3) 3 Minimaltests für 0%-Module (Import/Smoke), zielgerichtete 1–2 Tests für `app/api/chat.py`.

Anhang A: Auszug Rohlog (TMP)
-----------------------------

> Quelle: `novapolis-dev/logs/betriebsmodi-20251103-0341.tmp.md`

---

```markdown
---
stand: 2025-11-03 03:41
aufgabe: Daten sichern, Screenshot sichern+analysieren, Auswertung starten
modus: Sicherheitsprotokoll
checks: pytest -q PASS; snapshot task einmal FAIL, manueller timestamp OK
---

# Betriebsmodus-Log (Rohlog)

## Expected State

- Ziel: Zustand der letzten Sitzung nachvollziehbar sichern (Daten+Screenshot) und erste Auswertung beginnen.
- Nicht-Ziele: Keine Codeänderungen außerhalb der Log-Erstellung.
- Invarianten: Keine Build-/Test-Regressionen erzeugen; keine Binärdateien committen.
- Scope: `novapolis-dev/logs/**` (Markdown, Platzhalter), keine Codepfade.
- Budgets: ≤ 3 neue Dateien, ≤ 200 Zeilen.
- Akzeptanzchecks: (1) Rohlog angelegt, (2) Screenshot-Pfad dokumentiert, (3) Tests-Status protokolliert.
- Risiken/Abhängigkeiten: Screenshot aus Chat muss manuell ins Repo kopiert werden (Tool kann Anhang nicht extrahieren).

## Paket 1 (03:41)

Operationen:
- Pytest-Ergebnis und Terminalhistorie aus Kontext übernommen.
- TMP-Logdatei erstellt.
- Screenshot-Ablagepfad vorbereitet (siehe unten).

IST vs. SOLL:
- Tests: PASS (Exit Code 0) – erfüllt.
- Snapshot-Task: Ein Lauf FAIL (Quoting), manuell OK – dokumentiert; akzeptabel.

Driftbewertung:
- Diff-Drift: grün (kleine Dokuänderungen).
- Test-Drift: grün (PASS).
- Pfad-Drift: grün (nur `logs/`).
- Plan-Drift: grün.
- Zeit-Drift: grün.

Nächste Schritte:
- Screenshot-Datei in Pfad kopieren.
- Coverage-Task optional ausführen und Ergebnis anhängen.

## Artefakte & Pfade

- Screenshot (geplant): `novapolis-dev/logs/screenshots/20251103-0341-session.png`
  - Status: Bitte Screenshot aus Chat manuell dort ablegen; Datei wird nicht automatisch extrahiert.
- Terminal-Status:
  - Snapshot Task: ein Lauf FAIL mit `'Get-Date -Format 'yyyy-MM-dd HH:mm''` (Quote-Konflikt), manueller Lauf mit `"Get-Date -Format 'yyyy-MM-dd HH:mm'"` PASS.
  - Tests Task: `pytest -q` PASS (Exit Code 0), CWD `novapolis_agent`.
  - Coverage Task: `pytest --cov ... --cov-fail-under=80` PASS (Exit Code 0), Schwelle ≥ 80% erfüllt.

## Paket 2 (03:48)

Operationen:
- Pytests manuell im Terminal ausgeführt (cwd=`novapolis_agent`).
- Coverage manuell im Terminal ausgeführt.

Ergebnis:
- Pytest (manuell): PASS.
- Coverage (manuell): FAIL – Total 66% < fail-under 80%.

Auswertung (Kurz):
- Große Lücken in `app/api/api.py` (0%), `app/core/mode.py` (0%), `app/utils/convlog.py` (0%) und mehreren Scripts unter `scripts/`.
- Funktionale App-Pfade haben teils solide Werte (z. B. `app/core/settings.py` 94%, `app/main.py` 88%), aber `app/api/chat.py` liegt bei 55% und dominiert die Lücken.

Empfohlene 3 Sofort-Maßnahmen:
1) Coverage-Scope vorübergehend eingrenzen (nur `app/**`) via `.coveragerc` `omit`/`include`, um Skript-lastige Lücken nicht gating-wirksam zu machen.
2) Minimaltests für 0%-Module: Smoke/Import-Tests für `app/api/api.py`, `app/core/mode.py`, `app/utils/convlog.py` (heben Basis-Coverage schnell an).
3) Zielgerichtete Tests für Hotspots in `app/api/chat.py` (je 1–2 Cases für häufige Pfade), Rest in Modul-TODO aufnehmen.

Rest in TODO (ausgelagert):
- Langfristige Erhöhung der Coverage für `scripts/**` (separat tracken, nicht gating-relevant für App).

## Screenshot-Analyse (Vorschau)

- Editor: `novapolis-dev/docs/process/betriebsmodi-sicherheitsprotokoll-notizen.md` offen, Frontmatter `stand: 2025-11-03 03:20`.
- Terminal: Pytest-Ausgabe mit Punkten und einem `s` (zumindest 1 Skip), keine Fehler sichtbar.
- Chatfenster: Aufgabenliste zeigt Erstellung von 3 TODOs; Schritt „Testergebnis zusammenfassen“ in Arbeit; Hinweis auf Paketgröße ≤ 3 Aktionen im Sicherheitsprotokoll; Test-Task gestartet.
- Statusbar: Uhrzeit ~03:34, Sprache DEU, Terminal „Tests: pytest (-q)“ beendet.

## Offene Punkte

- Coverage laufen lassen und dokumentieren.
- Snapshot-Task robuster quoten (optional).
```


