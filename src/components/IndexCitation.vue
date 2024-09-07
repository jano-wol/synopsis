<script lang="ts">
import { useSynopsisStore } from "@/stores/SynopsisStore"
import type { CitationScheme } from '@/interfaces/synopsisInterface';

export default {
    data() {
        return {
            synopsisStore: useSynopsisStore(),
        }
    },
    props: {
        citations: {
            required: true,
            type: Array as () => (CitationScheme | null)[]
        }
    }
}
</script>

<template>
    <p v-for="(citation, index) in citations" :class="{
        'fw-bold': citation?.leading,
        'text-secondary fw-light': !citation
    }" class="text-center m-1" :key="index">
        {{ !citation ? "-" : synopsisStore.getCitation(citation.content[0].chapter, citation.content[0].verse,
        citation.content[citation.content.length - 1].chapter, citation.content[citation.content.length - 1].verse) }}
    </p>
</template>
