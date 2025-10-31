import fs from 'node:fs';
import path from 'node:path';
import process from 'node:process';
import Ajv2020 from 'ajv/dist/2020.js';
import addFormats from 'ajv-formats';
import chalk from 'chalk';

const repoRoot = path.resolve(process.cwd());
const manifestPath = path.join(repoRoot, 'database-curated', 'staging', 'manifest.json');
const schemaPath = path.join(repoRoot, 'coding', 'tools', 'validators', 'schemas', 'curated-manifest.schema.json');

function readJson(file) {
  const data = fs.readFileSync(file, 'utf8');
  return JSON.parse(data);
}

function main() {
  try {
    const manifest = readJson(manifestPath);
    const schema = readJson(schemaPath);

  const ajv = new Ajv2020({ allErrors: true, strict: false });
    addFormats(ajv);
    const validate = ajv.compile(schema);
    const valid = validate(manifest);
    if (!valid) {
      console.error(chalk.red('Curated manifest validation FAILED:'));
      for (const err of validate.errors ?? []) {
        console.error(` - ${err.instancePath || '/'} ${err.message}`);
      }
      process.exit(1);
    }
    console.log(chalk.green('Curated manifest validation OK'));
  } catch (e) {
    console.error(chalk.red('Error while validating curated manifest:'), e.message);
    process.exit(1);
  }
}

main();
