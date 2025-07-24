<template>
  <div class="space-y-6">
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
      <!-- Stats Cards -->
      <div class="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
        <div class="flex items-center">
          <div class="p-2 bg-blue-100 dark:bg-blue-900 rounded-lg">
            <AcademicCapIcon class="h-6 w-6 text-blue-600 dark:text-blue-400" />
          </div>
          <div class="ml-4">
            <p class="text-sm font-medium text-gray-600 dark:text-gray-400">Всего курсов</p>
            <p class="text-2xl font-semibold text-gray-900 dark:text-gray-100">12</p>
          </div>
        </div>
      </div>

      <div class="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
        <div class="flex items-center">
          <div class="p-2 bg-green-100 dark:bg-green-900 rounded-lg">
            <CheckCircleIcon class="h-6 w-6 text-green-600 dark:text-green-400" />
          </div>
          <div class="ml-4">
            <p class="text-sm font-medium text-gray-600 dark:text-gray-400">Завершено</p>
            <p class="text-2xl font-semibold text-gray-900 dark:text-gray-100">8</p>
          </div>
        </div>
      </div>

      <div class="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
        <div class="flex items-center">
          <div class="p-2 bg-yellow-100 dark:bg-yellow-900 rounded-lg">
            <ClockIcon class="h-6 w-6 text-yellow-600 dark:text-yellow-400" />
          </div>
          <div class="ml-4">
            <p class="text-sm font-medium text-gray-600 dark:text-gray-400">В процессе</p>
            <p class="text-2xl font-semibold text-gray-900 dark:text-gray-100">3</p>
          </div>
        </div>
      </div>

      <div class="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
        <div class="flex items-center">
          <div class="p-2 bg-purple-100 dark:bg-purple-900 rounded-lg">
            <StarIcon class="h-6 w-6 text-purple-600 dark:text-purple-400" />
          </div>
          <div class="ml-4">
            <p class="text-sm font-medium text-gray-600 dark:text-gray-400">Рейтинг</p>
            <p class="text-2xl font-semibold text-gray-900 dark:text-gray-100">4.8</p>
          </div>
        </div>
      </div>
    </div>

    <!-- Recent Activity -->
    <div class="bg-white dark:bg-gray-800 rounded-lg shadow">
      <div class="px-6 py-4 border-b border-gray-200 dark:border-gray-700">
        <h3 class="text-lg font-medium text-gray-900 dark:text-gray-100">Последняя активность</h3>
      </div>
      <div class="p-6">
        <div class="space-y-4">
          <div class="flex items-center space-x-4">
            <div class="w-2 h-2 bg-blue-600 rounded-full"></div>
            <div class="flex-1">
              <p class="text-sm text-gray-900 dark:text-gray-100">Завершен курс "Основы Python"</p>
              <p class="text-xs text-gray-500 dark:text-gray-400">2 часа назад</p>
            </div>
          </div>
          <div class="flex items-center space-x-4">
            <div class="w-2 h-2 bg-green-600 rounded-full"></div>
            <div class="flex-1">
              <p class="text-sm text-gray-900 dark:text-gray-100">Начат новый курс "Машинное обучение"</p>
              <p class="text-xs text-gray-500 dark:text-gray-400">1 день назад</p>
            </div>
          </div>
          <div class="flex items-center space-x-4">
            <div class="w-2 h-2 bg-yellow-600 rounded-full"></div>
            <div class="flex-1">
              <p class="text-sm text-gray-900 dark:text-gray-100">Обновлен профиль</p>
              <p class="text-xs text-gray-500 dark:text-gray-400">3 дня назад</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import {
  AcademicCapIcon,
  CheckCircleIcon,
  ClockIcon,
  StarIcon
} from '@heroicons/vue/24/outline'
</script> 