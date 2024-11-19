<script lang="ts">
import Section from '@/components/Section.vue'
import type { CitationScheme, SectionScheme } from '@/interfaces/synopsisInterface';
import { useSynopsisStore } from "@/stores/SynopsisStore"

export default {
    data() {
        return {
            synopsisStore: useSynopsisStore(),
        }
    },
    mounted()
    {
        //TODO: think about:
        //.renaming component sections to calendar or dailygospel etc
        //.think aobut keep it sections, and use it in /language/translation/:id too
        if (this.$route.name === 'today' || this.$route.name === 'calendar')
        {
            this.synopsisStore.getDailyGospel(new Date()).then(() => { console.log(this.synopsisStore.dailyGospelSections)});
        }
    },
    components: {
        Section
    }
}

</script>


<template>
    <!-- TODO: prepare if server is not answering, error handling etc -->
    <Section v-for="id in synopsisStore.dailyGospelSections" :id="id" />
</template>