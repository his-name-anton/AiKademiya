<template>
  <div class="space-y-6">
    <h1 class="text-2xl font-bold text-gray-900 dark:text-gray-100">Документация</h1>
    
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      <div v-for="doc in documentation" :key="doc.id" class="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
        <div class="flex items-center mb-4">
          <component :is="doc.icon" class="h-8 w-8 text-blue-600 dark:text-blue-400 mr-3" />
          <h3 class="text-lg font-medium text-gray-900 dark:text-gray-100">{{ doc.title }}</h3>
        </div>
        <p class="text-sm text-gray-600 dark:text-gray-400 mb-4">{{ doc.description }}</p>
        <button class="btn-outline text-sm w-full">Читать</button>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import {
  BookOpenIcon,
  AcademicCapIcon,
  CogIcon,
  QuestionMarkCircleIcon,
  ChartBarIcon,
  UserGroupIcon
} from '@heroicons/vue/24/outline'

const documentation = [
  {
    id: 1,
    title: 'Начало работы',
    description: 'Быстрый старт с платформой AiKademiya',
    icon: BookOpenIcon
  },
  {
    id: 2,
    title: 'Создание курсов',
    description: 'Пошаговое руководство по созданию курсов',
    icon: AcademicCapIcon
  },
  {
    id: 3,
    title: 'API документация',
    description: 'Техническая документация для разработчиков',
    icon: CogIcon
  },
  {
    id: 4,
    title: 'FAQ',
    description: 'Часто задаваемые вопросы',
    icon: QuestionMarkCircleIcon
  },
  {
    id: 5,
    title: 'Аналитика',
    description: 'Как использовать аналитические данные',
    icon: ChartBarIcon
  },
  {
    id: 6,
    title: 'Сообщество',
    description: 'Руководство по работе с сообществом',
    icon: UserGroupIcon
  }
]
</script> 