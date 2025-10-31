# Novapolis-RP Workspace (F:)

Ein schlanker Workspace für dein AI-geführtes RP „Chronist von Novapolis“. Fokus: belastbares Gedächtnis, saubere Struktur, schneller Szenenstart.

## Ordnerstruktur

- 00-admin/ – Systemprompt, Memory-Bundle, Meta
- 01-canon/ – Welt-Lore, Regeln, Fraktionen
- 02-characters/ – Charaktere (Ronja, Reflex, Jonas …)
- 03-locations/ – Orte (D5, C6, Tunnel …)
- 04-inventory/ – Inventar & Ressourcen
- 05-projects/ – Projekte (z. B. „Nordlinie 01“)
- 06-scenes/ – Szenen-Notizen, Tagebuch
- 99-exports/ – Exporte (PDF/TXT) aus Chat

## Quickstart

1) Lege deine Exporte in `99-exports/` (z. B. `chat-export-complete.txt`, PDF).
2) Öffne `00-admin/memory-bundle.md` als Kanon. Bei Änderungen dort nachführen.
3) Starte einen neuen Chat mit dem Inhalt aus `00-admin/system-prompt.md` als System-Prompt und poste dann das Memory-Bundle als User-Nachricht.
4) Logge Fortschritt in `novapolis-dev/docs/donelog.md`. Offene Aufgaben in `novapolis-dev/docs/todo.md` pflegen.

## Export-Hinweis

Bei sehr langen Threads: Auto-Exporter aus der Konsole verwenden (wurde dir im Chat geliefert). Speichere Zwischenstände in `99-exports/`.

## Schreibstil

- Keine Zitatblöcke in Antworten (besser für Screenreader).
- Cinematisch, fokussiert, 250–400 Wörter je Antwort.
- Vorschläge/Optionen nur auf Anfrage.

Viel Spaß und gute Fahrt durch D5/C6!

---

## Visualisierung

- Das Backend `novapolis-agent` stellt eine Simulations-API bereit (`GET /world/state`, `POST /world/step`) auf Port `AGENT_PORT` (Standard 8765).
- Das Godot-Projekt `novapolis-sim` fragt jeden 0,2 s einen Schritt `{dt:0.1}` ab und visualisiert Tick sowie Zeit.
- Startfolge: Agent per `uvicorn app.api.sim:app --host 127.0.0.1 --port 8765 --reload` (oder VS-Code-Task) starten, anschließend `novapolis-sim` in Godot öffnen und **Play** drücken.

---

## Projektüberblick

Dieses Repo enthält die Arbeitsbasis für das Novapolis‑RP: strukturierte Daten (Admin, Kanon, Charaktere, Orte, Inventar, Projekte, Szenen) und ein leichtgewichtiges Coding‑Verzeichnis mit Hilfsdokumenten.

### Agenten-Modul

Der Agent-Code wird inzwischen ausschließlich im Schwesterprojekt `../novapolis-agent/` gepflegt. Dieses Repository bündelt nur noch die RP-Daten, Workflows und begleitenden Tools.

### Ziele

- Reibungsloser Szenenstart mit stabilem Gedächtnis (Memory‑Bundle)
- Klare, nachvollziehbare Dokumentation und Exporte
- Einfache Automatisierung für Checks (Markdown‑Lint)

## Status & Automatisierung

- Lizenz: MIT (siehe `LICENSE`)
- CI: einfacher Markdown‑Lint‑Check via GitHub Actions

## Wie beitragen (kurz)

- Nutze `novapolis-dev/docs/todo.md` für Aufgaben und `novapolis-dev/docs/donelog.md` für Abschlüsse.
- PRs: kurze Beschreibung, was/warum geändert wurde; große Blöcke in überschaubare Schritte teilen.

## Badges

![Docs Lint](https://github.com/Panicgrinder/Novapolis-RP/actions/workflows/docs-lint.yml/badge.svg)

## Lizenz

MIT – siehe `LICENSE`.
