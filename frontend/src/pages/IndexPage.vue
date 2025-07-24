<template>
  <!-- Use AuthLayout for authenticated users -->
  <AuthLayout v-if="authStore.isAuthenticated">
    <div class="space-y-6">
      <div>
        <h1 class="text-2xl font-bold text-gray-900 dark:text-white">Добро пожаловать в AiKademiya</h1>
        <p class="mt-2 text-gray-600 dark:text-gray-400">
          Создавайте и изучайте курсы с помощью ИИ
        </p>
      </div>
      
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <div class="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
          <h3 class="text-lg font-semibold text-gray-900 dark:text-white mb-2">Быстрый старт</h3>
          <p class="text-gray-600 dark:text-gray-400 mb-4">Создайте свой первый курс за несколько минут</p>
          <router-link to="/generate" class="btn-primary inline-block">
            Создать курс
          </router-link>
        </div>
        
        <div class="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
          <h3 class="text-lg font-semibold text-gray-900 dark:text-white mb-2">Мои курсы</h3>
          <p class="text-gray-600 dark:text-gray-400 mb-4">Продолжите изучение ваших курсов</p>
          <router-link to="/learn" class="btn-primary inline-block">
            Перейти к обучению
          </router-link>
        </div>
        
        <div class="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
          <h3 class="text-lg font-semibold text-gray-900 dark:text-white mb-2">Профиль</h3>
          <p class="text-gray-600 dark:text-gray-400 mb-4">Управляйте настройками аккаунта</p>
          <router-link to="/profile" class="btn-primary inline-block">
            Открыть профиль
          </router-link>
        </div>
      </div>
    </div>
  </AuthLayout>
  
  <!-- Use public layout for guests -->
  <main v-else class="bg-gray-50 text-gray-900">
    <PublicHeader />
    <div class="container mx-auto px-4 max-w-7xl">
      <HeroSection />
      <HowItWorks />
      <Benefits />
    </div>
  </main>
</template>

<script setup>
import { useAuthStore } from '@/stores/auth'
import AuthLayout from '@/layouts/AuthLayout.vue'
import PublicHeader from '@/components/layout/PublicHeader.vue'
import HeroSection from '@/components/index/HeroSection.vue'
import HowItWorks from '@/components/index/HowItWorks.vue'
import Benefits from '@/components/index/Benefits.vue'

const authStore = useAuthStore()
</script> 