<script lang="ts">
import Citation from '@/components/Citation.vue'
import type { SubsectionScheme } from '@/interfaces/synopsisInterface'
import { useSynopsisStore } from "@/stores/SynopsisStore"

//TODO: proper typing
function locateSubsection(id: string): any {
    for (let i = 0; i < useSynopsisStore().synopsis.chapters.length; i++) {
        const chapter = useSynopsisStore().synopsis.chapters[i]
        for (let j = 0; j < chapter.sections.length; j++) {
            const section = chapter.sections[j]
            for (let k = 0; k < section.subsections.length; k++) {
                const subsection = section.subsections[k]
                if (subsection.id === id) {
                    return subsection
                }
            }
        }
    }
}

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
    components: {
        Citation
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
    },
    computed:
    {
        subsection() {
            return this.$route.params.id ? locateSubsection(this.$route.params.id as string) : this.synopsisStore.get(this.subsectionLocation)
        }
    }
}

</script>

<template>
    <div class="row align-items-center" :id="subsection.id">
        <div class="col-1">
        </div>
        <div class="col-10">
            <h3 class="text-center display-6">
                {{ subsection.id }}. {{ subsection.subsection_name
                }}
            </h3>
        </div>
        <div class="col-1">
            <router-link v-if="!$route.params.id" :to="{ name: 'subsection', params: { id: subsection.id } }"
                target="_blank">
                <button type="button" class=" float-right btn  btn-sm m-0"
                    :title="synopsisStore.translation.tooltips.openSeparately">
                    <i class="bi bi-arrow-up-right-square fs-6 text-secondary"></i>
                </button>
            </router-link>
            <router-link v-if="$route.params.id" :to="{ name: 'synopsis', hash: '#' + subsection.id }" target="_blank">
                <button type="button" class=" float-right btn  btn-sm m-0"
                    :title="synopsisStore.translation.tooltips.openInSynopsis">
                    <i class="bi bi-arrow-down-left-square fs-6 text-secondary"></i>
                </button>
            </router-link>
            <button @click="copyIdLink(subsection.id)" type="button" class=" float-right btn  btn-sm m-0"
                :title="synopsisStore.translation.tooltips.location">
                <i class="bi fs-6 text-secondary" :class="{ 'bi-link-45deg': !isIdCopied, 'bi-check': isIdCopied }"></i>
            </button>
            <button @click="copyShareLink(subsection.id)" type="button" class="float-right  btn  btn-sm"
                :title="synopsisStore.translation.tooltips.share">
                <i class="bi fs-6 text-secondary"
                    :class="{ 'bi-share-fill': !isShareCopied, 'bi-check': isShareCopied }"></i>
            </button>
        </div>

    </div>

    <template v-for="index in subsection.mt.length">
        <div class="row content mx-3">
            <div class="col-3 pb-3">
                <Citation v-if="subsection.mt[index - 1] !== null" :citation="subsection.mt[index - 1]" evangelist="mt"
                    :subsection-id="subsection.id" />
            </div>
            <div class="col-3 pb-3">
                <Citation v-if="subsection.mk[index - 1] !== null" :citation="subsection.mk[index - 1]" evangelist="mk"
                    :subsection-id="subsection.id" />
            </div>
            <div class="col-3 pb-3">
                <Citation v-if="subsection.lk[index - 1] !== null" :citation="subsection.lk[index - 1]" evangelist="lk"
                    :subsection-id="subsection.id" />
            </div>
            <div class="col-3 pb-3">
                <Citation v-if="subsection.jn[index - 1] !== null" :citation="subsection.jn[index - 1]" evangelist="jn"
                    :subsection-id="subsection.id" />
            </div>
        </div>
    </template>
</template>