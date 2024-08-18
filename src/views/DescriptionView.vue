<script lang="ts">
import { useSynopsisStore } from "@/stores/SynopsisStore"
import DescriptionHu from '@/components/hu/DescriptionHu.vue'
import DescriptionEn from "@/components/en/DescriptionEn.vue";


export default {
    data() {
        return {
            synopsisStore: useSynopsisStore()
        };
    },
    components: {
        DescriptionHu,
        DescriptionEn
    }
}

</script>

<template>
    <div class="container">
        <h1 class="text-center">{{ synopsisStore.translation.menu.description }}</h1>
        <DescriptionHu v-if="synopsisStore.language === 'hu'" />
        <DescriptionEn v-if="synopsisStore.language !== 'hu'" />
    </div>
</template>