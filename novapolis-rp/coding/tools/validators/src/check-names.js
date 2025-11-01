import fs from 'node:fs';
import path from 'node:path';
import process from 'node:process';
import { fileURLToPath } from 'node:url';
import fg from 'fast-glob';
import chalk from 'chalk';
import { canonicalFilename } from './utils/slugify.js';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const repoRoot = path.resolve(__dirname, '..', '..', '..', '..');
const rpRoot = path.join(repoRoot, 'database-rp');

function findViolations(filePath) {
  const rel = path.relative(repoRoot, filePath);
  const name = path.basename(filePath);
  const canonical = canonicalFilename(name);
  let reasons = [];
  if (/\s/.test(name)) reasons.push('contains whitespace');
  if (/[()\[\]{}'"!?,;:+*\\]/.test(name)) reasons.push('contains punctuation');
  if (/[_]/.test(name)) reasons.push('contains underscore');
  if (/-{2,}/.test(name)) reasons.push('multiple hyphens');
  if (/\.$/.test(name)) reasons.push('trailing dot');
  // ASCII-ish check (allow letters, digits, hyphen, dot)
  if (/[^A-Za-z0-9_.\-]/.test(name)) reasons.push('non-ascii characters');
  const ok = reasons.length === 0 && name === canonical;
  return { rel, name, canonical, ok, reasons };
}

async function main() {
  const apply = process.argv.includes('--apply');
  const patterns = [
    '00-admin/**/*',
    '01-canon/**/*',
    '02-characters/**/*',
    '03-locations/**/*',
    '04-inventory/**/*',
    '05-projects/**/*',
    '06-scenes/**/*'
  ];
  const files = await fg(patterns, { cwd: rpRoot, absolute: true, dot: false, onlyFiles: true });
  let violations = [];

  for (const file of files) {
    const { rel, name, canonical, ok, reasons } = findViolations(file);
    if (!ok) {
      violations.push({ rel, name, canonical, reasons, abs: file });
    }
  }

  if (!violations.length) {
    console.log(chalk.green('Name check OK: no violations in database-rp')); 
    return;
  }

  console.log(chalk.yellow(`Found ${violations.length} naming issues in database-rp:`));
  for (const v of violations) {
    console.log(` - ${v.rel} -> ${v.canonical} [${v.reasons.join(', ')}]`);
  }

  if (!apply) {
    console.error(chalk.red('Name check FAILED (dry-run). Run with --apply to rename locally.'));
    process.exit(1);
    return;
  }

  // Apply renames and update links in RP markdown files.
  // 1) Build rename map
  const renameMap = new Map();
  for (const v of violations) {
    const dir = path.dirname(v.abs);
    const target = path.join(dir, v.canonical);
    if (v.abs !== target) renameMap.set(v.abs, target);
  }

  // 2) Perform renames (sequential)
  for (const [from, to] of renameMap) {
    fs.renameSync(from, to);
  }

  // 3) Update markdown links within database-rp
  const mdFiles = await fg(['**/*.md'], { cwd: rpRoot, absolute: true });
  const replacements = [];
  for (const [from, to] of renameMap) {
    const fromRel = path.relative(rpRoot, from).replace(/\\/g, '/');
    const toRel = path.relative(rpRoot, to).replace(/\\/g, '/');
    replacements.push({ fromRel, toRel, fromName: path.basename(from), toName: path.basename(to) });
  }

  for (const file of mdFiles) {
    let content = fs.readFileSync(file, 'utf8');
    let changed = false;
    for (const r of replacements) {
      // Replace relative links and bare filename mentions inside links
      const patterns = [
        new RegExp(`(\]\()([^)]*?)${r.fromRel.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}(\))`, 'g'),
        new RegExp(`(\]\()([^)]*?)${r.fromName.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}(\))`, 'g')
      ];
      const before = content;
      content = content.replace(patterns[0], (m, a, mid, c) => `${a}${mid}${r.toRel}${c}`);
      content = content.replace(patterns[1], (m, a, mid, c) => `${a}${mid}${r.toName}${c}`);
      if (content !== before) changed = true;
    }
    if (changed) fs.writeFileSync(file, content, 'utf8');
  }

  console.log(chalk.green('Renames applied and markdown links updated.')); 
}

main().catch((e) => {
  console.error(chalk.red('check-names error:'), e);
  process.exit(1);
});
