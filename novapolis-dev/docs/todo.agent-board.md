---
stand: 2026-02-23 15:52
update: Schritt 10 umgesetzt: README/Runbook/Tasking auf evidenzbasierten Ist-Stand synchronisiert und dokumentiert.
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-dev/docs/todo.agent-board.md' 'novapolis-dev/docs/todo.index.md' 'novapolis-dev/docs/donelog.md' PASS (2026-02-23 13:52); .\.venv\Scripts\python.exe scripts/check_frontmatter.py 'novapolis-dev/docs/todo.agent-board.md' 'novapolis-dev/docs/todo.index.md' 'novapolis-dev/docs/donelog.md' PASS (EXITCODE=0, 2026-02-23 13:52)
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
- [x] [Jetzt] Provider-Interface + lokaler Dummy-Adapter anlegen (Coqui folgt spaeter), damit Endpunkte testbar integriert werden koennen.
  - Evidenz: `novapolis_agent/app/tts/providers.py` (`TtsProviderProtocol`, `DummyTtsProvider`, `NullTtsProvider`, Adapter-Scaffolds fuer `coqui`/`ollama`/`openai`), `novapolis_agent/app/main.py` (Provider-Fabrikverdrahtung), `novapolis_agent/tests/test_tts_provider_abstraction.py`.
- [x] [Jetzt] Einfache Auth-Regel fuer TTS-Endpunkte definieren (Header-Token/ENV), inkl. klarer 401/403-Pfade.
  - Evidenz: `novapolis_agent/app/core/settings.py` (`TTS_AUTH_ENABLED`, `TTS_AUTH_HEADER`, `TTS_AUTH_TOKEN`), `novapolis_agent/app/main.py` (`_require_tts_auth`), `novapolis_agent/tests/test_tts_auth_contract.py`.
- [x] [Jetzt] Rate-Limit-Verhalten fuer TTS festlegen (Reuse des vorhandenen In-Memory-Limiters, Grenzwerte, Header, keine Regression fuer Chat-Endpunkte).
  - Evidenz: `novapolis_agent/app/main.py` (scope-basierter In-Memory-Limiter), `novapolis_agent/app/core/settings.py` (`TTS_RATE_LIMIT_*`), `novapolis_agent/tests/test_tts_rate_limit_contract.py`, `novapolis_agent/tests/test_rate_limit_and_timeout.py`, `novapolis_agent/tests/test_input_length_and_rate_headers.py`.
- [x] [Jetzt] Lokalen TTS-Cache-Vertrag festlegen (Hash-Key aus Text+Stimme+Format+Settings, Zielpfad, Hit/Miss-Semantik, Loeschpfad).
  - Evidenz: `novapolis_agent/app/main.py` (`_tts_cache_*`, `/tts/cache/stats`, `/tts/cache/cleanup`), `novapolis_agent/app/core/settings.py` (`TTS_CACHE_*`), `novapolis_agent/tests/test_tts_cache_contract.py`.
- [x] [Jetzt] Tests fuer Mini-Service-Skeleton anlegen (API-Vertrag, Auth, Rate-Limit-Header, Cache-Hit/Miss, Error-Codes).
  - Evidenz: `novapolis_agent/tests/test_tts_api_contract.py`, `novapolis_agent/tests/test_tts_auth_contract.py`, `novapolis_agent/tests/test_tts_rate_limit_contract.py`, `novapolis_agent/tests/test_tts_cache_contract.py`, `novapolis_agent/tests/test_tts_provider_abstraction.py`, `novapolis_agent/tests/test_openapi_contract.py`.
- [ ] [Als naechstes] Coqui-Exporter (Build-Time) in Teilaufgaben aufspalten: (1) Voice-Mapping-Spec, (2) Hash-Cache-Layout, (3) Exportzielstruktur `novapolis-sim/assets/voiceovers/de/`, (4) CLI/Args, (5) Smoke-Test.
- [ ] [Als naechstes] VS Code Tasks (Planung): "TTS: export (coqui)", "TTS: clean cache", "TTS: check voices". Umsetzung erst nach Spec-Freigabe.
- [x] [Als naechstes] README-Truthfulness: TTS-Claims in `novapolis_agent/README.md` bis zur Implementierung explizit als „geplant“ markieren und auf dieses Board verweisen.
  - Evidenz: `novapolis_agent/README.md` (Abschnitt "Ist-Stand (Betriebsfaehigkeit)" mit klarer Contract-First-Einordnung), `novapolis_agent/docs/runbook.md` (operativer Ist-Stand), `.vscode/tasks.json` (TTS-Export-Task auf reales Wrapper-Script statt Platzhalter).
- [ ] [Als naechstes] Eigener TTS-Model-Track konkretisieren: (1) Daten-/Rechte-Policy, (2) Trainingsziel (Finetune vs. eigenes Modell), (3) Evaluationsmetriken, (4) Runtime-Adapter-Plan hinter Schritt 7.
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

1. [x] Laufzeitbasis stabilisieren: venv, editable install, reproduzierbarer Start (`run_server.py`/ASGI), klare Systemvoraussetzungen (Python, Ollama/Provider, Ports).
  Evidenz: `novapolis_agent/scripts/check_runtime_prereqs.py`, `novapolis_agent/tests/scripts/test_check_runtime_prereqs.py`, `novapolis_agent/run_server.py`.
2. [x] Konfigurationsvertrag fixieren: einheitliche ENV-Defaults in `app/core/settings.py`, Pflicht-/Optionalvariablen dokumentieren, sichere Fallbacks ohne Silent-Fail.
  Evidenz: `novapolis_agent/app/core/settings.py`, `novapolis_agent/tests/test_settings_parsing.py`, `novapolis_agent/README.md` (Abschnitt Konfigurationsvertrag).
3. [x] API-Vertragslage abschliessen: Chat + TTS-Endpunkte finalisieren (Schemas, Fehlercodes, Timeouts, Limits), OpenAPI als technische SSOT nutzen.
  Evidenz: `novapolis_agent/app/main.py` (responses + timeouts), `novapolis_agent/app/api/models.py` (`ApiErrorResponse`), `novapolis_agent/tests/test_openapi_contract.py`, `novapolis_agent/tests/test_tts_api_contract.py`.
4. [x] Auth + Zugriffsschutz aktivieren: minimal lokaler Schutz fuer sensible Endpunkte (Token/API-Key), klare 401/403-Semantik und testbare Ausnahmen.
  Evidenz: `novapolis_agent/app/main.py` (`_require_tts_auth`), `novapolis_agent/app/core/settings.py` (`TTS_AUTH_*`), `novapolis_agent/tests/test_tts_auth_contract.py`.
5. [x] Rate-Limit + Request-Grenzen harden: reproduzierbares Header-Verhalten, Schutz gegen Abuse, regressionsfrei fuer bestehende Chat-Flows.
  Evidenz: `novapolis_agent/app/main.py` (global+tts limiter), `novapolis_agent/app/core/settings.py` (`RATE_LIMIT_*`, `TTS_RATE_LIMIT_*`), `novapolis_agent/tests/test_tts_rate_limit_contract.py`, `novapolis_agent/tests/test_rate_limit_and_timeout.py`, `novapolis_agent/tests/test_input_length_and_rate_headers.py`.
6. [x] Cache- und Speicherstrategie einziehen: deterministische Key-Bildung, TTL/Size-Limits, Cleanup-Pfad, nachvollziehbare Hit/Miss-Telemetrie.
  Evidenz: `novapolis_agent/app/main.py` (`_tts_cache_key_from_payload`, `_tts_cache_cleanup_unlocked`, `/tts/cache/stats`, `/tts/cache/cleanup`), `novapolis_agent/app/core/settings.py` (`TTS_CACHE_TTL_SEC`, `TTS_CACHE_MAX_ENTRIES`, `TTS_CACHE_MAX_BYTES`), `novapolis_agent/tests/test_tts_cache_contract.py`.
7. [x] Provider-Abstraktion produktiv machen: Dummy/Null-Provider fuer Offline-Tests, danach Coqui-/Ollama-/OpenAI-Adapter hinter identischer Schnittstelle.
  Evidenz: `novapolis_agent/app/tts/providers.py`, `novapolis_agent/app/core/settings.py` (`TTS_PROVIDER`), `novapolis_agent/app/main.py` (abstrakte Provider-Verwendung), `novapolis_agent/tests/test_tts_provider_abstraction.py`.
8. [x] Testpyramide vollziehen: Unit + API + Streaming + Fehlerpfade + Contract-Tests, danach Marker-Laeufe in CI-identischem CWD-Modus.
  Evidenz: Markerlaeufe in `novapolis_agent`-CWD mit `.venv` erfolgreich (`pytest -q -m unit`, `pytest -q -m "api or streaming"`, `pytest -q -m scripts`) plus grüne Vertrags-/Fehlerpfad-Suites (`test_openapi_contract.py`, `test_app_chat_post_error.py`, `test_app_chat_stream_error.py`).
9. [x] Qualitaetsgates grün fahren: Reihenfolge Lint -> Typen -> Tests -> Coverage stabil auf >=80 %, bekannte Flakes beseitigen oder isolieren.
  Evidenz: `ruff check .` + `black --check .` grün, `pyright -p pyrightconfig.json` + `mypy --config-file mypy.ini app scripts` grün, `pytest -q` grün, `scripts/run_pytest_coverage.py --fail-under 80` Exitcode 0 (alles in CI-identischem `novapolis_agent`-CWD mit `.venv`).
10. [x] Betriebsfaehigkeit dokumentieren: README/Runbook/Tasks auf wahrheitsgetreuen Ist-Stand bringen (kein Claim ohne Evidenz), Postflight-Receipts und DONELOG sauber pflegen.
  Evidenz: `novapolis_agent/README.md` (Ist-Stand + Gate-Reihenfolge), `novapolis_agent/docs/runbook.md` (Betriebs-/Gate-Runbook), `.vscode/tasks.json` (`TTS: export (Coqui->OGG)` nutzt `tts_export_coqui.py --help`), `novapolis_agent/docs/DONELOG.txt` + `novapolis-dev/docs/donelog.md` (laufende Receipts/Logs).
