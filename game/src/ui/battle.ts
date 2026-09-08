import { el, showOverlay, hideOverlay, button } from './overlay';
import type { PlatformId, Question } from '../systems/content';
import { getSave, save } from '../systems/save';

export interface BattleConfig {
  platform: PlatformId;
  enemyName: string;
  enemyHp: number;
  playerHp: number;
  questions: Question[];
  /** Damage dealt per correct answer (base). */
  baseDamage?: number;
  /** Damage taken per wrong answer. */
  enemyDamage?: number;
  boss?: boolean;
}

export interface BattleResult {
  won: boolean;
  correct: number;
  wrong: number;
  bestStreak: number;
  xp: number;
}

/**
 * Turn-based quiz battle. Correct answer = you hit the enemy (streak bonus).
 * Wrong answer = the enemy hits you and you read the explanation.
 */
export function runBattle(cfg: BattleConfig): Promise<BattleResult> {
  return new Promise((resolve) => {
    const baseDamage = cfg.baseDamage ?? 30;
    const enemyDamage = cfg.enemyDamage ?? 25;
    let enemyHp = cfg.enemyHp;
    let playerHp = cfg.playerHp;
    let streak = 0;
    let bestStreak = 0;
    let correct = 0;
    let wrong = 0;
    let qi = 0;
    const questions = cfg.questions;

    const stats = getSave().stats;
    stats.battles++;

    const finish = (won: boolean) => {
      stats.correct += correct;
      stats.wrong += wrong;
      if (won) stats.wins++;
      stats.bestStreak = Math.max(stats.bestStreak, bestStreak);
      save();
      const xp = won ? correct * 20 + bestStreak * 10 + (cfg.boss ? 150 : 50) : correct * 5;
      hideOverlay();
      resolve({ won, correct, wrong, bestStreak, xp });
    };

    const hpBlock = (name: string, hp: number, max: number, enemy = false) => {
      const pct = Math.max(0, Math.round((hp / max) * 100));
      return el('div', { class: `hp ${enemy ? 'enemy' : ''}` }, [
        el('div', { class: 'name' }, [el('span', { text: name }), el('span', { text: `${Math.max(0, hp)}/${max}` })]),
        el('div', { class: 'bar' }, [el('i', { style: `width:${pct}%` })]),
      ]);
    };

    const render = () => {
      if (qi >= questions.length) {
        // Ran out of questions: decide by remaining HP ratio.
        finish(enemyHp / cfg.enemyHp <= playerHp / cfg.playerHp);
        return;
      }
      const q = questions[qi];
      const panel = el('div', { class: `panel full ${cfg.platform}` });
      panel.append(
        el('h2', { class: 'title' }, [
          el('span', { class: `chip ${cfg.platform}`, text: cfg.boss ? 'CHEFE' : 'BATALHA' }),
          el('span', { text: cfg.enemyName }),
        ]),
      );
      const hpRow = el('div', { class: 'hp-row' }, [
        hpBlock('Você', playerHp, cfg.playerHp),
        hpBlock(cfg.enemyName, enemyHp, cfg.enemyHp, true),
      ]);
      panel.append(hpRow);
      panel.append(
        el('div', { class: 'subtitle' }, [
          el('span', { text: `Pergunta ${qi + 1} de ${questions.length} · dificuldade ${'★'.repeat(q.difficulty)}` }),
          el('span', { class: 'streak', text: streak >= 2 ? `   🔥 sequência x${streak}` : '' }),
        ]),
      );
      panel.append(el('div', { class: 'question', text: q.prompt }));
      const options = el('div', { class: 'options' });
      const letters = ['A', 'B', 'C', 'D'];
      const buttons: HTMLButtonElement[] = [];
      q.options.forEach((opt, i) => {
        const b = el('button', { type: 'button', text: `${letters[i]}) ${opt}` });
        b.addEventListener('click', () => answer(i));
        buttons.push(b);
        options.append(b);
      });
      panel.append(options);

      const answer = (i: number) => {
        buttons.forEach((b) => (b.disabled = true));
        const ok = i === q.answer;
        buttons[q.answer].classList.add('correct');
        if (!ok) buttons[i].classList.add('wrong');
        let msg: string;
        if (ok) {
          correct++;
          streak++;
          bestStreak = Math.max(bestStreak, streak);
          const dmg = baseDamage + (streak - 1) * 10 + (q.difficulty - 1) * 5;
          enemyHp -= dmg;
          msg = `✅ Acertou! Você causou ${dmg} de dano.`;
        } else {
          wrong++;
          streak = 0;
          playerHp -= enemyDamage;
          msg = `❌ Errou. ${cfg.enemyName} causou ${enemyDamage} de dano.`;
          panel.classList.add('shake');
        }
        hpRow.replaceWith(hpBlockRow());
        const fb = el('div', { class: `feedback ${ok ? 'ok' : 'bad'}` }, [
          el('div', { html: `<strong>${msg}</strong>` }),
          el('div', { text: q.explanation }),
        ]);
        panel.append(fb);
        const actions = el('div', { class: 'actions' });
        const done = enemyHp <= 0 || playerHp <= 0;
        actions.append(
          button(done ? (enemyHp <= 0 ? 'Vitória! 🎉' : 'Derrota…') : 'Próxima pergunta ▶', () => {
            if (done) finish(enemyHp <= 0);
            else {
              qi++;
              render();
            }
          }),
        );
        panel.append(actions);
        fb.scrollIntoView({ behavior: 'smooth', block: 'end' });
      };

      const hpBlockRow = () =>
        el('div', { class: 'hp-row' }, [hpBlock('Você', playerHp, cfg.playerHp), hpBlock(cfg.enemyName, enemyHp, cfg.enemyHp, true)]);

      showOverlay(panel);
      panel.scrollTop = 0;
    };

    render();
  });
}
