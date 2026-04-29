---
stand: 2026-04-29 03:56
update: Sessions koennen jetzt zusaetzlich ein append-only `transcript.jsonl` fuer rohe Chatspuren fuehren.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260429_035444.md
---

Runtime Sessions
================

Zweck
-----

Dieser Ordner nimmt laufende RP-Sitzungen auf.

- Pro Sitzung ein eigener Unterordner.
- Dort liegen mindestens `scene-log.md` und bei Bedarf weitere Arbeitsdateien.
- Fuer lueckenlose Rohspur kann dieselbe Sitzung optional ein append-only `transcript.jsonl` fuehren.
- Session-Artefakte bleiben Arbeitsstand, bis ein gezielter Review- oder Promotionsschritt erfolgt.

Minimalvertrag
--------------

- Ordnername: `sessions/<session-id>/`
- Pflichtdatei: `scene-log.md`
- Optionale Dateien: `transcript.jsonl`, `notes.md`, `promotion-notes.md`, `open-threads.md`
- Jede Sitzung sollte Status und Kanonlage klar markieren.
- `transcript.jsonl` bleibt append-only und roh; nachtraegliche Korrekturen erfolgen ueber neue Records statt stiller Umschreibung.
- Wenn Tracking erst spaeter beginnt, startet die Datei ehrlich mit `transcript_tracking_started` und einem sichtbaren Backfill-Hinweis.
