---
stand: 2026-04-05 19:43
update: Yara Kest fuehrt jetzt einen eigenen Mind-Cluster fuer H12-Sicherheitsleitung, Alarmprotokolle und Reaktionsketten.
checks: snapshot-lock PASS (2026-04-05 10:32); markdownlint PASS; frontmatter PASS; validate:rp PASS
title: Yara Kest Mind Cluster
category: admin
slug: yara-kest-mind-cluster
status: active
version: "0.1"
last_updated: 2026-04-05T10:32:00+02:00
owner: yara-kest
---

Yara Kest Mind Cluster
----------------------

Verhaltenssignatur
------------------

- `tbd` - aus dem Kurzprofil noch nicht als Signaturformel belegt.

Geistnaher Zustand
------------------

- Grundmodus: prozedural streng, taktisch erfahren, in Infrastrukturfragen kompromissarm

Bekannte Entitaeten
-------------------

```yaml
known_entities:
  - observer_id: char:yara-kest
    target_id: char:varek-solun
    target_type: character
    policy_version: v0.1.0
    known: true
    relation_status: kooperativ
    relation_note: zentrale Befehls- und Eskalationslinie fuer Sicherheitsoperationen in H12
    x: 8
    y: 17
    z: 5
    normtreue: 28
    vertrauen: 65
    loyalitaet: 71
    ansehen: 55
    ruf: 10
    machtprojektion: 34
    kooperationsneigung: 40
    konfliktneigung: 16
    einfluss: 48
    bedrohung: 0
    pos_streak: 0
    neg_streak: 0
    confidence: 0.76
    volatility: 0.26
    last_updated: 2026-04-05T10:32:00+02:00
    event_id: evt:bootstrap-yara-mind-varek-0001
    reason_codes: [RC-bootstrap, RC-migration_from_character_canvas]
    applied_rules: [R-MCL-SSOT, R-MCL-DATA]
    top_contributors: [character_ssot, startbogen_h12]
  - observer_id: char:yara-kest
    target_id: char:kaspar-dorn
    target_type: character
    policy_version: v0.1.0
    known: true
    relation_status: angespannt
    relation_note: Handelsdruck und Sicherheitsdisziplin kollidieren regelmaessig an Transitpunkten
    x: 1
    y: 7
    z: 1
    normtreue: 20
    vertrauen: 29
    loyalitaet: 30
    ansehen: 34
    ruf: 6
    machtprojektion: 19
    kooperationsneigung: 30
    konfliktneigung: 18
    einfluss: 25
    bedrohung: 10
    pos_streak: 0
    neg_streak: 0
    confidence: 0.68
    volatility: 0.35
    last_updated: 2026-04-05T10:32:00+02:00
    event_id: evt:bootstrap-yara-mind-kaspar-0001
    reason_codes: [RC-bootstrap, RC-migration_from_character_canvas]
    applied_rules: [R-MCL-SSOT, R-MCL-DATA]
    top_contributors: [character_ssot]
```