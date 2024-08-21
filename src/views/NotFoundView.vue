<script lang="ts">
import { useSynopsisStore } from "@/stores/SynopsisStore"

export default {
    data() {
        return {
            synopsisStore: useSynopsisStore()
        };
    }
}

</script>

<template>
    <div class="container">
        <h1 class="text-center">4<img src="/favicon.svg" alt="Szinopszis" width="22" height="22">4 {{
            synopsisStore.dictionary.notFound.notFound }}</h1>
    </div>
</template>