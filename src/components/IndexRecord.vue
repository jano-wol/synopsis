<script lang="ts">
import IndexCitation from './IndexCitation.vue';


export default {
    props: {
        chapterName: String,
        sections: Object
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
        <table class="table table-striped table-bordered">
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
                    <th class="col-1" scope="row">{{ subsection.number }}</th>
                    <td class="col-7">{{ subsection.subsection_name }}</td>
                    <td class="col-1">
                        <IndexCitation :subsection-by-evangelist="subsection.Mt" />
                    </td>
                    <td class="col-1">
                        <IndexCitation :subsection-by-evangelist="subsection.Mk" />
                    </td>
                    <td class="col-1">
                        <IndexCitation :subsection-by-evangelist="subsection.Lk" />
                    </td>
                    <td class="col-1">
                        <IndexCitation :subsection-by-evangelist="subsection.Jn" />
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>
