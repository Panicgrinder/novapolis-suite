---
stand: 2026-05-20 06:28
update: Draisine-Transportmodul fuehrt jetzt die konservative Hand-/Schubdebatte als Arbeitsrichtung ohne Freigabe.
checks: snapshot-lock PASS (2026-05-20 06:28); npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc RP-Runtime-turn13-slice PASS (2026-05-20 06:22); .\.venv\Scripts\python.exe scripts\check_frontmatter.py RP-Runtime-turn13-slice PASS (EXITCODE=0, 2026-05-20 06:22)
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

- summary: Die Draisine steht im aktuellen Hauptpfad auf den D5-Bahnsteiggleisen als offener Prototyp von Jonas mit Pahl an der Sicherheits- und Freigabekante. Der vorige Zug belegt gebundenen Werkstattbestand und den Aufbau an der Schiene; T12 oeffnet durch Ronjas direkte Frage die konkrete Antriebsfrage. Turn 13 zieht die Debatte auf konservative nichtmotorische Varianten: eine einfache Hebel-/Handdraisine oder notfalls kontrolliertes Schieben auf gesicherter Strecke. Ein belegter Antrieb, eine Brems-/Stopplogik, eine Lastgrenze oder ein Testlauf sind damit weiterhin nicht gesetzt.
- drivers:
  - SSOT: Das Projekt ist ein konservativer Material-/Transport-Prototyp fuer die Nordlinie, kein schneller Zug und kein Dauerdienst ohne Tunnel-Freigaben.
  - SSOT: Jonas traegt Bau und Integration; Pahl traegt Sicherheits- und Systemreview.
  - Runtime: Der aktuelle gebundene Prototypbestand liegt in `inventory.md`.
  - Runtime: Ronja fragt in T12 Jonas und Pahl, wie die Draisine angetrieben wird.
  - Runtime: Turn 13 fuehrt Schieben auf gesicherter Strecke und eine einfache Hebel-/Handdraisine als pruefbare Arbeitsrichtungen, aber nicht als beschlossenen Baupfad.
- blockers:
  - konkreter Antrieb offen
  - keine der diskutierten nichtmotorischen Varianten ist bisher als Bauentscheidung, Freigabe oder realer Einsatzpfad bestaetigt
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
