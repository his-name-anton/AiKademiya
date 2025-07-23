<template>
  <div class="bg-gray-50">
    <MainNavbar />
    <HeroSection />
    <HowItWorks />
    <Benefits />
  </div>
</template>

<script setup>
import MainNavbar from '@/components/layout/MainNavbar.vue'
import HeroSection from '@/components/index/HeroSection.vue'
import HowItWorks from '@/components/index/HowItWorks.vue'
import Benefits from '@/components/index/Benefits.vue'
</script>