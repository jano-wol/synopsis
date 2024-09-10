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
                    <th class="text-nowrap" scope="col">{{ synopsisStore.currentDictionary.sources.originalTitle }}</th>
                    <th class="text-nowrap" scope="col">{{ synopsisStore.currentDictionary.sources.unifiedSZITTitle }}</th>
                </tr>
            </thead>
            <tbody class="table-group-divider">
                <tr>
                    <td class="col-lg-6 align-middle">
                        14. Keresztelő János megtérésre hívó beszéde
                    </td>
                    <td class="col-lg-6 align-middle">
                        14. Keresztelő János bűnbánatra hívó beszéde
                    </td>
                </tr>            
                <tr>
                    <td class="col-lg-6 align-middle">
                        19. Jézus nemzetségi táblázata
                    </td>
                    <td class="col-lg-6 align-middle">
                        19. Jézus nemzetségtáblája
                    </td>
                </tr>
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
                        28. Utazás Judeába
                    </td>
                    <td class="col-lg-6 align-middle">
                        28. Utazás Júdeába
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
                        35. Jézus tanít a kapernaumi zsinagógában
                    </td>
                    <td class="col-lg-6 align-middle">
                        35. Jézus tanít a kafarnaumi zsinagógában
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
                        48. Jézus sok beteget gyógyít a tenger mellett
                    </td>
                    <td class="col-lg-6 align-middle">
                        48. Jézus sok beteget gyógyít a tó mellett
                    </td>
                </tr>   
                <tr>
                    <td class="col-lg-6 align-middle">
                        56. A házasságtörésről és a válásról
                    </td>
                    <td class="col-lg-6 align-middle">
                        56. A házasságtörésről és a házassági elbocsátásról
                    </td>
                </tr>        
                <tr>
                    <td class="col-lg-6 align-middle">
                        65. A test lámpása a szem
                    </td>
                    <td class="col-lg-6 align-middle">
                        65. A test világa a szem
                    </td>
                </tr>      
                <tr>
                    <td class="col-lg-6 align-middle">
                        66. Isten és a mammon
                    </td>
                    <td class="col-lg-6 align-middle">
                        66. Isten és a Mammon
                    </td>
                </tr>                                         
                <tr>
                    <td class="col-lg-6 align-middle">
                        72. Szoros kapu, keskeny út
                    </td>
                    <td class="col-lg-6 align-middle">
                        72. Szűk kapu, keskeny út
                    </td>
                </tr>  
                <tr>
                    <td class="col-lg-6 align-middle">
                        75. Aki kősziklára épít
                    </td>
                    <td class="col-lg-6 align-middle">
                        75. Aki sziklára épít
                    </td>
                </tr>  
                <tr>
                    <td class="col-lg-6 align-middle">
                        76. A Hegyi Beszéd vége
                    </td>
                    <td class="col-lg-6 align-middle">
                        76. A hegyi beszéd vége
                    </td>
                </tr>                                                               
                <tr>
                    <td class="col-lg-6 align-middle">
                        83. Aki kősziklára épít
                    </td>
                    <td class="col-lg-6 align-middle">
                        83. Aki sziklára épít
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
                        90. Jézus lecsendesíti a tengert
                    </td>
                    <td class="col-lg-6 align-middle">
                        90. Jézus lecsendesíti a tavat
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
                        XI. Jézus a lombsátor-ünnepen Jeruzsálemben (János szerint)
                    </td>
                    <td class="col-lg-6 align-middle">
                        XI. Jézus a sátoros ünnepen Jeruzsálemben (János szerint)
                    </td>
                </tr>
                <tr>
                    <td class="col-lg-6 align-middle">
                        251. Úton Judeába
                    </td>
                    <td class="col-lg-6 align-middle">
                        251. Úton Júdeába
                    </td>
                </tr>
                <tr>
                    <td class="col-lg-6 align-middle">
                        265. Zákeus
                    </td>
                    <td class="col-lg-6 align-middle">
                        265. Zakeus
                    </td>
                </tr>                
                <tr>
                    <td class="col-lg-6 align-middle">
                        290. Itélet Judea felett
                    </td>
                    <td class="col-lg-6 align-middle">
                        290. Itélet Júdea felett
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
                        355. Jézus megjelenik két tanítványnak az emmausi úton
                    </td>
                    <td class="col-lg-6 align-middle">
                        355. Jézus megjelenik két tanítványnak az emmauszi úton
                    </td>
                </tr>
                <!-- NOTE: Eredetiben egyszer Tibériás máskor Tiberiás. KG fordításnál ellenőrizd. -->
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
                        367. A második, János szerinti befejezés: Jézus megjelenik a Tibérias tavánál
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>