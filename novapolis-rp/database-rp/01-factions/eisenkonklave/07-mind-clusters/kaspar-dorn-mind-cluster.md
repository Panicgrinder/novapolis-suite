---
stand: 2026-04-05 19:43
update: Kaspar Dorn fuehrt jetzt einen eigenen Mind-Cluster fuer H12-Handelsleitung, Sanktionen und Ressourcenpriorisierung.
checks: snapshot-lock PASS (2026-04-05 10:32); markdownlint PASS; frontmatter PASS; validate:rp PASS
title: Kaspar Dorn Mind Cluster
category: admin
slug: kaspar-dorn-mind-cluster
status: active
version: "0.1"
last_updated: 2026-04-05T10:32:00+02:00
owner: kaspar-dorn
---

Kaspar Dorn Mind Cluster
------------------------

Verhaltenssignatur
------------------

- `tbd` - aus dem Kurzprofil noch nicht als Signaturformel belegt.

Geistnaher Zustand
------------------

- Grundmodus: nüchtern, risikominimierend, ueber gesicherte Kanaele handelnd

Bekannte Entitaeten
-------------------

```yaml
known_entities:
  - observer_id: char:kaspar-dorn
    target_id: char:varek-solun
    target_type: character
    policy_version: v0.1.0
    known: true
    relation_status: kooperativ
    relation_note: bindender Leitungsanker; Handelsfenster folgen Vareks Sicherheits- und Priorlogik
    x: 4
    y: 12
    z: 5
    normtreue: 21
    vertrauen: 52
    loyalitaet: 56
    ansehen: 44
    ruf: 9
    machtprojektion: 20
    kooperationsneigung: 45
    konfliktneigung: 11
    einfluss: 34
    bedrohung: 2
    pos_streak: 0
    neg_streak: 0
    confidence: 0.71
    volatility: 0.30
    last_updated: 2026-04-05T10:32:00+02:00
    event_id: evt:bootstrap-kaspar-mind-varek-0001
    reason_codes: [RC-bootstrap, RC-migration_from_character_canvas]
    applied_rules: [R-MCL-SSOT, R-MCL-DATA]
    top_contributors: [character_ssot, startbogen_h12]
  - observer_id: char:kaspar-dorn
    target_id: char:yara-kest
    target_type: character
    policy_version: v0.1.0
    known: true
    relation_status: angespannt
    relation_note: Handelsrouten sind ohne Sicherheitsfreigaben blockiert; funktional, aber rauh abgestimmt
    x: 1
    y: 7
    z: 2
    normtreue: 18
    vertrauen: 31
    loyalitaet: 28
    ansehen: 35
    ruf: 7
    machtprojektion: 18
    kooperationsneigung: 34
    konfliktneigung: 15
    einfluss: 24
    bedrohung: 9
    pos_streak: 0
    neg_streak: 0
    confidence: 0.68
    volatility: 0.34
    last_updated: 2026-04-05T10:32:00+02:00
    event_id: evt:bootstrap-kaspar-mind-yara-0001
    reason_codes: [RC-bootstrap, RC-migration_from_character_canvas]
    applied_rules: [R-MCL-SSOT, R-MCL-DATA]
    top_contributors: [character_ssot]
```