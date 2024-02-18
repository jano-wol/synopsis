<script lang="ts">
import Citation from './Citation.vue'

export default {
    props: {
        subsectionName: String,
        number: String,
        matthew: Array,
        mark: Array,
        luke: Array,
        john: Array,

    },
    components: {
        Citation
    }
}
</script>

<template>
    <div class="row">

        <h3 class=" event text-center display-6 mt-5">
            {{ number }}. {{ subsectionName }}
        </h3>
    </div>

    <div class="row content mx-3">

        <div v-for="citation in matthew" class="col-3 pb-3">
            <Citation :citation="citation" name="Máté" />
        </div>
        <div v-for="citation in mark" class="col-3 pb-3">
            <Citation :citation="citation" name="Márk" />
        </div>
        <div v-for="citation in luke" class="col-3 pb-3">
            <Citation :citation="citation" name="Lukács" />
        </div>
        <div v-for="citation in john" class="col-3 pb-3">
            <Citation :citation="citation" name="János" />
        </div>
    </div>
</template>