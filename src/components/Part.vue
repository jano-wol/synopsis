<script lang="ts">
import Section from '@/components/Section.vue'
import type { PartScheme } from '@/interfaces/synopsisInterface'
import type { PropType } from 'vue';

export default {
  props: {
    part: {
      type: Object as PropType<PartScheme>,
      required: true
    }
  },
  components: {
    Section
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
    <Section v-for="section in part.sections" :id="section.id" :key="section.id"/>
  </div>
</template>
