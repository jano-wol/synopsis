import { createRouter, createWebHistory } from 'vue-router'
import SynopsisView from '@/views/SynopsisView.vue'
import IndexView from '@/views/IndexView.vue'
import SourcesView from '@/views/SourcesView.vue'
import AboutView from '@/views/AboutView.vue'
import ContactView from '@/views/ContactView.vue'
import NotFoundView from '@/views/NotFoundView.vue'
import Section from '@/components/Section.vue'
import { useSynopsisStore } from "@/stores/SynopsisStore"

const languageOptionsRegex = "(hu|en)"
const translationOptionsRegex = "(KG|SZIT|KNB|UF|ESV|BT)"
function defaultLanguage(){
  const timeZone = Intl.DateTimeFormat().resolvedOptions().timeZone
  if (timeZone === "Europe/Budapest")
  {
    return "/hu/KG"
  }
  return "/en/ESV"
}

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      redirect: defaultLanguage(),
    },
    {
      path: `/:language${languageOptionsRegex}/:translation${translationOptionsRegex}`,
      name: 'synopsis',
      component: SynopsisView
    },
    {
      path: `/:language${languageOptionsRegex}/about`,
      name: 'about',
      component: AboutView
    },
    {
      path: `/:language${languageOptionsRegex}/:translation${translationOptionsRegex}/index`,
      name: 'index',
      component: IndexView
    },
    {
      path: `/:language${languageOptionsRegex}/sources`,
      name: 'sources',
      component: SourcesView
    },
    {
      path: `/:language${languageOptionsRegex}/contact`,
      name: 'contact',
      component: ContactView
    },
    {
      path: `/:language${languageOptionsRegex}/:translation${translationOptionsRegex}/:id([1-9]|[1-9]\\d|[12]\\d{2}|3[0-5]\\d|36[0-7])`,
      name: 'section',
      component: Section,
      props: true
    }, {
      path: '/:param(.*)*',
      name: 'notFound',
      component: NotFoundView
    },
  ],
  scrollBehavior(to, from) {
    if (to.hash) {
      return {
        el: to.hash,
      }
    }

    if (to.name !== from.name) {
      setTimeout(() => {
      window.scrollTo(0, 0);
    }, 0);
    }
  },
})

router.beforeEach((to) => {
  useSynopsisStore().setupLanguage(to.params.language)
  useSynopsisStore().setupTranslation(to.params.translation)
})
export default router
