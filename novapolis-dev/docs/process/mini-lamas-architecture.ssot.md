---
stand: 2026-06-14 14:08
update: Neue Dev-/Process-SSOT fuer die Mini-Lamas-Architektur als KI-operativer Zielrahmen angelegt.
checks: pending post-mutation checks (naming, frontmatter, markdownlint)
---
Mini-Lamas Architecture (Dev/Process SSOT)
==========================================

Zweck
-----

- Diese SSOT legt die operative Rollen- und Betriebsarchitektur fuer lokale Mini-Lamas im Novapolis-Workspace fest.

Status / Scope
--------------

- Status: aktiv als Dev-/Process-SSOT.
- Scope: Dokumentierte Architektur- und Betriebsregeln fuer lokale Mini-Lamas, Local-Coding-Rollen und optionale externe QA.

Begriffsdefinition: Mini-Lamas
------------------------------

- Mini-Lamas sind lokal laufende, kleine bis mittlere Arbeitsmodelle fuer operative Teilaufgaben im Repo-Betrieb.
- Sie sind als Arbeitskern gedacht, nicht als autonomer Freigabe- oder Kanonmechanismus.

Grundsatz
---------

- Repo-Autonomie zuerst. Externe Mini-GPT-Pruefung optional. Lokale Mini-Lamas arbeiten, lokale Checks erzwingen, Mensch entscheidet.

Rollentrennung
--------------

- Kleine RP-/Chat-Mini-Lamas: laufender Betrieb, RP-nahe Runtime-Arbeit, Unterhaltung, Sprachchat-nahe Aufgaben.
- Local-Coding-Architect: qwen3-coder:30b.
- Aufgaben 30B: schwere lokale Coding-/Framework-/Architekturdiagnose; Patchplaene; groessere Code-/Testzusammenhaenge.
- Abgrenzung 30B: nicht fuer laufendes RP; beim RP-Tagesabschluss nur Konsistenz-Audit von Runtime-Daten, keine Szene/Lore/Figurenstimme.
- Local-Coding-Reviewer: qwen2.5-coder:14b.
- Aufgaben 14B: Review von 30B-Ergebnissen; Scope-/Diff-/Pfad-/Contract-/Gate-/DONELOG-Pruefung; technische und governance-operative RP-Mutationspruefung.
- Abgrenzung 14B: keine Lore-Hoheit.
- GPT-5 mini: optionales manuelles externes QA-/Konsistenzpruefwerkzeug des Users.
- Abgrenzung GPT-5 mini: keine notwendige Repo-Betriebskomponente; kein automatischer Gatekeeper.

Betriebsregeln
--------------

- 30B und 14B am Anfang read-only / text-only.
- Keine autonomen Writes.
- Mutation nur ueber explizit autorisierten Mutationslauf.
- Lokale Checks bleiben massgeblich.
- Mensch entscheidet Promotion/Kanon/Freigabe.

RP-Abgrenzung
-------------

- 30B beeinflusst keine Szene, Figurenstimme, Emotion oder Lore.
- 30B darf beim Tagesabschluss Runtime-Dateien gegeneinander pruefen.
- 14B prueft Dateioperationen, nicht Erzaehlwahrheit.

Nicht-Scope
-----------

- Keine TTS-Integration.
- Keine Sim-Integration.
- Keine Runtime-Codeverdrahtung.
- Keine Agent-Orchestrierung.
- Keine VS-Code-Settings-Aenderung.

Spaetere Folgekandidaten
------------------------

- Agent-Frontmatter nur nach separatem GO.
- Runtime-/Settings-Verdrahtung nur nach separatem GO.
- RP-Tagesabschluss-Audit-Vertrag nur nach separatem GO.
