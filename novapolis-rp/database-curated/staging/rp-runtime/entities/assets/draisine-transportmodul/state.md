---
stand: 2026-04-29 06:56
update: Draisine-Transportmodul fuehrt jetzt die offene Antriebsfrage aus T12 als eigenen Runtime-State.
checks: snapshot-lock PASS (2026-04-29 06:56); markdownlint PASS; frontmatter PASS; todo-index-sync PASS; logs-policy PASS; snapshot-gate PASS
---

Runtime State - Draisine-Transportmodul
=======================================

Status
------

- slug: draisine-transportmodul
- scope: asset
- state: Arbeitsstand
- review_state: working

Current State
-------------

- summary: Die Draisine steht im aktuellen Hauptpfad auf den D5-Bahnsteiggleisen als offener Prototyp von Jonas mit Pahl an der Sicherheits- und Freigabekante. Der vorige Zug belegt gebundenen Werkstattbestand und den Aufbau an der Schiene; T12 oeffnet durch Ronjas direkte Frage die konkrete Antriebsfrage. Ein belegter Antrieb, eine Brems-/Stopplogik, eine Lastgrenze oder ein Testlauf sind damit noch nicht gesetzt.
- drivers:
  - SSOT: Das Projekt ist ein konservativer Material-/Transport-Prototyp fuer die Nordlinie, kein schneller Zug und kein Dauerdienst ohne Tunnel-Freigaben.
  - SSOT: Jonas traegt Bau und Integration; Pahl traegt Sicherheits- und Systemreview.
  - Runtime: Der aktuelle gebundene Prototypbestand liegt in `inventory.md`.
  - Runtime: Ronja fragt in T12 Jonas und Pahl, wie die Draisine angetrieben wird.
- blockers:
  - konkreter Antrieb offen
  - Brems-/Stopplogik offen
  - Lastgrenze fuer den aktuellen Bauzustand offen
  - kein belegter Testlauf
  - kein belegter Einsatz als Materiallogistik fuer den Tunnel
- impacted_entities:
  - Draisine-Transportmodul
  - Jonas Merek
  - Pahl Brenner
  - Lumen
  - Ronja Kerschner
  - D5
  - Nordlinie 01

Evidence
--------

- SSOT: `database-rp/01-factions/novapolis/05-projects/Draisine-Transportmodul.md`
- Runtime: `inventory.md`
- Runtime: `../../locations/d5/state.md`
- Runtime: `../../projects/nordlinie-01/state.md`
- Session: `../../../../sessions/d5-c6-nordlinie-sanierung-01/scene-log.md`, Turn 11
- Session: `../../../../sessions/d5-c6-nordlinie-sanierung-01/scene-log.md`, Turn 12

Promotion Notes
---------------

- Nicht als geklaerten Antrieb promoten. Erst Jonas/Pahl-Antwort oder SSOT-Nachzug darf den konkreten Antrieb, Bremslogik, Lastgrenze oder Testlauf festlegen.
