import { el, showOverlay, hideOverlay, button, onceKey } from './overlay';
import type { Feature, PlatformId, Source } from '../systems/content';

export interface DialogPage {
  speaker: string;
  text: string;
  tips?: string[];
  sources?: Source[];
}

export interface DialogOptions {
  platform?: PlatformId | 'hub';
  /** Final page buttons. Resolves with the chosen id. */
  choices?: { id: string; label: string; secondary?: boolean }[];
}

/** Shows a multi-page dialog. Resolves with chosen id ('close' if none). */
export function showDialog(pages: DialogPage[], opts: DialogOptions = {}): Promise<string> {
  return new Promise((resolve) => {
    let index = 0;
    let cleanupKey: (() => void) | null = null;

    const render = () => {
      const page = pages[index];
      const last = index === pages.length - 1;
      const panel = el('div', { class: `panel ${opts.platform ?? ''}` });
      panel.append(el('h2', { class: 'title', text: page.speaker }));
      const body = el('div', { class: 'body' });
      for (const paragraph of page.text.split('\n')) body.append(el('p', { text: paragraph }));
      if (page.tips?.length) {
        body.append(el('p', { html: '<strong>Dicas:</strong>' }));
        body.append(el('ul', { class: 'tips' }, page.tips.map((t) => el('li', { text: t }))));
      }
      if (page.sources?.length) {
        const s = el('p', { class: 'small sources', html: 'Fontes: ' });
        page.sources.forEach((src, i) => {
          if (i) s.append(' · ');
          s.append(el('a', { href: src.url, target: '_blank', rel: 'noopener', text: src.title }));
        });
        body.append(s);
      }
      panel.append(body);
      const actions = el('div', { class: 'actions' });
      const finish = (id: string) => {
        cleanupKey?.();
        hideOverlay();
        resolve(id);
      };
      if (!last) {
        const next = button('Continuar ▶', () => {
          index++;
          render();
        });
        actions.append(next);
        cleanupKey?.();
        cleanupKey = onceKey(['Enter', ' ', 'e', 'E'], () => next.click());
      } else if (opts.choices?.length) {
        for (const c of opts.choices) actions.append(button(c.label, () => finish(c.id), c.secondary));
        cleanupKey?.();
        cleanupKey = onceKey(['Enter', ' ', 'e', 'E'], () => finish(opts.choices![0].id));
      } else {
        const close = button('Fechar', () => finish('close'));
        actions.append(close);
        cleanupKey?.();
        cleanupKey = onceKey(['Enter', ' ', 'e', 'E', 'Escape'], () => close.click());
      }
      panel.append(actions);
      showOverlay(panel);
      panel.scrollTop = 0;
    };
    render();
  });
}

/** Builds the teaching dialog for one feature (NPC lesson). */
export function featurePages(npcName: string, feature: Feature, sources: Source[]): DialogPage[] {
  return [
    { speaker: npcName, text: `Quer aprender sobre **${feature.name}**? Vou te contar o essencial.`.replace(/\*\*/g, '') },
    { speaker: `${npcName} · ${feature.name}`, text: feature.summary, tips: feature.tips, sources },
  ];
}
