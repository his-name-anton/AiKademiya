<template>
  <div class="space-y-6">
    <h1 class="text-2xl font-bold text-gray-900 dark:text-gray-100">Компоненты</h1>
    
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      <div v-for="component in components" :key="component.id" class="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
        <div class="flex items-center mb-4">
          <component :is="component.icon" class="h-8 w-8 text-blue-600 dark:text-blue-400 mr-3" />
          <h3 class="text-lg font-medium text-gray-900 dark:text-gray-100">{{ component.title }}</h3>
        </div>
        <p class="text-sm text-gray-600 dark:text-gray-400 mb-4">{{ component.description }}</p>
        <div class="flex space-x-2">
          <button class="btn-primary text-sm flex-1">Использовать</button>
          <button class="btn-outline text-sm">Код</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import {
  CubeIcon,
  DocumentTextIcon,
  PhotoIcon,
  VideoCameraIcon,
  SpeakerWaveIcon,
  ChartBarIcon
} from '@heroicons/vue/24/outline'

const components = [
  {
    id: 1,
    title: 'Текстовые блоки',
    description: 'Различные типы текстового контента',
    icon: DocumentTextIcon
  },
  {
    id: 2,
    title: 'Изображения',
    description: 'Компоненты для работы с изображениями',
    icon: PhotoIcon
  },
  {
    id: 3,
    title: 'Видео',
    description: 'Встраивание и воспроизведение видео',
    icon: VideoCameraIcon
  },
  {
    id: 4,
    title: 'Аудио',
    description: 'Аудио контент и подкасты',
    icon: SpeakerWaveIcon
  },
  {
    id: 5,
    title: 'Интерактивные элементы',
    description: 'Кнопки, формы и другие элементы',
    icon: CubeIcon
  },
  {
    id: 6,
    title: 'Аналитика',
    description: 'Графики и диаграммы',
    icon: ChartBarIcon
  }
]
</script> 