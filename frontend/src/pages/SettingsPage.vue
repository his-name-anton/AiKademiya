<template>
  <div class="bg-gray-50 dark:bg-gray-900 min-h-screen">
    <!-- Header -->
    <div class="bg-white shadow dark:bg-gray-800">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="py-6">
          <!-- Breadcrumb -->
          <nav class="flex mb-5" aria-label="Breadcrumb">
            <ol class="inline-flex items-center space-x-1 text-sm font-medium md:space-x-2">
              <li class="inline-flex items-center">
                <router-link 
                  to="/"
                  class="inline-flex items-center text-gray-700 hover:text-blue-600 dark:text-gray-300 dark:hover:text-white"
                >
                  <svg class="w-5 h-5 mr-2.5" fill="currentColor" viewBox="0 0 20 20">
                    <path d="M10.707 2.293a1 1 0 00-1.414 0l-7 7a1 1 0 001.414 1.414L4 10.414V17a1 1 0 001 1h2a1 1 0 001-1v-2a1 1 0 011-1h2a1 1 0 011 1v2a1 1 0 001 1h2a1 1 0 001-1v-6.586l.293.293a1 1 0 001.414-1.414l-7-7z"></path>
                  </svg>
                  Главная
                </router-link>
              </li>
              <li>
                <div class="flex items-center">
                  <svg class="w-6 h-6 text-gray-400" fill="currentColor" viewBox="0 0 20 20">
                    <path fill-rule="evenodd" d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z" clip-rule="evenodd"></path>
                  </svg>
                  <router-link 
                    to="/profile"
                    class="ml-1 text-gray-700 hover:text-blue-600 md:ml-2 dark:text-gray-300 dark:hover:text-white"
                  >
                    Профиль
                  </router-link>
                </div>
              </li>
              <li>
                <div class="flex items-center">
                  <svg class="w-6 h-6 text-gray-400" fill="currentColor" viewBox="0 0 20 20">
                    <path fill-rule="evenodd" d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z" clip-rule="evenodd"></path>
                  </svg>
                  <span class="ml-1 text-gray-400 md:ml-2 dark:text-gray-500" aria-current="page">
                    Настройки
                  </span>
                </div>
              </li>
            </ol>
          </nav>
          <h1 class="text-2xl font-bold text-gray-900 dark:text-white">Настройки</h1>
        </div>
      </div>
    </div>

    <!-- Content -->
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <div class="grid grid-cols-1 gap-6 xl:grid-cols-3">
        
        <!-- Avatar & Basic Info Section -->
        <div class="xl:col-span-1">
          <div class="bg-white rounded-lg shadow p-6 dark:bg-gray-800 mb-6">
            <div class="flex items-center space-x-4">
              <div class="relative">
                <img 
                  :src="userProfile?.avatar || defaultAvatar"
                  :alt="userProfile?.username || 'Avatar'"
                  class="w-28 h-28 rounded-lg object-cover"
                >
                <button 
                  @click="showAvatarUpload = true"
                  class="absolute bottom-0 right-0 bg-blue-600 text-white p-2 rounded-lg hover:bg-blue-700 transition-colors"
                >
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.232 5.232l3.536 3.536m-2.036-5.036a2.5 2.5 0 113.536 3.536L6.5 21.036H3v-3.572L16.732 3.732z"></path>
                  </svg>
                </button>
              </div>
              <div class="flex-1">
                <h3 class="text-xl font-bold text-gray-900 dark:text-white">Аватар</h3>
                <div class="text-sm text-gray-500 dark:text-gray-400 mb-4">
                  JPG, GIF или PNG. Максимум 2MB
                </div>
                <div class="flex items-center space-x-4">
                  <BaseButton 
                    @click="showAvatarUpload = true"
                    size="sm"
                  >
                    <svg class="w-4 h-4 mr-2" fill="currentColor" viewBox="0 0 20 20">
                      <path d="M5.5 13a3.5 3.5 0 01-.369-6.98 4 4 0 117.753-1.977A4.5 4.5 0 1113.5 13H11V9.413l1.293 1.293a1 1 0 001.414-1.414l-3-3a1 1 0 00-1.414 0l-3 3a1 1 0 001.414 1.414L9 9.414V13H5.5z"></path>
                      <path d="M9 13h2v5a1 1 0 11-2 0v-5z"></path>
                    </svg>
                    Загрузить
                  </BaseButton>
                  <BaseButton 
                    v-if="userProfile?.avatar"
                    @click="handleDeleteAvatar"
                    variant="secondary"
                    size="sm"
                    :loading="deletingAvatar"
                  >
                    Удалить
                  </BaseButton>
                </div>
              </div>
            </div>
          </div>

          <!-- Language & Time Section -->
          <div class="bg-white rounded-lg shadow p-6 dark:bg-gray-800 mb-6">
            <h3 class="text-xl font-semibold text-gray-900 dark:text-white mb-4">
              Язык и время
            </h3>
            <form @submit.prevent="saveLanguageSettings" class="space-y-4">
              <div>
                <label for="language" class="block text-sm font-medium text-gray-700 dark:text-white mb-2">
                  Выберите язык
                </label>
                <select 
                  id="language" 
                  v-model="languageSettings.language"
                  class="bg-gray-50 border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                >
                  <option value="ru">Русский</option>
                  <option value="en">English (US)</option>
                  <option value="it">Italiano</option>
                  <option value="fr">Français (France)</option>
                  <option value="zh">正體字</option>
                  <option value="es">Español (España)</option>
                  <option value="de">Deutsch</option>
                  <option value="pt">Português (Brasil)</option>
                </select>
              </div>
              
              <div>
                <label for="timezone" class="block text-sm font-medium text-gray-700 dark:text-white mb-2">
                  Часовой пояс
                </label>
                <select 
                  id="timezone" 
                  v-model="languageSettings.timezone"
                  class="bg-gray-50 border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                >
                  <option value="UTC+0">GMT+0 Greenwich Mean Time (GMT)</option>
                  <option value="UTC+1">GMT+1 Central European Time (CET)</option>
                  <option value="UTC+2">GMT+2 Eastern European Time (EET)</option>
                  <option value="UTC+3">GMT+3 Moscow Time (MSK)</option>
                  <option value="UTC+5">GMT+5 Pakistan Standard Time (PKT)</option>
                  <option value="UTC+8">GMT+8 China Standard Time (CST)</option>
                  <option value="UTC+10">GMT+10 Eastern Australia Standard Time (AEST)</option>
                </select>
              </div>
              
              <BaseButton 
                type="submit" 
                :loading="savingLanguage"
                class="w-full"
              >
                Сохранить
              </BaseButton>
            </form>
          </div>
        </div>

        <!-- Main Settings Section -->
        <div class="xl:col-span-2">
          <!-- General Information -->
          <div class="bg-white rounded-lg shadow p-6 dark:bg-gray-800 mb-6">
            <h3 class="text-xl font-semibold text-gray-900 dark:text-white mb-4">
              Основная информация
            </h3>
            <form @submit.prevent="saveGeneralInfo" class="space-y-6">
              <FormAlert 
                v-if="generalError" 
                type="error" 
                :message="generalError" 
                @close="generalError = ''"
              />
              
              <FormAlert 
                v-if="generalSuccess" 
                type="success" 
                :message="generalSuccess" 
                @close="generalSuccess = ''"
              />

              <div class="grid grid-cols-1 gap-6 sm:grid-cols-2">
                <div>
                  <label for="first_name" class="block text-sm font-medium text-gray-700 dark:text-white mb-2">
                    Имя
                  </label>
                  <BaseInput
                    id="first_name"
                    v-model="generalInfo.first_name"
                    placeholder="Введите имя"
                    :error="generalErrors.first_name"
                  />
                </div>

                <div>
                  <label for="last_name" class="block text-sm font-medium text-gray-700 dark:text-white mb-2">
                    Фамилия
                  </label>
                  <BaseInput
                    id="last_name"
                    v-model="generalInfo.last_name"
                    placeholder="Введите фамилию"
                    :error="generalErrors.last_name"
                  />
                </div>

                <div>
                  <label for="country" class="block text-sm font-medium text-gray-700 dark:text-white mb-2">
                    Страна
                  </label>
                  <BaseInput
                    id="country"
                    v-model="generalInfo.country"
                    placeholder="Россия"
                    :error="generalErrors.country"
                  />
                </div>

                <div>
                  <label for="city" class="block text-sm font-medium text-gray-700 dark:text-white mb-2">
                    Город
                  </label>
                  <BaseInput
                    id="city"
                    v-model="generalInfo.city"
                    placeholder="Москва"
                    :error="generalErrors.city"
                  />
                </div>

                <div>
                  <label for="address" class="block text-sm font-medium text-gray-700 dark:text-white mb-2">
                    Адрес
                  </label>
                  <BaseInput
                    id="address"
                    v-model="generalInfo.address"
                    placeholder="Ул. Пушкина, д. 10"
                    :error="generalErrors.address"
                  />
                </div>

                <div>
                  <label class="block text-sm font-medium text-gray-700 dark:text-white mb-2">
                    Email
                  </label>
                  <div class="p-3 bg-gray-50 dark:bg-gray-700 rounded-lg">
                    <p class="text-gray-900 dark:text-white">{{ userProfile?.email }}</p>
                    <p class="text-xs text-gray-500 dark:text-gray-400 mt-1">
                      Для изменения email обратитесь в поддержку
                    </p>
                  </div>
                </div>

                <div>
                  <label for="phone" class="block text-sm font-medium text-gray-700 dark:text-white mb-2">
                    Телефон
                  </label>
                  <BaseInput
                    id="phone"
                    v-model="generalInfo.phone"
                    type="tel"
                    placeholder="+7 (999) 123-45-67"
                    :error="generalErrors.phone"
                  />
                </div>

                <div>
                  <label for="birth_date" class="block text-sm font-medium text-gray-700 dark:text-white mb-2">
                    День рождения
                  </label>
                  <BaseInput
                    id="birth_date"
                    v-model="generalInfo.birth_date"
                    type="date"
                    :error="generalErrors.birth_date"
                  />
                </div>

                <div>
                  <label for="organization" class="block text-sm font-medium text-gray-700 dark:text-white mb-2">
                    Организация
                  </label>
                  <BaseInput
                    id="organization"
                    v-model="generalInfo.organization"
                    placeholder="Название компании"
                    :error="generalErrors.organization"
                  />
                </div>

                <div>
                  <label for="role" class="block text-sm font-medium text-gray-700 dark:text-white mb-2">
                    Должность
                  </label>
                  <BaseInput
                    id="role"
                    v-model="generalInfo.role"
                    placeholder="Frontend разработчик"
                    :error="generalErrors.role"
                  />
                </div>

                <div>
                  <label for="department" class="block text-sm font-medium text-gray-700 dark:text-white mb-2">
                    Отдел
                  </label>
                  <BaseInput
                    id="department"
                    v-model="generalInfo.department"
                    placeholder="Разработка"
                    :error="generalErrors.department"
                  />
                </div>

                <div>
                  <label for="zip_code" class="block text-sm font-medium text-gray-700 dark:text-white mb-2">
                    Почтовый индекс
                  </label>
                  <BaseInput
                    id="zip_code"
                    v-model="generalInfo.zip_code"
                    placeholder="123456"
                    :error="generalErrors.zip_code"
                  />
                </div>
              </div>

              <div class="flex justify-end">
                <BaseButton 
                  type="submit" 
                  :loading="savingGeneral"
                >
                  Сохранить все
                </BaseButton>
              </div>
            </form>
          </div>

          <!-- Password Section -->
          <div class="bg-white rounded-lg shadow p-6 dark:bg-gray-800 mb-6">
            <h3 class="text-xl font-semibold text-gray-900 dark:text-white mb-4">
              Изменение пароля
            </h3>
            <form @submit.prevent="changePassword" class="space-y-6">
              <FormAlert 
                v-if="passwordError" 
                type="error" 
                :message="passwordError" 
                @close="passwordError = ''"
              />
              
              <FormAlert 
                v-if="passwordSuccess" 
                type="success" 
                :message="passwordSuccess" 
                @close="passwordSuccess = ''"
              />

              <div class="grid grid-cols-1 gap-6 sm:grid-cols-2">
                <div class="sm:col-span-2">
                  <label for="current_password" class="block text-sm font-medium text-gray-700 dark:text-white mb-2">
                    Текущий пароль
                  </label>
                  <BaseInput
                    id="current_password"
                    v-model="passwordForm.current_password"
                    type="password"
                    placeholder="••••••••"
                    :error="passwordErrors.current_password"
                    required
                  />
                </div>

                <div>
                  <label for="new_password" class="block text-sm font-medium text-gray-700 dark:text-white mb-2">
                    Новый пароль
                  </label>
                  <BaseInput
                    id="new_password"
                    v-model="passwordForm.new_password"
                    type="password"
                    placeholder="••••••••"
                    :error="passwordErrors.new_password"
                    required
                  />
                </div>

                <div>
                  <label for="confirm_password" class="block text-sm font-medium text-gray-700 dark:text-white mb-2">
                    Подтвердите пароль
                  </label>
                  <BaseInput
                    id="confirm_password"
                    v-model="passwordForm.confirm_password"
                    type="password"
                    placeholder="••••••••"
                    :error="passwordErrors.confirm_password"
                    required
                  />
                </div>
              </div>

              <div class="flex justify-end">
                <BaseButton 
                  type="submit" 
                  :loading="changingPassword"
                >
                  Изменить пароль
                </BaseButton>
              </div>
            </form>
          </div>
        </div>
      </div>

      <!-- Notifications Section -->
      <div class="grid grid-cols-1 gap-6 xl:grid-cols-2 mt-6">
        <!-- Alerts & Notifications -->
        <div class="bg-white rounded-lg shadow p-6 dark:bg-gray-800">
          <h3 class="text-xl font-semibold text-gray-900 dark:text-white mb-4">
            Уведомления и оповещения
          </h3>
          <p class="text-sm text-gray-500 dark:text-gray-400 mb-6">
            Настройте уведомления для получения важной информации
          </p>
          
          <form @submit.prevent="saveNotificationSettings" class="space-y-4">
            <div 
              v-for="notification in notificationSettings" 
              :key="notification.key"
              class="flex items-center justify-between py-4 border-b border-gray-200 dark:border-gray-700 last:border-b-0"
            >
              <div class="flex flex-col flex-grow">
                <div class="text-lg font-semibold text-gray-900 dark:text-white">
                  {{ notification.title }}
                </div>
                <div class="text-base text-gray-500 dark:text-gray-400">
                  {{ notification.description }}
                </div>
              </div>
              <label class="relative flex items-center cursor-pointer ml-4">
                <input 
                  v-model="notification.enabled"
                  type="checkbox" 
                  class="sr-only"
                >
                <div 
                  :class="[
                    'relative w-11 h-6 rounded-full transition-colors duration-200',
                    notification.enabled ? 'bg-blue-600' : 'bg-gray-200 dark:bg-gray-700'
                  ]"
                >
                  <div 
                    :class="[
                      'absolute top-0.5 left-0.5 w-5 h-5 bg-white rounded-full transition-transform duration-200',
                      notification.enabled ? 'transform translate-x-5' : ''
                    ]"
                  ></div>
                </div>
              </label>
            </div>
            
            <div class="flex justify-end pt-4">
              <BaseButton 
                type="submit" 
                :loading="savingNotifications"
              >
                Сохранить все
              </BaseButton>
            </div>
          </form>
        </div>

        <!-- Email Notifications -->
        <div class="bg-white rounded-lg shadow p-6 dark:bg-gray-800">
          <h3 class="text-xl font-semibold text-gray-900 dark:text-white mb-4">
            Email уведомления
          </h3>
          <p class="text-sm text-gray-500 dark:text-gray-400 mb-6">
            Настройте email уведомления для важных событий
          </p>
          
          <form @submit.prevent="saveEmailSettings" class="space-y-4">
            <div 
              v-for="email in emailSettings" 
              :key="email.key"
              class="flex items-center justify-between py-4 border-b border-gray-200 dark:border-gray-700 last:border-b-0"
            >
              <div class="flex flex-col flex-grow">
                <div class="text-lg font-semibold text-gray-900 dark:text-white">
                  {{ email.title }}
                </div>
                <div class="text-base text-gray-500 dark:text-gray-400">
                  {{ email.description }}
                </div>
              </div>
              <label class="relative flex items-center cursor-pointer ml-4">
                <input 
                  v-model="email.enabled"
                  type="checkbox" 
                  class="sr-only"
                >
                <div 
                  :class="[
                    'relative w-11 h-6 rounded-full transition-colors duration-200',
                    email.enabled ? 'bg-blue-600' : 'bg-gray-200 dark:bg-gray-700'
                  ]"
                >
                  <div 
                    :class="[
                      'absolute top-0.5 left-0.5 w-5 h-5 bg-white rounded-full transition-transform duration-200',
                      email.enabled ? 'transform translate-x-5' : ''
                    ]"
                  ></div>
                </div>
              </label>
            </div>
            
            <div class="flex justify-end pt-4">
              <BaseButton 
                type="submit" 
                :loading="savingEmails"
              >
                Сохранить все
              </BaseButton>
            </div>
          </form>
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
const showAvatarUpload = ref(false)
const deletingAvatar = ref(false)

// General Info
const savingGeneral = ref(false)
const generalError = ref('')
const generalSuccess = ref('')

const generalInfo = reactive({
  first_name: '',
  last_name: '',
  country: '',
  city: '',
  address: '',
  phone: '',
  birth_date: '',
  organization: '',
  role: '',
  department: '',
  zip_code: ''
})

const generalErrors = reactive({
  first_name: '',
  last_name: '',
  country: '',
  city: '',
  address: '',
  phone: '',
  birth_date: '',
  organization: '',
  role: '',
  department: '',
  zip_code: ''
})

// Password
const changingPassword = ref(false)
const passwordError = ref('')
const passwordSuccess = ref('')

const passwordForm = reactive({
  current_password: '',
  new_password: '',
  confirm_password: ''
})

const passwordErrors = reactive({
  current_password: '',
  new_password: '',
  confirm_password: ''
})

// Language Settings
const savingLanguage = ref(false)
const languageSettings = reactive({
  language: 'ru',
  timezone: 'UTC+3'
})

// Notifications
const savingNotifications = ref(false)
const notificationSettings = ref([
  {
    key: 'company_news',
    title: 'Новости компании',
    description: 'Получать новости, объявления и обновления продуктов',
    enabled: false
  },
  {
    key: 'account_activity',
    title: 'Активность аккаунта',
    description: 'Получать важные уведомления о активности или пропущенных событиях',
    enabled: true
  },
  {
    key: 'meetups',
    title: 'Встречи рядом',
    description: 'Получать email когда организуется встреча рядом с моим местоположением',
    enabled: true
  },
  {
    key: 'new_messages',
    title: 'Новые сообщения',
    description: 'Получать уведомления о новых сообщениях и обновлениях',
    enabled: false
  }
])

// Email Settings
const savingEmails = ref(false)
const emailSettings = ref([
  {
    key: 'rating_reminders',
    title: 'Напоминания о рейтингах',
    description: 'Отправлять email напоминание оценить курс через неделю после покупки',
    enabled: false
  },
  {
    key: 'item_updates',
    title: 'Обновления элементов',
    description: 'Отправлять уведомления пользователей и продуктов для вас',
    enabled: true
  },
  {
    key: 'item_comments',
    title: 'Комментарии к элементам',
    description: 'Отправлять мне email когда кто-то комментирует один из моих элементов',
    enabled: true
  },
  {
    key: 'buyer_reviews',
    title: 'Отзывы покупателей',
    description: 'Отправлять мне email когда кто-то оставляет отзыв с оценкой',
    enabled: false
  }
])

// Computed
const userProfile = computed(() => authStore.user)

const defaultAvatar = 'data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTAwIiBoZWlnaHQ9IjEwMCIgdmlld0JveD0iMCAwIDEwMCAxMDAiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjxyZWN0IHdpZHRoPSIxMDAiIGhlaWdodD0iMTAwIiBmaWxsPSIjRjNGNEY2Ii8+CjxwYXRoIGQ9Ik01MCA1MEMzNS43NSA1MCAyNS41IDQwLjI1IDI1LjUgMjZDMjUuNSAxMS43NSAzNS43NSAyIDUwIDJDNjQuMjUgMiA3NC41IDExLjc1IDc0LjUgMjZDNzQuNSA0MC4yNSA2NC4yNSA1MCA1MCA1MFpNNzQgNjJDNzkuNSA2MiA4NCA2Ni41IDg0IDcyVjg4QzY0IDk0IDM2IDk0IDE2IDg4VjcyQzE2IDY2LjUgMjAuNSA2MiAyNiA2Mkg3NFoiIGZpbGw9IiM5Q0E0QUYiLz4KPC9zdmc+'

// Methods
const loadUserData = () => {
  if (userProfile.value) {
    // Load general info
    generalInfo.first_name = userProfile.value.first_name || ''
    generalInfo.last_name = userProfile.value.last_name || ''
    generalInfo.country = userProfile.value.country || ''
    generalInfo.city = userProfile.value.city || ''
    generalInfo.address = userProfile.value.address || ''
    generalInfo.phone = userProfile.value.phone || ''
    generalInfo.birth_date = userProfile.value.birth_date || ''
    generalInfo.organization = userProfile.value.organization || ''
    generalInfo.role = userProfile.value.role || ''
    generalInfo.department = userProfile.value.department || ''
    generalInfo.zip_code = userProfile.value.zip_code || ''

    // Load preferences
    languageSettings.language = userProfile.value.language || 'ru'
    languageSettings.timezone = userProfile.value.timezone || 'UTC+3'
  }
}

const saveGeneralInfo = async () => {
  savingGeneral.value = true
  generalError.value = ''
  generalSuccess.value = ''
  
  // Clear field errors
  Object.keys(generalErrors).forEach(key => {
    generalErrors[key as keyof typeof generalErrors] = ''
  })

  try {
    await authStore.updateProfile(generalInfo)
    generalSuccess.value = 'Основная информация успешно обновлена'
    toast.success('Информация обновлена')
  } catch (err: any) {
    if (err.response?.data?.errors) {
      const errors = err.response.data.errors
      Object.keys(generalErrors).forEach(key => {
        generalErrors[key as keyof typeof generalErrors] = errors[key]?.[0] || ''
      })
    } else {
      generalError.value = err.response?.data?.message || 'Ошибка обновления информации'
    }
  } finally {
    savingGeneral.value = false
  }
}

const changePassword = async () => {
  changingPassword.value = true
  passwordError.value = ''
  passwordSuccess.value = ''
  
  // Clear field errors
  Object.keys(passwordErrors).forEach(key => {
    passwordErrors[key as keyof typeof passwordErrors] = ''
  })

  // Validate passwords match
  if (passwordForm.new_password !== passwordForm.confirm_password) {
    passwordErrors.confirm_password = 'Пароли не совпадают'
    changingPassword.value = false
    return
  }

  try {
    await authApi.changePassword({
      oldPassword: passwordForm.current_password,
      newPassword: passwordForm.new_password
    })
    
    passwordSuccess.value = 'Пароль успешно изменен'
    toast.success('Пароль изменен')
    
    // Clear form
    passwordForm.current_password = ''
    passwordForm.new_password = ''
    passwordForm.confirm_password = ''
  } catch (err: any) {
    if (err.response?.data?.errors) {
      const errors = err.response.data.errors
      passwordErrors.current_password = errors.old_password?.[0] || ''
      passwordErrors.new_password = errors.new_password?.[0] || ''
    } else {
      passwordError.value = err.response?.data?.message || 'Ошибка изменения пароля'
    }
  } finally {
    changingPassword.value = false
  }
}

const saveLanguageSettings = async () => {
  savingLanguage.value = true
  
  try {
    await authStore.updateProfile(languageSettings)
    toast.success('Настройки языка сохранены')
  } catch (err: any) {
    toast.error(err.response?.data?.message || 'Ошибка сохранения настроек')
  } finally {
    savingLanguage.value = false
  }
}

const saveNotificationSettings = async () => {
  savingNotifications.value = true
  
  try {
    // TODO: Implement notification settings API
    await new Promise(resolve => setTimeout(resolve, 1000))
    toast.success('Настройки уведомлений сохранены')
  } catch (err: any) {
    toast.error('Ошибка сохранения настроек уведомлений')
  } finally {
    savingNotifications.value = false
  }
}

const saveEmailSettings = async () => {
  savingEmails.value = true
  
  try {
    // TODO: Implement email settings API
    await new Promise(resolve => setTimeout(resolve, 1000))
    toast.success('Настройки email сохранены')
  } catch (err: any) {
    toast.error('Ошибка сохранения настроек email')
  } finally {
    savingEmails.value = false
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
    await authApi.uploadAvatar(file)
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

// Lifecycle
onMounted(() => {
  loadUserData()
})
</script>