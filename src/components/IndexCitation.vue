<script lang="ts">
import { useSynopsisStore } from "@/stores/SynopsisStore"

export default {
    data() {
    return {
      synopsisStore: useSynopsisStore(),
    }
  },
    props: {
        citations: { type: Array<any>, required: true }
    }
}
</script>

<template>
    <p v-for="citation in citations" :class="{
        'fw-bold': citation?.leading,
        'text-secondary fw-light': !citation
    }" class="text-center m-1">
        {{ !citation ? "-" : synopsisStore.getCitation(citation.content[0].chapter, citation.content[0].verse, citation.content[citation.content.length - 1].chapter, citation.content[citation.content.length - 1].verse) }}
    </p>
</template>
