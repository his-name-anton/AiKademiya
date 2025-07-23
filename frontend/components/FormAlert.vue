<template>
  <div v-if="message" class="p-4 mb-4 text-sm text-red-800 rounded-lg bg-red-50 dark:bg-gray-800 dark:text-red-400" role="alert">
    {{ message }}
  </div>
</template>
<script setup>
const props = defineProps({
  message: String
})
</script>
