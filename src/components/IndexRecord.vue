<script lang="ts">
import IndexCitation from '@/components/IndexCitation.vue';
import { useSynopsisStore } from "@/stores/SynopsisStore"


export default {
    props: {
        chapterName: String,
        sections: Object //TODO: proper typing
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
    <div v-for="section in sections" class="row">
        <h3 class="text-center fs-4">{{ section.section_name }}</h3>
        <table class="table table-sm table-striped table-bordered">
            <thead>
                <tr>
                    <th class="fw-normal" scope="col">Id ( <i class="bi bi-arrow-down-left-square fs-6"></i> )</th>
                    <th class="fw-normal" scope="col">{{synopsisStore.translation.index.title}} ( <i class="bi bi-arrow-up-right-square fs-6"></i> )</th>
                    <th class="text-center fw-normal" scope="col">{{ synopsisStore.translation.evangelists.mt }}</th>
                    <th class="text-center fw-normal" scope="col">{{ synopsisStore.translation.evangelists.mk }}</th>
                    <th class="text-center fw-normal" scope="col">{{ synopsisStore.translation.evangelists.lk }}</th>
                    <th class="text-center fw-normal" scope="col">{{ synopsisStore.translation.evangelists.jn }}</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="subsection in section.subsections">
                    <th class="col-1 align-middle" scope="row">
                        <router-link :to="{ name: 'synopsis', hash: '#' + subsection.id }">
                            {{ subsection.id }}
                        </router-link>
                    </th>
                    <td class="col-7 align-middle">
                        <router-link :to="{ name: 'subsection', params: { id: subsection.id } }">
                            {{ subsection.subsection_name }}
                        </router-link>
                    </td>
                    <td class="col-1 align-middle">
                        <IndexCitation :citations="subsection.mt" />
                    </td>
                    <td class="col-1 align-middle">
                        <IndexCitation :citations="subsection.mk" />
                    </td>
                    <td class="col-1 align-middle">
                        <IndexCitation :citations="subsection.lk" />
                    </td>
                    <td class="col-1 align-middle">
                        <IndexCitation :citations="subsection.jn" />
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>
