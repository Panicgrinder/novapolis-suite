---
stand: 2026-02-25 18:33
update: Known-Entities auf strikte Per-Relation-Pflichtfelder und char:-ID-Namespace umgestellt.
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-rp/database-rp/01-factions/novapolis/07-mind-clusters/ronja-kerschner-mind-cluster.md' 'novapolis-dev/docs/donelog.md' PASS (2026-02-24 16:17); .\.venv\Scripts\python.exe scripts\check_frontmatter.py 'novapolis-rp/database-rp/01-factions/novapolis/07-mind-clusters/ronja-kerschner-mind-cluster.md' 'novapolis-dev/docs/donelog.md' PASS (2026-02-24 16:17); npm --prefix novapolis-rp/coding/tools/validators run validate:rp PASS (2026-02-24 16:17)
title: Ronja Kerschner Mind Cluster
category: admin
slug: ronja-kerschner-mind-cluster
status: active
version: "0.1"
last_updated: 2026-02-24T15:00:00+01:00
owner: ronja-kerschner
---

Ronja Kerschner Mind Cluster (Sphaerenmodell)
---------------------------------------------

Zweck
-----
- SSOT fuer beziehungsnahe Zustandsdaten von Ronja Kerschner.
- Enthaelt die aequatoriale Verortung bekannter Entitaeten plus geistnahen Zustand.

Quellenanker
------------
- Charakter-SSOT: `../02-characters/Ronja-Kerschner.md`
- Verhalten: `../../../00-admin/AI-Behavior-Mapping.md`
- Kampagnenregeln: `../../../00-admin/Reference-Campaign-State.md`

Verhaltenssignatur (SSOT im Mind-Cluster)
-----------------------------------------
- `R4=O82-T79-L70-E60-N69-C45-S38-M20-kpr`
- Lesart: kontrollierte, aber erschoepfte Technikerin (RAW `char_ronja_v2`).

Geistnaher Zustand (SSOT im Mind-Cluster)
-----------------------------------------
- Gesundheit: stabil
- Geistiger Zustand: instabil, aber funktional
- Erholungsbedarf: hoch
- Belastungsmanagement: planbare Ruhephasen priorisieren; sonst steigt Risiko fuer Sinnzweifel/Ueberreaktionen.
- Kernleitbild: hell/geordnet/lebendig machen

Bekannte Entitaeten (aequatoriale Verortung)
---------------------------------------------

```yaml
known_entities:
  - observer_id: char:ronja-kerschner
    target_id: char:reflex
    target_type: character
    policy_version: v0.1.0
    known: true
    relation_status: kooperativ
    relation_note: symbiotisch, behutsame Grenzen, gelegentlich besitzergreifend
    x: 18
    y: 36
    z: 14
    normtreue: 22
    vertrauen: 72
    loyalitaet: 81
    ansehen: 63
    ruf: 34
    machtprojektion: 28
    kooperationsneigung: 76
    konfliktneigung: 19
    einfluss: 69
    bedrohung: 27
    pos_streak: 0
    neg_streak: 0
    confidence: 0.68
    volatility: 0.36
    last_updated: 2026-02-24T15:00:00+01:00
    event_id: evt:bootstrap-ronja-mind-reflex-0001
    reason_codes: [bootstrap, migration_from_character_canvas]
    applied_rules: [R-MCL-SSOT, R-MCL-DATA]
    top_contributors: [ai_behavior_signature, campaign_state]
  - observer_id: char:ronja-kerschner
    target_id: char:jonas-merek
    target_type: character
    policy_version: v0.1.0
    known: true
    relation_status: kooperativ
    relation_note: vorsichtiger Vertrauensvorschuss
    x: 9
    y: 21
    z: 17
    normtreue: 19
    vertrauen: 46
    loyalitaet: 34
    ansehen: 52
    ruf: 22
    machtprojektion: 11
    kooperationsneigung: 49
    konfliktneigung: 12
    einfluss: 24
    bedrohung: -8
    pos_streak: 0
    neg_streak: 0
    confidence: 0.68
    volatility: 0.36
    last_updated: 2026-02-24T15:00:00+01:00
    event_id: evt:bootstrap-ronja-mind-jonas-0001
    reason_codes: [bootstrap, migration_from_character_canvas]
    applied_rules: [R-MCL-SSOT, R-MCL-DATA]
    top_contributors: [ai_behavior_signature, campaign_state]
  - observer_id: char:ronja-kerschner
    target_id: char:pahl-brenner
    target_type: character
    policy_version: v0.1.0
    known: true
    relation_status: angespannt
    relation_note: in Pflege, wertvolle Erfahrung
    x: -6
    y: 12
    z: 8
    normtreue: 14
    vertrauen: 23
    loyalitaet: 18
    ansehen: 47
    ruf: 17
    machtprojektion: 31
    kooperationsneigung: 26
    konfliktneigung: 41
    einfluss: 37
    bedrohung: 11
    pos_streak: 0
    neg_streak: 0
    confidence: 0.68
    volatility: 0.36
    last_updated: 2026-02-24T15:00:00+01:00
    event_id: evt:bootstrap-ronja-mind-pahl-0001
    reason_codes: [bootstrap, migration_from_character_canvas]
    applied_rules: [R-MCL-SSOT, R-MCL-DATA]
    top_contributors: [ai_behavior_signature, campaign_state]
```

Audit-Felder (Template)
-----------------------

```yaml
audit:
  policy_version: v0.1.0
  pos_streak: 0
  neg_streak: 0
  confidence: 0.68
  volatility: 0.36
  last_updated: 2026-02-24T15:00:00+01:00
  event_id: evt:bootstrap-ronja-mind-0001
  reason_codes: [bootstrap, migration_from_character_canvas]
  applied_rules: [R-MCL-SSOT, R-MCL-DATA]
  top_contributors: [ai_behavior_signature, campaign_state]
```
