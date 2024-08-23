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
    <template v-for="subchapter in subchapters" class="row">
        <h3 class="text-center fs-4">{{ subchapter.subchapter_name }}</h3>
        <div class="table-responsive">
            <table class="table bg-dark table-sm table-striped table-bordered">
                <thead>
                    <tr>
                        <th class="fw-normal text-nowrap" scope="col"># ( <i
                                class="bi bi-arrow-down-left-square fs-6"></i> )</th>
                        <th class="fw-normal text-nowrap" scope="col">{{ synopsisStore.dictionary.index.title }} ( <i
                                class="bi bi-arrow-up-right-square fs-6"></i> )</th>
                        <th class="text-center fw-normal" scope="col">{{ synopsisStore.dictionary.evangelists.mt }}
                        </th>
                        <th class="text-center fw-normal" scope="col">{{ synopsisStore.dictionary.evangelists.mk }}
                        </th>
                        <th class="text-center fw-normal" scope="col">{{ synopsisStore.dictionary.evangelists.lk }}
                        </th>
                        <th class="text-center fw-normal" scope="col">{{ synopsisStore.dictionary.evangelists.jn }}
                        </th>
                    </tr>
                </thead>
                <tbody class="table-group-divider">
                    <tr v-for="subsection in subchapter.subsections">
                        <th class="col-lg-1 align-middle text-nowrap" scope="row">
                            <router-link :to="{ name: 'synopsis', hash: '#' + subsection.id }">
                                {{ subsection.id }}
                            </router-link>
                        </th>
                        <td class="col-lg-7 align-middle text-nowrap">
                            <router-link :to="{ name: 'subsection', params: { id: subsection.id } }">
                                {{ subsection.subsection_name }}
                            </router-link>
                        </td>
                        <td class="col-lg-1 align-middle">
                            <IndexCitation :citations="subsection.mt" />
                        </td>
                        <td class="col-lg-1 align-middle">
                            <IndexCitation :citations="subsection.mk" />
                        </td>
                        <td class="col-lg-1 align-middle">
                            <IndexCitation :citations="subsection.lk" />
                        </td>
                        <td class="col-lg-1 align-middle">
                            <IndexCitation :citations="subsection.jn" />
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
    </template>
</template>
