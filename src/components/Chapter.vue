<script lang="ts">
import Subchapter from '@/components/Subchapter.vue'
import type { ChapterScheme } from '@/interfaces/synopsisInterface'
import type { PropType } from 'vue';

export default {
  props: {
    chapter: {
      type: Object as PropType<ChapterScheme>,
      required: false
    }
  },
  components: {
    Subchapter
  }
}
</script>

<template>
  <div class="row">
    <h2 class="event text-center display-4 mt-5">
      {{ chapter?.chapter_name }}
    </h2>
  </div>
  <Subchapter v-for="subchapter in chapter?.subchapters" :subchapter="subchapter" />
</template>
