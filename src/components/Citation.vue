<script lang="ts">
import type { PropType } from 'vue';
import type { CitationScheme } from '@/interfaces/synopsisInterface';
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
      for (let i = 0; i < useSynopsisStore().currentSynopsis.chapters.length; i++) {
        //TODO: think about better name than chapter in .json
        const chapter = useSynopsisStore().currentSynopsis.chapters[i]
        for (let j = 0; j < chapter.subchapters.length; j++) {
          const subchapter = chapter.subchapters[j]
          for (let k = 0; k < subchapter.sections.length; k++) {
            const section = subchapter.sections[k]
            //TODO: remove hacky solution.
            const evangelist = this.evangelist === "mt" ? "mt" : (this.evangelist === "mk" ? "mk" : (this.evangelist === "lk" ? "lk" : "jn"))
            // TODO: this.evangelist not type correct for some reason.
            for (let l = 0; l < section[evangelist].length; l++) {
              const citation = section[evangelist][l]
              if (citation?.leading) {
                for (let m = 0; m < citation.content.length; m++) {
                  const content = citation.content[m]
                  const formattedVerse = content.verse.slice(-1) === "a" || content.verse.slice(-1) === "b" ? content.verse.slice(0, -1) : content.verse
                  if (content.chapter === chapterLocation && formattedVerse === verseLocation) {
                    this.$router.push({ name: "synopsis", hash: "#" + section.id })
                  }
                }
              }
            }
          }
        }
      }
    },
    redirectToPreviousLeadingCitation() {
      let previousSectionId;
      for (let i = 0; i < useSynopsisStore().currentSynopsis.chapters.length; i++) {
        //TODO: think about better name than chapter in .json
        const chapter = useSynopsisStore().currentSynopsis.chapters[i]
        for (let j = 0; j < chapter.subchapters.length; j++) {
          const subchapter = chapter.subchapters[j]
          for (let k = 0; k < subchapter.sections.length; k++) {
            const section = subchapter.sections[k]
            //TODO: remove hacky solution.
            const evangelist = this.evangelist === "mt" ? "mt" : (this.evangelist === "mk" ? "mk" : (this.evangelist === "lk" ? "lk" : "jn"))
            // TODO: this.evangelist not type correct for some reason.
            for (let l = 0; l < section[evangelist].length; l++) {
              const citation = section[evangelist][l]
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
      }
    },
    redirectToNextLeadingCitation() {
      for (let i = 0; i < useSynopsisStore().currentSynopsis.chapters.length; i++) {
        //TODO: think about better name than chapter in .json
        const chapter = useSynopsisStore().currentSynopsis.chapters[i]
        for (let j = 0; j < chapter.subchapters.length; j++) {
          const subchapter = chapter.subchapters[j]
          for (let k = 0; k < subchapter.sections.length; k++) {
            const section = subchapter.sections[k]
            //TODO: remove hacky solution.
            const evangelist = this.evangelist === "mt" ? "mt" : (this.evangelist === "mk" ? "mk" : (this.evangelist === "lk" ? "lk" : "jn"))
            // TODO: this.evangelist not type correct for some reason.
            for (let l = 0; l < section[evangelist].length; l++) {
              const citation = section[evangelist][l]
              if (Number(section.id) > Number(this.sectionId) && citation?.leading) {
                this.$router.push({ name: "synopsis", hash: "#" + section.id })
                return
              }
            }
          }
        }
      }
    },
  },
  computed: {
    evangelistName() {
      switch (this.evangelist) {
        case "mt":
          return "Máté"
        case "mk":
          return "Márk"
        case "lk":
          return "Lukács"
        default:
          return "János"
      }
    },

  }
}
</script>

<template>
  <div class="card h-100" v-if="citation?.content"
    :class="{ 'shadow border-dark': citation.leading }">
    <div class="card-header sticky-top bg-light">
      {{ synopsisStore.currentDictionary.evangelists[evangelist] }} {{ citation?.citation }}
      <template v-if="!$route.params.id">
        <button v-if="!citation.leading"
          @click="redirectToLeadingCitation(citation.content[0].chapter, citation.content[0].verse)" type="button"
          class=" float-end btn  btn-sm py-0 m-0" :title="synopsisStore.currentDictionary.tooltips.jumpToMainText">

          <i class="bi bi-compass fs-6 text-secondary"></i>
        </button>

        <button v-if="citation.leading
    && !((evangelist === 'mt' && sectionId === '364')
      || (evangelist === 'mk' && sectionId === '363')
      || (evangelist === 'lk' && sectionId === '365')
      || (evangelist === 'jn' && sectionId === '367')
    )" @click="redirectToNextLeadingCitation()" type="button" class=" float-end btn  btn-sm py-0 m-0"
          :title="synopsisStore.currentDictionary.tooltips.nextMainText">
          <i class="bi bi-arrow-down fs-6 text-secondary"></i>
        </button>
        <button v-if="citation.leading && sectionId !== '1'" @click="redirectToPreviousLeadingCitation()"
          type="button" class=" float-end btn  btn-sm py-0 m-0"
          :title="synopsisStore.currentDictionary.tooltips.previousMainText">
          <i class="bi bi-arrow-up fs-6 text-secondary"></i>
        </button>
      </template>

    </div>
    <div class="card-body">
      <p>
        <template v-for="verse in citation?.content">
          {{ " " }}<sup class="text-secondary">{{ verse.verse }}</sup>{{ verse.text }}
        </template>
      </p>
    </div>
  </div>
</template>