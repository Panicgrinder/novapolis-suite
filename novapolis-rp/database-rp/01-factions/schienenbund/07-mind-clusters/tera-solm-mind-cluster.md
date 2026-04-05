---
stand: 2026-04-05 19:43
update: Tera Solm fuehrt jetzt einen eigenen Mind-Cluster fuer B2-Sicherheitsleitung, Trassenschutz und Sperrprotokolle.
checks: snapshot-lock PASS (2026-04-05 10:32); markdownlint PASS; frontmatter PASS; validate:rp PASS
title: Tera Solm Mind Cluster
category: admin
slug: tera-solm-mind-cluster
status: active
version: "0.1"
last_updated: 2026-04-05T10:32:00+02:00
owner: tera-solm
---

Tera Solm Mind Cluster
----------------------

Verhaltenssignatur
------------------

- `tbd` - aus dem Kurzprofil noch nicht als Signaturformel belegt.

Geistnaher Zustand
------------------

- Grundmodus: wachsam, einsatzorientiert, kompromissarm bei Zugangsdisziplin

Bekannte Entitaeten
-------------------

```yaml
known_entities:
  - observer_id: char:tera-solm
    target_id: char:helia-vorn
    target_type: character
    policy_version: v0.1.0
    known: true
    relation_status: kooperativ
    relation_note: Leitungsanker fuer Sperrlogik, Einsatzfenster und territoriale Entscheidungen
    x: 7
    y: 17
    z: 4
    normtreue: 26
    vertrauen: 58
    loyalitaet: 61
    ansehen: 51
    ruf: 9
    machtprojektion: 30
    kooperationsneigung: 38
    konfliktneigung: 16
    einfluss: 44
    bedrohung: 3
    pos_streak: 0
    neg_streak: 0
    confidence: 0.74
    volatility: 0.27
    last_updated: 2026-04-05T10:32:00+02:00
    event_id: evt:bootstrap-tera-mind-helia-0001
    reason_codes: [RC-bootstrap, RC-migration_from_character_canvas]
    applied_rules: [R-MCL-SSOT, R-MCL-DATA]
    top_contributors: [character_ssot, startbogen_b2]
  - observer_id: char:tera-solm
    target_id: char:rian-kord
    target_type: character
    policy_version: v0.1.0
    known: true
    relation_status: angespannt
    relation_note: Handelsdruck erzeugt Sicherheitskonflikte an den Freigabepunkten
    x: 1
    y: 8
    z: 1
    normtreue: 19
    vertrauen: 28
    loyalitaet: 26
    ansehen: 32
    ruf: 6
    machtprojektion: 17
    kooperationsneigung: 28
    konfliktneigung: 18
    einfluss: 25
    bedrohung: 10
    pos_streak: 0
    neg_streak: 0
    confidence: 0.67
    volatility: 0.35
    last_updated: 2026-04-05T10:32:00+02:00
    event_id: evt:bootstrap-tera-mind-rian-0001
    reason_codes: [RC-bootstrap, RC-migration_from_character_canvas]
    applied_rules: [R-MCL-SSOT, R-MCL-DATA]
    top_contributors: [character_ssot]
```