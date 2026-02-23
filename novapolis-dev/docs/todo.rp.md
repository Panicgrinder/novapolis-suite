---
title: "TODO (Novapolis-RP)"
date: 2025-11-12 08:59
tags: [doc]
stand: 2026-02-23 00:48
update: DoD-Punkt Stationsreferenzen (Karte+Kontrollmatrix) auf 54/54 geschlossen.
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-dev/docs/todo.rp.md' 'novapolis-dev/docs/todo.index.md' 'novapolis-dev/docs/donelog.md' 'novapolis-rp/database-rp/00-admin/Fraktionen-Taxonomie.md' 'novapolis-rp/database-rp/00-admin/Stationskontroll-Matrix.md' PASS (2026-02-23 00:48); .\\.venv\\Scripts\\python.exe scripts\\check_frontmatter.py 'novapolis-dev/docs/todo.rp.md' 'novapolis-dev/docs/todo.index.md' 'novapolis-dev/docs/donelog.md' 'novapolis-rp/database-rp/00-admin/Fraktionen-Taxonomie.md' 'novapolis-rp/database-rp/00-admin/Stationskontroll-Matrix.md' PASS (2026-02-23 00:48)
---
<!-- markdownlint-disable MD012 MD022 MD041 -->
TODO (Novapolis-RP)
-------------------

<!-- Migration: Quelle aus dem frueheren coding-Hub, uebernommen am 2025-10-29 -->
<!-- Relocated aus dem ehemaligen Novapolis-RP Development-Hub nach `novapolis-dev/docs/todo.rp.md` am 2025-10-29 -->

Canvas-Rettung - Sprint 1 (Stand 2025-11-01)
--------------------------------------------
Archiv-Hinweis (manuell, bis Validator bereit)
----------------------------------------------

- Sobald ein Abschnitt (H2/H3) vollständig abgehakt ist ([x] überall) und - für RP - kanonisiert, bitte den gesamten Block manuell nach `novapolis-dev/archive/todo.<modul>.archive.md` verschieben (neuester oben).
- Direkt unter der Abschnitts-Überschrift im Archiv eine Zeile ergänzen: `archived_at: YYYY-MM-DD HH:MM`.
- Automatisierung folgt erst nach Struktur-Review/Validator (Dry-Run only). Keine halb fertigen Blöcke verschieben.

Plan Charakter-Review (laufend)
-------------------------------

Reihenfolge
-----------

- Ronja Kerschner → Abgleich `resolved.md`, RAW `char_ronja_v2` + Flag, Rollenmatrix, Ziele, Systemverknüpfungen, Drift-Notizen. *(erledigt 2025-11-01T17:10+01:00)*
- Jonas Merek → RAW `RAW-canvas-2025-10-16T14-12-00-000Z.*`, Schwesterstatus gemäß `[FACT][JONAS-SIS]`, Werkstatt-/Tunnelinfos konsolidieren. *(erledigt 2025-11-02T13:55+01:00)*
- Lumen → Jonas-Quellen + `[FACT][PROXIMITY]`, Fähigkeiten/Kopplung und Trainings-Canvas aktualisieren. *(validiert erledigt 2026-02-21)*
- Kora Malenkov → RAW `RAW-canvas-2025-10-16T14-56-00-000Z.txt`, paranoide Vorsicht, C6-Linienstatus (FACT `C6-LINES`), Echo-Interaktion. *(erledigt 2025-11-02T14:20+01:00)*
- Senn Daru → Relationslog `RAW-canvas-2025-10-16T08-07-00-000Z.*`, Handels-/Diplomatie-Notizen, Wissensgrenzen. *(validiert erledigt 2026-02-21)*
- Marven Kael → RAW `RAW-canvas-2025-10-16T14-56-10-000Z.*`, Konvoi-/Handelsleitung (`[FACT][CARAVAN-LEADERSHIP]`), Beziehungen Händlergilde/Novapolis. *(erledigt 2025-11-02T14:45+01:00)*
- Arlen Dross → RAW `RAW-canvas-2025-10-16T14-56-20-000Z.*`, Vermittlerrolle, Reflex-Einschätzung. *(erledigt 2025-11-02T15:05+01:00)*
- Pahl → RAW `RAW-canvas-2025-10-16T14-41-00-000Z.*`, Gesundheitsstatus, Risiken, Energie-/Generatorwissen. *(erledigt 2025-11-02T15:25+01:00)*
- Reflex (Primärinstanz) → RAW `char_reflex_v2`, FACTs `[REFLEX-*]` (Frequenzband, Detach, Speech), Wissens-/Trainings-Canvas synchronisieren. *(erledigt 2025-11-02T16:05+01:00)*

Arbeitsschritte pro Charakter
-----------------------------

- Quellen sammeln: `database-curated/staging/reports/resolved.md`, `.../uncertainties.md`, zugehörige RAW-/Flag-Dateien, overlap-Reports.
- Canvas aktualisieren (Werte, Skills, Motivation, Wissensmatrix, Beziehungen, Ziele, Risiken) und Systemverknüpfungen prüfen.
- Zugehörige Wissens-/Trainings-Canvases mitziehen (Instanzen).
- Behavior-Signatur gegen Anchor-Register prüfen; Drift-Flags dokumentieren.
- JSON-Sidecar, `char-block-nord-sources.md`, `person-index-np.md`, DONELOGs (`novapolis-dev/docs/donelog.md`, Root `DONELOG.md`) und TODO-Status aktualisieren.
- Nach einem Bündel Updates Validator laufen lassen (`npm --prefix novapolis-rp/coding/tools/validators run validate:rp` + optional `npm --prefix ... run validate:crossrefs`).

Archivstatus (2026-02-22)
-------------------------

- Vollständig erledigte Blöcke `Aktiv jetzt (sicher)`, `Priorität B - Logistik & Inventar` und `Priorität C - Systeme, Indizes, Ereignisse` wurden nach `novapolis-dev/archive/todo.rp.archive.md` verschoben.

Arbeitsregeln & Referenzen
--------------------------

- Workflow siehe `novapolis-dev/docs/process/rp-canvas-rescue/canvas-rescue-plan.md`.
- Quellen + Drift-Notizen in `novapolis-dev/docs/process/rp-canvas-rescue/char-block-nord-sources.md` berücksichtigen.
- FACT-Beschlüsse aus `novapolis-dev/docs/process/rp-canvas-rescue/resolved.md` vor Promotion prüfen.
- Jede Migration mit JSON-Sidecar und DONELOG-Eintrag dokumentieren (`novapolis-dev/docs/donelog.md`).
- Flags (`vorsichtig_behandeln`, `korrupt`) sichtbar übernehmen, bis Review abgeschlossen ist.

Linkübersicht
-------------

- Plan: `novapolis-dev/docs/process/rp-canvas-rescue/canvas-rescue-plan.md`
- Quellen: `novapolis-dev/docs/process/rp-canvas-rescue/char-block-nord-sources.md`
- RAW: `database-raw/99-exports/`
- Kanon/Policies: `novapolis-dev/docs/process/rp-canvas-rescue/resolved.md`, `.github/copilot-instructions.md`

<details>
<summary>Archiviertes Backlog (ausgelagert)</summary>

- Volltext ausgelagert nach `novapolis-dev/archive/todo.rp.historical-backlog.md`.
- Inhalt bleibt historisch/nicht aktiv; Reaktivierung nur per explizitem Soll-Ist-Abgleich gegen aktuelle SSOT-Dateien.

</details>
Neue Aufgaben - Zeitmodell, Annotation & Logs (2025-11-01 22:24)
----------------------------------------------------------------

Prioritaet 0 - Gesamtbild T0 (vor Detailmengen)
-----------------------------------------------

Ziel
----

- Zuerst ein belastbares Gesamtbild aufbauen (Karte, Kontrolle, Warenlage), danach Detailmengen pro Station schrittweise nachziehen.
- Keine neuen unbelegten Canon-Behauptungen; unbekannte Punkte bleiben explizit `tbd`/`unklar`.

Umsetzungsreihenfolge (MVP)
---------------------------

- [x] P0.1 Metro-Topologie als Arbeitskarte T0 anlegen (Stationen, Verbindungen, Status pro Knoten/Kante).
- [x] P0.2 Stationskontrolle je Fraktion erfassen (gesichert/umkaempft/verlassen/unklar + Confidence).
- [x] P0.3 Warenueberblick T0 je Fraktion/Station als Bandbreitenmodell erfassen (`none|low|medium|high` statt Scheingenauigkeit).
- [x] P0.4 Herkunftslabel pro Warenposten verpflichtend setzen (`legacy|evac_e3|scavenged|produced|unknown`).
- [x] P0.5 D5/C6 sauber als fruehe Aufbauphase markieren (kein etablierter Handel; Bestand nur aus Altbestand/Funden/E3-Mitnahme).
  - Evidenz: `novapolis-rp/database-rp/00-admin/Metrokarte-T0.md`, `novapolis-rp/database-rp/00-admin/Stationskontroll-Matrix.md`, `novapolis-rp/database-rp/00-admin/Warenueberblick-T0.md`.

Scope-Guardrails
----------------

- [x] D5/C6: Keine Handelsnormalisierung simulieren, solange Handelsbeziehungen im RP noch nicht etabliert sind.
- [x] Etablierte Fraktionen: Grundvorräte zulassen, aber Stationenlage explizit als unvollstaendig kennzeichnen.
- [x] Mengenpraezision erst nach P0.1-P0.4 erhoehen; bis dahin nur Bandbreiten + Quellenanker.

Konkrete Deliverables
---------------------

- [x] Admin: Metrokarte-T0 (Knoten/Kanten + Statusmodell) unter `00-admin`.
- [x] Admin: Fraktionskontroll-Matrix Stationen (Fraktion x Station x Status x Confidence).
- [x] Admin: Warenueberblick-T0 (globales Raster + Herkunftssystem).
- [x] Fraktionen: Minimal-Abgleich je Basis/known stations mit Verweis auf Admin-SSOT. *(erledigt 2026-02-23)*
  - Evidenz: `novapolis-rp/database-rp/00-admin/Fraktionen-Taxonomie.md` (Abschnitt „Minimal-Abgleich Basis-/Known-Stationen (T0)“) mit Referenzen auf `Metrokarte-T0`, `Stationskontroll-Matrix`, `Warenueberblick-T0`.

Definition of Done (P0)
-----------------------

- [x] Jede bekannte Station ist in Karte + Kontrollmatrix mindestens einmal referenziert. *(erledigt 2026-02-23)*
  - Evidenz: `novapolis-rp/database-rp/00-admin/Stationskontroll-Matrix.md` enthält jetzt alle in `novapolis-rp/database-rp/00-admin/Metrokarte-T0.md` geführten Stationscodes (Abdeckung 54/54).
- [ ] Jede Fraktion hat einen T0-Warenueberblick mit Herkunftslabeln.
- [ ] D5/C6 sind konsistent als fruehe Aufbauphase modelliert; keine impliziten Handelsannahmen.
- [ ] Danach erst Mengen-Backfill in Inventaren (D5/C6/Fraktionen) starten.

- 24×1h-Runden (PC-zentriert) einführen
  - [x] Policy festhalten: Stunde spult leise weiter, bis ein PC-relevantes Ereignis eintritt (z. B. „Reflex weckt Ronja“). *(erledigt 2026-02-22)*
  - [x] Pro Stunde zwei Logs führen: `world_log` (Wahrheit) und `pc_log` (nur Sichtbares für den PC). *(erledigt 2026-02-22)*
  - [x] Sichtbarkeit umsetzen: scope `private|allies_only|pc|public`, plus `channel`, `source`, `confidence`, `freshness` (siehe Knowledge-Schema unten). *(erledigt 2026-02-22)*
  - [x] Referenz: `novapolis-dev/docs/specs/annotation-spec.md` vorhanden und weiterhin passend zum 24×1h-Vorgehen. *(validiert 2026-02-22)*

- Knowledge-Annotation schrittweise ergänzen (wichtige Charaktere/Missionen zuerst)
  - [x] Charaktere: Reflex, Ronja, Jonas - Knowledge-Einträge in dedizierten Dateien (z. B. `Reflex-Wissensstand-Trainingsstand.md`) und/oder Canvas-Frontmatter `knowledge:`. *(umgesetzt 2026-02-22)*
  - [x] Missionen/Ereignisse: je Kernereignis mind. ein Knowledge-Item mit `about`, `channel`, `source`, `scope`, `confidence`, `freshness`, `visibility_to`, `attachments`. *(umgesetzt 2026-02-22)*
  - [x] Rückblendenprozess: Items per Log/Funk von `allies_only/hidden` → `pc` heben (keine Retcons, nur Sichtbarkeit). *(umgesetzt 2026-02-22)*
  - [x] Referenz: `novapolis-dev/docs/specs/annotation-spec.md` vorhanden und weiterhin passend. *(validiert 2026-02-22)*

- Actions-Schema (für möglichen „Zug-um-Zug“-Wechsel) jetzt leicht mitpflegen
  - [x] In Missions-/Orts-Canvases `actions:` notieren: `verb`, `base_duration_min`, `effort`, `interruptible`, `locks`, `may_trigger_event`, `resources`. *(umgesetzt 2026-02-22)*
  - [x] Kernaktionen definieren (5-10): Reinigen, Reparatur, Reise, Wache, Funk, Erste Hilfe, Erkundung. *(umgesetzt 2026-02-22)*
  - [x] Naming-Konvention und kurze Beispiele dokumentieren. *(durch Spec vorhanden; validiert 2026-02-22)*
  - [x] Referenz: `novapolis-dev/docs/specs/annotation-spec.md` vorhanden und weiterhin passend. *(validiert 2026-02-22)*

- Skills aus Verhaltensmatrix ableiten (ohne zweites System)
  - [ ] Mapping-Gewichte je Skill (0-3) vorschlagen (Matrix-Dimensionen → Skill), Ausgangswerte pro Rolle.
  - [ ] Formel/Beispiele im Spec verlinken; Ableitung on-demand, keine Duplikat-Wahrheit.

- TTS (gemischt)
  - [ ] Vorproduzierte OGG-Summaries je Stunde (world/pc) - Kandidaten markieren.
  - [ ] Live-Dialoge via Coqui XTTS v2 mit Cache (Hash(Text+Stimme)); Fallback Windows/Azure nur bei Bedarf.




