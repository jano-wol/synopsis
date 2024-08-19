<script lang="ts">
import Citation from '@/components/Citation.vue'
import FunctionButtons from '@/components/FunctionButtons.vue'
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
        }
    },
    components: {
        Citation,
        FunctionButtons
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
    <div class="row align-items-center" :id="id">
        <div class="col-1">
        </div>
        <div class="col-10">
            <h3 class="text-center display-6">
                {{ id }}. {{ subsection.subsection_name
                }}
            </h3>
        </div>
        <div class="col-1">
            <FunctionButtons :subsection-location="subsectionLocation" :id="id"/>
        </div>

    </div>

    <template v-for="index in subsection.mt.length">
        <div class="row content mx-3">
            <div class="col-3 pb-3">
                <Citation v-if="subsection.mt[index - 1] !== null" :citation="subsection.mt[index - 1]" evangelist="mt"
                    :subsection-id="id" />
            </div>
            <div class="col-3 pb-3">
                <Citation v-if="subsection.mk[index - 1] !== null" :citation="subsection.mk[index - 1]" evangelist="mk"
                    :subsection-id="id" />
            </div>
            <div class="col-3 pb-3">
                <Citation v-if="subsection.lk[index - 1] !== null" :citation="subsection.lk[index - 1]" evangelist="lk"
                    :subsection-id="id" />
            </div>
            <div class="col-3 pb-3">
                <Citation v-if="subsection.jn[index - 1] !== null" :citation="subsection.jn[index - 1]" evangelist="jn"
                    :subsection-id="id" />
            </div>
        </div>
    </template>
</template>