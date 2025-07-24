<template>
  <div class="flex h-screen bg-gray-50 dark:bg-gray-900">
    <!-- Sidebar -->
    <div 
      class="fixed inset-y-0 left-0 z-50 w-64 bg-white dark:bg-gray-800 shadow-lg transform transition-transform duration-300 ease-in-out"
      :class="{ '-translate-x-full': !isOpen, 'translate-x-0': isOpen }"
    >
      <!-- Sidebar Header -->
      <div class="flex items-center justify-between h-16 px-4 border-b border-gray-200 dark:border-gray-700">
        <router-link to="/" class="flex items-center space-x-2">
          <div class="w-8 h-8 bg-blue-600 rounded-lg flex items-center justify-center">
            <span class="text-white font-bold text-sm">AI</span>
          </div>
          <span class="text-xl font-bold text-gray-900 dark:text-white">AiKademiya</span>
        </router-link>
        
        <!-- Close button for mobile -->
        <button
          @click="closeSidebar"
          class="lg:hidden p-2 rounded-md text-gray-400 hover:text-gray-500 hover:bg-gray-100 dark:hover:bg-gray-700"
        >
          <XMarkIcon class="h-6 w-6" />
        </button>
      </div>

      <!-- Search Bar -->
      <div class="p-4 border-b border-gray-200 dark:border-gray-700">
        <div class="relative">
          <MagnifyingGlassIcon class="absolute left-3 top-1/2 transform -translate-y-1/2 h-4 w-4 text-gray-400" />
          <input
            type="text"
            placeholder="Поиск курсов..."
            class="w-full pl-10 pr-4 py-2 border border-gray-300 dark:border-gray-600 rounded-lg bg-gray-50 dark:bg-gray-700 text-gray-900 dark:text-gray-100 placeholder-gray-500 dark:placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
          />
        </div>
      </div>

      <!-- Navigation Menu -->
      <nav class="flex-1 px-4 py-4 space-y-2">
        <!-- Main Navigation -->
        <div class="space-y-1">
          <router-link
            v-for="item in mainNavigation"
            :key="item.name"
            :to="item.href"
            class="flex items-center px-3 py-2 text-sm font-medium rounded-lg transition-colors"
            :class="[
              $route.path === item.href
                ? 'bg-blue-100 dark:bg-blue-900 text-blue-700 dark:text-blue-300'
                : 'text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700'
            ]"
          >
            <component :is="item.icon" class="h-5 w-5 mr-3" />
            {{ item.name }}
            <ChevronDownIcon v-if="item.hasDropdown" class="h-4 w-4 ml-auto" />
            <span v-if="item.badge" class="ml-auto bg-blue-600 text-white text-xs px-2 py-1 rounded-full">
              {{ item.badge }}
            </span>
          </router-link>
        </div>

        <!-- Secondary Navigation -->
        <div class="pt-4 border-t border-gray-200 dark:border-gray-700">
          <div class="space-y-1">
            <router-link
              v-for="item in secondaryNavigation"
              :key="item.name"
              :to="item.href"
              class="flex items-center px-3 py-2 text-sm font-medium rounded-lg transition-colors"
              :class="[
                $route.path === item.href
                  ? 'bg-blue-100 dark:bg-blue-900 text-blue-700 dark:text-blue-300'
                  : 'text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700'
              ]"
            >
              <component :is="item.icon" class="h-5 w-5 mr-3" />
              {{ item.name }}
            </router-link>
          </div>
        </div>
      </nav>

      <!-- User Profile Section -->
      <div class="p-4 border-t border-gray-200 dark:border-gray-700">
        <!-- User Header (Clickable) -->
        <button 
          @click="toggleUserMenu"
          class="flex items-center space-x-3 w-full text-left hover:bg-gray-50 dark:hover:bg-gray-700 rounded-lg p-2 transition-colors"
        >
          <img 
            :src="authStore.user?.avatar || defaultAvatar" 
            :alt="authStore.user?.username || 'User'"
            class="w-10 h-10 rounded-full"
          >
          <div class="flex-1 min-w-0">
            <p class="text-sm font-medium text-gray-900 dark:text-gray-100 truncate">
              {{ authStore.user?.username || authStore.user?.email }}
            </p>
            <p class="text-xs text-gray-500 dark:text-gray-400 truncate">
              {{ authStore.user?.email }}
            </p>
          </div>
          <ChevronDownIcon 
            class="h-4 w-4 text-gray-400 transition-transform duration-200"
            :class="{ 'rotate-180': isUserMenuOpen }"
          />
        </button>
        
        <!-- User Menu (Collapsible) -->
        <div 
          v-if="isUserMenuOpen"
          class="mt-3 space-y-1 animate-slide-down"
        >
          <router-link 
            to="/profile" 
            @click="closeUserMenu"
            class="flex items-center px-3 py-2 text-sm font-medium rounded-lg transition-colors text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700"
          >
            <UserIcon class="h-4 w-4 mr-3" />
            Профиль
          </router-link>
          <router-link 
            to="/settings" 
            @click="closeUserMenu"
            class="flex items-center px-3 py-2 text-sm font-medium rounded-lg transition-colors text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700"
          >
            <Cog6ToothIcon class="h-4 w-4 mr-3" />
            Настройки
          </router-link>
          <hr class="my-2 border-gray-200 dark:border-gray-600">
          <button 
            @click="logout"
            class="flex items-center w-full px-3 py-2 text-sm font-medium rounded-lg transition-colors text-red-600 dark:text-red-400 hover:bg-red-50 dark:hover:bg-red-900/20"
          >
            <ArrowRightOnRectangleIcon class="h-4 w-4 mr-3" />
            Выйти
          </button>
        </div>
      </div>

      <!-- Storage Usage -->
      <div class="p-4 border-t border-gray-200 dark:border-gray-700">
        <div class="mb-2">
          <p class="text-sm text-gray-600 dark:text-gray-400">Использовано места</p>
          <p class="text-sm font-medium text-gray-900 dark:text-gray-100">70 из 150 ГБ</p>
        </div>
        <div class="w-full bg-gray-200 dark:bg-gray-700 rounded-full h-2">
          <div class="bg-green-500 h-2 rounded-full" style="width: 47%"></div>
        </div>
        <button class="w-full mt-3 flex items-center justify-center px-3 py-2 text-sm font-medium text-blue-600 dark:text-blue-400 hover:bg-blue-50 dark:hover:bg-blue-900/20 rounded-lg transition-colors">
          <ArrowUpIcon class="h-4 w-4 mr-2" />
          Улучшить до Pro
        </button>
      </div>

      <!-- Theme Toggle -->
      <div class="p-4 border-t border-gray-200 dark:border-gray-700">
        <div class="flex items-center justify-between">
          <span class="text-sm font-medium text-gray-700 dark:text-gray-300">Тема</span>
          <ThemeToggle />
        </div>
      </div>
    </div>

    <!-- Overlay for mobile -->
    <div
      v-if="isOpen"
      @click="closeSidebar"
      class="fixed inset-0 z-40 bg-black bg-opacity-50 lg:hidden"
    ></div>

    <!-- Main Content -->
    <div class="flex-1 lg:ml-64">
      <!-- Page Content -->
      <main class="p-6">
        <slot />
      </main>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted, watch } from 'vue'
import { useRoute } from 'vue-router'
import {
  XMarkIcon,
  MagnifyingGlassIcon,
  ChevronDownIcon,
  ArrowUpIcon,
  ArrowRightOnRectangleIcon,
  HomeIcon,
  DocumentTextIcon,
  ChatBubbleLeftRightIcon,
  LockClosedIcon,
  BookOpenIcon,
  GlobeAltIcon,
  PlusIcon,
  AcademicCapIcon,
  Cog6ToothIcon,
  UserIcon
} from '@heroicons/vue/24/outline'
import ThemeToggle from '@/components/common/ThemeToggle.vue'
import { useAuthStore } from '@/stores/auth'
import { useRouter } from 'vue-router'
import { useToast } from 'vue-toastification'

const route = useRoute()
const router = useRouter()
const toast = useToast()
const authStore = useAuthStore()
const isOpen = ref(false)
const isUserMenuOpen = ref(false)

const defaultAvatar = 'data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzIiIGhlaWdodD0iMzIiIHZpZXdCb3g9IjAgMCAzMiAzMiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHJlY3Qgd2lkdGg9IjMyIiBoZWlnaHQ9IjMyIiBmaWxsPSIjRjNGNEY2Ii8+CjxwYXRoIGQ9Ik0xNiAxNkMxMS40NSAxNiA4LjQgMTIuODggOC40IDhDOC40IDMuMTIgMTEuNDUgMCAxNiAwQzIwLjU1IDAgMjMuNiAzLjEyIDIzLjYgOEMyMy42IDEyLjg4IDIwLjU1IDE2IDE2IDE2Wk0yMy42IDE5LjJDMjUuNDQgMTkuMiAyNi44OCAyMC42NCAyNi44OCAyMi40VjI4LjhDMjAuNDggMzAuMDggMTEuNTIgMzAuMDggNS4xMiAyOC44VjIyLjRDNS4xMiAyMC42NCA2LjU2IDE5LjIgOC4zMiAxOS4ySDIzLjZaIiBmaWxsPSIjOUNBNEFGIi8+Cjwvc3ZnPgo='



// Navigation items
const mainNavigation = [
  {
    name: 'Обзор',
    href: '/dashboard',
    icon: HomeIcon
  },
  {
    name: 'Создать курс',
    href: '/generate',
    icon: PlusIcon
  },
  {
    name: 'Мои курсы',
    href: '/learn',
    icon: AcademicCapIcon
  },
  {
    name: 'Каталог',
    href: '/catalog',
    icon: DocumentTextIcon,
    hasDropdown: true
  },
  {
    name: 'Сообщения',
    href: '/messages',
    icon: ChatBubbleLeftRightIcon,
    badge: '3'
  },
  {
    name: 'Безопасность',
    href: '/security',
    icon: LockClosedIcon,
    hasDropdown: true
  }
]

const secondaryNavigation = [
  {
    name: 'Документация',
    href: '/docs',
    icon: BookOpenIcon
  },
  {
    name: 'Помощь',
    href: '/help',
    icon: GlobeAltIcon
  }
]

// Sidebar controls
const openSidebar = () => {
  isOpen.value = true
}

const closeSidebar = () => {
  isOpen.value = false
}

const logout = async () => {
  try {
    await authStore.logout()
    toast.success('Вы успешно вышли из системы')
    router.push('/')
  } catch (error) {
    toast.error('Ошибка при выходе из системы')
  }
}

const toggleUserMenu = () => {
  isUserMenuOpen.value = !isUserMenuOpen.value
}

const closeUserMenu = () => {
  isUserMenuOpen.value = false
}

// Close sidebar on route change
const handleRouteChange = () => {
  if (window.innerWidth < 1024) {
    closeSidebar()
  }
}

// Handle window resize
const handleResize = () => {
  if (window.innerWidth >= 1024) {
    isOpen.value = true
  } else {
    isOpen.value = false
  }
}

onMounted(() => {
  // Set initial state based on screen size
  handleResize()
  
  // Add event listeners
  window.addEventListener('resize', handleResize)
})

onUnmounted(() => {
  window.removeEventListener('resize', handleResize)
})

// Watch for route changes
watch(() => route.path, handleRouteChange)
</script> 