<template>
  <section class="py-20 bg-gradient-to-br from-gray-50 to-blue-50">
    <div class="container mx-auto px-4">
      <!-- Section header -->
      <div class="text-center mb-16 animate-fade-in">
        <h2 class="text-4xl md:text-5xl font-bold text-gray-900 mb-4">
          Как это 
          <span class="bg-gradient-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent">
            работает
          </span>
        </h2>
        <p class="text-xl text-gray-600 max-w-2xl mx-auto">
          Всего три простых шага от идеи до готового курса
        </p>
      </div>

      <!-- Steps -->
      <div class="relative max-w-5xl mx-auto">
        <!-- Connection line for desktop -->
        <div class="hidden lg:block absolute top-24 left-0 right-0 h-1 bg-gradient-to-r from-blue-200 via-purple-200 to-green-200 rounded-full"></div>
        
        <div class="grid lg:grid-cols-3 gap-12 lg:gap-8">
          <!-- Step 1 -->
          <div class="relative group animate-slide-up">
            <!-- Step number circle -->
            <div class="relative z-10 mx-auto w-48 h-48 bg-gradient-to-br from-blue-500 to-blue-600 rounded-full flex items-center justify-center mb-8 group-hover:scale-110 transition-all duration-500 shadow-2xl group-hover:shadow-blue-500/50">
              <div class="text-center text-white">
                <div class="text-6xl font-bold mb-2">1</div>
                <div class="w-16 h-16 mx-auto bg-white/20 rounded-2xl flex items-center justify-center">
                  <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.232 5.232l3.536 3.536m-2.036-5.036a2.5 2.5 0 113.536 3.536L6.5 21.036H3v-3.572L16.732 3.732z"/>
                  </svg>
                </div>
              </div>
            </div>
            
            <!-- Content -->
            <div class="text-center group-hover:transform group-hover:-translate-y-2 transition-all duration-300">
              <h3 class="text-2xl font-bold text-gray-900 mb-4">Опишите тему курса</h3>
              <p class="text-gray-600 leading-relaxed mb-6">
                Просто расскажите, о чём хотите создать курс: укажите тему, целевую аудиторию и уровень сложности
              </p>
              <div class="bg-white rounded-xl p-4 shadow-lg border-l-4 border-blue-500">
                <div class="text-sm text-gray-500 mb-2">Пример:</div>
                <div class="text-gray-800 italic">"Создай курс по основам Python для начинающих программистов"</div>
              </div>
            </div>
          </div>

          <!-- Step 2 -->
          <div class="relative group animate-slide-up delay-300">
            <!-- Step number circle -->
            <div class="relative z-10 mx-auto w-48 h-48 bg-gradient-to-br from-purple-500 to-purple-600 rounded-full flex items-center justify-center mb-8 group-hover:scale-110 transition-all duration-500 shadow-2xl group-hover:shadow-purple-500/50">
              <div class="text-center text-white">
                <div class="text-6xl font-bold mb-2">2</div>
                <div class="w-16 h-16 mx-auto bg-white/20 rounded-2xl flex items-center justify-center">
                  <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"/>
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/>
                  </svg>
                </div>
              </div>
            </div>
            
            <!-- Content -->
            <div class="text-center group-hover:transform group-hover:-translate-y-2 transition-all duration-300">
              <h3 class="text-2xl font-bold text-gray-900 mb-4">ИИ создаёт курс</h3>
              <p class="text-gray-600 leading-relaxed mb-6">
                Наш продвинутый ИИ анализирует вашу тему и автоматически генерирует полную структуру курса с уроками и тестами
              </p>
              <div class="bg-white rounded-xl p-4 shadow-lg">
                <div class="flex items-center justify-center space-x-2 mb-3">
                  <div class="w-3 h-3 bg-purple-500 rounded-full animate-pulse"></div>
                  <div class="w-3 h-3 bg-purple-400 rounded-full animate-pulse delay-100"></div>
                  <div class="w-3 h-3 bg-purple-300 rounded-full animate-pulse delay-200"></div>
                </div>
                <div class="text-sm text-gray-600">ИИ генерирует контент...</div>
              </div>
            </div>
          </div>

          <!-- Step 3 -->
          <div class="relative group animate-slide-up delay-600">
            <!-- Step number circle -->
            <div class="relative z-10 mx-auto w-48 h-48 bg-gradient-to-br from-green-500 to-green-600 rounded-full flex items-center justify-center mb-8 group-hover:scale-110 transition-all duration-500 shadow-2xl group-hover:shadow-green-500/50">
              <div class="text-center text-white">
                <div class="text-6xl font-bold mb-2">3</div>
                <div class="w-16 h-16 mx-auto bg-white/20 rounded-2xl flex items-center justify-center">
                  <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.246 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"/>
                  </svg>
                </div>
              </div>
            </div>
            
            <!-- Content -->
            <div class="text-center group-hover:transform group-hover:-translate-y-2 transition-all duration-300">
              <h3 class="text-2xl font-bold text-gray-900 mb-4">Начинайте обучение</h3>
              <p class="text-gray-600 leading-relaxed mb-6">
                Получите готовый интерактивный курс с прогрессом, тестами и сертификатом. Сразу можете начинать учиться или делиться с другими
              </p>
              <div class="bg-white rounded-xl p-4 shadow-lg border-l-4 border-green-500">
                <div class="flex items-center justify-between mb-2">
                  <span class="text-sm font-medium text-gray-700">Прогресс курса:</span>
                  <span class="text-sm font-bold text-green-600">100%</span>
                </div>
                <div class="w-full bg-gray-200 rounded-full h-2">
                  <div class="bg-gradient-to-r from-green-400 to-green-600 h-2 rounded-full w-full"></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Call to action -->
      <div class="text-center mt-20 animate-fade-in delay-800">
        <h3 class="text-3xl font-bold text-gray-900 mb-6">
          Готовы создать свой первый курс?
        </h3>
        <p class="text-xl text-gray-600 mb-8 max-w-2xl mx-auto">
          Это займёт меньше минуты, а результат превзойдёт ваши ожидания
        </p>
        <div class="flex flex-col sm:flex-row gap-4 justify-center">
          <router-link 
            to="/register" 
            class="group px-8 py-4 bg-gradient-to-r from-blue-600 to-purple-600 text-white font-bold text-lg rounded-2xl hover:from-blue-700 hover:to-purple-700 transition-all duration-300 hover:scale-105 shadow-xl hover:shadow-2xl"
          >
            <span class="flex items-center justify-center">
              🚀 Создать курс бесплатно
              <svg class="w-5 h-5 ml-2 group-hover:translate-x-1 transition-transform duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"/>
              </svg>
            </span>
          </router-link>
          <button class="px-8 py-4 bg-white text-gray-700 font-semibold text-lg rounded-2xl border-2 border-gray-300 hover:border-gray-400 hover:bg-gray-50 transition-all duration-300 hover:scale-105">
            Посмотреть примеры
          </button>
        </div>
      </div>
    </div>
  </section>
</template>

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

.delay-300 {
  animation-delay: 0.3s;
}

.delay-600 {
  animation-delay: 0.6s;
}

.delay-800 {
  animation-delay: 0.8s;
}

.delay-100 {
  animation-delay: 0.1s;
}

.delay-200 {
  animation-delay: 0.2s;
}
</style>