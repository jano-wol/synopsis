<script lang="ts">
import Section from '@/components/Section.vue'
import type { SubchapterScheme } from '@/interfaces/synopsisInterface';
import type { PropType } from 'vue';
import { useSynopsisStore } from "@/stores/SynopsisStore"

export default {
    props: {
        //TODO: proper typing
        subchapterLocation: {
            type: Object,
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
            {{ synopsisStore.get(subchapterLocation).subchapter_name }}
        </h4>
    </div>

    <Section v-for="sectionIndex in synopsisStore.get(subchapterLocation).sections.length"
        :id="synopsisStore.get(subchapterLocation).sections[sectionIndex - 1].id"
        :section-location="{ ...subchapterLocation, sectionIndex: sectionIndex - 1 }" />
</template>