<template>
  <section class="py-20 bg-gray-50">
    <div class="container mx-auto px-4">
      <!-- Section header -->
      <div class="text-center mb-16 animate-fade-in">
        <h2 class="text-4xl md:text-5xl font-bold text-gray-900 mb-4">
          Что говорят наши 
          <span class="bg-gradient-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent">
            клиенты
          </span>
        </h2>
        <p class="text-xl text-gray-600 max-w-3xl mx-auto">
          Реальные истории успеха от компаний и экспертов, которые уже используют AiKademiya
        </p>
      </div>

      <!-- Testimonials grid -->
      <div class="grid lg:grid-cols-3 gap-8 mb-16">
        <!-- Testimonial 1: Corporate -->
        <div class="group bg-white rounded-3xl p-8 shadow-lg hover:shadow-2xl transition-all duration-300 hover:-translate-y-2 animate-slide-up border-l-4 border-blue-500">
          <div class="flex items-center mb-6">
            <div class="w-16 h-16 bg-gradient-to-br from-blue-500 to-blue-600 rounded-full flex items-center justify-center text-2xl font-bold text-white mr-4">
              МИ
            </div>
            <div>
              <div class="font-bold text-lg text-gray-900">Михаил Иванов</div>
              <div class="text-gray-600">Директор по обучению</div>
              <div class="text-sm text-blue-600 font-medium">FinTech Solutions</div>
            </div>
          </div>
          <div class="mb-6">
            <div class="flex text-yellow-400 mb-3">
              <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" v-for="i in 5" :key="i">
                <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/>
              </svg>
            </div>
          </div>
          <blockquote class="text-gray-700 italic mb-6 leading-relaxed">
            "Внедрили AiKademiya для корпоративного обучения. За 3 месяца создали 25 курсов по финансовой грамотности. 
            Сотрудники в восторге от качества материалов!"
          </blockquote>
          <div class="bg-blue-50 rounded-xl p-4">
            <div class="flex justify-between text-sm">
              <span class="text-gray-600">Курсов создано:</span>
              <span class="font-bold text-blue-600">25</span>
            </div>
            <div class="flex justify-between text-sm mt-1">
              <span class="text-gray-600">Экономия:</span>
              <span class="font-bold text-green-600">₽450,000</span>
            </div>
          </div>
        </div>

        <!-- Testimonial 2: Educational -->
        <div class="group bg-white rounded-3xl p-8 shadow-lg hover:shadow-2xl transition-all duration-300 hover:-translate-y-2 animate-slide-up delay-200 border-l-4 border-purple-500">
          <div class="flex items-center mb-6">
            <div class="w-16 h-16 bg-gradient-to-br from-purple-500 to-purple-600 rounded-full flex items-center justify-center text-2xl font-bold text-white mr-4">
              ЕП
            </div>
            <div>
              <div class="font-bold text-lg text-gray-900">Елена Петрова</div>
              <div class="text-gray-600">Методист</div>
              <div class="text-sm text-purple-600 font-medium">Онлайн-школа "Знание+"</div>
            </div>
          </div>
          <div class="mb-6">
            <div class="flex text-yellow-400 mb-3">
              <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" v-for="i in 5" :key="i">
                <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/>
              </svg>
            </div>
          </div>
          <blockquote class="text-gray-700 italic mb-6 leading-relaxed">
            "Как методист, я в восторге! ИИ создаёт структурированные курсы с логичной последовательностью. 
            Теперь могу сосредоточиться на педагогических нюансах."
          </blockquote>
          <div class="bg-purple-50 rounded-xl p-4">
            <div class="flex justify-between text-sm">
              <span class="text-gray-600">Курсов в месяц:</span>
              <span class="font-bold text-purple-600">12</span>
            </div>
            <div class="flex justify-between text-sm mt-1">
              <span class="text-gray-600">Время экономии:</span>
              <span class="font-bold text-green-600">80%</span>
            </div>
          </div>
        </div>

        <!-- Testimonial 3: Individual Expert -->
        <div class="group bg-white rounded-3xl p-8 shadow-lg hover:shadow-2xl transition-all duration-300 hover:-translate-y-2 animate-slide-up delay-400 border-l-4 border-green-500">
          <div class="flex items-center mb-6">
            <div class="w-16 h-16 bg-gradient-to-br from-green-500 to-green-600 rounded-full flex items-center justify-center text-2xl font-bold text-white mr-4">
              АВ
            </div>
            <div>
              <div class="font-bold text-lg text-gray-900">Алексей Волков</div>
              <div class="text-gray-600">IT-консультант</div>
              <div class="text-sm text-green-600 font-medium">Частный эксперт</div>
            </div>
          </div>
          <div class="mb-6">
            <div class="flex text-yellow-400 mb-3">
              <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" v-for="i in 5" :key="i">
                <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/>
              </svg>
            </div>
          </div>
          <blockquote class="text-gray-700 italic mb-6 leading-relaxed">
            "Запустил курс по Python за один вечер! Раньше на это уходило 2-3 недели. 
            Доход вырос в 4 раза благодаря возможности быстро создавать актуальные курсы."
          </blockquote>
          <div class="bg-green-50 rounded-xl p-4">
            <div class="flex justify-between text-sm">
              <span class="text-gray-600">Доход вырос:</span>
              <span class="font-bold text-green-600">в 4 раза</span>
            </div>
            <div class="flex justify-between text-sm mt-1">
              <span class="text-gray-600">Курсов создано:</span>
              <span class="font-bold text-blue-600">18</span>
            </div>
          </div>
        </div>
      </div>

      <!-- Company logos section -->
      <div class="animate-fade-in delay-600">
        <div class="text-center mb-12">
          <h3 class="text-2xl font-bold text-gray-900 mb-4">Нам доверяют ведущие компании</h3>
          <p class="text-gray-600">Присоединяйтесь к экосистеме успешных организаций</p>
        </div>
        
        <div class="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-6 gap-8 items-center opacity-60">
          <!-- Mock company logos -->
          <div class="bg-gray-200 rounded-xl h-16 flex items-center justify-center text-gray-500 font-bold">
            TechCorp
          </div>
          <div class="bg-gray-200 rounded-xl h-16 flex items-center justify-center text-gray-500 font-bold">
            EduCenter
          </div>
          <div class="bg-gray-200 rounded-xl h-16 flex items-center justify-center text-gray-500 font-bold">
            FinanceGroup
          </div>
          <div class="bg-gray-200 rounded-xl h-16 flex items-center justify-center text-gray-500 font-bold">
            IT-Academy
          </div>
          <div class="bg-gray-200 rounded-xl h-16 flex items-center justify-center text-gray-500 font-bold">
            StartupHub
          </div>
          <div class="bg-gray-200 rounded-xl h-16 flex items-center justify-center text-gray-500 font-bold">
            ProConsult
          </div>
        </div>
      </div>

      <!-- Video testimonial section -->
      <div class="mt-20 animate-fade-in delay-800">
        <div class="bg-gradient-to-r from-gray-900 to-gray-800 rounded-3xl p-12 text-white text-center">
          <h3 class="text-3xl font-bold mb-4">Видео-отзыв от клиента</h3>
          <p class="text-xl text-gray-300 mb-8">
            Узнайте, как компания "Цифровые решения" увеличила эффективность обучения на 300%
          </p>
          <div class="bg-gray-700/50 rounded-2xl p-8 max-w-2xl mx-auto border border-gray-600">
            <div class="w-20 h-20 bg-gradient-to-br from-blue-500 to-purple-600 rounded-full flex items-center justify-center mx-auto mb-4 cursor-pointer hover:scale-110 transition-transform duration-300">
              <svg class="w-8 h-8 text-white" fill="currentColor" viewBox="0 0 20 20">
                <path d="M10 18a8 8 0 100-16 8 8 0 000 16zM9.555 7.168A1 1 0 008 8v4a1 1 0 001.555.832l3-2a1 1 0 000-1.664l-3-2z"/>
              </svg>
            </div>
            <div class="text-sm text-gray-400 mb-2">Видео-отзыв • 3:24</div>
            <div class="font-semibold">Дмитрий Козлов, CTO "Цифровые решения"</div>
          </div>
        </div>
      </div>

      <!-- Final CTA -->
      <div class="text-center mt-16 animate-fade-in delay-1000">
        <h3 class="text-3xl font-bold text-gray-900 mb-6">
          Станьте следующей историей успеха
        </h3>
        <p class="text-xl text-gray-600 mb-8 max-w-2xl mx-auto">
          Присоединяйтесь к тысячам довольных клиентов и начните экономить время и деньги уже сегодня
        </p>
        <div class="flex flex-col sm:flex-row gap-4 justify-center">
          <router-link 
            to="/register" 
            class="px-8 py-4 bg-gradient-to-r from-blue-600 to-purple-600 text-white font-bold text-lg rounded-2xl hover:from-blue-700 hover:to-purple-700 transition-all duration-300 hover:scale-105 shadow-xl"
          >
            🚀 Начать бесплатно
          </router-link>
          <button class="px-8 py-4 bg-white text-gray-700 font-semibold text-lg rounded-2xl border-2 border-gray-300 hover:border-gray-400 hover:bg-gray-50 transition-all duration-300">
            Забронировать демо
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
</style> 