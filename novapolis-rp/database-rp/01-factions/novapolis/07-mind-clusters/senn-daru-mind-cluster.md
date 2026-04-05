---
stand: 2026-04-05 19:43
update: Senn Daru fuehrt jetzt einen eigenen Mind-Cluster fuer C6-Erstkontakte, Handelsanbahnung und H-47-Anschluss.
checks: snapshot-lock PASS (2026-04-05 10:32); markdownlint PASS; frontmatter PASS; validate:rp PASS
title: Senn Daru Mind Cluster
category: admin
slug: senn-daru-mind-cluster
status: active
version: "0.1"
last_updated: 2026-04-05T10:32:00+02:00
owner: senn-daru
---

Senn Daru Mind Cluster (Sphaerenmodell)
---------------------------------------

Zweck
-----

- SSOT fuer Senns beziehungsnahe Lage als C6-Erstkontakt zwischen Karawane, Haendlerbund und Novapolis.

Quellenanker
------------

- Charakter-SSOT: `../02-characters/Senn-Daru.md`
- Startbogen G7: `../../../../../../novapolis-dev/docs/process/rp-startbogen-haendlerbund-g7.ssot.md`

Verhaltenssignatur (SSOT im Mind-Cluster)
-----------------------------------------

- `SND1=E72-N64-L58-O46-S42-T38-C30-M22-P44-s`
- Lesart: empathischer Vermittler mit offener Neugier und niedriger Dominanz.

Geistnaher Zustand (SSOT im Mind-Cluster)
-----------------------------------------

- Stabilitaet: hoch in persoenlichen Kontaktlagen, offen fuer neue Bindungen bei klaren Regeln
- Grundmodus: freundlich, vermittelnd, kontaktstiftend
- Kernleitbild: Zugang schaffen, ohne C6-Freigaben zu verletzen

Bekannte Entitaeten (aequatoriale Verortung)
--------------------------------------------

```yaml
known_entities:
  - observer_id: char:senn-daru
    target_id: char:marven-kael
    target_type: character
    policy_version: v0.1.0
    known: true
    relation_status: kooperativ
    relation_note: Karawanenanker fuer operative Verantwortung und Rueckhalt
    x: 12
    y: 20
    z: 14
    normtreue: 18
    vertrauen: 66
    loyalitaet: 58
    ansehen: 49
    ruf: 15
    machtprojektion: 21
    kooperationsneigung: 71
    konfliktneigung: 7
    einfluss: 37
    bedrohung: -8
    pos_streak: 0
    neg_streak: 0
    confidence: 0.72
    volatility: 0.30
    last_updated: 2026-04-05T10:32:00+02:00
    event_id: evt:bootstrap-senn-mind-marven-0001
    reason_codes: [RC-bootstrap, RC-migration_from_character_canvas]
    applied_rules: [R-MCL-SSOT, R-MCL-DATA]
    top_contributors: [character_ssot, startbogen_g7]
  - observer_id: char:senn-daru
    target_id: char:ronja-kerschner
    target_type: character
    policy_version: v0.1.0
    known: true
    relation_status: neutral
    relation_note: kennt Novapolis ueber C6-Erstkontakt, aber ohne tiefe Freigaben oder Bindung
    x: 5
    y: 14
    z: 11
    normtreue: 17
    vertrauen: 38
    loyalitaet: 24
    ansehen: 41
    ruf: 11
    machtprojektion: 12
    kooperationsneigung: 49
    konfliktneigung: 6
    einfluss: 22
    bedrohung: -1
    pos_streak: 0
    neg_streak: 0
    confidence: 0.64
    volatility: 0.32
    last_updated: 2026-04-05T10:32:00+02:00
    event_id: evt:bootstrap-senn-mind-ronja-0001
    reason_codes: [RC-bootstrap, RC-migration_from_character_canvas]
    applied_rules: [R-MCL-SSOT, R-MCL-DATA]
    top_contributors: [character_ssot]
```

Audit-Felder (Template)
-----------------------

```yaml
audit:
  policy_version: v0.1.0
  pos_streak: 0
  neg_streak: 0
  confidence: 0.68
  volatility: 0.31
  last_updated: 2026-04-05T10:32:00+02:00
  event_id: evt:bootstrap-senn-mind-0001
  reason_codes: [RC-bootstrap, RC-migration_from_character_canvas]
  applied_rules: [R-MCL-SSOT, R-MCL-DATA]
  top_contributors: [character_ssot, startbogen_g7]
```