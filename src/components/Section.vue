<script lang="ts">
import Subsection from '@/components/Subsection.vue'

export default {
    props: {
        sectionName: String,
        subsections: Object // NOTE: might be good if the object format is declared
    },
    components: {
        Subsection
    }
}
</script>

<template>
    <div class="row">
        <h4 class="event text-center display-5">
            {{ sectionName }}
        </h4>
    </div>

    <Subsection v-for="subsection in subsections"
    :number="subsection.number"
    :subsection-name="subsection.subsection_name"
    :matthew="subsection.Mt"
    :mark="subsection.Mk"
    :luke="subsection.Lk"
    :john="subsection.Jn" />
</template>