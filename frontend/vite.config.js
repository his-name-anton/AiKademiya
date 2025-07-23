import {defineConfig} from 'vite'
import vue from '@vitejs/plugin-vue'
import {resolve} from 'path'

export default defineConfig(({mode}) => ({
    plugins: [vue()],
    base: mode === 'development' ? '/' : '/static/frontend/',
    build: {
        outDir: resolve(__dirname, '../static/frontend'),
        emptyOutDir: true,
        manifest: true
    },
    server: {
        host: true,
        port: 5173
    }
}))