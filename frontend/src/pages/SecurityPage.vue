<template>
  <div class="space-y-6">
    <h1 class="text-2xl font-bold text-gray-900 dark:text-gray-100">Безопасность</h1>
    
    <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
      <!-- Password Section -->
      <div class="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
        <h3 class="text-lg font-medium text-gray-900 dark:text-gray-100 mb-4">Смена пароля</h3>
        <form class="space-y-4">
          <div>
            <label class="form-label">Текущий пароль</label>
            <input type="password" class="form-input" />
          </div>
          <div>
            <label class="form-label">Новый пароль</label>
            <input type="password" class="form-input" />
          </div>
          <div>
            <label class="form-label">Подтвердите новый пароль</label>
            <input type="password" class="form-input" />
          </div>
          <button type="submit" class="btn-primary">Изменить пароль</button>
        </form>
      </div>

      <!-- Two-Factor Authentication -->
      <div class="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
        <h3 class="text-lg font-medium text-gray-900 dark:text-gray-100 mb-4">Двухфакторная аутентификация</h3>
        <div class="space-y-4">
          <div class="flex items-center justify-between">
            <div>
              <p class="text-sm font-medium text-gray-900 dark:text-gray-100">SMS аутентификация</p>
              <p class="text-sm text-gray-600 dark:text-gray-400">Получайте код подтверждения по SMS</p>
            </div>
            <button class="btn-outline text-sm">Включить</button>
          </div>
          <div class="flex items-center justify-between">
            <div>
              <p class="text-sm font-medium text-gray-900 dark:text-gray-100">Приложение аутентификации</p>
              <p class="text-sm text-gray-600 dark:text-gray-400">Используйте Google Authenticator</p>
            </div>
            <button class="btn-outline text-sm">Включить</button>
          </div>
        </div>
      </div>

      <!-- Login History -->
      <div class="bg-white dark:bg-gray-800 rounded-lg shadow p-6 lg:col-span-2">
        <h3 class="text-lg font-medium text-gray-900 dark:text-gray-100 mb-4">История входов</h3>
        <div class="space-y-3">
          <div v-for="login in loginHistory" :key="login.id" class="flex items-center justify-between p-3 border border-gray-200 dark:border-gray-700 rounded-lg">
            <div class="flex items-center space-x-3">
              <div class="w-8 h-8 bg-green-100 dark:bg-green-900 rounded-full flex items-center justify-center">
                <CheckIcon class="h-4 w-4 text-green-600 dark:text-green-400" />
              </div>
              <div>
                <p class="text-sm font-medium text-gray-900 dark:text-gray-100">{{ login.location }}</p>
                <p class="text-xs text-gray-500 dark:text-gray-400">{{ login.device }}</p>
              </div>
            </div>
            <span class="text-sm text-gray-500 dark:text-gray-400">{{ login.time }}</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { CheckIcon } from '@heroicons/vue/24/outline'

const loginHistory = [
  {
    id: 1,
    location: 'Москва, Россия',
    device: 'Chrome на Windows',
    time: '2 часа назад'
  },
  {
    id: 2,
    location: 'Москва, Россия',
    device: 'Safari на iPhone',
    time: '1 день назад'
  },
  {
    id: 3,
    location: 'Санкт-Петербург, Россия',
    device: 'Firefox на Mac',
    time: '3 дня назад'
  }
]
</script> 