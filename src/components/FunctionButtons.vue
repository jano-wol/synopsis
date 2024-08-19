<script lang="ts">
import { useSynopsisStore } from "@/stores/SynopsisStore"

export default {
    props: {
        id: {
            type: String,
            requested: true,
            default: "0"
        },
        //TODO: proper typing
        subsectionLocation: {
            type: Object,
        }
    },
    data() {
        return {
            synopsisStore: useSynopsisStore(),
            isShareCopied: false,
            isIdCopied: false,
        }
    },
    methods: {
        copyShareLink(id: string) {
            console.log(this.$router);

            navigator.clipboard.writeText(window.location.origin + "/" + id);
            this.isShareCopied = true
            setTimeout(() => {
                this.isShareCopied = false;
            }, 1500);
        },
        copyIdLink(id: string) {
            navigator.clipboard.writeText(window.location.origin + "/#" + id);
            this.isIdCopied = true
            setTimeout(() => {
                this.isIdCopied = false;
            }, 1500);
        },
    }
}

</script>

<template>
    <router-link v-if="$route.name !== 'subsection'" :to="{ name: 'subsection', params: { id: id } }" target="_blank">
        <button type="button" class="float-right btn btn-light  btn-sm ms-1 mb-1"
            :title="synopsisStore.translation.tooltips.openSeparately">
            <i class="bi bi-arrow-up-right-square fs-6"></i>
        </button>
    </router-link>
    <router-link v-if="$route.name !== 'synopsis'" :to="{ name: 'synopsis', hash: '#' + id }">
        <button type="button" class="float-right btn btn-light btn-sm ms-1 mb-1"
            :title="synopsisStore.translation.tooltips.openInSynopsis">
            <i class="bi bi-arrow-down-left-square fs-6"></i>
        </button>
    </router-link>
    <button @click="copyIdLink(id)" type="button" class=" float-right btn btn-light btn-sm ms-1 mb-1"
        :title="synopsisStore.translation.tooltips.location">
        <i class="bi fs-6" :class="{ 'bi-link-45deg': !isIdCopied, 'bi-check': isIdCopied }"></i>
    </button>
    <button @click="copyShareLink(id)" type="button" class="float-right  btn btn-light btn-sm ms-1 mb-1"
        :title="synopsisStore.translation.tooltips.share">
        <i class="bi fs-6" :class="{ 'bi-share-fill': !isShareCopied, 'bi-check': isShareCopied }"></i>
    </button>
</template>