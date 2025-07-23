// frontend/tailwind.config.js
import flowbitePlugin from 'flowbite/plugin'

export default {
  content: [
    "./index.html",
    "./components/**/*.{vue,js,ts}",
    "./src/**/*.{vue,js,ts}",
    "./node_modules/flowbite/**/*.js"
  ],
  theme: {
    extend: {},
  },
  plugins: [
    flowbitePlugin,
    require('@tailwindcss/forms')
  ],
}
