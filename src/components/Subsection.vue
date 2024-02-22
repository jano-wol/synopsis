<script lang="ts">
import Citation from '@/components/Citation.vue'
import type { SubsectionScheme } from '@/interfaces/synopsisInterface';
import type { PropType } from 'vue';

export default {
    props: {
        subsection: {
            type: Object as PropType<SubsectionScheme>,
            required: true
        }

    },
    components: {
        Citation
    }
}
</script>

<template>
    <div class="row" :id="subsection.number">

        <h3 class=" event text-center display-6 mt-5">
            {{ subsection.number }}. {{ subsection.subsection_name }}
        </h3>
    </div>

    <template v-for="index in subsection.Mt.length">
        <div class="row content mx-3">
            <div class="col-3 pb-3">
                <Citation :citation="subsection.Mt[index - 1]" name="Máté" />
            </div>
            <div class="col-3 pb-3">
                <Citation :citation="subsection.Mk[index - 1]" name="Márk" />
            </div>
            <div class="col-3 pb-3">
                <Citation :citation="subsection.Lk[index - 1]" name="Lukács" />
            </div>
            <div class="col-3 pb-3">
                <Citation :citation="subsection.Jn[index - 1]" name="János" />
            </div>
        </div>
    </template>
</template>