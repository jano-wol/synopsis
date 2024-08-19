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
      if (index < this.synopsisStore.synopsis.chapters.length) {
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
    <h1 class="text-center">{{ synopsisStore.translation.menu.index }}</h1>

    <IndexRecord
        :chapter-name="synopsisStore.synopsis.chapters[0].chapter_name"
        :sections="synopsisStore.synopsis.chapters[0].sections" />
    <template v-for="chapterIndex in synopsisStore.synopsis.chapters.length">
      <IndexRecord v-if="visibleIndex >= chapterIndex"
        :chapter-name="synopsisStore.synopsis.chapters[chapterIndex].chapter_name"
        :sections="synopsisStore.synopsis.chapters[chapterIndex].sections" />
    </template>

  </div>
</template>
