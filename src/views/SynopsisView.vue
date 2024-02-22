<script lang="ts">
import Chapter from '@/components/Chapter.vue'
import type { ChapterScheme } from '@/interfaces/synopsisInterface';
import { useSynopsisStore } from "@/stores/SynopsisStore"

const chapters: ChapterScheme[] = useSynopsisStore().synopsis.chapters

export default {
  data() {
    return {
      chapters: chapters
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
    <h1 class="text-center display-1">Szinopszis</h1>

    <Chapter v-for="chapter in chapters" :chapter="chapter" />

  </div>
</template>

