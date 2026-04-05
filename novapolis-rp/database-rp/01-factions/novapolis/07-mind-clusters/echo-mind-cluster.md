---
stand: 2026-04-05 19:43
update: Echo fuehrt jetzt einen eigenen Mind-Cluster fuer Kora-Kopplung, Instanzschutz und gefilterte D5-Bezuege.
checks: snapshot-lock PASS (2026-04-05 08:10); markdownlint PASS; frontmatter PASS; validate:rp PASS
title: Echo Mind Cluster
category: admin
slug: echo-mind-cluster
status: active
version: "0.1"
last_updated: 2026-04-05T08:10:00+02:00
owner: echo
---

Echo Mind Cluster (Sphaerenmodell)
----------------------------------

Zweck
-----

- SSOT fuer Echos beziehungsnahe Startlage im lokalen C6-Schutznetz.

Quellenanker
------------

- Charakter-SSOT: `../02-characters/Echo.md`
- Startbogen C6: `../../../../../../novapolis-dev/docs/process/rp-startbogen-novapolis-c6.ssot.md`
- Charakter-SSOT Reflex: `../02-characters/Reflex.md`

Verhaltenssignatur (SSOT im Mind-Cluster)
-----------------------------------------

- `ECO1=L85-S74-T62-E58-N52-O44-C28-M16-P30-ks`
- Lesart: enge, kindlich-selbstlose Schutzinstanz mit hoher Bindungs- und Abschirmungstendenz.

Geistnaher Zustand (SSOT im Mind-Cluster)
-----------------------------------------

- Stabilitaet: lokal stabil bei Koerpernaehe, deutlich fragiler bei Distanz
- Grundmodus: leise, beobachtend, assistierend
- Eskalationsmuster: schuetzt zuerst Kora, deutet Fremdnaehe frueh als potentielles Risiko
- Kernleitbild: Naehe halten, Signale filtern, Kora nicht offen lassen

Bekannte Entitaeten (aequatoriale Verortung)
--------------------------------------------

```yaml
known_entities:
  - observer_id: char:echo
    target_id: char:kora-malenkov
    target_type: character
    policy_version: v0.1.0
    known: true
    relation_status: kooperativ
    relation_note: primäre Bezugsperson; Echo ordnet Schutz, Naehe und Alarmverhalten strikt um Kora herum
    x: 24
    y: 38
    z: 21
    normtreue: 23
    vertrauen: 90
    loyalitaet: 94
    ansehen: 58
    ruf: 14
    machtprojektion: 17
    kooperationsneigung: 87
    konfliktneigung: 6
    einfluss: 61
    bedrohung: -27
    pos_streak: 0
    neg_streak: 0
    confidence: 0.79
    volatility: 0.29
    last_updated: 2026-04-05T08:10:00+02:00
    event_id: evt:bootstrap-echo-mind-kora-0001
    reason_codes: [RC-bootstrap, RC-migration_from_character_canvas]
    applied_rules: [R-MCL-SSOT, R-MCL-DATA]
    top_contributors: [character_ssot, startbogen_c6]
  - observer_id: char:echo
    target_id: char:reflex
    target_type: character
    policy_version: v0.1.0
    known: true
    relation_status: kooperativ
    relation_note: Primärinstanz und Referenz fuer Schutz- und Signallogik
    x: 18
    y: 27
    z: 15
    normtreue: 19
    vertrauen: 71
    loyalitaet: 63
    ansehen: 55
    ruf: 11
    machtprojektion: 26
    kooperationsneigung: 73
    konfliktneigung: 8
    einfluss: 49
    bedrohung: -12
    pos_streak: 0
    neg_streak: 0
    confidence: 0.74
    volatility: 0.31
    last_updated: 2026-04-05T08:10:00+02:00
    event_id: evt:bootstrap-echo-mind-reflex-0001
    reason_codes: [RC-bootstrap, RC-migration_from_character_canvas]
    applied_rules: [R-MCL-SSOT, R-MCL-DATA]
    top_contributors: [character_ssot, startbogen_c6]
  - observer_id: char:echo
    target_id: char:ronja-kerschner
    target_type: character
    policy_version: v0.1.0
    known: true
    relation_status: kooperativ
    relation_note: entfernte Leitungsreferenz ueber Reflex- und Kora-Kontext; Schutzbezug bleibt indirekt
    x: 9
    y: 18
    z: 11
    normtreue: 17
    vertrauen: 43
    loyalitaet: 36
    ansehen: 42
    ruf: 10
    machtprojektion: 18
    kooperationsneigung: 48
    konfliktneigung: 9
    einfluss: 24
    bedrohung: -3
    pos_streak: 0
    neg_streak: 0
    confidence: 0.66
    volatility: 0.34
    last_updated: 2026-04-05T08:10:00+02:00
    event_id: evt:bootstrap-echo-mind-ronja-0001
    reason_codes: [RC-bootstrap, RC-migration_from_character_canvas]
    applied_rules: [R-MCL-SSOT, R-MCL-DATA]
    top_contributors: [character_ssot, startbogen_c6]
```

Audit-Felder (Template)
-----------------------

```yaml
audit:
  policy_version: v0.1.0
  pos_streak: 0
  neg_streak: 0
  confidence: 0.73
  volatility: 0.31
  last_updated: 2026-04-05T08:10:00+02:00
  event_id: evt:bootstrap-echo-mind-0001
  reason_codes: [RC-bootstrap, RC-migration_from_character_canvas]
  applied_rules: [R-MCL-SSOT, R-MCL-DATA]
  top_contributors: [character_ssot, startkorridor_ssot]
```