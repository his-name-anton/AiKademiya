<template>
  <section class="py-20 bg-gradient-to-r from-blue-600 via-purple-600 to-indigo-700 text-white relative overflow-hidden">
    <!-- Background decorations -->
    <div class="absolute inset-0">
      <div class="absolute top-10 left-10 w-32 h-32 bg-white/10 rounded-full blur-2xl animate-pulse"></div>
      <div class="absolute bottom-20 right-20 w-48 h-48 bg-yellow-300/20 rounded-full blur-3xl animate-pulse delay-1000"></div>
      <div class="absolute top-1/2 left-1/4 w-24 h-24 bg-green-300/30 rounded-full blur-xl animate-bounce delay-500"></div>
    </div>

    <div class="container mx-auto px-4 relative z-10">
      <!-- Section header -->
      <div class="text-center mb-16 animate-fade-in">
        <h2 class="text-4xl md:text-5xl font-bold mb-4">
          Платформе доверяют
        </h2>
        <p class="text-xl text-blue-100 max-w-2xl mx-auto">
          Впечатляющие результаты говорят сами за себя
        </p>
      </div>

      <!-- Stats grid -->
      <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-8">
        <!-- Stat 1: Courses Created -->
        <div class="text-center group animate-slide-up">
          <div class="w-20 h-20 mx-auto mb-6 bg-white/20 backdrop-blur-sm rounded-2xl flex items-center justify-center group-hover:scale-110 transition-all duration-300">
            <svg class="w-10 h-10 text-yellow-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.246 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"/>
            </svg>
          </div>
          <div class="text-4xl lg:text-5xl font-bold mb-2 animate-number" data-target="2847">0</div>
          <div class="text-lg text-blue-100 font-medium">курсов создано</div>
          <div class="text-sm text-blue-200 mt-2">+150 за последний месяц</div>
        </div>

        <!-- Stat 2: Time Saved -->
        <div class="text-center group animate-slide-up delay-200">
          <div class="w-20 h-20 mx-auto mb-6 bg-white/20 backdrop-blur-sm rounded-2xl flex items-center justify-center group-hover:scale-110 transition-all duration-300">
            <svg class="w-10 h-10 text-green-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
            </svg>
          </div>
          <div class="text-4xl lg:text-5xl font-bold mb-2 animate-number" data-target="12500">0</div>
          <div class="text-lg text-blue-100 font-medium">часов сэкономлено</div>
          <div class="text-sm text-blue-200 mt-2">времени разработчиков</div>
        </div>

        <!-- Stat 3: Money Saved -->
        <div class="text-center group animate-slide-up delay-400">
          <div class="w-20 h-20 mx-auto mb-6 bg-white/20 backdrop-blur-sm rounded-2xl flex items-center justify-center group-hover:scale-110 transition-all duration-300">
            <svg class="w-10 h-10 text-yellow-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1"/>
            </svg>
          </div>
          <div class="text-4xl lg:text-5xl font-bold mb-2">$18M+</div>
          <div class="text-lg text-blue-100 font-medium">сэкономлено клиентами</div>
          <div class="text-sm text-blue-200 mt-2">на разработке контента</div>
        </div>

        <!-- Stat 4: Satisfaction -->
        <div class="text-center group animate-slide-up delay-600">
          <div class="w-20 h-20 mx-auto mb-6 bg-white/20 backdrop-blur-sm rounded-2xl flex items-center justify-center group-hover:scale-110 transition-all duration-300">
            <svg class="w-10 h-10 text-pink-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/>
            </svg>
          </div>
          <div class="text-4xl lg:text-5xl font-bold mb-2 animate-number" data-target="97">0</div>
          <div class="text-lg text-blue-100 font-medium">% довольных клиентов</div>
          <div class="text-sm text-blue-200 mt-2">по результатам опросов</div>
        </div>
      </div>

      <!-- Testimonial highlight -->
      <div class="mt-20 text-center animate-fade-in delay-800">
        <div class="bg-white/10 backdrop-blur-sm rounded-3xl p-8 md:p-12 max-w-4xl mx-auto border border-white/20">
          <div class="text-6xl mb-6">💬</div>
          <blockquote class="text-2xl md:text-3xl font-light italic mb-6 leading-relaxed">
            "За 2 месяца мы создали 15 корпоративных курсов вместо обычных 2. 
            Экономия бюджета составила более 300 тысяч рублей."
          </blockquote>
          <div class="flex items-center justify-center space-x-4">
            <div class="w-16 h-16 bg-gradient-to-br from-yellow-400 to-orange-500 rounded-full flex items-center justify-center text-2xl font-bold text-white">
              АС
            </div>
            <div class="text-left">
              <div class="font-semibold text-lg">Анна Смирнова</div>
              <div class="text-blue-200">Руководитель отдела обучения, TechCorp</div>
            </div>
          </div>
        </div>
      </div>

      <!-- CTA -->
      <div class="text-center mt-16 animate-fade-in delay-1000">
        <router-link 
          to="/register"
          class="inline-flex items-center px-8 py-4 bg-white text-blue-600 font-bold text-lg rounded-2xl hover:bg-gray-100 transition-all duration-300 hover:scale-105 shadow-2xl"
        >
          Присоединиться к успешным компаниям
          <svg class="w-5 h-5 ml-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"/>
          </svg>
        </router-link>
      </div>
    </div>
  </section>
</template>

<script setup>
import { onMounted } from 'vue'

// Animate numbers
onMounted(() => {
  const animateNumber = (element, target, duration = 2000) => {
    const start = 0
    const increment = target / (duration / 16)
    let current = start
    
    const timer = setInterval(() => {
      current += increment
      if (current >= target) {
        current = target
        clearInterval(timer)
      }
      element.textContent = Math.floor(current).toLocaleString()
    }, 16)
  }

  // Start animation when component is mounted
  setTimeout(() => {
    const numberElements = document.querySelectorAll('.animate-number')
    numberElements.forEach(element => {
      const target = parseInt(element.dataset.target)
      animateNumber(element, target)
    })
  }, 500)
})
</script>

<style scoped>
@keyframes fade-in {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes slide-up {
  from {
    opacity: 0;
    transform: translateY(40px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.animate-fade-in {
  animation: fade-in 1s ease-out forwards;
}

.animate-slide-up {
  animation: slide-up 0.8s ease-out forwards;
}

.delay-200 {
  animation-delay: 0.2s;
}

.delay-400 {
  animation-delay: 0.4s;
}

.delay-600 {
  animation-delay: 0.6s;
}

.delay-800 {
  animation-delay: 0.8s;
}

.delay-1000 {
  animation-delay: 1s;
}

.delay-500 {
  animation-delay: 0.5s;
}
</style> 