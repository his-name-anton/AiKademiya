import { createRouter, createWebHistory } from 'vue-router'
import type { RouteRecordRaw } from 'vue-router'

// Define routes
const routes: RouteRecordRaw[] = [
  // Main page
  {
    path: '/',
    name: 'Home',
    component: () => import('../../pages/IndexPage.vue'),
    meta: { title: 'AiKademiya - Генерация курсов с ИИ' }
  },
  
  // Generate page
  {
    path: '/generate',
    name: 'Generate',
    component: () => import('../../components/GeneratePage.vue'),
    meta: { title: 'Создать курс - AiKademiya' }
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
  // Set page title
  if (to.meta.title) {
    document.title = to.meta.title as string
  }
  next()
})

export default router