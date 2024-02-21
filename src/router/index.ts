import { createRouter, createWebHistory } from 'vue-router'
import SynopsisView from '@/views/SynopsisView.vue'
import IndexView from '@/views/IndexView.vue'
import DetailsView from '@/views/DetailsView.vue'
import DescriptionView from '@/views/DescriptionView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'synopsis',
      component: SynopsisView
    },
    {
      path: '/description',
      name: 'description',
      component: DescriptionView
    },
    {
      path: '/index',
      name: 'index',
      component: IndexView
    },
    {
      path: '/details',
      name: 'details',
      component: DetailsView
    },
  ],
  scrollBehavior(to, from, savedPosition) {
    if (to.hash) {
      return {
        el: to.hash,
      }
    }
  },
})

export default router
