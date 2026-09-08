// Generates simple PNG app icons without any dependency (pure zlib PNG encoder).
import { deflateSync } from 'node:zlib';
import { writeFileSync, mkdirSync } from 'node:fs';

function crc32(buf) {
  let c, crc = 0xffffffff;
  for (let n = 0; n < buf.length; n++) {
    c = (crc ^ buf[n]) & 0xff;
    for (let k = 0; k < 8; k++) c = c & 1 ? 0xedb88320 ^ (c >>> 1) : c >>> 1;
    crc = (crc >>> 8) ^ c;
  }
  return (crc ^ 0xffffffff) >>> 0;
}
function chunk(type, data) {
  const len = Buffer.alloc(4); len.writeUInt32BE(data.length);
  const td = Buffer.concat([Buffer.from(type), data]);
  const crc = Buffer.alloc(4); crc.writeUInt32BE(crc32(td));
  return Buffer.concat([len, td, crc]);
}
function png(size, pixel) {
  const raw = Buffer.alloc((size * 4 + 1) * size);
  for (let y = 0; y < size; y++) {
    raw[y * (size * 4 + 1)] = 0;
    for (let x = 0; x < size; x++) {
      const [r, g, b] = pixel(x / size, y / size);
      const o = y * (size * 4 + 1) + 1 + x * 4;
      raw[o] = r; raw[o + 1] = g; raw[o + 2] = b; raw[o + 3] = 255;
    }
  }
  const ihdr = Buffer.alloc(13);
  ihdr.writeUInt32BE(size, 0); ihdr.writeUInt32BE(size, 4);
  ihdr[8] = 8; ihdr[9] = 6; ihdr[10] = 0; ihdr[11] = 0; ihdr[12] = 0;
  return Buffer.concat([
    Buffer.from([0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a]),
    chunk('IHDR', ihdr), chunk('IDAT', deflateSync(raw)), chunk('IEND', Buffer.alloc(0)),
  ]);
}
// Icon: dark background, three colored "kingdom" blocks and a purple sword-ish diagonal.
const pixel = (u, v) => {
  const bg = [15, 16, 32];
  const inCircle = (cx, cy, r) => (u - cx) ** 2 + (v - cy) ** 2 < r * r;
  if (inCircle(0.32, 0.36, 0.16)) return [16, 163, 127];
  if (inCircle(0.68, 0.36, 0.16)) return [217, 119, 87];
  if (inCircle(0.5, 0.68, 0.16)) return [79, 124, 255];
  if (Math.abs(u - v) < 0.035 && u > 0.2 && u < 0.8) return [139, 92, 246];
  return bg;
};
mkdirSync('public/icons', { recursive: true });
for (const s of [192, 512]) writeFileSync(`public/icons/icon-${s}.png`, png(s, pixel));
console.log('icons written');
