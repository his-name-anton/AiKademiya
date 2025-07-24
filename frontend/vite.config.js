import {defineConfig} from 'vite'
import vue from '@vitejs/plugin-vue'
import {resolve} from 'path'
import tailwindcss from '@tailwindcss/vite'

export default defineConfig(({mode}) => ({
    plugins: [
        vue(),
        tailwindcss()
    ],
    base: '/',
    build: {
        outDir: resolve(__dirname, 'dist'),
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
        host: '0.0.0.0', // Важно для Docker
        port: 5173,
        watch: {
            usePolling: true, // Важно для Docker на некоторых системах
        },
        proxy: {
            '/api': {
                target: process.env.NODE_ENV === 'development' 
                    ? 'http://web:8000'  // Docker service name
                    : 'http://localhost:8000',
                changeOrigin: true,
            },
        },
    }
}))