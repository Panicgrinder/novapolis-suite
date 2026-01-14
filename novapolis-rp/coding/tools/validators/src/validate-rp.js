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

function isSlugLike(value) {
  // Allow both '-' and '_' for backwards compatibility.
  // Long-term target is kebab-case (lowercase-hyphen) everywhere.
  return typeof value === 'string' && /^[a-z0-9]+(?:[-_][a-z0-9]+)*$/.test(value);
}

function ensureFileHasHeading(mdContent, file, meta) {
  const fmTitle = meta && typeof meta.title === 'string' ? meta.title.trim() : '';
  // markdownlint MD025 can treat frontmatter `title` as the top-level heading.
  // If we have a frontmatter title, do not additionally require a body H1.
  if (fmTitle) return;

  const lines = mdContent.split(/\r?\n/);
  const hasAtxH1 = lines.some(l => l.trim().startsWith('# '));
  const hasSetextH1 = lines.some((l, i) => {
    if (i + 1 >= lines.length) return false;
    const titleLine = l.trim();
    if (!titleLine) return false;
    // Setext H1: a non-empty line followed by === underline.
    const underline = (lines[i + 1] ?? '').trim();
    return /^=+$/.test(underline);
  });
  const hasH1 = hasAtxH1 || hasSetextH1;
  if (!hasH1) {
    throw new Error(`Missing H1 heading in ${file}`);
  }
}

function validateFrontmatter(meta, file) {
  // Soft validation: if frontmatter exists, check basic types
  if (!meta || Object.keys(meta).length === 0) return; // allowed
  for (const k of ['last-updated', 'last_updated', 'lastUpdated']) {
    if (Object.prototype.hasOwnProperty.call(meta, k)) {
      const v = meta[k];
      const isString = typeof v === 'string';
      const isDate = Object.prototype.toString.call(v) === '[object Date]';
      if (!isString && !isDate) {
        throw new Error(`frontmatter.${k} must be string in ${file}`);
      }
    }
  }
  if (meta.version && typeof meta.version !== 'string' && typeof meta.version !== 'number') {
    throw new Error(`frontmatter.version must be string/number in ${file}`);
  }

  if (Object.prototype.hasOwnProperty.call(meta, 'category') && typeof meta.category !== 'string') {
    throw new Error(`frontmatter.category must be string in ${file}`);
  }
}

function getLastUpdated(meta) {
  if (!meta) return undefined;
  for (const k of ['last_updated', 'last-updated', 'lastUpdated']) {
    if (Object.prototype.hasOwnProperty.call(meta, k)) return meta[k];
  }
  return undefined;
}

function requireNonEmptyString(meta, key, file) {
  const v = meta?.[key];
  if (typeof v !== 'string' || !v.trim()) {
    throw new Error(`frontmatter.${key} is required and must be non-empty string in ${file}`);
  }
}

function requireStringOrDate(meta, key, file) {
  const v = meta?.[key];
  const isString = typeof v === 'string' && v.trim();
  const isDate = Object.prototype.toString.call(v) === '[object Date]';
  if (!isString && !isDate) {
    throw new Error(`frontmatter.${key} is required and must be string or date in ${file}`);
  }
}

function assertStringArray(meta, key, file) {
  if (!Object.prototype.hasOwnProperty.call(meta, key)) return;
  const v = meta?.[key];
  if (!Array.isArray(v)) {
    throw new Error(`frontmatter.${key} must be an array in ${file}`);
  }
  for (const item of v) {
    if (typeof item !== 'string' || !item.trim()) {
      throw new Error(`frontmatter.${key} must contain non-empty strings in ${file}`);
    }
  }
}

function assertOptionalString(meta, key, file) {
  if (!Object.prototype.hasOwnProperty.call(meta, key)) return;
  const v = meta?.[key];
  if (typeof v !== 'string' || !v.trim()) {
    throw new Error(`frontmatter.${key} must be non-empty string in ${file}`);
  }
}

function assertOptionalEnum(meta, key, allowed, file) {
  if (!Object.prototype.hasOwnProperty.call(meta, key)) return;
  const v = meta?.[key];
  if (typeof v !== 'string' || !allowed.includes(v)) {
    throw new Error(`frontmatter.${key} must be one of [${allowed.join(', ')}] in ${file}`);
  }
}

function validateByCategory(meta, file) {
  const category = meta?.category;
  if (!category) return;

  const requireVersionCategories = new Set(['character', 'location', 'inventory', 'project']);
  if (requireVersionCategories.has(category) && !Object.prototype.hasOwnProperty.call(meta, 'version')) {
    throw new Error(`frontmatter.version is required for category '${category}' in ${file}`);
  }

  const requireLastUpdatedCategories = new Set(['character', 'location', 'inventory', 'project']);
  if (requireLastUpdatedCategories.has(category)) {
    const lu = getLastUpdated(meta);
    const isString = typeof lu === 'string' && lu.trim();
    const isDate = Object.prototype.toString.call(lu) === '[object Date]';
    if (!isString && !isDate) {
      throw new Error(`frontmatter.last_updated (or last-updated) is required for category '${category}' in ${file}`);
    }
  }

  // If an explicit id is provided, keep it consistent with slug.
  if (Object.prototype.hasOwnProperty.call(meta, 'id')) {
    const id = meta?.id;
    if (typeof id !== 'string' || !id.trim()) {
      throw new Error(`frontmatter.id must be non-empty string in ${file}`);
    }
    if (typeof meta?.slug === 'string' && meta.slug.trim() && id.trim() !== meta.slug.trim()) {
      throw new Error(`frontmatter.id must match frontmatter.slug in ${file}`);
    }
  }

  switch (category) {
    case 'character': {
      requireNonEmptyString(meta, 'title', file);
      assertStringArray(meta, 'tags', file);
      assertStringArray(meta, 'affiliations', file);
      assertStringArray(meta, 'dependencies', file);
      assertOptionalString(meta, 'primary_location', file);
      assertOptionalString(meta, 'last_seen', file);
      break;
    }
    case 'location': {
      requireNonEmptyString(meta, 'title', file);
      assertStringArray(meta, 'tags', file);
      assertStringArray(meta, 'affiliations', file);
      assertStringArray(meta, 'connections', file);
      assertOptionalString(meta, 'status', file);
      break;
    }
    case 'inventory': {
      // Inventory historically uses either title (template) or canvas (legacy).
      const hasTitle = typeof meta?.title === 'string' && meta.title.trim();
      const hasCanvas = typeof meta?.canvas === 'string' && meta.canvas.trim();
      if (!hasTitle && !hasCanvas) {
        throw new Error(`frontmatter.title or frontmatter.canvas is required for category 'inventory' in ${file}`);
      }
      requireNonEmptyString(meta, 'owner', file);
      assertOptionalEnum(meta, 'scope', ['faction', 'location', 'global'], file);
      assertStringArray(meta, 'tags', file);
      break;
    }
    case 'project': {
      requireNonEmptyString(meta, 'title', file);
      assertOptionalEnum(meta, 'status', ['planned', 'active', 'paused', 'done', 'prototyping'], file);
      assertStringArray(meta, 'owners', file);
      assertStringArray(meta, 'locations', file);
      assertStringArray(meta, 'dependencies', file);
      assertStringArray(meta, 'tags', file);
      break;
    }
    case 'scene': {
      requireStringOrDate(meta, 'date', file);
      // NOTE: scenes are special; keep last_updated optional.
      assertStringArray(meta, 'characters', file);
      assertStringArray(meta, 'locations', file);
      assertStringArray(meta, 'inventoryRefs', file);
      assertStringArray(meta, 'tags', file);
      break;
    }
    default:
      break;
  }
}

async function main() {
  try {
    const files = await fg(['**/*.md'], { cwd: rpRoot, dot: false, absolute: true });
    let errors = [];
    const slugToFiles = new Map();
    const requireSlugCategories = new Set(['character', 'location', 'inventory', 'project', 'scene']);
    const allowNoH1 = new Set([
      path.join('database-rp', '00-admin', 'system-prompt.md')
    ]);

    for (const file of files) {
      const content = fs.readFileSync(file, 'utf8');
      try {
        const rel = path.relative(repoRoot, file);
        const parsed = matter(content);
        validateFrontmatter(parsed.data, rel);
        validateByCategory(parsed.data, rel);

        const category = parsed?.data?.category;
        if (requireSlugCategories.has(category)) {
          const raw = parsed?.data?.slug;
          if (raw === undefined || raw === null || (typeof raw === 'string' && !raw.trim())) {
            throw new Error(`frontmatter.slug is required for category '${category}'`);
          }
        }

        const slugRaw = parsed?.data?.slug;
        if (typeof slugRaw === 'string') {
          const slug = slugRaw.trim();
          if (!slug) {
            throw new Error('frontmatter.slug must be non-empty if provided');
          }
          if (!isSlugLike(slug)) {
            throw new Error(`frontmatter.slug must be slug-like (lowercase, digits, '-' or '_'): ${slug}`);
          }
          const list = slugToFiles.get(slug) ?? [];
          list.push(rel);
          slugToFiles.set(slug, list);
        } else if (slugRaw !== undefined) {
          throw new Error('frontmatter.slug must be string if provided');
        }

        if (!allowNoH1.has(rel)) {
          ensureFileHasHeading(content, rel, parsed.data);
        }
      } catch (e) {
        const rel = path.relative(repoRoot, file);
        errors.push(`${rel}: ${e.message}`);
      }
    }

    for (const [slug, relFiles] of slugToFiles.entries()) {
      if (relFiles.length > 1) {
        errors.push(`Duplicate slug '${slug}' in: ${relFiles.join(', ')}`);
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
