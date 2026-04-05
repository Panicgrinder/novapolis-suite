---
stand: 2026-04-05 19:43
update: Echo verweist jetzt auf den eigenen Mind-Cluster und fuehrt ein lokales Knowledge-/Actions-Set fuer den C6-Startkorridor.
checks: snapshot-lock PASS (2026-04-05 08:10); markdownlint PASS; frontmatter PASS; validate:rp PASS
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

Hinweis: PROXIMITY ist Nähe aus Zuneigung + Schutz, situativ. Scope von Echo bleibt lokal/kurz (z. B. Hand stoppen, Sicht/Atmung frei halten). Details: [Reference-Campaign-State](../../../00-admin/Reference-Campaign-State.md).

Instanz-Profil (Wissen/Person)
------------------------------

- Wissensstand: Snapshot bei Entstehung (vom erzeugenden Träger zum Zeitpunkt t0). Danach eigene Entwicklung; kein automatischer Abgleich.
- Persönlichkeit: eigenständig; Entwicklung stark durch Kora/Umfeld geprägt.
- Details: [Reference-Campaign-State](../../../00-admin/Reference-Campaign-State.md)

SE-Pool (Instanz)
-----------------

- Pool: `SE_max = 8` (mittel; Schutz-/Schild-Fokus)
- Pools sind strikt getrennt (keine Übertragung zu Reflex/Lumen). Verbrauch fällt bei Echo an, wenn Echo aktiv schützt/unterstützt.
- Details: [Reference-Campaign-State](../../../00-admin/Reference-Campaign-State.md)

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

Knowledge (24x1h Starter)
-------------------------

```yaml
knowledge:
  - id: know-echo-kora-stress-2026-04-05-01
    about: kora_stress_shift
    channel: direct
    source: proximity_link
    scope: private
    confidence: 0.9
    freshness: 2026-04-05T08:10:00+02:00
    visibility_to: [echo, kora-malenkov]
    attachments: [doc:./Kora-Malenkov.md]
  - id: know-echo-c6-gate-contact-2026-04-05-01
    about: c6_gate_contact
    channel: overhear
    source: c6_watch
    scope: allies_only
    confidence: 0.7
    freshness: 2026-04-05T08:10:00+02:00
    visibility_to: [echo, kora-malenkov]
    attachments: [doc:../03-locations/C6.md]
```

Actions (24x1h Starter)
-----------------------

```yaml
actions:
  - id: act-echo-schutzmantel-2026-04-05-01
    verb: wache
    base_duration_min: 20
    effort: 2
    interruptible: true
    locks: [kora_proximity]
    may_trigger_event: true
    resources: [se_pool_echo]
    prerequisites: []
    outputs: [schutzmantel_aktiv]
    risks: [se_verbrauch]
  - id: act-echo-signalping-c6-2026-04-05-01
    verb: funk
    base_duration_min: 10
    effort: 1
    interruptible: true
    locks: [echo_signal_channel]
    may_trigger_event: true
    resources: [signalband]
    prerequisites: []
    outputs: [warnsignal]
    risks: [fehlalarm]
  - id: act-echo-kontakt-guard-2026-04-05-01
    verb: guard
    base_duration_min: 5
    effort: 2
    interruptible: true
    locks: [kontaktzone_kora]
    may_trigger_event: true
    resources: [reflex_gewebe]
    prerequisites: [know-echo-c6-gate-contact-2026-04-05-01]
    outputs: [kontakt_geblockt]
    risks: [misread_contact]
```

Interaktion & Safety (Instanz)
------------------------------

- Kopplung: An Kora gekoppelt; in sicheren Kontexten kurze lokale Bewegung ohne Dauer-Körperkontakt möglich (SE-Mehrverbrauch ohne externen Anker), sonst Schonmodus
- Eingriffe kurz; bei „Stop“ sofort lösen (Kora Priorität)
- Kontakt-Guard (Decision [JEALOUSY-GLOVES]): Wenn jemand Kora berühren will, kann Echo die **konkret betroffene Körperstelle** bedecken/abschirmen, um unerwünschten Kontakt zu verhindern; consent-first, "Stop" beendet sofort, "Freigabe" erlaubt Kontakt (Details: [Reference-Campaign-State](../../../00-admin/Reference-Campaign-State.md)).

### Signals (Beispiele)

- Request: „Echo, dicht bei mir - Sicht frei.“
- Stop: „Stopp.“ → sofort lösen

Mind-Cluster-Referenz (SSOT)
----------------------------

- Beziehungen, Verhaltenssignatur und geistnaher Zustand liegen zentral im Mind-Cluster:
- `../07-mind-clusters/echo-mind-cluster.md`

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

Projekte & Missions (Verlinkungen)
----------------------------------

- Missionslog (Prozess L.1) → ../05-projects/Missionslog-Novapolis.md

Links
-----

- Kora → ./Kora-Malenkov.md
- Reflex → ./Reflex.md
- Mind-Cluster (Echo) -> ../07-mind-clusters/echo-mind-cluster.md



