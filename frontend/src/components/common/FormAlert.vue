<template>
  <div 
    v-if="message"
    :class="alertClasses"
    class="p-4 mb-4 text-sm rounded-lg"
    role="alert"
  >
    <div class="flex items-center justify-between">
      <div class="flex items-center">
        <component :is="iconComponent" class="w-5 h-5 mr-2 flex-shrink-0" />
        <div>
          <span class="font-medium">{{ title }}</span>
          <div class="mt-1">{{ message }}</div>
        </div>
      </div>
      <button 
        v-if="closeable"
        @click="$emit('close')"
        type="button"
        class="ml-auto -mx-1.5 -my-1.5 rounded-lg focus:ring-2 p-1.5 inline-flex h-8 w-8 hover:bg-opacity-20"
      >
        <span class="sr-only">Закрыть</span>
        <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
          <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"></path>
        </svg>
      </button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'

interface Props {
  type?: 'success' | 'error' | 'warning' | 'info'
  message: string
  title?: string
  closeable?: boolean
}

const props = withDefaults(defineProps<Props>(), {
  type: 'info',
  title: '',
  closeable: true
})

defineEmits<{
  close: []
}>()

const alertClasses = computed(() => {
  const baseClasses = 'p-4 mb-4 text-sm rounded-lg'
  
  switch (props.type) {
    case 'success':
      return `${baseClasses} text-green-800 bg-green-50 dark:bg-gray-800 dark:text-green-400`
    case 'error':
      return `${baseClasses} text-red-800 bg-red-50 dark:bg-gray-800 dark:text-red-400`
    case 'warning':
      return `${baseClasses} text-yellow-800 bg-yellow-50 dark:bg-gray-800 dark:text-yellow-300`
    default:
      return `${baseClasses} text-blue-800 bg-blue-50 dark:bg-gray-800 dark:text-blue-400`
  }
})

const iconComponent = computed(() => {
  switch (props.type) {
    case 'success':
      return 'CheckCircleIcon'
    case 'error':
      return 'ExclamationCircleIcon'
    case 'warning':
      return 'ExclamationTriangleIcon'
    default:
      return 'InformationCircleIcon'
  }
})
</script>

<script lang="ts">
// Icon components
const CheckCircleIcon = {
  template: `<svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>`
}

const ExclamationCircleIcon = {
  template: `<svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>`
}

const ExclamationTriangleIcon = {
  template: `<svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-2.5L13.732 4c-.77-.833-1.964-.833-2.732 0L3.732 16.5c-.77.833.192 2.5 1.732 2.5z"></path></svg>`
}

const InformationCircleIcon = {
  template: `<svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>`
}

export { CheckCircleIcon, ExclamationCircleIcon, ExclamationTriangleIcon, InformationCircleIcon }
</script>