#!/usr/bin/env python3
"""
Enrich sidecar JSON metadata from Markdown (YAML Front Matter aware)
- Scans repo for *.md with sibling *.json
- Parses YAML Front Matter between '---' fences (top of file)
    Supported keys:
        title: str
        category: enum {admin, canon, character, location, inventory, project, scene}
        slug: str
        version: str
        last_updated: str (ISO-8601 with TZ)
        last_change: str (optional)
        tags: [str]
        affiliations: [str]
        locations: [str]
        characters: [str]  (only for scenes)
        dependencies: [str]
- Extracts first H1 ('# ') as fallback title
- Writes sidecar JSON with new schema; migrates away from legacy keys:
        - remove 'chapter'; map to 'title' if needed
        - remove singular 'location'; map into 'locations'
        - drop 'characters' for non-scene docs
- Does NOT touch Markdown
- Skips database-raw/99-exports and common tool folders
"""
from __future__ import annotations
import json
import os
import re
from pathlib import Path
from typing import Any, Dict, List, Tuple, Optional

ROOT = Path(os.getcwd()).resolve()
SKIP_DIRS = {
    'node_modules', '.git', '.venv', '.vscode', '.idea', '.DS_Store',
    'database-raw/99-exports'
}

FRONTMATTER_MAX_LINES = 200  # safety cap

ALLOWED_CATEGORIES = {"admin", "canon", "character", "location", "inventory", "project", "scene"}


def relp(p: Path) -> str:
    return p.relative_to(ROOT).as_posix()


def should_skip_dir(d: Path) -> bool:
    if d == ROOT:
        return False
    rp = relp(d)
    for s in SKIP_DIRS:
        if rp == s or rp.startswith(s + '/'):
            return True
    return False


def parse_bracket_list(val: str) -> List[str]:
    # Example: [A, B, C]
    inner = val.strip().strip('[]').strip()
    if not inner:
        return []
    return [x.strip().strip('"\'') for x in inner.split(',') if x.strip()]


def parse_front_matter(lines: List[str]) -> Dict[str, Any]:
    """Parse YAML-like front matter between the first two '---' fences.
    Supports simple key: value pairs, bracket lists, and dash lists.
    Returns empty dict if no fenced block is found at top.
    """
    data: Dict[str, Any] = {}
    if not lines:
        return data
    # Find first fence at or near top
    start = None
    for idx, ln in enumerate(lines[:FRONTMATTER_MAX_LINES]):
        if ln.strip() == '---':
            start = idx
            break
        if ln.strip().startswith('#') and idx < 5:
            # H1 before fence → assume no front matter
            return {}
        if ln.strip():
            # first non-empty non-fence line before any fence
            # treat as no front matter
            if idx < 5:
                return {}
    if start is None:
        return {}
    # Find end fence
    end = None
    for j in range(start + 1, min(len(lines), start + FRONTMATTER_MAX_LINES)):
        if lines[j].strip() == '---':
            end = j
            break
    if end is None:
        return {}

    # Parse block between start+1 and end-1
    i = start + 1
    while i < end:
        line = lines[i].rstrip('\n')
        if not line.strip():
            i += 1
            continue
        if ':' in line:
            key, val = line.split(':', 1)
            k = key.strip()
            v = val.strip()
            if v == '':
                # Possibly a YAML-style list follows (- item)
                items: List[str] = []
                j = i + 1
                while j < end:
                    nxt = lines[j].rstrip('\n')
                    if not nxt.strip():
                        j += 1
                        continue
                    if nxt.lstrip().startswith('- '):
                        # keep raw token, strip quotes
                        tok = nxt.split('- ', 1)[1].strip().strip("'\"")
                        items.append(tok)
                        j += 1
                        continue
                    # stop at next key-like
                    if ':' in nxt:
                        break
                    break
                data[k] = items
                i = j
                continue
            else:
                # inline value; support bracket lists
                if v.startswith('[') and v.endswith(']'):
                    data[k] = parse_bracket_list(v)
                else:
                    data[k] = v.strip().strip("'\"")
        i += 1
    return data


def extract_h1(lines: List[str]) -> Optional[str]:
    for ln in lines:
        if ln.startswith('# '):
            return ln[2:].strip()
    return None


def load_json(p: Path) -> Dict[str, Any]:
    try:
        return json.loads(p.read_text(encoding='utf-8'))
    except Exception:
        return {}


def save_json(p: Path, obj: Dict[str, Any]) -> None:
    p.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')


def derive_category_from_path(md_path: Path) -> Optional[str]:
    rp = relp(md_path)
    # database-rp/<nn>-<name>/...
    parts = rp.split('/')
    if len(parts) < 2:
        return None
    bucket = parts[1].lower()
    if bucket.startswith('00-'):
        return 'admin'
    if bucket.startswith('01-'):
        return 'canon'
    if bucket.startswith('02-'):
        return 'character'
    if bucket.startswith('03-'):
        return 'location'
    if bucket.startswith('04-'):
        return 'inventory'
    if bucket.startswith('05-'):
        return 'project'
    if bucket.startswith('06-'):
        return 'scene'
    return None


def make_slug_from_filename(md_path: Path) -> str:
    name = md_path.stem
    # Normalize: replace spaces with '-', lower, umlauts
    trans = (
        ('ä', 'ae'), ('ö', 'oe'), ('ü', 'ue'), ('ß', 'ss'),
        ('Ä', 'ae'), ('Ö', 'oe'), ('Ü', 'ue')
    )
    for a, b in trans:
        name = name.replace(a, b)
    name = re.sub(r'[^A-Za-z0-9\- ]+', '', name)
    name = name.replace(' ', '-').lower()
    name = re.sub(r'-+', '-', name)
    return name


def enrich_pair(md_path: Path, json_path: Path) -> Tuple[bool, str]:
    # returns (changed, reason)
    src = md_path.read_text(encoding='utf-8', errors='ignore').splitlines()
    fm = parse_front_matter(src[:FRONTMATTER_MAX_LINES])
    h1 = extract_h1(src)

    orig = load_json(json_path)
    data: Dict[str, Any] = {}
    changed = False

    # Migrate legacy fields if present
    legacy_chapter = (orig.get('chapter') or '').strip() if isinstance(orig.get('chapter'), str) else ''
    legacy_location = (orig.get('location') or '').strip() if isinstance(orig.get('location'), str) else ''
    legacy_tags = orig.get('tags') if isinstance(orig.get('tags'), list) else []

    # Title
    title = None
    if isinstance(fm.get('title'), str) and fm.get('title').strip():
        title = fm['title'].strip()
    elif legacy_chapter:
        title = legacy_chapter
    elif h1:
        title = h1
    else:
        title = md_path.stem
    data['title'] = title

    # Category
    cat = None
    if isinstance(fm.get('category'), str) and fm.get('category').strip():
        cat = fm['category'].strip().lower()
    if cat not in ALLOWED_CATEGORIES:
        guess = derive_category_from_path(md_path)
        cat = guess or 'admin'
    data['category'] = cat

    # Slug
    slug = None
    if isinstance(fm.get('slug'), str) and fm.get('slug').strip():
        slug = fm['slug'].strip()
    else:
        slug = make_slug_from_filename(md_path)
    data['slug'] = slug

    # Version
    if isinstance(fm.get('version'), str) and fm.get('version').strip():
        data['version'] = fm['version'].strip()
    else:
        # default staging version
        data['version'] = orig.get('version') or "0.9"

    # last_updated
    if isinstance(fm.get('last_updated'), str) and fm.get('last_updated').strip():
        data['last_updated'] = fm['last_updated'].strip()
    else:
        # preserve if already present
        if isinstance(orig.get('last_updated'), str) and orig['last_updated'].strip():
            data['last_updated'] = orig['last_updated'].strip()

    # last_change
    if isinstance(fm.get('last_change'), str) and fm.get('last_change').strip():
        data['last_change'] = fm['last_change'].strip()
    elif isinstance(orig.get('last_change'), str) and orig['last_change'].strip():
        data['last_change'] = orig['last_change'].strip()

    # tags
    fm_tags = fm.get('tags') if isinstance(fm.get('tags'), list) else []
    new_tags = sorted({str(x).strip() for x in (legacy_tags + fm_tags) if str(x).strip()})
    data['tags'] = new_tags

    # affiliations
    aff = fm.get('affiliations') if isinstance(fm.get('affiliations'), list) else []
    data['affiliations'] = [str(x).strip() for x in aff if str(x).strip()]

    # locations / primary_location / last_seen
    # Scenes keep 'locations' (array). Characters use singular fields and drop 'locations'.
    if data['category'] == 'scene':
        locs = fm.get('locations') if isinstance(fm.get('locations'), list) else []
        locs_list = [str(x).strip() for x in locs if str(x).strip()]
        if legacy_location and legacy_location not in locs_list:
            locs_list = [legacy_location] + locs_list
        data['locations'] = locs_list
    else:
        # Non-scenes: prefer singular markers if present
        pl = fm.get('primary_location') if isinstance(fm.get('primary_location'), str) else None
        ls = fm.get('last_seen') if isinstance(fm.get('last_seen'), str) else None
        if pl and pl.strip():
            data['primary_location'] = pl.strip()
        if ls and ls.strip():
            data['last_seen'] = ls.strip()
        # Remove any legacy 'locations' for non-scene docs to avoid ambiguity
        if 'locations' in data:
            data.pop('locations', None)

    # characters (only for scenes)
    if data['category'] == 'scene':
        chars = fm.get('characters') if isinstance(fm.get('characters'), list) else []
        data['characters'] = [str(x).strip() for x in chars if str(x).strip()]

    # dependencies
    deps = fm.get('dependencies') if isinstance(fm.get('dependencies'), list) else []
    data['dependencies'] = [str(x).strip() for x in deps if str(x).strip()]

    # source
    data['source'] = relp(md_path)

    # Determine if changed compared to current JSON (ignoring legacy-only keys)
    # Build a normalized view of orig without legacy fields
    orig_norm = {k: v for k, v in orig.items() if k not in {'chapter', 'location', 'characters'} or data.get('category') == 'scene' and k == 'characters'}
    if data != orig_norm:
        save_json(json_path, data)
        changed = True
    return changed, relp(json_path)


def main() -> int:
    touched = 0
    for dirpath, dirnames, filenames in os.walk(ROOT):
        d = Path(dirpath)
        if should_skip_dir(d):
            dirnames[:] = []
            continue
        dirnames[:] = [nm for nm in dirnames if not should_skip_dir(d / nm)]
        for fname in filenames:
            if not fname.lower().endswith('.md'):
                continue
            md_path = d / fname
            json_path = md_path.with_suffix('.json')
            if not json_path.exists():
                continue
            changed, jp = enrich_pair(md_path, json_path)
            if changed:
                touched += 1
    print(f"Enriched JSON files: {touched}")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
