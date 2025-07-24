import { createRouter, createWebHistory } from 'vue-router'
import type { RouteRecordRaw } from 'vue-router'
import { useAuthStore } from '../stores/auth'

// Define routes
const routes: RouteRecordRaw[] = [
  // Main page
  {
    path: '/',
    name: 'Home',
    component: () => import('../../pages/IndexPage.vue'),
    meta: { title: 'AiKademiya - Генерация курсов с ИИ' }
  },
  
  // Authentication pages
  {
    path: '/login',
    name: 'Login',
    component: () => import('../pages/auth/LoginPage.vue'),
    meta: { title: 'Вход - AiKademiya', requiresGuest: true }
  },
  
  {
    path: '/register',
    name: 'Register',
    component: () => import('../pages/auth/RegisterPage.vue'),
    meta: { title: 'Регистрация - AiKademiya', requiresGuest: true }
  },
  
  {
    path: '/forgot-password',
    name: 'ForgotPassword',
    component: () => import('../pages/auth/ForgotPasswordPage.vue'),
    meta: { title: 'Восстановление пароля - AiKademiya', requiresGuest: true }
  },
  
  // Protected pages
  {
    path: '/generate',
    name: 'Generate',
    component: () => import('../../components/GeneratePage.vue'),
    meta: { title: 'Создать курс - AiKademiya', requiresAuth: true }
  },
  
  {
    path: '/learn',
    name: 'Learn',
    component: () => import('../pages/LearnPage.vue'),
    meta: { title: 'Обучение - AiKademiya', requiresAuth: true }
  },
  
  {
    path: '/profile',
    name: 'Profile',
    component: () => import('../pages/ProfilePage.vue'),
    meta: { title: 'Профиль - AiKademiya', requiresAuth: true }
  },
  
  {
    path: '/settings',
    name: 'Settings',
    component: () => import('../pages/SettingsPage.vue'),
    meta: { title: 'Настройки - AiKademiya', requiresAuth: true }
  },

  // Catch all 404
  {
    path: '/:pathMatch(.*)*',
    name: 'NotFound',
    component: () => import('../../pages/IndexPage.vue'),
    meta: { title: 'Страница не найдена - AiKademiya' }
  }
]

// Create router
const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition
    }
    if (to.hash) {
      return { el: to.hash }
    }
    return { top: 0 }
  }
})

// Navigation guards
router.beforeEach(async (to, from, next) => {
  const authStore = useAuthStore()
  
  // Set page title
  if (to.meta.title) {
    document.title = to.meta.title as string
  }
  
  // Check authentication requirements
  if (to.meta.requiresAuth && !authStore.isAuthenticated) {
    next('/login')
    return
  }
  
  // Redirect authenticated users away from auth pages
  if (to.meta.requiresGuest && authStore.isAuthenticated) {
    next('/')
    return
  }
  
  next()
})

export default router