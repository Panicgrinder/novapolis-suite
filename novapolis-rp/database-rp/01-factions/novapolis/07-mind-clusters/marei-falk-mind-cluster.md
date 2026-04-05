---
stand: 2026-04-05 19:43
update: Marei Falk fuehrt jetzt einen eigenen Mind-Cluster fuer C6-Tageskoordination, E3-Nachsorge und Kora-Abstimmung.
checks: snapshot-lock PASS (2026-04-05 10:32); markdownlint PASS; frontmatter PASS; validate:rp PASS
title: Marei Falk Mind Cluster
category: admin
slug: marei-falk-mind-cluster
status: active
version: "0.1"
last_updated: 2026-04-05T10:32:00+02:00
owner: marei-falk
---

Marei Falk Mind Cluster (Sphaerenmodell)
----------------------------------------

Zweck
-----

- SSOT fuer Mareis beziehungsnahe Lage zwischen C6-Logistik, E3-Evakuierungsnachsorge und Teamkoordination.

Quellenanker
------------

- Charakter-SSOT: `../02-characters/Marei-Falk.md`
- Startbogen C6: `../../../../../../novapolis-dev/docs/process/rp-startbogen-novapolis-c6.ssot.md`

Verhaltenssignatur (SSOT im Mind-Cluster)
-----------------------------------------

- `tbd` - aus der aktiven Charakter-SSOT noch nicht als Signaturformel belegt.

Geistnaher Zustand (SSOT im Mind-Cluster)
-----------------------------------------

- Stabilitaet: hoch in geregelten Schicht- und Versorgungsablaeufen
- Grundmodus: strukturierend, versorgungsorientiert, auf Entlastung der Leitung bedacht
- Kernleitbild: C6-Ordnung und E3-Nachsorge ohne Leerlauf halten

Bekannte Entitaeten (aequatoriale Verortung)
--------------------------------------------

```yaml
known_entities:
  - observer_id: char:marei-falk
    target_id: char:kora-malenkov
    target_type: character
    policy_version: v0.1.0
    known: true
    relation_status: kooperativ
    relation_note: direkte Leitung und engste operative Abstimmung im C6-Alltag
    x: 12
    y: 22
    z: 15
    normtreue: 21
    vertrauen: 69
    loyalitaet: 64
    ansehen: 55
    ruf: 15
    machtprojektion: 19
    kooperationsneigung: 74
    konfliktneigung: 7
    einfluss: 44
    bedrohung: -9
    pos_streak: 0
    neg_streak: 0
    confidence: 0.73
    volatility: 0.29
    last_updated: 2026-04-05T10:32:00+02:00
    event_id: evt:bootstrap-marei-mind-kora-0001
    reason_codes: [RC-bootstrap, RC-migration_from_character_canvas]
    applied_rules: [R-MCL-SSOT, R-MCL-DATA]
    top_contributors: [character_ssot, startbogen_c6]
  - observer_id: char:marei-falk
    target_id: char:ronja-kerschner
    target_type: character
    policy_version: v0.1.0
    known: true
    relation_status: kooperativ
    relation_note: Fraktionsleitung und Freigabeanker fuer groessere Versorgungsentscheidungen
    x: 9
    y: 19
    z: 13
    normtreue: 24
    vertrauen: 58
    loyalitaet: 48
    ansehen: 57
    ruf: 14
    machtprojektion: 25
    kooperationsneigung: 63
    konfliktneigung: 8
    einfluss: 39
    bedrohung: -6
    pos_streak: 0
    neg_streak: 0
    confidence: 0.70
    volatility: 0.31
    last_updated: 2026-04-05T10:32:00+02:00
    event_id: evt:bootstrap-marei-mind-ronja-0001
    reason_codes: [RC-bootstrap, RC-migration_from_character_canvas]
    applied_rules: [R-MCL-SSOT, R-MCL-DATA]
    top_contributors: [character_ssot]
  - observer_id: char:marei-falk
    target_id: char:echo
    target_type: character
    policy_version: v0.1.0
    known: true
    relation_status: kooperativ
    relation_note: plant Abläufe um Echo-Naeheprotokolle herum und behandelt die Instanz als echten C6-Faktor
    x: 10
    y: 18
    z: 14
    normtreue: 17
    vertrauen: 54
    loyalitaet: 41
    ansehen: 42
    ruf: 10
    machtprojektion: 14
    kooperationsneigung: 62
    konfliktneigung: 5
    einfluss: 28
    bedrohung: -5
    pos_streak: 0
    neg_streak: 0
    confidence: 0.68
    volatility: 0.30
    last_updated: 2026-04-05T10:32:00+02:00
    event_id: evt:bootstrap-marei-mind-echo-0001
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
  confidence: 0.70
  volatility: 0.30
  last_updated: 2026-04-05T10:32:00+02:00
  event_id: evt:bootstrap-marei-mind-0001
  reason_codes: [RC-bootstrap, RC-migration_from_character_canvas]
  applied_rules: [R-MCL-SSOT, R-MCL-DATA]
  top_contributors: [character_ssot, startkorridor_ssot]
```