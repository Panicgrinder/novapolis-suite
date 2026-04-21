---
stand: 2026-04-21 01:59
update: Sessions erhalten hier einen festen Landing-Path fuer laufende Szenen- und Verwaltungsprotokolle.
checks: snapshot-lock PASS (2026-04-21 01:59); markdownlint=PASS; frontmatter=PASS (touched md)
---

Runtime Sessions
================

Zweck
-----

Dieser Ordner nimmt laufende RP-Sitzungen auf.

- Pro Sitzung ein eigener Unterordner.
- Dort liegen mindestens `scene-log.md` und bei Bedarf weitere Arbeitsdateien.
- Session-Artefakte bleiben Arbeitsstand, bis ein gezielter Review- oder Promotionsschritt erfolgt.

Minimalvertrag
--------------

- Ordnername: `sessions/<session-id>/`
- Pflichtdatei: `scene-log.md`
- Optionale Dateien: `notes.md`, `promotion-notes.md`, `open-threads.md`
- Jede Sitzung sollte Status und Kanonlage klar markieren.