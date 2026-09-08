import Phaser from 'phaser';
import { BootScene } from './scenes/BootScene';
import { WorldScene } from './scenes/WorldScene';
import { HudScene } from './scenes/HudScene';
import { registerSW } from 'virtual:pwa-register';

registerSW({ immediate: true });

new Phaser.Game({
  type: Phaser.AUTO,
  parent: 'game',
  backgroundColor: '#0f1020',
  pixelArt: true,
  roundPixels: true,
  scale: {
    mode: Phaser.Scale.RESIZE,
    autoCenter: Phaser.Scale.CENTER_BOTH,
    width: window.innerWidth,
    height: window.innerHeight,
  },
  physics: { default: 'arcade', arcade: { debug: false } },
  input: { activePointers: 3 },
  scene: [BootScene, WorldScene, HudScene],
});
