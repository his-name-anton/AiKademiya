<template>
  <div class="bg-gray-50 dark:bg-gray-900 min-h-screen flex items-center justify-center px-6 py-8">
    <div class="w-full max-w-screen-xl flex flex-col md:flex-row items-center justify-center gap-12">

      <!-- Левая колонка -->
      <div class="hidden md:block w-full md:w-1/2">
        <div class="mb-8">
          <router-link to="/" class="flex items-center text-2xl font-bold text-blue-600 mb-6">
            <img src="https://flowbite.s3.amazonaws.com/blocks/marketing-ui/logo.svg" class="w-8 h-8 mr-2" alt="logo">
            AiKademiya
          </router-link>
          <ul class="space-y-6">
            <li>
              <div class="flex items-start space-x-4">
                <svg class="w-6 h-6 text-blue-600 mt-1" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 01.083 1.32l-.083.094-8 8a1 1 0 01-1.32.083l-.094-.083-4-4a1 1 0 011.32-1.497l.094.083L8 12.584l7.293-7.291a1 1 0 011.414 0z" clip-rule="evenodd"/></svg>
                <div>
                  <h3 class="font-semibold text-gray-900 dark:text-white">Генерируй курсы за 5 минут</h3>
                  <p class="text-gray-500 dark:text-gray-400">Полностью автоматически. Без технических знаний.</p>
                </div>
              </div>
            </li>
            <li>
              <div class="flex items-start space-x-4">
                <svg class="w-6 h-6 text-blue-600 mt-1" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 01.083 1.32l-.083.094-8 8a1 1 0 01-1.32.083l-.094-.083-4-4a1 1 0 011.32-1.497l.094.083L8 12.584l7.293-7.291a1 1 0 011.414 0z" clip-rule="evenodd"/></svg>
                <div>
                  <h3 class="font-semibold text-gray-900 dark:text-white">Изучи любой навык</h3>
                  <p class="text-gray-500 dark:text-gray-400">Интерактивное обучение по твоим запросам.</p>
                </div>
              </div>
            </li>
          </ul>
        </div>
      </div>

      <!-- Правая колонка: форма -->
      <div class="w-full md:w-1/2 max-w-md bg-white rounded-lg shadow p-6 md:p-8 dark:bg-gray-800 dark:border dark:border-gray-700">
        <h1 class="text-xl font-bold text-gray-900 dark:text-white mb-6">С возвращением</h1>

        <div class="space-y-4 mb-6">
          <button 
            @click="loginWithGoogle"
            class="w-full flex items-center justify-center border border-gray-300 rounded-lg px-4 py-2 text-gray-700 hover:bg-gray-50 dark:text-white dark:hover:bg-gray-700 transition-colors"
          >
            <img class="w-5 h-5 mr-2" src="https://www.svgrepo.com/show/475656/google-color.svg" alt="Google"> 
            Войти через Google
          </button>
          <button 
            @click="loginWithApple"
            class="w-full flex items-center justify-center border border-gray-300 rounded-lg px-4 py-2 text-gray-700 hover:bg-gray-50 dark:text-white dark:hover:bg-gray-700 transition-colors"
          >
            <svg class="w-5 h-5 mr-2" fill="currentColor" viewBox="0 0 20 20">
              <path d="M16.365 1.43c-.325.153-.748.315-1.29.49-.49.158-.98.287-1.47.388.278-.316.504-.647.677-1.01.168-.34.258-.637.258-.888a1.4 1.4 0 00-.318-.933c-.213-.23-.514-.345-.904-.345-.518 0-1.05.214-1.595.64-.528.425-.955 1.02-1.28 1.786-.204.45-.31.89-.32 1.325-.255.02-.508.043-.76.07-.256.027-.51.064-.762.11-.25.048-.5.108-.75.182-.25.076-.5.164-.75.265a9.857 9.857 0 00-1.38.57 8.776 8.776 0 00-1.29.88A9.296 9.296 0 001.5 5.6c-.47.647-.9 1.342-1.3 2.085-.39.744-.715 1.524-.975 2.34-.26.818-.39 1.644-.39 2.48 0 .735.145 1.44.437 2.113.295.67.708 1.267 1.24 1.79.53.523 1.153.936 1.87 1.238.72.303 1.508.457 2.365.457a6.1 6.1 0 003.212-.903 5.64 5.64 0 001.983-2.13c.238-.494.436-1.02.59-1.58h-.01a6.53 6.53 0 01-1.23.67 4.005 4.005 0 01-1.545.28c-.65 0-1.18-.157-1.59-.47a2.294 2.294 0 01-.76-1.152c-.138-.482-.205-.982-.205-1.5 0-.627.1-1.227.3-1.8.2-.57.465-1.08.795-1.53.34-.45.723-.82 1.15-1.11.43-.287.885-.43 1.365-.43.347 0 .667.077.96.23.29.153.51.345.66.577.13.232.237.498.32.798.085.3.15.592.19.875.04.284.075.574.107.87.033.293.057.59.073.89.02.298.033.595.04.892.01.297.02.592.03.885.015.293.028.583.038.87.012.287.023.57.035.85.01.277.02.55.03.82.01.27.023.532.04.785.01.254.022.498.035.73.01.232.02.457.03.675.01.218.02.425.028.623a9.34 9.34 0 00.493-.523c.163-.184.31-.367.444-.547a6.06 6.06 0 001.185-2.243 7.01 7.01 0 00.18-2.635 6.26 6.26 0 00-.568-2.202 6.8 6.8 0 00-1.437-2.094z"/>
            </svg>
            Войти через Apple
          </button>
        </div>

        <div class="flex items-center mb-4">
          <hr class="flex-grow border-gray-200" />
          <span class="mx-2 text-sm text-gray-400">или</span>
          <hr class="flex-grow border-gray-200" />
        </div>

        <form @submit.prevent="handleLogin" class="space-y-4">
          <FormAlert 
            v-if="error" 
            type="error" 
            :message="error" 
            @close="error = ''"
          />

          <div>
            <label for="email" class="block mb-1 text-sm font-medium text-gray-700 dark:text-white">
              Email
            </label>
            <BaseInput
              id="email"
              v-model="credentials.email"
              type="email"
              placeholder="Введите email"
              :error="fieldErrors.email"
              required
            />
          </div>

          <div>
            <label for="password" class="block mb-1 text-sm font-medium text-gray-700 dark:text-white">
              Пароль
            </label>
            <div class="relative">
              <BaseInput
                id="password"
                v-model="credentials.password"
                :type="showPassword ? 'text' : 'password'"
                placeholder="••••••••"
                :error="fieldErrors.password"
                required
              />
              <button 
                type="button" 
                @click="showPassword = !showPassword"
                class="absolute right-2 top-2.5 text-gray-500 hover:text-gray-800 dark:text-gray-400 dark:hover:text-gray-200 transition-colors"
              >
                {{ showPassword ? '🙈' : '👁' }}
              </button>
            </div>
          </div>

          <div class="flex items-center justify-between text-sm">
            <label class="flex items-center space-x-2">
              <input 
                v-model="rememberMe"
                type="checkbox" 
                class="w-4 h-4 border-gray-300 rounded focus:ring-blue-500"
              >
              <span class="dark:text-white">Запомнить меня</span>
            </label>
            <router-link 
              to="/forgot-password" 
              class="text-blue-600 hover:underline"
            >
              Забыли пароль?
            </router-link>
          </div>

          <BaseButton 
            type="submit" 
            :loading="loading"
            class="w-full"
          >
            Войти
          </BaseButton>
          
          <p class="text-sm text-center text-gray-500">
            Нет аккаунта? 
            <router-link to="/register" class="text-blue-600 hover:underline">
              Зарегистрироваться
            </router-link>
          </p>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, reactive } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import { useToast } from 'vue-toastification'
import BaseButton from '@/components/common/BaseButton.vue'
import BaseInput from '@/components/common/BaseInput.vue'
import FormAlert from '@/components/common/FormAlert.vue'

const router = useRouter()
const authStore = useAuthStore()
const toast = useToast()

// Form state
const loading = ref(false)
const error = ref('')
const showPassword = ref(false)
const rememberMe = ref(false)

const credentials = reactive({
  email: '',
  password: ''
})

const fieldErrors = reactive({
  email: '',
  password: ''
})

// Methods
const handleLogin = async () => {
  loading.value = true
  error.value = ''
  fieldErrors.email = ''
  fieldErrors.password = ''

  try {
    await authStore.login(credentials)
    toast.success('Добро пожаловать!')
    router.push('/')
  } catch (err: any) {
    if (err.response?.data?.errors) {
      // Handle field-specific errors
      const errors = err.response.data.errors
      fieldErrors.email = errors.email?.[0] || ''
      fieldErrors.password = errors.password?.[0] || ''
    } else {
      error.value = err.response?.data?.message || 'Ошибка входа. Проверьте данные.'
    }
  } finally {
    loading.value = false
  }
}

const loginWithGoogle = () => {
  // TODO: Implement Google OAuth
  toast.info('Google авторизация будет добавлена позже')
}

const loginWithApple = () => {
  // TODO: Implement Apple OAuth
  toast.info('Apple авторизация будет добавлена позже')
}
</script>