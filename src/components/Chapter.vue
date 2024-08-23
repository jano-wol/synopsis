<script lang="ts">
import Subchapter from '@/components/Subchapter.vue'
import type { ChapterScheme } from '@/interfaces/synopsisInterface'
import type { PropType } from 'vue';
import { useSynopsisStore } from "@/stores/SynopsisStore"


export default {
  props: {
    chapterLocation: {
      //TODO: Proper typing
      type: Object,
      required: true
    }
  },
  data() {
    return {
      synopsisStore: useSynopsisStore()
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
      <!-- {{ chapterIndex  }} -->
      {{ synopsisStore.get(chapterLocation)?.chapter_name }}
    </h2>
  </div>
  <Subchapter v-for="subchapterIndex in synopsisStore.get(chapterLocation)?.subchapters.length"
    :subchapter-location="{ ...chapterLocation, subchapterIndex: subchapterIndex - 1 }" />
</template>
