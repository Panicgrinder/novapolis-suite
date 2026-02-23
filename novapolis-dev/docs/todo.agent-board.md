---
stand: 2026-02-23 12:35
update: 10-Schritte-Masterplan fuer stabile KI-Inbetriebnahme im Agent-Board ergaenzt.
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-dev/docs/todo.agent-board.md' 'novapolis-dev/docs/donelog.md' PASS (2026-02-23 10:42); C:/Users/FloAu/AppData/Local/Programs/Python/Python313/python.exe scripts/check_frontmatter.py 'novapolis-dev/docs/todo.agent-board.md' 'novapolis-dev/docs/donelog.md' PASS (EXITCODE=0, 2026-02-23 10:42)
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

- [x] [Jetzt] Driftfix: Coqui-Exporter-Iststand gegen Board abgleichen (`scripts/tts_coqui_export.py` fehlt aktuell im Modul) und Boardstatus danach sauber aktualisieren.
  - Evidenz: `novapolis_agent/scripts/tts_coqui_export.py` (Skeleton mit CLI-Vertrag + `--dry-run`).
- [x] [Jetzt] Mini-Service API-Vertrag definieren (`/tts/health`, `/tts/voices`, `/tts/synthesize`, Request-/Response-Modelle, Fehlercodes, OGG/WAV-Outputmodi).
  - Evidenz: `novapolis_agent/app/api/tts_models.py`, `novapolis_agent/app/main.py`, `novapolis_agent/tests/test_tts_api_contract.py`.
- [ ] [Jetzt] Provider-Interface + lokaler Dummy-Adapter anlegen (Coqui folgt spaeter), damit Endpunkte testbar integriert werden koennen.
- [ ] [Jetzt] Einfache Auth-Regel fuer TTS-Endpunkte definieren (Header-Token/ENV), inkl. klarer 401/403-Pfade.
- [ ] [Jetzt] Rate-Limit-Verhalten fuer TTS festlegen (Reuse des vorhandenen In-Memory-Limiters, Grenzwerte, Header, keine Regression fuer Chat-Endpunkte).
- [ ] [Jetzt] Lokalen TTS-Cache-Vertrag festlegen (Hash-Key aus Text+Stimme+Format+Settings, Zielpfad, Hit/Miss-Semantik, Loeschpfad).
- [ ] [Jetzt] Tests fuer Mini-Service-Skeleton anlegen (API-Vertrag, Auth, Rate-Limit-Header, Cache-Hit/Miss, Error-Codes).
- [ ] [Als naechstes] Coqui-Exporter (Build-Time) in Teilaufgaben aufspalten: (1) Voice-Mapping-Spec, (2) Hash-Cache-Layout, (3) Exportzielstruktur `novapolis-sim/assets/voiceovers/de/`, (4) CLI/Args, (5) Smoke-Test.
- [ ] [Als naechstes] VS Code Tasks (Planung): "TTS: export (coqui)", "TTS: clean cache", "TTS: check voices". Umsetzung erst nach Spec-Freigabe.
- [ ] [Als naechstes] README-Truthfulness: TTS-Claims in `novapolis_agent/README.md` bis zur Implementierung explizit als „geplant“ markieren und auf dieses Board verweisen.
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

Masterplan: KI-End-to-End in 10 grossen Schritten
--------------------------------------------------

1. Laufzeitbasis stabilisieren: venv, editable install, reproduzierbarer Start (`run_server.py`/ASGI), klare Systemvoraussetzungen (Python, Ollama/Provider, Ports).
2. Konfigurationsvertrag fixieren: einheitliche ENV-Defaults in `app/core/settings.py`, Pflicht-/Optionalvariablen dokumentieren, sichere Fallbacks ohne Silent-Fail.
3. API-Vertragslage abschliessen: Chat + TTS-Endpunkte finalisieren (Schemas, Fehlercodes, Timeouts, Limits), OpenAPI als technische SSOT nutzen.
4. Auth + Zugriffsschutz aktivieren: minimal lokaler Schutz fuer sensible Endpunkte (Token/API-Key), klare 401/403-Semantik und testbare Ausnahmen.
5. Rate-Limit + Request-Grenzen harden: reproduzierbares Header-Verhalten, Schutz gegen Abuse, regressionsfrei fuer bestehende Chat-Flows.
6. Cache- und Speicherstrategie einziehen: deterministische Key-Bildung, TTL/Size-Limits, Cleanup-Pfad, nachvollziehbare Hit/Miss-Telemetrie.
7. Provider-Abstraktion produktiv machen: Dummy/Null-Provider fuer Offline-Tests, danach Coqui-/Ollama-/OpenAI-Adapter hinter identischer Schnittstelle.
8. Testpyramide vollziehen: Unit + API + Streaming + Fehlerpfade + Contract-Tests, danach Marker-Laeufe in CI-identischem CWD-Modus.
9. Qualitaetsgates grün fahren: Reihenfolge Lint -> Typen -> Tests -> Coverage stabil auf >=80 %, bekannte Flakes beseitigen oder isolieren.
10. Betriebsfaehigkeit dokumentieren: README/Runbook/Tasks auf wahrheitsgetreuen Ist-Stand bringen (kein Claim ohne Evidenz), Postflight-Receipts und DONELOG sauber pflegen.
