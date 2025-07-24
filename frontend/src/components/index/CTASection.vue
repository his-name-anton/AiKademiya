<template>
  <section class="py-20 bg-gradient-to-br from-gray-900 via-blue-900 to-purple-900 text-white relative overflow-hidden">
    <!-- Background decorations -->
    <div class="absolute inset-0">
      <div class="absolute top-20 left-20 w-64 h-64 bg-blue-500/20 rounded-full blur-3xl animate-pulse"></div>
      <div class="absolute bottom-20 right-20 w-48 h-48 bg-purple-500/30 rounded-full blur-2xl animate-pulse delay-1000"></div>
      <div class="absolute top-1/2 left-1/3 w-32 h-32 bg-yellow-400/20 rounded-full blur-xl animate-bounce delay-500"></div>
    </div>

    <div class="container mx-auto px-4 relative z-10">
      <!-- Main CTA content -->
      <div class="text-center max-w-4xl mx-auto animate-fade-in">
        <div class="inline-flex items-center bg-yellow-400/20 text-yellow-300 px-6 py-2 rounded-full text-sm font-medium mb-6 animate-pulse">
          🎯 Ограниченное предложение
        </div>
        
        <h2 class="text-4xl md:text-6xl font-bold mb-6 leading-tight">
          Начните создавать курсы 
          <span class="bg-gradient-to-r from-yellow-400 to-orange-500 bg-clip-text text-transparent">
            прямо сейчас
          </span>
        </h2>
        
        <p class="text-xl md:text-2xl text-gray-300 mb-12 leading-relaxed">
          Присоединяйтесь к революции в образовании. Создайте свой первый курс бесплатно 
          и откройте для себя силу искусственного интеллекта.
        </p>

        <!-- Main CTA buttons -->
        <div class="flex flex-col sm:flex-row gap-6 justify-center mb-16 animate-slide-up delay-300">
          <router-link 
            to="/register"
            class="group relative px-12 py-6 bg-gradient-to-r from-yellow-400 to-orange-500 text-gray-900 font-bold text-xl rounded-2xl shadow-2xl transform hover:scale-105 transition-all duration-300 hover:shadow-yellow-500/50 overflow-hidden"
          >
            <span class="relative z-10 flex items-center justify-center">
              🚀 Создать курс бесплатно
              <svg class="w-6 h-6 ml-2 group-hover:translate-x-1 transition-transform duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"/>
              </svg>
            </span>
            <div class="absolute inset-0 bg-gradient-to-r from-yellow-300 to-orange-400 opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
          </router-link>
          
          <button class="group px-12 py-6 bg-white/10 backdrop-blur-sm border-2 border-white/30 text-white font-bold text-xl rounded-2xl hover:bg-white/20 transition-all duration-300 hover:scale-105">
            <span class="flex items-center justify-center">
              📞 Заказать консультацию
            </span>
          </button>
        </div>

        <!-- Feature highlights -->
        <div class="grid md:grid-cols-3 gap-8 mb-16 animate-slide-up delay-600">
          <div class="text-center">
            <div class="w-16 h-16 bg-green-500/20 rounded-2xl flex items-center justify-center mx-auto mb-4">
              <svg class="w-8 h-8 text-green-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
              </svg>
            </div>
            <h3 class="text-lg font-semibold mb-2">Бесплатный старт</h3>
            <p class="text-gray-400">Создайте первый курс без оплаты</p>
          </div>
          
          <div class="text-center">
            <div class="w-16 h-16 bg-blue-500/20 rounded-2xl flex items-center justify-center mx-auto mb-4">
              <svg class="w-8 h-8 text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/>
              </svg>
            </div>
            <h3 class="text-lg font-semibold mb-2">Быстрый результат</h3>
            <p class="text-gray-400">Курс готов за 5 минут</p>
          </div>
          
          <div class="text-center">
            <div class="w-16 h-16 bg-purple-500/20 rounded-2xl flex items-center justify-center mx-auto mb-4">
              <svg class="w-8 h-8 text-purple-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M18.364 5.636l-3.536 3.536m0 5.656l3.536 3.536M9.172 9.172L5.636 5.636m3.536 9.192L5.636 18.364M21 12a9 9 0 11-18 0 9 9 0 0118 0zm-5 0a4 4 0 11-8 0 4 4 0 018 0z"/>
              </svg>
            </div>
            <h3 class="text-lg font-semibold mb-2">Полная поддержка</h3>
            <p class="text-gray-400">Помощь на каждом шаге</p>
          </div>
        </div>

        <!-- Urgency and social proof -->
        <div class="bg-white/5 backdrop-blur-sm rounded-3xl p-8 border border-white/10 animate-fade-in delay-800">
          <div class="grid md:grid-cols-2 gap-8 items-center">
            <div class="text-left">
              <h3 class="text-2xl font-bold mb-4">⏰ Не упустите момент!</h3>
              <p class="text-gray-300 mb-4">
                Каждый день промедления — это упущенная возможность создать курс, 
                который может изменить вашу карьеру или бизнес.
              </p>
              <div class="flex items-center text-green-400">
                <svg class="w-5 h-5 mr-2" fill="currentColor" viewBox="0 0 20 20">
                  <path d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"/>
                </svg>
                Регистрация занимает 30 секунд
              </div>
            </div>
            
            <div class="text-center md:text-right">
              <div class="text-4xl font-bold text-yellow-400 mb-2">2,847</div>
              <p class="text-gray-300">курсов уже создано</p>
              <div class="text-lg text-green-400 mt-2">+47 за последние 24 часа</div>
            </div>
          </div>
        </div>

        <!-- Risk reversal -->
        <div class="mt-12 animate-fade-in delay-1000">
          <p class="text-gray-400 mb-4">
            💰 <strong>100% гарантия возврата денег в течение 30 дней</strong>
          </p>
          <p class="text-sm text-gray-500">
            Не нравится результат? Вернём деньги без вопросов. 
            Но мы уверены — вы останетесь довольны качеством наших курсов.
          </p>
        </div>

        <!-- Final push -->
        <div class="mt-16 p-8 bg-gradient-to-r from-red-600/20 to-orange-600/20 rounded-2xl border border-red-500/30 animate-pulse-glow">
          <h3 class="text-2xl font-bold text-red-400 mb-4">🔥 Последний шанс!</h3>
          <p class="text-lg text-gray-200 mb-6">
            Присоединяйтесь к тысячам пользователей, которые уже экономят время и деньги с AiKademiya
          </p>
          <router-link 
            to="/register"
            class="inline-flex items-center px-8 py-4 bg-red-600 hover:bg-red-700 text-white font-bold text-lg rounded-xl transition-all duration-300 hover:scale-105 shadow-xl"
          >
            Начать прямо сейчас →
          </router-link>
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

@keyframes pulse-glow {
  0%, 100% {
    box-shadow: 0 0 20px rgba(239, 68, 68, 0.3);
  }
  50% {
    box-shadow: 0 0 40px rgba(239, 68, 68, 0.6);
  }
}

.animate-fade-in {
  animation: fade-in 1s ease-out forwards;
}

.animate-slide-up {
  animation: slide-up 0.8s ease-out forwards;
}

.animate-pulse-glow {
  animation: pulse-glow 2s ease-in-out infinite;
}

.delay-300 {
  animation-delay: 0.3s;
}

.delay-500 {
  animation-delay: 0.5s;
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
</style> 