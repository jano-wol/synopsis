<script lang="ts">
import Section from '@/components/Section.vue'
import type { ChapterScheme } from '@/interfaces/synopsisInterface'
import type { PropType } from 'vue';
import { useSynopsisStore } from "@/stores/SynopsisStore"


export default {
  props: {
    chapterLocation: {
      //TODO: Proper typing
      type: Object,
      required: true
    }
  },
  data() {
    return {
      synopsisStore: useSynopsisStore()
    }
  },
  components: {
    Section
  }
}
</script>

<template>
  <div class="row">
    <h2 class="event text-center display-4 mt-5">
      <!-- {{ chapterIndex  }} -->
      {{ synopsisStore.get(chapterLocation)?.chapter_name }}
    </h2>
  </div>
  <Section v-for="sectionIndex in synopsisStore.get(chapterLocation)?.sections.length"
    :section-location="{ ...chapterLocation, sectionIndex: sectionIndex - 1 }" />
</template>
