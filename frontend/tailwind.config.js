// frontend/tailwind.config.js
import flowbitePlugin from 'flowbite/plugin'

export default {
    content: [
        './index.html',
        './components/**/*.{vue,js}',
        './pages/**/*.{vue,js}',
        './router/**/*.{js,ts}',
        './App.vue',
        './node_modules/flowbite/**/*.js'
    ],
    theme: {
        extend: {},
    },
    plugins: [
        flowbitePlugin,
        require('@tailwindcss/forms')
    ],
}
