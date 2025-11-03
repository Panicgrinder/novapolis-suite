# Staging – Curation Leitfaden

Ziel: Große Exporte schrittweise, reproduzierbar und überprüfbar kuratieren.

Empfohlene Tags beim Annotieren:
- [SCENE] – Szenenanker (Ort/Zeit/Übergang)
- [FACT] – Kanon-Fakt (Welt/Regel/Technik)
- [CHAR] – Charakter-bezogene Info
- [LOC] – Ort-bezogene Info
- [PROJ] – Projekt-/Aufgabenstatus
- [INV] – Inventar/Material/Fehlteil
- [OPEN] – Offener Faden/Frage/Blocker

Arbeitsablauf pro Datei:
1) Quelle in `manifest.json` prüfen (Status `pending`).
2) Normalisierte Textfassung erzeugen: <basename>.normalized.txt (Leerzeilen trimmen, triviale Doppelte entfernen).
3) Optional: <basename>.jsonl generieren (Felder: speaker, text, ts?).
4) Annotiertes Review-Dokument anlegen: <basename>.review.md mit obigen Tags.
5) Querprüfung gegen PDF/weitere Exporte (Stichproben, fehlende Abschnitte).
6) Status in `manifest.json` auf `reviewed` -> ggf. `approved` setzen.
7) Artefakte nach `../final/` übernehmen; Folgearbeiten in `database-rp/` anstoßen.

Qualitätssicherung (Checkliste):
- [ ] Deduplizierung grober Doppler durchgeführt
- [ ] Offensichtliche OCR/Copy-Paste-Artefakte bereinigt
- [ ] Mindestens 10% Stichprobe gegen Sekundärquelle geprüft (PDF)
- [ ] Extrakte (Fakten/Szenenanker) erstellt
- [ ] Offene Punkte dokumentiert ([OPEN])

