import { createRouter, createWebHistory } from 'vue-router'
import SynopsisView from '@/views/SynopsisView.vue'
import IndexView from '@/views/IndexView.vue'
import DateGospelView from '@/views/DateGospelView.vue'
import SourcesView from '@/views/SourcesView.vue'
import AboutView from '@/views/AboutView.vue'
import ContactView from '@/views/ContactView.vue'
import NotFoundView from '@/views/NotFoundView.vue'
import Section from '@/components/Section.vue'
import DailyGospelView from '@/components/DailyGospelView.vue'
import { useSynopsisStore } from "@/stores/SynopsisStore"

const options: { [key: string]: string[] } = {
  "hu": ["SZIT", "KG", "KNB", "RUF"],
  "en": ["ESV", "EU", "BT", "BJW", "RSP", "SBLGNT", "NV"]
}

const languageDefaultRedirect = (path : string) =>
  Object.keys(options).map(language => ({
    path: `/${language}/${path}`,
    redirect: `/${language}/${options[language][0]}/${path}`
  }));

const translationDefaultRedirect = (path : string) =>
  Object.entries(options).flatMap(([language, versions]) =>
    versions.map(version => ({
      path: `/${version}/${path}`,
      redirect: `/${language}/${version}/${path}`
    }))
  );

const languageOptionsRegex = `(${Object.keys(options).join("|")})`;
const translationOptionsRegex = `(${Object.values(options).flat().join("|")})`;
function defaultLanguage() {
  const timeZone = Intl.DateTimeFormat().resolvedOptions().timeZone
  if (timeZone === "Europe/Budapest") {
    return `/hu/${options.hu[0]}`
  }
  if (timeZone === "Europe/Warsaw Poland") {
    return "/en/BT"
  }
  return `/en/${options.en[0]}`
}

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      redirect: defaultLanguage(),
    },
    ...languageDefaultRedirect(''),
    ...translationDefaultRedirect(''),
    {
      path: `/:language${languageOptionsRegex}?/:translation${translationOptionsRegex}?`,
      name: 'synopsis',
      component: SynopsisView
    },
    ...languageDefaultRedirect('index'),
    ...translationDefaultRedirect('index'),
    {
      path: `/:language${languageOptionsRegex}?/about`,
      name: 'about',
      component: AboutView
    },
    {
      path: `/:language${languageOptionsRegex}?/:translation${translationOptionsRegex}?/index`,
      name: 'index',
      component: IndexView
    },
    ...languageDefaultRedirect('calendar/today'),
    ...translationDefaultRedirect('calendar/today'),
    {
      path: `/:language${languageOptionsRegex}?/:translation${translationOptionsRegex}?/calendar/today`,
      name: 'today',
      component: DailyGospelView
    },
    {
      path: `/:language${languageOptionsRegex}?/:translation${translationOptionsRegex}?/calendar/:date`,
      name: 'calendar',
      component: DateGospelView
    },
    {
      path: `/:language${languageOptionsRegex}?/sources`,
      name: 'sources',
      component: SourcesView
    },
    {
      path: `/:language${languageOptionsRegex}?/contact`,
      name: 'contact',
      component: ContactView
    },
    {
      path: `/:language${languageOptionsRegex}?/:translation${translationOptionsRegex}?/:id([1-9]|[1-9]\\d|[12]\\d{2}|3[0-5]\\d|36[0-7])`,
      name: 'section',
      component: Section,
      props: true
    },
    {
      path: '/:param(.*)*',
      name: 'notFound',
      component: NotFoundView
    },
  ],
  scrollBehavior(to, from) {
    if (to.hash) {
      const el = window.location.href.split("#")[1];
      if (el.length) {
        const element = document.getElementById(el);
        if (element) {
          const elementPosition = element.getBoundingClientRect().top + window.scrollY;

          const offset = 60;
          window.scrollTo({
            top: elementPosition - offset,
            behavior: 'smooth'
          });
          return
        }
      }
    }

    if (to.name !== from.name) {
      setTimeout(() => {
        window.scrollTo(0, 0);
      }, 0);
    }
  },
})

router.beforeEach((to, from, next) => {
  useSynopsisStore().setupLanguage(to.params.language)
  useSynopsisStore().setupTranslation(to.params.translation, options)

  const requiresLanguage = to.matched.some((record) => {
    return record.path.includes(`/:language${languageOptionsRegex}?`);
  });
  const requiresTranslation = to.matched.some((record) => {
    return record.path.includes(`/:translation${translationOptionsRegex}?`);
  });
  const params = { ...to.params }
  if (requiresLanguage)
  {
    params.language = useSynopsisStore().currentLanguage
  }
  if (requiresTranslation)
  {
    params.translation = useSynopsisStore().currentTranslation
  }


  if (params.language !== to.params.language || params.translation !== to.params.translation) {
    next({ ...to, params: params });
  } else {
    next();
  }

})
export default router
