<script lang="ts">
import Section from '@/components/Section.vue'
import type { QuoteScheme } from '@/interfaces/dailyGospelInterface';
import type { CitationScheme, SectionScheme } from '@/interfaces/synopsisInterface';
import { useSynopsisStore } from "@/stores/SynopsisStore"
import ErrorMessage from '@/components/ErrorMessage.vue'
import Loader from '@/components/Loader.vue';

export default {
    data() {
        return {
            synopsisStore: useSynopsisStore(),
            gospelSections: [] as Array<string>,
        }
    },
    mounted()
    {
        this.gospelSections = this.synopsisStore.dailyGospelSections
        this.synopsisStore.getGospel(new Date().toISOString().split('T')[0]).then(() => { console.log(this.synopsisStore.dailyGospelSections)});
    },
    components: {
        Section, Loader, ErrorMessage
    }
}

</script>


<template>
    <Loader v-if="synopsisStore.dailyGospel === null && synopsisStore.error === null"/>
    <ErrorMessage />
    <h1 v-if="!synopsisStore.isLoading && synopsisStore.error === null" class="text-center"><i class="bi bi-sun"></i></h1>
    <Section v-for="id in gospelSections" :id="id" :key="id" />
</template>