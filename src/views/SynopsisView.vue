<script lang="ts">
import Chapter from '@/components/Chapter.vue'
import type { ChapterScheme } from '@/interfaces/synopsisInterface';
import { useSynopsisStore } from "@/stores/SynopsisStore"


export default {
  data() {
    return {
      synopsisStore: useSynopsisStore(),
      visibleIndex: 0,
      scrolledToAnchor: false,
      showScroller: false
    }
  },
  components:
  {
    Chapter
  },
  mounted() {
    if (this.$route.hash.substring(1)) {
      this.showScroller = true
    }
    this.delayedRender(0);
  },
  methods: {
    delayedRender(index: number) {
      if (index < this.synopsisStore.synopsis.chapters.length) {
        setTimeout(() => {
          this.visibleIndex = index + 1;
          this.delayedRender(index + 1);
          if (!this.scrolledToAnchor) {
            this.scrollToAnchor();
          }
          if (index + 1 === this.synopsisStore.synopsis.chapters.length) {
            this.showScroller = false;
          }
        }, 1);
      }
    },
    scrollToAnchor() {
      this.$nextTick(() => {
        const hash = this.$route.hash.substring(1);
        if (hash) {
          const anchorElement = document.getElementById(hash);
          if (anchorElement) {
            this.scrolledToAnchor = true
            anchorElement.scrollIntoView();
          }
        }
      });
    }
  }
}

</script>

<template>
  <div class="container-fluid">
    <div class="container text-center">
      <div class="row justify-content-md-center">
        <div class="col col-lg-2">
        </div>
        <div class="col-md-auto">
          <h1 class="text-center display-1">{{ synopsisStore.translation.menu.synopsis }}</h1>
        </div>
        <div class="col col-lg-2 d-flex align-items-center justify-content-start">
          <div v-if="showScroller" class="spinner-border spinner-border-sm text-secondary" role="status">
            <span class="visually-hidden">Loading...</span>
          </div>
        </div>
      </div>
    </div>

    <template v-for="chapterIndex in synopsisStore.synopsis.chapters.length">
      <Chapter v-if="visibleIndex >= chapterIndex - 1"
        :chapter-location="{ chapterIndex: chapterIndex - 1, sectionIndex: null, subsectionIndex: null }" />
    </template>

  </div>
</template>
