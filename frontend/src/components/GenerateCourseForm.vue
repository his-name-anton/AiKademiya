<template>
  <form @submit.prevent="submit">
    <div class="mb-6">
      <h3 class="mb-5 text-lg font-medium text-gray-900 dark:text-white">Что будет изучать?</h3>
      <BaseInput id="course-topic" v-model="topic" placeholder="Например Основы программирования на python" />
    </div>
    <div class="mb-6">
      <h3 class="mb-5 text-lg font-medium text-gray-900 dark:text-white">Какая сложность?</h3>
      <RadioCardGroup v-model="difficulty" name="difficulty" :options="difficultyOptions" />
    </div>
    <div class="mb-6">
      <h3 class="mb-5 text-lg font-medium text-gray-900 dark:text-white">В каком стиле составить курс?</h3>
      <div v-for="s in styleOptions" :key="s.value" class="flex items-center ps-4 border border-gray-200 rounded-sm dark:border-gray-700">
        <input :id="s.id" type="radio" name="style" :value="s.value" v-model="style" class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600">
        <label :for="s.id" class="w-full py-4 ms-2 text-sm font-medium text-gray-900 dark:text-gray-300">{{ s.label }}</label>
      </div>
    </div>
    <FormAlert :message="error || apiError" />
    <div class="mb-6">
      <BaseButton type="submit">Поехали!</BaseButton>
    </div>
  </form>
</template>
<script setup>
import { ref } from 'vue'
import BaseInput from './BaseInput.vue'
import RadioCardGroup from './RadioCardGroup.vue'
import BaseButton from './BaseButton.vue'
import FormAlert from './FormAlert.vue'

const props = defineProps({
  apiError: String
})
const emit = defineEmits(['submit'])

const topic = ref('')
const difficulty = ref('')
const style = ref('')
const error = ref('')

const difficultyOptions = [
  { value: 'beginner', title: 'Лёгкий', description: 'Вы новичок в этой теме' },
  { value: 'intermediate', title: 'Продвинутый', description: 'Вы уже знакомы с этой темой, хотите углубиться' },
  { value: 'advanced', title: 'Профессиональный', description: 'В этой теме вы как рыба в воде, но хотите стать ещё лучше' }
]
const styleOptions = [
  { id: 'bordered-radio-1', value: 'default', label: 'Стандартный' },
  { id: 'bordered-radio-2', value: 'academic', label: 'Академический' },
  { id: 'bordered-radio-3', value: 'rebel', label: 'Хулиган' }
]

function submit() {
  if (!topic.value || !difficulty.value || !style.value) {
    error.value = 'Заполните все поля перед отправкой.'
    return
  }
  error.value = ''
  emit('submit', { topic: topic.value, difficulty: difficulty.value, style: style.value })
}
</script>
