<template>
  <div class="bg-gray-50 dark:bg-gray-900 min-h-screen">
    <!-- Header -->
    <div class="bg-white shadow dark:bg-gray-800">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="py-6">
          <h1 class="text-2xl font-bold text-gray-900 dark:text-white">Профиль</h1>
        </div>
      </div>
    </div>

    <!-- Content -->
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <div class="grid grid-cols-1 gap-6 lg:grid-cols-3">
        
        <!-- Profile Card -->
        <div class="lg:col-span-1">
          <div class="bg-white shadow rounded-lg p-6 dark:bg-gray-800">
            <div class="text-center">
              <div class="relative inline-block">
                <img 
                  :src="userProfile?.avatar || defaultAvatar"
                  :alt="userProfile?.username || 'Avatar'"
                  class="w-24 h-24 rounded-full mx-auto object-cover"
                >
                <button 
                  @click="showAvatarUpload = true"
                  class="absolute bottom-0 right-0 bg-blue-600 text-white p-2 rounded-full hover:bg-blue-700 transition-colors"
                >
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.232 5.232l3.536 3.536m-2.036-5.036a2.5 2.5 0 113.536 3.536L6.5 21.036H3v-3.572L16.732 3.732z"></path>
                  </svg>
                </button>
              </div>
              
              <h3 class="mt-4 text-lg font-medium text-gray-900 dark:text-white">
                {{ userProfile?.username || 'Пользователь' }}
              </h3>
              <p class="text-gray-500 dark:text-gray-400">
                {{ userProfile?.email }}
              </p>
              
              <div class="mt-4 space-y-2">
                <div class="bg-gray-50 dark:bg-gray-700 rounded-lg p-3">
                  <div class="text-sm text-gray-600 dark:text-gray-400">Подписка</div>
                  <div class="font-medium text-blue-600 dark:text-blue-400">Free</div>
                </div>
                
                <div class="bg-gray-50 dark:bg-gray-700 rounded-lg p-3">
                  <div class="text-sm text-gray-600 dark:text-gray-400">Дата регистрации</div>
                  <div class="font-medium text-gray-900 dark:text-white">
                    {{ formatDate(userProfile?.date_joined) }}
                  </div>
                </div>
              </div>

              <div class="mt-6">
                <router-link to="/generate">
                  <BaseButton class="w-full">
                    Создать новый курс
                  </BaseButton>
                </router-link>
              </div>
            </div>
          </div>
        </div>

        <!-- Profile Form -->
        <div class="lg:col-span-2">
          <div class="bg-white shadow rounded-lg p-6 dark:bg-gray-800">
            <h3 class="text-lg font-medium text-gray-900 dark:text-white mb-6">
              Основная информация
            </h3>
            
            <form @submit.prevent="handleUpdateProfile" class="space-y-6">
              <FormAlert 
                v-if="error" 
                type="error" 
                :message="error" 
                @close="error = ''"
              />
              
              <FormAlert 
                v-if="success" 
                type="success" 
                :message="success" 
                @close="success = ''"
              />

              <div class="grid grid-cols-1 gap-6 sm:grid-cols-2">
                <div>
                  <label for="first_name" class="block text-sm font-medium text-gray-700 dark:text-white">
                    Имя
                  </label>
                  <BaseInput
                    id="first_name"
                    v-model="profileForm.first_name"
                    placeholder="Введите имя"
                    :error="fieldErrors.first_name"
                  />
                </div>

                <div>
                  <label for="last_name" class="block text-sm font-medium text-gray-700 dark:text-white">
                    Фамилия
                  </label>
                  <BaseInput
                    id="last_name"
                    v-model="profileForm.last_name"
                    placeholder="Введите фамилию"
                    :error="fieldErrors.last_name"
                  />
                </div>

                <div>
                  <label for="username" class="block text-sm font-medium text-gray-700 dark:text-white">
                    Имя пользователя
                  </label>
                  <BaseInput
                    id="username"
                    v-model="profileForm.username"
                    placeholder="Введите имя пользователя"
                    :error="fieldErrors.username"
                  />
                </div>

                <div>
                  <label class="block text-sm font-medium text-gray-700 dark:text-white">
                    Email
                  </label>
                  <div class="mt-1 p-3 bg-gray-50 dark:bg-gray-700 rounded-lg">
                    <p class="text-gray-900 dark:text-white">{{ userProfile?.email }}</p>
                    <p class="text-xs text-gray-500 dark:text-gray-400 mt-1">
                      Для изменения email обратитесь в поддержку
                    </p>
                  </div>
                </div>

                <div>
                  <label for="birth_date" class="block text-sm font-medium text-gray-700 dark:text-white">
                    Дата рождения
                  </label>
                  <BaseInput
                    id="birth_date"
                    v-model="profileForm.birth_date"
                    type="date"
                    :error="fieldErrors.birth_date"
                  />
                </div>

                <div>
                  <label for="occupation" class="block text-sm font-medium text-gray-700 dark:text-white">
                    Чем занимаюсь
                  </label>
                  <BaseInput
                    id="occupation"
                    v-model="profileForm.occupation"
                    placeholder="Например: Frontend разработчик"
                    :error="fieldErrors.occupation"
                  />
                </div>
              </div>

              <div class="flex justify-end">
                <BaseButton 
                  type="submit" 
                  :loading="loading"
                >
                  Сохранить изменения
                </BaseButton>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>

    <!-- Avatar Upload Modal -->
    <div 
      v-if="showAvatarUpload" 
      class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50"
      @click.self="showAvatarUpload = false"
    >
      <div class="bg-white dark:bg-gray-800 rounded-lg p-6 max-w-md w-full mx-4">
        <h3 class="text-lg font-medium text-gray-900 dark:text-white mb-4">
          Загрузить аватар
        </h3>
        
        <div class="space-y-4">
          <div class="flex items-center justify-center w-full">
            <label 
              for="avatar-upload" 
              class="flex flex-col items-center justify-center w-full h-32 border-2 border-gray-300 border-dashed rounded-lg cursor-pointer bg-gray-50 dark:hover:bg-gray-600 dark:bg-gray-700 hover:bg-gray-100 dark:border-gray-600 dark:hover:border-gray-500"
            >
              <div class="flex flex-col items-center justify-center pt-5 pb-6">
                <svg class="w-8 h-8 mb-4 text-gray-500 dark:text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12"></path>
                </svg>
                <p class="mb-2 text-sm text-gray-500 dark:text-gray-400">
                  <span class="font-semibold">Нажмите для выбора</span>
                </p>
                <p class="text-xs text-gray-500 dark:text-gray-400">
                  PNG, JPG до 2MB
                </p>
              </div>
              <input 
                id="avatar-upload" 
                type="file" 
                class="hidden" 
                accept="image/*"
                @change="handleAvatarUpload"
              />
            </label>
          </div>
          
          <div class="flex space-x-3">
            <BaseButton 
              variant="secondary" 
              @click="showAvatarUpload = false"
              class="flex-1"
            >
              Отмена
            </BaseButton>
            <BaseButton 
              v-if="userProfile?.avatar"
              variant="danger" 
              @click="handleDeleteAvatar"
              :loading="deletingAvatar"
              class="flex-1"
            >
              Удалить
            </BaseButton>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, reactive, onMounted, computed } from 'vue'
import { useAuthStore } from '../stores/auth'
import { useToast } from 'vue-toastification'
import BaseButton from '../components/common/BaseButton.vue'
import BaseInput from '../components/common/BaseInput.vue'
import FormAlert from '../components/common/FormAlert.vue'
import { authApi } from '../api/auth'

const authStore = useAuthStore()
const toast = useToast()

// State
const loading = ref(false)
const error = ref('')
const success = ref('')
const showAvatarUpload = ref(false)
const deletingAvatar = ref(false)

const profileForm = reactive({
  username: '',
  first_name: '',
  last_name: '',
  birth_date: '',
  occupation: ''
})

const fieldErrors = reactive({
  username: '',
  first_name: '',
  last_name: '',
  birth_date: '',
  occupation: ''
})

// Computed
const userProfile = computed(() => authStore.user)

const defaultAvatar = 'data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTAwIiBoZWlnaHQ9IjEwMCIgdmlld0JveD0iMCAwIDEwMCAxMDAiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjxyZWN0IHdpZHRoPSIxMDAiIGhlaWdodD0iMTAwIiBmaWxsPSIjRjNGNEY2Ii8+CjxwYXRoIGQ9Ik01MCA1MEMzNS43NSA1MCAyNS41IDQwLjI1IDI1LjUgMjZDMjUuNSAxMS43NSAzNS43NSAyIDUwIDJDNjQuMjUgMiA3NC41IDExLjc1IDc0LjUgMjZDNzQuNSA0MC4yNSA2NC4yNSA1MCA1MCA1MFpNNzQgNjJDNzkuNSA2MiA4NCA2Ni41IDg0IDcyVjg4QzY0IDk0IDM2IDk0IDE2IDg4VjcyQzE2IDY2LjUgMjAuNSA2MiAyNiA2Mkg3NFoiIGZpbGw9IiM5Q0E0QUYiLz4KPC9zdmc+'

// Methods
const loadProfile = () => {
  if (userProfile.value) {
    profileForm.username = userProfile.value.username || ''
    profileForm.first_name = userProfile.value.first_name || ''
    profileForm.last_name = userProfile.value.last_name || ''
    profileForm.birth_date = userProfile.value.birth_date || ''
    profileForm.occupation = userProfile.value.occupation || ''
  }
}

const handleUpdateProfile = async () => {
  loading.value = true
  error.value = ''
  success.value = ''
  
  // Clear field errors
  Object.keys(fieldErrors).forEach(key => {
    fieldErrors[key as keyof typeof fieldErrors] = ''
  })

  try {
    await authStore.updateProfile(profileForm)
    success.value = 'Профиль успешно обновлен'
    toast.success('Профиль обновлен')
  } catch (err: any) {
    if (err.response?.data?.errors) {
      const errors = err.response.data.errors
      Object.keys(fieldErrors).forEach(key => {
        fieldErrors[key as keyof typeof fieldErrors] = errors[key]?.[0] || ''
      })
    } else {
      error.value = err.response?.data?.message || 'Ошибка обновления профиля'
    }
  } finally {
    loading.value = false
  }
}

const handleAvatarUpload = async (event: Event) => {
  const target = event.target as HTMLInputElement
  const file = target.files?.[0]
  
  if (!file) return

  // Validate file
  if (file.size > 2 * 1024 * 1024) {
    toast.error('Файл слишком большой. Максимум 2MB.')
    return
  }

  if (!file.type.startsWith('image/')) {
    toast.error('Выберите изображение')
    return
  }

  try {
    await authApi.uploadAvatar(file, (progress) => {
      // TODO: Show upload progress
    })
    
    await authStore.fetchProfile()
    showAvatarUpload.value = false
    toast.success('Аватар обновлен')
  } catch (err: any) {
    toast.error(err.response?.data?.message || 'Ошибка загрузки аватара')
  }
}

const handleDeleteAvatar = async () => {
  deletingAvatar.value = true
  
  try {
    await authApi.deleteAvatar()
    await authStore.fetchProfile()
    showAvatarUpload.value = false
    toast.success('Аватар удален')
  } catch (err: any) {
    toast.error(err.response?.data?.message || 'Ошибка удаления аватара')
  } finally {
    deletingAvatar.value = false
  }
}

const formatDate = (dateString?: string) => {
  if (!dateString) return 'Не указано'
  return new Date(dateString).toLocaleDateString('ru-RU')
}

// Lifecycle
onMounted(() => {
  loadProfile()
})
</script>