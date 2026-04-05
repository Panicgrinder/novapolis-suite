---
stand: 2026-04-05 19:43
update: Sera Kaal fuehrt jetzt einen eigenen Mind-Cluster fuer K4-Sicherheitsleitung, Gegenaufklaerung und Zutrittskontrolle.
checks: snapshot-lock PASS (2026-04-05 10:32); markdownlint PASS; frontmatter PASS; validate:rp PASS
title: Sera Kaal Mind Cluster
category: admin
slug: sera-kaal-mind-cluster
status: active
version: "0.1"
last_updated: 2026-04-05T10:32:00+02:00
owner: sera-kaal
---

Sera Kaal Mind Cluster
----------------------

Verhaltenssignatur
------------------

- `tbd` - aus dem Kurzprofil noch nicht als Signaturformel belegt.

Geistnaher Zustand
------------------

- Grundmodus: vorsichtig, gegenaufklaerungsstark, auf Reaktionsketten und Zutrittsdisziplin konzentriert

Bekannte Entitaeten
-------------------

```yaml
known_entities:
  - observer_id: char:sera-kaal
    target_id: char:iris-vey
    target_type: character
    policy_version: v0.1.0
    known: true
    relation_status: kooperativ
    relation_note: Leitungsanker fuer Prioritaeten, Tarnung und Eskalationsgrenzen des K4-Netzes
    x: 9
    y: 18
    z: 4
    normtreue: 21
    vertrauen: 60
    loyalitaet: 63
    ansehen: 48
    ruf: 10
    machtprojektion: 30
    kooperationsneigung: 43
    konfliktneigung: 15
    einfluss: 45
    bedrohung: 1
    pos_streak: 0
    neg_streak: 0
    confidence: 0.74
    volatility: 0.27
    last_updated: 2026-04-05T10:32:00+02:00
    event_id: evt:bootstrap-sera-kaal-mind-iris-0001
    reason_codes: [RC-bootstrap, RC-migration_from_character_canvas]
    applied_rules: [R-MCL-SSOT, R-MCL-DATA]
    top_contributors: [character_ssot, startbogen_k4]
  - observer_id: char:sera-kaal
    target_id: char:corin-mael
    target_type: character
    policy_version: v0.1.0
    known: true
    relation_status: angespannt
    relation_note: Sicherheitsinteressen kollidieren mit indirekten Handelskanaelen und Kontaktbreite
    x: 2
    y: 8
    z: 1
    normtreue: 16
    vertrauen: 30
    loyalitaet: 27
    ansehen: 31
    ruf: 7
    machtprojektion: 16
    kooperationsneigung: 30
    konfliktneigung: 17
    einfluss: 24
    bedrohung: 9
    pos_streak: 0
    neg_streak: 0
    confidence: 0.67
    volatility: 0.35
    last_updated: 2026-04-05T10:32:00+02:00
    event_id: evt:bootstrap-sera-kaal-mind-corin-0001
    reason_codes: [RC-bootstrap, RC-migration_from_character_canvas]
    applied_rules: [R-MCL-SSOT, R-MCL-DATA]
    top_contributors: [character_ssot]
```