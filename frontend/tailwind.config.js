// frontend/tailwind.config.js
import flowbitePlugin from 'flowbite/plugin'

export default {
    darkMode: 'class', // Включаем dark mode через CSS класс
    content: [
        './index.html',
        './src/**/*.{vue,js,ts}', // Исправляем путь к файлам
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
