import type { PlatformId } from '../systems/content';

/** Tile indexes inside the generated tileset texture. */
export const T = {
  GRASS: 0,
  GRASS2: 1,
  PATH: 2,
  WATER: 3,
  TREE: 4,
  WALL: 5,
  FLOOR_OPENAI: 6,
  FLOOR_CLAUDE: 7,
  FLOOR_MANUS: 8,
  FLOOR_HUB: 9,
  FLOWER: 10,
  DOOR: 11,
  SIGN: 12,
} as const;

export const TILE = 16;
export const MAP_W = 80;
export const MAP_H = 72;

export const COLLIDES: number[] = [T.WATER, T.TREE, T.WALL];

/** Region size in tiles: 5 columns x 4 rows of mentors = 20 slots, plus a boss. */
export const REGION_W = 28;
export const REGION_H = 24;
export const NPC_SLOTS_PER_REGION = 20;

export interface Region {
  id: PlatformId;
  title: string;
  subtitle: string;
  color: number; // hex
  floor: number;
  rect: { x: number; y: number; w: number; h: number }; // in tiles
  /** Which wall has the door: regions above the hub open at the bottom, below it at the top. */
  door: 'top' | 'bottom';
  /** Where NPCs stand (tile coords). Features fill these slots in order. */
  npcSlots: { x: number; y: number }[];
  boss: { x: number; y: number; name: string };
  sign: { x: number; y: number };
}

export interface WorldTheme {
  hub: { rect: { x: number; y: number; w: number; h: number }; spawn: { x: number; y: number }; guide: { x: number; y: number } };
  regions: Region[];
}

function makeRegion(base: Omit<Region, 'rect' | 'npcSlots' | 'boss' | 'sign'> & { x: number; y: number; bossName: string }): Region {
  const { x, y, door } = base;
  const rect = { x, y, w: REGION_W, h: REGION_H };
  const cols = [4, 9, 14, 19, 24].map((dx) => x + dx);
  const rows = (door === 'bottom' ? [5, 10, 15, 20] : [3, 8, 13, 18]).map((dy) => y + dy);
  const npcSlots: { x: number; y: number }[] = [];
  for (const ry of rows) for (const cx of cols) npcSlots.push({ x: cx, y: ry });
  const boss = door === 'bottom' ? { x: x + 14, y: y + 2, name: base.bossName } : { x: x + 14, y: y + 21, name: base.bossName };
  const doorX = x + Math.floor(REGION_W / 2);
  const sign = door === 'bottom' ? { x: doorX + 1, y: y + REGION_H } : { x: doorX + 1, y: y - 1 };
  return { id: base.id, title: base.title, subtitle: base.subtitle, color: base.color, floor: base.floor, door, rect, npcSlots, boss, sign };
}

/** Three "kingdoms" around a central hub. Sizes are tiles. */
export const WORLD: WorldTheme = {
  hub: {
    rect: { x: 30, y: 32, w: 20, h: 10 },
    spawn: { x: 40, y: 38 },
    guide: { x: 40, y: 34 },
  },
  regions: [
    makeRegion({ id: 'openai', title: 'Reino OpenAI', subtitle: 'Terra do ChatGPT e da API', color: 0x10a37f, floor: T.FLOOR_OPENAI, x: 4, y: 4, door: 'bottom', bossName: 'Guardião do Token' }),
    makeRegion({ id: 'claude', title: 'Reino Claude', subtitle: 'Domínio da Anthropic e do Claude Code', color: 0xd97757, floor: T.FLOOR_CLAUDE, x: 48, y: 4, door: 'bottom', bossName: 'Sentinela do Contexto' }),
    makeRegion({ id: 'manus', title: 'Reino Manus', subtitle: 'Vale dos Agentes Autônomos', color: 0x4f7cff, floor: T.FLOOR_MANUS, x: 26, y: 44, door: 'top', bossName: 'Mestre das Tarefas' }),
  ],
};

/** Deterministic pseudo-random so the map looks the same every run. */
function mulberry32(seed: number) {
  return () => {
    seed |= 0;
    seed = (seed + 0x6d2b79f5) | 0;
    let t = Math.imul(seed ^ (seed >>> 15), 1 | seed);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

function inRect(x: number, y: number, r: { x: number; y: number; w: number; h: number }, pad = 0) {
  return x >= r.x - pad && x < r.x + r.w + pad && y >= r.y - pad && y < r.y + r.h + pad;
}

/** Builds the 2D tile array for the overworld. */
export function buildMap(): number[][] {
  const rnd = mulberry32(20260908);
  const map: number[][] = [];
  for (let y = 0; y < MAP_H; y++) {
    const row: number[] = [];
    for (let x = 0; x < MAP_W; x++) {
      const border = x < 2 || y < 2 || x >= MAP_W - 2 || y >= MAP_H - 2;
      if (border) row.push(T.WATER);
      else {
        const r = rnd();
        row.push(r < 0.06 ? T.FLOWER : r < 0.3 ? T.GRASS2 : T.GRASS);
      }
    }
    map.push(row);
  }

  // Scatter trees away from regions/hub/paths.
  const reserved = [WORLD.hub.rect, ...WORLD.regions.map((r) => r.rect)];
  for (let y = 2; y < MAP_H - 2; y++) {
    for (let x = 2; x < MAP_W - 2; x++) {
      if (reserved.some((r) => inRect(x, y, r, 2))) continue;
      if (rnd() < 0.12) map[y][x] = T.TREE;
    }
  }

  // Region floors with a wall ring and a door facing the hub.
  for (const region of WORLD.regions) {
    const { x, y, w, h } = region.rect;
    for (let yy = y; yy < y + h; yy++) {
      for (let xx = x; xx < x + w; xx++) {
        const edge = xx === x || yy === y || xx === x + w - 1 || yy === y + h - 1;
        map[yy][xx] = edge ? T.WALL : region.floor;
      }
    }
    // Door: for top regions, bottom wall center; for bottom region, top wall center.
    const doorX = x + Math.floor(w / 2);
    const doorY = region.door === 'top' ? y : y + h - 1;
    map[doorY][doorX] = T.DOOR;
    map[doorY][doorX - 1] = T.DOOR;
    map[region.sign.y][region.sign.x] = T.SIGN;
    // Boss pedestal
    map[region.boss.y][region.boss.x] = T.FLOOR_HUB;
  }

  // Hub floor
  {
    const { x, y, w, h } = WORLD.hub.rect;
    for (let yy = y; yy < y + h; yy++) for (let xx = x; xx < x + w; xx++) map[yy][xx] = T.FLOOR_HUB;
  }

  // Paths hub -> each door (L-shaped, 2 tiles wide).
  const hubC = { x: WORLD.hub.rect.x + Math.floor(WORLD.hub.rect.w / 2), y: WORLD.hub.rect.y + Math.floor(WORLD.hub.rect.h / 2) };
  for (const region of WORLD.regions) {
    const doorX = region.rect.x + Math.floor(region.rect.w / 2);
    const doorY = region.door === 'top' ? region.rect.y : region.rect.y + region.rect.h - 1;
    const outsideY = region.door === 'top' ? doorY - 1 : doorY + 1;
    // vertical from outside door to hub row
    const y0 = Math.min(outsideY, hubC.y);
    const y1 = Math.max(outsideY, hubC.y);
    for (let yy = y0; yy <= y1; yy++) for (const dx of [-1, 0]) paint(map, doorX + dx, yy);
    // horizontal along hub row
    const x0 = Math.min(doorX - 1, hubC.x);
    const x1 = Math.max(doorX, hubC.x);
    for (let xx = x0; xx <= x1; xx++) for (const dy of [0, 1]) paint(map, xx, hubC.y + dy);
  }
  return map;
}

function paint(map: number[][], x: number, y: number) {
  if (y < 0 || y >= MAP_H || x < 0 || x >= MAP_W) return;
  const cur = map[y][x];
  if (cur === T.FLOOR_HUB || cur === T.DOOR || cur === T.WALL) return;
  if (([T.FLOOR_OPENAI, T.FLOOR_CLAUDE, T.FLOOR_MANUS] as number[]).includes(cur)) return;
  map[y][x] = T.PATH;
}
