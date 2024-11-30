<script lang="ts">
import { ErrorCode } from "@/enums/ErrorCode";
import { useSynopsisStore } from "@/stores/SynopsisStore"

export default {
    data() {
        return {
            synopsisStore: useSynopsisStore(),
        }
    },
    methods: {
        getMessage(error : ErrorCode) {
        switch (error) {
            case ErrorCode.SERVER:
                return this.synopsisStore.currentDictionary.error.server;
            case ErrorCode.DATE:
                return this.synopsisStore.currentDictionary.error.date;
        }
        }
    }
}
</script>

<template>
    <div class="container">
        <p class="text-center" v-if="synopsisStore.error !== null">
                {{ getMessage(synopsisStore.error) }}
        </p>
    </div>
</template>