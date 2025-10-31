#!/usr/bin/env node
/**
 * Lightweight curated-data validator.
 * Validates database-curated/staging/manifest.json shape and required fields.
 * No external deps; intentionally strict on structure, lenient on file existence.
 */
const fs = require('fs');
const path = require('path');

const REPO_ROOT = process.cwd();
const MANIFEST_PATH = path.join(REPO_ROOT, 'database-curated', 'staging', 'manifest.json');

function fail(msg) {
  console.error(`FAIL: ${msg}`);
}

function warn(msg) {
  console.warn(`WARN: ${msg}`);
}

function ok(msg) {
  console.log(`OK: ${msg}`);
}

function isIsoDate(s) {
  // Accept YYYY-MM-DD or full ISO timestamp
  return /^(\d{4}-\d{2}-\d{2})([Tt].+)?$/.test(String(s || ''));
}

function validateManifestShape(obj, idx) {
  const errors = [];
  function reqStr(key) {
    if (typeof obj[key] !== 'string' || obj[key].trim() === '') {
      errors.push(`item[${idx}].${key} muss String sein`);
    }
  }

  reqStr('id');
  reqStr('source');
  reqStr('type');
  reqStr('status');
  reqStr('createdAt');
  if (!isIsoDate(obj.createdAt)) {
    errors.push(`item[${idx}].createdAt kein ISO-Datum`);
  }

  const allowedTypes = new Set(['raw-txt', 'raw-jsonl']);
  if (!allowedTypes.has(obj.type)) {
    errors.push(`item[${idx}].type unerwartet: ${obj.type}`);
  }
  const allowedStatus = new Set(['pending', 'in-progress', 'reviewed', 'approved']);
  if (!allowedStatus.has(obj.status)) {
    errors.push(`item[${idx}].status unerwartet: ${obj.status}`);
  }

  if (obj.artifacts && typeof obj.artifacts === 'object') {
    const a = obj.artifacts;
    // Strings if present
    for (const k of ['normalized', 'chunksDir', 'index', 'review']) {
      if (k in a && typeof a[k] !== 'string') {
        errors.push(`item[${idx}].artifacts.${k} muss String sein`);
      }
    }
    if (a.reports && typeof a.reports === 'object') {
      for (const k of Object.keys(a.reports)) {
        if (typeof a.reports[k] !== 'string') {
          errors.push(`item[${idx}].artifacts.reports.${k} muss String sein`);
        }
      }
    }
    if (a.views && typeof a.views === 'object') {
      for (const k of Object.keys(a.views)) {
        if (typeof a.views[k] !== 'string') {
          errors.push(`item[${idx}].artifacts.views.${k} muss String sein`);
        }
      }
    }
  } else if (obj.artifacts !== undefined) {
    errors.push(`item[${idx}].artifacts muss Objekt sein`);
  }

  if (obj.notes !== undefined && typeof obj.notes !== 'string') {
    errors.push(`item[${idx}].notes muss String sein, falls vorhanden`);
  }

  return errors;
}

function main() {
  let exitCode = 0;

  if (!fs.existsSync(MANIFEST_PATH)) {
    warn('manifest.json nicht gefunden – überspringe curated-Validierung');
    console.log('HINWEIS: Erwarteter Pfad:', path.relative(REPO_ROOT, MANIFEST_PATH));
    return exitCode;
  }

  let raw;
  try {
    raw = fs.readFileSync(MANIFEST_PATH, 'utf8');
  } catch (e) {
    fail(`manifest.json konnte nicht gelesen werden: ${e.message}`);
    return 2;
  }

  let data;
  try {
    data = JSON.parse(raw);
  } catch (e) {
    fail(`manifest.json ist kein gültiges JSON: ${e.message}`);
    return 2;
  }

  if (!Array.isArray(data)) {
    fail('manifest.json: Top-Level muss ein Array sein');
    return 2;
  }

  const allErrors = [];
  data.forEach((item, i) => {
    if (typeof item !== 'object' || item === null || Array.isArray(item)) {
      allErrors.push(`item[${i}] muss Objekt sein`);
      return;
    }
    const errs = validateManifestShape(item, i);
    allErrors.push(...errs);
  });

  if (allErrors.length) {
    for (const e of allErrors) fail(e);
    exitCode = 1;
  } else {
    ok(`manifest.json: ${data.length} Eintrag(e) – Struktur ok`);
  }

  return exitCode;
}

process.exit(main());
