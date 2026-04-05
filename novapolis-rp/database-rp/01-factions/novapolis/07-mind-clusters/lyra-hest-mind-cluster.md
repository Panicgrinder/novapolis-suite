---
stand: 2026-04-05 19:43
update: Lyra Hest fuehrt jetzt einen eigenen Mind-Cluster fuer zivile Leitung, Logistikkoordination und D5-C6-Abgleich.
checks: snapshot-lock PASS (2026-04-05 10:32); markdownlint PASS; frontmatter PASS; validate:rp PASS
title: Lyra Hest Mind Cluster
category: admin
slug: lyra-hest-mind-cluster
status: active
version: "0.1"
last_updated: 2026-04-05T10:32:00+02:00
owner: lyra-hest
---

Lyra Hest Mind Cluster (Sphaerenmodell)
---------------------------------------

Zweck
-----

- SSOT fuer Lyras beziehungsnahe Lage zwischen ziviler Leitung, D5-C6-Logistik und Stellvertretungsfunktion.

Quellenanker
------------

- Charakter-SSOT: `../02-characters/Lyra-Hest.md`
- Charakter-SSOT Varek: `../../eisenkonklave/02-characters/Varek-Solun.md`

Verhaltenssignatur (SSOT im Mind-Cluster)
-----------------------------------------

- `LYH1=O74-L68-T62-E58-S54-N46-M32-C28-P48-r`
- Lesart: strukturierte Logistikerin mit Loyalitaetskern und ruhigem Krisenmanagement.

Geistnaher Zustand (SSOT im Mind-Cluster)
-----------------------------------------

- Stabilitaet: hoch in geordneten Prozess- und Versorgungslagen
- Grundmodus: koordinierend, abwägend, institutionsnah
- Kernleitbild: Zivilschicht und Versorgung auch unter Mehrortdruck stabil halten

Bekannte Entitaeten (aequatoriale Verortung)
--------------------------------------------

```yaml
known_entities:
  - observer_id: char:lyra-hest
    target_id: char:varek-solun
    target_type: character
    policy_version: v0.1.0
    known: true
    relation_status: kooperativ
    relation_note: strategischer Leitungsanker; Lyra arbeitet im zivil-logistischen Stellvertretungsrahmen fuer ihn
    x: 11
    y: 20
    z: 13
    normtreue: 24
    vertrauen: 61
    loyalitaet: 66
    ansehen: 58
    ruf: 14
    machtprojektion: 27
    kooperationsneigung: 64
    konfliktneigung: 7
    einfluss: 43
    bedrohung: -7
    pos_streak: 0
    neg_streak: 0
    confidence: 0.71
    volatility: 0.28
    last_updated: 2026-04-05T10:32:00+02:00
    event_id: evt:bootstrap-lyra-mind-varek-0001
    reason_codes: [RC-bootstrap, RC-migration_from_character_canvas]
    applied_rules: [R-MCL-SSOT, R-MCL-DATA]
    top_contributors: [character_ssot]
  - observer_id: char:lyra-hest
    target_id: char:ronja-kerschner
    target_type: character
    policy_version: v0.1.0
    known: true
    relation_status: neutral
    relation_note: kennt Ronja als benachbarte Logistik- und Leitungsreferenz, aber ohne tiefen Beziehungsbeleg
    x: 4
    y: 12
    z: 8
    normtreue: 18
    vertrauen: 34
    loyalitaet: 26
    ansehen: 37
    ruf: 9
    machtprojektion: 16
    kooperationsneigung: 42
    konfliktneigung: 8
    einfluss: 23
    bedrohung: -2
    pos_streak: 0
    neg_streak: 0
    confidence: 0.63
    volatility: 0.29
    last_updated: 2026-04-05T10:32:00+02:00
    event_id: evt:bootstrap-lyra-mind-ronja-0001
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
  confidence: 0.67
  volatility: 0.28
  last_updated: 2026-04-05T10:32:00+02:00
  event_id: evt:bootstrap-lyra-mind-0001
  reason_codes: [RC-bootstrap, RC-migration_from_character_canvas]
  applied_rules: [R-MCL-SSOT, R-MCL-DATA]
  top_contributors: [character_ssot]
```