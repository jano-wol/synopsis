<script lang="ts">
import Chapter from '@/components/Chapter.vue'
import type { ChapterScheme } from '@/interfaces/synopsisInterface';
import { useSynopsisStore } from "@/stores/SynopsisStore"


export default {
  data() {
    return {
      synopsisStore: useSynopsisStore()
    }
  },
  components:
  {
    Chapter
  }
}

</script>

<template>
  <div class="container-fluid">
    <h1 class="text-center display-1">{{ synopsisStore.translation.menu.synopsis }}</h1>

    <Chapter v-for="chapterIndex in synopsisStore.synopsis.chapters.length"
      :chapter-location="{ chapterIndex: chapterIndex - 1, sectionIndex: null, subsectionIndex: null }" />

  </div>
</template>
