<script lang="ts">
import IndexRecord from '@/components/IndexRecord.vue';
import { useSynopsisStore } from "@/stores/SynopsisStore"


export default {
  data() {
    return {
      chapters: useSynopsisStore().synopsis.chapters
    };
  },
  components: { IndexRecord }
}

</script>

<template>
  <div class="container">
    <h1 class="text-center">Tartalomjegyzék</h1>



    <IndexRecord v-for="chapter in chapters" :chapter-name="chapter.chapter_name" :sections="chapter.sections" />

  </div>
</template>
