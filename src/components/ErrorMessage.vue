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
                return 'The requested gospel is currently unavailable.';
            case ErrorMessageEnum.DATE:
                return 'Date ERROR';
        }
        }
    }
}
</script>

<template>
    <div class="container">
        <h1 class="text-center" v-if="synopsisStore.error !== null">
                {{ getMessage(synopsisStore.error) }}
        </h1>
    </div>
</template>