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
        sectionLocation: {
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

            navigator.clipboard.writeText(window.location.origin + this.$route.path);
            this.isShareCopied = true
            setTimeout(() => {
                this.isShareCopied = false;
            }, 1500);
        },
        copyIdLink(id: string) {
            navigator.clipboard.writeText(window.location.origin + "/" + this.$route.params.lang + "/" + this.$route.params.translation + "#" + id);
            this.isIdCopied = true
            setTimeout(() => {
                this.isIdCopied = false;
            }, 1500);
        },
    }
}

</script>

<template>
    <router-link v-if="$route.name !== 'section'"
        :to="{ name: 'section', params: { lang: synopsisStore.language, translation: synopsisStore.translation, id: id } }"
        target="_blank">
        <button type="button" class="float-right btn btn-light  btn-sm ms-1 mb-1"
            :title="synopsisStore.dictionary.tooltips.openSeparately">
            <i class="bi bi-arrow-up-right-square fs-6"></i>
        </button>
    </router-link>
    <router-link v-if="$route.name !== 'synopsis'"
        :to="{ name: 'synopsis', params: { lang: synopsisStore.language, translation: synopsisStore.translation }, hash: '#' + id }">
        <button type="button" class="float-right btn btn-light btn-sm ms-1 mb-1"
            :title="synopsisStore.dictionary.tooltips.openInSynopsis">
            <i class="bi bi-arrow-down-left-square fs-6"></i>
        </button>
    </router-link>
    <button v-if="$route.name === 'synopsis'" @click="copyIdLink(id)" type="button"
        class=" float-right btn btn-light btn-sm ms-1 mb-1" :title="synopsisStore.dictionary.tooltips.location">
        <i class="bi fs-6" :class="{ 'bi-link-45deg': !isIdCopied, 'bi-check': isIdCopied }"></i>
    </button>
    <button v-if="$route.name === 'section'" @click="copyShareLink(id)" type="button"
        class="float-right  btn btn-light btn-sm ms-1 mb-1" :title="synopsisStore.dictionary.tooltips.share">
        <i class="bi fs-6" :class="{ 'bi-link-45deg': !isShareCopied, 'bi-check': isShareCopied }"></i>
    </button>
</template>