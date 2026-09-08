import Phaser from 'phaser';
import { T, TILE } from '../data/world';

/**
 * All art is generated at runtime with the Canvas API so the game has zero
 * binary assets to license or download. Swap these for real sprite sheets
 * (Kenney, OpenGameArt) later without touching the scenes.
 */

type Ctx = CanvasRenderingContext2D;

function px(ctx: Ctx, x: number, y: number, c: string, w = 1, h = 1) {
  ctx.fillStyle = c;
  ctx.fillRect(x, y, w, h);
}

function noise(ctx: Ctx, ox: number, oy: number, colors: string[], count: number, seed: number) {
  let s = seed;
  const rnd = () => {
    s = (s * 1664525 + 1013904223) >>> 0;
    return s / 4294967296;
  };
  for (let i = 0; i < count; i++) {
    px(ctx, ox + Math.floor(rnd() * TILE), oy + Math.floor(rnd() * TILE), colors[Math.floor(rnd() * colors.length)]);
  }
}

function drawTile(_ctx: Ctx, index: number, draw: (ox: number) => void) {
  draw(index * TILE);
}

export function createTileset(scene: Phaser.Scene): void {
  const count = 13;
  const tex = scene.textures.createCanvas('tiles', TILE * count, TILE);
  if (!tex) return;
  const ctx = tex.context;

  const fill = (ox: number, c: string) => px(ctx, ox, 0, c, TILE, TILE);

  drawTile(ctx, T.GRASS, (ox) => {
    fill(ox, '#3f9b4a');
    noise(ctx, ox, 0, ['#4aad55', '#368a41'], 14, 1);
  });
  drawTile(ctx, T.GRASS2, (ox) => {
    fill(ox, '#3a9245');
    noise(ctx, ox, 0, ['#4aad55', '#2f7d3a', '#57b862'], 18, 7);
  });
  drawTile(ctx, T.PATH, (ox) => {
    fill(ox, '#c9a86a');
    noise(ctx, ox, 0, ['#d6b87c', '#b8955a'], 16, 3);
  });
  drawTile(ctx, T.WATER, (ox) => {
    fill(ox, '#2f6fd6');
    px(ctx, ox + 2, 4, '#5a95ee', 5, 1);
    px(ctx, ox + 9, 10, '#5a95ee', 4, 1);
    px(ctx, ox + 4, 13, '#244fa8', 6, 1);
  });
  drawTile(ctx, T.TREE, (ox) => {
    fill(ox, '#3f9b4a');
    px(ctx, ox + 6, 11, '#6b4423', 4, 5);
    px(ctx, ox + 2, 3, '#1f6b2c', 12, 9);
    px(ctx, ox + 4, 1, '#1f6b2c', 8, 2);
    px(ctx, ox + 4, 4, '#2f8f3f', 6, 4);
    px(ctx, ox + 5, 2, '#3fa851', 3, 2);
  });
  drawTile(ctx, T.WALL, (ox) => {
    fill(ox, '#6f6f7a');
    for (let y = 0; y < TILE; y += 4) {
      px(ctx, ox, y, '#4d4d57', TILE, 1);
      const off = (y / 4) % 2 === 0 ? 0 : 4;
      for (let x = off; x < TILE; x += 8) px(ctx, ox + x, y, '#4d4d57', 1, 4);
    }
    noise(ctx, ox, 0, ['#8a8a96'], 10, 11);
  });
  const floor = (index: number, base: string, alt: string, line: string) =>
    drawTile(ctx, index, (ox) => {
      fill(ox, base);
      px(ctx, ox, 0, line, TILE, 1);
      px(ctx, ox, 0, line, 1, TILE);
      px(ctx, ox + 8, 8, alt, 8, 8);
      px(ctx, ox, 8, alt, 8, 8);
      px(ctx, ox + 8, 0, base, 8, 8);
      px(ctx, ox + 8, 8, alt, 1, 8);
      px(ctx, ox, 8, line, TILE, 1);
      px(ctx, ox + 8, 0, line, 1, TILE);
    });
  floor(T.FLOOR_OPENAI, '#bfe6d4', '#a9d9c3', '#8fc2ab');
  floor(T.FLOOR_CLAUDE, '#f3d6c4', '#e9c3ac', '#d2a58b');
  floor(T.FLOOR_MANUS, '#cbd8ff', '#b5c6fb', '#96a8e6');
  floor(T.FLOOR_HUB, '#d9d4e8', '#c8c1de', '#a99fc6');
  drawTile(ctx, T.FLOWER, (ox) => {
    fill(ox, '#3f9b4a');
    noise(ctx, ox, 0, ['#4aad55', '#368a41'], 10, 5);
    px(ctx, ox + 4, 5, '#ff6b9d', 2, 2);
    px(ctx, ox + 10, 9, '#ffe066', 2, 2);
    px(ctx, ox + 7, 12, '#ffffff', 2, 2);
  });
  drawTile(ctx, T.DOOR, (ox) => {
    fill(ox, '#c9a86a');
    px(ctx, ox, 0, '#6f6f7a', TILE, 2);
    px(ctx, ox, 14, '#6f6f7a', TILE, 2);
    noise(ctx, ox, 0, ['#d6b87c'], 8, 21);
  });
  drawTile(ctx, T.SIGN, (ox) => {
    fill(ox, '#c9a86a');
    px(ctx, ox + 7, 8, '#7a5230', 2, 8);
    px(ctx, ox + 2, 2, '#a9743f', 12, 7);
    px(ctx, ox + 3, 3, '#e8c98f', 10, 5);
    px(ctx, ox + 4, 5, '#7a5230', 8, 1);
  });

  tex.refresh();
}

/** Simple 16x16 character sprites: 4 directions x 2 walk frames, drawn from pixel strings. */
const CHAR = {
  down: [
    '....HHHHHH......',
    '...HHHHHHHH.....',
    '...HSSSSSSH.....',
    '...HSESSESH.....',
    '...HSSSSSSH.....',
    '....SSMMSS......',
    '.....SSSS.......',
    '...BBBBBBBB.....',
    '..SBBBBBBBBS....',
    '..SBBBBBBBBS....',
    '..SBBBBBBBBS....',
    '...BBBBBBBB.....',
    '....PPPPPP......',
    '....PP..PP......',
    '....FF..FF......',
    '................',
  ],
  up: [
    '....HHHHHH......',
    '...HHHHHHHH.....',
    '...HHHHHHHH.....',
    '...HHHHHHHH.....',
    '...HHHHHHHH.....',
    '....HHHHHH......',
    '.....SSSS.......',
    '...BBBBBBBB.....',
    '..SBBBBBBBBS....',
    '..SBBBBBBBBS....',
    '..SBBBBBBBBS....',
    '...BBBBBBBB.....',
    '....PPPPPP......',
    '....PP..PP......',
    '....FF..FF......',
    '................',
  ],
  side: [
    '....HHHHHH......',
    '...HHHHHHHH.....',
    '...HHSSSSS......',
    '...HHSESSS......',
    '...HHSSSSS......',
    '....SSSMS.......',
    '.....SSSS.......',
    '....BBBBBB......',
    '...BBBBBBBS.....',
    '...BBBBBBBS.....',
    '...BBBBBBB......',
    '....BBBBBB......',
    '....PPPPPP......',
    '....PP..PP......',
    '....FF..FF......',
    '................',
  ],
};

export interface Palette {
  H: string; // hair
  S: string; // skin
  E: string; // eyes
  M: string; // mouth
  B: string; // body
  P: string; // pants
  F: string; // feet
}

export const PALETTES: Record<string, Palette> = {
  player: { H: '#3b2a1a', S: '#f2c9a0', E: '#1a1a1a', M: '#c96a5a', B: '#3b6fe0', P: '#2a2a44', F: '#5a3a22' },
  openai: { H: '#e8e8e8', S: '#f2c9a0', E: '#1a1a1a', M: '#c96a5a', B: '#10a37f', P: '#0b5f4a', F: '#333333' },
  claude: { H: '#5a3a22', S: '#f2c9a0', E: '#1a1a1a', M: '#c96a5a', B: '#d97757', P: '#7a3b26', F: '#333333' },
  manus: { H: '#1c1c2e', S: '#e6b48f', E: '#1a1a1a', M: '#c96a5a', B: '#4f7cff', P: '#25397f', F: '#333333' },
  guide: { H: '#c9c9c9', S: '#f2c9a0', E: '#1a1a1a', M: '#c96a5a', B: '#8b5cf6', P: '#3b2a6b', F: '#333333' },
  boss: { H: '#1a1a1a', S: '#c9c9c9', E: '#ff3b3b', M: '#7a1a1a', B: '#2a2a2a', P: '#111111', F: '#000000' },
};

export function createCharacter(scene: Phaser.Scene, key: string, pal: Palette): void {
  // Sheet layout (frame index): 0-1 down, 2-3 up, 4-5 right (left is flipX)
  const frames = 6;
  const tex = scene.textures.createCanvas(key, TILE * frames, TILE);
  if (!tex) return;
  const ctx = tex.context;
  const draw = (rows: string[], frame: number, legShift: number) => {
    const ox = frame * TILE;
    rows.forEach((row, y) => {
      [...row].forEach((ch, x) => {
        if (ch === '.') return;
        let yy = y;
        if ((ch === 'P' || ch === 'F') && y >= 13) yy = y + (legShift && x < 8 ? 1 : 0);
        if (yy >= TILE) return;
        px(ctx, ox + x, yy, pal[ch as keyof Palette]);
      });
    });
  };
  draw(CHAR.down, 0, 0);
  draw(CHAR.down, 1, 1);
  draw(CHAR.up, 2, 0);
  draw(CHAR.up, 3, 1);
  draw(CHAR.side, 4, 0);
  draw(CHAR.side, 5, 1);
  tex.refresh();
  for (let i = 0; i < frames; i++) tex.add(i, 0, i * TILE, 0, TILE, TILE);
}

export function createMarkers(scene: Phaser.Scene): void {
  const tex = scene.textures.createCanvas('markers', 32, 16);
  if (!tex) return;
  const ctx = tex.context;
  // 0: "!" quest available, 1: check mark learned
  px(ctx, 6, 2, '#ffe066', 4, 8);
  px(ctx, 6, 12, '#ffe066', 4, 2);
  px(ctx, 16 + 3, 8, '#7CFC9A', 2, 2);
  px(ctx, 16 + 5, 10, '#7CFC9A', 2, 2);
  px(ctx, 16 + 7, 8, '#7CFC9A', 2, 2);
  px(ctx, 16 + 9, 6, '#7CFC9A', 2, 2);
  px(ctx, 16 + 11, 4, '#7CFC9A', 2, 2);
  tex.refresh();
  tex.add(0, 0, 0, 0, 16, 16);
  tex.add(1, 0, 16, 0, 16, 16);
}
