<script lang="ts">
import Citation from '@/components/Citation.vue'
import FunctionButtons from '@/components/FunctionButtons.vue'
import type { CitationScheme, SectionScheme } from '@/interfaces/synopsisInterface';
import { useSynopsisStore } from "@/stores/SynopsisStore"

export default {
    props: {
        id: {
            type: String,
            requested: true,
            default: "0"
        },
        //TODO: remove unused props, language, translation
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
    mounted()
    {
        if (this.$route.name === 'section')
        {
            this.synopsisStore.getGospel(new Date().toISOString().split('T')[0]).then(() => { console.log(this.synopsisStore.dailyGospelSections)});
        }
    },
    components: {
        Citation,
        FunctionButtons
    },
    computed:
    {
        section() {
            return this.synopsisStore.locateSection(this.id)
        }
    }
}

</script>

<style>
.scroll-margin {
    scroll-margin-top: 60px;
}
</style>

<template>


    <div class="scroll-margin row align-items-center mx-3 mt-1" :id="id">
        <div class="col-lg-2 col-md-12">
        </div>
        <div class="col-lg-8 col-md-12">
            <h4 class="text-center fs-3">
                {{ id }}. {{ section.section_title }}
                <i v-if="synopsisStore.dailyGospelSections.includes(id)" class="bi bi-sun"></i>
            </h4>
        </div>
        <div class="col-lg-2 col-md-12 d-flex justify-content-center justify-content-lg-end">
            <FunctionButtons :id="id" />
        </div>
    </div>

    <template v-for="index in section.mt.length" :key="index">
        <div class="row content mx-3 mb-2">
            <div class="col-lg-3 col-md-12 pb-3" v-for="evangelist in ['mt', 'mk', 'lk', 'jn']" :key="evangelist">
                <Citation v-if="section[evangelist as keyof SectionScheme][index - 1] !== null"
                :citation="section[evangelist as keyof SectionScheme][index - 1] as CitationScheme"
                :evangelist="evangelist"
                :section-id="id" />
            </div>
        </div>
        <hr class="d-lg-none">
    </template>
</template>