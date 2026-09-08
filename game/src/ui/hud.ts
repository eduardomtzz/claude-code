import { el } from './overlay';
import { getSave, xpProgress } from '../systems/save';

let root: HTMLElement | null = null;
let regionLabel: HTMLElement | null = null;
let onMenu: (() => void) | null = null;

export function mountHud(menuHandler: () => void): void {
  onMenu = menuHandler;
  if (root) return;
  root = el('div', { id: 'hud' });
  document.body.append(root);
  refreshHud();
}

export function setRegionLabel(text: string): void {
  if (regionLabel) regionLabel.textContent = text;
}

export function refreshHud(): void {
  if (!root) return;
  const s = getSave();
  const p = xpProgress(s.xp);
  const pct = Math.round((p.into / p.need) * 100);
  const menu = el('button', { type: 'button', text: '☰' });
  menu.addEventListener('click', () => onMenu?.());
  regionLabel = el('span', { class: 'region', text: regionLabel?.textContent ?? 'Praça Central' });
  root.replaceChildren(
    el('span', { text: `Nv ${p.level}` }),
    el('div', { class: 'xpbar' }, [el('i', { style: `width:${pct}%` })]),
    el('span', { text: `${p.into}/${p.need} XP` }),
    regionLabel,
    menu,
  );
}

export function unmountHud(): void {
  root?.remove();
  root = null;
}
