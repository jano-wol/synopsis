<script lang="ts">
import Section from '@/components/Section.vue'
import type { QuoteScheme } from '@/interfaces/dailyGospelInterface';
import type { CitationScheme, SectionScheme } from '@/interfaces/synopsisInterface';
import { useSynopsisStore } from "@/stores/SynopsisStore"
import ErrorMessage from '@/components/ErrorMessage.vue'
import Loader from '@/components/Loader.vue'

export default {
    data() {
        return {
            synopsisStore: useSynopsisStore(),
            gospelSections: null as null | QuoteScheme,
        }
    },
    mounted()
    {
        this.gospelSections = this.synopsisStore.dateGospelSections
        this.synopsisStore.getGospel(this.$route.params.date as string, false).then(() => { console.log(this.synopsisStore.dailyGospelSections)});
    },
    components: {
        Section, Loader, ErrorMessage
    }
}

</script>


<template>
    <Loader />
    <ErrorMessage />
    <!-- TODO: prepare if server is not answering, error handling etc -->
     <!-- TODO: Section out of context doesnt have function buttons, here they does have  -->
    <Section v-for="id in gospelSections" :id="id" />
</template>