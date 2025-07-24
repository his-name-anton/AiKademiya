<template>
  <div id="app" class="min-h-screen bg-gray-50">
    <!-- Main app content -->
    <router-view />
  </div>
</template>

<script setup lang="ts">
// Simplified app without complex initialization
</script>

<style>
/* Add any global styles here */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.2s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>