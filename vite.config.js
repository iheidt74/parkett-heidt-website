import { defineConfig } from 'vite';
import { resolve } from 'path';
import { readdirSync } from 'fs';

// Auto-discover all HTML files in leistungen/ directory
const leistungenPages = {};
try {
  const files = readdirSync(resolve(__dirname, 'leistungen'));
  files.filter(f => f.endsWith('.html')).forEach(f => {
    const name = f.replace('.html', '').replace(/-/g, '_');
    leistungenPages[`leistungen_${name}`] = resolve(__dirname, 'leistungen', f);
  });
} catch (e) { /* leistungen dir may not exist yet */ }

export default defineConfig({
  build: {
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'index.html'),
        leistungen: resolve(__dirname, 'leistungen.html'),
        ueberUns: resolve(__dirname, 'ueber-uns.html'),
        referenzen: resolve(__dirname, 'referenzen.html'),
        kontakt: resolve(__dirname, 'kontakt.html'),
        impressum: resolve(__dirname, 'impressum.html'),
        ...leistungenPages
      }
    }
  }
});
