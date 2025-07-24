<template>
  <div id="app" class="min-h-screen bg-gray-50 dark:bg-gray-900 transition-colors duration-200">
    <!-- Loading overlay -->
    <div v-if="isInitializing" class="fixed inset-0 bg-white dark:bg-gray-900 flex items-center justify-center z-50">
      <div class="flex flex-col items-center space-y-4">
        <div class="w-16 h-16 border-4 border-blue-200 border-t-blue-600 rounded-full animate-spin"></div>
        <p class="text-gray-600 dark:text-gray-400">Загрузка...</p>
      </div>
    </div>

    <!-- Main app content -->
    <router-view v-else />
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useAuth } from '@/composables/useAuth'
import { useTheme } from '@/composables/useTheme'

const { initializeAuth } = useAuth()
const { initializeTheme } = useTheme()

const isInitializing = ref(true)

onMounted(async () => {
  try {
    // Initialize theme
    initializeTheme()
    
    // Initialize authentication state
    await initializeAuth()
  } catch (error) {
    console.error('Failed to initialize app:', error)
  } finally {
    isInitializing.value = false
  }
})
</script>

<style>
/* Add any global styles here */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.2s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

.slide-enter-active,
.slide-leave-active {
  transition: transform 0.3s ease;
}

.slide-enter-from {
  transform: translateX(-100%);
}

.slide-leave-to {
  transform: translateX(100%);
}
</style>