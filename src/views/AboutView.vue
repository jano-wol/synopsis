<script lang="ts">
import { useSynopsisStore } from "@/stores/SynopsisStore"
import AboutHu from '@/components/hu/AboutHu.vue'
import AboutEn from "@/components/en/AboutEn.vue";


export default {
    data() {
        return {
            synopsisStore: useSynopsisStore()
        };
    },
    components: {
        AboutHu,
        AboutEn
    }
}

</script>

<template>
    <div class="container">
        <h1 class="text-center">{{ synopsisStore.dictionary.menu.about }}</h1>
        <AboutHu v-if="synopsisStore.language === 'hu'" />
        <AboutEn v-if="synopsisStore.language !== 'hu'" />
    </div>
</template>