<script lang="ts">
import IndexRecord from '@/components/IndexRecord.vue';
import { useSynopsisStore } from "@/stores/SynopsisStore"


export default {
  data() {
    return {
      synopsisStore: useSynopsisStore(),
      visibleIndex: 0
    };
  },
  components: { IndexRecord },
  mounted() {
    this.delayedRender(0);
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


    <template  v-for="(chapter, chapterIndex) in synopsisStore.synopsis.chapters">
      <IndexRecord v-if="visibleIndex >= chapterIndex"
        :chapter-name="chapter.chapter_name" :sections="chapter.sections" />
    </template>

  </div>
</template>
