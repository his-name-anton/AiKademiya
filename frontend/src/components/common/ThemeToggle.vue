<template>
  <button
    type="button"
    class="bg-white dark:bg-gray-800 p-2 rounded-full text-gray-400 hover:text-gray-500 dark:text-gray-300 dark:hover:text-gray-200 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 transition-colors"
    @click="toggleTheme"
  >
    <span class="sr-only">Переключить тему</span>
    
    <!-- Sun icon (light mode) -->
    <SunIcon 
      v-if="isDark" 
      class="h-5 w-5" 
    />
    
    <!-- Moon icon (dark mode) -->
    <MoonIcon 
      v-else 
      class="h-5 w-5" 
    />
  </button>
</template>

<script setup lang="ts">
import { SunIcon, MoonIcon } from '@heroicons/vue/24/outline'
import { useTheme } from '@/composables/useTheme'

const { isDark, toggleTheme } = useTheme()
</script>