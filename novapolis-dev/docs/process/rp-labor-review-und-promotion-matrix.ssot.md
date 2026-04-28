---
stand: 2026-04-28 05:46
update: Diese SSOT behandelt jetzt auch `mind/` als feste Runtime-Typflaeche in Review und Promotion des RP-Laborpfads.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp/results/reports/checks_report_20260428_052348.md; snapshot-lock PASS (2026-04-28 05:46)
---

RP Labor Review- und Promotion-Matrix
=====================================

Zweck
-----

Diese SSOT verhindert, dass beim RP-Bespielen im Chat mehrere Zeitlinien still in die Hauptwelt rueberlaufen.

- Der laufende Hauptweltpfad bleibt eindeutig lesbar.
- Laborzuege duerfen weiter Daten erzeugen, aber nicht ohne Review in den Kanon oder in Trainingsartefakte wandern.
- Review, Promotion und Trainingsableitung bleiben getrennte Schritte.

Kernregel
---------

- Eine Hauptwelt, mehrere moegliche Laborzuege, keine stille Zeitlinienmischung.
- Der aktuelle Hauptwelt- und Fortsetzungsstand wird immer explizit benannt.
- Alles andere bleibt `Probe`, `Laborpfad`, `verworfen` oder `bewusst pausiert`, bis ein ausdruecklicher Richtungswechsel beschlossen ist.

Aktuelle Matrix
---------------

| Strang | Aktueller Status | Sofort erlaubt | Gesperrt | Naechster sauberer Schritt |
| --- | --- | --- | --- | --- |
| Nordlinie D5-C6 | Hauptweltpfad, chronologisch aktueller Weltstand | Fortsetzen, verdichten, in Runtime-Typdateien spiegeln, gegen SSOT pruefen | Kein freier Vollerfolg ohne Beleg; keine direkte Trainingsnutzung aus Rohspur | Weitere Laborzuege sammeln, danach gezielte Promotion in `database-rp/**` |
| C6-H47 Handelsfenster | verworfener Probe-Einstiegspunkt | Dokumentiert halten, als Routing- oder Vergleichsversuch lesen | Nicht still als Hauptfortsetzung weiterlesen; keine Promotion in die Hauptwelt ohne Richtungswechsel | Nur bei ausdruecklicher Rueckkehr bewusst neu ansetzen oder separat reviewen |
| Neue Labor-Session | Laborpfad, noch unentschieden | Rohspur, Scene-Log und Typdateien schreiben; Review markieren | Keine automatische Kanonisierung; keine direkte Trainingsnutzung | Nach einigen Zuegen gegen Hauptweltpfad und SSOT pruefen |

Review-Stufen
-------------

1. `Probe`
   - fruehe Lesart oder Testzug
   - darf Widersprueche, Richtungswechsel oder verworfene Einstiege noch enthalten
2. `Arbeitsstand`
   - mehrere Zuege konsistent verdichtet
   - Runtime-Typdateien spiegeln die belastbaren Folgen bereits knapp mit
3. `review_required`
   - gegen SSOT, Hauptweltpfad und andere aktive Runtime-Strukturen gegenlesen
   - offene Widersprueche, Zeitspruenge und ungesicherte Links muessen sichtbar bleiben
4. `promotion_ready`
   - nur fuer Inhalte, die belastbar, widerspruchsarm und sauber verlinkt sind
   - erst danach Uebernahme nach `database-rp/**` oder in ein freigegebenes Curation-Artefakt

Pflichtpruefung vor Promotion
-----------------------------

Vor jeder Promotion muessen alle folgenden Fragen mit Ja beantwortet sein:

1. Ist klar markiert, welcher Strang Hauptweltpfad ist und welcher Strang nur Labor oder Probe war?
2. Stimmen `scene-log.md`, `transcript.jsonl` und alle betroffenen Typdateien (`state/`, `inventories/`, `relationships/`, `characters/`, `mind/`) im selben Richtungsentscheid ueberein?
3. Verweist der Strang auf die relevanten SSOT-Anker in `database-rp/**` und widerspricht ihnen nicht?
4. Ist sichtbar, ob der Eintrag nur Runtime-Arbeitsstand, reviewpflichtig oder wirklich promotionsreif ist?
5. Wuerde eine Uebernahme in die Hauptwelt keinen zweiten parallelen Weltverlauf erzeugen?

Laborpfad und Datennutzen
-------------------------

- Weitere RP-Fortsetzung unter Laborbedingungen ist ausdruecklich sinnvoll.
- Sie hilft dem Projekt durch mehr Rohdaten fuer Stil, Weltverdichtung, Figurenstimme, Review und spaetere Curation.
- Dieser Nutzen entsteht aber nur, wenn Laborzuege sauber als solche markiert bleiben und nicht vorschnell als Hauptwelt gelesen werden.
- Mehr Labor-Daten sind deshalb ein Vorteil fuer spaetere Trainingsarbeit, aber nur ueber den Zwischenschritt Review und Promotion.

Trainingsbezug
-------------

- `rp-runtime/**` und `transcript.jsonl` sind nicht direkt trainierbar.
- Direkte Builder- oder Exportpfade fuer Training duerfen nur auf RP-SSOT oder explizit freigegebene Curation-Artefakte zeigen.
- Ein Laborzug kann spaeter nuetzlich fuer Training werden, aber erst nach dieser Kette:
  1. Laborzug in `rp-runtime/`
  2. Review gegen Hauptweltpfad und SSOT
  3. Promotion nach `database-rp/**` oder in ein freigegebenes Curation-Artefakt
  4. erst danach Ableitung in Eval-/Trainingspakete

Verknuepfte Quellen
-------------------

- `novapolis-rp/database-curated/staging/rp-runtime/README.md`
- `novapolis-rp/database-curated/staging/rp-runtime/mind/README.md`
- `novapolis-dev/docs/process/rp-chat-transcript-flow.ssot.md`
- `novapolis-dev/docs/process/rp-runtime-surface-matrix.ssot.md`
- `novapolis-dev/docs/dataset-provenance.md`
- `novapolis-rp/database-rp/01-factions/novapolis/Nordlinie-D5-C6-Index.md`
