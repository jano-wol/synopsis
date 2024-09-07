<script lang="ts">
import IndexCitation from '@/components/IndexCitation.vue';
import type { CitationScheme, SectionScheme } from '@/interfaces/synopsisInterface';
import { useSynopsisStore } from "@/stores/SynopsisStore"


export default {
    props: {
        partTitle: String,
        sections: Array<SectionScheme>
    },
    data() {
        return {
            synopsisStore: useSynopsisStore()
        }
    },
    components: {
        IndexCitation
    }
}
</script>

<template>
    <div class="row">
        <h2 class="event text-center mt-5">
            {{ partTitle }}
        </h2>
    </div>
    
        <div clas="row">
            <div class="table-responsive">
                <table class="table bg-dark table-sm table-striped table-bordered">
                    <thead>
                        <tr>
                            <th class="fw-normal text-nowrap" scope="col"># ( <i
                                    class="bi bi-arrow-down-left-square fs-6"></i> )</th>
                            <th class="fw-normal text-nowrap" scope="col">{{ synopsisStore.currentDictionary.index.title }} ( <i
                                    class="bi bi-arrow-up-right-square fs-6"></i> )</th>
                            <th class="text-center fw-normal" scope="col">{{ synopsisStore.currentDictionary.evangelists.mt }}
                            </th>
                            <th class="text-center fw-normal" scope="col">{{ synopsisStore.currentDictionary.evangelists.mk }}
                            </th>
                            <th class="text-center fw-normal" scope="col">{{ synopsisStore.currentDictionary.evangelists.lk }}
                            </th>
                            <th class="text-center fw-normal" scope="col">{{ synopsisStore.currentDictionary.evangelists.jn }}
                            </th>
                        </tr>
                    </thead>
                    <tbody class="table-group-divider">
                        <tr v-for="section in sections" :key="section.id">
                            <th class="col-lg-1 align-middle text-nowrap" scope="row">
                                <router-link :to="{ name: 'synopsis', hash: '#' + section.id }">
                                    {{ section.id }}
                                </router-link>
                            </th>
                            <td class="col-lg-7 align-middle text-nowrap">
                                <router-link :to="{ name: 'section', params: { id: section.id } }">
                                    {{ section.section_title }}
                                </router-link>
                            </td>
                            <td class="col-lg-1 align-middle" v-for="evangelist in ['mt', 'mk', 'lk', 'jn']" :key="evangelist">
                                <IndexCitation
                                :citations="section[evangelist as keyof SectionScheme] as Array<CitationScheme>" />
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>

</template>
