---
stand: 2026-02-16 16:05
update: Aus 00-admin extrahiert; Novapolis-spezifischer Campaign-State (Snapshot/FSM) angelegt.
checks: not run (migration)
title: Novapolis - Campaign State
category: canon
slug: novapolis-campaign-state
version: "0.1"
status: active
owners: [admin-novapolis]
tags: [rp, campaign, state, novapolis]
relatedSlugs: [novapolis, current-state, reference-campaign-state]
---

<!-- markdownlint-disable MD025 -->

Novapolis - Campaign State
==========================

Zweck
-----

Fraktionsspezifischer Zustands-Snapshot für Novapolis. Globale Mechanikregeln (`SE-POOLS`, `PROXIMITY`, `REFLEX-CONTROL`, `DETACH`, `JEALOUSY-GLOVES`) bleiben in `00-admin/Reference-Campaign-State.md`.

Start here
----------

- Current State (global): [Current-State](../../../00-admin/Current-State.md)
- Mechanik-SSOT (global): [Reference-Campaign-State](../../../00-admin/Reference-Campaign-State.md)

Campaign-State (Definitionen, Transitions, Beispiele)
-----------------------------------------------------

State-Übersicht (kanonische Namen)
----------------------------------

- CALM: Normalbetrieb, geringe Bedrohung, Fokus auf Arbeit/Alltag/Regeneration.
- ALERT: Erhöhtes Risiko/Unbekanntes; Vorsicht, Distanzen enger, Schutzbereitschaft hoch.
- CRISIS: Akute Gefahr (Selbst-/Fremdgefährdung); Notfallprotokolle und Übernahme erlaubt.
- AFTERMATH: Unmittelbare Gefahr gebrochen; Deeskalation, Checks, Versorgung, Review.
- MAINTENANCE: Geplante Ruhe-/Reset-Fenster (Schlaf, Technikservice), kein aktives Szenen-Spiel.
- Schonmodus (Overlay): Ressourcen-/Stabilitätsüberlagerung bei sehr niedriger SE oder harter Distanzverletzung; reduziert Fähigkeiten unabhängig vom Haupt-State.

Transitions (Trigger, Guards, Entry/Exit)
-----------------------------------------

- CALM → ALERT bei Unbekanntem Kontakt, Sensor-/Funk-Alarm, Distanzverletzung oder unsicherer Umgebung.
- ALERT → CALM bei bestätigter Entwarnung und stabiler Lage.
- ALERT → CRISIS bei akuter Gefahr/medizinischer Eskalation.
- CRISIS → ALERT nach Bruch der unmittelbaren Gefahr.
- CRISIS → AFTERMATH, wenn „Sicher“ erfüllt ist.
- AFTERMATH → CALM nach Regeneration, Review und ToDo-Übergabe.
- CALM ↔ MAINTENANCE für Schlaf/Servicefenster.

Hinweis: Detaillierte Trigger-/Guard-Definitionen sind global in [Reference-Campaign-State](../../../00-admin/Reference-Campaign-State.md) dokumentiert.

Beispiele / Use-Cases (Novapolis)
---------------------------------

- Werkstatt-Alltag (D5, Lumen↔Jonas): `CALM` mit kurzem Wechsel nach `ALERT` bei Tunnel-Pings.
- Tunnel-Patrouille (D5↔C6, Reflex↔Ronja): Start in `ALERT`, bei Gefahrenlage `CRISIS`, dann `AFTERMATH`.
- Kontakt-Guard (Marktszene, Echo↔Kora): Grenze setzen in `ALERT`, Rückkehr zu `CALM` nach Deeskalation.

Verweise
--------

- Missionsstatus: [Missionslog-Novapolis](../05-projects/Missionslog-Novapolis.md)
- Fraktionsübersicht: [Novapolis](../Novapolis.md)
- Globales Regelindex: [index-rules](../../../00-admin/index-rules.md)
