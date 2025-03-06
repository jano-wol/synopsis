<script lang="ts">
import Section from '@/components/Section.vue'
import type { QuoteScheme } from '@/interfaces/dailyGospelInterface';
import type { CitationScheme, SectionScheme } from '@/interfaces/synopsisInterface';
import { useSynopsisStore } from "@/stores/SynopsisStore"
import ErrorMessage from '@/components/ErrorMessage.vue'
import Loader from '@/components/Loader.vue'
import router from '../router';

export default {
    data() {
        return {
            synopsisStore: useSynopsisStore(),
            selectedDate: "",
        }
    },
    mounted()
    {
        this.selectedDate = this.$route.params.date as string;
        this.synopsisStore.getGospel(this.$route.params.date as string)
    },
    beforeRouteUpdate(to)
    {
        this.synopsisStore.getGospel(to.params.date as string)
        this.selectedDate = to.params.date as string
    },
    components: {
        Section, Loader, ErrorMessage
    },
    methods: {
        handleDateChange() {
            router.push({ name: "calendar", params: {date: this.selectedDate}});
        }
    }
}

</script>


<template>
    <!-- v-if won't work properly if it will be possible to change date on the 'calendar' route  -->
    <Loader v-if="synopsisStore.dateGospel === null && synopsisStore.error === null"/>
    <ErrorMessage />
    <template v-if="synopsisStore.dateGospel !== null">
        <h1 class="text-center"><i class="bi bi-sun"></i></h1>
        <div class="d-flex justify-content-center">
            <input type="date" class="form-control w-auto"
            min="1901-01-01"
            max="2100-12-31"
            @change="handleDateChange()"
            v-model="selectedDate">
        </div>
    </template>

    <Section v-for="id in synopsisStore.dateGospelSections" :id="id" :key="id" />
</template>