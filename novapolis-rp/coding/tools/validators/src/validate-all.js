import { spawnSync } from 'node:child_process';
import fs from 'fs';
import path from 'path';

function run(cmd, args, name) {
  const res = spawnSync(cmd, args, { stdio: 'inherit', shell: false });
  if (res.status !== 0) {
    throw new Error(`${name} failed with exit code ${res.status}`);
  }
}

function writeStatus(ok, extra = {}) {
  try {
    const baseDirEnv = process.env.VALIDATOR_STATUS_DIR || ''; // optional override
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
    // Status-Datei ist „nice to have“ – nie den Exit-Status verhindern
    console.error('[validate-all] WARN: Konnte Status-Datei nicht schreiben:', e?.message || e);
  }
}

try {
  run('node', ['src/validate-curated.js'], 'validate-curated');
  run('node', ['src/validate-rp.js'], 'validate-rp');
  run('node', ['src/check-crossrefs.js'], 'crossrefs');
  console.log('All validations passed');
} catch (e) {
  console.error(e.message);
  process.exit(1);
}

// Hauptlauf einfangen und Status protokollieren
(async () => {
  try {
    // ...existing code...
    // Angenommen: resultOk gibt es (boolean), sonst auf Exitcode zurückfallen
    const resultOk = typeof overallOk !== 'undefined' ? overallOk : (process.exitCode === 0);
    writeStatus(resultOk, { exitCode: process.exitCode ?? 0 });
    if (!resultOk) process.exitCode = process.exitCode || 1;
  } catch (err) {
    writeStatus(false, { error: String(err && err.message || err) });
    process.exitCode = 1;
  }
})();
