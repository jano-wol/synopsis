<script lang="ts">
import type { PropType } from 'vue';
import type { PartScheme, CitationScheme, SectionScheme, EvangelistsScheme } from '@/interfaces/synopsisInterface';
import { useSynopsisStore } from "@/stores/SynopsisStore"
import toLeading from "@/assets/redirect/toLeading.json"
import toPrevious from "@/assets/redirect/toPrevious.json"
import toNext from "@/assets/redirect/toNext.json"

export default {
  data() {
    return {
      synopsisStore: useSynopsisStore(),
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
    redirectToLeadingCitation(citation: string): void {
      this.synopsisStore.pushToHistoryAndRedirect(
        { name: "synopsis", params: { language: this.synopsisStore.currentLanguage, translation: this.synopsisStore.currentTranslation }, hash: "#" + this.sectionId },
        { name: "synopsis", params: { language: this.synopsisStore.currentLanguage, translation: this.synopsisStore.currentTranslation }, hash: "#" + toLeading[citation] }
      )
    },
    redirectToPreviousLeadingCitation(citation: string) {
      this.synopsisStore.pushToHistoryAndRedirect(
        { name: "synopsis", params: { language: this.synopsisStore.currentLanguage, translation: this.synopsisStore.currentTranslation }, hash: "#" + this.sectionId },
        { name: "synopsis", params: { language: this.synopsisStore.currentLanguage, translation: this.synopsisStore.currentTranslation }, hash: "#" + toPrevious[citation] }
      )
    },
    redirectToNextLeadingCitation(citation: string) {
      this.synopsisStore.pushToHistoryAndRedirect(
        { name: "synopsis", params: { language: this.synopsisStore.currentLanguage, translation: this.synopsisStore.currentTranslation }, hash: "#" + this.sectionId },
        { name: "synopsis", params: { language: this.synopsisStore.currentLanguage, translation: this.synopsisStore.currentTranslation }, hash: "#" + toNext[citation] }
      )
    },
    isLastSection(evangelist: string) {
      return ((evangelist === 'mt' && this.sectionId === '364')
        || (evangelist === 'mk' && this.sectionId === '363')
        || (evangelist === 'lk' && this.sectionId === '365')
        || (evangelist === 'jn' && this.sectionId === '367')
      )
    }
  }
}
</script>

<template>
  <div class="card h-100" v-if="citation?.content" :class="{ 'shadow border-2 border-secondary bg-body-tertiary': citation.leading }">
    <div class="card-header bg-white z-1" :class="{ 'bg-dark-subtle': citation.leading }">
      {{ synopsisStore.currentSynopsis.evangelists[evangelist as keyof EvangelistsScheme] }} {{
    synopsisStore.getCitation(citation.content[0].chapter, citation.content[0].verse,
      citation.content[citation.content.length - 1].chapter, citation.content[citation.content.length - 1].verse) }}
      <template v-if="!$route.params.id">
        <button v-if="!citation.leading"
          @click="redirectToLeadingCitation(
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
    && !isLastSection(evangelist)" @click="redirectToNextLeadingCitation(
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
        <button v-if="citation.leading && sectionId !== '1'" @click="redirectToPreviousLeadingCitation(
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
    <div class="card-body">
      <p>
        <template v-for="verse in citation?.content" :key="verse.chapter+','+verse.verse">
          {{ " " }}<sup class="text-secondary">{{ verse.verse }}</sup>{{ verse.text }}
        </template>
      </p>
    </div>
  </div>
</template>