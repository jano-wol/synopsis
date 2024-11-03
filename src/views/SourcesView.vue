<script lang="ts">
import { useSynopsisStore } from "@/stores/SynopsisStore"
import SourcesHu from '@/components/hu/SourcesHu.vue'
import SourcesEn from "@/components/en/SourcesEn.vue";


export default {
    data() {
        return {
            synopsisStore: useSynopsisStore()
        };
    },
    components: {
        SourcesHu,
        SourcesEn
    }
}

</script>

<template>
    <div class="container">
        <h1 class="text-center">{{ synopsisStore.currentDictionary.menu.sources }}</h1>
        <SourcesHu v-if="synopsisStore.currentLanguage === 'hu'" />
        <SourcesEn v-if="synopsisStore.currentLanguage !== 'hu'" />
    </div>
</template>