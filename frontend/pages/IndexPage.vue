<template>
  <main class="bg-gray-50 text-gray-900">
    <MainNavbar />
    <div class="container mx-auto px-4 max-w-7xl">
      <HeroSection />
      <HowItWorks />
      <Benefits />
    </div>
  </main>
</template>

<script setup>
import MainNavbar from '@/components/layout/MainNavbar.vue'
import HeroSection from '@/components/index/HeroSection.vue'
import HowItWorks from '@/components/index/HowItWorks.vue'
import Benefits from '@/components/index/Benefits.vue'
</script>