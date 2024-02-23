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
        }
    },
    data() {
        return {
            subsection: locateSubsection(this.id),
            isCopied: false
        }
    },
    components: {
        Citation
    },
    methods: {
        copyShareLink(id: string) {
            navigator.clipboard.writeText(window.location.origin + this.$router.currentRoute.value.fullPath + id);
            this.isCopied = true
            setTimeout(() => {
                this.isCopied = false;
            }, 1500);

        }
    }
}

</script>

<template>
    <div class="row" :id="subsection.id">
        <h3 class=" event text-center display-6 mt-5">
            {{ subsection.id }}. {{ subsection.subsection_name }}
            <button @click="copyShareLink(subsection.id)" type="button" class="btn  btn-sm">
                <i class="bi fs-5 text-secondary" :class="{ 'bi-clipboard': !isCopied, 'bi-check': isCopied }"></i>
            </button>
        </h3>
    </div>

    <template v-for="index in subsection.mt.length">
        <div class="row content mx-3">
            <div class="col-3 pb-3">
                <Citation v-if="subsection.mt[index - 1] !== null" :citation="subsection.mt[index - 1]" name="Máté" />
            </div>
            <div class="col-3 pb-3">
                <Citation v-if="subsection.mk[index - 1] !== null" :citation="subsection.mk[index - 1]" name="Márk" />
            </div>
            <div class="col-3 pb-3">
                <Citation v-if="subsection.lk[index - 1] !== null" :citation="subsection.lk[index - 1]" name="Lukács" />
            </div>
            <div class="col-3 pb-3">
                <Citation v-if="subsection.jn[index - 1] !== null" :citation="subsection.jn[index - 1]" name="János" />
            </div>
        </div>
    </template>
</template>