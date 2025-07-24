import { createRouter, createWebHistory } from 'vue-router'
import type { RouteRecordRaw } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

// Import layouts
import AppLayout from '@/layouts/AppLayout.vue'
import AuthLayout from '@/layouts/AuthLayout.vue'
import PublicLayout from '@/layouts/PublicLayout.vue'

// Define routes
const routes: RouteRecordRaw[] = [
  // Public routes
  {
    path: '/',
    component: PublicLayout,
    children: [
      {
        path: '',
        name: 'Home',
        component: () => import('@/pages/HomePage.vue'),
        meta: { title: 'AiKademiya - Генерация курсов с ИИ' }
      },
      {
        path: '/about',
        name: 'About',
        component: () => import('@/pages/AboutPage.vue'),
        meta: { title: 'О нас - AiKademiya' }
      },
      {
        path: '/pricing',
        name: 'Pricing',
        component: () => import('@/pages/PricingPage.vue'),
        meta: { title: 'Тарифы - AiKademiya' }
      },
      {
        path: '/catalog',
        name: 'Catalog',
        component: () => import('@/pages/CatalogPage.vue'),
        meta: { title: 'Каталог курсов - AiKademiya' }
      },
    ]
  },

  // Authentication routes
  {
    path: '/auth',
    component: AuthLayout,
    meta: { requiresGuest: true },
    children: [
      {
        path: '/login',
        name: 'Login',
        component: () => import('@/pages/auth/LoginPage.vue'),
        meta: { title: 'Вход - AiKademiya' }
      },
      {
        path: '/register',
        name: 'Register',
        component: () => import('@/pages/auth/RegisterPage.vue'),
        meta: { title: 'Регистрация - AiKademiya' }
      },
      {
        path: '/forgot-password',
        name: 'ForgotPassword',
        component: () => import('@/pages/auth/ForgotPasswordPage.vue'),
        meta: { title: 'Восстановление пароля - AiKademiya' }
      },
      {
        path: '/reset-password/:token',
        name: 'ResetPassword',
        component: () => import('@/pages/auth/ResetPasswordPage.vue'),
        meta: { title: 'Новый пароль - AiKademiya' }
      },
    ]
  },

  // Protected app routes
  {
    path: '/app',
    component: AppLayout,
    meta: { requiresAuth: true },
    children: [
      // Dashboard
      {
        path: '/dashboard',
        name: 'Dashboard',
        component: () => import('@/pages/dashboard/DashboardPage.vue'),
        meta: { title: 'Панель управления - AiKademiya' }
      },

      // Courses
      {
        path: '/courses',
        name: 'Courses',
        component: () => import('@/pages/course/CoursesPage.vue'),
        meta: { title: 'Мои курсы - AiKademiya' }
      },
      {
        path: '/course/:id',
        name: 'CourseDetail',
        component: () => import('@/pages/course/CourseDetailPage.vue'),
        meta: { title: 'Курс - AiKademiya' }
      },
      {
        path: '/generate',
        name: 'GenerateCourse',
        component: () => import('@/pages/course/GenerateCoursePage.vue'),
        meta: { title: 'Создать курс - AiKademiya' }
      },
      {
        path: '/status/:workflowId',
        name: 'GenerationStatus',
        component: () => import('@/pages/course/GenerationStatusPage.vue'),
        meta: { title: 'Статус генерации - AiKademiya' }
      },

      // Learning
      {
        path: '/learn',
        name: 'Learn',
        component: () => import('@/pages/LearnPage.vue'),
        meta: { title: 'Обучение - AiKademiya' }
      },
      {
        path: '/enrolled',
        name: 'EnrolledCourses',
        component: () => import('@/pages/course/EnrolledCoursesPage.vue'),
        meta: { title: 'Мое обучение - AiKademiya' }
      },

      // Profile
      {
        path: '/profile',
        name: 'Profile',
        component: () => import('@/pages/ProfilePage.vue'),
        meta: { title: 'Профиль - AiKademiya' }
      },
      {
        path: '/settings',
        name: 'Settings',
        component: () => import('@/pages/SettingsPage.vue'),
        meta: { title: 'Настройки - AiKademiya' }
      },
    ]
  },

  // Catch all 404
  {
    path: '/:pathMatch(.*)*',
    name: 'NotFound',
    component: () => import('@/pages/NotFoundPage.vue'),
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

  // Check if route requires authentication
  if (to.meta.requiresAuth) {
    if (!authStore.isAuthenticated) {
      next({ 
        name: 'Login', 
        query: { redirect: to.fullPath } 
      })
      return
    }
  }

  // Check if route requires guest (unauthenticated) user
  if (to.meta.requiresGuest) {
    if (authStore.isAuthenticated) {
      next({ name: 'Dashboard' })
      return
    }
  }

  next()
})

export default router