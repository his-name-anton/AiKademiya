<template>
  <div class="space-y-6">
    <h1 class="text-2xl font-bold text-gray-900 dark:text-gray-100">Сообщения</h1>
    
    <div class="bg-white dark:bg-gray-800 rounded-lg shadow">
      <div class="p-6">
        <div class="space-y-4">
          <div v-for="message in messages" :key="message.id" class="flex items-start space-x-4 p-4 border border-gray-200 dark:border-gray-700 rounded-lg">
            <div class="w-10 h-10 bg-blue-600 rounded-full flex items-center justify-center">
              <span class="text-white font-semibold">{{ message.sender.charAt(0) }}</span>
            </div>
            <div class="flex-1">
              <div class="flex items-center justify-between">
                <h3 class="font-medium text-gray-900 dark:text-gray-100">{{ message.sender }}</h3>
                <span class="text-sm text-gray-500 dark:text-gray-400">{{ message.time }}</span>
              </div>
              <p class="text-sm text-gray-600 dark:text-gray-400 mt-1">{{ message.content }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
const messages = [
  {
    id: 1,
    sender: 'Система',
    content: 'Ваш курс "Основы Python" успешно создан!',
    time: '2 часа назад'
  },
  {
    id: 2,
    sender: 'Поддержка',
    content: 'Спасибо за обращение. Мы рассмотрим ваш вопрос в ближайшее время.',
    time: '1 день назад'
  },
  {
    id: 3,
    sender: 'Система',
    content: 'Добро пожаловать в AiKademiya! Начните создавать свои первые курсы.',
    time: '3 дня назад'
  }
]
</script> 