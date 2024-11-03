<script lang="ts">
import { useSynopsisStore } from "@/stores/SynopsisStore"

export default {
    data() {
        return {
            synopsisStore: useSynopsisStore()
        };
    }
}

</script>

<template>
    <ul>
        <li v-for="synopsis in synopsisStore.synopses">
            <a
            :href="`https://raw.githubusercontent.com/anwolosz/synopsis/main/src/assets/translations/${synopsis.translation.toLowerCase()}.json`">
            {{synopsis.translation}}
            </a>
        </li>
    </ul>
</template>