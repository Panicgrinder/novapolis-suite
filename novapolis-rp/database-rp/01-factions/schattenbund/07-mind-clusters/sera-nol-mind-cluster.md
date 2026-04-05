---
stand: 2026-04-05 19:43
update: Sera Nol fuehrt jetzt einen eigenen Mind-Cluster fuer F9-Sicherheitsleitung, Gegenaufklaerung und Abschirmung.
checks: snapshot-lock PASS (2026-04-05 10:32); markdownlint PASS; frontmatter PASS; validate:rp PASS
title: Sera Nol Mind Cluster
category: admin
slug: sera-nol-mind-cluster
status: active
version: "0.1"
last_updated: 2026-04-05T10:32:00+02:00
owner: sera-nol
---

Sera Nol Mind Cluster
---------------------

Verhaltenssignatur
------------------

- `tbd` - aus dem Kurzprofil noch nicht als Signaturformel belegt.

Geistnaher Zustand
------------------

- Grundmodus: kontrolliert, gegenaufklaerungsstark, mehrstufig abschirmend

Bekannte Entitaeten
-------------------

```yaml
known_entities:
  - observer_id: char:sera-nol
    target_id: char:nyra-vehl
    target_type: character
    policy_version: v0.1.0
    known: true
    relation_status: kooperativ
    relation_note: Fuehrungsanker fuer Zugriffsstufen, Leck-Reaktion und Eskalationsgrenzen
    x: 8
    y: 17
    z: 4
    normtreue: 22
    vertrauen: 58
    loyalitaet: 62
    ansehen: 48
    ruf: 10
    machtprojektion: 31
    kooperationsneigung: 41
    konfliktneigung: 16
    einfluss: 45
    bedrohung: 2
    pos_streak: 0
    neg_streak: 0
    confidence: 0.74
    volatility: 0.27
    last_updated: 2026-04-05T10:32:00+02:00
    event_id: evt:bootstrap-sera-nol-mind-nyra-0001
    reason_codes: [RC-bootstrap, RC-migration_from_character_canvas]
    applied_rules: [R-MCL-SSOT, R-MCL-DATA]
    top_contributors: [character_ssot, startbogen_f9]
  - observer_id: char:sera-nol
    target_id: char:jarek-voan
    target_type: character
    policy_version: v0.1.0
    known: true
    relation_status: angespannt
    relation_note: Sicherheitsgrenzen kollidieren wiederholt mit verdeckten Lieferlogiken und Zeitdruck
    x: 2
    y: 7
    z: 1
    normtreue: 18
    vertrauen: 29
    loyalitaet: 27
    ansehen: 32
    ruf: 6
    machtprojektion: 17
    kooperationsneigung: 29
    konfliktneigung: 18
    einfluss: 25
    bedrohung: 10
    pos_streak: 0
    neg_streak: 0
    confidence: 0.67
    volatility: 0.35
    last_updated: 2026-04-05T10:32:00+02:00
    event_id: evt:bootstrap-sera-nol-mind-jarek-0001
    reason_codes: [RC-bootstrap, RC-migration_from_character_canvas]
    applied_rules: [R-MCL-SSOT, R-MCL-DATA]
    top_contributors: [character_ssot]
```