<template>
  <section class="relative overflow-hidden bg-gradient-to-br from-blue-600 via-blue-700 to-purple-800 py-20 lg:py-32">
    <!-- Background decorations -->
    <div class="absolute inset-0">
      <div class="absolute top-1/4 left-1/4 w-64 h-64 bg-white/10 rounded-full blur-3xl animate-pulse"></div>
      <div class="absolute bottom-1/4 right-1/4 w-48 h-48 bg-purple-300/20 rounded-full blur-2xl animate-pulse delay-1000"></div>
      <div class="absolute top-1/2 right-1/3 w-32 h-32 bg-blue-300/30 rounded-full blur-xl animate-bounce delay-500"></div>
    </div>
    
    <div class="relative container mx-auto px-4 text-center text-white">
      <!-- Main heading with staggered animation -->
      <div class="animate-fade-in">
        <h1 class="text-4xl md:text-6xl lg:text-7xl font-bold mb-6 leading-tight">
          <span class="block animate-slide-up">Создавай курсы</span>
          <span class="block animate-slide-up delay-200 bg-gradient-to-r from-yellow-400 to-orange-500 bg-clip-text text-transparent">
            с помощью ИИ
          </span>
          <span class="block animate-slide-up delay-400 text-3xl md:text-4xl lg:text-5xl mt-2 font-normal text-blue-100">
            за считанные минуты
          </span>
        </h1>
      </div>
      
      <!-- Subtitle -->
      <div class="animate-fade-in delay-600">
        <p class="text-xl md:text-2xl text-blue-100 mb-4 max-w-3xl mx-auto leading-relaxed">
          Революционная платформа для автоматической генерации образовательных курсов
        </p>
        <p class="text-lg text-blue-200 mb-12 max-w-2xl mx-auto">
          От идеи до готового курса с тестами и структурой — всего за несколько кликов
        </p>
      </div>
      
      <!-- CTA Buttons -->
      <div class="animate-slide-up delay-800 flex flex-col sm:flex-row gap-6 justify-center items-center">
        <router-link 
          to="/register"
          class="group relative px-8 py-4 bg-gradient-to-r from-yellow-400 to-orange-500 text-gray-900 font-bold text-lg rounded-2xl shadow-2xl transform hover:scale-105 transition-all duration-300 hover:shadow-yellow-500/50 overflow-hidden"
        >
          <span class="relative z-10">🚀 Создать первый курс</span>
          <div class="absolute inset-0 bg-gradient-to-r from-yellow-300 to-orange-400 opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
        </router-link>
        
        <button class="group px-8 py-4 bg-white/10 backdrop-blur-sm border-2 border-white/30 text-white font-semibold text-lg rounded-2xl hover:bg-white/20 transition-all duration-300 hover:scale-105">
          <span class="flex items-center gap-2">
            <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 20 20">
              <path d="M10 18a8 8 0 100-16 8 8 0 000 16zM9.555 7.168A1 1 0 008 8v4a1 1 0 001.555.832l3-2a1 1 0 000-1.664l-3-2z"/>
            </svg>
            Посмотреть демо
          </span>
        </button>
      </div>
      
      <!-- Trust indicators -->
      <div class="animate-fade-in delay-1000 mt-16 pt-12 border-t border-white/20">
        <p class="text-blue-200 mb-6 text-sm uppercase tracking-wider">Уже доверяют нам</p>
        <div class="flex flex-wrap justify-center items-center gap-8 opacity-70">
          <div class="flex items-center gap-2 text-blue-100">
            <span class="text-2xl font-bold">1000+</span>
            <span>курсов создано</span>
          </div>
          <div class="w-px h-8 bg-white/30 hidden sm:block"></div>
          <div class="flex items-center gap-2 text-blue-100">
            <span class="text-2xl font-bold">50+</span>
            <span>компаний</span>
          </div>
          <div class="w-px h-8 bg-white/30 hidden sm:block"></div>
          <div class="flex items-center gap-2 text-blue-100">
            <span class="text-2xl font-bold">95%</span>
            <span>экономии времени</span>
          </div>
        </div>
      </div>
    </div>
    
    <!-- Scroll indicator -->
    <div class="absolute bottom-8 left-1/2 transform -translate-x-1/2 animate-bounce delay-1200">
      <div class="w-6 h-10 border-2 border-white/50 rounded-full flex justify-center">
        <div class="w-1 h-3 bg-white/70 rounded-full mt-2 animate-pulse"></div>
      </div>
    </div>
  </section>
</template>

<style scoped>
@keyframes fade-in {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes slide-up {
  from {
    opacity: 0;
    transform: translateY(30px);
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

.delay-1200 {
  animation-delay: 1.2s;
}

.delay-500 {
  animation-delay: 0.5s;
}
</style>