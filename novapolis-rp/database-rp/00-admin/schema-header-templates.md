---
stand: 2025-11-07 03:32
update: H1/H2 auf Setext umgestellt; Stand aktualisiert.
checks: markdownlint-cli2 PASS (single file)
---

RP Header-Templates (Frontmatter)
=================================

Hinweis
-------
- Die folgenden Frontmatter-Beispiele sind minimal und domänenspezifisch.
- Regeln/Validatoren bleiben zentral (Root) verwaltet; hier nur Metadatenanker (id/slug/category/...).
- Slugs in kebab-case; optionale Felder nur verwenden, wenn sinnvoll/gegeben.

02-characters
--------------

```yaml
---
title: <Vorname Nachname>
category: character
slug: <vorname-nachname>
version: "1.0"
last_updated: YYYY-MM-DDTHH:MM:SS+01:00
tags: []
affiliations: [novapolis]
primary_location: d5
last_seen: c6
dependencies: [reflex, lumen, echo, jonas-merek, kora-malenkov, d5, c6]
---
```

03-locations
-------------

```yaml
---
title: <Ort/Knoten>
category: location
slug: <slug>
version: "1.0"
last_updated: YYYY-MM-DDTHH:MM:SS+01:00
affiliations: [novapolis]
status: teilaktiv
connections: ["d5", "e3"]
tags: []
---
```

04-inventory
------------

```yaml
---
title: Inventar - <Fraktion/Ort>
category: inventory
slug: <slug>-inventar
owner: <novapolis|d5|c6|...>
scope: faction  # faction|location|global
version: "0.1"
last_updated: YYYY-MM-DDTHH:MM:SS+01:00
tags: []
---
```

05-projects
-----------

```yaml
---
title: <Projektname>
category: project
slug: <slug>
status: active   # planned|active|paused|done
owners: ["<char-slug>", "<char-slug>"]
locations: ["<loc-slug>", "<loc-slug>"]
dependencies: ["<artefakt-slug>"]
version: "1.0"
last_updated: YYYY-MM-DDTHH:MM:SS+01:00
tags: []
---
```

06-scenes
---------

```yaml
---
id: scene-YYYY-MM-DD-<a>
category: scene
date: YYYY-MM-DD
characters: ["<char-slug>", "<char-slug>"]
locations: ["<loc-slug>", "<loc-slug>"]
inventoryRefs: ["<inventar-slug>"]
version: "1.0"
tags: []
---
```

Hinweise zur Verwendung
-----------------------
- Keine Wiederholung von Root-Regeln in den Dateien; Metadaten genügen für Navigation/Validierung.
- Referenzen (characters/locations/dependencies) verwenden Slugs der Zielobjekte.
- Falls ein Feld unbekannt ist, weglassen statt Dummy-Werte einzutragen (Validatoren erlauben optionale Felder).


