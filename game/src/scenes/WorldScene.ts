import Phaser from 'phaser';
import { buildMap, COLLIDES, MAP_H, MAP_W, TILE, WORLD, type Region } from '../data/world';
import { getContent, questionsForFeature, questionsForPlatform, sourcesFor, type Feature, type PlatformId } from '../systems/content';
import { addXp, getSave, isLearned, markBoss, markLearned, setPos } from '../systems/save';
import { showDialog, featurePages } from '../ui/dialog';
import { runBattle } from '../ui/battle';
import { isOverlayOpen } from '../ui/overlay';
import { mountHud, refreshHud, setRegionLabel } from '../ui/hud';
import type { HudScene } from './HudScene';

type Interactable =
  | { kind: 'npc'; sprite: Phaser.Physics.Arcade.Sprite; region: Region; feature: Feature; name: string; marker: Phaser.GameObjects.Image }
  | { kind: 'boss'; sprite: Phaser.Physics.Arcade.Sprite; region: Region; marker: Phaser.GameObjects.Image }
  | { kind: 'guide'; sprite: Phaser.Physics.Arcade.Sprite }
  | { kind: 'sign'; x: number; y: number; region: Region };

const NPC_NAMES = ['Mestre', 'Sábia', 'Arquiteto', 'Guardiã', 'Escriba', 'Alquimista', 'Navegadora', 'Oráculo'];

export class WorldScene extends Phaser.Scene {
  private player!: Phaser.Physics.Arcade.Sprite;
  private cursors!: Phaser.Types.Input.Keyboard.CursorKeys;
  private wasd!: Record<'W' | 'A' | 'S' | 'D' | 'E' | 'SPACE', Phaser.Input.Keyboard.Key>;
  private hud!: HudScene;
  private interactables: Interactable[] = [];
  private prompt!: Phaser.GameObjects.Text;
  private busy = false;
  private facing: 'down' | 'up' | 'left' | 'right' = 'down';
  private currentRegion: string | null = null;

  constructor() {
    super('World');
  }

  create(data: { fresh?: boolean }): void {
    const map = this.make.tilemap({ data: buildMap(), tileWidth: TILE, tileHeight: TILE });
    const tiles = map.addTilesetImage('tiles', 'tiles', TILE, TILE, 0, 0)!;
    const layer = map.createLayer(0, tiles, 0, 0)!;
    layer.setCollision(COLLIDES);

    this.physics.world.setBounds(0, 0, MAP_W * TILE, MAP_H * TILE);

    // Player
    const saved = getSave().pos;
    const spawn = !data.fresh && saved ? saved : { x: WORLD.hub.spawn.x * TILE + 8, y: WORLD.hub.spawn.y * TILE + 8 };
    this.player = this.physics.add.sprite(spawn.x, spawn.y, 'char-player', 0);
    this.player.setSize(10, 8).setOffset(3, 8).setCollideWorldBounds(true).setDepth(5);
    this.physics.add.collider(this.player, layer);
    this.createAnims('char-player');

    // Region labels + NPCs
    const { packs } = getContent();
    for (const region of WORLD.regions) {
      const pack = packs[region.id];
      this.createAnims(`char-${region.id}`);
      this.add
        .text(region.rect.x * TILE + (region.rect.w * TILE) / 2, region.rect.y * TILE - 10, region.title, {
          fontFamily: 'system-ui, sans-serif', fontSize: '10px', color: '#ffffff', stroke: '#000', strokeThickness: 3,
        })
        .setOrigin(0.5)
        .setDepth(20);

      region.npcSlots.forEach((slot, i) => {
        const feature = pack.features[i];
        if (!feature) return;
        const sprite = this.physics.add.sprite(slot.x * TILE + 8, slot.y * TILE + 8, `char-${region.id}`, 0).setImmovable(true).setDepth(4);
        sprite.body!.setSize(12, 12).setOffset(2, 4);
        this.physics.add.collider(this.player, sprite);
        const marker = this.add.image(sprite.x, sprite.y - 14, 'markers', isLearned(region.id, feature.id) ? 1 : 0).setDepth(6);
        this.tweens.add({ targets: marker, y: marker.y - 3, duration: 600, yoyo: true, repeat: -1, ease: 'Sine.easeInOut' });
        const name = `${NPC_NAMES[i % NPC_NAMES.length]} ${this.shortName(feature.name)}`;
        this.interactables.push({ kind: 'npc', sprite, region, feature, name, marker });
      });

      const bossSprite = this.physics.add.sprite(region.boss.x * TILE + 8, region.boss.y * TILE + 8, 'char-boss', 0).setImmovable(true).setDepth(4).setScale(1.25);
      bossSprite.body!.setSize(12, 12).setOffset(2, 4);
      this.physics.add.collider(this.player, bossSprite);
      const bossMarker = this.add.image(bossSprite.x, bossSprite.y - 18, 'markers', getSave().bosses.includes(region.id) ? 1 : 0).setDepth(6);
      this.interactables.push({ kind: 'boss', sprite: bossSprite, region, marker: bossMarker });
      this.interactables.push({ kind: 'sign', x: region.sign.x * TILE + 8, y: region.sign.y * TILE + 8, region });
    }
    this.createAnims('char-guide');
    const guide = this.physics.add.sprite(WORLD.hub.guide.x * TILE + 8, WORLD.hub.guide.y * TILE + 8, 'char-guide', 0).setImmovable(true).setDepth(4);
    guide.body!.setSize(12, 12).setOffset(2, 4);
    this.physics.add.collider(this.player, guide);
    this.interactables.push({ kind: 'guide', sprite: guide });
    this.add
      .text(WORLD.hub.rect.x * TILE + (WORLD.hub.rect.w * TILE) / 2, WORLD.hub.rect.y * TILE - 6, 'Praça Central', {
        fontFamily: 'system-ui, sans-serif', fontSize: '10px', color: '#ffffff', stroke: '#000', strokeThickness: 3,
      })
      .setOrigin(0.5)
      .setDepth(20);

    // Camera
    this.cameras.main.setBounds(0, 0, MAP_W * TILE, MAP_H * TILE).startFollow(this.player, true, 0.15, 0.15).setRoundPixels(true);
    this.applyZoom();
    this.scale.on('resize', () => this.applyZoom());

    // Input
    this.cursors = this.input.keyboard!.createCursorKeys();
    this.wasd = this.input.keyboard!.addKeys('W,A,S,D,E,SPACE') as WorldScene['wasd'];

    this.scene.launch('Hud');
    this.hud = this.scene.get('Hud') as HudScene;

    this.prompt = this.add
      .text(0, 0, '', { fontFamily: 'system-ui, sans-serif', fontSize: '9px', color: '#fff', backgroundColor: '#000000aa', padding: { x: 4, y: 2 } })
      .setOrigin(0.5, 1)
      .setDepth(30)
      .setVisible(false);

    mountHud(() => this.openMenu());
    refreshHud();

    if (data.fresh) this.time.delayedCall(300, () => this.intro());

    this.time.addEvent({ delay: 3000, loop: true, callback: () => setPos(this.player.x, this.player.y) });

    // Test hook used by the /playtest skill and smoke tests: window.__aiquest.teleport(tileX, tileY)
    (window as unknown as { __aiquest: unknown }).__aiquest = {
      teleport: (tx: number, ty: number) => this.player.setPosition(tx * TILE + 8, ty * TILE + 8),
      npcs: () => this.interactables.filter((i) => i.kind === 'npc').map((i) => (i.kind === 'npc' ? { x: i.sprite.x / TILE, y: i.sprite.y / TILE, name: i.name } : null)),
    };
  }

  /** Short label for battle headers: cut at the first parenthesis/colon, cap length. */
  private battleName(name: string): string {
    const cut = name.split(/[(:]/)[0].trim();
    return cut.length > 32 ? `${cut.slice(0, 30)}…` : cut;
  }

  private shortName(name: string): string {
    const first = name.split(/[\s(:]/)[0];
    return first.length > 14 ? first.slice(0, 14) : first;
  }

  private applyZoom(): void {
    const { width, height } = this.scale;
    const shortest = Math.min(width, height);
    // Aim for roughly 14 tiles across the shortest axis.
    const zoom = Phaser.Math.Clamp(Math.round((shortest / (14 * TILE)) * 2) / 2, 1.5, 4);
    this.cameras.main.setZoom(zoom);
  }

  private createAnims(key: string): void {
    if (this.anims.exists(`${key}-down`)) return;
    const mk = (suffix: string, frames: number[]) =>
      this.anims.create({ key: `${key}-${suffix}`, frames: frames.map((f) => ({ key, frame: f })), frameRate: 6, repeat: -1 });
    mk('down', [0, 1]);
    mk('up', [2, 3]);
    mk('side', [4, 5]);
  }

  update(): void {
    if (this.busy || isOverlayOpen()) {
      this.player.setVelocity(0, 0);
      this.player.anims.stop();
      return;
    }
    const speed = 90;
    let vx = 0;
    let vy = 0;
    if (this.cursors.left.isDown || this.wasd.A.isDown) vx = -1;
    else if (this.cursors.right.isDown || this.wasd.D.isDown) vx = 1;
    if (this.cursors.up.isDown || this.wasd.W.isDown) vy = -1;
    else if (this.cursors.down.isDown || this.wasd.S.isDown) vy = 1;
    if (vx === 0 && vy === 0 && this.hud?.vector.length() > 0) {
      vx = this.hud.vector.x;
      vy = this.hud.vector.y;
    }
    const v = new Phaser.Math.Vector2(vx, vy);
    if (v.length() > 1) v.normalize();
    this.player.setVelocity(v.x * speed, v.y * speed);

    if (v.length() > 0) {
      if (Math.abs(v.x) > Math.abs(v.y)) {
        this.facing = v.x < 0 ? 'left' : 'right';
        this.player.setFlipX(v.x < 0);
        this.player.anims.play('char-player-side', true);
      } else {
        this.facing = v.y < 0 ? 'up' : 'down';
        this.player.setFlipX(false);
        this.player.anims.play(`char-player-${this.facing}`, true);
      }
    } else {
      this.player.anims.stop();
      this.player.setFrame(this.facing === 'up' ? 2 : this.facing === 'down' ? 0 : 4);
    }

    // Nearest interactable
    const near = this.nearest();
    if (near) {
      const label = near.kind === 'npc' ? near.name : near.kind === 'boss' ? near.region.boss.name : near.kind === 'guide' ? 'Guia' : 'Placa';
      const pos = near.kind === 'sign' ? { x: near.x, y: near.y } : { x: near.sprite.x, y: near.sprite.y };
      this.prompt.setText(`${label}  [A]`).setPosition(pos.x, pos.y - 20).setVisible(true);
    } else this.prompt.setVisible(false);

    const pressed =
      Phaser.Input.Keyboard.JustDown(this.wasd.E) || Phaser.Input.Keyboard.JustDown(this.wasd.SPACE) || this.hud?.consumeAction();
    if (pressed && near) void this.interact(near);

    this.updateRegionLabel();
  }

  private nearest(): Interactable | null {
    let best: Interactable | null = null;
    let bestD = 26;
    for (const it of this.interactables) {
      const pos = it.kind === 'sign' ? { x: it.x, y: it.y } : { x: it.sprite.x, y: it.sprite.y };
      const d = Phaser.Math.Distance.Between(this.player.x, this.player.y, pos.x, pos.y);
      if (d < bestD) {
        bestD = d;
        best = it;
      }
    }
    return best;
  }

  private updateRegionLabel(): void {
    const tx = Math.floor(this.player.x / TILE);
    const ty = Math.floor(this.player.y / TILE);
    let label = 'Campo';
    for (const r of WORLD.regions) {
      if (tx >= r.rect.x && tx < r.rect.x + r.rect.w && ty >= r.rect.y && ty < r.rect.y + r.rect.h) label = r.title;
    }
    const h = WORLD.hub.rect;
    if (tx >= h.x && tx < h.x + h.w && ty >= h.y && ty < h.y + h.h) label = 'Praça Central';
    if (label !== this.currentRegion) {
      this.currentRegion = label;
      setRegionLabel(label);
    }
  }

  private async interact(it: Interactable): Promise<void> {
    this.busy = true;
    this.hud.setControlsVisible(false);
    try {
      if (it.kind === 'guide') await this.talkGuide();
      else if (it.kind === 'sign') await this.readSign(it.region);
      else if (it.kind === 'npc') await this.talkNpc(it);
      else if (it.kind === 'boss') await this.fightBoss(it);
    } finally {
      this.busy = false;
      this.hud.setControlsVisible(true);
      refreshHud();
    }
  }

  private async intro(): Promise<void> {
    this.busy = true;
    this.hud.setControlsVisible(false);
    await showDialog([
      { speaker: 'Guia', text: 'Bem-vindo à Praça Central, aventureiro! Três reinos cercam esta praça: OpenAI ao noroeste, Claude ao nordeste e Manus ao sul.' },
      { speaker: 'Guia', text: 'Em cada reino, mentores ensinam uma funcionalidade da plataforma. Depois da lição, você enfrenta uma batalha de perguntas. Acertar ataca, errar machuca.' },
      { speaker: 'Guia', text: 'Quando aprender tudo de um reino, desafie o chefe. Vá em frente: siga as trilhas de areia.' },
    ], { platform: 'hub' });
    this.busy = false;
    this.hud.setControlsVisible(true);
  }

  private async talkGuide(): Promise<void> {
    const s = getSave();
    const { packs } = getContent();
    const lines = WORLD.regions.map((r) => {
      const total = Math.min(packs[r.id].features.length, r.npcSlots.length);
      const learned = packs[r.id].features.slice(0, total).filter((f) => isLearned(r.id, f.id)).length;
      return `${r.title}: ${learned}/${total} lições${s.bosses.includes(r.id) ? ' · chefe derrotado ✔' : ''}`;
    });
    await showDialog([
      { speaker: 'Guia', text: `Seu progresso:\n${lines.join('\n')}` },
      { speaker: 'Guia', text: `Estatísticas: ${s.stats.battles} batalhas, ${s.stats.wins} vitórias, ${s.stats.correct} acertos, ${s.stats.wrong} erros, melhor sequência ${s.stats.bestStreak}.` },
    ], { platform: 'hub' });
  }

  private async readSign(region: Region): Promise<void> {
    const pack = getContent().packs[region.id];
    await showDialog([
      { speaker: region.title, text: `${region.subtitle}.\n${pack.features.length} funcionalidades catalogadas · conteúdo de ${pack.updatedAt}.\nFale com os mentores marcados com "!" e depois desafie ${region.boss.name}.` },
    ], { platform: region.id });
  }

  private async talkNpc(it: Extract<Interactable, { kind: 'npc' }>): Promise<void> {
    const { region, feature } = it;
    const learned = isLearned(region.id, feature.id);
    const pages = featurePages(it.name, feature, sourcesFor(region.id, feature));
    const choice = await showDialog(pages, {
      platform: region.id,
      choices: [
        { id: 'battle', label: learned ? 'Treinar de novo ⚔️' : 'Aceitar o desafio ⚔️' },
        { id: 'later', label: 'Depois', secondary: true },
      ],
    });
    if (choice !== 'battle') return;
    const questions = questionsForFeature(region.id, feature.id, 4);
    if (questions.length === 0) {
      await showDialog([{ speaker: it.name, text: 'Ainda não tenho perguntas preparadas. Volte quando o conteúdo for atualizado.' }], { platform: region.id });
      return;
    }
    const result = await runBattle({
      platform: region.id,
      enemyName: `Dúvida: ${this.battleName(feature.name)}`,
      enemyHp: 80,
      playerHp: 100,
      questions,
    });
    await this.afterBattle(result.won, result.xp, result.correct, result.wrong, () => {
      if (!learned) {
        markLearned(region.id, feature.id);
        it.marker.setFrame(1);
      }
    }, region.id);
  }

  private async fightBoss(it: Extract<Interactable, { kind: 'boss' }>): Promise<void> {
    const { region } = it;
    const pack = getContent().packs[region.id];
    const total = Math.min(pack.features.length, region.npcSlots.length);
    const learned = pack.features.slice(0, total).filter((f) => isLearned(region.id, f.id)).length;
    const beaten = getSave().bosses.includes(region.id);
    const required = Math.ceil(total * 0.75);
    if (learned < required && !beaten) {
      await showDialog([
        { speaker: region.boss.name, text: `Você ainda não está pronto. Aprenda com pelo menos ${required} dos ${total} mentores deste reino (você tem ${learned}) e volte.` },
      ], { platform: region.id });
      return;
    }
    const choice = await showDialog([
      { speaker: region.boss.name, text: beaten ? 'Quer testar seu domínio outra vez?' : `Então você acha que domina ${pack.name}? Prove. Serão 8 perguntas de todo o reino.` },
    ], { platform: region.id, choices: [{ id: 'fight', label: 'Lutar! ⚔️' }, { id: 'later', label: 'Ainda não', secondary: true }] });
    if (choice !== 'fight') return;
    const result = await runBattle({
      platform: region.id,
      enemyName: region.boss.name,
      enemyHp: 200,
      playerHp: 100,
      questions: questionsForPlatform(region.id, 8),
      enemyDamage: 30,
      boss: true,
    });
    await this.afterBattle(result.won, result.xp, result.correct, result.wrong, () => {
      markBoss(region.id);
      it.marker.setFrame(1);
    }, region.id);
  }

  private async afterBattle(won: boolean, xp: number, correct: number, wrong: number, onWin: () => void, platform: PlatformId): Promise<void> {
    const { before, after } = addXp(xp);
    if (won) onWin();
    refreshHud();
    const text = won
      ? `Vitória! ${correct} acertos, ${wrong} erros. Você ganhou ${xp} XP.${after > before ? `\nSubiu para o nível ${after}! 🎉` : ''}`
      : `Derrota. ${correct} acertos, ${wrong} erros. Você ganhou ${xp} XP de consolação. Releia a lição e tente de novo.`;
    await showDialog([{ speaker: won ? 'Vitória' : 'Derrota', text }], { platform });
  }

  private async openMenu(): Promise<void> {
    if (this.busy || isOverlayOpen()) return;
    this.busy = true;
    this.hud.setControlsVisible(false);
    const choice = await showDialog([{ speaker: 'Menu', text: 'O progresso é salvo automaticamente neste navegador.' }], {
      platform: 'hub',
      choices: [
        { id: 'resume', label: 'Voltar ao jogo' },
        { id: 'title', label: 'Tela inicial', secondary: true },
      ],
    });
    this.busy = false;
    this.hud.setControlsVisible(true);
    if (choice === 'title') {
      setPos(this.player.x, this.player.y);
      this.scene.stop('Hud');
      this.scene.start('Boot');
    }
  }
}
