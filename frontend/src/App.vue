<template>
  <div id="app" class="min-h-screen bg-gray-50 dark:bg-gray-900">
    <!-- Loading state -->
    <div v-if="isInitializing" class="min-h-screen flex items-center justify-center">
      <div class="animate-spin rounded-full h-32 w-32 border-b-2 border-blue-600"></div>
    </div>
    
    <!-- Main app content -->
    <template v-else>
      <!-- Use AuthLayout for authenticated pages -->
      <AuthLayout v-if="shouldUseAuthLayout">
        <router-view />
      </AuthLayout>
      
      <!-- Use default layout for public pages -->
      <router-view v-else />
    </template>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onBeforeMount } from 'vue'
import { useRoute } from 'vue-router'
import { useAuthStore } from './stores/auth'
import { useTheme } from './composables/useTheme'
import AuthLayout from './layouts/AuthLayout.vue'

const authStore = useAuthStore()
const route = useRoute()
const isInitializing = ref(true)
const { initializeTheme } = useTheme()

// Check if current route should use auth layout
const shouldUseAuthLayout = computed(() => {
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

// Initialize app before mounting
onBeforeMount(async () => {
  try {
    // Initialize theme first
    initializeTheme()
    
    // Auth is already initialized in main.ts, just wait for it
    // This prevents double initialization and race conditions
    let retries = 0;
    const maxRetries = 50; // 5 seconds max wait
    
    while (!authStore.isInitialized && retries < maxRetries) {
      await new Promise(resolve => setTimeout(resolve, 100));
      retries++;
    }
    
    if (!authStore.isInitialized) {
      console.warn('Auth initialization timed out, continuing...');
    } else {
      console.log('Auth initialization confirmed in App.vue');
    }
  } catch (error) {
    console.error('Failed to wait for auth initialization:', error)
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