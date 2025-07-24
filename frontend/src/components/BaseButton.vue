<template>
  <button :type="type" @click="$emit('click')" class="w-full block text-white bg-gradient-to-br from-purple-600 to-blue-500 hover:bg-gradient-to-bl focus:ring-4 focus:outline-none focus:ring-blue-300 dark:focus:ring-blue-800 font-medium rounded-lg text-sm px-5 py-2.5 text-center">
    <slot />
  </button>
</template>
<script setup>
const props = defineProps({
  type: { type: String, default: 'button' }
})
</script>
