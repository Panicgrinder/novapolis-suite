---
stand: 2026-02-23 03:55
update: Frische-Review durchgeführt; Header-Templates und Tag-Referenz weiterhin gültig (kein Kanon-Delta).
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-rp/database-rp/00-admin/schema-header-templates.md' PASS (2026-02-23 03:56); .\\.venv\\Scripts\\python.exe scripts\\check_frontmatter.py 'novapolis-rp/database-rp/00-admin/schema-header-templates.md' PASS (2026-02-23 03:56); npm --prefix novapolis-rp/coding/tools/validators run validate:rp PASS (2026-02-23 03:56)
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
owners: ["<faction-slug>"]  # Owner ist die zustaendige Fraktion
authority_chain:
  - "fraktion:<faction-slug>"
  - "fraktions-leitung:<char-slug>"
  - "stellv-fraktions-leitung:<char-slug>"
  - "leitung-sicherheit:<char-slug>"
  - "leitung-logistik:<char-slug>"
  - "rolle:<char-slug>"          # optional mehrfach
  - "stationsleitung:<char-slug>"
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
- Bei Projekten ist `owners` der Fraktions-Slug; operative Befehlsgewalt wird in `authority_chain` in der festen Reihenfolge dokumentiert.
- Falls ein Feld unbekannt ist, weglassen statt Dummy-Werte einzutragen (Validatoren erlauben optionale Felder).
- Gültige Tag-Werte und Startersets werden zentral in `00-admin/Tags-Taxonomie.md` gepflegt.


