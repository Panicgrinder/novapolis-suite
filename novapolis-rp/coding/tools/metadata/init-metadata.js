#!/usr/bin/env node
/*
  GPT Hybrid Metadata Generator
  - Scans the workspace for all .md files
  - For each .md, creates a sibling .json with the same base name if missing
  - Preserves folder hierarchy, does not touch Markdown content
  - JSON scaffold shape:
    {
      "chapter": "",
      "characters": [],
      "location": "",
      "tags": [],
      "source": "relative/path/to/file.md"
    }
  - Options:
    --dry-run   Only print actions, do not write files
    --overwrite Overwrite existing .json files (default: false)
    --root <path> Root directory to scan (default: cwd)
*/

const fs = require('fs');
const fsp = fs.promises;
const path = require('path');

const args = process.argv.slice(2);
const isDryRun = args.includes('--dry-run');
const shouldOverwrite = args.includes('--overwrite');
const rootArgIndex = args.indexOf('--root');
const rootDir = rootArgIndex !== -1 ? path.resolve(args[rootArgIndex + 1]) : process.cwd();

const SKIP_DIRS = new Set([
  'node_modules', '.git', '.venv', '.vscode', '.idea', '.DS_Store',
  'database-raw/99-exports' // do not process raw exports
]);

function shouldSkipDir(fullPath) {
  const rel = path.relative(rootDir, fullPath).replace(/\\/g, '/');
  if (!rel || rel === '') return false;
  for (const skip of SKIP_DIRS) {
    if (rel === skip || rel.startsWith(skip + '/')) return true;
  }
  return false;
}

async function* walk(dir) {
  const entries = await fsp.readdir(dir, { withFileTypes: true });
  for (const entry of entries) {
    const fullPath = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      if (shouldSkipDir(fullPath)) continue;
      yield* walk(fullPath);
    } else if (entry.isFile()) {
      yield fullPath;
    }
  }
}

function mdToJsonPath(mdPath) {
  const dir = path.dirname(mdPath);
  const base = path.basename(mdPath, '.md');
  return path.join(dir, base + '.json');
}

async function ensureJsonForMd(mdPath) {
  if (!mdPath.toLowerCase().endsWith('.md')) return { skipped: true };
  const jsonPath = mdToJsonPath(mdPath);

  try {
    const exists = fs.existsSync(jsonPath);
    if (exists && !shouldOverwrite) {
      return { exists: true, jsonPath };
    }

    const relMd = path.relative(rootDir, mdPath).replace(/\\/g, '/');
    const scaffold = {
      chapter: "",
      characters: [],
      location: "",
      tags: [],
      source: relMd
    };

    if (isDryRun) {
      return { wouldWrite: true, jsonPath };
    }

    await fsp.writeFile(jsonPath, JSON.stringify(scaffold, null, 2) + '\n', 'utf8');
    return { written: true, jsonPath };
  } catch (err) {
    return { error: err, mdPath };
  }
}

(async () => {
  const results = { written: 0, exists: 0, skipped: 0, errors: 0, files: [] };
  for await (const file of walk(rootDir)) {
    if (!file.toLowerCase().endsWith('.md')) continue;
    const res = await ensureJsonForMd(file);
    results.files.push({ file, ...res });
    if (res.written) results.written++;
    else if (res.exists) results.exists++;
    else if (res.skipped) results.skipped++;
    else if (res.error) results.errors++;
  }

  const summary = `Hybrid metadata: written=${results.written}, exists=${results.exists}, errors=${results.errors}`;
  console.log(summary);
  if (results.errors > 0) {
    for (const r of results.files.filter(f => f.error)) {
      console.error('Error for', r.mdPath || r.file, '-', r.error.message);
    }
    process.exitCode = 1;
  }
})();
