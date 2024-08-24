<script lang="ts">
import Citation from '@/components/Citation.vue'
import FunctionButtons from '@/components/FunctionButtons.vue'
import type { SectionScheme } from '@/interfaces/synopsisInterface'
import { useSynopsisStore } from "@/stores/SynopsisStore"

//TODO: proper typing
function locateSection(id: string): any {
    for (let i = 0; i < useSynopsisStore().synopsis.chapters.length; i++) {
        const chapter = useSynopsisStore().synopsis.chapters[i]
        for (let j = 0; j < chapter.subchapters.length; j++) {
            const subchapter = chapter.subchapters[j]
            for (let k = 0; k < subchapter.sections.length; k++) {
                const section = subchapter.sections[k]
                if (section.id === id) {
                    return section
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
        sectionLocation: {
            type: Object,
        },
        language: {
            type: String
        },
        translation: {
            type: String
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
        section() {
            return this.$route.params.id ? locateSection(this.$route.params.id as string) : this.synopsisStore.get(this.sectionLocation)
        }
    }
}

</script>

<template>


    <div class="row align-items-center mx-3" :id="id">
        <div class="col-lg-2 col-md-12">
        </div>
        <div class="col-lg-8 col-md-12">
            <h3 class="text-center display-6">
                {{ id }}. {{ section.section_name
                }}
            </h3>
        </div>
        <div class="col-lg-2 col-md-12 d-flex justify-content-center justify-content-lg-end">
            <FunctionButtons :section-location="sectionLocation" :id="id" />
        </div>
    </div>

    <template v-for="index in section.mt.length">
        <div class="row content mx-3">
            <div class="col-lg-3 col-md-12 pb-3">
                <Citation v-if="section.mt[index - 1] !== null" :citation="section.mt[index - 1]" evangelist="mt"
                    :section-id="id" />
            </div>
            <div class="col-lg-3 col-md-12 pb-3">
                <Citation v-if="section.mk[index - 1] !== null" :citation="section.mk[index - 1]" evangelist="mk"
                    :section-id="id" />
            </div>
            <div class="col-lg-3 col-md-12 pb-3">
                <Citation v-if="section.lk[index - 1] !== null" :citation="section.lk[index - 1]" evangelist="lk"
                    :section-id="id" />
            </div>
            <div class="col-lg-3 col-md-12 pb-3">
                <Citation v-if="section.jn[index - 1] !== null" :citation="section.jn[index - 1]" evangelist="jn"
                    :section-id="id" />
            </div>
        </div>
        <hr class="d-lg-none">
    </template>
</template>