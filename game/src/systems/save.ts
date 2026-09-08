/** Player progress lives in localStorage so it survives reloads and works offline. */

export interface SaveData {
  version: 1;
  xp: number;
  learned: string[]; // feature ids ("platform:featureId")
  bosses: string[]; // platform ids defeated
  pos: { x: number; y: number } | null;
  stats: { battles: number; wins: number; correct: number; wrong: number; bestStreak: number };
}

const KEY = 'ai-quest-save-v1';

const fresh = (): SaveData => ({
  version: 1,
  xp: 0,
  learned: [],
  bosses: [],
  pos: null,
  stats: { battles: 0, wins: 0, correct: 0, wrong: 0, bestStreak: 0 },
});

let data: SaveData = fresh();

export function loadSave(): SaveData {
  try {
    const raw = localStorage.getItem(KEY);
    if (raw) {
      const parsed = JSON.parse(raw) as SaveData;
      if (parsed && parsed.version === 1) data = { ...fresh(), ...parsed };
    }
  } catch {
    /* storage unavailable: play without persistence */
  }
  return data;
}

export function save(): void {
  try {
    localStorage.setItem(KEY, JSON.stringify(data));
  } catch {
    /* ignore */
  }
}

export function getSave(): SaveData {
  return data;
}

export function resetSave(): void {
  data = fresh();
  save();
}

/** Level curve: each level needs 100 more XP than the previous one. */
export function levelFromXp(xp: number): number {
  let level = 1;
  let need = 100;
  let remaining = xp;
  while (remaining >= need) {
    remaining -= need;
    level++;
    need += 100;
  }
  return level;
}

export function xpProgress(xp: number): { level: number; into: number; need: number } {
  let level = 1;
  let need = 100;
  let remaining = xp;
  while (remaining >= need) {
    remaining -= need;
    level++;
    need += 100;
  }
  return { level, into: remaining, need };
}

export function addXp(amount: number): { before: number; after: number } {
  const before = levelFromXp(data.xp);
  data.xp += amount;
  save();
  return { before, after: levelFromXp(data.xp) };
}

export function markLearned(platform: string, featureId: string): void {
  const key = `${platform}:${featureId}`;
  if (!data.learned.includes(key)) data.learned.push(key);
  save();
}

export function isLearned(platform: string, featureId: string): boolean {
  return data.learned.includes(`${platform}:${featureId}`);
}

export function markBoss(platform: string): void {
  if (!data.bosses.includes(platform)) data.bosses.push(platform);
  save();
}

export function setPos(x: number, y: number): void {
  data.pos = { x, y };
  save();
}
