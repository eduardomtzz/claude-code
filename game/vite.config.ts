import { defineConfig } from 'vite';
import { VitePWA } from 'vite-plugin-pwa';

// `base: './'` makes the build work from any path (GitHub Pages subfolder, local file, etc.).
export default defineConfig({
  base: './',
  server: { port: 5173 },
  build: {
    target: 'es2020',
    sourcemap: false,
    chunkSizeWarningLimit: 1600,
  },
  plugins: [
    VitePWA({
      registerType: 'autoUpdate',
      includeAssets: ['icons/icon-192.png', 'icons/icon-512.png'],
      manifest: {
        name: 'AI Quest: RPG das Plataformas de IA',
        short_name: 'AI Quest',
        description: 'Aprenda OpenAI, Claude e Manus jogando um RPG 2D.',
        lang: 'pt-BR',
        start_url: './',
        display: 'fullscreen',
        orientation: 'any',
        background_color: '#0f1020',
        theme_color: '#0f1020',
        icons: [
          { src: 'icons/icon-192.png', sizes: '192x192', type: 'image/png' },
          { src: 'icons/icon-512.png', sizes: '512x512', type: 'image/png', purpose: 'any maskable' },
        ],
      },
      workbox: {
        globPatterns: ['**/*.{js,css,html,json,png,svg,woff2}'],
        maximumFileSizeToCacheInBytes: 4 * 1024 * 1024,
      },
    }),
  ],
});
