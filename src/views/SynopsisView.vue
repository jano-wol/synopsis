<script lang="ts">
import Part from '@/components/Part.vue'
import Loader from '@/components/Loader.vue'
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
    Part, Loader
  },
  mounted() {
    if (this.isValidHash(this.hash)) {
      this.synopsisStore.isLoading = true
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
        }, 0);
      }
    },
    scrollToAnchor() {
        if (this.hash) {
          const anchorElement = document.getElementById(this.hash);
          if (anchorElement) {
            this.showScroller = false
            this.scrolledToAnchor = true
            anchorElement.scrollIntoView();
            this.synopsisStore.isLoading = false
          }
        }
    },
    isValidHash(hash: string) {
      return parseInt(hash) > 0 && parseInt(hash) < 368 && parseInt(hash) !== 361 && parseInt(hash) !== 362
    }
  }
}

</script>

<template>
  <Loader />
  <div class="container-fluid">
    <h1 class="text-center display-1 pt-4">{{ synopsisStore.currentSynopsis.heading }}</h1>
    <p class="text-center pb-4">{{ synopsisStore.currentSynopsis.subheading }}</p>


    <template v-for="partIndex in synopsisStore.currentSynopsis.parts.length">
      <Part v-if="visibleIndex >= partIndex - 1" :key="partIndex"
        :part="synopsisStore.currentSynopsis.parts[partIndex - 1]" />
    </template>

  </div>
</template>
