---
stand: 2026-04-05 19:43
update: Liora Navesh fuehrt jetzt einen eigenen Mind-Cluster fuer Forschungsrat, A1-Leitung und externe Sicherheitspruefung.
checks: snapshot-lock PASS (2026-04-05 10:32); markdownlint PASS; frontmatter PASS; validate:rp PASS
title: Liora Navesh Mind Cluster
category: admin
slug: liora-navesh-mind-cluster
status: active
version: "0.1"
last_updated: 2026-04-05T10:32:00+02:00
owner: liora-navesh
---

Liora Navesh Mind Cluster
-------------------------

Zweck
-----

- SSOT fuer Lioras beziehungsnahe Lage zwischen Forschungsrat, medizinischer Leitung und A1-Sicherheitsgrenzen.

Verhaltenssignatur
------------------

- `LNR1=O82-T76-N68-S58-L52-M47-E34-C21-P55-r`
- Lesart: analytisch, rational und auf validierte Erkenntniswege ausgerichtet.

Bekannte Entitaeten
-------------------

```yaml
known_entities:
  - observer_id: char:liora-navesh
    target_id: char:nera-vossen
    target_type: character
    policy_version: v0.1.0
    known: true
    relation_status: kooperativ
    relation_note: Handelsleitung als kontrollierte Versorgungsschnittstelle fuer Forschung und Medizin
    x: 8
    y: 17
    z: 9
    normtreue: 22
    vertrauen: 52
    loyalitaet: 49
    ansehen: 55
    ruf: 12
    machtprojektion: 24
    kooperationsneigung: 57
    konfliktneigung: 8
    einfluss: 43
    bedrohung: -3
    pos_streak: 0
    neg_streak: 0
    confidence: 0.73
    volatility: 0.29
    last_updated: 2026-04-05T10:32:00+02:00
    event_id: evt:bootstrap-liora-mind-nera-0001
    reason_codes: [RC-bootstrap, RC-migration_from_character_canvas]
    applied_rules: [R-MCL-SSOT, R-MCL-DATA]
    top_contributors: [character_ssot, startbogen_a1]
  - observer_id: char:liora-navesh
    target_id: char:borin-khade
    target_type: character
    policy_version: v0.1.0
    known: true
    relation_status: kooperativ
    relation_note: Sicherheitsleitung als Schutzschild fuer A1-Protokolle und Anomaliearbeit
    x: 6
    y: 15
    z: 7
    normtreue: 24
    vertrauen: 57
    loyalitaet: 53
    ansehen: 58
    ruf: 13
    machtprojektion: 29
    kooperationsneigung: 52
    konfliktneigung: 9
    einfluss: 46
    bedrohung: -2
    pos_streak: 0
    neg_streak: 0
    confidence: 0.75
    volatility: 0.28
    last_updated: 2026-04-05T10:32:00+02:00
    event_id: evt:bootstrap-liora-mind-borin-0001
    reason_codes: [RC-bootstrap, RC-migration_from_character_canvas]
    applied_rules: [R-MCL-SSOT, R-MCL-DATA]
    top_contributors: [character_ssot, startbogen_a1]
```