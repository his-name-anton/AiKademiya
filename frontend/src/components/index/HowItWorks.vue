<template>
  <section class="py-24 bg-white dark:bg-gray-900 transition-colors duration-300">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <!-- Section header -->
      <div class="text-center mb-20">
        <h2 class="text-4xl md:text-5xl font-bold text-gray-900 dark:text-white mb-6">
          Как работает <span class="bg-gradient-to-r from-blue-600 to-purple-600 dark:from-blue-400 dark:to-purple-400 bg-clip-text text-transparent">AI-обучение</span>
        </h2>
        <p class="text-xl text-gray-600 dark:text-gray-300 max-w-3xl mx-auto">
          Всего за 3 простых шага от любопытства до знаний
        </p>
      </div>

      <!-- Steps -->
      <div class="grid lg:grid-cols-3 gap-12 lg:gap-8 mb-20">
        <!-- Step 1: Tell us what you want to learn -->
        <div class="text-center group">
          <div class="relative mb-8">
            <!-- Step number -->
            <div class="w-20 h-20 bg-gradient-to-br from-blue-500 to-indigo-600 dark:from-blue-400 dark:to-indigo-500 rounded-full flex items-center justify-center mx-auto mb-6 group-hover:scale-110 transition-transform duration-300 shadow-lg">
              <span class="text-2xl font-bold text-white">1</span>
            </div>
            <!-- Icon -->
            <div class="absolute -bottom-2 left-1/2 transform -translate-x-1/2 w-12 h-12 bg-blue-100 dark:bg-blue-900/50 rounded-full flex items-center justify-center border-4 border-white dark:border-gray-900 shadow-lg">
              <svg class="w-6 h-6 text-blue-600 dark:text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"/>
              </svg>
            </div>
          </div>
          <h3 class="text-2xl font-bold text-gray-900 dark:text-white mb-4">Расскажите, что хотите изучить</h3>
          <p class="text-gray-600 dark:text-gray-300 leading-relaxed mb-6">
            Просто опишите тему своими словами. Хотите изучить Python? Научиться готовить суши? Понять квантовую физику? AI поймёт любой запрос.
          </p>
          <div class="bg-gray-50 dark:bg-gray-800 rounded-xl p-4 border border-gray-200 dark:border-gray-700">
            <div class="text-sm text-gray-500 dark:text-gray-400 mb-2">Пример:</div>
            <div class="text-gray-900 dark:text-white font-medium">"Хочу научиться фотографировать портреты для начинающих"</div>
          </div>
        </div>

        <!-- Arrow -->
        <div class="hidden lg:flex items-start justify-center pt-10">
          <svg class="w-8 h-8 text-gray-300 dark:text-gray-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"/>
          </svg>
        </div>

        <!-- Step 2: AI creates your personal course -->
        <div class="text-center group">
          <div class="relative mb-8">
            <!-- Step number -->
            <div class="w-20 h-20 bg-gradient-to-br from-purple-500 to-pink-600 dark:from-purple-400 dark:to-pink-500 rounded-full flex items-center justify-center mx-auto mb-6 group-hover:scale-110 transition-transform duration-300 shadow-lg">
              <span class="text-2xl font-bold text-white">2</span>
            </div>
            <!-- Icon -->
            <div class="absolute -bottom-2 left-1/2 transform -translate-x-1/2 w-12 h-12 bg-purple-100 dark:bg-purple-900/50 rounded-full flex items-center justify-center border-4 border-white dark:border-gray-900 shadow-lg">
              <svg class="w-6 h-6 text-purple-600 dark:text-purple-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z"/>
              </svg>
            </div>
          </div>
          <h3 class="text-2xl font-bold text-gray-900 dark:text-white mb-4">AI создаёт ваш курс</h3>
          <p class="text-gray-600 dark:text-gray-300 leading-relaxed mb-6">
            Искусственный интеллект анализирует ваш запрос, определяет ваш уровень и создаёт персональный учебный план с уроками, тестами и практическими заданиями.
          </p>
          <div class="space-y-3">
            <div class="flex items-center justify-center gap-2 text-sm text-green-600 dark:text-green-400">
              <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
                <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/>
              </svg>
              Адаптация под ваш уровень
            </div>
            <div class="flex items-center justify-center gap-2 text-sm text-blue-600 dark:text-blue-400">
              <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
                <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/>
              </svg>
              Структурированные уроки
            </div>
            <div class="flex items-center justify-center gap-2 text-sm text-purple-600 dark:text-purple-400">
              <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
                <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/>
              </svg>
              Интерактивные тесты
            </div>
          </div>
        </div>

        <!-- Arrow -->
        <div class="hidden lg:flex items-start justify-center pt-10">
          <svg class="w-8 h-8 text-gray-300 dark:text-gray-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"/>
          </svg>
        </div>

        <!-- Step 3: Learn and achieve your goals -->
        <div class="text-center group">
          <div class="relative mb-8">
            <!-- Step number -->
            <div class="w-20 h-20 bg-gradient-to-br from-green-500 to-emerald-600 dark:from-green-400 dark:to-emerald-500 rounded-full flex items-center justify-center mx-auto mb-6 group-hover:scale-110 transition-transform duration-300 shadow-lg">
              <span class="text-2xl font-bold text-white">3</span>
            </div>
            <!-- Icon -->
            <div class="absolute -bottom-2 left-1/2 transform -translate-x-1/2 w-12 h-12 bg-green-100 dark:bg-green-900/50 rounded-full flex items-center justify-center border-4 border-white dark:border-gray-900 shadow-lg">
              <svg class="w-6 h-6 text-green-600 dark:text-green-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
              </svg>
            </div>
          </div>
          <h3 class="text-2xl font-bold text-gray-900 dark:text-white mb-4">Учитесь и достигайте целей</h3>
          <p class="text-gray-600 dark:text-gray-300 leading-relaxed mb-6">
            Проходите уроки в удобном темпе, задавайте вопросы AI-наставнику и получайте мгновенные ответы. Отслеживайте прогресс и празднуйте достижения.
          </p>
          <div class="bg-gradient-to-r from-green-50 to-emerald-50 dark:from-green-900/20 dark:to-emerald-900/20 rounded-xl p-4 border border-green-200 dark:border-green-800">
            <div class="text-green-700 dark:text-green-300 font-medium">Средний результат:</div>
            <div class="text-green-900 dark:text-green-100 font-bold text-lg">Освоение навыка за 2-4 недели</div>
          </div>
        </div>
      </div>

      <!-- Demo preview -->
      <div class="bg-gradient-to-r from-gray-50 to-white dark:from-gray-800 dark:to-gray-700 rounded-3xl p-8 lg:p-12 border border-gray-200 dark:border-gray-600">
        <div class="text-center mb-8">
          <h3 class="text-3xl font-bold text-gray-900 dark:text-white mb-4">Посмотрите, как это выглядит</h3>
          <p class="text-gray-600 dark:text-gray-300">Пример созданного AI курса по фотографии</p>
        </div>
        
        <!-- Mock course interface -->
        <div class="max-w-4xl mx-auto">
          <div class="bg-white dark:bg-gray-800 rounded-2xl shadow-xl border border-gray-200 dark:border-gray-600 overflow-hidden">
            <!-- Header -->
            <div class="bg-gradient-to-r from-blue-600 to-purple-600 dark:from-blue-500 dark:to-purple-500 px-6 py-4">
              <div class="flex items-center gap-3">
                <div class="w-8 h-8 bg-white/20 rounded-lg flex items-center justify-center">
                  <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 9a2 2 0 012-2h.93a2 2 0 001.664-.89l.812-1.22A2 2 0 0110.07 4h3.86a2 2 0 011.664.89l.812 1.22A2 2 0 0018.07 7H19a2 2 0 012 2v9a2 2 0 01-2 2H5a2 2 0 01-2-2V9z"/>
                  </svg>
                </div>
                <div>
                  <h4 class="text-white font-semibold">Основы портретной фотографии</h4>
                  <p class="text-blue-100 text-sm">Персональный курс от AI</p>
                </div>
              </div>
            </div>
            
            <!-- Content -->
            <div class="p-6">
              <div class="grid md:grid-cols-2 gap-6">
                <!-- Lessons list -->
                <div>
                  <h5 class="font-semibold text-gray-900 dark:text-white mb-4">Уроки курса:</h5>
                  <div class="space-y-3">
                    <div class="flex items-center gap-3 p-3 bg-green-50 dark:bg-green-900/20 rounded-lg border border-green-200 dark:border-green-800">
                      <div class="w-6 h-6 bg-green-500 rounded-full flex items-center justify-center">
                        <svg class="w-3 h-3 text-white" fill="currentColor" viewBox="0 0 20 20">
                          <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/>
                        </svg>
                      </div>
                      <span class="text-gray-700 dark:text-gray-300">Основы композиции</span>
                    </div>
                    <div class="flex items-center gap-3 p-3 bg-blue-50 dark:bg-blue-900/20 rounded-lg border border-blue-200 dark:border-blue-800">
                      <div class="w-6 h-6 bg-blue-500 rounded-full flex items-center justify-center">
                        <span class="text-white text-xs font-bold">2</span>
                      </div>
                      <span class="text-gray-700 dark:text-gray-300">Работа с освещением</span>
                    </div>
                    <div class="flex items-center gap-3 p-3 bg-gray-50 dark:bg-gray-700 rounded-lg border border-gray-200 dark:border-gray-600">
                      <div class="w-6 h-6 bg-gray-300 dark:bg-gray-600 rounded-full flex items-center justify-center">
                        <span class="text-gray-600 dark:text-gray-400 text-xs font-bold">3</span>
                      </div>
                      <span class="text-gray-500 dark:text-gray-400">Настройки камеры</span>
                    </div>
                  </div>
                </div>
                
                <!-- AI Chat -->
                <div>
                  <h5 class="font-semibold text-gray-900 dark:text-white mb-4">AI-наставник всегда на связи:</h5>
                  <div class="bg-gray-50 dark:bg-gray-700 rounded-lg p-4 border border-gray-200 dark:border-gray-600">
                    <div class="space-y-3">
                      <div class="flex gap-3">
                        <div class="w-8 h-8 bg-blue-500 rounded-full flex items-center justify-center">
                          <svg class="w-4 h-4 text-white" fill="currentColor" viewBox="0 0 20 20">
                            <path fill-rule="evenodd" d="M12.395 2.553a1 1 0 00-1.45-.385c-.345.23-.614.558-.822.88-.214.33-.403.713-.57 1.116-.334.804-.614 1.768-.84 2.734a31.365 31.365 0 00-.613 3.58 2.64 2.64 0 01-.945-1.067c-.328-.68-.398-1.534-.398-2.654A1 1 0 005.05 6.05 6.981 6.981 0 003 11a7 7 0 1011.95-4.95c-.592-.591-.98-.985-1.348-1.467-.363-.476-.724-1.063-1.207-2.03zM12.12 15.12A3 3 0 017 13s.879.5 2.5.5c0-1 .5-4 1.25-4.5.5 1 .786 1.293 1.371 1.879A2.99 2.99 0 0113 13a2.99 2.99 0 01-.879 2.121z" clip-rule="evenodd"/>
                          </svg>
                        </div>
                        <div class="bg-white dark:bg-gray-600 rounded-lg p-3 text-sm text-gray-700 dark:text-gray-200">
                          Отлично! Вы освоили основы композиции. Хотите узнать о правиле третей подробнее?
                        </div>
                      </div>
                      <div class="flex gap-3 justify-end">
                        <div class="bg-blue-500 text-white rounded-lg p-3 text-sm max-w-xs">
                          Да, расскажите про правило третей!
                        </div>
                        <div class="w-8 h-8 bg-gray-300 dark:bg-gray-600 rounded-full"></div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
/* Smooth animations will be handled by Tailwind classes */
</style>