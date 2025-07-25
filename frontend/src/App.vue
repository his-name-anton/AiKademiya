<template>
  <div id="app" class="min-h-screen bg-gray-50 dark:bg-gray-900">
    <!-- Loading state while auth store is initializing -->
    <div v-if="!authStore.isInitialized" class="min-h-screen flex items-center justify-center">
      <div class="text-center">
        <div class="inline-block h-8 w-8 animate-spin rounded-full border-4 border-solid border-current border-r-transparent align-[-0.125em] motion-reduce:animate-[spin_1.5s_linear_infinite]" role="status">
          <span class="!absolute !-m-px !h-px !w-px !overflow-hidden !whitespace-nowrap !border-0 !p-0 ![clip:rect(0,0,0,0)]">Loading...</span>
        </div>
        <p class="mt-4 text-gray-600 dark:text-gray-400">Инициализация...</p>
      </div>
    </div>
    
    <!-- Use AuthLayout for authenticated pages -->
    <AuthLayout v-else-if="shouldUseAuthLayout">
      <router-view />
    </AuthLayout>
    
    <!-- Use default layout for public pages -->
    <router-view v-else />
  </div>
</template>

<script setup lang="ts">
import { computed, onBeforeMount } from 'vue'
import { useRoute } from 'vue-router'
import { useAuthStore } from './stores/auth'
import { useTheme } from './composables/useTheme'
import AuthLayout from './layouts/AuthLayout.vue'

const authStore = useAuthStore()
const route = useRoute()
const { initializeTheme } = useTheme()

// Check if current route should use auth layout
const shouldUseAuthLayout = computed(() => {
  // Don't show auth layout until auth store is initialized
  if (!authStore.isInitialized) {
    return false
  }
  
  // For routes with explicit auth layout requirement
  if (route.meta.layout === 'auth' && authStore.isAuthenticated) {
    return true
  }
  
  // For home page, use auth layout if user is authenticated
  if (route.path === '/' && authStore.isAuthenticated) {
    return true
  }
  
  return false
})

// Initialize theme on mount
onBeforeMount(() => {
  initializeTheme()
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