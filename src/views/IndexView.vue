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
      if (index < this.synopsisStore.currentSynopsis.parts.length) {
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

    <IndexRecord :part-title="synopsisStore.currentSynopsis.parts[0].part_title"
      :sections="synopsisStore.currentSynopsis.parts[0].sections" />
    <template v-for="partIndex in synopsisStore.currentSynopsis.parts.length - 1" :key="partIndex">
      <IndexRecord v-if="visibleIndex >= partIndex"
        :part-title="synopsisStore.currentSynopsis.parts[partIndex].part_title"
        :sections="synopsisStore.currentSynopsis.parts[partIndex].sections" />
    </template>

  </div>
</template>
