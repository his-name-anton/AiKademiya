import { createRouter, createWebHistory } from 'vue-router'

import IndexPage from '@/pages/IndexPage.vue'
// здесь ты позже добавишь другие страницы

const routes = [
  {
    path: '/',
    name: 'Home',
    component: IndexPage
  },
  // пример для будущих страниц:
  // {
  //   path: '/courses',
  //   name: 'Courses',
  //   component: () => import('@/pages/CourseCatalog.vue')
  // }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
