import { createRouter, createWebHistory } from 'vue-router'
import type { RouteRecordRaw } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

// Define routes
const routes: RouteRecordRaw[] = [
  // Main page
  {
    path: '/',
    name: 'Home',
    component: () => import('@/pages/IndexPage.vue'),
    meta: { title: 'AiKademiya - Генерация курсов с ИИ' }
  },
  
  // Authentication pages
  {
    path: '/login',
    name: 'Login',
    component: () => import('@/pages/auth/LoginPage.vue'),
    meta: { title: 'Вход - AiKademiya', requiresGuest: true }
  },
  
  {
    path: '/register',
    name: 'Register',
    component: () => import('@/pages/auth/RegisterPage.vue'),
    meta: { title: 'Регистрация - AiKademiya', requiresGuest: true }
  },
  
  {
    path: '/forgot-password',
    name: 'ForgotPassword',
    component: () => import('@/pages/auth/ForgotPasswordPage.vue'),
    meta: { title: 'Восстановление пароля - AiKademiya', requiresGuest: true }
  },
  
  // Protected pages with sidebar layout
  {
    path: '/generate',
    name: 'Generate',
    component: () => import('@/components/GeneratePage.vue'),
    meta: { title: 'Создать курс - AiKademiya', requiresAuth: true, layout: 'auth' }
  },
  
  {
    path: '/learn',
    name: 'Learn',
    component: () => import('@/pages/LearnPage.vue'),
    meta: { title: 'Обучение - AiKademiya', requiresAuth: true, layout: 'auth' }
  },
  
  {
    path: '/profile',
    name: 'Profile',
    component: () => import('@/pages/ProfilePage.vue'),
    meta: { title: 'Профиль - AiKademiya', requiresAuth: true, layout: 'auth' }
  },
  
  {
    path: '/settings',
    name: 'Settings',
    component: () => import('@/pages/SettingsPage.vue'),
    meta: { title: 'Настройки - AiKademiya', requiresAuth: true, layout: 'auth' }
  },

  // Additional protected pages
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: () => import('@/pages/DashboardPage.vue'),
    meta: { title: 'Панель управления - AiKademiya', requiresAuth: true, layout: 'auth' }
  },

  {
    path: '/catalog',
    name: 'Catalog',
    component: () => import('@/pages/CatalogPage.vue'),
    meta: { title: 'Каталог курсов - AiKademiya', requiresAuth: true, layout: 'auth' }
  },

  {
    path: '/messages',
    name: 'Messages',
    component: () => import('@/pages/MessagesPage.vue'),
    meta: { title: 'Сообщения - AiKademiya', requiresAuth: true, layout: 'auth' }
  },

  {
    path: '/security',
    name: 'Security',
    component: () => import('@/pages/SecurityPage.vue'),
    meta: { title: 'Безопасность - AiKademiya', requiresAuth: true, layout: 'auth' }
  },

  {
    path: '/docs',
    name: 'Docs',
    component: () => import('@/pages/DocsPage.vue'),
    meta: { title: 'Документация - AiKademiya', requiresAuth: true, layout: 'auth' }
  },

  {
    path: '/components',
    name: 'Components',
    component: () => import('@/pages/ComponentsPage.vue'),
    meta: { title: 'Компоненты - AiKademiya', requiresAuth: true, layout: 'auth' }
  },

  {
    path: '/help',
    name: 'Help',
    component: () => import('@/pages/HelpPage.vue'),
    meta: { title: 'Помощь - AiKademiya', requiresAuth: true, layout: 'auth' }
  },

  // Catch all 404
  {
    path: '/:pathMatch(.*)*',
    name: 'NotFound',
    component: () => import('@/pages/IndexPage.vue'),
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
  // Wait for auth initialization before checking auth state
  if (!authStore.isInitialized) {
    console.log('Auth not initialized in router, waiting...')
    try {
      await authStore.initializeAuth()
    } catch (error) {
      console.error('Failed to initialize auth in router:', error)
      authStore.clearAuthData()
    }
  }
  // Set page title
  if (to.meta.title) {
    document.title = to.meta.title as string
  }
  
  // Wait for auth initialization if not already done
  if (!authStore.isInitialized) {
    console.log('⏳ Auth store not initialized yet, waiting for initialization...');
    try {
      await authStore.initializeAuth();
      console.log('✅ Auth store initialization completed in router guard');
    } catch (error) {
      console.error('❌ Auth initialization failed in router guard:', error);
    }
  }
  
  // Check authentication requirements
  if (to.meta.requiresAuth && !authStore.isAuthenticated) {
    console.log('🚫 Route requires auth but user not authenticated, redirecting to login');
    next('/login')
    return
  }
  
  // Redirect authenticated users away from auth pages
  if (to.meta.requiresGuest && authStore.isAuthenticated) {
    console.log('Authenticated user trying to access guest page, redirecting to dashboard')
    next('/dashboard')
    return
  }
  
  console.log('✅ Router guard: allowing navigation to', to.path);
  next()
})

export default router