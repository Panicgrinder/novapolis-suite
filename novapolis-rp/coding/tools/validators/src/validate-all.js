import { spawnSync } from 'node:child_process';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'node:url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

function run(cmd, args, name) {
  const res = spawnSync(cmd, args, { stdio: 'inherit', shell: false });
  if (res.status !== 0) {
    const error = new Error(`${name} failed with exit code ${res.status}`);
    error.exitCode = res.status;
    throw error;
  }
}

function writeStatus(ok, extra = {}) {
  try {
    const baseDirEnv = process.env.VALIDATOR_STATUS_DIR || '';
    const statusDir = baseDirEnv
      ? path.resolve(baseDirEnv)
      : path.resolve(__dirname, '..', '.last-run');
    fs.mkdirSync(statusDir, { recursive: true });
    const statusFile = path.join(statusDir, 'validate-data.json');
    const payload = {
      tool: 'validate-all',
      ok: Boolean(ok),
      ts: new Date().toISOString(),
      cwd: process.cwd(),
      node: process.version,
      ...extra,
    };
    fs.writeFileSync(statusFile, JSON.stringify(payload, null, 2), 'utf8');
  } catch (e) {
    console.error('[validate-all] WARN: Konnte Status-Datei nicht schreiben:', e?.message || e);
  }
}

let overallOk = true;
let errorExitCode = 0;

try {
  run('node', ['src/validate-curated.js'], 'validate-curated');
  run('node', ['src/validate-rp.js'], 'validate-rp');
  run('node', ['src/check-crossrefs.js'], 'crossrefs');
  console.log('All validations passed');
} catch (e) {
  overallOk = false;
  errorExitCode = typeof e.exitCode === 'number' ? e.exitCode : 1;
  console.error(e.message);
  process.exitCode = errorExitCode;
}

const currentExit = typeof process.exitCode === 'number' ? process.exitCode : (overallOk ? 0 : Math.max(1, errorExitCode));
const ok = overallOk && currentExit === 0;
writeStatus(ok, { exitCode: currentExit });

if (!ok && currentExit === 0) {
  process.exitCode = 1;
}

if (!ok && typeof process.exitCode !== 'number') {
  process.exitCode = Math.max(1, currentExit);
}
