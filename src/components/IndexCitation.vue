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
        'text-secondary fw-light': !citation
    }" class="text-center m-1">
        {{ !citation?.citation ? "-" : citation?.citation }}
    </p>
</template>
