<script lang="ts">
import IndexCitation from '@/components/IndexCitation.vue';
import { useSynopsisStore } from "@/stores/SynopsisStore"


export default {
    props: {
        chapterName: String,
        subchapters: Object //TODO: proper typing
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
            {{ chapterName }}
        </h2>
    </div>
    <template v-for="subchapter in subchapters">
        <div clas="row">
            <h3 class="text-center fs-4">{{ subchapter.subchapter_name }}</h3>
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
                        <tr v-for="section in subchapter.sections">
                            <th class="col-lg-1 align-middle text-nowrap" scope="row">
                                <router-link :to="{ name: 'synopsis', hash: '#' + section.id }">
                                    {{ section.id }}
                                </router-link>
                            </th>
                            <td class="col-lg-7 align-middle text-nowrap">
                                <router-link :to="{ name: 'section', params: { id: section.id } }">
                                    {{ section.section_name }}
                                </router-link>
                            </td>
                            <td class="col-lg-1 align-middle">
                                <IndexCitation :citations="section.mt" />
                            </td>
                            <td class="col-lg-1 align-middle">
                                <IndexCitation :citations="section.mk" />
                            </td>
                            <td class="col-lg-1 align-middle">
                                <IndexCitation :citations="section.lk" />
                            </td>
                            <td class="col-lg-1 align-middle">
                                <IndexCitation :citations="section.jn" />
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </template>
</template>
