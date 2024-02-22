<script lang="ts">
import Section from '@/components/Section.vue'
import type { ChapterScheme } from '@/interfaces/synopsisInterface'
import type { PropType } from 'vue';


export default {
  props: {
    chapter: {
      type: Object as PropType<ChapterScheme>,
      required: true
    }
  },
  components: {
    Section
  }
}
</script>

<template>
  <div class="row">
    <h2 class="event text-center display-4 mt-5">
      {{ chapter.chapter_name }}
    </h2>
  </div>
  <Section v-for="section in chapter.sections" :section="section" />
</template>
