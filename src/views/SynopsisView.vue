<script lang="ts">
  import { RouterLink, RouterView } from 'vue-router'
  import Chapter from '../components/Chapter.vue'
  import synopsis from '@/assets/synopsis.json'
export default {
  data() {
    return {
      chapters: synopsis.chapters
    }
  },
  components:
  {
    Chapter
  }
}

</script>

<template>
  <div class="container-fluid">
    <h1 class="text-center display-1">Szinopszis</h1>

    <Chapter v-for="chapter in chapters" :chapter-name="chapter.chapter_name" :sections="chapter.sections"/>

  </div>

  <RouterView />
</template>

