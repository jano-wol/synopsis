<script lang="ts">
import Part from '@/components/Part.vue'
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
    Part
  },
  mounted() {
    if (this.isValidHash(this.hash)) {
      this.showScroller = true
    }
    this.delayedRender(0);
  },
  methods: {
    delayedRender(index: number) {
      if (!this.scrolledToAnchor) {
        this.scrollToAnchor();
      }
      if (index < this.synopsisStore.currentSynopsis.parts.length) {
        setTimeout(() => {
          this.visibleIndex = index + 1;
          this.delayedRender(index + 1);
        }, 1);
      }
    },
    scrollToAnchor() {
        if (this.hash) {
          const anchorElement = document.getElementById(this.hash);
          if (anchorElement) {
            this.showScroller = false
            this.scrolledToAnchor = true
            anchorElement.scrollIntoView();
          }
        }
    },
    isValidHash(hash: string) {
      return parseInt(hash) > 0 && parseInt(hash) < 368 && parseInt(hash) !== 361 && parseInt(hash) !== 362
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
    <h1 class="text-center display-1">{{ synopsisStore.currentDictionary.menu.synopsis }}</h1>
    <p class="text-center">{{ synopsisStore.currentDictionary.synopsis.subheading }}</p>
    <div v-if="showScroller" class="spinner-background">
      <!-- Spinner -->
      <div class="spinner-border spinner-border-lg" role="status">
        <span class="visually-hidden">Loading...</span>
      </div>
    </div>

    <template v-for="partIndex in synopsisStore.currentSynopsis.parts.length">
      <Part v-if="visibleIndex >= partIndex - 1" :key="partIndex"
        :part="synopsisStore.currentSynopsis.parts[partIndex - 1]" />
    </template>

  </div>
</template>
