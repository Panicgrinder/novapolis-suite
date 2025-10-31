#!/usr/bin/env node
/**
 * Repository RP validator.
 * - Validates Markdown basics (H1 present) and link targets exist
 * - Scans 06-scenes JSONL for optional refs and cross-checks against rp slugs
 * No external deps.
 */
const fs = require('fs');
const path = require('path');

const REPO_ROOT = process.cwd();
const RP_DIR = path.join(REPO_ROOT, 'database-rp');

function walk(dir, filterFn) {
  const out = [];
  if (!fs.existsSync(dir)) return out;
  for (const name of fs.readdirSync(dir)) {
    const p = path.join(dir, name);
    const stat = fs.statSync(p);
    if (stat.isDirectory()) out.push(...walk(p, filterFn));
    else if (!filterFn || filterFn(p)) out.push(p);
  }
  return out;
}

function readText(p) {
  try { return fs.readFileSync(p, 'utf8'); } catch { return ''; }
}

function rel(p) { return path.relative(REPO_ROOT, p).replace(/\\/g, '/'); }

function collectSlugs(dir) {
  const mds = walk(dir, p => p.endsWith('.md'));
  const slugs = new Set();
  for (const p of mds) {
    const base = path.basename(p, '.md');
    slugs.add(base);
  }
  return slugs;
}

function validateMarkdownFiles() {
  const mdFiles = walk(RP_DIR, p => p.endsWith('.md'));
  const errors = [];
  const linkRe = /\[[^\]]+\]\(([^)]+)\)/g;

  for (const p of mdFiles) {
    const txt = readText(p);
    // H1 check within first 5 lines
    const firstLines = txt.split(/\r?\n/).slice(0, 5).join('\n');
    if (!/^#\s+/.test(firstLines)) {
      errors.push(`${rel(p)}: H1 ("# ") in den ersten Zeilen fehlt`);
    }

    // Link target existence check for relative links
    let m;
    while ((m = linkRe.exec(txt)) !== null) {
      const target = m[1];
      if (/^(https?:)?\/\//i.test(target)) continue; // skip URLs
      if (target.startsWith('#')) continue; // skip intra-doc anchors
      const abs = path.resolve(path.dirname(p), target);
      if (!fs.existsSync(abs)) {
        errors.push(`${rel(p)}: Link-Ziel fehlt → ${rel(abs)}`);
      }
    }
  }
  return errors;
}

function validateSceneRefs() {
  const scenesDir = path.join(RP_DIR, '06-scenes');
  const jsonlFiles = walk(scenesDir, p => p.endsWith('.jsonl'));
  const errors = [];
  const warnings = [];

  const charSlugs = collectSlugs(path.join(RP_DIR, '02-characters'));
  const locSlugs = collectSlugs(path.join(RP_DIR, '03-locations'));
  const invSlugs = collectSlugs(path.join(RP_DIR, '04-inventory'));

  for (const jf of jsonlFiles) {
    const lines = readText(jf).split(/\r?\n/).filter(Boolean);
    for (const line of lines) {
      let obj;
      try { obj = JSON.parse(line); } catch { continue; }
      if (!obj || typeof obj !== 'object' || obj._meta) continue;
      const refs = obj.refs;
      if (!refs) {
        warnings.push(`${rel(jf)}: Szene ${obj.id || '(ohne id)'} ohne refs – (nur Hinweis, kein Fehler)`);
        continue;
      }
      if (refs.characters) {
        for (const s of refs.characters) {
          if (!charSlugs.has(String(s))) {
            errors.push(`${rel(jf)}: refs.characters → unbekannt: ${s}`);
          }
        }
      }
      if (refs.locations) {
        for (const s of refs.locations) {
          if (!locSlugs.has(String(s))) {
            errors.push(`${rel(jf)}: refs.locations → unbekannt: ${s}`);
          }
        }
      }
      if (refs.inventory) {
        for (const s of refs.inventory) {
          if (!invSlugs.has(String(s))) {
            errors.push(`${rel(jf)}: refs.inventory → unbekannt: ${s}`);
          }
        }
      }
    }
  }
  return { errors, warnings };
}

function main() {
  let exitCode = 0;
  if (!fs.existsSync(RP_DIR)) {
    console.warn('WARN: database-rp nicht gefunden – überspringe');
    return exitCode;
  }

  const mdErrors = validateMarkdownFiles();
  mdErrors.forEach(e => console.error('FAIL:', e));
  if (mdErrors.length) exitCode = 1;
  else console.log('OK: Markdown-Basis + Links geprüft');

  const { errors: sceneErrs, warnings: sceneWarns } = validateSceneRefs();
  sceneWarns.forEach(w => console.warn('WARN:', w));
  sceneErrs.forEach(e => console.error('FAIL:', e));
  if (sceneErrs.length) exitCode = 1;
  else console.log('OK: Szenen-Refs (falls vorhanden) geprüft');

  return exitCode;
}

process.exit(main());
