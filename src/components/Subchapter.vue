<script lang="ts">
import Subsection from '@/components/Subsection.vue'
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
        Subsection
    }
}
</script>

<template>
    <div class="row">
        <h4 class="event text-center display-5">
            {{ synopsisStore.get(subchapterLocation).subchapter_name }}
        </h4>
    </div>

    <Subsection v-for="subsectionIndex in synopsisStore.get(subchapterLocation).subsections.length"
        :id="synopsisStore.get(subchapterLocation).subsections[subsectionIndex - 1].id"
        :subsection-location="{ ...subchapterLocation, subsectionIndex: subsectionIndex - 1 }" />
</template>