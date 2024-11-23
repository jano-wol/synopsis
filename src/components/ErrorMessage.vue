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
                return `Invalid date (${this.$route.params.date}). Please use the format YYYY-MM-DD (e.g., ${new Date().toISOString().split('T')[0]}).`;
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