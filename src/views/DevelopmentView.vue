<script lang="ts">
import { useSynopsisStore } from "@/stores/SynopsisStore"
import DevelopmentHu from '@/components/hu/DevelopmentHu.vue'
import DevelopmentEn from "@/components/en/DevelopmentEn.vue";


export default {
  data() {
    return {
      synopsisStore: useSynopsisStore()
    };
  },
  components:
  {
    DevelopmentHu,
    DevelopmentEn
  }
}

</script>

<template>
  <div class="container">
    <h1 class="text-center">{{ synopsisStore.dictionary.menu.development }}</h1>
    <DevelopmentHu v-if="synopsisStore.language === 'hu'" />
    <DevelopmentEn v-if="synopsisStore.language !== 'hu'" />
  </div>
</template>