<script lang="ts">
// TODO: need enum in enum name? what about redirection? make it consistent
import { ErrorMessageEnum } from "@/enums/ErrorMessageEnum";
import { useSynopsisStore } from "@/stores/SynopsisStore"

export default {
    data() {
        return {
            synopsisStore: useSynopsisStore(),
        }
    },
    methods: {
        getMessage(error : ErrorMessageEnum) {
        switch (error) {
            case ErrorMessageEnum.SERVER:
                return this.synopsisStore.currentDictionary.error.server;
            case ErrorMessageEnum.DATE:
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