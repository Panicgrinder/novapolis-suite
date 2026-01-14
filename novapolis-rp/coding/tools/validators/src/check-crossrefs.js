import fs from 'node:fs';
import path from 'node:path';
import process from 'node:process';
import { fileURLToPath } from 'node:url';
import fg from 'fast-glob';
import matter from 'gray-matter';
import chalk from 'chalk';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const repoRoot = path.resolve(__dirname, '..', '..', '..', '..');
const rpRoot = path.join(repoRoot, 'database-rp');
const scenesDir = path.join(rpRoot, '06-scenes');

function isSlug(value) {
  return typeof value === 'string' && /^[a-z0-9]+(?:-[a-z0-9]+)*$/.test(value);
}

function isSlugLike(value) {
  return typeof value === 'string' && /^[a-z0-9]+(?:[-_][a-z0-9]+)*$/.test(value);
}

function indexBySlugOnly(files, label, errors) {
  const idx = new Set();
  for (const file of files) {
    const rel = path.relative(repoRoot, file);
    const content = fs.readFileSync(file, 'utf8');
    const { data } = matter(content);
    const slug = data?.slug;
    if (typeof slug === 'string' && slug.trim()) {
      idx.add(slug.trim());
    } else {
      errors.push(`${rel}: missing frontmatter.slug (required for ${label} crossref indexing)`);
    }
  }
  return idx;
}

function indexAnySlugs(files) {
  const idx = new Set();
  for (const file of files) {
    const content = fs.readFileSync(file, 'utf8');
    const { data } = matter(content);
    const slug = data?.slug;
    if (typeof slug === 'string' && slug.trim()) {
      idx.add(slug.trim());
    }
  }
  return idx;
}

async function main() {
  try {
    const [allMdFiles, characterFiles, locationFiles, inventoryFiles, projectFiles, sceneFiles] = await Promise.all([
      fg(['**/*.md'], { cwd: rpRoot, absolute: true }),
      fg(['02-characters/*.md', '01-factions/*/02-characters/*.md'], { cwd: rpRoot, absolute: true }),
      fg(['03-locations/*.md', '01-factions/*/03-locations/*.md'], { cwd: rpRoot, absolute: true }),
      fg(['04-inventory/*.md', '01-factions/*/04-inventory/*.md'], { cwd: rpRoot, absolute: true }),
      fg(['05-projects/*.md', '01-factions/*/05-projects/*.md'], { cwd: rpRoot, absolute: true }),
      fg(['06-scenes/*.md'], { cwd: rpRoot, absolute: true })
    ]);

    let errors = [];
    const idxAny = indexAnySlugs(allMdFiles);
    const idxChars = indexBySlugOnly(characterFiles, 'character', errors);
    const idxLocs = indexBySlugOnly(locationFiles, 'location', errors);
    const idxInv = indexBySlugOnly(inventoryFiles, 'inventory', errors);
    const idxProj = indexBySlugOnly(projectFiles, 'project', errors);

    for (const file of sceneFiles) {
      const rel = path.relative(repoRoot, file);
      const { data } = matter(fs.readFileSync(file, 'utf8'));
      const chars = Array.isArray(data?.characters) ? data.characters : [];
      const locs = Array.isArray(data?.locations) ? data.locations : [];
      const invs = Array.isArray(data?.inventoryRefs) ? data.inventoryRefs : [];

      for (const c of chars) {
        if (!isSlug(c)) errors.push(`${rel}: character ref must be slug (lowercase-hyphen): ${c}`);
        else if (!idxChars.has(c)) errors.push(`${rel}: character ref not found: ${c}`);
      }
      for (const l of locs) {
        if (!isSlug(l)) errors.push(`${rel}: location ref must be slug (lowercase-hyphen): ${l}`);
        else if (!idxLocs.has(l)) errors.push(`${rel}: location ref not found: ${l}`);
      }
      for (const i of invs) {
        if (!isSlug(i)) errors.push(`${rel}: inventory ref must be slug (lowercase-hyphen): ${i}`);
        else if (!idxInv.has(i)) errors.push(`${rel}: inventory ref not found: ${i}`);
      }

      // Co-occurrence rules (Bezugspaare):
      // - Ronja-Kerschner -> Reflex
      // - Jonas-Merek     -> Lumen
      // - Kora-Malenkov   -> Echo
      const requires = [
        { a: 'ronja-kerschner', b: 'reflex', msg: 'Wenn ronja-kerschner vorkommt, muss auch reflex erwähnt werden.' },
        { a: 'jonas-merek', b: 'lumen', msg: 'Wenn jonas-merek vorkommt, muss auch lumen erwähnt werden.' },
        { a: 'kora-malenkov', b: 'echo', msg: 'Wenn kora-malenkov vorkommt, muss auch echo erwähnt werden.' },
      ];
      for (const rule of requires) {
        if (chars.includes(rule.a) && !chars.includes(rule.b)) {
          errors.push(`${rel}: Co-Occurrence verletzt: ${rule.msg}`);
        }
      }
    }

    // Character dependencies
    for (const file of characterFiles) {
      const rel = path.relative(repoRoot, file);
      const { data } = matter(fs.readFileSync(file, 'utf8'));
      const deps = Array.isArray(data?.dependencies) ? data.dependencies : [];
      for (const d of deps) {
        if (!isSlugLike(d)) errors.push(`${rel}: dependency must be slug-like (lowercase, digits, '-' or '_'): ${d}`);
        else if (!idxAny.has(d)) errors.push(`${rel}: dependency not found (slug-only): ${d}`);
      }
    }

    // Location connections
    for (const file of locationFiles) {
      const rel = path.relative(repoRoot, file);
      const { data } = matter(fs.readFileSync(file, 'utf8'));
      const conns = Array.isArray(data?.connections) ? data.connections : [];
      for (const c of conns) {
        if (!isSlugLike(c)) errors.push(`${rel}: connection must be slug-like (lowercase, digits, '-' or '_'): ${c}`);
        else if (!idxLocs.has(c)) errors.push(`${rel}: connection not found (location slug expected, slug-only): ${c}`);
      }
    }

    // Project refs
    for (const file of projectFiles) {
      const rel = path.relative(repoRoot, file);
      const { data } = matter(fs.readFileSync(file, 'utf8'));
      const owners = Array.isArray(data?.owners) ? data.owners : [];
      const locs = Array.isArray(data?.locations) ? data.locations : [];
      const deps = Array.isArray(data?.dependencies) ? data.dependencies : [];

      for (const o of owners) {
        if (!isSlugLike(o)) errors.push(`${rel}: owner must be slug-like (lowercase, digits, '-' or '_'): ${o}`);
        else if (!idxChars.has(o)) errors.push(`${rel}: owner not found (character slug expected): ${o}`);
      }
      for (const l of locs) {
        if (!isSlug(l)) errors.push(`${rel}: project location must be slug (lowercase-hyphen): ${l}`);
        else if (!idxLocs.has(l)) errors.push(`${rel}: project location not found: ${l}`);
      }
      for (const d of deps) {
        if (!isSlugLike(d)) errors.push(`${rel}: dependency must be slug-like (lowercase, digits, '-' or '_'): ${d}`);
        else if (!idxAny.has(d)) errors.push(`${rel}: dependency not found (slug-only): ${d}`);
      }
    }

    if (errors.length) {
      console.error(chalk.red('Cross-reference check FAILED:'));
      for (const msg of errors) console.error(' - ' + msg);
      process.exit(1);
    }
    console.log(chalk.green('Cross-reference check OK'));
  } catch (e) {
    console.error(chalk.red('Error during cross-reference check:'), e.message);
    process.exit(1);
  }
}

main();
