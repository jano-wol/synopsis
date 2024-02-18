<script lang="ts">
import type { PropType } from 'vue';

interface CitationScheme {
  citation: string;
  primary: boolean;
  leading: boolean;
  content: { text: string, chapter: string, verse: string }[];
}


export default {
  props: {
    name: String,
    citation: { type: Object }
  }
}
</script>

<template>
  <div class="card h-100" v-if="citation?.content && citation.primary"
    :class="{ 'shadow border-dark': citation.leading, 'border-light text-bg-light': !citation.primary }">
    <div class="card-header sticky-top bg-light">
      {{ name }} {{ citation?.citation }}
    </div>
    <div class="card-body">
      <p>
        <template v-for="verse in citation?.content">
          {{ " " }}<sup class="text-secondary">{{ verse.verse }}</sup>{{ verse.text }}
        </template>
      </p>
    </div>
    <!-- <div class="card-footer">
                                                            </div> -->

  </div>
</template>