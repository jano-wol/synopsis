import { createRouter, createWebHistory } from 'vue-router'
import SynopsisView from '@/views/SynopsisView.vue'
import IndexView from '@/views/IndexView.vue'
import SourcesView from '@/views/SourcesView.vue'
import DescriptionView from '@/views/DescriptionView.vue'
import DevelopersView from '@/views/DevelopersView.vue'
import NotFoundView from '@/views/NotFoundView.vue'
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
      path: '/sources',
      name: 'sources',
      component: SourcesView
    },
    {
      path: '/developers',
      name: 'developers',
      component: DevelopersView
    },
    {
      path: '/:id([1-9]|[1-9]\\d|[12]\\d{2}|3[0-5]\\d|36[0-7])',
      name: 'subsection',
      component: Subsection,
      props: true
    }, {
      path: '/:param(\.*)',
      name: 'tmp',
      component: NotFoundView
    },
  ],
  scrollBehavior(to, from, savedPosition) {
    if (to.hash) {
      return {
        el: to.hash,
      }
    }
    else {
      return { top: 1 }
    }
  },
})

export default router
