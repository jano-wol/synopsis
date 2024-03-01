<script lang="ts">
import IndexCitation from '@/components/IndexCitation.vue';


export default {
    props: {
        chapterName: String,
        sections: Object //TODO: proper typing
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
                    <th scope="col"></th>
                    <th scope="col"></th>
                    <th class="text-center" scope="col">Máté</th>
                    <th class="text-center" scope="col">Márk</th>
                    <th class="text-center" scope="col">Lukács</th>
                    <th class="text-center" scope="col">János</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="subsection in section.subsections">
                    <th class="col-1" scope="row">
                        <router-link :to="{ name: 'synopsis', hash: '#' + subsection.id }">
                            {{ subsection.id }}
                        </router-link>
                    </th>
                    <td class="col-7">
                        <router-link :to="{ name: 'subsection', params: { id: subsection.id } }">
                            {{ subsection.subsection_name }}
                        </router-link>
                    </td>
                    <td class="col-1">
                        <IndexCitation :citations="subsection.mt" />
                    </td>
                    <td class="col-1">
                        <IndexCitation :citations="subsection.mk" />
                    </td>
                    <td class="col-1">
                        <IndexCitation :citations="subsection.lk" />
                    </td>
                    <td class="col-1">
                        <IndexCitation :citations="subsection.jn" />
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>
