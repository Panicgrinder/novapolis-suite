---
stand: 2026-04-05 19:43
update: Varek Solun fuehrt jetzt einen eigenen Mind-Cluster fuer Kommandofuehrung, H12-Sicherheit und kontrollierte Handelskanaele.
checks: snapshot-lock PASS (2026-04-05 10:32); markdownlint PASS; frontmatter PASS; validate:rp PASS
title: Varek Solun Mind Cluster
category: admin
slug: varek-solun-mind-cluster
status: active
version: "0.1"
last_updated: 2026-04-05T10:32:00+02:00
owner: varek-solun
---

Varek Solun Mind Cluster
------------------------

Verhaltenssignatur
------------------

- `VRS1=O88-M76-S68-T62-L55-N44-C28-E25-P60-pr`
- Lesart: kontrollorientierte Fuehrung mit hoher Wachsamkeit und niedriger Fehlertoleranz.

Bekannte Entitaeten
-------------------

```yaml
known_entities:
  - observer_id: char:varek-solun
    target_id: char:kaspar-dorn
    target_type: character
    policy_version: v0.1.0
    known: true
    relation_status: kooperativ
    relation_note: Handelsleitung als strikt begrenztes Werkzeug fuer Ressourcen- und Einflusskontrolle
    x: 5
    y: 14
    z: 5
    normtreue: 23
    vertrauen: 48
    loyalitaet: 51
    ansehen: 50
    ruf: 10
    machtprojektion: 28
    kooperationsneigung: 44
    konfliktneigung: 13
    einfluss: 40
    bedrohung: 2
    pos_streak: 0
    neg_streak: 0
    confidence: 0.73
    volatility: 0.28
    last_updated: 2026-04-05T10:32:00+02:00
    event_id: evt:bootstrap-varek-mind-kaspar-0001
    reason_codes: [RC-bootstrap, RC-migration_from_character_canvas]
    applied_rules: [R-MCL-SSOT, R-MCL-DATA]
    top_contributors: [character_ssot, startbogen_h12]
  - observer_id: char:varek-solun
    target_id: char:yara-kest
    target_type: character
    policy_version: v0.1.0
    known: true
    relation_status: kooperativ
    relation_note: Sicherheitsleitung als verlängerter Arm fuer Disziplin und Gegenmaßnahmen
    x: 7
    y: 16
    z: 6
    normtreue: 27
    vertrauen: 63
    loyalitaet: 68
    ansehen: 56
    ruf: 11
    machtprojektion: 35
    kooperationsneigung: 42
    konfliktneigung: 15
    einfluss: 49
    bedrohung: 1
    pos_streak: 0
    neg_streak: 0
    confidence: 0.76
    volatility: 0.26
    last_updated: 2026-04-05T10:32:00+02:00
    event_id: evt:bootstrap-varek-mind-yara-0001
    reason_codes: [RC-bootstrap, RC-migration_from_character_canvas]
    applied_rules: [R-MCL-SSOT, R-MCL-DATA]
    top_contributors: [character_ssot, startbogen_h12]
```