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

function ensureFileHasHeading(mdContent, file) {
  const lines = mdContent.split(/\r?\n/);
  const hasH1 = lines.some(l => l.trim().startsWith('# '));
  if (!hasH1) {
    throw new Error(`Missing H1 heading in ${file}`);
  }
}

function validateFrontmatter(meta, file) {
  // Soft validation: if frontmatter exists, check basic types
  if (!meta || Object.keys(meta).length === 0) return; // allowed
  if (Object.prototype.hasOwnProperty.call(meta, 'last-updated')) {
    const v = meta['last-updated'];
    const isString = typeof v === 'string';
    const isDate = Object.prototype.toString.call(v) === '[object Date]';
    if (!isString && !isDate) {
      throw new Error(`frontmatter.last-updated must be string in ${file}`);
    }
  }
  if (meta.version && typeof meta.version !== 'string' && typeof meta.version !== 'number') {
    throw new Error(`frontmatter.version must be string/number in ${file}`);
  }
}

async function main() {
  try {
    const files = await fg(['**/*.md'], { cwd: rpRoot, dot: false, absolute: true });
    let errors = [];
    const allowNoH1 = new Set([
      path.join('database-rp', '00-admin', 'system-prompt.md')
    ]);

    for (const file of files) {
      const content = fs.readFileSync(file, 'utf8');
      try {
        const rel = path.relative(repoRoot, file);
        if (!allowNoH1.has(rel)) {
          ensureFileHasHeading(content, rel);
        }
        const parsed = matter(content);
        validateFrontmatter(parsed.data, rel);
      } catch (e) {
        errors.push(e.message);
      }
    }
    if (errors.length) {
      console.error(chalk.red('RP markdown validation FAILED:'));
      for (const msg of errors) console.error(' - ' + msg);
      process.exit(1);
    }
    console.log(chalk.green('RP markdown validation OK'));
  } catch (e) {
    console.error(chalk.red('Error during RP validation:'), e.message);
    process.exit(1);
  }
}

main();
