---
stand: 2026-04-05 19:43
update: Marven Kael fuehrt jetzt einen eigenen Mind-Cluster fuer Konvoisicherheit, Kora-Abgleich und Novapolis-Verhandlung.
checks: snapshot-lock PASS (2026-04-05 10:32); markdownlint PASS; frontmatter PASS; validate:rp PASS
title: Marven Kael Mind Cluster
category: admin
slug: marven-kael-mind-cluster
status: active
version: "0.1"
last_updated: 2026-04-05T10:32:00+02:00
owner: marven-kael
---

Marven Kael Mind Cluster (Sphaerenmodell)
-----------------------------------------

Zweck
-----

- SSOT fuer Marvens beziehungsnahe Lage zwischen Karawanenfuehrung, C6-Basis und kontrollierter Novapolis-Kooperation.

Quellenanker
------------

- Charakter-SSOT: `../02-characters/Marven-Kael.md`
- Startbogen G7: `../../../../../../novapolis-dev/docs/process/rp-startbogen-haendlerbund-g7.ssot.md`
- Startbogen C6: `../../../../../../novapolis-dev/docs/process/rp-startbogen-novapolis-c6.ssot.md`

Verhaltenssignatur (SSOT im Mind-Cluster)
-----------------------------------------

- `MRV2=L62-T55-N80-E58-O66-C70-M42-P50-qa`
- Lesart: vorsichtiger Stratege mit hoher Crew-Loyalitaet und ausgepraegtem Risikofokus.

Geistnaher Zustand (SSOT im Mind-Cluster)
-----------------------------------------

- Stabilitaet: hoch in strukturierten Lagebildern, langsamer unter plötzlichem Risiko
- Grundmodus: prüfend, absichernd, rueckzugsorientiert
- Kernleitbild: Crew und Konvoi nur ueber belastbare Allianzen exponieren

Bekannte Entitaeten (aequatoriale Verortung)
--------------------------------------------

```yaml
known_entities:
  - observer_id: char:marven-kael
    target_id: char:arlen-dross
    target_type: character
    policy_version: v0.1.0
    known: true
    relation_status: kooperativ
    relation_note: diplomatischer Partner, der Risikoanalysen in verhandelbare Pfade ueberfuehrt
    x: 14
    y: 25
    z: 16
    normtreue: 18
    vertrauen: 74
    loyalitaet: 65
    ansehen: 55
    ruf: 21
    machtprojektion: 24
    kooperationsneigung: 72
    konfliktneigung: 8
    einfluss: 47
    bedrohung: -10
    pos_streak: 0
    neg_streak: 0
    confidence: 0.75
    volatility: 0.29
    last_updated: 2026-04-05T10:32:00+02:00
    event_id: evt:bootstrap-marven-mind-arlen-0001
    reason_codes: [RC-bootstrap, RC-migration_from_character_canvas]
    applied_rules: [R-MCL-SSOT, R-MCL-DATA]
    top_contributors: [character_ssot, startbogen_g7]
  - observer_id: char:marven-kael
    target_id: char:kora-malenkov
    target_type: character
    policy_version: v0.1.0
    known: true
    relation_status: kooperativ
    relation_note: zentrale C6-Schnittstelle fuer Uebergaben und Lageabgleich
    x: 10
    y: 20
    z: 11
    normtreue: 17
    vertrauen: 57
    loyalitaet: 39
    ansehen: 50
    ruf: 18
    machtprojektion: 22
    kooperationsneigung: 59
    konfliktneigung: 10
    einfluss: 38
    bedrohung: -4
    pos_streak: 0
    neg_streak: 0
    confidence: 0.72
    volatility: 0.31
    last_updated: 2026-04-05T10:32:00+02:00
    event_id: evt:bootstrap-marven-mind-kora-0001
    reason_codes: [RC-bootstrap, RC-migration_from_character_canvas]
    applied_rules: [R-MCL-SSOT, R-MCL-DATA]
    top_contributors: [character_ssot, startbogen_c6]
  - observer_id: char:marven-kael
    target_id: char:ronja-kerschner
    target_type: character
    policy_version: v0.1.0
    known: true
    relation_status: kooperativ
    relation_note: strategische Verhandlungspartnerin; Kooperation nur mit klaren Belegen und Rueckfalloptionen
    x: 7
    y: 19
    z: 10
    normtreue: 19
    vertrauen: 49
    loyalitaet: 31
    ansehen: 53
    ruf: 17
    machtprojektion: 28
    kooperationsneigung: 54
    konfliktneigung: 11
    einfluss: 41
    bedrohung: -2
    pos_streak: 0
    neg_streak: 0
    confidence: 0.70
    volatility: 0.33
    last_updated: 2026-04-05T10:32:00+02:00
    event_id: evt:bootstrap-marven-mind-ronja-0001
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
  event_id: evt:bootstrap-marven-mind-0001
  reason_codes: [RC-bootstrap, RC-migration_from_character_canvas]
  applied_rules: [R-MCL-SSOT, R-MCL-DATA]
  top_contributors: [character_ssot, startkorridor_ssot]
```