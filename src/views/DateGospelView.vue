<script lang="ts">
import Section from '@/components/Section.vue'
import type { QuoteScheme } from '@/interfaces/dailyGospelInterface';
import type { CitationScheme, SectionScheme } from '@/interfaces/synopsisInterface';
import { useSynopsisStore } from "@/stores/SynopsisStore"
import ErrorMessage from '@/components/ErrorMessage.vue'
import Loader from '@/components/Loader.vue'

//TODO: very similar to dailygosepl component. its needed to be separated a separataed because of realoading.
// when visiting on 'calendar' first then 'today', it should be rerendered. acceptable, but think about a better option
// also in the future it could have unique functions (eg calendar for date selection, next day, last day etc)
export default {
    data() {
        return {
            synopsisStore: useSynopsisStore(),
            gospelSections: [] as Array<string>,
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
    // v-if won't work properly if it will be possible to change date on the 'calendar' route 
    <Loader v-if="synopsisStore.dateGospel === null"/>
    <ErrorMessage />
    <Section v-for="id in gospelSections" :id="id" />
</template>