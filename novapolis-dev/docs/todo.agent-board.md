---
stand: 2026-02-23 09:19
update: Analysebefunde in konkrete Agent-TODO-Punkte fuer TTS-Mini-Service ueberfuehrt (Driftfix, API-Vertrag, Auth/Cache/Tests).
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-dev/docs/todo.agent-board.md' 'novapolis-dev/docs/todo.index.md' 'novapolis-dev/docs/donelog.md' PASS (2026-02-23 09:09); .\.venv\Scripts\python.exe scripts\check_frontmatter.py 'novapolis-dev/docs/todo.agent-board.md' 'novapolis-dev/docs/todo.index.md' 'novapolis-dev/docs/donelog.md' PASS (EXITCODE=0, 2026-02-23 09:09)
---

<!-- markdownlint-disable MD012 MD022 MD041 -->

Novapolis Agent - ToDo & Roadmap (SSOT)
---------------------------------------

Hinweis
------
- Dies ist die zentrale ToDo-Datei (Single Source of Truth) fuer das Agent-Modul.
- Historische Inhalte aus frueheren Redirect-Dateien sind bereits in dieses Board/Archiv ueberfuehrt.
- Bis zur vollstaendigen Migration verweist die alte Datei als Redirect-Stub auf diese Seite.

Prioritaetstags (aktiv)
-----------------------

- `Jetzt`: Mini-Service (Runtime, Planung).
- `Als naechstes`: VS Code Tasks (Planung) fuer TTS.
- `Spaeter`: Templates fuer `knowledge:`/`actions:` in Agent-README verlinken.

Platzhalter

- [x] Abgleich mit Root Coverage-Gate (R-COV) und Aufnahme fehlender Pruefsteps (Receipt-Formate) in diesen Plan

R-COV Abgleich (Agent)
----------------------

- [x] Gate-Wert uebernommen: Coverage-Fail-Under bleibt `80` (Root-Policy).
- [x] Laufreihenfolge festgelegt: Lint -> Typen -> Tests -> Coverage.
- [x] Standard-Entrypoints dokumentiert:
  - `python scripts/run_checks_and_report.py --scope full`
  - `python scripts/run_pytest_coverage.py --fail-under 80`
- [x] Receipt-Pflicht konkretisiert:
  - `DONELOG.md`: PASS/FAIL, Quote, Zeitstempel, Commit-SHA.
  - `WORKSPACE_STATUS.md`: Kurzstatus "Tests/Typen/Coverage aktuell" mit Datum/Quote.

Neue Aufgaben - TTS & Tools (2025-11-01 22:24)
----------------------------------------------

- [ ] [Jetzt] Driftfix: Coqui-Exporter-Iststand gegen Board abgleichen (`scripts/tts_coqui_export.py` fehlt aktuell im Modul) und Boardstatus danach sauber aktualisieren.
- [ ] [Jetzt] Mini-Service API-Vertrag definieren (`/tts/synthesize`, `/tts/health`, Request-/Response-Modelle, Fehlercodes, OGG/WAV-Outputmodi).
- [ ] [Jetzt] Provider-Interface + lokaler Dummy-Adapter anlegen (Coqui folgt spaeter), damit Endpunkte testbar integriert werden koennen.
- [ ] [Jetzt] Einfache Auth-Regel fuer TTS-Endpunkte definieren (Header-Token/ENV), inkl. klarer 401/403-Pfade.
- [ ] [Jetzt] Lokalen TTS-Cache-Vertrag festlegen (Hash-Key aus Text+Stimme+Format, Zielpfad, Hit/Miss-Semantik).
- [ ] [Jetzt] Tests fuer Mini-Service-Skeleton anlegen (API-Vertrag, Auth, Rate-Limit-Header, Cache-Hit/Miss).
- [ ] [Als naechstes] VS Code Tasks (Planung): "TTS: export (coqui)", "TTS: clean cache", "TTS: check voices". Umsetzung erst nach Spec-Freigabe.
- [ ] [Spaeter] Templates bereitstellen: Beispiel-YAML fuer `knowledge:`/`actions:` in Agent-README verlinken (Quelle: Dev-Annotation-Spec).

TTS-Basisentscheidung (2026-02-22)
----------------------------------

- Exporter-Entrypoint bleibt `scripts/tts_coqui_export.py`.
- I/O-Vertrag fuer Build-Time-MVP:
  - Input: `--input <jsonl|yaml|txt>` + `--voice-map <yaml>` + `--lang de`.
  - Output: OGG-Dateien nach `novapolis-sim/assets/voiceovers/de/` mit stabilem Dateinamensschema und Hash-Cache.
- Scope heute: Spezifikation verbindlich; Implementierung/Tasks bleiben als offene Board-Punkte bestehen.

Archivierte Bloecke (Agent)
--------------------------
- Kurzfristige Ziele (Heute) - archiviert am 2025-11-01 19:16 -> `novapolis-dev/archive/todo.agent.archive.md`
