/** Tiny DOM helpers for the HTML overlay that sits above the Phaser canvas. */

export const ui = (): HTMLElement => document.getElementById('ui') as HTMLElement;

export function el<K extends keyof HTMLElementTagNameMap>(
  tag: K,
  attrs: Record<string, string> = {},
  children: (Node | string)[] = [],
): HTMLElementTagNameMap[K] {
  const node = document.createElement(tag);
  for (const [k, v] of Object.entries(attrs)) {
    if (k === 'class') node.className = v;
    else if (k === 'text') node.textContent = v;
    else if (k === 'html') node.innerHTML = v;
    else node.setAttribute(k, v);
  }
  for (const c of children) node.append(c);
  return node;
}

export function showOverlay(content: HTMLElement): void {
  const root = ui();
  root.replaceChildren(content);
  root.hidden = false;
}

export function hideOverlay(): void {
  const root = ui();
  root.replaceChildren();
  root.hidden = true;
}

export function isOverlayOpen(): boolean {
  return !ui().hidden;
}

export function button(label: string, onClick: () => void, secondary = false): HTMLButtonElement {
  const b = el('button', { class: `btn${secondary ? ' secondary' : ''}`, type: 'button', text: label });
  b.addEventListener('click', onClick);
  return b;
}

/** Listen once for a real "confirm" (Enter/Space/E) key while an overlay is open. */
export function onceKey(keys: string[], cb: () => void): () => void {
  const handler = (e: KeyboardEvent) => {
    if (keys.includes(e.key)) {
      e.preventDefault();
      window.removeEventListener('keydown', handler);
      cb();
    }
  };
  window.addEventListener('keydown', handler);
  return () => window.removeEventListener('keydown', handler);
}
