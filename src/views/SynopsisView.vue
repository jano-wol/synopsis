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
      showScroller: false,
      hash: this.$route.hash.substring(1)
    }
  },
  components:
  {
    Chapter
  },
  mounted() {
    if (this.hash && this.isValidHash(this.hash)) {
      this.showScroller = true
    }
    this.delayedRender(0);
  },
  methods: {
    delayedRender(index: number) {
      if (!this.scrolledToAnchor) {
        this.scrollToAnchor();
      }
      if (index < this.synopsisStore.synopsis.chapters.length) {
        setTimeout(() => {
          this.visibleIndex = index + 1;
          this.delayedRender(index + 1);
        }, 1);
      }
    },
    scrollToAnchor() {
      this.$nextTick(() => {
        if (this.hash) {
          const anchorElement = document.getElementById(this.hash);
          if (anchorElement) {
            this.showScroller = false
            this.scrolledToAnchor = true
            anchorElement.scrollIntoView();
          }
        }
      });
    },
    isValidHash(hash: string)
    {
      let validHashes = []
      for (let i = 1; i<368; i++)
      {
        validHashes.push(i);
      }
      validHashes.splice(360, 2);
      console.log(validHashes)
      return validHashes.includes(parseInt(hash))
    }
  }
}

</script>

<style>
.spinner-background {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: white;
  z-index: 9999;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: rgba(255, 255, 255, 0.5)
}
</style>

<template>
  <div class="container-fluid">
    <h1 class="text-center display-1">{{ synopsisStore.translation.menu.synopsis }}</h1>
    <p class="text-center">Máté, Márk, Lukács és János evangéliumának párhuzamos szövege.</p>
    <div v-if="showScroller" class="spinner-background">
      <!-- Spinner -->
      <div class="spinner-border spinner-border-lg" role="status">
        <span class="visually-hidden">Loading...</span>
      </div>
    </div>

    <template v-show="!showScroller" v-for="chapterIndex in synopsisStore.synopsis.chapters.length">
      <Chapter v-if="visibleIndex >= chapterIndex - 1"
        :chapter-location="{ chapterIndex: chapterIndex - 1, sectionIndex: null, subsectionIndex: null }" />
    </template>

  </div>
</template>
