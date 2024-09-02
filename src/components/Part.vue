<script lang="ts">
import Subpart from '@/components/Subpart.vue'
import type { PartScheme } from '@/interfaces/synopsisInterface'
import type { PropType } from 'vue';

export default {
  props: {
    part: {
      type: Object as PropType<PartScheme>,
      required: false
    }
  },
  components: {
    Subpart
  }
}
</script>

<template>
  <div>
    <div class="row">
      <h2 class="event text-center display-4 mt-5">
        {{ part?.part_title }}
      </h2>
    </div>
    <Subpart v-for="subpart in part?.subparts" :subpart="subpart" />
  </div>
</template>
