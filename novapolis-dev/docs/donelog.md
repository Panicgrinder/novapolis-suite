<!-- markdownlint-disable MD005 MD007 MD032 MD041 -->
<!-- Migration: Quelle aus dem frueheren coding-Hub, uebernommen am 2025-10-29 -->
<!-- Relocated aus dem ehemaligen Novapolis-RP Development-Hub nach `novapolis-dev/docs/donelog.md` am 2025-10-29 -->

Canvas-Rettung Sprint 1 – C6/E3 Linienabgleich (2025-11-02T13:30:00+01:00)

- Neue Location-Canvas `database-rp/03-locations/Verbindungstunnel-C6-E3.{md,json}` angelegt (Status, Nutzung als Evakuierungsroute für 20 E3-Flüchtlinge, Aufgabenliste); Index (`database-rp/index.json`) erweitert und Metadaten mit C6/E3 verknüpft.
- `database-rp/03-locations/C6.md` um Bevölkerung/Verbindungen ergänzt (20 Evakuierte aus E3, 4 Karawanenmitglieder, aktive Tunnel); Sidecar `C6.json` Dependencies auf beide Tunnel gesetzt.
- Lexikon `database-curated/reviewed/chat-export (1)/lexicon.json` aktualisiert (Slug/Aliasse für C6–E3-Tunnel, neue Bewohner-Kontexte beibehalten).

Canvas-Rettung Sprint 1 – Behavior-Signaturen & Validator (2025-11-02T12:45:00+01:00)

- Anchor-Signaturen für Echo, Lumen, Liora, Lyra, Senn und Varek kuratiert (`AI-Behavior-Mapping.md` aktualisiert, Quelle auf Canvas verwiesen, Sidecar-Zeitstempel synchronisiert).
- Charakter-Canvases (`02-characters/*.md` + JSON) um Verhaltenseinträge ergänzt; Skill-Listen auf Leerzeichen-Indents umgestellt, Markdownlint-Ausnahmen (MD025) lokalisiert.
- Validator `coding/tools/validators/behavior_matrix_check.py` erweitert (Signatur-Format/Quellen-Check + Psymatrix-Diff >5-Punkte-Schwelle), README und TODO mit Ausführungshinweis aktualisiert; Task als erledigt markiert.

Canvas-Rettung Sprint 1 – AI Behavior Matrix (2025-11-01T17:55:00+01:00)

- RAW-Canvas `database-raw/99-exports/RAW-canvas-2025-10-16T11-05-00-000Z.txt` promotet: `database-rp/00-admin/AI-Behavior-Mapping.md` auf Version 1.0 erweitert (Cluster-Tabelle, Intensitätsskala, Modifikatoren, Pflege-Routine, Einsatzrichtlinien).
- Anchor-Register um alle aktuellen Charaktere in `02-characters/` ergänzt (inkl. Echo/Lumen/Liora/Lyra/Senn/Varek; `n/a` markiert fehlende Signaturen); Psymatrix-Abgleich-Routine mit Schwellen (`PsySignatur_Dissonanz`, Kohäsion) dokumentiert.
- Sidecar `AI-Behavior-Mapping.json` synchronisiert (Version 1.0, last_updated, dependencies `ai_behavior_index_v2`/`ai_psymatrix_index_v1`, Tag-Set ergänzt).
- TODO aktualisiert (AI-Behavior-Index erledigt, Validator-Follow-up) und Arbeitsablauf um Anchor-Check erweitert; Quellen/Flag-Hinweise verankert.

Canvas-Rettung Sprint 1 – Jonas Merek (2025-11-02T13:55:00+01:00)

- Charakter-Canvas `database-rp/02-characters/Jonas-Merek.md` auf Version 1.0 gehoben; Werte/Skills aus RAW übernommen, Rollen (Werkstatt/Logistik/Terminal) konsolidiert, Sicherheits- & Proximity-Protokolle ergänzt.
- Korruptes RAW-Makel („Schuld am Tod der Schwester“) aufgelöst – Schwesterstatus gemäß FACT `[JONAS-SIS]` als „vermisst/unklar“ dokumentiert, Schuldflag als subjektives Kommentar markiert.
- JSON-Sidecar synchronisiert (Version, Tags, Dependencies `missionslog`, `ai_behavior_index_v2`); `char-block-nord-sources.md` und TODO aktualisiert.
- Verweise auf FACTs `[PROXIMITY]`, `[COMMS-PROTO]`, `[C6-FIRST]`, `[FR-KNOWLEDGE]` eingepflegt; Validierungsintervall notiert.

Canvas-Rettung Sprint 1 – Kora Malenkov (2025-11-02T14:20:00+01:00)

- Charakter-Canvas `database-rp/02-characters/Kora-Malenkov.md` auf Version 1.0 aktualisiert; Werte/Skills aus RAW übernommen, Rollen- und Sicherheitsverantwortung für C6 (Logistik, Echo-Schutz, Terminalprozesse) präzisiert.
- FACT `[CARAVAN-LEADERSHIP]` und `[PROXIMITY]` konsolidiert: interne Logistikführung abgegrenzt zu Marven/Arlen, Echo-Protokolle und Kontrolllisten dokumentiert, Händlergilde+Novapolis Zugehörigkeit festgehalten.
- JSON-Sidecar erweitert (Version, Tags `logistik`/`haendlerbund`, Dependencies `logistik`, `missionslog`, `ai_behavior_index_v2`, `caravan_moves`); `char-block-nord-sources.md`, dev TODO sowie Personenindex-Notiz ergänzt.
- Hinweise auf Sicherheits-/Ermüdungsrisiken und Evakuierungskoordination integriert; Validierungsintervall erfasst.

Canvas-Rettung Sprint 1 – Marven Kael (2025-11-02T14:45:00+01:00)

- Neues Charakter-Canvas `database-rp/02-characters/Marven-Kael.md` erstellt; Konvoi-/Handelsrolle aus RAW übernommen, Sicherheits- und Verhandlungsprotokolle festgeschrieben, Zugehörigkeit zur Händlergilde betont.
- FACT `[CARAVAN-LEADERSHIP]` umgesetzt: klare Trennung zwischen externem Konvoi (Marven), interner Logistik (Kora) und Vermittlung (Arlen); `[FR-KNOWLEDGE]` berücksichtigt (keine Novapolis-Koordinaten).
- JSON-Sidecar ergänzt (Version 1.0, Tags `karawane`/`haendlerbund`, Dependencies `caravan_moves`, `ai_behavior_index_v2`, `missionslog`, `logistik`, `c6`); Quellenreport aktualisiert, dev TODO abgehakt.
- Risiko- und Zielsetzungen dokumentiert (Entscheidungsstarre, Crewschutz, Handelsabkommen); Validierungsintervall notiert.

Canvas-Rettung Sprint 1 – Arlen Dross (2025-11-02T15:05:00+01:00)

- Charakter-Canvas `database-rp/02-characters/Arlen-Dross.md` auf Version 1.0 gehoben; Diplomatie-/Vermittlerrolle gegenüber Novapolis ausgearbeitet, Abgrenzung zu Kora (Logistik) und Marven (Konvoi) gemäß FACT `[CARAVAN-LEADERSHIP]` dokumentiert.
- Wissensmatrix und Sicherheitslinien ergänzt: `[FR-KNOWLEDGE]` respektiert (keine Novapolis-Koordinaten), Reflex als unkalkulierbare Variable mit klaren Freigabesignalen beschrieben, Routine/Validierungszyklen aus RAW übernommen.
- JSON-Sidecar erstellt (Tags `karawane`/`haendlerbund`/`diplomatie`, Dependencies `caravan_moves`, `ai_behavior_index_v2`, `missionslog`, `logistik`, `c6`, `handel_diplomatie_haendlergilde_v1`, `index_haendlergilde_v1`); Quellenreport `char-block-nord-sources.md`, TODO und Personenindex aktualisiert.
- Risiko-/Zielkatalog ergänzt (Entscheidungsparalyse mitigieren, Handelsprotokoll standardisieren, Crew-Moderation sichern); Signals-Beispiele und Systemverknüpfungen dokumentiert.

Canvas-Rettung Sprint 1 – Pahl (2025-11-02T15:25:00+01:00)

- Charakter-Canvas `database-rp/02-characters/Pahl.md` erstellt; Gesundheitsstatus (Reha, Atemprotokolle) aus RAW verifiziert, Rollen (Systemaufsicht, Wartungsplanung, Hausregeln) gemäß FACT `[HOUSE-RULES]`/`[LOGISTICS]` beschrieben.
- Wissens- und Sicherheitsmatrix ergänzt (Atemlog, Belastungsgrenzen, Validierungsintervall, Eskalationspfade „Regel Blau/Rot“), Interaktionshinweise aus Chatpassagen zum Lagerzugang integriert.
- JSON-Sidecar angelegt (Tags `technik`/`novapolis`/`gesundheit`, Dependencies `d5`, `logistik`, `missionslog`, `ai_behavior_index_v2`, `ronja-kerschner`, `jonas-merek`, `reflex`); Quellenreport aktualisiert, dev TODO abgehakt.
- Ziele/Risiken erweitert (Reha abschließen, Systemhandbuch v1.0, Wartungsschnittstelle D5↔C6); Signals-Beispiele dokumentiert.

Canvas-Rettung Sprint 1 – Pahl Herkunfts-Abgleich (2025-11-02T15:50:00+01:00)

- FACT `[PAHL-RESCUE]` in `database-curated/staging/reports/resolved.md` aufgenommen: C6-Reaktorunfall, Rettung durch Ronja/Reflex, Transfer & Reha unter Jonas.
- Canvas `Pahl.md`/`Pahl.json` angepasst (Herkunft, Dependency `c6`, Quellenblock), Memory-Bundle und Personenindex synchronisiert, Quellenreport `char-block-nord-sources.md` erweitert.
- RAW-Flag-Hinweis belassen, aber kanonische Herkunft auf `[PAHL-RESCUE]` gestellt.

Canvas-Rettung Sprint 1 – Ronja Kerschner (2025-11-01T17:12:00+01:00)

- Charakter-Canvas `database-rp/02-characters/Ronja-Kerschner.md` auf Version 1.0 aktualisiert; Status-/Systemabschnitte aus RAW `char_ronja_v2` übernommen und Drift („Vallin“) gemäß `resolved.md #[NAME-RONJA]` dokumentiert.
- JSON-Sidecar (`Ronja-Kerschner.json`) synchronisiert; Routine- und Systemverknüpfungen mit Review-Hinweis auf logistik-/inventar-v1 markiert.
- TODO-Boards (`novapolis-dev/docs/todo.md`, Root `TODO.md`) aktualisiert; Aufgabe „Ronja Kerschner“ auf erledigt gesetzt.
- Quellenhinweise erweitert (Canvas-Quellenblock + `char-block-nord-sources.md` Ronja-Abschnitt aktualisiert); Metadaten-Zeitstempel angepasst.

Canvas-Rettung Sprint 1 – Echo Metadatenabgleich (2025-11-01T16:35:00+01:00)

- Canvas `database-rp/02-characters/Echo.md` um Front-Matter ergänzt (Titel, Version, Zugehörigkeit, Standort, Dependencies) und Markdown-Formatierung mit Leerzeichen/Abständen an Vorlagen angepasst.
- JSON-Sidecar `database-rp/02-characters/Echo.json` auf dieselben Metafelder synchronisiert (last_updated, tags, affiliations, primary_location, dependencies).
- Keine Inhaltsänderungen; Fokus auf formale Angleichung für Lint/Validator-Kompatibilität.

Canvas-Rettung Sprint 1 – Liora Navesh (2025-11-01T16:25:00+01:00)

- Charakter-Canvas `database-rp/02-characters/Liora-Navesh.md` + JSON-Sidecar erstellt; Arkologie-A1-Taxonomie und Validierungsintervall übernommen, Novapolis/D5 weiterhin als unbekannt markiert, SÜDFRAGMENT-Signale und A9-Protokolle hervorgehoben.
- Quellenreport `char-block-nord-sources.md` aktualisiert; Flag-Hinweise (Secrecy, Taxonomie) als abgearbeitet vermerkt und Curated-Verweis ergänzt.
- `novapolis-dev/docs/todo.md` → Liora-Aufgabe als erledigt mit Zeitstempel 2025-11-01T16:20+01:00 markiert; last-updated synchronisiert.
- Personenindex `database-rp/00-admin/person_index_np.md` um Liora ergänzt (Rolle, Zugehörigkeit Arkologie A1, Fokus auf SÜDFRAGMENT, keine Novapolis-Kenntnisse).
- JSON-Sidecar verweist auf Canvas und Abhängigkeiten (`ai_behavior_index_v2`, `relationslog_arkologie_v1`, `ereignislog_weltgeschehen_v1`, `cluster_index_v1`).

Canvas-Rettung Sprint 1 – Varek Solun (2025-11-01T15:55:00+01:00)

- Charakter-Canvas `database-rp/02-characters/Varek-Solun.md` + JSON-Sidecar erstellt; Standortcode H12 (Alias „Sektor_H3“) harmonisiert, Wissensstand gemäß FACT SECRECY auf Gerüchte begrenzt.
- Quellen/Drift-Notizen in `char-block-nord-sources.md` aktualisiert; Flag-Hinweise (Novapolis-Außenwissen, Standortcodierung) als erledigt markiert.
- `novapolis-dev/docs/todo.md` und Root-`TODO.md` → Varek-Aufgabe als erledigt vermerkt (Zeitstempel 2025-11-01T15:45+01:00).
- Personenindex `database-rp/00-admin/person_index_np.md` um Varek ergänzt (Rolle, Zugehörigkeit, Verlinkung).
- JSON-Sidecar referenziert Metadaten + Quelle; Routine- und Systemverknüpfungen dokumentiert.

Canvas-Rettung Vorbereitungsrunde (2025-11-01T14:30:00+01:00)

- Canvas-Rettungsplan in `database-curated/staging/reports/canvas-rescue-plan.md` ausgearbeitet (Prioritäten A–C, Workflow, Sprint-Checkpoints, Prüfpfade).
- Quellenaggregation `char-block-nord-sources.md` erstellt (RAW-Referenzen, Drift-Overrides für Ronja/Jonas, Flag-Hinweise gebündelt).
- TODO-Board `novapolis-dev/docs/todo.md` auf Canvas-Rettung Sprint 1 fokussiert, Altbacklog in Archiv-Section überführt.
- Hinweis gesetzt: Jede Canvas-Migration → JSON-Sidecar + DONELOG-Eintrag obligatorisch.

Root-Dokumentation (2025-11-01T00:00:00Z)

- Root-Übersichten `WORKSPACE_STATUS.md`, `TODO.md`, `README.md`, `DONELOG.md` auf Stand 2025-11-01 gebracht (Health-Checks, Aufgaben, Querlinks).
- Tree-Snapshots (`workspace_tree*.txt`) als fällige Folgeaufgabe markiert.

Dev-Hub QA (2025-11-01)

- Modul `novapolis-dev` vollständig geprüft: Primärdokumente, Meta-Sidecars und Platzhalterverzeichnisse vorhanden; keine offenen Drift-Punkte.
- Rolle des Dev-Hubs bestätigt – Dokumentations-/Planungsdrehscheibe, Datenströme verbleiben in `novapolis-rp` (`database-raw`, `database-curated`, `database-rp`).

Agent-Runtime entkoppelt (2025-10-31)

- `novapolis-rp/agents/cvn_agent/` vollständig entfernt; Root-README, RP-README und Ignore-Regeln auf das eigenständige `novapolis_agent`-Repository umgestellt.
- Verweise auf das gebündelte Runtime-Paket bereinigt (`requirements.txt`, `.github/copilot-instructions.md`).
- Obsoletes Patch `_cvn_agent_removal.patch` gelöscht; RP-Workspace enthält nur noch Daten/Docs.
- Leeres Paketverzeichnis `novapolis-rp/agents/` entfernt; keine Agent-Stubs mehr im RP-Repo.

Workspace-Status Snapshot (2025-10-31)

- Gesamtübersicht `WORKSPACE_STATUS.md` auf Root-Ebene angelegt (Stand 2025-10-31) inkl. Health-Checks, Risiken, Empfehlungen.
- Vollständigen Verzeichnisbaum via `tree /A /F` erzeugt und als `workspace_tree.txt` im Root abgelegt.
- Root-`TODO.md` um Verweis auf Statusbericht ergänzt (Pflegezyklus vermerkt).
- Redundante Snapshot-Datei `workspace_tree_full.txt` als Backup abgelegt; zusätzlich kompaktes Verzeichnis-Listing `workspace_tree_dirs.txt` erzeugt.
- README-Hinweise für `.tmp-datasets/` und `.tmp-results/` ergänzt, Zweck der temporären Artefakte dokumentiert.
- Archivierungsplan in `TODO.md` konkretisiert (ZIP-Rotation, Manifest/Script-Aufgaben); Status-Doku verweist jetzt auf koordinierte Snapshot-Aktualisierung.
- Redundanten Snapshot `workspace_tree_compact.txt` entfernt, da `workspace_tree_dirs.txt` die kompakte Ansicht abdeckt.

Relocation Follow-up (2025-10-31)

- Datenpools `database-curated`, `database-raw`, `database-rp` wieder unter `novapolis-rp/` verankert; Dev Hub verweist nur noch auf diese Quelle (`README.md`, `docs/todo.md`).
- `novapolis_agent/docs/TODO.md` um aktuellen RAG-Status aktualisiert (Tests & Doku als erledigt markiert).
- Zentrale Markdown-Lint-Checks via `.github/workflows/markdownlint.yml` reaktiviert; rp-spezifische Duplikat-Workflows entfernt (`docs-lint.yml`, redundante Schritte in `validate.yml`).

Dev Hub Konsolidierung (2025-10-29)

- Dev Hub vom ehemaligen RP-Development-Hub nach `novapolis-dev/docs` verlegt; Referenzen aktualisiert und Meta-Sidecars harmonisiert.
- Legacy `development/docs` bereinigt; Meta-Sidecars geprüft; `.github/copilot-instructions.md` im RP-Repo ergänzt.
- 2025-10-29: Meta sidecars normalized: origin → full legacy path; migrated_at added.
- 2025-10-29: Dev Hub polish (README/index), VS Code Copilot instructions verlinkt; Residual-Sweep ohne Treffer.

VS Code Launch-Konfigurationen (2025-10-28)

- `.vscode/launch.json` hinzugefügt:
  - PowerShell-Runner: `validate:data (ps1)`, `lint:names (ps1)`, `lint:markdown (ps1)`, `system:check (windows)`.
  - Node-Varianten: `validate:data (node/npm)`, `lint:names (node)`, `lint:markdown (npx)`, `validate:data (status)`.
  - Ziel: Checks direkt per Startmenü (Run and Debug) nutzbar; identische Pfade wie Tasks/Wrapper.

Dokumentation/Tasks aktualisiert (2025-10-27T20:06:30+01:00)

- `novapolis-dev/docs/index.md` (vormals Coding-Index): Abschnitt "Validierung & Tasks" ergänzt (Validatoren, Lint, Systemcheck); Verweise auf `tools/validators/` und Devcontainer; `last-updated` angepasst.
- `novapolis-dev/docs/copilot-behavior.md` (vormals Coding-Copilot-Policy): Prozessregeln präzisiert – vor Push lokale Tasks ausführen (validate/data, lint/markdown, optional lint/names); Szenen‑Front‑Matter und Co‑Occurrence beachten.
- `novapolis-dev/docs/todo.md` (vormals Coding-TODO): Status synchronisiert – Rückwärts‑Review bis part‑001 abgehakt; Day‑Switch‑Canvas abgehakt; QA‑Punkt zu Szenen‑Front‑Matter in "etabliert" (✓) und "Backfill" (offen) aufgeteilt; `last-updated` angepasst.

Canvas-Verbesserungen (2025-10-27)
Linter-Wrapper (2025-10-27T20:12:30+01:00)

- `coding/tools/validators/run_check_names.ps1` hinzugefügt: stabiler Aufruf des Name-Linters ohne PowerShell `-Command`‑Quoting; nutzt Docker (falls vorhanden) oder Node/npm, sonst Exit 1 mit klarer Meldung.
- `coding/tools/validators/README.md` ergänzt (Wrapper‑Hinweis); `novapolis-dev/docs/index.md` mit Fallback‑Befehl verlinkt.

PS1-Tasks ergänzt (2025-10-27T20:18:30+01:00)

- `.vscode/tasks.json`: zusätzliche Tasks ohne Inline‑`-Command` aufgenommen:
  - `lint:names (ps1)` → `run_check_names.ps1`
  - `validate:data (ps1)` → `run_validate_all.ps1`
  - `lint:markdown (ps1)` → `run_lint_markdown.ps1`
- Neue Wrapper: `run_validate_all.ps1`, `run_lint_markdown.ps1` (Docker bevorzugt; sonst lokal; klare Fehlermeldung bei fehlenden Voraussetzungen).

CI erweitert (2025-10-27T22:40:00+01:00)

- `.github/workflows/validate.yml` aufgeteilt:
  - Linux-Job (Node 20) mit npm cache; führt Validatoren, Name‑Check, Markdown‑Lint aus.
  - Windows-Job (PS1‑Wrapper) – führt `run_validate_all.ps1`, `run_check_names.ps1`, `run_lint_markdown.ps1` aus, um PowerShell‑Skripte in CI mitzuprüfen.
- Validator-Fixes:
  - Ajv 2020‑12 für kuratiertes Manifest (`validate-curated.js`).
  - Front‑Matter‑Validator (`validate-rp.js`): `last-updated` tolerant (String/Date), H1‑Allowlist für `00-admin/system-prompt.md`.

Markdown‑Lint Wrapper gefixt (2025-10-27T22:55:00+01:00)

- `coding/tools/validators/run_lint_markdown.ps1`: Fallbacks ergänzt
  - absolute `node.exe` Erkennung; direkter Aufruf von `npx-cli.js` via `node.exe` (unabhängig von PATH)
  - Reihenfolge: Docker → node+npx-cli.js → npx.cmd → Fehlermeldung
  - Behebt Fehler "'node' is not recognized" bei fehlendem PATH.
- `00-admin/Canvas-Admin-Day-Switch-Debug.md`: ATSD-Definition ergänzt, Systemmeldungs-Template aufgenommen, Fehlerfälle/Recovery ergänzt.
- `00-admin/Canvas-T+0-Timeline.md`: Marker-Raster (Beginn/Ereignisse/Ende) und Delta-Log ergänzt.
- `00-admin/canon-canvas.draft.md`: Front-Matter (last-updated, status) hinzugefügt; Tippfehler "Akologie"→"Arkologie" korrigiert; Revision vermerkt.
- `06-scenes/scene-2025-10-27-a.md`: Erste Szenen-Kachel mit Front-Matter (characters/locations/inventoryRefs) und Cross-Links angelegt; Timeline T+0 verlinkt.
- RAW-Canvas abgelegt: `database-raw/99-exports/RAW-canvas-2025-10-16T03-25-20-000Z.txt` (Quelle: Canvas; Entität Reflex – Wurzelgewebe D5 v1; TIMESTAMP: 2025-10-16_03:25).
- Sidecar-Flag erstellt: `database-raw/99-exports/RAW-canvas-2025-10-16T03-25-20-000Z.flags.txt` (vorsichtig_behandeln; Grund: Regeln [REFLEX-*] abgleichen; „Entfernen möglich“ vs [REFLEX-DETACH] klären; Frequenzband/Terminologie synchronisieren).
- RAW-Canvas abgelegt: `database-raw/99-exports/RAW-canvas-2025-10-16T03-25-10-000Z.txt` (Quelle: Canvas; Charakter Dr. Liora Navesh v1; TIMESTAMP: 2025-10-16_03:25).
- Sidecar-Flag erstellt: `database-raw/99-exports/RAW-canvas-2025-10-16T03-25-10-000Z.flags.txt` (vorsichtig_behandeln; Grund: [FR-KNOWLEDGE] wahren; H‑47/SÜDFRAGMENT gegen [EVENT-TIMELINE] prüfen; Arkologie_A1 Taxonomie mit Cluster/Relations harmonisieren).
- RAW-Canvas abgelegt: `database-raw/99-exports/RAW-canvas-2025-10-16T03-25-00-000Z.txt` (Quelle: Canvas; Charakter Varek Solun v1; TIMESTAMP: 2025-10-16_03:25).
- Sidecar-Flag erstellt: `database-raw/99-exports/RAW-canvas-2025-10-16T03-25-00-000Z.flags.txt` (vorsichtig_behandeln; Grund: [FR-KNOWLEDGE] wahren; H‑47‑Routenstatus prüfen; Standort‑Taxonomie H12 vs „Sektor_H3“ harmonisieren vor Promotion).
 - RAW-Canvas abgelegt: `database-raw/99-exports/RAW-canvas-2025-10-16T08-07-00-000Z.txt` (Quelle: Canvas; Relationslog Novapolis v1; TIMESTAMP: 2025-10-16_08:07).
 - Sidecar-Flag erstellt: `database-raw/99-exports/RAW-canvas-2025-10-16T08-07-00-000Z.flags.txt` (vorsichtig_behandeln; Grund: Namens-/ID-Drift – System „novapolis_logistik_v1“ vs. Schema `logistik_novapolis_v*`; Händlerkontakt „Senn Daru“ unbekannt; gegen Händlergilde-Kanon prüfen/normalisieren).
 - RAW-Canvas abgelegt: `database-raw/99-exports/RAW-canvas-2025-10-16T11-05-00-000Z.txt` (Quelle: Canvas; AI Behavior Index v2; TIMESTAMP: 2025-10-16_11:05).
 - Sidecar-Flag erstellt: `database-raw/99-exports/RAW-canvas-2025-10-16T11-05-00-000Z.flags.txt` (vorsichtig_behandeln; Grund: Globales Matrix‑Canvas – Versionsabgleich mit [BEHAVIOR-VERSION] und `ai_psymatrix_index_v1`; Modifikatoren-/Code‑Format vereinheitlichen, Mappings dokumentieren).
 - RAW-Canvas abgelegt: `database-raw/99-exports/RAW-canvas-2025-10-16T05-34-00-000Z.txt` (Quelle: Canvas; Ereignislog Weltgeschehen v1; TIMESTAMP: 2025-10-16_05:34).
 - Sidecar-Flag erstellt: `database-raw/99-exports/RAW-canvas-2025-10-16T05-34-00-000Z.flags.txt` (vorsichtig_behandeln; Grund: Timeline/Namensabgleich – H‑47 Identität offen; "Allianz" gegen [SECRECY]/[FR-KNOWLEDGE] prüfen; mit Missionslog/Sim‑Woche synchronisieren).
 - RAW-Canvas abgelegt: `database-raw/99-exports/RAW-canvas-2025-10-16T13-05-00-000Z.txt` (Quelle: Canvas; Logistik Novapolis v2; TIMESTAMP: 2025-10-16_13:05).
 - Sidecar-Flag erstellt: `database-raw/99-exports/RAW-canvas-2025-10-16T13-05-00-000Z.flags.txt` (vorsichtig_behandeln; Grund: Konsistenzprüfung Link-Graph v2; Curation vormerken).
 - RAW-Canvas abgelegt: `database-raw/99-exports/RAW-canvas-2025-10-16T12-55-00-000Z.txt` (Quelle: Canvas; Logistik C6 v2; TIMESTAMP: 2025-10-16_12:55).
 - Sidecar-Flag erstellt: `database-raw/99-exports/RAW-canvas-2025-10-16T12-55-00-000Z.flags.txt` (vorsichtig_behandeln; Grund: Verknüpfungen referenzieren `logistik_novapolis_v1` trotz v2; vor Promotion angleichen/begründen).
 - RAW-Canvas abgelegt: `database-raw/99-exports/RAW-canvas-2025-10-16T12-30-00-000Z.txt` (Quelle: Canvas; Inventar C6 v2; TIMESTAMP: 2025-10-16_12:30).
 - Sidecar-Flag erstellt: `database-raw/99-exports/RAW-canvas-2025-10-16T12-30-00-000Z.flags.txt` (vorsichtig_behandeln; Grund: Systemverknüpfungen referenzieren `logistik_novapolis_v1`; v2-Set angleichen oder begründen).
 - RAW-Canvas abgelegt: `database-raw/99-exports/RAW-canvas-2025-10-16T12-00-00-000Z.txt` (Quelle: Canvas; Station D5 – Basis (legacy)); TIMESTAMP: 2025-10-16_12:00).
 - Sidecar-Flag erstellt: `database-raw/99-exports/RAW-canvas-2025-10-16T12-00-00-000Z.flags.txt` (vorsichtig_behandeln; Grund: Legacy‑Snapshot; mit D5 v2.1/Kanon abgleichen, erst danach promoten).
 - RAW-Canvas abgelegt: `database-raw/99-exports/RAW-canvas-2025-10-16T14-12-00-000Z.txt` (Quelle: Canvas; Charakter Jonas v2; TIMESTAMP: 2025-10-16_14:12).
 - Sidecar-Flag erstellt: `database-raw/99-exports/RAW-canvas-2025-10-16T14-12-00-000Z.flags.txt` (vorsichtig_behandeln, korrupt; Grund: Konflikt mit Kanon [JONAS-SIS] – Schwester gilt als vermisst/unklar, nicht tot; bei Ingest normalisieren und Review-Hinweis setzen).
 - RAW-Canvas abgelegt: `database-raw/99-exports/RAW-canvas-2025-10-16T14-56-20-000Z.txt` (Quelle: Canvas; Charakter Arlen Dross v2; TIMESTAMP: 2025-10-16_14:56).
 - Sidecar-Flag erstellt: `database-raw/99-exports/RAW-canvas-2025-10-16T14-56-20-000Z.flags.txt` (vorsichtig_behandeln; Grund: Führungs-/Titel-Overlap mit Kora/Marven, vor Promotion klären).

# Done Log (Novapolis-RP)

**Hinweis (2025-10-29):** Dieses Done-Log liegt nun unter `novapolis-dev/docs/donelog.md`. Historische Einträge behalten Bezüge auf den "Development-Hub" inhaltlich bei, ohne die alten Pfadangaben.

2025-10-23
- Workspace-Struktur auf F:\Novapolis-RP erstellt (00-admin, 01-canon, 02-characters, 03-locations, 04-inventory, 05-projects, 06-scenes, 99-exports).
- README.md, todo.md, donelog.md angelegt.
- Memory-Bundle und System-Prompt vorbereitet (00-admin/).
- Erste Charakter-/Orts-/Projektdateien werden als Templates folgen.

2025-10-27
- Curation-Staging eingerichtet: `database-curated/` mit `staging/` und `final/`.
- Leitfäden und Manifest ergänzt (`database-curated/README.md`, `database-curated/staging/README.md`, `database-curated/staging/manifest.json`).
- Erste Datei zur Bearbeitung vorgemerkt: `database-raw/99-exports/chat-export (1).txt` (Status: pending).
- Audit-Tools hinzugefügt: `coding/tools/curation/text_stats.py`, `segment_hash.py`, `delta_report.py`.
- Reports erzeugt unter `database-curated/staging/reports/`:
  - `text-stats.md` (Zeilen/Bytes/Tokens)
  - `segment-hash-w5.txt` (5-Zeilen-Window Dupe-Hashes)
  - `delta-*.md` (Vergleiche zwischen Exportständen)
- Normalisierung & Chunking durchgeführt:
  - `database-curated/staging/chat-export (1).normalized.txt`
  - Re-Chunking: 500-Zeilen-Chunks (`database-curated/staging/chunks/chat-export (1)/chat-export (1).part-*.txt`, 22 Chunks)
  - `database-curated/staging/chunks/chat-export (1)/index.json`
  - Views: `database-curated/staging/recent-500.txt`, `recent-1000.txt`, Reverse-Chunks unter `.../reverse/`
  - Unklarheiten-Liste erstellt: `database-curated/staging/reports/uncertainties.md`
  - Kanon-Canvas (Draft) vorbereitet: `database-rp/00-admin/canon-canvas.draft.md` (vorläufig, kein Wiedereinstiegspunkt)

 - ToDo aktualisiert: JSONL als optional/pausiert markiert; TXT-Normalisierung + 500er-Chunks (Index/Views) vermerkt; Review-Aufgabe „part-021 annotieren“ ergänzt (`novapolis-dev/docs/todo.md`).
 - Review erweitert: Abschnitt für `Chunk part-021 (global 10001–10500)` mit [FACT?]/[OPEN] hinzugefügt in `database-curated/staging/chat-export (1).review.md`.
 - Unklarheiten mit Evidenz angereichert (Fraktionen, Layout/2t-Aufzug, Tunnel-Länge, Energie/Logistik-Verknüpfungen, Day-Switch, A/T/S/D, Draisine): `database-curated/staging/reports/uncertainties.md` aktualisiert.
 - Review weiter ergänzt: `Chunk part-020 (global 9501–10000)` ergänzt (Weekly‑Sim/Canvas‑Audit, Reflex‑Regeln, Anomalien) mit [FACT?]/[OPEN].
 - Unklarheiten erweitert: `database-curated/staging/reports/uncertainties.md` → [CARAVAN-LEADERSHIP].
 - Report hinzugefügt: `database-curated/staging/reports/overlap-arlen-dross.md` (Overlap-Check, Vorschlag Titel-Entzerrung: Arlen als Händler/Vermittler).

2025-10-27 (später)
- Admin‑Canvas angelegt: `database-rp/00-admin/Canvas-T+0-Timeline.md` (Tagesanker, Sequenz, Debug‑Hinweise, Links)
- Admin‑Canvas angelegt: `database-rp/00-admin/Canvas-Admin-Day-Switch-Debug.md` (Tageswechsel‑Prozedur, ATSD+Canvas‑Zahl, Logs, Testfälle)
- Cross‑Links ergänzt: `database-rp/03-locations/C6.md` ↔ `database-rp/00-admin/C6-Logistik-Policy.md`; Index‑Link in `00-admin/Logistik.md` ergänzt
- Missionslog aktualisiert: Abschnitt „Prozess L.1 – Missionsfluss“ mit Verweis zur C6‑Logistik‑Policy hinzugefügt
 - AI‑Behavior‑Mapping angelegt: `database-rp/00-admin/AI-Behavior-Mapping.md` (Zustände/Trigger/Interaktionen: Reflex + Hooks Ronja/Jonas; Links zu Charakter‑Canvas)
 - last-updated ergänzt: `novapolis-dev/docs/index.md`, `novapolis-dev/docs/todo.md` (ISO‑8601 mit Zeitzone)
 - Karawanen‑Canvas angelegt: `database-rp/05-projects/caravan_moves.md` (Zeitplan, Routen, Risiken, Abhängigkeiten, Links)
 - Fraktionsinventar‑Gerüste erstellt (Policy Y.1):
  - `database-rp/04-inventory/Novapolis-inventar.md`
  - `database-rp/04-inventory/Arkologie-inventar.md`
  - `database-rp/04-inventory/Schienenbund-inventar.md`
  - `database-rp/04-inventory/Eiserne-Enklave-inventar.md`
  - `database-rp/04-inventory/Haendlerbund-inventar.md`
  - `database-rp/04-inventory/Freie-Gruppen-inventar.md`
 - Personen aktualisiert (2025-10-27T16:58:26+01:00):
  - `database-rp/00-admin/person_index_np.md` – Einträge für Lyra Hest (Stellv. Leitung Zivil/Logistik) und Senn Daru (Händler/Vermittler) ergänzt; last-updated gesetzt.
  - `database-rp/02-characters/Lyra-Hest.md` neu angelegt (Rolle, Zugehörigkeit, Stärken, Notizen, Verlinkungen).
 - Korrektur (2025-10-27T17:02:55+01:00):
  - `database-rp/00-admin/person_index_np.md` – Jonas Merek Zugehörigkeit von C6 → D5 angepasst; Link auf D5 gesetzt; last-updated aktualisiert.

- Personen/Canvas aktualisiert (2025-10-27T17:11:18+01:00):
  - `database-rp/02-characters/Ronja-Kerschner.md` – Canvas umfassend ergänzt (Rollen, Zugehörigkeit/Standort, Wissensstand, Safety, Ziele, Beziehungen, Links); last-updated gesetzt; Cross-Links zu AI-Behavior-Mapping/Missionslog hinzugefügt. Grundlage: `database-curated/staging/reports/uncertainties.md` ([REFLEX-*], [FR-KNOWLEDGE], [JEALOUSY-GLOVES], [REFLEX-DETACH], [ROLES]).

- Behavior/Emotionen präzisiert (2025-10-27T17:32:08+01:00):

  - `database-rp/02-characters/Ronja-Kerschner.md` – Consent-Zeile geschärft (Angst→Schutz-Umhüllung möglich; „Stop“=sofort lösen; Rückfrage bei Unklarheit), last-updated aktualisiert.
  - `database-rp/00-admin/AI-Behavior-Mapping.md` – Leitplanke „Affekt-Gewichtung“ ergänzt (Kind-/Gefühlslogik ohne Regelbruch: Stop priorisiert, Training→Rückfrage).
  - `database-rp/02-characters/Reflex.md` – Abschnitt „Emotionale Dynamik (kanonisch)“ hinzugefügt (Beschützertrieb, Verlustangst/Eifersucht, Affekt-Gewichtung, Heuristik statt Regelwissen). Quellen: kuratierte Beschlüsse ([PROXIMITY], [JEALOUSY-GLOVES], [REFLEX-CONTROL]) + RAW-Chat-Passagen (Besitzergreifend/Schutz/Umhüllung, Exo-Idee, Instanz-Überwachung C6).

Behavior/Safety Klarstellungen (2025-10-27T17:55:04+01:00)
- `database-rp/02-characters/Ronja-Kerschner.md`: Consent-Gate erweitert um „Überreaktionen kurz/reversibel; danach Rückfrage/Regulation; Sprache priorisiert (außer unmittelbare Gefahr)“; kleiner „Signals“-Block (Request/Stop) ergänzt. RAW-Evidenz: Chat ~251 (Dämpfung testen), ~413 (Stufe I/Neopren), ~847 (gewünschte Kontrolle), ~3619–3624 (Coverage/Stop), ~3252 (Handschutz), ~2094/2428 (Instanz/Ort).
- `database-rp/02-characters/Reflex.md`: Fähigkeit „temporäre sensorische Reduktion (kurz; revert-on-stop)“ ergänzt; Abschnitt „Risiken/Leitplanken (Stufe I)“ mit Overreach-Flag (Hände/Gesicht) + Mitigation/Duration. RAW-Evidenz: Chat ~346/351 (Verlustangst/Verweigerung Lösen), ~3619–3624 (Kontrollüberhang/Stop), ~3252 (Hand/Face), Canvas: ent_d5_reflex_v1 (Stufe I, keine Penetration), char_reflex_v2 (Impulsdämpfung, autonome Reaktion).
- `database-rp/00-admin/AI-Behavior-Mapping.md`: Mikro-Protokolle ergänzt – EPP (Trigger/Aktion/Guardrails/Training-Hook) und „Jealousy-Gloves“ (Face-Coverage nur mit Consent, außer unmittelbare Gefahr). RAW-Evidenz wie oben; Canvas-Verweise: Reflex v2, ent_d5_reflex_v1.

Repo-Sync (2025-10-27T18:10:05+01:00)
- Commit `ffdbf61` gepusht: „chore: Admin/Location/Inventory-Updates + neue Canvases“.
- Umfang: 16 Dateien geändert (277 ⊕, 4 ⊖).
  - Neu: Admin-Canvases `database-rp/00-admin/Canvas-T+0-Timeline.md`, `database-rp/00-admin/Canvas-Admin-Day-Switch-Debug.md`.
  - Neu: Charakter `database-rp/02-characters/Lyra-Hest.md`.
  - Neu: Inventar-Übersichten `database-rp/04-inventory/*-inventar.md` (Novapolis, Arkologie, Schienenbund, Eiserne Enklave, Händlerbund, Freie Gruppen).
  - Neu: Projekte `database-rp/05-projects/caravan_moves.md`.
  - Updates: `novapolis-dev/docs/index.md`, `novapolis-dev/docs/todo.md`, Admin (`database-rp/00-admin/Logistik.md`, `.../Missionslog.md`, `.../person_index_np.md`), Location `database-rp/03-locations/C6.md`.
− Ergebnis: Branch up-to-date, Working Tree clean.

Stempel + Cross-Links (2025-10-27T18:13:52+01:00)
- Admin-Canvases auf ISO-Zeitstempel gebracht:
  - `database-rp/00-admin/Canvas-Admin-Day-Switch-Debug.md`
  - `database-rp/00-admin/Canvas-T+0-Timeline.md`
- `database-rp/00-admin/Logistik.md`: last-updated vereinheitlicht; Links zu Admin-Canvases (Day-Switch & Debug, Timeline T+0) ergänzt.
- `database-rp/02-characters/Lyra-Hest.md`: Front-Matter (`last-updated`) ergänzt; Cross-Links zu Logistik, Missionslog, Personenindex hinzugefügt.

Devcontainer & Lint-Task (2025-10-27)
- Altes Artefakt entfernt: `.devcontainer/devcontainer.json` (am Repo-Root).
- Neuer Devcontainer abgelegt unter `coding/devcontainer/`:
  - `coding/devcontainer/devcontainer.json` (Node 22; installiert `markdownlint-cli2`).
  - `coding/devcontainer/README.md` (Nutzung/ Hinweise).
 - VS Code Task hinzugefügt: `.vscode/tasks.json` → "lint:markdown (docker)" führt `markdownlint-cli2` in einem Node-Docker-Container aus (ohne lokale Node-Installation).
  Hinweis: `.vscode/tasks.json` ist per `.gitignore` (team-Policy) nicht versioniert; lokal nutzbar. Für geteilte Nutzung alternativ Devcontainer öffnen.

VS Code Settings – automatische Freigaben (2025-10-27)
- Workspace-Einstellungen ergänzt (`.vscode/settings.json`):
  - `task.allowAutomaticTasks: "on"` – automatische Tasks erlauben
  - `security.workspace.trust.untrustedFiles: "open"`, `security.workspace.trust.enabled: true` – weniger Blocker bei unbekannten Dateien (nur in vertrauenswürdigen Repos nutzen)
  - `remote.autoForwardPorts: true`, `remote.autoForwardPortsSource: "hybrid"` – Auto-Portforwarding (Remote/Container)
  - `extensions.autoCheckUpdates: true`, `extensions.autoUpdate: true` – Extension-Updates automatisch prüfen/installieren

Systemcheck-Task (2025-10-27)
- Werkzeug ergänzt: `coding/tools/diagnostics/systemcheck.ps1` – prüft Firmware-Virtualisierung, Windows-Features (VirtualMachinePlatform, WSL), WSL-Default-Version/Status sowie Docker-CLI. Ausgabe mit PASS/WARN/FAIL-Hinweisen; nur Diagnose, Exitcode 0.
- VS Code Task hinzugefügt: `.vscode/tasks.json` → "system:check (windows)" (führt das Skript via PowerShell mit `-ExecutionPolicy Bypass` aus).
- Follow-up notiert: Root-Artefakt `.devcontainer/devcontainer.json` ist wieder vorhanden; Entfernung in separatem Cleanup-Commit.

Validierung & CI (2025-10-27)
- Validator-Paket hinzugefügt: `coding/tools/validators/` (Node 20+, Ajv, fast-glob, gray-matter)
  - Skripte: `src/validate-curated.js` (Schema-Check Manifest), `src/validate-rp.js` (Markdown-Basisregeln), `src/check-crossrefs.js` (Szenen↔Chars/Orte/Inventar), `src/validate-all.js` (Aggregator)
  - Schema: `schemas/curated-manifest.schema.json`
- CI aktualisiert: `.github/workflows/validate.yml` installiert Dependencies und führt `npm --prefix coding/tools/validators run validate` aus; anschließend Markdown-Lint.
- VS Code Task ergänzt: `.vscode/tasks.json` → `validate:data (auto)` (Docker bevorzugt, sonst lokal npm) für einheitliche lokale Ausführung.
- Hinweis/README: `coding/tools/validators/README.md` mit Nutzung und empfohlener Szenen-Front-Matter.

Benennung vereinheitlichen (2025-10-27)
- Policy erstellt: `novapolis-dev/docs/naming-policy.md` (ASCII, Bindestrich-Trennung, Umlaute → ae/oe/ue/ss, Endungen klein, keine Leerzeichen/Klammern).
- Name-Linter hinzugefügt: `coding/tools/validators/src/check-names.js` (Scope: `database-rp/**`).
- CI erweitert: Name-Check als zusätzlicher Step in `.github/workflows/validate.yml` (Dry-Run, bricht bei Verstößen ab).
- VS Code Task: `lint:names (auto)` zum lokalen Dry-Run (Docker bevorzugt; alternativ Node/npm).
 - Dry-Run ausgeführt: 0 Verstöße in `database-rp/**` – keine Umbenennungen erforderlich.

Co-Occurrence-Regel (2025-10-27)
- Validator erweitert: `coding/tools/validators/src/check-crossrefs.js` prüft jetzt Bezugspaare in Szenen:
  - Ronja-Kerschner → Reflex
  - Jonas-Merek → Lumen
  - Kora-Malenkov → Echo
- Szenen-Leitfaden aktualisiert: `database-rp/06-scenes/README.md` mit Abschnitt "Co-Occurrence (Bezugspaare)".
- Szene aktualisiert: `database-rp/06-scenes/scene-2025-10-27-a.md` → `characters` um „Lumen“ ergänzt (wegen Jonas→Lumen).
- Charakter-Stubs hinzugefügt: `database-rp/02-characters/Lumen.md`, `.../Kora-Malenkov.md`, `.../Echo.md` (Minimalinhalt, Cross-Links).

Charakter-Canvas vereinheitlicht (2025-10-27)
- Vorlage: `database-rp/02-characters/Ronja-Kerschner.md` als Strukturvorbild (Meta/Rollen/Zugehörigkeit/Wissensstand/Safety/Ziele/Beziehungen/Links)
- Überarbeitet:
  - `database-rp/02-characters/Jonas-Merek.md` – Struktur nach Vorlage; Inhalte/Platzhalter ergänzt
  - `database-rp/02-characters/Lumen.md` – Instanz-spezifische Struktur (Kopplung an Jonas)
  - `database-rp/02-characters/Kora-Malenkov.md` – Leitung C6, Kopplung Echo
  - `database-rp/02-characters/Echo.md` – Instanz-spezifische Struktur (Kopplung an Kora)
  - `database-rp/02-characters/Reflex.md` – Zugehörigkeit/Ziele/Beziehungen/Links ergänzt
  - `database-rp/02-characters/Lyra-Hest.md` – Sektionen/Platzhalter ergänzt
  - `database-rp/02-characters/Senn-Daru.md` – Sektionen/Platzhalter ergänzt

Reflex – Guards & Wissens-/Trainings-Canvases (2025-10-28)
  - `02-characters/Reflex.md`: Meta aktualisiert; Guards unter Kokon/Overreach ergänzt (Lebensgefahr + dynamisches Ausmaß/Dauer; weitere Aspekte werden erlernt).
  - Wissens-/Trainings-Status ausgelagert:
    - `02-characters/Reflex-Wissensstand-Trainingsstand.md`
    - `02-characters/Lumen-Wissensstand-Trainingsstand.md`
    - `02-characters/Echo-Wissensstand-Trainingsstand.md`

Hybrid-Metadaten angereichert (2025-10-28)
- Tool hinzugefügt: `coding/tools/metadata/enrich_metadata.py` (füllt fehlende Felder aus Front-Matter/H1; nicht-destruktiv, Markdown bleibt unverändert).
- Task ergänzt: `.vscode/tasks.json` → `gpt:enrich:metadata` (läuft über `with_lock.ps1`, bevorzugt `.venv`-Python).
- Sidecar-JSON aktualisiert: 241 Dateien angereichert (chapter/characters/locations/tags); zentrale Index-Logik unverändert (append-only).

YAML-Front-Matter Schema & Validator (2025-10-28T18:30:00+01:00)
- Enricher erweitert: YAML-Front-Matter zwischen `---` wird gelesen; JSON-Schema vereinheitlicht (`title/category/slug/version/last_updated/last_change/tags/affiliations/locations/dependencies[/characters]/source`). Legacy-Felder (`chapter`, singulares `location`) werden migriert/entfernt.
- Validator hinzugefügt: `coding/tools/metadata/validate_frontmatter.py` (Pflichtfelder, Kategorie-Spezifika, Slug-Format, ISO-Zeit, Referenzen per Slug). Task: `.vscode/tasks.json` → `gpt:validate:frontmatter`.

Tagging-Pipeline (YAML-getrieben) – erster Lauf (2025-10-28T09:59:20Z)

- Neues Tool: `coding/tools/curation/tag_chunks_from_yaml.py` (lexicon aus Front-Matter; Aliase; line-level Tags [CHAR|LOC|PROJ|ENT], [TIME], [FACT?]; Streaming; Windows-Pfad-safe; optional PyYAML Fallback).
- Ausführung (dry-run): Range 019–016 – Summaries geprüft; Aliase/Slugs validiert; Dateinamensschema `*.part-XYZ.txt` automatisch erkannt.
- Ausführung (write): Ergebnisse unter `database-curated/reviewed/chat-export (1)/` erzeugt:
  - `part-019.tagged.txt`, `part-018.tagged.txt`, `part-017.tagged.txt`, `part-016.tagged.txt`
  - `index_review.json` (per-File Lines/Chars/Tag-Counts/Top-Slugs)
  - `unresolved.json` (Dependencies: echo, reflex-wissensstand-trainingsstand; alias collisions: none)
  - `lexicon.json` (by_slug + aliases Dump)
  - Warnings: `reports/tagging-20251028T095920Z.log` (LOC-only-Hinweise; non-blocking)
- Nächste Schritte: ggf. Alias-Ergänzungen, dann Ranges 015–010 und 009–001 taggen.

Tagging-Pipeline – Heuristiken erweitert + Re-Run 019–016 (2025-10-28T11:10:05Z)

- Ergänzt: N7→c6-nord Kanonisierung (metro-kontextsensitiv, ±3 Zeilen Fenster; Redirects/Deprecated im Lexikon).
- Ergänzt: [NOTE] für Meta-Zeilen (Warnungen für LOC-only unterdrückt), [EVENT] konservativ, [MISSION] Kategorie (C6-Nord, versiegelt/gesperrt/Untersuchung im ±3-Zeilen-Fenster).
- Ergänzt: Sektor-Codes (E3/F1/…) als Fallback-Orte, Titel-Alias-Erweiterung (Vor-/Nachname), Co-Occurrence-Vorschläge (Report-only).
- Retag-Modus: `--retag-in`/`--retag-out` (nur a/b/c Regeln; idempotent).
- Ausführung: 019–016 neu getaggt; `index_review.json`, `unresolved.json`, `lexicon.json` aktualisiert. Logs: `reports/tagging-20251028T111005Z.log` inkl. "Canonicalized N7→c6-nord total: 1".
- Folgearbeiten: Alias-Kollision "C6" (c6 vs c6-nord) entscheiden; fehlende Entities (`Echo`, `Reflex-Wissensstand-Trainingsstand`) anlegen/umbiegen; nächste Ranges 015–010, 009–001.

Sim-Visualisierung angebunden (2025-10-29T15:50:00Z)

- `novapolis_agent`: FastAPI-Miniserver `app/api/sim.py` ergänzt (`GET /world/state`, `POST /world/step`), Task/Launch für Uvicorn, pytest-Abdeckung (`tests/tests_sim_api.py`).
- `novapolis-sim`: Godot-4-Mini-Client (Autoload `SimClient`, Szene `Main.tscn`) pollt die API und zeigt Tick/Zeit inkl. Status bei Offline-Agent.
- `novapolis-rp`: README-Abschnitt „Visualisierung“ ergänzt; Donelog/TODO synchronisiert.
