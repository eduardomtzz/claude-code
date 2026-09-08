import Phaser from 'phaser';
import { loadContent } from '../systems/content';
import { loadSave } from '../systems/save';
import { createTileset, createCharacter, createMarkers, PALETTES } from '../systems/textures';
import { showTitle } from '../ui/title';

export class BootScene extends Phaser.Scene {
  constructor() {
    super('Boot');
  }

  create(): void {
    const { width, height } = this.scale;
    const label = this.add
      .text(width / 2, height / 2, 'Carregando conhecimento…', { fontFamily: 'system-ui, sans-serif', fontSize: '18px', color: '#ffffff' })
      .setOrigin(0.5);

    createTileset(this);
    for (const [key, pal] of Object.entries(PALETTES)) createCharacter(this, `char-${key}`, pal);
    createMarkers(this);
    loadSave();

    loadContent()
      .then(async () => {
        label.destroy();
        const mode = await showTitle();
        this.scene.start('World', { fresh: mode === 'new' });
      })
      .catch((err: Error) => {
        label.setText(`Erro ao carregar conteúdo:\n${err.message}\n\nVerifique a pasta public/content.`).setAlign('center');
      });
  }
}
