<template>
  <header class="bg-white dark:bg-gray-900 shadow-sm">
    <nav class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex justify-between items-center h-16">
        <!-- Logo -->
        <router-link to="/" class="flex items-center space-x-2">
          <div class="w-8 h-8 bg-blue-600 rounded-lg flex items-center justify-center">
            <span class="text-white font-bold text-sm">AI</span>
          </div>
          <span class="text-xl font-bold text-gray-900 dark:text-white">AiKademiya</span>
        </router-link>

        <!-- Desktop Navigation -->
        <div class="hidden md:flex items-center space-x-8">
          <router-link 
            v-for="item in navigation" 
            :key="item.name"
            :to="item.href" 
            class="nav-link"
            :class="{ 'active': $route.path === item.href }"
          >
            {{ item.name }}
          </router-link>

          <div class="flex items-center space-x-4">
            <ThemeToggle />
            
            <!-- Auth buttons -->
            <div v-if="!isAuthenticated" class="flex items-center space-x-3">
              <router-link 
                to="/login" 
                class="text-gray-600 dark:text-gray-400 hover:text-gray-900 dark:hover:text-gray-100 px-3 py-2 text-sm font-medium transition-colors"
              >
                Вход
              </router-link>
              <router-link 
                to="/register" 
                class="btn-primary text-sm"
              >
                Регистрация
              </router-link>
            </div>

            <!-- User menu -->
            <div v-else class="flex items-center space-x-3">
              <router-link 
                to="/generate" 
                class="btn-primary text-sm"
              >
                Создать курс
              </router-link>
              <UserDropdown />
            </div>
          </div>
        </div>

        <!-- Mobile menu button -->
        <div class="md:hidden flex items-center space-x-2">
          <ThemeToggle />
          <button
            type="button"
            class="inline-flex items-center justify-center p-2 rounded-md text-gray-400 hover:text-gray-500 hover:bg-gray-100 dark:hover:bg-gray-800 focus:outline-none focus:ring-2 focus:ring-inset focus:ring-blue-500"
            @click="mobileMenuOpen = !mobileMenuOpen"
          >
            <span class="sr-only">Открыть меню</span>
            <Bars3Icon v-if="!mobileMenuOpen" class="h-6 w-6" />
            <XMarkIcon v-else class="h-6 w-6" />
          </button>
        </div>
      </div>

      <!-- Mobile Navigation -->
      <Transition name="slide-down">
        <div v-if="mobileMenuOpen" class="md:hidden">
          <div class="px-2 pt-2 pb-3 space-y-1 sm:px-3 border-t border-gray-200 dark:border-gray-700">
            <router-link 
              v-for="item in navigation" 
              :key="item.name"
              :to="item.href" 
              class="block px-3 py-2 rounded-md text-base font-medium text-gray-700 dark:text-gray-300 hover:text-gray-900 dark:hover:text-white hover:bg-gray-50 dark:hover:bg-gray-800 transition-colors"
              @click="mobileMenuOpen = false"
            >
              {{ item.name }}
            </router-link>

            <div class="border-t border-gray-200 dark:border-gray-700 pt-4 pb-3">
              <div v-if="!isAuthenticated" class="space-y-2">
                <router-link 
                  to="/login"
                  class="block w-full text-left px-3 py-2 rounded-md text-base font-medium text-gray-700 dark:text-gray-300 hover:text-gray-900 dark:hover:text-white hover:bg-gray-50 dark:hover:bg-gray-800 transition-colors"
                  @click="mobileMenuOpen = false"
                >
                  Вход
                </router-link>
                <router-link 
                  to="/register"
                  class="block w-full text-center btn-primary"
                  @click="mobileMenuOpen = false"
                >
                  Регистрация
                </router-link>
              </div>
              <div v-else class="space-y-2">
                <router-link 
                  to="/generate"
                  class="block w-full text-center btn-primary"
                  @click="mobileMenuOpen = false"
                >
                  Создать курс
                </router-link>
              </div>
            </div>
          </div>
        </div>
      </Transition>
    </nav>
  </header>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import { Bars3Icon, XMarkIcon } from '@heroicons/vue/24/outline'
import { useAuthStore } from '@/stores/auth'
import ThemeToggle from '@/components/common/ThemeToggle.vue'
import UserDropdown from '@/components/layout/UserDropdown.vue'

const authStore = useAuthStore()
const isAuthenticated = computed(() => authStore.isAuthenticated)
const mobileMenuOpen = ref(false)

const navigation = [
  { name: 'Главная', href: '/' },
  { name: 'О нас', href: '/about' },
  { name: 'Каталог', href: '/catalog' },
  { name: 'Тарифы', href: '/pricing' },
]
</script>