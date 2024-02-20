<script lang="ts">
import Citation from '@/components/Citation.vue'

export default {
    props: {
        subsectionName: String,
        number: String,
        matthew: { type: Array<Object>, required: true },
        mark: { type: Array<Object>, required: true },
        luke: { type: Array<Object>, required: true },
        john: { type: Array<Object>, required: true },

    },
    components: {
        Citation
    }
}
</script>

<template>
    <div class="row" :id="number">

        <h3 class=" event text-center display-6 mt-5">
            {{ number }}. {{ subsectionName }}
        </h3>
    </div>

    <template v-for="index in matthew?.length">
        <div class="row content mx-3">
            <div class="col-3 pb-3">
                <Citation :citation="matthew[index - 1]" name="Máté" />
            </div>
            <div class="col-3 pb-3">
                <Citation :citation="mark[index - 1]" name="Márk" />
            </div>
            <div class="col-3 pb-3">
                <Citation :citation="luke[index - 1]" name="Lukács" />
            </div>
            <div class="col-3 pb-3">
                <Citation :citation="john[index - 1]" name="János" />
            </div>
        </div>
    </template>
</template>