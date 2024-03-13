<script lang="ts">
import { useSynopsisStore } from "@/stores/SynopsisStore"


export default {
  data() {
    return {
      synopsisStore: useSynopsisStore()
    };
  }
}

</script>

<template>
    <div class="container">
        <h1 class="text-center">{{ synopsisStore.translation.menu.development }}</h1>
        <p>A fejlesztés GitHubon zajlik. A repo <a href="https://github.com/anwolosz/synopsis">ezen</a> a linken érhető el.</p>
        <p>A Szinopszis vázát képező .json adatbázis <a href="https://raw.githubusercontent.com/anwolosz/synopsis/main/src/assets/synopsis_szit.json">ezen</a> a linken érhető el.</p>
    </div>  
</template>
  