<template>
  <div class="bg-gray-50 dark:bg-gray-900 min-h-screen flex items-center justify-center px-6 py-8">
    <div class="w-full max-w-md">
      <div class="bg-white rounded-lg shadow p-6 md:p-8 dark:bg-gray-800 dark:border dark:border-gray-700">
        
        <!-- Success state -->
        <div v-if="emailSent" class="text-center">
          <div class="mx-auto w-16 h-16 bg-green-100 rounded-full flex items-center justify-center mb-4">
            <svg class="w-8 h-8 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
            </svg>
          </div>
          <h1 class="text-xl font-bold text-gray-900 dark:text-white mb-4">Письмо отправлено</h1>
          <p class="text-gray-600 dark:text-gray-400 mb-6">
            На ваш email {{ email }} отправлены инструкции по восстановлению пароля.
          </p>
          <div class="space-y-3">
            <BaseButton @click="resendEmail" :loading="loading" variant="outline" class="w-full">
              Отправить повторно
            </BaseButton>
            <router-link to="/login" class="block w-full">
              <BaseButton variant="secondary" class="w-full">
                Вернуться к входу
              </BaseButton>
            </router-link>
          </div>
        </div>

        <!-- Form state -->
        <div v-else>
          <div class="text-center mb-6">
            <router-link to="/" class="inline-flex items-center text-2xl font-bold text-blue-600 mb-4">
              <img src="https://flowbite.s3.amazonaws.com/blocks/marketing-ui/logo.svg" class="w-8 h-8 mr-2" alt="logo">
              AiKademiya
            </router-link>
            <h1 class="text-xl font-bold text-gray-900 dark:text-white">Забыли пароль?</h1>
            <p class="text-gray-600 dark:text-gray-400 mt-2">
              Введите ваш email и мы отправим инструкции по восстановлению пароля.
            </p>
          </div>

          <form @submit.prevent="handleForgotPassword" class="space-y-4">
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
                v-model="email"
                type="email"
                placeholder="Введите ваш email"
                :error="fieldError"
                required
                autofocus
              />
            </div>

            <BaseButton 
              type="submit" 
              :loading="loading"
              class="w-full"
            >
              Восстановить пароль
            </BaseButton>
            
            <div class="text-center">
              <router-link 
                to="/login" 
                class="text-sm text-blue-600 hover:underline"
              >
                Вспомнили пароль? Войти
              </router-link>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { authApi } from '@/api/auth'
import { useToast } from 'vue-toastification'
import BaseButton from '@/components/common/BaseButton.vue'
import BaseInput from '@/components/common/BaseInput.vue'
import FormAlert from '@/components/common/FormAlert.vue'

const toast = useToast()

// Form state
const loading = ref(false)
const error = ref('')
const fieldError = ref('')
const email = ref('')
const emailSent = ref(false)

// Methods
const handleForgotPassword = async () => {
  loading.value = true
  error.value = ''
  fieldError.value = ''

  try {
    await authApi.requestPasswordReset(email.value)
    emailSent.value = true
    toast.success('Инструкции отправлены на ваш email')
  } catch (err: any) {
    if (err.response?.data?.errors?.email) {
      fieldError.value = err.response.data.errors.email[0]
    } else {
      error.value = err.response?.data?.message || 'Ошибка отправки. Попробуйте снова.'
    }
  } finally {
    loading.value = false
  }
}

const resendEmail = async () => {
  await handleForgotPassword()
}
</script>