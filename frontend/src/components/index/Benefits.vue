<template>
  <section class="py-20 bg-white">
    <div class="container mx-auto px-4">
      <!-- Section header -->
      <div class="text-center mb-16 animate-fade-in">
        <h2 class="text-4xl md:text-5xl font-bold text-gray-900 mb-4">
          Почему выбирают 
          <span class="bg-gradient-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent">
            AiKademiya
          </span>
        </h2>
        <p class="text-xl text-gray-600 max-w-3xl mx-auto">
          Революционная платформа, которая меняет подход к созданию образовательного контента
        </p>
      </div>

      <!-- Benefits grid -->
      <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8 mb-16">
        <!-- Benefit 1: Speed -->
        <div class="group p-8 rounded-2xl bg-gradient-to-br from-blue-50 to-blue-100 hover:from-blue-100 hover:to-blue-200 transition-all duration-300 hover:shadow-xl hover:-translate-y-2 animate-slide-up">
          <div class="w-16 h-16 bg-gradient-to-br from-blue-500 to-blue-600 rounded-2xl flex items-center justify-center mb-6 group-hover:scale-110 transition-transform duration-300">
            <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/>
            </svg>
          </div>
          <h3 class="text-2xl font-bold text-gray-900 mb-4">Молниеносная скорость</h3>
          <p class="text-gray-600 leading-relaxed">
            Создавайте полноценные курсы за минуты вместо месяцев. От идеи до готового контента — всего несколько кликов.
          </p>
          <div class="mt-4 text-blue-600 font-semibold">
            ⚡ В 100+ раз быстрее традиционных методов
          </div>
        </div>

        <!-- Benefit 2: Cost -->
        <div class="group p-8 rounded-2xl bg-gradient-to-br from-green-50 to-green-100 hover:from-green-100 hover:to-green-200 transition-all duration-300 hover:shadow-xl hover:-translate-y-2 animate-slide-up delay-200">
          <div class="w-16 h-16 bg-gradient-to-br from-green-500 to-green-600 rounded-2xl flex items-center justify-center mb-6 group-hover:scale-110 transition-transform duration-300">
            <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1"/>
            </svg>
          </div>
          <h3 class="text-2xl font-bold text-gray-900 mb-4">Экономия до 70%</h3>
          <p class="text-gray-600 leading-relaxed">
            Снижение стоимости разработки курсов с $15,000 до $8,500. Больше никаких астрономических бюджетов на контент.
          </p>
          <div class="mt-4 text-green-600 font-semibold">
            💰 Экономия $6,500+ на каждом курсе
          </div>
        </div>

        <!-- Benefit 3: Quality -->
        <div class="group p-8 rounded-2xl bg-gradient-to-br from-purple-50 to-purple-100 hover:from-purple-100 hover:to-purple-200 transition-all duration-300 hover:shadow-xl hover:-translate-y-2 animate-slide-up delay-400">
          <div class="w-16 h-16 bg-gradient-to-br from-purple-500 to-purple-600 rounded-2xl flex items-center justify-center mb-6 group-hover:scale-110 transition-transform duration-300">
            <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
            </svg>
          </div>
          <h3 class="text-2xl font-bold text-gray-900 mb-4">Профессиональное качество</h3>
          <p class="text-gray-600 leading-relaxed">
            Структурированные курсы с тестами, заданиями и отслеживанием прогресса. Качество экспертного уровня автоматически.
          </p>
          <div class="mt-4 text-purple-600 font-semibold">
            ✨ Готовые к использованию курсы
          </div>
        </div>

        <!-- Benefit 4: Russian Focus -->
        <div class="group p-8 rounded-2xl bg-gradient-to-br from-red-50 to-red-100 hover:from-red-100 hover:to-red-200 transition-all duration-300 hover:shadow-xl hover:-translate-y-2 animate-slide-up delay-600">
          <div class="w-16 h-16 bg-gradient-to-br from-red-500 to-red-600 rounded-2xl flex items-center justify-center mb-6 group-hover:scale-110 transition-transform duration-300">
            <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 12a9 9 0 01-9 9m9-9a9 9 0 00-9-9m9 9H3m9 9v-9m0-9v9m0 9c-5 0-9-4-9-9s4-9 9-9"/>
            </svg>
          </div>
          <h3 class="text-2xl font-bold text-gray-900 mb-4">Русскоязычная платформа</h3>
          <p class="text-gray-600 leading-relaxed">
            Полная локализация и интеграция с российскими сервисами. ЮKassa, ВКонтакте и другие знакомые инструменты.
          </p>
          <div class="mt-4 text-red-600 font-semibold">
            🇷🇺 Создано для русскоязычного рынка
          </div>
        </div>

        <!-- Benefit 5: Automation -->
        <div class="group p-8 rounded-2xl bg-gradient-to-br from-orange-50 to-orange-100 hover:from-orange-100 hover:to-orange-200 transition-all duration-300 hover:shadow-xl hover:-translate-y-2 animate-slide-up delay-800">
          <div class="w-16 h-16 bg-gradient-to-br from-orange-500 to-orange-600 rounded-2xl flex items-center justify-center mb-6 group-hover:scale-110 transition-transform duration-300">
            <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"/>
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/>
            </svg>
          </div>
          <h3 class="text-2xl font-bold text-gray-900 mb-4">Полная автоматизация</h3>
          <p class="text-gray-600 leading-relaxed">
            Курсы создаются "под ключ": от структуры и контента до тестов и заданий. Минимальное участие человека.
          </p>
          <div class="mt-4 text-orange-600 font-semibold">
            🤖 ИИ делает всю работу за вас
          </div>
        </div>

        <!-- Benefit 6: Scalability -->
        <div class="group p-8 rounded-2xl bg-gradient-to-br from-indigo-50 to-indigo-100 hover:from-indigo-100 hover:to-indigo-200 transition-all duration-300 hover:shadow-xl hover:-translate-y-2 animate-slide-up delay-1000">
          <div class="w-16 h-16 bg-gradient-to-br from-indigo-500 to-indigo-600 rounded-2xl flex items-center justify-center mb-6 group-hover:scale-110 transition-transform duration-300">
            <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 12l3-3 3 3 4-4M8 21l4-4 4 4M3 4h18M4 4h16v12a1 1 0 01-1 1H5a1 1 0 01-1-1V4z"/>
            </svg>
          </div>
          <h3 class="text-2xl font-bold text-gray-900 mb-4">Безграничный масштаб</h3>
          <p class="text-gray-600 leading-relaxed">
            Создавайте курсы на любые темы в любых количествах. Идеально для компаний, школ и образовательных центров.
          </p>
          <div class="mt-4 text-indigo-600 font-semibold">
            📈 Растите без ограничений
          </div>
        </div>
      </div>

      <!-- Call to action -->
      <div class="text-center animate-fade-in delay-1200">
        <div class="bg-gradient-to-r from-blue-600 to-purple-600 rounded-3xl p-12 text-white">
          <h3 class="text-3xl font-bold mb-4">Готовы революционизировать обучение?</h3>
          <p class="text-xl mb-8 text-blue-100">
            Присоединяйтесь к тысячам пользователей, которые уже экономят время и деньги
          </p>
          <router-link 
            to="/register" 
            class="inline-flex items-center px-8 py-4 bg-white text-blue-600 font-bold text-lg rounded-2xl hover:bg-gray-100 transition-all duration-300 hover:scale-105 shadow-lg"
          >
            Начать бесплатно
            <svg class="w-5 h-5 ml-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"/>
            </svg>
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
</style>
