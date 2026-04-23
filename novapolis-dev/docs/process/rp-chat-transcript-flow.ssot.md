---
stand: 2026-04-23 16:00
update: Diese SSOT definiert jetzt einen append-only Rohpfad fuer RP-Chattranskripte unterhalb der Runtime-Sessions.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp/results/reports/checks_report_20260423_155606.md; snapshot-lock PASS (2026-04-23 16:00)
---

RP Chat Transcript Flow
======================

Zweck
-----

Diese SSOT fuehrt einen kleinen, belastbaren Rohpfad fuer RP-Chatverlaeufe ein.

- RP-Sitzungen koennen pro Session ein append-only `transcript.jsonl` mitfuehren.
- Der Rohpfad dient lueckenloser Nachvollziehbarkeit, spaeterer Review-Arbeit und einer sauberen Vorstufe fuer moegliche Trainingsableitungen.
- Der Rohpfad ersetzt weder `scene-log.md` noch RP-SSOT und wird nicht direkt trainiert.

Scope
-----

- Geltungsbereich: `novapolis-rp/database-curated/staging/rp-runtime/sessions/<session-id>/transcript.jsonl`
- Inhalt: RP-Zuege, Admin-Hinweise, Moduswechsel, Korrekturhinweise und andere rohe Chatsegmente, solange sie zur laufenden Session gehoeren.
- Koexistenz: `scene-log.md` bleibt die verdichtete Arbeits- und Fortsetzungsspur derselben Session.

Nicht-Ziele
-----------

- kein neuer kanonischer Wahrheitslayer neben `novapolis-rp/database-rp/**`
- kein direkter Builder-Input fuer Training oder Export/Pack
- kein stilles Rueckschreiben frueherer Nachrichten ohne sichtbaren Backfill- oder Bootstrap-Eintrag

Dateivertrag
------------

- Pfad: `sessions/<session-id>/transcript.jsonl`
- Format: UTF-8, eine JSON-Zeile pro Record, append-only
- Mindestfelder pro Record:
  - `record_type`
  - `session_id`
  - `timestamp`
- Fuer `record_type=message` zusaetzlich erwartet:
  - `role`
  - `channel`
  - `content`
- Empfohlene Zusatzfelder:
  - `turn_ref`
  - `evidence_state`
  - `source`
  - `meta`

Erlaubte Grundtypen
-------------------

- `transcript_tracking_started`: markiert den Beginn der Repo-seitigen Rohspur einer bereits laufenden Session.
- `message`: rohe Nutzer-, RP-, Admin- oder Agent-Nachricht.
- `correction`: sichtbare Korrektur eines frueheren Rohrecords ohne Rueckschreiben.

Arbeitsregeln
-------------

- `transcript.jsonl` bleibt roh und append-only; nachtraegliche Aenderungen erfolgen als neuer `correction`-Record statt per stiller Ueberschreibung.
- Wenn eine Session bereits vor Einfuehrung des Rohpfads lief, beginnt die Datei ehrlich mit `transcript_tracking_started` und `backfill_status=not_backfilled` oder einem gleichwertigen expliziten Hinweis.
- Verdichtete Folgen gehoeren weiterhin in `scene-log.md`, `state/*.md`, `inventories/*.md`, `relationships/*.md` oder `characters/*.md`.
- Ein Rohtranskript darf fuer Review, Audit und spaetere Extraktion gelesen werden, aber nicht direkt als RP-SSOT oder Trainingspaket gelten.

Promotionspfad
--------------

1. Rohchat landet append-only in `sessions/<session-id>/transcript.jsonl`.
2. Verdichtete, belastbare Folgen werden wie bisher nach `scene-log.md` und die passenden Runtime-Typdateien gezogen.
3. Erst nach Review duerfen Inhalte in RP-SSOT oder in ein freigegebenes Curation-Pack uebernommen werden.
4. Jede Trainingsnutzung bleibt an denselben Gate-Pfad aus Provenienz, Review und Promotionsentscheidung gebunden.

Verknuepfte Quellen
-------------------

- `novapolis-rp/database-curated/staging/rp-runtime/README.md`
- `novapolis-rp/database-curated/staging/rp-runtime/sessions/README.md`
- `novapolis_agent/docs/runbook.md`
- `novapolis-dev/docs/architecture-summary-local-ai.md`
- `novapolis-dev/docs/dataset-provenance.md`
