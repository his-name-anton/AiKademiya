<template>
  <section class="py-24 bg-gray-50 dark:bg-gray-800/50 transition-colors duration-300">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <!-- Section header -->
      <div class="text-center mb-20">
        <h2 class="text-4xl md:text-5xl font-bold text-gray-900 dark:text-white mb-6">
          Истории успеха наших <span class="bg-gradient-to-r from-blue-600 to-purple-600 dark:from-blue-400 dark:to-purple-400 bg-clip-text text-transparent">студентов</span>
        </h2>
        <p class="text-xl text-gray-600 dark:text-gray-300 max-w-3xl mx-auto">
          Реальные люди, реальные результаты, реальные истории изменений
        </p>
      </div>

      <!-- Testimonials grid -->
      <div class="grid lg:grid-cols-3 md:grid-cols-2 gap-8 mb-16">
        <!-- Student 1: Career Change -->
        <div class="group relative bg-white dark:bg-gray-800 rounded-2xl p-8 shadow-sm hover:shadow-xl transition-all duration-500 hover:-translate-y-2 border border-gray-100 dark:border-gray-700">
          <div class="absolute inset-0 bg-gradient-to-br from-blue-50 to-indigo-50 dark:from-blue-900/20 dark:to-indigo-900/20 rounded-2xl opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
          <div class="relative">
            <!-- Quote -->
            <div class="mb-6">
              <svg class="w-8 h-8 text-blue-500 dark:text-blue-400 mb-4" fill="currentColor" viewBox="0 0 24 24">
                <path d="M14.017 21v-7.391c0-5.704 3.731-9.57 8.983-10.609l.995 2.151c-2.432.917-3.995 3.638-3.995 5.849h4v10h-9.983zm-14.017 0v-7.391c0-5.704 3.748-9.57 9-10.609l.996 2.151c-2.433.917-3.996 3.638-3.996 5.849h4v10h-10z"/>
              </svg>
              <p class="text-gray-700 dark:text-gray-300 leading-relaxed mb-6">
                "За 3 месяца изучила веб-разработку с нуля и получила работу junior frontend разработчика. AI-курсы адаптировались под мой график работы мамы двоих детей."
              </p>
            </div>
            
            <!-- Profile -->
            <div class="flex items-center gap-4">
              <div class="w-12 h-12 bg-gradient-to-br from-blue-400 to-blue-600 rounded-full flex items-center justify-center">
                <span class="text-white font-bold">МС</span>
              </div>
              <div>
                <h4 class="font-semibold text-gray-900 dark:text-white">Мария Соколова</h4>
                <p class="text-sm text-gray-500 dark:text-gray-400">Веб-разработчик в IT-стартапе</p>
              </div>
            </div>
            
            <!-- Course badge -->
            <div class="mt-4 inline-flex items-center gap-2 px-3 py-1 bg-blue-100 dark:bg-blue-900/30 text-blue-700 dark:text-blue-300 text-sm rounded-full">
              <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
                <path fill-rule="evenodd" d="M12.395 2.553a1 1 0 00-1.45-.385c-.345.23-.614.558-.822.88-.214.33-.403.713-.57 1.116-.334.804-.614 1.768-.84 2.734a31.365 31.365 0 00-.613 3.58 2.64 2.64 0 01-.945-1.067c-.328-.68-.398-1.534-.398-2.654A1 1 0 005.05 6.05 6.981 6.981 0 003 11a7 7 0 1011.95-4.95c-.592-.591-.98-.985-1.348-1.467-.363-.476-.724-1.063-1.207-2.03zM12.12 15.12A3 3 0 017 13s.879.5 2.5.5c0-1 .5-4 1.25-4.5.5 1 .786 1.293 1.371 1.879A2.99 2.99 0 0113 13a2.99 2.99 0 01-.879 2.121z" clip-rule="evenodd"/>
              </svg>
              Веб-разработка для начинающих
            </div>
          </div>
        </div>

        <!-- Student 2: Skill Upgrade -->
        <div class="group relative bg-white dark:bg-gray-800 rounded-2xl p-8 shadow-sm hover:shadow-xl transition-all duration-500 hover:-translate-y-2 border border-gray-100 dark:border-gray-700">
          <div class="absolute inset-0 bg-gradient-to-br from-green-50 to-emerald-50 dark:from-green-900/20 dark:to-emerald-900/20 rounded-2xl opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
          <div class="relative">
            <!-- Quote -->
            <div class="mb-6">
              <svg class="w-8 h-8 text-green-500 dark:text-green-400 mb-4" fill="currentColor" viewBox="0 0 24 24">
                <path d="M14.017 21v-7.391c0-5.704 3.731-9.57 8.983-10.609l.995 2.151c-2.432.917-3.995 3.638-3.995 5.849h4v10h-9.983zm-14.017 0v-7.391c0-5.704 3.748-9.57 9-10.609l.996 2.151c-2.433.917-3.996 3.638-3.996 5.849h4v10h-10z"/>
              </svg>
              <p class="text-gray-700 dark:text-gray-300 leading-relaxed mb-6">
                "Освоил Data Science и машинное обучение. Получил повышение и теперь возглавляю отдел аналитики. AI понимал мои вопросы лучше, чем преподаватели в вузе."
              </p>
            </div>
            
            <!-- Profile -->
            <div class="flex items-center gap-4">
              <div class="w-12 h-12 bg-gradient-to-br from-green-400 to-green-600 rounded-full flex items-center justify-center">
                <span class="text-white font-bold">АП</span>
              </div>
              <div>
                <h4 class="font-semibold text-gray-900 dark:text-white">Алексей Петров</h4>
                <p class="text-sm text-gray-500 dark:text-gray-400">Руководитель отдела аналитики</p>
              </div>
            </div>
            
            <!-- Course badge -->
            <div class="mt-4 inline-flex items-center gap-2 px-3 py-1 bg-green-100 dark:bg-green-900/30 text-green-700 dark:text-green-300 text-sm rounded-full">
              <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
                <path fill-rule="evenodd" d="M12.395 2.553a1 1 0 00-1.45-.385c-.345.23-.614.558-.822.88-.214.33-.403.713-.57 1.116-.334.804-.614 1.768-.84 2.734a31.365 31.365 0 00-.613 3.58 2.64 2.64 0 01-.945-1.067c-.328-.68-.398-1.534-.398-2.654A1 1 0 005.05 6.05 6.981 6.981 0 003 11a7 7 0 1011.95-4.95c-.592-.591-.98-.985-1.348-1.467-.363-.476-.724-1.063-1.207-2.03zM12.12 15.12A3 3 0 017 13s.879.5 2.5.5c0-1 .5-4 1.25-4.5.5 1 .786 1.293 1.371 1.879A2.99 2.99 0 0113 13a2.99 2.99 0 01-.879 2.121z" clip-rule="evenodd"/>
              </svg>
              Data Science с нуля
            </div>
          </div>
        </div>

        <!-- Student 3: Personal Interest -->
        <div class="group relative bg-white dark:bg-gray-800 rounded-2xl p-8 shadow-sm hover:shadow-xl transition-all duration-500 hover:-translate-y-2 border border-gray-100 dark:border-gray-700">
          <div class="absolute inset-0 bg-gradient-to-br from-purple-50 to-pink-50 dark:from-purple-900/20 dark:to-pink-900/20 rounded-2xl opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
          <div class="relative">
            <!-- Quote -->
            <div class="mb-6">
              <svg class="w-8 h-8 text-purple-500 dark:text-purple-400 mb-4" fill="currentColor" viewBox="0 0 24 24">
                <path d="M14.017 21v-7.391c0-5.704 3.731-9.57 8.983-10.609l.995 2.151c-2.432.917-3.995 3.638-3.995 5.849h4v10h-9.983zm-14.017 0v-7.391c0-5.704 3.748-9.57 9-10.609l.996 2.151c-2.433.917-3.996 3.638-3.996 5.849h4v10h-10z"/>
              </svg>
              <p class="text-gray-700 dark:text-gray-300 leading-relaxed mb-6">
                "Всегда мечтала играть на фортепиано. За полгода научилась играть любимые мелодии. AI создавал упражнения именно для моих проблемных мест."
              </p>
            </div>
            
            <!-- Profile -->
            <div class="flex items-center gap-4">
              <div class="w-12 h-12 bg-gradient-to-br from-purple-400 to-purple-600 rounded-full flex items-center justify-center">
                <span class="text-white font-bold">ЕК</span>
              </div>
              <div>
                <h4 class="font-semibold text-gray-900 dark:text-white">Елена Кузнецова</h4>
                <p class="text-sm text-gray-500 dark:text-gray-400">Врач, хобби-пианистка</p>
              </div>
            </div>
            
            <!-- Course badge -->
            <div class="mt-4 inline-flex items-center gap-2 px-3 py-1 bg-purple-100 dark:bg-purple-900/30 text-purple-700 dark:text-purple-300 text-sm rounded-full">
              <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
                <path fill-rule="evenodd" d="M12.395 2.553a1 1 0 00-1.45-.385c-.345.23-.614.558-.822.88-.214.33-.403.713-.57 1.116-.334.804-.614 1.768-.84 2.734a31.365 31.365 0 00-.613 3.58 2.64 2.64 0 01-.945-1.067c-.328-.68-.398-1.534-.398-2.654A1 1 0 005.05 6.05 6.981 6.981 0 003 11a7 7 0 1011.95-4.95c-.592-.591-.98-.985-1.348-1.467-.363-.476-.724-1.063-1.207-2.03zM12.12 15.12A3 3 0 017 13s.879.5 2.5.5c0-1 .5-4 1.25-4.5.5 1 .786 1.293 1.371 1.879A2.99 2.99 0 0113 13a2.99 2.99 0 01-.879 2.121z" clip-rule="evenodd"/>
              </svg>
              Фортепиано для взрослых
            </div>
          </div>
        </div>

        <!-- Student 4: Language Learning -->
        <div class="group relative bg-white dark:bg-gray-800 rounded-2xl p-8 shadow-sm hover:shadow-xl transition-all duration-500 hover:-translate-y-2 border border-gray-100 dark:border-gray-700">
          <div class="absolute inset-0 bg-gradient-to-br from-orange-50 to-red-50 dark:from-orange-900/20 dark:to-red-900/20 rounded-2xl opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
          <div class="relative">
            <!-- Quote -->
            <div class="mb-6">
              <svg class="w-8 h-8 text-orange-500 dark:text-orange-400 mb-4" fill="currentColor" viewBox="0 0 24 24">
                <path d="M14.017 21v-7.391c0-5.704 3.731-9.57 8.983-10.609l.995 2.151c-2.432.917-3.995 3.638-3.995 5.849h4v10h-9.983zm-14.017 0v-7.391c0-5.704 3.748-9.57 9-10.609l.996 2.151c-2.433.917-3.996 3.638-3.996 5.849h4v10h-10z"/>
              </svg>
              <p class="text-gray-700 dark:text-gray-300 leading-relaxed mb-6">
                "Выучил японский за 8 месяцев и теперь работаю в Токио! AI адаптировал курс под мой стиль обучения и помогал с произношением."
              </p>
            </div>
            
            <!-- Profile -->
            <div class="flex items-center gap-4">
              <div class="w-12 h-12 bg-gradient-to-br from-orange-400 to-red-600 rounded-full flex items-center justify-center">
                <span class="text-white font-bold">ДИ</span>
              </div>
              <div>
                <h4 class="font-semibold text-gray-900 dark:text-white">Дмитрий Иванов</h4>
                <p class="text-sm text-gray-500 dark:text-gray-400">IT-консультант в Японии</p>
              </div>
            </div>
            
            <!-- Course badge -->
            <div class="mt-4 inline-flex items-center gap-2 px-3 py-1 bg-orange-100 dark:bg-orange-900/30 text-orange-700 dark:text-orange-300 text-sm rounded-full">
              <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
                <path fill-rule="evenodd" d="M12.395 2.553a1 1 0 00-1.45-.385c-.345.23-.614.558-.822.88-.214.33-.403.713-.57 1.116-.334.804-.614 1.768-.84 2.734a31.365 31.365 0 00-.613 3.58 2.64 2.64 0 01-.945-1.067c-.328-.68-.398-1.534-.398-2.654A1 1 0 005.05 6.05 6.981 6.981 0 003 11a7 7 0 1011.95-4.95c-.592-.591-.98-.985-1.348-1.467-.363-.476-.724-1.063-1.207-2.03zM12.12 15.12A3 3 0 717 13s.879.5 2.5.5c0-1 .5-4 1.25-4.5.5 1 .786 1.293 1.371 1.879A2.99 2.99 0 0113 13a2.99 2.99 0 01-.879 2.121z" clip-rule="evenodd"/>
              </svg>
              Японский язык
            </div>
          </div>
        </div>

        <!-- Student 5: Creative Skills -->
        <div class="group relative bg-white dark:bg-gray-800 rounded-2xl p-8 shadow-sm hover:shadow-xl transition-all duration-500 hover:-translate-y-2 border border-gray-100 dark:border-gray-700">
          <div class="absolute inset-0 bg-gradient-to-br from-cyan-50 to-blue-50 dark:from-cyan-900/20 dark:to-blue-900/20 rounded-2xl opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
          <div class="relative">
            <!-- Quote -->
            <div class="mb-6">
              <svg class="w-8 h-8 text-cyan-500 dark:text-cyan-400 mb-4" fill="currentColor" viewBox="0 0 24 24">
                <path d="M14.017 21v-7.391c0-5.704 3.731-9.57 8.983-10.609l.995 2.151c-2.432.917-3.995 3.638-3.995 5.849h4v10h-9.983zm-14.017 0v-7.391c0-5.704 3.748-9.57 9-10.609l.996 2.151c-2.433.917-3.996 3.638-3.996 5.849h4v10h-10z"/>
              </svg>
              <p class="text-gray-700 dark:text-gray-300 leading-relaxed mb-6">
                "Научилась создавать потрясающие фотографии и теперь это мой дополнительный источник дохода. AI помог найти свой уникальный стиль."
              </p>
            </div>
            
            <!-- Profile -->
            <div class="flex items-center gap-4">
              <div class="w-12 h-12 bg-gradient-to-br from-cyan-400 to-blue-600 rounded-full flex items-center justify-center">
                <span class="text-white font-bold">АР</span>
              </div>
              <div>
                <h4 class="font-semibold text-gray-900 dark:text-white">Анна Романова</h4>
                <p class="text-sm text-gray-500 dark:text-gray-400">Фотограф-фрилансер</p>
              </div>
            </div>
            
            <!-- Course badge -->
            <div class="mt-4 inline-flex items-center gap-2 px-3 py-1 bg-cyan-100 dark:bg-cyan-900/30 text-cyan-700 dark:text-cyan-300 text-sm rounded-full">
              <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
                <path fill-rule="evenodd" d="M12.395 2.553a1 1 0 00-1.45-.385c-.345.23-.614.558-.822.88-.214.33-.403.713-.57 1.116-.334.804-.614 1.768-.84 2.734a31.365 31.365 0 00-.613 3.58 2.64 2.64 0 01-.945-1.067c-.328-.68-.398-1.534-.398-2.654A1 1 0 005.05 6.05 6.981 6.981 0 003 11a7 7 0 1011.95-4.95c-.592-.591-.98-.985-1.348-1.467-.363-.476-.724-1.063-1.207-2.03zM12.12 15.12A3 3 0 717 13s.879.5 2.5.5c0-1 .5-4 1.25-4.5.5 1 .786 1.293 1.371 1.879A2.99 2.99 0 0113 13a2.99 2.99 0 01-.879 2.121z" clip-rule="evenodd"/>
              </svg>
              Художественная фотография
            </div>
          </div>
        </div>

        <!-- Student 6: Business Skills -->
        <div class="group relative bg-white dark:bg-gray-800 rounded-2xl p-8 shadow-sm hover:shadow-xl transition-all duration-500 hover:-translate-y-2 border border-gray-100 dark:border-gray-700">
          <div class="absolute inset-0 bg-gradient-to-br from-teal-50 to-green-50 dark:from-teal-900/20 dark:to-green-900/20 rounded-2xl opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
          <div class="relative">
            <!-- Quote -->
            <div class="mb-6">
              <svg class="w-8 h-8 text-teal-500 dark:text-teal-400 mb-4" fill="currentColor" viewBox="0 0 24 24">
                <path d="M14.017 21v-7.391c0-5.704 3.731-9.57 8.983-10.609l.995 2.151c-2.432.917-3.995 3.638-3.995 5.849h4v10h-9.983zm-14.017 0v-7.391c0-5.704 3.748-9.57 9-10.609l.996 2.151c-2.433.917-3.996 3.638-3.996 5.849h4v10h-10z"/>
              </svg>
              <p class="text-gray-700 dark:text-gray-300 leading-relaxed mb-6">
                "Освоил digital-маркетинг и запустил свой онлайн-магазин. За год вышел на 500к рублей в месяц. AI учил именно тому, что работает."
              </p>
            </div>
            
            <!-- Profile -->
            <div class="flex items-center gap-4">
              <div class="w-12 h-12 bg-gradient-to-br from-teal-400 to-green-600 rounded-full flex items-center justify-center">
                <span class="text-white font-bold">СТ</span>
              </div>
              <div>
                <h4 class="font-semibold text-gray-900 dark:text-white">Сергей Титов</h4>
                <p class="text-sm text-gray-500 dark:text-gray-400">Владелец интернет-магазина</p>
              </div>
            </div>
            
            <!-- Course badge -->
            <div class="mt-4 inline-flex items-center gap-2 px-3 py-1 bg-teal-100 dark:bg-teal-900/30 text-teal-700 dark:text-teal-300 text-sm rounded-full">
              <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
                <path fill-rule="evenodd" d="M12.395 2.553a1 1 0 00-1.45-.385c-.345.23-.614.558-.822.88-.214.33-.403.713-.57 1.116-.334.804-.614 1.768-.84 2.734a31.365 31.365 0 00-.613 3.58 2.64 2.64 0 01-.945-1.067c-.328-.68-.398-1.534-.398-2.654A1 1 0 005.05 6.05 6.981 6.981 0 003 11a7 7 0 1011.95-4.95c-.592-.591-.98-.985-1.348-1.467-.363-.476-.724-1.063-1.207-2.03zM12.12 15.12A3 3 0 717 13s.879.5 2.5.5c0-1 .5-4 1.25-4.5.5 1 .786 1.293 1.371 1.879A2.99 2.99 0 0113 13a2.99 2.99 0 01-.879 2.121z" clip-rule="evenodd"/>
              </svg>
              Digital-маркетинг
            </div>
          </div>
        </div>
      </div>

      <!-- CTA Section -->
      <div class="text-center bg-gradient-to-r from-blue-600 via-purple-600 to-indigo-600 dark:from-blue-500 dark:via-purple-500 dark:to-indigo-500 rounded-3xl p-12">
        <h3 class="text-3xl md:text-4xl font-bold text-white mb-4">
          Ваша история успеха начинается сегодня
        </h3>
        <p class="text-xl text-blue-100 mb-8 max-w-2xl mx-auto">
          Присоединяйтесь к тысячам студентов, которые уже изменили свою жизнь с помощью AI-образования
        </p>
        <div class="flex flex-col sm:flex-row gap-4 justify-center">
          <router-link 
            to="/register"
            class="inline-flex items-center gap-2 px-8 py-4 bg-white text-blue-600 font-semibold text-lg rounded-xl hover:bg-gray-50 transition-all duration-300 hover:scale-105 shadow-lg"
          >
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/>
            </svg>
            Начать бесплатно
          </router-link>
          <button class="px-8 py-4 bg-white/10 backdrop-blur-sm border-2 border-white/30 text-white font-semibold text-lg rounded-xl hover:bg-white/20 transition-all duration-300 hover:scale-105">
            Посмотреть больше историй
          </button>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
/* Smooth animations will be handled by Tailwind classes */
</style> 