<template>
  <section class="py-24 bg-white dark:bg-gray-900 transition-colors duration-300">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <!-- Main CTA -->
      <div class="relative">
        <!-- Background elements -->
        <div class="absolute inset-0 bg-gradient-to-r from-blue-600 via-purple-600 to-indigo-600 dark:from-blue-500 dark:via-purple-500 dark:to-indigo-500 rounded-3xl transform -rotate-1"></div>
        <div class="relative bg-gradient-to-r from-blue-600 via-purple-600 to-indigo-600 dark:from-blue-500 dark:via-purple-500 dark:to-indigo-500 rounded-3xl p-12 lg:p-16 text-white">
          <!-- Background decoration -->
          <div class="absolute inset-0 overflow-hidden rounded-3xl">
            <div class="absolute -top-40 -right-40 w-80 h-80 bg-white/10 rounded-full blur-3xl"></div>
            <div class="absolute -bottom-40 -left-40 w-80 h-80 bg-white/10 rounded-full blur-3xl"></div>
          </div>
          
          <div class="relative text-center">
            <!-- Icon -->
            <div class="w-20 h-20 bg-white/20 backdrop-blur-sm rounded-2xl flex items-center justify-center mx-auto mb-8">
              <svg class="w-10 h-10 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z"/>
              </svg>
            </div>

            <!-- Heading -->
            <h2 class="text-4xl md:text-6xl font-bold mb-6">
              Начните учиться уже сегодня
            </h2>
            
            <!-- Subheading -->
            <p class="text-xl md:text-2xl text-blue-100 mb-12 max-w-3xl mx-auto leading-relaxed">
              Искусственный интеллект создаст персональный курс специально для вас. 
              <span class="text-white font-semibold">Первая неделя абсолютно бесплатна</span> — без обязательств и скрытых платежей.
            </p>

            <!-- Features list -->
            <div class="grid md:grid-cols-3 gap-6 mb-12">
              <div class="flex items-center gap-3 justify-center md:justify-start">
                <div class="w-8 h-8 bg-green-500 rounded-full flex items-center justify-center flex-shrink-0">
                  <svg class="w-4 h-4 text-white" fill="currentColor" viewBox="0 0 20 20">
                    <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/>
                  </svg>
                </div>
                <span class="text-blue-100 font-medium">7 дней бесплатно</span>
              </div>
              <div class="flex items-center gap-3 justify-center md:justify-start">
                <div class="w-8 h-8 bg-green-500 rounded-full flex items-center justify-center flex-shrink-0">
                  <svg class="w-4 h-4 text-white" fill="currentColor" viewBox="0 0 20 20">
                    <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/>
                  </svg>
                </div>
                <span class="text-blue-100 font-medium">Отмена в любой момент</span>
              </div>
              <div class="flex items-center gap-3 justify-center md:justify-start">
                <div class="w-8 h-8 bg-green-500 rounded-full flex items-center justify-center flex-shrink-0">
                  <svg class="w-4 h-4 text-white" fill="currentColor" viewBox="0 0 20 20">
                    <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/>
                  </svg>
                </div>
                <span class="text-blue-100 font-medium">AI-персонализация</span>
              </div>
            </div>

            <!-- CTA Buttons -->
            <div class="flex flex-col sm:flex-row gap-4 justify-center mb-8">
              <router-link 
                to="/register"
                class="group inline-flex items-center gap-3 px-10 py-5 bg-white text-blue-600 font-bold text-xl rounded-2xl hover:bg-gray-50 transition-all duration-300 hover:scale-105 shadow-xl"
              >
                <svg class="w-6 h-6 group-hover:translate-x-1 transition-transform duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/>
                </svg>
                Попробовать бесплатно
              </router-link>
              
              <button class="group inline-flex items-center gap-3 px-10 py-5 bg-white/10 backdrop-blur-sm border-2 border-white/30 text-white font-bold text-xl rounded-2xl hover:bg-white/20 transition-all duration-300 hover:scale-105">
                <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 20 20">
                  <path d="M10 18a8 8 0 100-16 8 8 0 000 16zM9.555 7.168A1 1 0 008 8v4a1 1 0 001.555.832l3-2a1 1 0 000-1.664l-3-2z"/>
                </svg>
                Смотреть демо
              </button>
            </div>

            <!-- Trust indicators -->
            <div class="text-center text-blue-100 text-sm">
              <p class="mb-2">Уже доверяют 10,000+ студентов</p>
              <div class="flex justify-center items-center gap-1">
                <div class="flex text-yellow-400">
                  <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
                    <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/>
                  </svg>
                  <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
                    <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/>
                  </svg>
                  <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
                    <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/>
                  </svg>
                  <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
                    <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/>
                  </svg>
                  <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
                    <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/>
                  </svg>
                </div>
                <span class="ml-2">4.9 из 5 звёзд</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Secondary features -->
      <div class="mt-20 grid md:grid-cols-3 gap-8">
        <!-- Feature 1 -->
        <div class="text-center group">
          <div class="w-16 h-16 bg-gradient-to-br from-blue-500 to-indigo-600 dark:from-blue-400 dark:to-indigo-500 rounded-2xl flex items-center justify-center mx-auto mb-6 group-hover:scale-110 transition-transform duration-300">
            <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6V4m0 2a2 2 0 100 4m0-4a2 2 0 110 4m-6 8a2 2 0 100-4m0 4a2 2 0 100 4m0-4v2m0-6V4m6 6v10m6-2a2 2 0 100-4m0 4a2 2 0 100 4m0-4v2m0-6V4"/>
            </svg>
          </div>
          <h3 class="text-xl font-bold text-gray-900 dark:text-white mb-3">Индивидуальный подход</h3>
          <p class="text-gray-600 dark:text-gray-300">
            AI анализирует ваш стиль обучения и создаёт курс именно под вас
          </p>
        </div>

        <!-- Feature 2 -->
        <div class="text-center group">
          <div class="w-16 h-16 bg-gradient-to-br from-green-500 to-emerald-600 dark:from-green-400 dark:to-emerald-500 rounded-2xl flex items-center justify-center mx-auto mb-6 group-hover:scale-110 transition-transform duration-300">
            <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/>
            </svg>
          </div>
          <h3 class="text-xl font-bold text-gray-900 dark:text-white mb-3">Быстрые результаты</h3>
          <p class="text-gray-600 dark:text-gray-300">
            Большинство студентов видят прогресс уже в первую неделю обучения
          </p>
        </div>

        <!-- Feature 3 -->
        <div class="text-center group">
          <div class="w-16 h-16 bg-gradient-to-br from-purple-500 to-pink-600 dark:from-purple-400 dark:to-pink-500 rounded-2xl flex items-center justify-center mx-auto mb-6 group-hover:scale-110 transition-transform duration-300">
            <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"/>
            </svg>
          </div>
          <h3 class="text-xl font-bold text-gray-900 dark:text-white mb-3">24/7 поддержка</h3>
          <p class="text-gray-600 dark:text-gray-300">
            AI-наставник всегда готов ответить на вопросы и помочь с обучением
          </p>
        </div>
      </div>

      <!-- FAQ teaser -->
      <div class="mt-20 text-center">
        <h3 class="text-2xl font-bold text-gray-900 dark:text-white mb-4">Остались вопросы?</h3>
        <p class="text-gray-600 dark:text-gray-300 mb-8">
          Мы ответили на самые частые вопросы о нашей платформе
        </p>
        <div class="grid md:grid-cols-2 gap-6 max-w-4xl mx-auto">
          <!-- FAQ Item 1 -->
          <div class="bg-gray-50 dark:bg-gray-800 rounded-xl p-6 text-left">
            <h4 class="font-semibold text-gray-900 dark:text-white mb-2">Подойдёт ли мне, если я полный новичок?</h4>
            <p class="text-gray-600 dark:text-gray-300 text-sm">
              Конечно! AI определит ваш уровень и создаст курс с самых основ.
            </p>
          </div>
          
          <!-- FAQ Item 2 -->
          <div class="bg-gray-50 dark:bg-gray-800 rounded-xl p-6 text-left">
            <h4 class="font-semibold text-gray-900 dark:text-white mb-2">Сколько времени нужно уделять обучению?</h4>
            <p class="text-gray-600 dark:text-gray-300 text-sm">
              Всего 15-30 минут в день. AI адаптирует курс под ваш график.
            </p>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
/* Smooth animations will be handled by Tailwind classes */
</style> 