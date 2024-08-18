<script lang="ts">
import Chapter from '@/components/Chapter.vue'
import type { ChapterScheme } from '@/interfaces/synopsisInterface';
import { useSynopsisStore } from "@/stores/SynopsisStore"


export default {
  data() {
    return {
      synopsisStore: useSynopsisStore(),
      visibleIndex: 0,
    }
  },
  components:
  {
    Chapter
  },
  mounted() {
    this.delayedRender(0);
  },
  methods: {
    delayedRender(index: number) {
      if (index < this.synopsisStore.synopsis.chapters.length) {
        setTimeout(() => {
          this.visibleIndex = index + 1;
          this.delayedRender(index + 1);
        }, 1000);
      }
    }
  }
}

</script>

<template>
  <div class="container-fluid">
    <h1 class="text-center display-1">{{ synopsisStore.translation.menu.synopsis }}</h1>

    <template v-for="chapterIndex in synopsisStore.synopsis.chapters.length">
      <Chapter v-if="visibleIndex >= chapterIndex - 1"
        :chapter-location="{ chapterIndex: chapterIndex - 1, sectionIndex: null, subsectionIndex: null }" />
    </template>

  </div>
</template>
