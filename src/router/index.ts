import { createRouter, createWebHistory } from 'vue-router'
import SynopsisView from '@/views/SynopsisView.vue'
import IndexView from '@/views/IndexView.vue'
import DetailsView from '@/views/DetailsView.vue'
import DescriptionView from '@/views/DescriptionView.vue'
import DevelopersView from '@/views/DevelopersView.vue'
import Subsection from '@/components/Subsection.vue'

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
    {
      path: '/developers',
      name: 'developers',
      component: DevelopersView
    },
    {
      path: '/:id',
      name: 'subsection',
      component: Subsection,
      props: true
    },
  ],
  scrollBehavior(to, from, savedPosition) {
    if (to.hash) {
      return {
        el: to.hash,
      }
    }
    else{
      return {top: 1}
    }
  },
})

export default router
