---
stand: 2026-04-05 19:43
update: Arlen Dross fuehrt jetzt einen eigenen Mind-Cluster fuer Diplomatie, Karawanenmoderation und C6-Verbundkontakte.
checks: snapshot-lock PASS (2026-04-05 10:32); markdownlint PASS; frontmatter PASS; validate:rp PASS
title: Arlen Dross Mind Cluster
category: admin
slug: arlen-dross-mind-cluster
status: active
version: "0.1"
last_updated: 2026-04-05T10:32:00+02:00
owner: arlen-dross
---

Arlen Dross Mind Cluster (Sphaerenmodell)
-----------------------------------------

Zweck
-----

- SSOT fuer Arlens beziehungsnahe Lage zwischen Karawanendiplomatie, C6-Moderation und Novapolis-Anschluss.

Quellenanker
------------

- Charakter-SSOT: `../02-characters/Arlen-Dross.md`
- Startbogen G7: `../../../../../../novapolis-dev/docs/process/rp-startbogen-haendlerbund-g7.ssot.md`
- Startbogen C6: `../../../../../../novapolis-dev/docs/process/rp-startbogen-novapolis-c6.ssot.md`

Verhaltenssignatur (SSOT im Mind-Cluster)
-----------------------------------------

- `ARD5=L67-T72-N74-E58-O66-C71-M48-P40-db`
- Lesart: ausgleichender Vermittler mit hohem Freiheitsdrang, der Risiken lieber verhandelt als frontal austrägt.

Geistnaher Zustand (SSOT im Mind-Cluster)
-----------------------------------------

- Stabilitaet: funktional, aber unter Kontroll- und Loyalitaetsdruck spuerbar angespannt
- Grundmodus: moderierend, abwaegend, schriftlich absichernd
- Kernleitbild: Handelsfreiheit sichern, ohne Crew oder Novapolis zu destabilisieren

Bekannte Entitaeten (aequatoriale Verortung)
--------------------------------------------

```yaml
known_entities:
  - observer_id: char:arlen-dross
    target_id: char:marven-kael
    target_type: character
    policy_version: v0.1.0
    known: true
    relation_status: kooperativ
    relation_note: strategischer Partner fuer Verhandlungen und Rueckfallentscheide
    x: 14
    y: 24
    z: 17
    normtreue: 16
    vertrauen: 71
    loyalitaet: 67
    ansehen: 58
    ruf: 19
    machtprojektion: 26
    kooperationsneigung: 77
    konfliktneigung: 8
    einfluss: 46
    bedrohung: -11
    pos_streak: 0
    neg_streak: 0
    confidence: 0.74
    volatility: 0.30
    last_updated: 2026-04-05T10:32:00+02:00
    event_id: evt:bootstrap-arlen-mind-marven-0001
    reason_codes: [RC-bootstrap, RC-migration_from_character_canvas]
    applied_rules: [R-MCL-SSOT, R-MCL-DATA]
    top_contributors: [character_ssot, startbogen_g7]
  - observer_id: char:arlen-dross
    target_id: char:kora-malenkov
    target_type: character
    policy_version: v0.1.0
    known: true
    relation_status: kooperativ
    relation_note: operative C6-Schnittstelle mit klaren Zustaendigkeiten und hoher Lagebindung
    x: 9
    y: 19
    z: 13
    normtreue: 18
    vertrauen: 58
    loyalitaet: 42
    ansehen: 51
    ruf: 17
    machtprojektion: 23
    kooperationsneigung: 63
    konfliktneigung: 10
    einfluss: 39
    bedrohung: -6
    pos_streak: 0
    neg_streak: 0
    confidence: 0.71
    volatility: 0.31
    last_updated: 2026-04-05T10:32:00+02:00
    event_id: evt:bootstrap-arlen-mind-kora-0001
    reason_codes: [RC-bootstrap, RC-migration_from_character_canvas]
    applied_rules: [R-MCL-SSOT, R-MCL-DATA]
    top_contributors: [character_ssot, startbogen_c6]
  - observer_id: char:arlen-dross
    target_id: char:ronja-kerschner
    target_type: character
    policy_version: v0.1.0
    known: true
    relation_status: kooperativ
    relation_note: primäre Verhandlungspartnerin Novapolis-seitig; respektiert ihre Leitung, prueft aber Folgen streng nach
    x: 8
    y: 21
    z: 12
    normtreue: 20
    vertrauen: 54
    loyalitaet: 35
    ansehen: 56
    ruf: 18
    machtprojektion: 29
    kooperationsneigung: 61
    konfliktneigung: 9
    einfluss: 42
    bedrohung: -4
    pos_streak: 0
    neg_streak: 0
    confidence: 0.70
    volatility: 0.33
    last_updated: 2026-04-05T10:32:00+02:00
    event_id: evt:bootstrap-arlen-mind-ronja-0001
    reason_codes: [RC-bootstrap, RC-migration_from_character_canvas]
    applied_rules: [R-MCL-SSOT, R-MCL-DATA]
    top_contributors: [character_ssot, startbogen_g7]
```

Audit-Felder (Template)
-----------------------

```yaml
audit:
  policy_version: v0.1.0
  pos_streak: 0
  neg_streak: 0
  confidence: 0.72
  volatility: 0.31
  last_updated: 2026-04-05T10:32:00+02:00
  event_id: evt:bootstrap-arlen-mind-0001
  reason_codes: [RC-bootstrap, RC-migration_from_character_canvas]
  applied_rules: [R-MCL-SSOT, R-MCL-DATA]
  top_contributors: [character_ssot, startkorridor_ssot]
```