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
    this.synopsisStore.getGospel(new Date().toISOString().split('T')[0]).then(() => { console.log(this.synopsisStore.dailyGospelSections)});

    if (this.isValidHash(this.hash)) {
      this.synopsisStore.isLoading = true
      this.showScroller = true
    }
    this.synopsisStore.delayedRender(0, this.scrollToAnchor);
  },
  methods: {
    scrollToAnchor() {
      this.visibleIndex++;
      if (this.hash && !this.scrolledToAnchor) {
        const anchorElement = document.getElementById(this.hash);
        if (anchorElement) {
          setTimeout(()=>
          {
            this.showScroller = false
            this.scrolledToAnchor = true
            anchorElement.scrollIntoView();
            this.synopsisStore.isLoading = false
          }, 0)
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
  
  <h1 class="text-center display-1">{{ synopsisStore.currentSynopsis.heading }}</h1>
  <h2 class="text-center fs-6">{{ synopsisStore.currentSynopsis.subheading }}</h2>
  
  
    <template v-for="partIndex in synopsisStore.currentSynopsis.parts.length">
      <Part v-if="visibleIndex >= partIndex - 1" :key="partIndex"
        :part="synopsisStore.currentSynopsis.parts[partIndex - 1]" />
    </template>

</template>
