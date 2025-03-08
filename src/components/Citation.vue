<script lang="ts">
import type { PropType } from 'vue';
import type { CitationScheme, SectionScheme, EvangelistsScheme } from '@/interfaces/synopsisInterface';
import { useSynopsisStore } from "@/stores/SynopsisStore"
import { Redirection } from "@/enums/Redirection"
import toLeading from "@/assets/redirect/toLeading.json"
import toPrevious from "@/assets/redirect/toPrevious.json"
import toNext from "@/assets/redirect/toNext.json"

export default {
  data() {
    return {
      synopsisStore: useSynopsisStore(),
      redirection: Redirection
    }
  },
  props: {
    evangelist: {
      type: String,
      required: true,
    },
    citation: {
      type: Object as PropType<CitationScheme | null>,
      required: true
    },
    sectionId: {
      type: String,
      required: true
    },
  },
  methods: {
    redirectToCitation(redirection: Redirection, citation: string): void {
      let redirectionSectionId = 0
      switch (redirection) {
        case Redirection.TO_LEADING:
          redirectionSectionId = toLeading[citation as keyof typeof toLeading]
          break
        case Redirection.TO_PREVIOUS:
          redirectionSectionId = toPrevious[citation as keyof typeof toPrevious]
          break
        case Redirection.TO_NEXT:
          redirectionSectionId = toNext[citation as keyof typeof toNext]
          break
      }
      this.synopsisStore.pushToHistoryAndRedirect(
        { name: "synopsis", hash: "#" + this.sectionId },
        { name: "synopsis", hash: "#" + redirectionSectionId }
      )
    },
    isLastSection(evangelist: string) {
      return ((evangelist === 'mt' && this.sectionId === '364')
        || (evangelist === 'mk' && this.sectionId === '363')
        || (evangelist === 'lk' && this.sectionId === '365')
        || (evangelist === 'jn' && this.sectionId === '367')
      )
    }
  },
  computed: {
    spanClass() {
      return (evangelist: string, chapter:string, verse:string) => {
        const isInDateGospel = this.synopsisStore.isQuoteInGospel(evangelist, chapter, verse);
        if (isInDateGospel) {
          return "bg-warning-subtle"
        }
        return '';
      };
    },
  },
}
</script>

<template>
  <div class="card h-100" v-if="citation?.content" :class="{ 'shadow border-2 border-secondary bg-body-tertiary': citation.leading }">
    <div class="card-header bg-white z-1" :class="{ 'bg-dark-subtle': citation.leading }">
      {{ synopsisStore.currentSynopsis.evangelists[evangelist as keyof EvangelistsScheme] }} {{
    synopsisStore.getCitation(citation.content[0].chapter, citation.content[0].verse,
      citation.content[citation.content.length - 1].chapter, citation.content[citation.content.length - 1].verse) }}
      <template v-if="$route.name === 'synopsis'">
        <button v-if="!citation.leading"
          @click="redirectToCitation(redirection.TO_LEADING,
                    evangelist +
                    synopsisStore.getCitation(
                      citation.content[0].chapter,
                      citation.content[0].verse,
                      citation.content[citation.content.length - 1].chapter,
                      citation.content[citation.content.length - 1].verse)
                    )"
          type="button" class=" float-end btn  btn-sm py-0 m-0" :title="synopsisStore.currentDictionary.tooltips.jumpToMainText">

          <i class="bi bi-compass fs-6 text-secondary"></i>
        </button>

        <button v-if="citation.leading
    && !isLastSection(evangelist)" @click="redirectToCitation(redirection.TO_NEXT,
                    evangelist +
                    synopsisStore.getCitation(
                      citation.content[0].chapter,
                      citation.content[0].verse,
                      citation.content[citation.content.length - 1].chapter,
                      citation.content[citation.content.length - 1].verse)
                    )"
          type="button" class=" float-end btn  btn-sm py-0 m-0" :title="synopsisStore.currentDictionary.tooltips.nextMainText">
          <i class="bi bi-arrow-down fs-6"></i>
        </button>
        <button v-if="citation.leading && sectionId !== '1'"
                  @click="redirectToCitation(redirection.TO_PREVIOUS,
                    evangelist +
                    synopsisStore.getCitation(
                      citation.content[0].chapter,
                      citation.content[0].verse,
                      citation.content[citation.content.length - 1].chapter,
                      citation.content[citation.content.length - 1].verse)
                    )"
          type="button" class=" float-end btn  btn-sm py-0 m-0" :title="synopsisStore.currentDictionary.tooltips.previousMainText">
          <i class="bi bi-arrow-up fs-6"></i>
        </button>
      </template>

    </div>
    <!-- TODO: verse.verse not good -->
    <div class="card-body">
      <p>
        <template v-for="verse in citation?.content" :key="verse.chapter+','+verse.verse">
          <span :class="spanClass(evangelist, verse.chapter, verse.verse)">{{ " " }}<sup class="text-secondary">{{ verse.verse }}</sup>{{ verse.text }}</span>
        </template>
      </p>
    </div>
  </div>
</template>