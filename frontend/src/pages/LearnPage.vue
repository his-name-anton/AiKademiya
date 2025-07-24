<template>
  <div class="bg-gray-50 dark:bg-gray-900 min-h-screen">
    <!-- Header -->
    <div class="bg-white shadow dark:bg-gray-800">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="py-6">
          <h1 class="text-2xl font-bold text-gray-900 dark:text-white">Обучение</h1>
          <p class="mt-2 text-gray-600 dark:text-gray-400">
            Изучайте курсы, созданные с помощью ИИ
          </p>
        </div>
      </div>
    </div>

    <!-- Content -->
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      
      <!-- Loading state -->
      <div v-if="loading" class="flex justify-center items-center py-12">
        <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600"></div>
      </div>

      <!-- Empty state -->
      <div v-else-if="!courses.length" class="text-center py-12">
        <div class="mx-auto w-24 h-24 bg-gray-100 rounded-full flex items-center justify-center mb-6">
          <svg class="w-12 h-12 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.746 0 3.332.477 4.5 1.253v13C19.832 18.477 18.246 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"></path>
          </svg>
        </div>
        <h3 class="text-lg font-medium text-gray-900 dark:text-white mb-2">
          Пока нет курсов для изучения
        </h3>
        <p class="text-gray-500 dark:text-gray-400 mb-6">
          Создайте свой первый курс с помощью ИИ или дождитесь, пока ваши курсы будут готовы к изучению.
        </p>
        <router-link to="/generate">
          <BaseButton>
            Создать курс
          </BaseButton>
        </router-link>
      </div>

      <!-- Courses Grid -->
      <div v-else class="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3">
        <div 
          v-for="course in courses" 
          :key="course.id"
          class="bg-white rounded-lg shadow-sm hover:shadow-md transition-shadow duration-200 overflow-hidden dark:bg-gray-800"
        >
          <!-- Course Image -->
          <div class="h-48 bg-gradient-to-br from-blue-500 to-purple-600 relative">
            <img 
              v-if="course.image" 
              :src="course.image" 
              :alt="course.title"
              class="w-full h-full object-cover"
            >
            <div class="absolute inset-0 bg-black bg-opacity-20 flex items-center justify-center">
              <div class="text-center">
                <div class="text-white text-xl font-bold mb-2">{{ course.title }}</div>
                <div class="text-blue-200 text-sm">{{ course.lessons_count }} уроков</div>
              </div>
            </div>
          </div>

          <!-- Course Info -->
          <div class="p-6">
            <h3 class="text-lg font-semibold text-gray-900 dark:text-white mb-2">
              {{ course.title }}
            </h3>
            <p class="text-gray-600 dark:text-gray-400 text-sm mb-4 line-clamp-2">
              {{ course.description }}
            </p>

            <!-- Progress Bar -->
            <div class="mb-4">
              <div class="flex justify-between items-center mb-2">
                <span class="text-sm text-gray-600 dark:text-gray-400">Прогресс</span>
                <span class="text-sm font-medium text-gray-900 dark:text-white">
                  {{ Math.round((course.completed_lessons / course.lessons_count) * 100) }}%
                </span>
              </div>
              <div class="w-full bg-gray-200 rounded-full h-2 dark:bg-gray-700">
                <div 
                  class="bg-blue-600 h-2 rounded-full transition-all duration-300"
                  :style="{ width: `${(course.completed_lessons / course.lessons_count) * 100}%` }"
                ></div>
              </div>
            </div>

            <!-- Course Meta -->
            <div class="flex items-center justify-between text-sm text-gray-500 dark:text-gray-400 mb-4">
              <div class="flex items-center">
                <svg class="w-4 h-4 mr-1" fill="currentColor" viewBox="0 0 20 20">
                  <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm1-12a1 1 0 10-2 0v4a1 1 0 00.293.707l2.828 2.829a1 1 0 101.415-1.415L11 9.586V6z" clip-rule="evenodd"></path>
                </svg>
                {{ formatDuration(course.estimated_duration) }}
              </div>
              <div class="flex items-center">
                <svg class="w-4 h-4 mr-1" fill="currentColor" viewBox="0 0 20 20">
                  <path d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                </svg>
                {{ course.completed_lessons }}/{{ course.lessons_count }}
              </div>
            </div>

            <!-- Action Buttons -->
            <div class="flex space-x-2">
              <BaseButton 
                @click="startCourse(course)"
                :variant="course.completed_lessons > 0 ? 'outline' : 'primary'"
                class="flex-1"
                size="sm"
              >
                {{ course.completed_lessons > 0 ? 'Продолжить' : 'Начать' }}
              </BaseButton>
              <BaseButton 
                @click="viewCourseDetails(course)"
                variant="ghost"
                size="sm"
              >
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                </svg>
              </BaseButton>
            </div>
          </div>
        </div>
      </div>

      <!-- Load More Button -->
      <div v-if="hasMoreCourses" class="flex justify-center mt-8">
        <BaseButton 
          @click="loadMoreCourses"
          :loading="loadingMore"
          variant="outline"
        >
          Загрузить еще
        </BaseButton>
      </div>
    </div>

    <!-- Course Details Modal -->
    <div 
      v-if="selectedCourse" 
      class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4"
      @click.self="selectedCourse = null"
    >
      <div class="bg-white dark:bg-gray-800 rounded-lg max-w-2xl w-full max-h-[90vh] overflow-y-auto">
        <div class="p-6">
          <div class="flex justify-between items-start mb-4">
            <h2 class="text-xl font-bold text-gray-900 dark:text-white">
              {{ selectedCourse.title }}
            </h2>
            <button 
              @click="selectedCourse = null"
              class="text-gray-400 hover:text-gray-600 dark:hover:text-gray-300"
            >
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
              </svg>
            </button>
          </div>

          <p class="text-gray-600 dark:text-gray-400 mb-6">
            {{ selectedCourse.description }}
          </p>

          <!-- Course Stats -->
          <div class="grid grid-cols-3 gap-4 mb-6">
            <div class="text-center">
              <div class="text-2xl font-bold text-blue-600 dark:text-blue-400">
                {{ selectedCourse.lessons_count }}
              </div>
              <div class="text-sm text-gray-500 dark:text-gray-400">Уроков</div>
            </div>
            <div class="text-center">
              <div class="text-2xl font-bold text-green-600 dark:text-green-400">
                {{ selectedCourse.completed_lessons }}
              </div>
              <div class="text-sm text-gray-500 dark:text-gray-400">Пройдено</div>
            </div>
            <div class="text-center">
              <div class="text-2xl font-bold text-purple-600 dark:text-purple-400">
                {{ formatDuration(selectedCourse.estimated_duration) }}
              </div>
              <div class="text-sm text-gray-500 dark:text-gray-400">Время</div>
            </div>
          </div>

          <!-- Lessons List -->
          <div v-if="selectedCourse.lessons" class="mb-6">
            <h3 class="text-lg font-medium text-gray-900 dark:text-white mb-3">
              Уроки
            </h3>
            <div class="space-y-2">
              <div 
                v-for="(lesson, index) in selectedCourse.lessons" 
                :key="lesson.id"
                class="flex items-center p-3 bg-gray-50 dark:bg-gray-700 rounded-lg"
              >
                <div class="flex-shrink-0 mr-3">
                  <div 
                    v-if="lesson.completed"
                    class="w-6 h-6 bg-green-500 rounded-full flex items-center justify-center"
                  >
                    <svg class="w-4 h-4 text-white" fill="currentColor" viewBox="0 0 20 20">
                      <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"></path>
                    </svg>
                  </div>
                  <div v-else class="w-6 h-6 bg-gray-300 dark:bg-gray-600 rounded-full flex items-center justify-center">
                    <span class="text-xs text-gray-600 dark:text-gray-400">{{ index + 1 }}</span>
                  </div>
                </div>
                <div class="flex-grow">
                  <div class="font-medium text-gray-900 dark:text-white">
                    {{ lesson.title }}
                  </div>
                  <div class="text-sm text-gray-500 dark:text-gray-400">
                    {{ formatDuration(lesson.duration) }}
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- Action Buttons -->
          <div class="flex space-x-3">
            <BaseButton 
              @click="startCourse(selectedCourse)"
              class="flex-1"
            >
              {{ selectedCourse.completed_lessons > 0 ? 'Продолжить обучение' : 'Начать обучение' }}
            </BaseButton>
            <BaseButton 
              @click="selectedCourse = null"
              variant="secondary"
              class="flex-1"
            >
              Закрыть
            </BaseButton>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useToast } from 'vue-toastification'
import BaseButton from '@/components/common/BaseButton.vue'
// TODO: Import courses API when available

const router = useRouter()
const toast = useToast()

// State
const loading = ref(true)
const loadingMore = ref(false)
const courses = ref<any[]>([])
const selectedCourse = ref(null)
const hasMoreCourses = ref(false)

// Methods
const loadCourses = async () => {
  loading.value = true
  
  try {
    // TODO: Replace with actual API call
    // Simulate API call
    await new Promise(resolve => setTimeout(resolve, 1000))
    
    // Mock data for now
    courses.value = [
      {
        id: 1,
        title: 'Введение в JavaScript',
        description: 'Изучите основы JavaScript - самого популярного языка программирования для веб-разработки.',
        image: null,
        lessons_count: 12,
        completed_lessons: 5,
        estimated_duration: 480, // minutes
        lessons: [
          { id: 1, title: 'Переменные и типы данных', completed: true, duration: 30 },
          { id: 2, title: 'Функции', completed: true, duration: 45 },
          { id: 3, title: 'Массивы и объекты', completed: false, duration: 40 },
          // ... more lessons
        ]
      },
      {
        id: 2,
        title: 'Основы Python',
        description: 'Начните изучение Python - универсального языка программирования для анализа данных и веб-разработки.',
        image: null,
        lessons_count: 15,
        completed_lessons: 0,
        estimated_duration: 600,
        lessons: []
      }
    ]
    
    hasMoreCourses.value = false
  } catch (error) {
    toast.error('Ошибка загрузки курсов')
  } finally {
    loading.value = false
  }
}

const loadMoreCourses = async () => {
  loadingMore.value = true
  
  try {
    // TODO: Implement pagination
    await new Promise(resolve => setTimeout(resolve, 1000))
    hasMoreCourses.value = false
  } catch (error) {
    toast.error('Ошибка загрузки курсов')
  } finally {
    loadingMore.value = false
  }
}

const startCourse = (course: any) => {
  // TODO: Navigate to course learning interface
  toast.info(`Переход к курсу: ${course.title}`)
  // router.push(`/learn/${course.id}`)
}

const viewCourseDetails = (course: any) => {
  selectedCourse.value = course
}

const formatDuration = (minutes: number) => {
  if (minutes < 60) {
    return `${minutes} мин`
  }
  const hours = Math.floor(minutes / 60)
  const remainingMinutes = minutes % 60
  if (remainingMinutes === 0) {
    return `${hours} ч`
  }
  return `${hours} ч ${remainingMinutes} мин`
}

// Lifecycle
onMounted(() => {
  loadCourses()
})
</script>

<style scoped>
.line-clamp-2 {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
</style>