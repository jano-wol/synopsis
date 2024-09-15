<script lang="ts">
import { useSynopsisStore } from "@/stores/SynopsisStore"
import SourcesHu from '@/components/hu/SourcesHu.vue'
import SourcesEn from "@/components/en/SourcesEn.vue";


export default {
    data() {
        return {
            synopsisStore: useSynopsisStore()
        };
    },
    components: {
        SourcesHu,
        SourcesEn
    }
}

</script>

<template>
    <div class="container">
        <h1 class="text-center">{{ synopsisStore.currentDictionary.menu.sources }}</h1>
        <ul>
            <li>
                Biblia,
                Károli Gáspár revideált,
                <a href="https://szentiras.hu/api">szentiras.hu API</a>
            </li>
            <li>
                Biblia,
                <a href="https://szentistvantarsulat.hu/">Szent István Társulat</a>,
                <a href="https://szentiras.hu/api">szentiras.hu API</a>
            </li>
            <li>
                Biblia,
                <a href="https://www.biblia-tarsulat.hu/">Káldi-Neovulgáta</a>,
                <a href="https://szentiras.hu/api">szentiras.hu API</a>
            </li>
            <li>
                Biblia,
                <a href="https://bibliatarsulat.hu">Magyar Bibliatársulat újfordítású Bibliája (1990)</a>,
                <a href="https://szentiras.hu/api">szentiras.hu API</a>
            </li>
            <li>
                Bible,
                <a href="https://www.esv.org/">ESV</a>,
                <a href="https://api.esv.org/">esv.org API</a>
            </li>
            <li>
                Biblia,
                <a href="https://pallottinum.pl/">Tysiąclecia</a>
            </li>
            <li>
                Szinopszis – Máté, Márk, Lukács és János evangéliumának párhuzamos szövege,
                <a href="https://kalvinkiado.hu/">Kálvin Kiadó</a>
                , Budapest, 1994, ISBN: 9633005922
            </li>
            <li>
                Synopsis Quattuor Evangeliorum, Kurt Aland,
                <a href="https://www.die-bibel.de/">Deutsche Bibelgesellschaft</a>
                , Stuttgart, 2005, ISBN: 9783438051301
            </li>
        </ul>
        <SourcesHu v-if="synopsisStore.currentLanguage === 'hu'" />
        <SourcesEn v-if="synopsisStore.currentLanguage !== 'hu'" />
    </div>
</template>