<template>
  <input
    :id="id"
    :type="type"
    :placeholder="placeholder"
    v-model="inputValue"
    @input="$emit('update:modelValue', inputValue)"
    class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" />
</template>
<script setup>
import { ref, watch } from 'vue'

const props = defineProps({
  id: String,
  type: { type: String, default: 'text' },
  modelValue: String,
  placeholder: String
})

const inputValue = ref(props.modelValue || '')
watch(() => props.modelValue, v => inputValue.value = v)
</script>
