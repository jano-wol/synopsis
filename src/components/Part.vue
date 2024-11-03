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
      <h3 class="event text-center display-5 mt-5">
        {{ part?.part_title }}
      </h3>
    </div>
    <Section v-for="section in part.sections" :id="section.id" :key="section.id"/>
  </div>
</template>
