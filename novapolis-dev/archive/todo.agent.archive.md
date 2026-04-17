---
stand: 2026-04-17 04:39
update: Der zuletzt geschlossene Agent-Handover-Block ist archiviert; das Live-Board kann wieder schlank fuer neue Agent-Punkte arbeiten.
checks: snapshot-lock PASS (2026-04-17 04:15); workspace-evidence PASS (todo.agent-board, todo.agent.archive); markdownlint=PASS; frontmatter=PASS
---

TODO-Archiv - Agent
===================

Zweck: Vollständig abgeschlossene TODO-Abschnitte aus `novapolis_agent/docs/TODO.md` aufnehmen, damit `TODO.md` schlank bleibt.

Regeln (kurz)

- Nur Abschnitte verschieben, deren Checklisten vollständig auf [x] stehen.
- Inhalt unverändert übernehmen. Direkt unter der Abschnitts-Überschrift eine Einzeile ergänzen: `archived_at: YYYY-MM-DD HH:MM`.
- Headings in diesem Archiv: Setext (MD003 konform, H1/H2).
- Präsentation: Lint-Läufe mit PRESENTATION=SHARED.
- DONELOG: Ein Zeilen-Eintrag im Agent-DONELOG genügt (kein Volltext hier).

Ablage

- Neueste Einträge oben einfügen.

<!-- Hier unterhalb neue, vollständig erledigte Blöcke einfügen (neu zuerst). -->

Offene Aufgaben - Slice-2 Folgepfad (2026-04-17)
------------------------------------------------

archived_at: 2026-04-17 04:15

- [x] [Jetzt] `Text-RPG Product Gate v1` um einen zweiten Handover-Referenzfall hinter `slot 30` erweitern.
  - Ziel: Der kanonische Agent-Gatepfad soll nicht nur den ersten Slice und den Grundvertrag pruefen, sondern denselben Session-/Artefaktvertrag auch fuer den Resume-/Replay-Folgepfad hinter `slot 30` deterministisch absichern.
  - Akzeptanzkriterien:
    1) es existiert ein zweiter reproduzierbarer Referenzfall oder eine aequivalente Referenz-Session fuer den Handover-Folgepfad hinter `slot 30`,
    2) Product Gate, Runbook und Tasking fuehren fuer diesen Fall denselben Namen und denselben Ablauf,
    3) `resume_checkpoint_id`, `savegame.json`, `world_log.jsonl`, `pc_log.jsonl` und `replay_manifest.json` werden fuer den Folgefall gegen denselben Vertrag validiert,
    4) die neue Referenz oeffnet keinen Parallelpfad neben dem bestehenden `Text-RPG Product Gate v1`, sondern erweitert den vorhandenen Standardlauf.
  - Evidenz: `novapolis_agent/docs/runbook.md` fordert fuer neue Referenzfaelle, Gate-Erweiterungen oder Resume-Checks hinter `slot 30` explizit denselben Session- und Artefaktvertrag; `novapolis-dev/docs/process/text-rpg-slice-2-handover-v1.ssot.md` bindet denselben Folgepfad bereits an `resume_checkpoint_id` und Carry-Over-Zustand, ohne dass dafuer bislang ein zweiter Agent-Referenzfall im Board steht.
  - Ergebnis 2026-04-17 04:00: `novapolis_agent/eval/config/text_rpg_reference_session_handover_slot31_40.v1.json` materialisiert jetzt den zweiten deterministischen Folgefall hinter `slot 30` bis `slot 40`. `novapolis_agent/scripts/run_text_rpg_reference_session.py` fuehrt denselben Standardlauf jetzt mit wiederholbarem `--spec` fuer mehrere Referenzfaelle aus, und `scripts/run_text_rpg_product_gate.py` sowie `Tests: text-rpg reference session` ziehen den D5-Basisfall plus Handover-Folgefall im selben Gate-Schritt. `novapolis_agent/docs/runbook.md`, `novapolis-dev/docs/process/text-rpg-product-gate-v1.ssot.md` und `novapolis-dev/docs/process/text-rpg-slice-2-handover-v1.ssot.md` benennen im selben Lauf denselben erweiterten Standardpfad; das Agent-Board steht damit wieder bei `offen: 0`.

Root-Uebernahme: novapolis_agent Block aus todo.root
---------------------------------------------------

archived_at: 2026-02-21 04:52

Quelle: `todo.root.md` (Abschnitte `novapolis_agent`, `Tests/Typen/Coverage`, `RP-Audit Befunde`, `Frontmatter/Markdown-Sweep`).

- [x] Agent-Root-Aufgabenblock als abgeschlossen archiviert.
- [x] Tests/Typen/Coverage-Teilblock als abgeschlossen archiviert.
- [x] RP-Audit-Befunde-Teilblock als abgeschlossen archiviert.
- [x] Frontmatter/Markdown-Sweep-Teilblock als abgeschlossen archiviert.
- [x] Aktiver Root-Backlog enthaelt diese Detailhistorie nicht mehr; Verweise bleiben in den Archiven.

Kurzfristige Ziele (Heute)
--------------------------

archived_at: 2025-11-01 19:16

- [x] Eval-Profile festziehen
  - Ziel: Reproduzierbare Läufe via `eval/config/profiles.json` (quiet default, temp, optionale Checks).
  - Status: Done (UI lädt Profile; Meta-Header vollständig; kurzer ASGI-Lauf konsistent).
- [x] Eval-UI: Profile-/Quiet-/ASGI-/Guard-Bypass-Integration
  - Ziel: Läufe steuerbar über Profile, reduzierte Logs, In-Process-ASGI, optionaler Vorab-Guard.
  - Status: Done (Menü integriert, Flags wirksam, Trends/Exports ok).
- [x] Synonym-Overlay (privat) einführen und mergen
  - Ziel: `eval/config/synonyms.local.json` (gitignored) automatisch mit `synonyms.json` mergen.
  - Status: Done (Loader-Merge, Sample-Datei, Doku in README & eval/README, .gitignore ergänzt).
- [x] Eval-Pfade harmonisieren & Meta-Header erweitern
  - Ziel: Nutzung von `eval/datasets|results|config`, Meta mit overrides (model/host/temperature).
  - Status: Done (Runner/UI angepasst, Ergebnisse validiert).


