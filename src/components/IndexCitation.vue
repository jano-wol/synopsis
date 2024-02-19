<script lang="ts">
export default {
    props: {
        subsectionByEvangelist: { type: Array<any>, required: true }
    }
}
</script>

<template>
    <p v-for="index in subsectionByEvangelist?.length" :class="{
        'fw-bold': subsectionByEvangelist[index - 1]?.leading,
        'text-secondary fw-light': !subsectionByEvangelist[index - 1]?.primary
    }" class="text-center">
        <template v-if="subsectionByEvangelist[index - 1]?.primary">
            {{ subsectionByEvangelist[index - 1]?.citation }}
        </template>
    </p>
</template>
