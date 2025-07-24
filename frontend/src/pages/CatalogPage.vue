<template>
  <div class="space-y-6">
    <div class="flex justify-between items-center">
      <h1 class="text-2xl font-bold text-gray-900 dark:text-gray-100">Каталог курсов</h1>
      <div class="flex space-x-2">
        <button class="btn-primary">
          <PlusIcon class="h-4 w-4 mr-2" />
          Создать курс
        </button>
      </div>
    </div>

    <!-- Filters -->
    <div class="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
      <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
        <div>
          <label class="form-label">Категория</label>
          <select class="form-input">
            <option>Все категории</option>
            <option>Программирование</option>
            <option>Дизайн</option>
            <option>Маркетинг</option>
          </select>
        </div>
        <div>
          <label class="form-label">Сложность</label>
          <select class="form-input">
            <option>Любая сложность</option>
            <option>Начинающий</option>
            <option>Средний</option>
            <option>Продвинутый</option>
          </select>
        </div>
        <div>
          <label class="form-label">Статус</label>
          <select class="form-input">
            <option>Все статусы</option>
            <option>Активные</option>
            <option>Завершенные</option>
            <option>Черновики</option>
          </select>
        </div>
      </div>
    </div>

    <!-- Course Grid -->
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      <div v-for="course in courses" :key="course.id" class="bg-white dark:bg-gray-800 rounded-lg shadow overflow-hidden">
        <div class="h-48 bg-gradient-to-br from-blue-500 to-purple-600"></div>
        <div class="p-6">
          <div class="flex items-center justify-between mb-2">
            <span class="text-xs font-medium text-blue-600 dark:text-blue-400 bg-blue-100 dark:bg-blue-900 px-2 py-1 rounded">
              {{ course.category }}
            </span>
            <span class="text-xs text-gray-500 dark:text-gray-400">{{ course.duration }}</span>
          </div>
          <h3 class="text-lg font-semibold text-gray-900 dark:text-gray-100 mb-2">{{ course.title }}</h3>
          <p class="text-sm text-gray-600 dark:text-gray-400 mb-4">{{ course.description }}</p>
          <div class="flex items-center justify-between">
            <div class="flex items-center space-x-2">
              <StarIcon class="h-4 w-4 text-yellow-400" />
              <span class="text-sm text-gray-600 dark:text-gray-400">{{ course.rating }}</span>
            </div>
            <button class="btn-primary text-sm">Открыть</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { PlusIcon, StarIcon } from '@heroicons/vue/24/outline'

const courses = [
  {
    id: 1,
    title: 'Основы Python',
    description: 'Изучите основы программирования на Python',
    category: 'Программирование',
    duration: '8 часов',
    rating: '4.8'
  },
  {
    id: 2,
    title: 'Веб-разработка',
    description: 'Создавайте современные веб-приложения',
    category: 'Программирование',
    duration: '12 часов',
    rating: '4.9'
  },
  {
    id: 3,
    title: 'UI/UX Дизайн',
    description: 'Создавайте красивые интерфейсы',
    category: 'Дизайн',
    duration: '10 часов',
    rating: '4.7'
  }
]
</script> 