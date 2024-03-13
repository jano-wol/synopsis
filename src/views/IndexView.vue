<script lang="ts">
import IndexRecord from '@/components/IndexRecord.vue';
import { useSynopsisStore } from "@/stores/SynopsisStore"


export default {
  data() {
    return {
      synopsisStore: useSynopsisStore()
    };
  },
  components: { IndexRecord }
}

</script>

<template>
  <div class="container">
    <h1 class="text-center">{{synopsisStore.translation.menu.index}}</h1>



    <IndexRecord v-for="chapter in synopsisStore.synopsis.chapters" :chapter-name="chapter.chapter_name" :sections="chapter.sections" />

  </div>
</template>
