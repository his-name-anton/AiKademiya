<template>
  <div class="space-y-6">
    <h1 class="text-2xl font-bold text-gray-900 dark:text-gray-100">Помощь</h1>
    
    <!-- Search -->
    <div class="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
      <div class="max-w-md">
        <label class="form-label">Поиск по вопросам</label>
        <div class="relative">
          <input
            type="text"
            placeholder="Введите ваш вопрос..."
            class="form-input pr-10"
          />
          <MagnifyingGlassIcon class="absolute right-3 top-1/2 transform -translate-y-1/2 h-5 w-5 text-gray-400" />
        </div>
      </div>
    </div>

    <!-- FAQ -->
    <div class="bg-white dark:bg-gray-800 rounded-lg shadow">
      <div class="px-6 py-4 border-b border-gray-200 dark:border-gray-700">
        <h3 class="text-lg font-medium text-gray-900 dark:text-gray-100">Часто задаваемые вопросы</h3>
      </div>
      <div class="p-6">
        <div class="space-y-4">
          <div v-for="faq in faqs" :key="faq.id" class="border border-gray-200 dark:border-gray-700 rounded-lg">
            <button
              @click="toggleFaq(faq.id)"
              class="w-full px-4 py-3 text-left flex items-center justify-between hover:bg-gray-50 dark:hover:bg-gray-700"
            >
              <span class="font-medium text-gray-900 dark:text-gray-100">{{ faq.question }}</span>
              <ChevronDownIcon 
                class="h-5 w-5 text-gray-500 dark:text-gray-400 transition-transform"
                :class="{ 'rotate-180': openFaqs.includes(faq.id) }"
              />
            </button>
            <div v-if="openFaqs.includes(faq.id)" class="px-4 pb-3">
              <p class="text-sm text-gray-600 dark:text-gray-400">{{ faq.answer }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Contact Support -->
    <div class="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
      <h3 class="text-lg font-medium text-gray-900 dark:text-gray-100 mb-4">Связаться с поддержкой</h3>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div>
          <h4 class="font-medium text-gray-900 dark:text-gray-100 mb-2">Email поддержка</h4>
          <p class="text-sm text-gray-600 dark:text-gray-400 mb-2">support@aikademiya.com</p>
          <p class="text-sm text-gray-500 dark:text-gray-400">Время ответа: до 24 часов</p>
        </div>
        <div>
          <h4 class="font-medium text-gray-900 dark:text-gray-100 mb-2">Чат поддержки</h4>
          <p class="text-sm text-gray-600 dark:text-gray-400 mb-2">Доступен 24/7</p>
          <button class="btn-primary text-sm">Начать чат</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { MagnifyingGlassIcon, ChevronDownIcon } from '@heroicons/vue/24/outline'

const openFaqs = ref<number[]>([])

const faqs = [
  {
    id: 1,
    question: 'Как создать свой первый курс?',
    answer: 'Для создания курса перейдите в раздел "Создать курс", выберите тему, сложность и стиль. Наша ИИ система автоматически сгенерирует контент для вашего курса.'
  },
  {
    id: 2,
    question: 'Можно ли редактировать созданные курсы?',
    answer: 'Да, вы можете редактировать любой созданный курс. Перейдите в раздел "Мои курсы" и выберите курс для редактирования.'
  },
  {
    id: 3,
    question: 'Как работает система подписок?',
    answer: 'У нас есть несколько тарифных планов. Бесплатный план позволяет создавать ограниченное количество курсов, а премиум планы дают больше возможностей.'
  },
  {
    id: 4,
    question: 'Можно ли экспортировать курсы?',
    answer: 'Да, вы можете экспортировать курсы в различных форматах, включая PDF, SCORM и другие популярные форматы.'
  }
]

const toggleFaq = (id: number) => {
  const index = openFaqs.value.indexOf(id)
  if (index > -1) {
    openFaqs.value.splice(index, 1)
  } else {
    openFaqs.value.push(id)
  }
}
</script> 