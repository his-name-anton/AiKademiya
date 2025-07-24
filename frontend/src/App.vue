<template>
  <div id="app" class="min-h-screen bg-gray-50 dark:bg-gray-900">
    <!-- Loading state -->
    <div v-if="isInitializing" class="min-h-screen flex items-center justify-center">
      <div class="animate-spin rounded-full h-32 w-32 border-b-2 border-blue-600"></div>
    </div>
    
    <!-- Main app content -->
    <router-view v-else />
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useAuthStore } from './stores/auth'

const authStore = useAuthStore()
const isInitializing = ref(true)

onMounted(async () => {
  try {
    await authStore.initializeAuth()
  } catch (error) {
    console.error('Failed to initialize auth:', error)
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

/* Dark mode scrollbar */
html.dark {
  color-scheme: dark;
}

/* Custom scrollbar */
::-webkit-scrollbar {
  width: 8px;
}

::-webkit-scrollbar-track {
  background: #f1f1f1;
}

::-webkit-scrollbar-thumb {
  background: #c1c1c1;
  border-radius: 4px;
}

::-webkit-scrollbar-thumb:hover {
  background: #a8a8a8;
}

.dark ::-webkit-scrollbar-track {
  background: #374151;
}

.dark ::-webkit-scrollbar-thumb {
  background: #6b7280;
}

.dark ::-webkit-scrollbar-thumb:hover {
  background: #9ca3af;
}
</style>