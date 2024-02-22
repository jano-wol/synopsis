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
                if (subsection.number === id) {
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
    <div class="row" :id="subsection.number">

        <h3 class=" event text-center display-6 mt-5">
            {{ subsection.number }}. {{ subsection.subsection_name }}
            <button @click="copyShareLink(subsection.number)" type="button" class="btn btn-outline-dark">
                {{ isCopied ? 'Copied!' : 'Share!' }}
            </button>
        </h3>
    </div>

    <template v-for="index in subsection.Mt.length">
        <div class="row content mx-3">
            <div class="col-3 pb-3">
                <Citation v-if="subsection.Mt[index - 1] !== null" :citation="subsection.Mt[index - 1]" name="Máté" />
            </div>
            <div class="col-3 pb-3">
                <Citation v-if="subsection.Mk[index - 1] !== null" :citation="subsection.Mk[index - 1]" name="Márk" />
            </div>
            <div class="col-3 pb-3">
                <Citation v-if="subsection.Lk[index - 1] !== null" :citation="subsection.Lk[index - 1]" name="Lukács" />
            </div>
            <div class="col-3 pb-3">
                <Citation v-if="subsection.Jn[index - 1] !== null" :citation="subsection.Jn[index - 1]" name="János" />
            </div>
        </div>
    </template>
</template>