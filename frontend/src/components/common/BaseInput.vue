<template>
  <div class="relative">
    <input
      :id="id"
      :type="type"
      :value="modelValue"
      :placeholder="placeholder"
      :disabled="disabled"
      :readonly="readonly"
      :required="required"
      :autofocus="autofocus"
      :class="inputClasses"
      @input="$emit('update:modelValue', ($event.target as HTMLInputElement).value)"
      @blur="$emit('blur', $event)"
      @focus="$emit('focus', $event)"
    />
    <div 
      v-if="error" 
      class="mt-1 text-sm text-red-600 dark:text-red-400"
    >
      {{ error }}
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'

interface Props {
  id?: string
  type?: string
  modelValue?: string | number
  placeholder?: string
  disabled?: boolean
  readonly?: boolean
  required?: boolean
  autofocus?: boolean
  error?: string
  size?: 'sm' | 'md' | 'lg'
}

const props = withDefaults(defineProps<Props>(), {
  type: 'text',
  modelValue: '',
  size: 'md'
})

defineEmits<{
  'update:modelValue': [value: string]
  blur: [event: FocusEvent]
  focus: [event: FocusEvent]
}>()

const inputClasses = computed(() => {
  const baseClasses = 'block w-full border rounded-lg focus:outline-none transition-colors'
  const sizeClasses = {
    sm: 'px-3 py-2 text-sm',
    md: 'px-4 py-2.5 text-sm',
    lg: 'px-4 py-3 text-base'
  }
  
  const stateClasses = props.error
    ? 'border-red-300 text-red-900 placeholder-red-300 focus:ring-red-500 focus:border-red-500 dark:bg-red-50 dark:border-red-400 dark:text-red-900'
    : 'border-gray-300 text-gray-900 placeholder-gray-400 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:text-white dark:placeholder-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500'
  
  const disabledClasses = props.disabled
    ? 'bg-gray-100 cursor-not-allowed dark:bg-gray-600'
    : 'bg-white dark:bg-gray-700'

  return `${baseClasses} ${sizeClasses[props.size]} ${stateClasses} ${disabledClasses}`
})
</script>