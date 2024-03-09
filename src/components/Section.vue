<script lang="ts">
import Subsection from '@/components/Subsection.vue'
import type { SectionScheme } from '@/interfaces/synopsisInterface';
import type { PropType } from 'vue';
import { useSynopsisStore } from "@/stores/SynopsisStore"

export default {
    props: {
        //TODO: proper typing
        sectionLocation: {
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
        Subsection
    }
}
</script>

<template>
    <div class="row">
        <h4 class="event text-center display-5">
            {{ synopsisStore.get(sectionLocation).section_name }}
        </h4>
    </div>

    <Subsection v-for="subsectionIndex in synopsisStore.get(sectionLocation).subsections.length"
        :id="synopsisStore.get(sectionLocation).subsections[subsectionIndex - 1].id"
        :subsection-location="{ ...sectionLocation, subsectionIndex: subsectionIndex - 1 }" />
</template>