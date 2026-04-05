---
stand: 2026-04-05 19:43
update: Rian Kord fuehrt jetzt einen eigenen Mind-Cluster fuer B2-Handelsleitung, Trassenlogik und Vorteilskorridore.
checks: snapshot-lock PASS (2026-04-05 10:32); markdownlint PASS; frontmatter PASS; validate:rp PASS
title: Rian Kord Mind Cluster
category: admin
slug: rian-kord-mind-cluster
status: active
version: "0.1"
last_updated: 2026-04-05T10:32:00+02:00
owner: rian-kord
---

Rian Kord Mind Cluster
----------------------

Verhaltenssignatur
------------------

- `tbd` - aus dem Kurzprofil noch nicht als Signaturformel belegt.

Geistnaher Zustand
------------------

- Grundmodus: knapp kalkulierend, durchsatzorientiert, verhandelt nur im Vorteilskorridor

Bekannte Entitaeten
-------------------

```yaml
known_entities:
  - observer_id: char:rian-kord
    target_id: char:helia-vorn
    target_type: character
    policy_version: v0.1.0
    known: true
    relation_status: kooperativ
    relation_note: Leitung gibt den strategischen Rahmen vor, in dem Rian Lieferfenster optimiert
    x: 5
    y: 13
    z: 5
    normtreue: 20
    vertrauen: 49
    loyalitaet: 52
    ansehen: 43
    ruf: 9
    machtprojektion: 18
    kooperationsneigung: 44
    konfliktneigung: 13
    einfluss: 34
    bedrohung: 2
    pos_streak: 0
    neg_streak: 0
    confidence: 0.70
    volatility: 0.30
    last_updated: 2026-04-05T10:32:00+02:00
    event_id: evt:bootstrap-rian-mind-helia-0001
    reason_codes: [RC-bootstrap, RC-migration_from_character_canvas]
    applied_rules: [R-MCL-SSOT, R-MCL-DATA]
    top_contributors: [character_ssot, startbogen_b2]
  - observer_id: char:rian-kord
    target_id: char:tera-solm
    target_type: character
    policy_version: v0.1.0
    known: true
    relation_status: angespannt
    relation_note: Sicherheitsdisziplin beschneidet Durchsatz; funktional abgestimmt, aber oft friktiv
    x: 1
    y: 8
    z: 2
    normtreue: 17
    vertrauen: 30
    loyalitaet: 27
    ansehen: 33
    ruf: 7
    machtprojektion: 15
    kooperationsneigung: 31
    konfliktneigung: 17
    einfluss: 24
    bedrohung: 9
    pos_streak: 0
    neg_streak: 0
    confidence: 0.67
    volatility: 0.35
    last_updated: 2026-04-05T10:32:00+02:00
    event_id: evt:bootstrap-rian-mind-tera-0001
    reason_codes: [RC-bootstrap, RC-migration_from_character_canvas]
    applied_rules: [R-MCL-SSOT, R-MCL-DATA]
    top_contributors: [character_ssot]
```