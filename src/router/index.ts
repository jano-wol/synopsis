import { createRouter, createWebHistory } from 'vue-router'
import SynopsisView from '@/views/SynopsisView.vue'
import IndexView from '@/views/IndexView.vue'
import SourcesView from '@/views/SourcesView.vue'
import AboutView from '@/views/AboutView.vue'
import ContactView from '@/views/ContactView.vue'
import NotFoundView from '@/views/NotFoundView.vue'
import Section from '@/components/Section.vue'
import { useSynopsisStore } from "@/stores/SynopsisStore"

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/:language(hu|en)/:translation(SZIT|ESV)',
      alias: '/',
      name: 'synopsis',
      component: SynopsisView
    },
    {
      path: '/:language(hu|en)/about',
      name: 'about',
      component: AboutView
    },
    {
      path: '/:language(hu|en)/:translation(SZIT|ESV)/index',
      name: 'index',
      component: IndexView
    },
    {
      path: '/:language(hu|en)/sources',
      name: 'sources',
      component: SourcesView
    },
    {
      path: '/:language(hu|en)/contact',
      name: 'contact',
      component: ContactView
    },
    {
      path: '/:language(hu|en)/:translation(SZIT|ESV)/:id([1-9]|[1-9]\\d|[12]\\d{2}|3[0-5]\\d|36[0-7])',
      name: 'section',
      component: Section,
      props: true
    }, {
      path: '/:param(.*)*',
      name: 'notFound',
      component: NotFoundView
    },
  ],
  scrollBehavior(to) {
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

router.beforeEach((to) => {
  useSynopsisStore().setupLanguage(to.params.language)
  useSynopsisStore().setupTranslation(to.params.translation)
})
export default router
