<script lang="ts">
import type { PropType } from 'vue';
import type { PartScheme, CitationScheme, SectionScheme, EvangelistsScheme } from '@/interfaces/synopsisInterface';
import { useSynopsisStore } from "@/stores/SynopsisStore"

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
    redirectToLeadingCitation(chapterLocation: string, verseLocation: string): void {
      for (let i = 0; i < useSynopsisStore().currentSynopsis.parts.length; i++) {
        const part: PartScheme = useSynopsisStore().currentSynopsis.parts[i]
        for (let j = 0; j < part.sections.length; j++) {

          const section: SectionScheme = part.sections[j]
          for (let l = 0; l < section[this.evangelist as keyof SectionScheme].length; l++) {
            const citation = section[this.evangelist as keyof SectionScheme][l] as CitationScheme
            if (citation?.leading) {
              for (let m = 0; m < citation.content.length; m++) {
                const content = citation.content[m]
                const formattedVerse = content.verse.slice(-1) === "a" || content.verse.slice(-1) === "b" ? content.verse.slice(0, -1) : content.verse
                if (content.chapter === chapterLocation && formattedVerse === verseLocation) {
                  this.$router.push({ name: "synopsis", params: { language: this.synopsisStore.currentLanguage, translation: this.synopsisStore.currentTranslation }, hash: "#" + section.id })
                  return
                }
              }
            }
          }
        }
      }
    },
    redirectToPreviousLeadingCitation() {
      let previousSectionId;
      for (let i = 0; i < useSynopsisStore().currentSynopsis.parts.length; i++) {
        const part: PartScheme = useSynopsisStore().currentSynopsis.parts[i]
        for (let j = 0; j < part.sections.length; j++) {
          const section: SectionScheme = part.sections[j]
          for (let l = 0; l < section[this.evangelist as keyof SectionScheme].length; l++) {
            const citation = section[this.evangelist as keyof SectionScheme][l] as CitationScheme
            if (section.id === this.sectionId) {
              this.$router.push({ name: "synopsis", hash: "#" + previousSectionId })
              return
            }
            if (citation?.leading) {
              previousSectionId = section.id
            }
          }
        }
      }
    },
    redirectToNextLeadingCitation() {
      for (let i = 0; i < useSynopsisStore().currentSynopsis.parts.length; i++) {
        const part: PartScheme = useSynopsisStore().currentSynopsis.parts[i]
        for (let j = 0; j < part.sections.length; j++) {
          const section: SectionScheme = part.sections[j]
          for (let l = 0; l < section[this.evangelist as keyof SectionScheme].length; l++) {
            const citation = section[this.evangelist as keyof SectionScheme][l] as CitationScheme
            if (Number(section.id) > Number(this.sectionId) && citation?.leading) {
              this.$router.push({ name: "synopsis", hash: "#" + section.id })
              return
            }
          }
        }
      }
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
  <div class="card h-100" v-if="citation?.content" :class="{ 'shadow border-dark': citation.leading }">
    <div class="card-header sticky-top bg-light z-1">
      {{ synopsisStore.currentSynopsis.evangelists[evangelist as keyof EvangelistsScheme] }} {{
    synopsisStore.getCitation(citation.content[0].chapter, citation.content[0].verse,
      citation.content[citation.content.length - 1].chapter, citation.content[citation.content.length - 1].verse) }}
      <template v-if="!$route.params.id">
        <button v-if="!citation.leading"
          @click="redirectToLeadingCitation(citation.content[0].chapter, citation.content[0].verse)" type="button"
          class=" float-end btn  btn-sm py-0 m-0" :title="synopsisStore.currentDictionary.tooltips.jumpToMainText">

          <i class="bi bi-compass fs-6 text-secondary"></i>
        </button>

        <button v-if="citation.leading
    && !isLastSection(evangelist)" @click="redirectToNextLeadingCitation()" type="button"
          class=" float-end btn  btn-sm py-0 m-0" :title="synopsisStore.currentDictionary.tooltips.nextMainText">
          <i class="bi bi-arrow-down fs-6 text-secondary"></i>
        </button>
        <button v-if="citation.leading && sectionId !== '1'" @click="redirectToPreviousLeadingCitation()" type="button"
          class=" float-end btn  btn-sm py-0 m-0" :title="synopsisStore.currentDictionary.tooltips.previousMainText">
          <i class="bi bi-arrow-up fs-6 text-secondary"></i>
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