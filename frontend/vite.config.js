import {defineConfig} from 'vite'
import vue from '@vitejs/plugin-vue'
import {resolve} from 'path'
import tailwindcss from '@tailwindcss/vite'

export default defineConfig(({mode}) => ({
    plugins: [
        vue(),
        tailwindcss()
    ],
    base: mode === 'development' ? '/' : '/static/frontend/',
    build: {
        outDir: resolve(__dirname, '../static/frontend'),
        emptyOutDir: true,
        manifest: true
    },
    resolve: {
        alias: {
            '@': resolve(__dirname, './'), // 👈 указывает, что @ = ./frontend
        },
    },
    server: {
        host: true,
        port: 5173,
    }
}))