<script lang="ts">
export default {
    props: {
        citations: { type: Array<any>, required: true }
    }
}
</script>

<template>
    <p v-for="citation in citations" :class="{
        'fw-bold': citation?.leading,
        'text-secondary fw-light': !citation?.primary
    }" class="text-center">
        {{ !citation?.primary || citation.citation === null ? "-" : citation?.citation }}
    </p>
</template>
