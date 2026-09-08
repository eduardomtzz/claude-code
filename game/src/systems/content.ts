/**
 * Content packs are plain JSON files in `public/content/`.
 * The game never hardcodes platform facts: everything an NPC says, every quiz
 * question, comes from these files, so refreshing knowledge = editing JSON.
 */

export type PlatformId = 'openai' | 'claude' | 'manus';

export interface Source {
  id: string;
  title: string;
  url: string;
  type: 'docs' | 'blog' | 'youtube';
  date: string | null;
  channel?: string | null;
}

export interface Feature {
  id: string;
  name: string;
  category: string;
  summary: string;
  tips: string[];
  sourceIds: string[];
}

export interface Question {
  id: string;
  featureId?: string;
  platform?: PlatformId | 'general';
  videoId?: string;
  type: 'multiple_choice';
  prompt: string;
  options: string[];
  answer: number;
  explanation: string;
  difficulty: 1 | 2 | 3;
}

export interface ContentPack {
  platform: PlatformId;
  name: string;
  updatedAt: string;
  sources: Source[];
  features: Feature[];
  questions: Question[];
}

export interface Video {
  id: string;
  platform: PlatformId | 'general';
  title: string;
  channel: string;
  url: string;
  date: string | null;
  views: string | null;
  language: 'en' | 'pt';
  tips: string[];
}

export interface YoutubePack {
  updatedAt: string;
  videos: Video[];
  questions: Question[];
}

export interface ContentDB {
  packs: Record<PlatformId, ContentPack>;
  youtube: YoutubePack;
}

const PLATFORMS: PlatformId[] = ['openai', 'claude', 'manus'];

async function fetchJson<T>(path: string): Promise<T> {
  const res = await fetch(path, { cache: 'no-cache' });
  if (!res.ok) throw new Error(`Falha ao carregar ${path}: ${res.status}`);
  return (await res.json()) as T;
}

let db: ContentDB | null = null;

export async function loadContent(): Promise<ContentDB> {
  if (db) return db;
  const base = import.meta.env.BASE_URL.replace(/\/?$/, '/');
  const [openai, claude, manus, youtube] = await Promise.all([
    fetchJson<ContentPack>(`${base}content/openai.json`),
    fetchJson<ContentPack>(`${base}content/claude.json`),
    fetchJson<ContentPack>(`${base}content/manus.json`),
    fetchJson<YoutubePack>(`${base}content/youtube.json`),
  ]);
  db = { packs: { openai, claude, manus }, youtube };
  return db;
}

export function getContent(): ContentDB {
  if (!db) throw new Error('Conteúdo ainda não carregado');
  return db;
}

export function platformIds(): PlatformId[] {
  return PLATFORMS;
}

/** Questions for one feature plus, as filler, platform-wide YouTube questions. */
export function questionsForFeature(platform: PlatformId, featureId: string, count: number): Question[] {
  const { packs, youtube } = getContent();
  const own = packs[platform].questions.filter((q) => q.featureId === featureId);
  const extra = youtube.questions.filter((q) => q.platform === platform || q.platform === 'general');
  const pool = [...shuffle(own), ...shuffle(extra)];
  return pool.slice(0, count);
}

/** Boss fights mix everything the platform has. */
export function questionsForPlatform(platform: PlatformId, count: number): Question[] {
  const { packs, youtube } = getContent();
  const pool = [
    ...packs[platform].questions,
    ...youtube.questions.filter((q) => q.platform === platform),
  ];
  return shuffle(pool).slice(0, count);
}

export function sourcesFor(platform: PlatformId, feature: Feature): Source[] {
  const pack = getContent().packs[platform];
  return feature.sourceIds
    .map((id) => pack.sources.find((s) => s.id === id))
    .filter((s): s is Source => Boolean(s));
}

export function shuffle<T>(arr: T[]): T[] {
  const a = arr.slice();
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}
