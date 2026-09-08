import Phaser from 'phaser';

/**
 * Touch controls drawn on top of the world: a floating joystick on the left
 * half of the screen and an action button on the right. Keyboard still works.
 */
export class HudScene extends Phaser.Scene {
  private base!: Phaser.GameObjects.Arc;
  private thumb!: Phaser.GameObjects.Arc;
  private actionBtn!: Phaser.GameObjects.Container;
  private joyPointerId: number | null = null;
  private origin = new Phaser.Math.Vector2();
  public vector = new Phaser.Math.Vector2(0, 0);
  public actionPressed = false;
  private radius = 44;

  constructor() {
    super({ key: 'Hud', active: false });
  }

  create(): void {
    this.base = this.add.circle(0, 0, this.radius, 0xffffff, 0.15).setStrokeStyle(2, 0xffffff, 0.4).setVisible(false).setDepth(10);
    this.thumb = this.add.circle(0, 0, 20, 0xffffff, 0.5).setVisible(false).setDepth(11);

    const btnBg = this.add.circle(0, 0, 34, 0x8b5cf6, 0.75).setStrokeStyle(3, 0xffffff, 0.6);
    const btnTxt = this.add.text(0, 0, 'A', { fontFamily: 'system-ui, sans-serif', fontSize: '26px', color: '#ffffff', fontStyle: 'bold' }).setOrigin(0.5);
    this.actionBtn = this.add.container(0, 0, [btnBg, btnTxt]).setDepth(10);
    btnBg.setInteractive(new Phaser.Geom.Circle(0, 0, 40), Phaser.Geom.Circle.Contains);
    btnBg.on('pointerdown', () => {
      this.actionPressed = true;
      btnBg.setFillStyle(0xa78bfa, 0.9);
    });
    btnBg.on('pointerup', () => btnBg.setFillStyle(0x8b5cf6, 0.75));
    btnBg.on('pointerout', () => btnBg.setFillStyle(0x8b5cf6, 0.75));

    this.input.addPointer(2);
    this.input.on('pointerdown', (p: Phaser.Input.Pointer) => {
      if (this.joyPointerId !== null) return;
      if (p.x > this.scale.width * 0.55) return; // right side reserved for action button
      this.joyPointerId = p.id;
      this.origin.set(p.x, p.y);
      this.base.setPosition(p.x, p.y).setVisible(true);
      this.thumb.setPosition(p.x, p.y).setVisible(true);
    });
    this.input.on('pointermove', (p: Phaser.Input.Pointer) => {
      if (p.id !== this.joyPointerId) return;
      const dx = p.x - this.origin.x;
      const dy = p.y - this.origin.y;
      const len = Math.min(Math.hypot(dx, dy), this.radius);
      const ang = Math.atan2(dy, dx);
      this.thumb.setPosition(this.origin.x + Math.cos(ang) * len, this.origin.y + Math.sin(ang) * len);
      const strength = len / this.radius;
      this.vector.set(strength < 0.15 ? 0 : Math.cos(ang) * strength, strength < 0.15 ? 0 : Math.sin(ang) * strength);
    });
    const release = (p: Phaser.Input.Pointer) => {
      if (p.id !== this.joyPointerId) return;
      this.joyPointerId = null;
      this.vector.set(0, 0);
      this.base.setVisible(false);
      this.thumb.setVisible(false);
    };
    this.input.on('pointerup', release);
    this.input.on('pointerupoutside', release);

    this.layout();
    this.scale.on('resize', () => this.layout());
  }

  private layout(): void {
    const { width, height } = this.scale;
    this.actionBtn.setPosition(width - 60, height - 70);
  }

  /** WorldScene polls this once per frame and then clears it. */
  consumeAction(): boolean {
    const v = this.actionPressed;
    this.actionPressed = false;
    return v;
  }

  setControlsVisible(visible: boolean): void {
    this.actionBtn.setVisible(visible);
    if (!visible) {
      this.joyPointerId = null;
      this.vector.set(0, 0);
      this.base.setVisible(false);
      this.thumb.setVisible(false);
    }
  }
}
