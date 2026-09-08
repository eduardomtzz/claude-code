import { el, showOverlay, hideOverlay, button } from './overlay';
import { getSave, resetSave, xpProgress } from '../systems/save';
import { getContent } from '../systems/content';

export function showTitle(): Promise<'continue' | 'new'> {
  return new Promise((resolve) => {
    const s = getSave();
    const hasSave = s.xp > 0 || s.learned.length > 0;
    const { packs } = getContent();
    const totalFeatures = Object.values(packs).reduce((n, p) => n + p.features.length, 0);

    const panel = el('div', { class: 'panel center' });
    panel.append(
      el('div', { class: 'hero' }, [
        el('h1', { html: 'AI <span>Quest</span>' }),
        el('p', { text: 'Um RPG para dominar OpenAI, Claude e Manus.' }),
      ]),
    );
    panel.append(
      el('div', { class: 'legend' }, [
        el('div', { style: 'background: var(--openai)', text: 'Reino OpenAI' }),
        el('div', { style: 'background: var(--claude)', text: 'Reino Claude' }),
        el('div', { style: 'background: var(--manus)', text: 'Reino Manus' }),
      ]),
    );
    panel.append(
      el('p', { class: 'body', text: 'Fale com os mentores de cada reino, aprenda uma funcionalidade e vença a batalha de perguntas para ganhar XP. Derrote o chefe de cada reino para provar que dominou a plataforma.' }),
    );
    panel.append(
      el('p', { class: 'small', text: 'Controles: arraste na tela (joystick) ou use as setas/WASD. Toque no botão de ação ou aperte E/Espaço perto de alguém.' }),
    );
    if (hasSave) {
      const p = xpProgress(s.xp);
      panel.append(el('p', { class: 'small', text: `Progresso salvo: nível ${p.level} · ${s.learned.length}/${totalFeatures} lições · ${s.bosses.length}/3 chefes` }));
    }
    const actions = el('div', { class: 'actions' });
    if (hasSave) {
      actions.append(
        button('Continuar', () => {
          hideOverlay();
          resolve('continue');
        }),
      );
      actions.append(
        button('Novo jogo', () => {
          if (confirm('Apagar o progresso salvo e começar de novo?')) {
            resetSave();
            hideOverlay();
            resolve('new');
          }
        }, true),
      );
    } else {
      actions.append(
        button('Começar aventura', () => {
          hideOverlay();
          resolve('new');
        }),
      );
    }
    panel.append(actions);
    const updated = Object.values(packs).map((p) => `${p.name}: ${p.updatedAt}`).join(' · ');
    panel.append(el('p', { class: 'small', text: `Conteúdo atualizado em ${updated}` }));
    showOverlay(panel);
  });
}
