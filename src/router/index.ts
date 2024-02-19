import { createRouter, createWebHistory } from 'vue-router'
import SynopsisView from '../views/SynopsisView.vue'
import IndexViewVue from '@/views/IndexView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'synopsis',
      component: SynopsisView
    },
    {
      path: '/index',
      name: 'index',
      component: IndexViewVue
    },
  ]
})

export default router
