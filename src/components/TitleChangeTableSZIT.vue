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
    <div class="table-responsive">
        <table class="table bg-dark table-sm table-striped table-bordered">
            <thead>
                <tr>
                    <th class="text-nowrap" scope="col">{{ synopsisStore.translation.sources.originalTitle }}</th>
                    <th class="text-nowrap" scope="col">{{ synopsisStore.translation.sources.unifiedSZITTitle }}</th>
                </tr>
            </thead>
            <tbody class="table-group-divider">
                <tr>
                    <td class="col-lg-6 align-middle">
                        23. Tartózkodás Kapernaumban
                    </td>
                    <td class="col-lg-6 align-middle">
                        23. Tartózkodás Kafarnaumban
                    </td>
                </tr>
                <tr>
                    <td class="col-lg-6 align-middle">
                        31. Jézus és a samáriai asszony
                    </td>
                    <td class="col-lg-6 align-middle">
                        31. Jézus és a szamáriai asszony
                    </td>
                </tr>
                <tr>
                    <td class="col-lg-6 align-middle">
                        39. Jézus elhagyja Kapernaumot
                    </td>
                    <td class="col-lg-6 align-middle">
                        39. Jézus elhagyja Kafarnaumot
                    </td>
                </tr>
                <tr>
                    <td class="col-lg-6 align-middle">
                        85. Jézus meggyógyítja a kapernaumi százados szolgáját
                    </td>
                    <td class="col-lg-6 align-middle">
                        85. Jézus meggyógyítja a kafarnaumi százados szolgáját
                    </td>
                </tr>
                <tr>
                    <td class="col-lg-6 align-middle">
                        86. Jézus feltámasztja a naini ifjút
                    </td>
                    <td class="col-lg-6 align-middle">
                        86. Jézus feltámasztja a naimi ifjút
                    </td>
                </tr>
                <tr>
                    <td class="col-lg-6 align-middle">
                        141. Jézus beteget gyógyít szombaton a Betesda tavánál
                    </td>
                    <td class="col-lg-6 align-middle">
                        141. Jézus beteget gyógyít szombaton a Beteszda tavánál
                    </td>
                </tr>
                <tr>
                    <td class="col-lg-6 align-middle">
                        156. A bétsaidai vak meggyógyítása
                    </td>
                    <td class="col-lg-6 align-middle">
                        156. A betszaidai vak meggyógyítása
                    </td>
                </tr>
                <tr>
                    <td class="col-lg-6 align-middle">
                        175. Jézust nem fogadják be egy samáriai faluban
                    </td>
                    <td class="col-lg-6 align-middle">
                        175. Jézust nem fogadják be egy szamáriai faluban
                    </td>
                </tr>
                <tr>
                    <td class="col-lg-6 align-middle">
                        188. Jézust Belzebub szövetségesének mondják
                    </td>
                    <td class="col-lg-6 align-middle">
                        188. Jézust Beelzebul szövetségesének mondják
                    </td>
                </tr>
                <tr>
                    <td class="col-lg-6 align-middle">
                        220. Az elveszett drahma
                    </td>
                    <td class="col-lg-6 align-middle">
                        220. Az elveszett drachma
                    </td>
                </tr>
                <tr>
                    <td class="col-lg-6 align-middle">
                        1. A Gecsemáné kertbe vezető úton
                    </td>
                    <td class="col-lg-6 align-middle">
                        1. A Getszemáni kertbe vezető úton
                    </td>
                </tr>
                <tr>
                    <td class="col-lg-6 align-middle">
                        XI. Jézus a lombsátor-ünnepen Jeruzsálemben (János szerint)
                    </td>
                    <td class="col-lg-6 align-middle">
                        XI. Jézus a sátoros ünnepen Jeruzsálemben (János szerint)
                    </td>
                </tr>
                <tr>
                    <td class="col-lg-6 align-middle">
                        330. A Gecsemáné kertben
                    </td>
                    <td class="col-lg-6 align-middle">
                        330. A Getszemáni kertben
                    </td>
                </tr>
                <tr>
                    <td class="col-lg-6 align-middle">
                        339. Jézus és Barabbás
                    </td>
                    <td class="col-lg-6 align-middle">
                        339. Jézus és Barabás
                    </td>
                </tr>
                <tr>
                    <td class="col-lg-6 align-middle">
                        360. Jézus megjelenik a tanítványoknak a Tibériás tengernél
                    </td>
                    <td class="col-lg-6 align-middle">
                        360. Jézus megjelenik a tanítványoknak a Tibériás tavánál
                    </td>
                </tr>
                <tr>
                    <td class="col-lg-6 align-middle">
                        367. A második, János szerinti befejezés: Jézus megjelenik a Tiberias tengernél
                    </td>
                    <td class="col-lg-6 align-middle">
                        367. A második, János szerinti befejezés: Jézus megjelenik a Tiberias tavánál
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>