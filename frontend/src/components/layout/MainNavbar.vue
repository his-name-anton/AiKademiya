<template>
  <fwb-navbar>
    <template #logo>
      <fwb-navbar-logo
          alt="AiKademiya Logo" image-url="/static/images/logo.svg" link="/">
        AiKademiya
      </fwb-navbar-logo>
    </template>

    <template #default="{ isShowMenu }">
      <fwb-navbar-collapse :is-show-menu="isShowMenu">
        <fwb-navbar-link link="/">Главная</fwb-navbar-link>
        
        <!-- Authenticated user links -->
        <template v-if="authStore.isAuthenticated">
          <fwb-navbar-link link="/generate">Создать курс</fwb-navbar-link>
          <fwb-navbar-link link="/learn">Обучение</fwb-navbar-link>
        </template>
        
        <!-- Public links -->
        <fwb-navbar-link link="/about">О нас</fwb-navbar-link>
        <fwb-navbar-link link="/pricing">Тарифы</fwb-navbar-link>
        <fwb-navbar-link link="/contacts">Контакты</fwb-navbar-link>
      </fwb-navbar-collapse>
    </template>

    <template #right-side>
      <!-- Authenticated user menu -->
      <div v-if="authStore.isAuthenticated" class="flex items-center space-x-4">
        <!-- User dropdown -->
        <div class="relative" ref="dropdownRef">
          <button 
            @click="showDropdown = !showDropdown"
            class="flex items-center space-x-2 text-sm font-medium text-gray-700 hover:text-gray-900 dark:text-gray-300 dark:hover:text-white focus:outline-none"
          >
            <img 
              :src="authStore.user?.avatar || defaultAvatar" 
              :alt="authStore.user?.username || 'User'"
              class="w-8 h-8 rounded-full"
            >
            <span>{{ authStore.user?.username || authStore.user?.email }}</span>
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
            </svg>
          </button>
          
          <!-- Dropdown menu -->
          <div 
            v-if="showDropdown"
            class="absolute right-0 mt-2 w-48 bg-white rounded-md shadow-lg py-1 z-50 dark:bg-gray-800"
          >
            <router-link 
              to="/profile" 
              @click="showDropdown = false"
              class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-300 dark:hover:bg-gray-700"
            >
              Профиль
            </router-link>
            <router-link 
              to="/settings" 
              @click="showDropdown = false"
              class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-300 dark:hover:bg-gray-700"
            >
              Настройки
            </router-link>
            <hr class="my-1 border-gray-200 dark:border-gray-600">
            <button 
              @click="logout"
              class="block w-full text-left px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-300 dark:hover:bg-gray-700"
            >
              Выйти
            </button>
          </div>
        </div>
      </div>
      
      <!-- Guest user buttons -->
      <div v-else class="flex items-center space-x-2">
        <fwb-button tag="router-link" to="/login" variant="outline">
          Войти
        </fwb-button>
        <fwb-button tag="router-link" to="/register">
          Регистрация
        </fwb-button>
      </div>
    </template>
  </fwb-navbar>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import { useToast } from 'vue-toastification'
import {
  FwbButton,
  FwbNavbar,
  FwbNavbarCollapse,
  FwbNavbarLink,
  FwbNavbarLogo,
} from 'flowbite-vue'

const authStore = useAuthStore()
const router = useRouter()
const toast = useToast()

const showDropdown = ref(false)
const dropdownRef = ref<HTMLElement>()

const defaultAvatar = 'data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzIiIGhlaWdodD0iMzIiIHZpZXdCb3g9IjAgMCAzMiAzMiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHJlY3Qgd2lkdGg9IjMyIiBoZWlnaHQ9IjMyIiBmaWxsPSIjRjNGNEY2Ii8+CjxwYXRoIGQ9Ik0xNiAxNkMxMS40NSAxNiA4LjQgMTIuODggOC40IDhDOC40IDMuMTIgMTEuNDUgMCAxNiAwQzIwLjU1IDAgMjMuNiAzLjEyIDIzLjYgOEMyMy42IDEyLjg4IDIwLjU1IDE2IDE2IDE2Wk0yMy42IDE5LjJDMjUuNDQgMTkuMiAyNi44OCAyMC42NCAyNi44OCAyMi40VjI4LjhDMjAuNDggMzAuMDggMTEuNTIgMzAuMDggNS4xMiAyOC44VjIyLjRDNS4xMiAyMC42NCA2LjU2IDE5LjIgOC4zMiAxOS4ySDIzLjZaIiBmaWxsPSIjOUNBNEFGIi8+Cjwvc3ZnPgo='

const logout = async () => {
  try {
    await authStore.logout()
    toast.success('Вы успешно вышли из системы')
    router.push('/')
  } catch (error) {
    toast.error('Ошибка при выходе из системы')
  }
  showDropdown.value = false
}

// Close dropdown when clicking outside
const handleClickOutside = (event: Event) => {
  if (dropdownRef.value && !dropdownRef.value.contains(event.target as Node)) {
    showDropdown.value = false
  }
}

onMounted(() => {
  document.addEventListener('click', handleClickOutside)
})

onUnmounted(() => {
  document.removeEventListener('click', handleClickOutside)
})
</script>