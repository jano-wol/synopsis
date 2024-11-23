<script lang="ts">
import { useSynopsisStore } from "@/stores/SynopsisStore"

export default {
    props: {
        id: {
            type: String,
            requested: true,
            default: "0"
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
        copyShareLink() {
            navigator.clipboard.writeText(window.location.origin + "/" + this.synopsisStore.currentLanguage + "/" + this.synopsisStore.currentTranslation + "/" + this.id);
            this.isShareCopied = true
            setTimeout(() => {
                this.isShareCopied = false;
            }, 1500);
        },
        copyIdLink() {
            navigator.clipboard.writeText(window.location.origin + "/" + this.synopsisStore.currentLanguage + "/" + this.synopsisStore.currentTranslation + "#" + this.id);
            this.isIdCopied = true
            setTimeout(() => {
                this.isIdCopied = false;
            }, 1500);
        },
    }
}

</script>

<template>
    <a v-if="$route.name === 'synopsis'"
        @click="synopsisStore.pushToHistoryAndRedirect(
            { name: 'synopsis', hash: '#' + id},
            { name: 'section', params: {id: id } }
        )">
        <button type="button" class="float-right btn btn-light  btn-sm ms-1 mb-1"
            :title="synopsisStore.currentDictionary.tooltips.openSeparately">
            <i class="bi bi-arrow-up-right-square fs-6"></i>
        </button>
    </a>
    <router-link v-if="$route.name === 'section' || $route.name === 'today' || $route.name === 'calendar'"
        :to="{ name: 'synopsis', hash: '#' + id }">
        <button type="button" class="float-right btn btn-light btn-sm ms-1 mb-1"
            :title="synopsisStore.currentDictionary.tooltips.openInSynopsis">
            <i class="bi bi-arrow-down-left-square fs-6"></i>
        </button>
    </router-link>
    <button v-if="$route.name === 'synopsis'" @click="copyIdLink()" type="button"
        class=" float-right btn btn-light btn-sm ms-1 mb-1" :title="synopsisStore.currentDictionary.tooltips.location">
        <i class="bi fs-6" :class="{ 'bi-link-45deg': !isIdCopied, 'bi-check': isIdCopied }"></i>
    </button>
    <button v-if="$route.name === 'section' || $route.name === 'today' || $route.name === 'calendar'" @click="copyShareLink()" type="button"
        class="float-right  btn btn-light btn-sm ms-1 mb-1" :title="synopsisStore.currentDictionary.tooltips.share">
        <i class="bi fs-6" :class="{ 'bi-link-45deg': !isShareCopied, 'bi-check': isShareCopied }"></i>
    </button>
</template>