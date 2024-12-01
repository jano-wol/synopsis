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
    <h2 class="fs-3">Felhasznált források</h2>
    <SourcesUsed />    
    <h2 class="fs-3">Eltérések a forrásoktól</h2>
    <p>A honlap tartalma bizonyos esetekben eltér a forrásoktól. Az eltéréseket a projekt <a href="https://github.com/anwolosz/synopsis/wiki/Differences-from-the-sources">wiki oldalán</a> felsoroltuk.</p>
    <h2 class="fs-3">Letölthető anyagok</h2>
    <AvailableSources />
</template>