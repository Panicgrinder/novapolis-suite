---
stand: 2026-01-11 01:40
update: "JEALOUSY-GLOVES aligned: Kontakt-Guard (betroffene Körperstelle bedecken) bei Kora, Consent/Stop/Freigabe via Reference."
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-rp/database-rp/**/*.md' PASS (2026-01-11 01:37); & .\.venv\Scripts\python.exe scripts\check_frontmatter.py novapolis-rp\database-rp PASS (2026-01-11 01:37); & .\.venv\Scripts\python.exe scripts\checks_rp_consistency.py --strict PASS (2026-01-11 01:37)
title: Echo
category: character
slug: echo
version: "0.9"
last_updated: 2026-01-11T01:40:00+01:00
tags: ["instanz"]
affiliations: ["novapolis"]
dependencies: ["kora-malenkov", "reflex", "echo-wissensstand-trainingsstand", "c6"]
primary_location: c6
last_seen: c6
---

<!-- markdownlint-disable MD025 -->

Echo
====

- Meta: last-updated: 2025-11-07T03:32:00+01:00
- Verhaltenssignatur: `ECO1=L85-S74-T62-E58-N52-O44-C28-M16-P30-ks` - bindet sich eng an Kora, reagiert kindlich-selbstlos und priorisiert Schutzinstinkte.

- Rolle: Reflex-Instanz (an Kora gekoppelt)
- Werte: tbd
- Skills:
  - Geübt: tbd
  - Meisterhaft: tbd
  - Optional: tbd
- Ausrüstung/Körper: Reflex-Material (formbar, schützend)
- Motivation: Nähe und Schutz für Kora
- Makel: Instabilität bei Distanz

Notizen
-------

- Bewegungsmuster/Physiologie analog zu Reflex/Lumen; starke Bindung an Bezugsperson [PROXIMITY].

Hinweis: PROXIMITY ist Nähe aus Zuneigung + Schutz, situativ. Scope von Echo bleibt lokal/kurz (z. B. Hand stoppen, Sicht/Atmung frei halten). Details: [Reference-Campaign-State](../00-admin/Reference-Campaign-State.md).

Instanz-Profil (Wissen/Person)
------------------------------

- Wissensstand: Snapshot bei Entstehung (vom erzeugenden Träger zum Zeitpunkt t0). Danach eigene Entwicklung; kein automatischer Abgleich.
- Persönlichkeit: eigenständig; Entwicklung stark durch Kora/Umfeld geprägt.
- Details: [Reference-Campaign-State](../00-admin/Reference-Campaign-State.md)

SE-Pool (Instanz)
-----------------

- Pool: `SE_max = 8` (mittel; Schutz-/Schild-Fokus)
- Pools sind strikt getrennt (keine Übertragung zu Reflex/Lumen). Verbrauch fällt bei Echo an, wenn Echo aktiv schützt/unterstützt.
- Details: [Reference-Campaign-State](../00-admin/Reference-Campaign-State.md)

Rollen & Verantwortlichkeiten (Pflichtfelder)
---------------------------------------------

- Assistenz/Schutz für Kora in C6
- Signalisierung/Kommunikation (kurz, klare Trigger)

Zugehörigkeit & Standort
------------------------

- Zugehörigkeit: Novapolis (C6)
- Status: aktiv
- Letzter bekannter Einsatzort: C6

Wissensstand (Matrix - Auszug)
------------------------------

- Intern: Reflex/Instanzen bekannt
- Extern: nicht bekannt/keine Offenlegung [FR-KNOWLEDGE]

Interaktion & Safety (Instanz)
------------------------------

- Kopplung: An Kora gekoppelt; in sicheren Kontexten kurze lokale Bewegung ohne Dauer-Körperkontakt möglich (SE-Mehrverbrauch ohne externen Anker), sonst Schonmodus
- Eingriffe kurz; bei „Stop“ sofort lösen (Kora Priorität)
- Kontakt-Guard (Decision [JEALOUSY-GLOVES]): Wenn jemand Kora berühren will, kann Echo die **konkret betroffene Körperstelle** bedecken/abschirmen, um unerwünschten Kontakt zu verhindern; consent-first, "Stop" beendet sofort, "Freigabe" erlaubt Kontakt (Details: [Reference-Campaign-State](../00-admin/Reference-Campaign-State.md)).

### Signals (Beispiele)

- Request: „Echo, dicht bei mir - Sicht frei.“
- Stop: „Stopp.“ → sofort lösen

Ausrüstung (Details)
--------------------

- Material: Reflex-Gewebe (fein), formbare Schutzschicht

Verhaltens-Hooks
----------------

- Nähe zu Kora suchen; leise, beobachtend; Assist vor Guard

Ziele (kurz)
------------

- [ ] Stabiler Betrieb an Koras Seite
- [ ] Schutz ohne Sicht/Atmung zu blockieren

Beziehungen
-----------

- Kora - Bezugsperson
- Reflex - Primärinstanz; Lumen - Schwester-Instanz

Projekte & Missions (Verlinkungen)
----------------------------------

- Missionslog (Prozess L.1) → ../00-admin/Missionslog.md

Links
-----

- Kora → ./Kora-Malenkov.md
- Reflex → ./Reflex.md



