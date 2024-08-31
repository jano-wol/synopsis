<script lang="ts">
import Section from '@/components/Section.vue'
import { useSynopsisStore } from "@/stores/SynopsisStore"
import type { SubchapterScheme } from '@/interfaces/synopsisInterface'
import type { PropType } from 'vue';

export default {
    props: {
        subchapter: {
            type: Object as PropType<SubchapterScheme>,
            required: true
        }
    },
    data() {
        return {
            synopsisStore: useSynopsisStore()
        }
    },
    components: {
        Section
    }
}
</script>

<template>
    <div class="row">
        <h4 class="event text-center display-5">
            {{ subchapter.subchapter_name }}
        </h4>
    </div>

    <Section v-for="section in subchapter.sections" :id="section.id" :key="section.id"/>


</template>