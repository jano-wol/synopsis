import { createRouter, createWebHistory } from 'vue-router'
import SynopsisView from '../views/SynopsisView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'synopsis',
      component: SynopsisView
    },
  ]
})

export default router
