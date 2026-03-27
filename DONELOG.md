---
stand: 2026-03-27 09:54
update: Folgebacklog nach dem Wochenabschluss auf Root-/Dev-Ebene konkretisiert; offene Restarbeit ist wieder explizit benannt.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260327_011507.md
---

DONELOG (Root Summary)
======================

Hinweis
-------

- Diese Datei ist der Root-Summary-/Release-Log (kurz und scanbar).
- Detailhistorie liegt unter `novapolis-dev/archive/docs/donelogs/donelog_root.md`.
- Technische Laufdetails liegen in Reports unter `.tmp/results/reports/`.

Aktuelle Eintraege (Summary)
----------------------------

- 2026-03-27 04:34: Offene Folgearbeit nach dem Wochenabschluss konkretisiert. Das Root-/Dev-Backlog fuehrt jetzt drei klare Restspuren: RP-Transferkette plus Delta-Struktur fuer den Inventar-Backfill, die bekannten Sim-Asset-Warnungen als echten Board-Punkt und den sichtbaren Metadaten-Drift in `novapolis-dev/docs/todo.index.md`.

- 2026-03-27 01:16: Wochenabschluss gemaess SSOT komplett abgeschlossen. `scripts/run_checks_and_report.py` ist wieder voll gruen (`overall=PASS`, Coverage `93.69%`), der separate Coverage-Lauf endet mit Exit `0`, und die Hygiene-KPIs liegen nach Refresh der beiden stale Boards (`novapolis-dev/docs/todo.agent-board.md`, `novapolis-dev/docs/todo.sim.md`) wieder bei `0`. Der Sim-Asset-Check bleibt ohne harte Fehler (`summary=fail:0,warn:2`).

- 2026-03-18 22:47: O11 geschlossen. Das neue Installblatt `novapolis-dev/docs/process/standalone-beta-installblatt.md` beschreibt den externen Setup-/Run-/Verify-Pfad fuer die Standalone-Beta; `README.md`, `todo.root.md`, `novapolis-dev/docs/todo.dev.md` und `novapolis-dev/docs/todo.index.md` sind auf diesen Stand synchronisiert.

- 2026-03-18 22:40: Community-/Maintainer-Paket abgeschlossen. `SUPPORT.md`, `RELEASE.md`, `MAINTAINERS.md`, Root-Issue-Templates und ein PR-Template wurden angelegt; `README.md`, `novapolis-dev/docs/todo.dev.md` und `novapolis-dev/docs/todo.index.md` sind darauf synchronisiert, der Dev-Open-Count liegt nun bei `2`.

- 2026-03-18 22:36: ADR-Aktivierung abgeschlossen. Unter `docs/adr/` liegen jetzt `0001-donelog-ebenen.md` und `0002-quality-gate-sequenz.md` als akzeptierte Grundsatzentscheidungen; parallel wurden `docs/adr/README.md`, `novapolis-dev/docs/todo.dev.md` und `novapolis-dev/docs/todo.index.md` auf den neuen Iststand synchronisiert.

- 2026-03-18 22:20: Dokumentations-Sync fuer den aktuellen Arbeitsstand eingezogen. `WORKSPACE_STATUS.md`, `todo.root.md`, `novapolis-dev/docs/todo.dev.md` und `novapolis-dev/docs/todo.index.md` spiegeln jetzt den dokumentierten PASS-Lauf `checks_report_20260318_052318.md`; der Dev-Coverage-Sprint wurde evidenzbasiert mit `93.69%` als erreicht abgeschlossen und der Dev-Open-Count auf `4` reduziert.

- 2026-03-18 05:20: Integritaets-Hygiene nachgezogen. Das veraltete RP-Brainstorming wurde aus `novapolis-dev/docs/` sauber nach `novapolis-dev/archive/docs/others/brainstorming.rp.archive.2026-03-18.md` ueberfuehrt, der Active-Surface-Index bereinigt und die zugehoerige Mind-Cluster-Instruction vom toten Aktivpfad geloest. Parallel wurde ein echter Ruff-Blocker im Agent-Test `novapolis_agent/tests/test_chat_additional_branches.py` korrigiert und die gemeldete Formatdrift in den acht betroffenen Testdateien per gezieltem Ruff/Black-Lauf bereinigt.

- 2026-03-11 11:53: Gemeldeten Parse-Error `Identifier "_on_api_card_panel_gui_input" not declared` behoben. In `novapolis-sim/scripts/Main.gd` wurde die Signalbindung auf explizites `Callable(self, "_on_api_card_panel_gui_input")` umgestellt, wodurch der Callback parser-sicher aufgeloest wird.
- 2026-03-11 11:50: Freigegebene Umstellung fuer Punkt 3 umgesetzt: ein unteres Feld zeigt drei Themenbloecke manuell durchschaltbar statt parallel. In `novapolis-sim/scripts/Main.gd` wurde `api_card_panel` als Shared-Detailfeld mit Klick-Zyklus implementiert (`Agent/API` -> `Runtime/Ops` -> `Eval/Quality` -> ...). Headertext zeigt aktiv: `Thema: ... (Klick: wechseln)`.
- 2026-03-11 11:39: Ausrichtung aller vier oberen Bereiche geprueft; gezielter Fix in Bereich-01 (linker Textblock) umgesetzt. Evidenz aus Bild: `Slot`, `Audio`, `Epoch` wirkten vertikal uneinheitlich, `Epoch` hing sichtbar zu tief. `novapolis-sim/scripts/Main.gd` (`_apply_editor_hub_layout`) nutzt dort jetzt ein sauberes Zeilenraster (`line_h` + `line_gap`) fuer `HubTitle/API/Slot/Audio/Epoch`, wodurch die Inhalte gleichmaessig und kantenparallel sitzen. Bereiche 02-04 wurden geprueft und auf den zuvor synchronisierten pixelgenauen Flaechenwerten belassen.
- 2026-03-11 11:36: Nutzeranpassung uebernommen: pixelgenaue Positionen der vier oberen Flaechen (`bereich-01..04`) aus `novapolis-sim/Main.tscn` in `novapolis-sim/scripts/Main.gd` (`_apply_editor_hub_layout`) synchronisiert. Uebernommene Werte: Bereich-01 `98/117/497/231`, Bereich-02 `520/116/902/229`, Bereich-03 `1018/117/1399/230`, Bereich-04 `1424/116/1821/228`.
- 2026-03-11 11:33: Screenshot-Teilausschnitt weiter verfeinert (`Epoch: --` / `Epochen: ...`). Evidenz aus Bild: rechter Epochen-Text war weiterhin zu eng eingepasst. Fix in `novapolis-sim/scripts/Main.gd` (`_apply_editor_hub_layout`): feste Breite von `epoch_label` reduziert (`220 -> 110`) und Start von `epoch_status_label` entsprechend nach links gezogen (`224 -> 114`), damit die Statuszeile sichtbar mehr Lauflaenge im Panel bekommt.
- 2026-03-11 11:29: Screenshot-Teilausschnitt mit Nutzerwunsch umgesetzt. Evidenz aus Bild: links lagen `Epoch: --` und die darueberliegenden Zeilen visuell zu tief; zusaetzlich sollten die Flaechen voll durchsichtig werden. Fix in `novapolis-sim/scripts/Main.gd`: vertikale Offsets fuer den linken Stack (`HubTitleLabel`, `HubApiLabel`, `SlotLabel`, `AudioStatusLabel`, `EpochLabel`, `EpochStatusLabel`) im Editor-Hub-Layout nach oben/kompakter gesetzt. Fix in `novapolis-sim/Main.tscn`: `bereich-01..04` jeweils `modulate = Color(1, 1, 1, 0)` fuer komplette Transparenz.
- 2026-03-11 11:24: Neuer Screenshot-Teilausschnitt (linker Hub-Bereich) fokussiert. Evidenz aus Bild: `Epochen: keine Daten unter res://data/epochs` lief horizontal ueber den Kasten hinaus in Richtung Mitte (`Run Checks`). Fix in `novapolis-sim/scripts/Main.gd`: alle Schreibpfade von `epoch_status_label` auf `_set_marquee_text(...)` umgestellt (`_load_epochs`), damit lange Epochenmeldungen innerhalb der Labelbreite bleiben und kontrolliert scrollen.
- 2026-03-11 11:19: Screenshot-Teilausschnitt (Hub-Top links) verbessert. Evidenz aus Bild: API-Zeile begann teils mit fuehrendem `|` und zeigte gekuerzten `reason` mit offener Klammer (`...Verbindungsproblem (`). Fix in `novapolis-sim/scripts/Main.gd`: Marquee-Separator von `"   |   "` auf reine Leerzeichen umgestellt und `_compact_reason_text()` so erweitert, dass abgeschnittene Endzeichen wie `(`, `[`, `{`, `|`, `-`, `,`, `;`, `:` vor dem `...` entfernt werden.
- 2026-03-11 11:15: Warnungsbereinigung mit Screenshot-Evidenz umgesetzt. Belegt waren: (1) `area_03_bottom` deklariert, aber ungenutzt, (2) Variable `abs` kollidiert mit Built-in (2x), (3) lokale Variable `reason` deklariert, aber ungenutzt. Fix in `novapolis-sim/scripts/Main.gd`: `_area_03_bottom`, `_reason` und Umbenennung `abs -> abs_path` an beiden Fundstellen.
- 2026-03-11 11:12: Laufzeitfehler aus Godot-Debugger behoben (`Main.gd:4306`, `_refresh_agent_studio_ui`): `full_status_text` hatte 16 `%s`-Platzhalter bei 17 Argumenten. Ein zusaetzlicher `%s`-Platzhalter wurde ergaenzt, damit die String-Formatierung wieder konsistent ist.
- 2026-03-11 11:04: Folgefix fuer Godot Parse-Error an `Main.gd:977`: `var max_chars := min(...)` auf strikt typisierte int-Variante umgestellt (`var max_chars: int = mini(...)`), damit keine Variant-Inferenz mehr entsteht.
- 2026-03-11 11:02: Parse-Fehler in `novapolis-sim/scripts/Main.gd` behoben (`line 977`): `entry` im Marquee-State wird explizit als `Dictionary` typisiert (`as Dictionary`), damit bei aktivem "warnings as errors" kein Variant-Infer-Fehler mehr ausgeloest wird.
- 2026-03-11 10:52: Marquee-Mechanik in `novapolis-sim/scripts/Main.gd` eingefuehrt (`_set_marquee_text` + Helper), aktiv fuer `HubApiLabel`, `HubPollingLabel`, `HubQueueLabel`, `HubErrorsLabel` und `HubConfigStatusLabel`. Ueberlange Texte werden jetzt horizontal durchlaufen statt hart abgeschnitten.
- 2026-03-11 10:48: Nächster Screenshot-Teilabschnitt gefixt: `HubConfigStatusLabel` in `Main.tscn` auf `top=92/bottom=113` gesetzt (kein Bottom-Bleed mehr), und in `_apply_editor_hub_layout` (`Main.gd`) die Statuszeilenhoehe/-abstaende reduziert (`16/2`, Server-Row-Shift `32`), sodass `Tick/Zeit` wieder im oberen Statusbereich bleiben.
- 2026-03-11 10:44: Ueberlagerungen im Sim-Hub behoben: `status_label` bekommt in beiden Layoutpfaden feste Begrenzung, `StatusLabel`/`ServerStatusLabel` clippen Text in `Main.tscn`, und die Server-Kopfzeile wurde auf `Server: <state>` reduziert, damit lange Reason-Texte nicht mehr in Nachbarbereiche laufen.
- 2026-03-11 10:38: Sim-Hub-Layout nachgezogen: `novapolis-sim/scripts/Main.gd` (Funktion `_apply_editor_hub_layout`) auf die in `novapolis-sim/Main.tscn` vorbereiteten Rahmenkoordinaten synchronisiert. Damit werden die neuen Fensterpositionen auch bei aktiver Runtime-Layoutlogik nicht mehr auf alte Werte zurueckgesetzt.
- 2026-03-11 07:24: Punkt 1 geschlossen: Full-Gate wieder gruen (`overall=PASS`). Parallel Start des 91%-Coverage-Sprints mit erstem messbaren Uplift (`76.24% -> 80.45%`) durch gezielten Testausbau im Agent-Script-Scope.
- 2026-03-11 07:07: Auf User-Freigabe mit Punkt 3 gestartet. Dev-Teststrategie auf moderne Coverage-Governance umgestellt und 90%-Qualitaetsziel verbindlich verankert (`novapolis-dev/docs/tests.md`, `novapolis-dev/docs/process/abschluss-routine.ssot.md`).
- 2026-03-11 06:57: Neuer Dev-Optimierungszyklus gestartet und in `novapolis-dev/docs/todo.dev.md` aufgenommen. Punkt 1 (`ruff`/`black`/`pytest+coverage`) wurde begonnen; Ruff/Black-Befunde bereinigt, verbleibender Blocker ist Coverage (`76.24%` vs. Ziel `>=80%`).
- 2026-03-11 06:49: Letzter offener Dev-Optimierungspunkt geschlossen. Woechentliche 60-Minuten-Hygiene-Cadence mit KPI-Protokoll in `novapolis-dev/docs/process/abschluss-routine.ssot.md` verankert; Dev-Board und TODO-Index auf `offen: 0` synchronisiert.
- 2026-03-11 06:43: Rueckwaertskompatibilitaet fuer TODO-Index-CLI wiederhergestellt. `scripts/check_todo_index_sync.py` akzeptiert erneut `--root` als Alias zu `--repo-root` und toleriert `--strict` als Deprecated-Noop, damit bestehende Aufrufe nicht fehlschlagen.
- 2026-03-11 05:12: Beide Folgepunkte umgesetzt. `README.md` und `novapolis-dev/README.md` auf aktive Kurzoberflaeche gestrafft; `scripts/check_todo_index_sync.py` auf Auto-Write von Open-Counts/Board-Metadaten erweitert und in `scripts/run_checks_and_report.py` sowie `.vscode/tasks.json` eingebunden.
- 2026-03-11 04:49: Receipt-Hygiene abgeschlossen. Neue Governance-Dokumente (`SECURITY.md`, `CODE_OF_CONDUCT.md`, `CHANGELOG.md`, `docs/adr/README.md`) enthalten jetzt echte Gate-Receipts statt temporaerer `checks: pending`-Marker.
- 2026-03-11 04:46: README-Finish fuer aktive Lesbarkeit umgesetzt. Root-README verlinkt nun explizit `SECURITY.md`, `CODE_OF_CONDUCT.md`, `.github/CODEOWNERS`, `CHANGELOG.md` und `docs/adr/`; `novapolis-dev/README.md` wurde von einem veralteten Receipt-Block bereinigt und den Abschnitt `Checks & Reports` auf dauerhafte, scanbare Form gebracht.
- 2026-03-11 04:46: Root-DONELOG auf Summary-Ebene reduziert (Informationsarchitektur Schritt 2). Historische Detailketten in den Root-Archivpfad ausgelagert/verankert; aktive Root-Ansicht bleibt bewusst kurz.
- 2026-03-11 04:27: Doku-Informationsarchitektur geschaerft: aktive Oberflaechen in `novapolis-dev/docs` reduziert, Archiv-/Log-Matrix in Root/Dev-README verankert, TODO-Index-Guard und DONELOG-Workflow gehaertet.
- 2026-03-10 15:40: Wochenabschluss gemaess SSOT ausgefuehrt; Governance-Gates PASS, Restpunkte bei `ruff`, `black`, `pytest` im Full-Check.

Archiv-Verweise
---------------

- Root-Detailhistorie: `novapolis-dev/archive/docs/donelogs/donelog_root.md`
- Dev-Current-Window: `novapolis-dev/docs/donelog.md`
- Historische Dev-Window-Archive: `novapolis-dev/archive/docs/donelogs/`
