<script lang="ts">
import SourcesUsed from "@/components/SourcesUsed.vue"
import AvailableSources from "@/components/AvailableSources.vue"

export default {
    components: {
        SourcesUsed,
        AvailableSources
    }
}

</script>

<template>
    <h2 class="fs-3">Sources Used</h2>
    <SourcesUsed />    
    <h2 class="fs-3">Differences from the Sources</h2>
    <p>The implementation differs from the sources, with significant differences in some cases. These differences are documented on the project's <a href="https://github.com/anwolosz/synopsis/wiki/Differences-from-the-sources">wiki page</a>.</p>
    <h2 class="fs-3">Downloadable Materials</h2>
    <AvailableSources />
</template>