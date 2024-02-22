<script lang="ts">
import Subsection from '@/components/Subsection.vue'
import type { SectionScheme } from '@/interfaces/synopsisInterface';
import type { PropType } from 'vue';

export default {
    props: {
        section: {
            type: Object as PropType<SectionScheme>,
            required: true
        },
    },
    components: {
        Subsection
    }
}
</script>

<template>
    <div class="row">
        <h4 class="event text-center display-5">
            {{ section.section_name }}
        </h4>
    </div>

    <Subsection v-for="subsection in section.subsections" :subsection="subsection" />
</template>