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
    subsectionId: {
      type: String,
      required: true
    },
  },
  methods: {
    redirectToLeadingCitation(chapterLocation: string, verseLocation: string): void {
      for (let i = 0; i < useSynopsisStore().synopsis.chapters.length; i++) {
        //TODO: think about better name than chapter in .json
        const chapter = useSynopsisStore().synopsis.chapters[i]
        for (let j = 0; j < chapter.subchapters.length; j++) {
          const subchapter = chapter.subchapters[j]
          for (let k = 0; k < subchapter.subsections.length; k++) {
            const subsection = subchapter.subsections[k]
            //TODO: remove hacky solution.
            const evangelist = this.evangelist === "mt" ? "mt" : (this.evangelist === "mk" ? "mk" : (this.evangelist === "lk" ? "lk" : "jn"))
            // TODO: this.evangelist not type correct for some reason.
            for (let l = 0; l < subsection[evangelist].length; l++) {
              const citation = subsection[evangelist][l]
              if (citation?.leading) {
                for (let m = 0; m < citation.content.length; m++) {
                  const content = citation.content[m]
                  const formattedVerse = content.verse.slice(-1) === "a" || content.verse.slice(-1) === "b" ? content.verse.slice(0, -1) : content.verse
                  if (content.chapter === chapterLocation && formattedVerse === verseLocation) {
                    this.$router.push({ name: "synopsis", hash: "#" + subsection.id })
                  }
                }
              }
            }
          }
        }
      }
    },
    redirectToPreviousLeadingCitation() {
      let previousSubsectionId;
      for (let i = 0; i < useSynopsisStore().synopsis.chapters.length; i++) {
        //TODO: think about better name than chapter in .json
        const chapter = useSynopsisStore().synopsis.chapters[i]
        for (let j = 0; j < chapter.subchapters.length; j++) {
          const subchapter = chapter.subchapters[j]
          for (let k = 0; k < subchapter.subsections.length; k++) {
            const subsection = subchapter.subsections[k]
            //TODO: remove hacky solution.
            const evangelist = this.evangelist === "mt" ? "mt" : (this.evangelist === "mk" ? "mk" : (this.evangelist === "lk" ? "lk" : "jn"))
            // TODO: this.evangelist not type correct for some reason.
            for (let l = 0; l < subsection[evangelist].length; l++) {
              const citation = subsection[evangelist][l]
              if (subsection.id === this.subsectionId) {
                this.$router.push({ name: "synopsis", hash: "#" + previousSubsectionId })
                return
              }
              if (citation?.leading) {
                previousSubsectionId = subsection.id
              }
            }
          }
        }
      }
    },
    redirectToNextLeadingCitation() {
      for (let i = 0; i < useSynopsisStore().synopsis.chapters.length; i++) {
        //TODO: think about better name than chapter in .json
        const chapter = useSynopsisStore().synopsis.chapters[i]
        for (let j = 0; j < chapter.subchapters.length; j++) {
          const subchapter = chapter.subchapters[j]
          for (let k = 0; k < subchapter.subsections.length; k++) {
            const subsection = subchapter.subsections[k]
            //TODO: remove hacky solution.
            const evangelist = this.evangelist === "mt" ? "mt" : (this.evangelist === "mk" ? "mk" : (this.evangelist === "lk" ? "lk" : "jn"))
            // TODO: this.evangelist not type correct for some reason.
            for (let l = 0; l < subsection[evangelist].length; l++) {
              const citation = subsection[evangelist][l]
              if (Number(subsection.id) > Number(this.subsectionId) && citation?.leading) {
                this.$router.push({ name: "synopsis", hash: "#" + subsection.id })
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
      {{ synopsisStore.dictionary.evangelists[evangelist] }} {{ citation?.citation }}
      <template v-if="!$route.params.id">
        <button v-if="!citation.leading"
          @click="redirectToLeadingCitation(citation.content[0].chapter, citation.content[0].verse)" type="button"
          class=" float-end btn  btn-sm py-0 m-0" :title="synopsisStore.dictionary.tooltips.jumpToMainText">

          <i class="bi bi-compass fs-6 text-secondary"></i>
        </button>

        <button v-if="citation.leading
    && !((evangelist === 'mt' && subsectionId === '364')
      || (evangelist === 'mk' && subsectionId === '363')
      || (evangelist === 'lk' && subsectionId === '365')
      || (evangelist === 'jn' && subsectionId === '367')
    )" @click="redirectToNextLeadingCitation()" type="button" class=" float-end btn  btn-sm py-0 m-0"
          :title="synopsisStore.dictionary.tooltips.nextMainText">
          <i class="bi bi-arrow-down fs-6 text-secondary"></i>
        </button>
        <button v-if="citation.leading && subsectionId !== '1'" @click="redirectToPreviousLeadingCitation()"
          type="button" class=" float-end btn  btn-sm py-0 m-0"
          :title="synopsisStore.dictionary.tooltips.previousMainText">
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