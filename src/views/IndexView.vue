<script lang="ts">
import synopsis from '@/assets/synopsis.json'
import IndexRecord from '@/components/IndexRecord.vue';

export default {
  data() {
    return {
      chapters: synopsis.chapters
    };
  },
  components: { IndexRecord }
}

</script>

<template>
  <div class="container">
    <h1 class="text-center display-1">Tartalomjegyzék</h1>



    <IndexRecord v-for="chapter in chapters" :chapter-name="chapter.chapter_name" :sections="chapter.sections" />

  </div>
</template>
