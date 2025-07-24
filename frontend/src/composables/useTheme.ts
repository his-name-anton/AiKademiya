import { ref, computed, watch } from 'vue'
import type { Theme } from '@/types'

const theme = ref<Theme>('system')
const systemTheme = ref<'light' | 'dark'>('light')

export function useTheme() {
  // Computed properties
  const isDark = computed(() => {
    if (theme.value === 'system') {
      return systemTheme.value === 'dark'
    }
    return theme.value === 'dark'
  })

  const currentTheme = computed(() => theme.value)

  // Initialize theme
  function initializeTheme() {
    // Get saved theme from localStorage
    const savedTheme = localStorage.getItem('theme') as Theme | null
    if (savedTheme && ['light', 'dark', 'system'].includes(savedTheme)) {
      theme.value = savedTheme
    }

    // Detect system theme
    updateSystemTheme()
    
    // Listen for system theme changes
    const mediaQuery = window.matchMedia('(prefers-color-scheme: dark)')
    mediaQuery.addEventListener('change', updateSystemTheme)

    // Apply initial theme
    applyTheme()
  }

  // Update system theme
  function updateSystemTheme() {
    systemTheme.value = window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'
  }

  // Apply theme to document
  function applyTheme() {
    const htmlElement = document.documentElement
    
    if (isDark.value) {
      htmlElement.classList.add('dark')
    } else {
      htmlElement.classList.remove('dark')
    }
  }

  // Set theme
  function setTheme(newTheme: Theme) {
    theme.value = newTheme
    localStorage.setItem('theme', newTheme)
    applyTheme()
  }

  // Toggle between light and dark (skip system)
  function toggleTheme() {
    if (theme.value === 'light') {
      setTheme('dark')
    } else {
      setTheme('light')
    }
  }

  // Watch for theme changes
  watch([theme, systemTheme], () => {
    applyTheme()
  })

  return {
    // State
    theme: currentTheme,
    isDark,
    
    // Actions
    setTheme,
    toggleTheme,
    initializeTheme,
  }
}