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

function baseName(file) {
  return path.basename(file).replace(/\.[^.]+$/, '');
}

function indexByBasename(files) {
  const idx = new Set(files.map(f => baseName(f)));
  return idx;
}

async function main() {
  try {
    const [characterFiles, locationFiles, inventoryFiles, sceneFiles] = await Promise.all([
      fg(['02-characters/*.md'], { cwd: rpRoot, absolute: true }),
      fg(['03-locations/*.md'], { cwd: rpRoot, absolute: true }),
      fg(['04-inventory/*.md'], { cwd: rpRoot, absolute: true }),
      fg(['06-scenes/*.md'], { cwd: rpRoot, absolute: true })
    ]);

    const idxChars = indexByBasename(characterFiles);
    const idxLocs = indexByBasename(locationFiles);
    const idxInv  = indexByBasename(inventoryFiles);

    let errors = [];

    for (const file of sceneFiles) {
      const rel = path.relative(repoRoot, file);
      const { data } = matter(fs.readFileSync(file, 'utf8'));
      const chars = Array.isArray(data?.characters) ? data.characters : [];
      const locs = Array.isArray(data?.locations) ? data.locations : [];
      const invs = Array.isArray(data?.inventoryRefs) ? data.inventoryRefs : [];

      for (const c of chars) if (!idxChars.has(c)) errors.push(`${rel}: character ref not found: ${c}`);
      for (const l of locs) if (!idxLocs.has(l)) errors.push(`${rel}: location ref not found: ${l}`);
      for (const i of invs) if (!idxInv.has(i))  errors.push(`${rel}: inventory ref not found: ${i}`);

      // Co-occurrence rules (Bezugspaare):
      // - Ronja-Kerschner -> Reflex
      // - Jonas-Merek     -> Lumen
      // - Kora-Malenkov   -> Echo
      const requires = [
        { a: 'Ronja-Kerschner', b: 'Reflex', msg: 'Wenn Ronja-Kerschner vorkommt, muss auch Reflex erwähnt werden.' },
        { a: 'Jonas-Merek', b: 'Lumen', msg: 'Wenn Jonas-Merek vorkommt, muss auch Lumen erwähnt werden.' },
        { a: 'Kora-Malenkov', b: 'Echo', msg: 'Wenn Kora-Malenkov vorkommt, muss auch Echo erwähnt werden.' },
      ];
      for (const rule of requires) {
        if (chars.includes(rule.a) && !chars.includes(rule.b)) {
          errors.push(`${rel}: Co-Occurrence verletzt: ${rule.msg}`);
        }
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
