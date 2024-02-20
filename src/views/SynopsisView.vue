<script lang="ts">
import Chapter from '@/components/Chapter.vue'
import { useSynopsisStore } from "@/stores/SynopsisStore"

export default {
  data() {
    return {
      chapters: useSynopsisStore().synopsis.chapters
    }
  },
  components:
  {
    Chapter
  }
}

</script>

<template>
  <!-- {{ chapters }} -->
  <div class="container-fluid">
    <h1 class="text-center display-1">Szinopszis</h1>

    <Chapter v-for="chapter in chapters" :chapter-name="chapter.chapter_name" :sections="chapter.sections" />

  </div>
</template>

