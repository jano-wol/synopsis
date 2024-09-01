<script lang="ts">
import Section from '@/components/Section.vue'
import { useSynopsisStore } from "@/stores/SynopsisStore"
import type { SubcpartScheme } from '@/interfaces/synopsisInterface'
import type { PropType } from 'vue';

export default {
    props: {
        subpart: {
            type: Object as PropType<SubcpartScheme>,
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
            {{ subpart.subpart_title }}
        </h4>
    </div>

    <Section v-for="section in subpart.sections" :id="section.id" :key="section.id"/>


</template>