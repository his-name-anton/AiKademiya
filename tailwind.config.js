// tailwind.config.js
module.exports = {
  darkMode: 'class',
  content: [
    './templates/**/*.html',       // все шаблоны
    './aikademiya/**/*.py',        // если ты используешь классы в Python (напр. в render)
  ],
  theme: {
    extend: {
      colors: {
        primary: {
          50: '#eff6ff',
          100: '#dbeafe',
          200: '#bfdbfe',
          300: '#93c5fd',
          400: '#60a5fa',
          500: '#3b82f6',   // это будет bg-primary-500
          600: '#2563eb',   // bg-primary-600
          700: '#1d4ed8',
          800: '#1e40af',
          900: '#1e3a8a',
        }
      }
    }
  },
  plugins: []
};