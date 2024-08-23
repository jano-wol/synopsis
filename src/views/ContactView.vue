<script lang="ts">
import { useSynopsisStore } from "@/stores/SynopsisStore"
import ContactHu from '@/components/hu/ContactHu.vue'
import ContactEn from "@/components/en/ContactEn.vue";


export default {
  data() {
    return {
      synopsisStore: useSynopsisStore()
    };
  },
  components:
  {
    ContactHu,
    ContactEn
  }
}

</script>

<template>
  <div class="container">
    <h1 class="text-center">{{ synopsisStore.dictionary.menu.contact }}</h1>
    <ContactHu v-if="synopsisStore.language === 'hu'" />
    <ContactEn v-if="synopsisStore.language !== 'hu'" />
  </div>
</template>