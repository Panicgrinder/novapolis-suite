---
stand: 2026-04-05 19:43
update: Nera Vossen fuehrt jetzt einen eigenen Mind-Cluster fuer A1-Handelsleitung und Versorgungssicherheit.
checks: snapshot-lock PASS (2026-04-05 10:32); markdownlint PASS; frontmatter PASS; validate:rp PASS
title: Nera Vossen Mind Cluster
category: admin
slug: nera-vossen-mind-cluster
status: active
version: "0.1"
last_updated: 2026-04-05T10:32:00+02:00
owner: nera-vossen
---

Nera Vossen Mind Cluster
------------------------

Verhaltenssignatur
------------------

- `tbd` - aus dem Kurzprofil noch nicht als Signaturformel belegt.

Geistnaher Zustand
------------------

- Grundmodus: hart verhandelnd, dokumentationsstark, versorgungssichernd

Bekannte Entitaeten
-------------------

```yaml
known_entities:
  - observer_id: char:nera-vossen
    target_id: char:liora-navesh
    target_type: character
    policy_version: v0.1.0
    known: true
    relation_status: kooperativ
    relation_note: Fraktionsleitung mit Forschungsprioritaet; Nera uebersetzt Bedarf in belastbare Lieferfenster
    x: 7
    y: 16
    z: 9
    normtreue: 20
    vertrauen: 56
    loyalitaet: 52
    ansehen: 48
    ruf: 11
    machtprojektion: 19
    kooperationsneigung: 59
    konfliktneigung: 9
    einfluss: 39
    bedrohung: -4
    pos_streak: 0
    neg_streak: 0
    confidence: 0.71
    volatility: 0.30
    last_updated: 2026-04-05T10:32:00+02:00
    event_id: evt:bootstrap-nera-mind-liora-0001
    reason_codes: [RC-bootstrap, RC-migration_from_character_canvas]
    applied_rules: [R-MCL-SSOT, R-MCL-DATA]
    top_contributors: [character_ssot, startbogen_a1]
  - observer_id: char:nera-vossen
    target_id: char:borin-khade
    target_type: character
    policy_version: v0.1.0
    known: true
    relation_status: angespannt
    relation_note: Sicherheitsfreigaben begrenzen Transitfenster; Kooperation ist funktional, aber restriktiv
    x: 2
    y: 10
    z: 4
    normtreue: 18
    vertrauen: 37
    loyalitaet: 29
    ansehen: 39
    ruf: 9
    machtprojektion: 18
    kooperationsneigung: 41
    konfliktneigung: 14
    einfluss: 28
    bedrohung: 7
    pos_streak: 0
    neg_streak: 0
    confidence: 0.69
    volatility: 0.34
    last_updated: 2026-04-05T10:32:00+02:00
    event_id: evt:bootstrap-nera-mind-borin-0001
    reason_codes: [RC-bootstrap, RC-migration_from_character_canvas]
    applied_rules: [R-MCL-SSOT, R-MCL-DATA]
    top_contributors: [character_ssot]
```