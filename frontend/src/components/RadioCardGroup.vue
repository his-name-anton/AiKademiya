<template>
  <ul class="grid w-full gap-6 md:grid-cols-1">
    <li v-for="o in options" :key="o.value">
      <input :id="o.value" type="radio" :name="name" :value="o.value" v-model="model" class="hidden peer" required />
      <label :for="o.value" class="inline-flex items-center justify-between w-full p-5 text-gray-500 bg-white border border-gray-200 rounded-lg cursor-pointer dark:hover:text-gray-300 dark:border-gray-700 dark:peer-checked:text-blue-500 peer-checked:border-blue-600 dark:peer-checked:border-blue-600 peer-checked:text-blue-600 hover:text-gray-600 hover:bg-gray-100 dark:text-gray-400 dark:bg-gray-800 dark:hover:bg-gray-700">
        <div class="block">
          <div class="w-full text-lg font-semibold">{{ o.title }}</div>
          <div class="w-full">{{ o.description }}</div>
        </div>
        <svg class="w-5 h-5 ms-3 rtl:rotate-180" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 10">
          <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M1 5h12m0 0L9 1m4 4L9 9" />
        </svg>
      </label>
    </li>
  </ul>
</template>
<script setup>
import { ref, watch } from 'vue'
const props = defineProps({
  options: { type: Array, default: () => [] },
  name: String,
  modelValue: String
})
const emit = defineEmits(['update:modelValue'])
const model = ref(props.modelValue || '')
watch(() => props.modelValue, v => model.value = v)
watch(model, v => emit('update:modelValue', v))
</script>