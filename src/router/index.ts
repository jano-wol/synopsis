import { createRouter, createWebHistory } from 'vue-router'
import SynopsisView from '@/views/SynopsisView.vue'
import IndexView from '@/views/IndexView.vue'
import SourcesView from '@/views/SourcesView.vue'
import AboutView from '@/views/AboutView.vue'
import DevelopmentView from '@/views/DevelopmentView.vue'
import NotFoundView from '@/views/NotFoundView.vue'
import Subsection from '@/components/Subsection.vue'
import { useSynopsisStore } from "@/stores/SynopsisStore"

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'synopsis',
      component: SynopsisView
    },
    {
      path: '/about',
      name: 'about',
      component: AboutView
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
      path: '/development',
      name: 'development',
      component: DevelopmentView
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

router.beforeEach(() => {
  useSynopsisStore().setupLanguage(localStorage.getItem("lang"))
})
export default router
