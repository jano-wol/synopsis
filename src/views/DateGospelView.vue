<script lang="ts">
import Section from '@/components/Section.vue'
import type { QuoteScheme } from '@/interfaces/dailyGospelInterface';
import type { SectionScheme } from '@/interfaces/synopsisInterface';
import { useSynopsisStore } from "@/stores/SynopsisStore"
import ErrorMessage from '@/components/ErrorMessage.vue'
import Loader from '@/components/Loader.vue'
import router from '../router';
import { dateToString, stringToDate } from '@/utils/date';

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
        navigateDate() {
            router.push({ name: "calendar", params: {date: this.selectedDate}});
        },
        shiftDate(n: number)
        {
            const date = stringToDate(this.selectedDate)
            date.setDate(date.getDate() + n);
            this.selectedDate = dateToString(date)
            this.navigateDate()
        },
        navigateTomorrow()
        {
            this.shiftDate(1)
        },
        navigateYesterday()
        {
            this.shiftDate(-1)
        }
    }
}

</script>


<template>
    <Loader v-if="synopsisStore.dateGospel === null && synopsisStore.error === null"/>
    <ErrorMessage />
    <template v-if="synopsisStore.dateGospel !== null">
        <h1 class="text-center"><i class="bi bi-sun"></i></h1>
        <div class="d-flex justify-content-center">
            <button class="btn" @click="navigateYesterday()"><i class="bi bi-chevron-left"></i></button>
            <input type="date" class="form-control w-auto"
            min="1901-01-01"
            max="2100-12-31"
            @input="navigateDate()"
            v-model="selectedDate">
            <button class="btn" @click="navigateTomorrow()"><i class="bi bi-chevron-right"></i></button>
        </div>
    </template>

    <Section v-for="id in synopsisStore.dateGospelSections" :id="id" :key="id" />
</template>