<script lang="ts">
import Section from './Section.vue'


export default {
  props: {
    chapterName: String,
    sections: Object // NOTE: might be good if the object format is declared
  },
  components:{
    Section
  }
}
</script>

<template>
    <div class="row">
        <h2 class="event text-center display-4 mt-5">
            {{ chapterName }}
        </h2>
    </div>
    <Section v-for="section in sections" :section-name="section.section_name" :subsections="section.subsections"/>
</template>
