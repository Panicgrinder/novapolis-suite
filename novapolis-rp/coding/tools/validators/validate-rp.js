#!/usr/bin/env node
/**
 * Legacy entry-point (kept for compatibility).
 *
 * This repo uses ESM (`package.json` has `type: "module"`). The canonical
 * implementation lives in `src/validate-rp.js`.
 */

import path from 'node:path';
import process from 'node:process';
import { fileURLToPath, pathToFileURL } from 'node:url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

console.warn(
  'DEPRECATED: Use `npm --prefix novapolis-rp\\coding\\tools\\validators run validate:rp` instead of running validate-rp.js directly.'
);

try {
  const targetUrl = pathToFileURL(path.join(__dirname, 'src', 'validate-rp.js')).href;
  await import(targetUrl);
} catch (e) {
  const msg = e && typeof e === 'object' && 'stack' in e ? e.stack : String(e);
  console.error('FAIL:', msg);
  process.exitCode = 1;
}
