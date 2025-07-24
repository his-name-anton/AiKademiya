import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { resolve } from 'path'

export default defineConfig(({ mode }) => ({
  plugins: [
    vue(),
  ],
  base: mode === 'development' ? '/' : '/static/frontend/',
  build: {
    outDir: resolve(__dirname, '../static/frontend'),
    emptyOutDir: true,
    manifest: true,
    rollupOptions: {
      input: resolve(__dirname, 'index.html'),
    },
  },
  resolve: {
    alias: {
      '@': resolve(__dirname, './src'),
    },
  },
  server: {
    host: true,
    port: 5173,
    proxy: {
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: true,
      },
    },
  },
  define: {
    __VUE_OPTIONS_API__: false,
    __VUE_PROD_DEVTOOLS__: false,
  },
}))