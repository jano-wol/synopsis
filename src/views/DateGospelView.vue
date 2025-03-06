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
        }
    },
    mounted()
    {
        this.synopsisStore.getGospel(this.$route.params.date as string)
    },
    components: {
        Section, Loader, ErrorMessage
    }
}

</script>


<template>
    <!-- v-if won't work properly if it will be possible to change date on the 'calendar' route  -->
    <Loader v-if="synopsisStore.dateGospel === null && synopsisStore.error === null"/>
    <ErrorMessage />
    <Section v-for="id in synopsisStore.dateGospelSections" :id="id" :key="id" />
</template>