<template>
  <div class="min-h-screen bg-gray-50 dark:bg-gray-900 flex flex-col justify-center py-12 sm:px-6 lg:px-8">
    <div class="sm:mx-auto sm:w-full sm:max-w-md">
      <!-- Logo -->
      <router-link to="/" class="flex justify-center">
        <div class="flex items-center space-x-2">
          <div class="w-10 h-10 bg-blue-600 rounded-lg flex items-center justify-center">
            <span class="text-white font-bold text-xl">AI</span>
          </div>
          <span class="text-2xl font-bold text-gray-900 dark:text-white">AiKademiya</span>
        </div>
      </router-link>
    </div>

    <div class="mt-8 sm:mx-auto sm:w-full sm:max-w-md">
      <div class="bg-white dark:bg-gray-800 py-8 px-4 shadow sm:rounded-lg sm:px-10">
        <router-view />
      </div>

      <!-- Back to home link -->
      <div class="mt-6 text-center">
        <router-link 
          to="/" 
          class="text-sm text-blue-600 hover:text-blue-500 dark:text-blue-400 dark:hover:text-blue-300 transition-colors"
        >
          ← Вернуться на главную
        </router-link>
      </div>
    </div>

    <!-- Theme toggle -->
    <div class="fixed bottom-4 right-4">
      <ThemeToggle />
    </div>
  </div>
</template>

<script setup lang="ts">
import ThemeToggle from '@/components/common/ThemeToggle.vue'
</script>