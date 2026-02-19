---
stand: 2026-02-20 00:57
update: MCP-Prototyp verifiziert (lokaler Start mit PYTHONPATH, Web-Client-Health-Check erfolgreich).
checks: "Invoke-WebRequest -UseBasicParsing http://127.0.0.1:4000/health PASS ({\"status\":\"ok\"}) (2026-02-19 23:14)"
---

MCP OpenAI Eval (Prototyp)
==========================

Ziel
----

Minimaler lokaler Integrationspunkt als FastAPI-Server mit stabilem Health-Endpunkt.
Der Prototyp dient als Basis fuer spaetere MCP-/Eval-Bridge-Funktionen.

Implementierungsstand
---------------------

- Server: `novapolis-dev/integrations/mcp-openai-eval/src/mcp_openai_eval/server.py`
- App: FastAPI mit `GET /health`
- Script Entry-Point: `mcp-openai-eval`
- Standard-Port: `4000`

Lokal starten
-------------

Aus dem Repo-Root:

```powershell
& .\.venv\Scripts\python.exe novapolis-dev\integrations\mcp-openai-eval\src\mcp_openai_eval\server.py
```

Alternativ ueber Paket-Entry-Point (falls installiert):

```powershell
mcp-openai-eval
```

VS Code Launch
--------------

Empfohlene Debug-Konfiguration (Root-`.vscode/launch.json`):

- `Integration: MCP OpenAI Eval (uvicorn)`
- CWD: `novapolis-dev/integrations/mcp-openai-eval`
- Host/Port: `127.0.0.1:4000`

Verbindungstest (Web-Client)
----------------------------

1. Server starten.
2. Browser-Test (Swagger): `http://127.0.0.1:4000/docs`
3. Health-Endpunkt pruefen:

```powershell
Invoke-WebRequest -UseBasicParsing http://127.0.0.1:4000/health | Select-Object -ExpandProperty Content
```

Erwartete Antwort:

```json
{"status":"ok"}
```

Bekannte Grenzen (Prototyp)
---------------------------

- Noch keine MCP-Tool-Registry/Methoden ausser Health.
- Keine Auth-/Tenant-Logik.
- Keine Persistenz- oder Eval-Job-Orchestrierung.

Naechste Ausbaustufe
--------------------

- MCP-Methoden fuer Eval-Job-Start/Status/Result-Metadaten.
- Optionaler API-Key-Guard fuer lokale Netzsegmente.
- Bruecke zu vorhandenen Eval-Resultaten unter `novapolis_agent/eval/results/`.


