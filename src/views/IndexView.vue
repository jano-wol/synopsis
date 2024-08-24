<script lang="ts">
import IndexRecord from '@/components/IndexRecord.vue';
import { useSynopsisStore } from "@/stores/SynopsisStore"


export default {
  data() {
    return {
      synopsisStore: useSynopsisStore(),
      visibleIndex: 1
    };
  },
  components: { IndexRecord },
  mounted() {
    this.delayedRender(1);
  },
  methods: {
    delayedRender(index: number) {
      if (index < this.synopsisStore.currentSynopsis.chapters.length) {
        setTimeout(() => {
          this.visibleIndex = index + 1;
          this.delayedRender(index + 1);
        }, 1);
      }
    }
  }
}

</script>

<template>
  <div class="container">
    <h1 class="text-center">{{ synopsisStore.currentDictionary.menu.index }}</h1>

    <IndexRecord :chapter-name="synopsisStore.currentSynopsis.chapters[0].chapter_name"
      :subchapters="synopsisStore.currentSynopsis.chapters[0].subchapters" />
    <template v-for="chapterIndex in synopsisStore.currentSynopsis.chapters.length - 1">
      <IndexRecord v-if="visibleIndex >= chapterIndex"
        :chapter-name="synopsisStore.currentSynopsis.chapters[chapterIndex].chapter_name"
        :subchapters="synopsisStore.currentSynopsis.chapters[chapterIndex].subchapters" />
    </template>

  </div>
</template>
