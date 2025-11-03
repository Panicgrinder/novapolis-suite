stand: 2025-11-03 03:57
update: STOP-Regeln (Task-Queue), manuelle Testpflicht, <1s-PASS Heuristik
checks: keine
---

<!-- markdownlint-disable MD022 MD041 -->

# Betriebsmodi – Arbeitsnotizen

Dieses Dokument sammelt die Detailregeln für die Betriebsmodi "Standardlauf" und "Sicherheitsprotokoll". Es dient als Grundlage für die spätere Konsolidierung in den offiziellen Arbeitsanweisungen (`.github/copilot-instructions.md`, Modul-TODOs, README-Hinweise).

## Standardlauf (Baseline-Modus)

- **Zweck:** Normaler Arbeitsfluss ohne zusätzliche Einschränkungen. Fokus auf Effizienz bei gleichzeitiger Einhaltung der bestehenden STOP-Gates.
- **Aktivierung:** Default nach Freigabe eines STOP-Gates oder nachdem das Sicherheitsprotokoll (siehe unten) sauber abgeschlossen wurde.
- **Verpflichtungen:**
  - Erwartungszustand (siehe Abschnitt "Expected State") vor Taskbeginn festhalten.
  - STOP-Gates pro bestehender Regel anwenden (Moduswechsel, Unsicherheiten, Policies).
  - Ergebnisse und Prüfungen wie gewohnt dokumentieren (DONELOG, TODOs, Checks in Frontmatter).
- **Rückfall in Sicherheitsprotokoll:** Bei unerwarteten Abweichungen, Budget-/Test-/Pfad-Drifts oder manueller Anforderung.

## Sicherheitsprotokoll (Schutzmodus)

- **Zweck:** Eng getaktete Arbeitsschritte bei erhöhter Unsicherheit, um Drift schnell zu erkennen und Ursachen zu dokumentieren.
- **Aktivierung (automatisch oder manuell):**
  - STOP ausgelöst durch Abweichung, Fehler oder unerwartetes Verhalten (kein vollständiger Abbruch nötig).
  - Aufgaben mit explizitem "erhöhten Vorsicht"-Flag.
  - Wiederkehrende Drifts (Diff, Tests, Pfade, Plan, Zeit) außerhalb definierter Budgets.
  - Manuelle Entscheidung von Nutzer oder Copilot.
- **Arbeitsweise:**
  - Schritte in Paketen zu 3–5 wirksamen Operationen (zählen nur mutierende Aktionen oder Test-/Lint-Läufe).
  - Nach jedem Paket kurzer Abgleich IST vs. SOLL, Sammlung der Drift-Indikatoren.
  - Kontrollierte Schreibaktionen sind zulässig, müssen aber vorab angekündigt und unmittelbar überprüft werden.
  - Rohdaten-Log (`novapolis-dev/logs/`) je Sitzung mit Abschnitt pro Paket (siehe Abschnitt "Logging").
  - STOP-Priorisierung: Debug/Analyse vor Ausführung. Keine neuen Build-/Test-/Run-Tasks automatisch starten; Task-Anfragen werden in eine Queue gelegt und erst nach Freigabe gestartet.
  - Manuell-ausführen-Pflicht: Bei Coverage-Gates und Fehlersuche Tests manuell im Terminal (expliziter Interpreter, korrektes cwd) starten; Task-Runs nur ergänzend nutzen.
  - Test-Plausibilität: Kommt ein kompletter Testlauf „instant“ (< 1 s) mit PASS zurück, als verdächtig werten und unmittelbar manuell wiederholen; Ergebnis und Laufzeit im Log notieren.
- **Deaktivierung:**
  - Ursache identifiziert und mitigiert **und** zwei Pakete in Folge ohne Drift außerhalb der Budgets.
  - Alternativ manuelle Freigabe durch Nutzer.
  - Rückmeldung an Nutzer mit Kurzreport (Befund, durchgeführte Prüfungen, Rest-Risiken).

## Expected State (Soll-Beschreibung)

Vor jedem Task wird ein Expected-State-Block erstellt (Teil der TODO- oder Log-Notiz):

- **Ziel:** Ein Satz, was am Ende wahr sein muss.
- **Nicht-Ziele:** Aspekte, die explizit unberührt bleiben.
- **Invarianten:** Bedingungen, die unter keinen Umständen verletzt werden dürfen (z.\u00a0B. Tests grün, API-Signaturen stabil, Godot-Projekt startet).
- **Scope-Grenzen:** Pfade/Dateien, die geändert werden dürfen.
- **Budgets:** Grenzwerte für geänderte Dateien/Zeilen, Laufzeit-Anstieg, neue Warnungen.
- **Akzeptanzchecks:** 3–5 konkrete Prüfungen, die den Erfolg belegen.
- **Risiken/Abhängigkeiten:** Externe Faktoren oder bekannte Stolpersteine.

## Drift-Kategorien

Drift wird als Abweichung vom Expected State bewertet. Kategorien (Ampel, individuell gewichtbar):

1. **Diff-Drift:** Überschreitet das vereinbarte Diff-Budget (Dateien, Zeilen, Binärartefakte).
2. **Test-Drift:** Neue Fehler/Warnungen oder auffällig längere Laufzeiten.
3. **Pfad-Drift:** Änderungen außerhalb des definierten Scopes (hartes Rot).
4. **Plan-Drift:** Zusätzlich notwendige Schritte, die den ursprünglichen Plan verlassen.
5. **Zeit-Drift:** Paket sprengt die geplante Timebox.

Ampelbewertung:
- **Rot (harte Verletzung):** Sofort STOP und Ursachenanalyse (insbesondere Pfad-/Invariant-Drift).
- **Gelb (weiter im Protokoll):** Leichte Überschreitungen innerhalb der Budgets.
- **Gelb eskaliert:** Wiederholte Überschreitungen in zwei Paketen hintereinander.

## Logging & Ablage

- **Arbeitsverzeichnis:** `novapolis-dev/logs/` (ggf. neu anlegen, steht jetzt bereit). Datei je Sitzung, z. B. `betriebsmodi-20251103-0256.tmp.md`.
- **Vorlage:** `novapolis-dev/logs/log-template.md` enthält Frontmatter, Expected-State-Block und Paketstruktur.
- **README:** `novapolis-dev/logs/README.md` dokumentiert Benennung, Rotation und Mindestinhalte.
- **Format je Abschnitt:**
  - Frontmatter: `stand`, `aufgabe`, `modus`, `checks`.
  - Pro Paket: Zeitstempel, Operationen, IST, SOLL, Drift, Maßnahmen, nächste Schritte.
- **Rotation:** Letzte fünf Rohlogs behalten, ältere komprimieren oder entfernen. Kürzere Zusammenfassungen dürfen ins Repo committed werden.
- **CI-Sicherheit:** Keine Skripte/Tasks in `novapolis-dev/logs/`, um CI nicht zu beeinträchtigen.

## Modul-spezifische Expected-State-Stichpunkte

- **Agent (Python):** Tests grün, API-Signaturen unverändert, Scope auf `novapolis_agent/**`, Budget ≤ 5 Dateien/≤ 200 Zeilen, Checks = relevanter Pytest-Subset + Lint + Dev-Server-Dry-Run.
- **RP (Daten/Regeln):** Schema konsistent, Referenzen gültig, Scope auf betroffene Dateninsel, Budget = begrenzte Datensätze, Checks = Schema-Validator, Link-Checker, Diff-Stat.
- **Sim (Godot):** Projekt lädt ohne neue Warnungen, Scope auf betroffene Szene/Skript, Budget = limitierte Ressourcen keine unnötigen Binärdateien, Checks = Headless-Load, Log ohne Warnungen.
- **Root/Workflows:** Actions laufen grün, Pfadfilter korrekt, Scope auf `.github/workflows/**`, Budget = eine Datei pro Schritt, Checks = Workflow-Lint und optionaler Dry-Run.

## Offene Punkte

- Abstimmung, ob Rotationsregeln automatisiert werden sollen (Skript oder manueller Leitfaden).
