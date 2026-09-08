// Validates the content packs in public/content so a typo never breaks the game silently.
import { readFileSync } from 'node:fs';
import { resolve, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const root = resolve(dirname(fileURLToPath(import.meta.url)), '..', 'public', 'content');
const errors = [];
const warn = [];

function load(name) {
  try {
    return JSON.parse(readFileSync(resolve(root, name), 'utf8'));
  } catch (e) {
    errors.push(`${name}: JSON inválido (${e.message})`);
    return null;
  }
}

function checkQuestion(q, where, featureIds) {
  if (!q.id) errors.push(`${where}: pergunta sem id`);
  if (!q.prompt) errors.push(`${where}/${q.id}: sem prompt`);
  if (!Array.isArray(q.options) || q.options.length !== 4) errors.push(`${where}/${q.id}: precisa de exatamente 4 opções`);
  if (!Number.isInteger(q.answer) || q.answer < 0 || q.answer > 3) errors.push(`${where}/${q.id}: answer deve ser 0..3`);
  if (![1, 2, 3].includes(q.difficulty)) errors.push(`${where}/${q.id}: difficulty deve ser 1, 2 ou 3`);
  if (!q.explanation) warn.push(`${where}/${q.id}: sem explanation`);
  if (featureIds && q.featureId && !featureIds.has(q.featureId)) errors.push(`${where}/${q.id}: featureId "${q.featureId}" não existe`);
}

for (const platform of ['openai', 'claude', 'manus']) {
  const pack = load(`${platform}.json`);
  if (!pack) continue;
  const where = `${platform}.json`;
  if (pack.platform !== platform) errors.push(`${where}: platform deve ser "${platform}"`);
  if (!pack.updatedAt) errors.push(`${where}: sem updatedAt`);
  const sourceIds = new Set((pack.sources ?? []).map((s) => s.id));
  const featureIds = new Set();
  for (const f of pack.features ?? []) {
    if (!f.id) errors.push(`${where}: feature sem id`);
    if (featureIds.has(f.id)) errors.push(`${where}: feature id duplicado "${f.id}"`);
    featureIds.add(f.id);
    if (!f.name || !f.summary) errors.push(`${where}/${f.id}: precisa de name e summary`);
    if (!Array.isArray(f.tips) || f.tips.length === 0) warn.push(`${where}/${f.id}: sem tips`);
    for (const sid of f.sourceIds ?? []) if (!sourceIds.has(sid)) errors.push(`${where}/${f.id}: sourceId "${sid}" não existe`);
    const qs = (pack.questions ?? []).filter((q) => q.featureId === f.id);
    if (qs.length < 2) warn.push(`${where}/${f.id}: só ${qs.length} pergunta(s); o ideal são 2+`);
  }
  const qids = new Set();
  for (const q of pack.questions ?? []) {
    if (qids.has(q.id)) errors.push(`${where}: pergunta id duplicado "${q.id}"`);
    qids.add(q.id);
    checkQuestion(q, where, featureIds);
  }
  console.log(`${where}: ${pack.features?.length ?? 0} funcionalidades, ${pack.questions?.length ?? 0} perguntas, ${pack.sources?.length ?? 0} fontes`);
}

const yt = load('youtube.json');
if (yt) {
  const videoIds = new Set((yt.videos ?? []).map((v) => v.id));
  for (const v of yt.videos ?? []) if (!/^https:\/\/(www\.)?youtube\.com\/watch\?v=/.test(v.url)) warn.push(`youtube.json/${v.id}: url fora do padrão`);
  for (const q of yt.questions ?? []) {
    checkQuestion(q, 'youtube.json', null);
    if (!['openai', 'claude', 'manus', 'general'].includes(q.platform)) errors.push(`youtube.json/${q.id}: platform inválida`);
    if (q.videoId && !videoIds.has(q.videoId)) errors.push(`youtube.json/${q.id}: videoId "${q.videoId}" não existe`);
  }
  console.log(`youtube.json: ${yt.videos?.length ?? 0} vídeos, ${yt.questions?.length ?? 0} perguntas`);
}

for (const w of warn) console.log(`AVISO  ${w}`);
for (const e of errors) console.log(`ERRO   ${e}`);
if (errors.length) {
  console.log(`\n${errors.length} erro(s).`);
  process.exit(1);
}
console.log(`\nOK (${warn.length} aviso(s)).`);
