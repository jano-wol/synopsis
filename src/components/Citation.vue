<script lang="ts">
import type { PropType } from 'vue';
import type { CitationScheme } from '@/interfaces/synopsisInterface';
import { useSynopsisStore } from "@/stores/SynopsisStore"

export default {
  props: {
    evangelist: {
      type: String,
      required: true,
    },
    citation: {
      type: Object as PropType<CitationScheme | null>,
      required: true
    },
  },
  methods: {
    locateLeadingCitation(chapterLocation: string, verseLocation: string): void {
      for (let i = 0; i < useSynopsisStore().synopsis.chapters.length; i++) {
        //TODO: think about better name than chapter in .json
        const chapter = useSynopsisStore().synopsis.chapters[i]
        for (let j = 0; j < chapter.sections.length; j++) {
          const section = chapter.sections[j]
          for (let k = 0; k < section.subsections.length; k++) {
            const subsection = section.subsections[k]
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
                    console.log(subsection.id)
                    this.$router.push({ name: "synopsis", hash: "#" + subsection.id })
                  }
                }
              }
            }
          }
        }
      }
    }
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
    }
  }
}
</script>

<template>
  <div class="card h-100" v-if="citation?.content && citation.primary"
    :class="{ 'shadow border-dark': citation.leading, 'border-light text-bg-light': !citation.primary }">
    <div class="card-header sticky-top bg-light">
      {{ evangelistName }} {{ citation?.citation }}
      <button v-if="!citation.leading"
        @click="locateLeadingCitation(citation.content[0].chapter, citation.content[0].verse)" type="button"
        class=" float-end btn  btn-sm py-0 m-0" data-bs-toggle="tooltip" data-bs-placement="top"
        data-bs-title="Ugrás a törzsszöveghez">

        <i class="bi bi-compass fs-6 text-secondary"></i>
      </button>
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