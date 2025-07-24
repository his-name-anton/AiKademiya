<template>
  <div class="h-screen flex overflow-hidden bg-gray-100 dark:bg-gray-900">
    <!-- Mobile sidebar overlay -->
    <Transition name="fade">
      <div
        v-if="sidebarOpen"
        class="fixed inset-0 flex z-40 md:hidden"
        @click="sidebarOpen = false"
      >
        <div class="fixed inset-0 bg-gray-600 bg-opacity-75" />
      </div>
    </Transition>

    <!-- Mobile sidebar -->
    <Transition name="slide">
      <div
        v-if="sidebarOpen"
        class="relative flex-1 flex flex-col max-w-xs w-full bg-white dark:bg-gray-800 md:hidden"
      >
        <div class="absolute top-0 right-0 -mr-12 pt-2">
          <button
            type="button"
            class="ml-1 flex items-center justify-center h-10 w-10 rounded-full focus:outline-none focus:ring-2 focus:ring-inset focus:ring-white"
            @click="sidebarOpen = false"
          >
            <span class="sr-only">Закрыть сайдбар</span>
            <XMarkIcon class="h-6 w-6 text-white" />
          </button>
        </div>
        <AppSidebar />
      </div>
    </Transition>

    <!-- Desktop sidebar -->
    <div class="hidden md:flex md:flex-shrink-0">
      <div class="flex flex-col w-64">
        <AppSidebar />
      </div>
    </div>

    <!-- Main content -->
    <div class="flex flex-col w-0 flex-1 overflow-hidden">
      <!-- Top navigation -->
      <div class="relative z-10 flex-shrink-0 flex h-16 bg-white dark:bg-gray-800 shadow">
        <!-- Mobile menu button -->
        <button
          type="button"
          class="px-4 border-r border-gray-200 dark:border-gray-700 text-gray-500 dark:text-gray-400 focus:outline-none focus:ring-2 focus:ring-inset focus:ring-blue-500 md:hidden"
          @click="sidebarOpen = true"
        >
          <span class="sr-only">Открыть сайдбар</span>
          <Bars3Icon class="h-6 w-6" />
        </button>

        <!-- Top navigation content -->
        <div class="flex-1 px-4 flex justify-between">
          <div class="flex-1 flex">
            <!-- Search -->
            <div class="w-full flex md:ml-0">
              <div class="relative w-full text-gray-400 focus-within:text-gray-600">
                <div class="absolute inset-y-0 left-0 flex items-center pointer-events-none">
                  <MagnifyingGlassIcon class="h-5 w-5" />
                </div>
                <input
                  id="search-field"
                  class="block w-full h-full pl-8 pr-3 py-2 border-transparent text-gray-900 dark:text-gray-100 placeholder-gray-500 dark:placeholder-gray-400 focus:outline-none focus:placeholder-gray-400 focus:ring-0 focus:border-transparent bg-transparent"
                  placeholder="Поиск..."
                  type="search"
                  name="search"
                />
              </div>
            </div>
          </div>

          <!-- Right side -->
          <div class="ml-4 flex items-center md:ml-6 space-x-4">
            <!-- Notifications -->
            <button
              type="button"
              class="bg-white dark:bg-gray-800 p-1 rounded-full text-gray-400 hover:text-gray-500 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
            >
              <span class="sr-only">Уведомления</span>
              <BellIcon class="h-6 w-6" />
            </button>

            <!-- Theme toggle -->
            <ThemeToggle />

            <!-- Profile dropdown -->
            <UserDropdown />
          </div>
        </div>
      </div>

      <!-- Main content area -->
      <main class="flex-1 relative overflow-y-auto focus:outline-none">
        <div class="py-6">
          <div class="max-w-7xl mx-auto px-4 sm:px-6 md:px-8">
            <router-view />
          </div>
        </div>
      </main>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import {
  Bars3Icon,
  XMarkIcon,
  MagnifyingGlassIcon,
  BellIcon,
} from '@heroicons/vue/24/outline'

import AppSidebar from '@/components/layout/AppSidebar.vue'
import UserDropdown from '@/components/layout/UserDropdown.vue'
import ThemeToggle from '@/components/common/ThemeToggle.vue'

const sidebarOpen = ref(false)
</script>