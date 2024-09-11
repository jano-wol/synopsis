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
                    <th class="text-nowrap" scope="col">{{ synopsisStore.currentDictionary.sources.unifiedKGTitle }}</th>
                </tr>
            </thead>
            <tbody class="table-group-divider">
                <tr>
                    <td class="col-lg-6 align-middle">
                        10. Menekülés Egyiptomba és visszatérés
                    </td>
                    <td class="col-lg-6 align-middle">
                        10. Menekülés Égyiptomba és visszatérés
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
                        37. Jézus meggyógyítja Péter anyósát
                    </td>
                    <td class="col-lg-6 align-middle">
                        37. Jézus meggyógyítja Simon napát
                    </td>
                </tr>                
                <tr>
                    <td class="col-lg-6 align-middle">
                        42. Jézus meggyógyít egy leprást
                    </td>
                    <td class="col-lg-6 align-middle">
                        42. Jézus meggyógyít egy bélpoklost
                    </td>
                </tr>
                <tr>
                    <td class="col-lg-6 align-middle">
                        43. Jézus meggyógyítja a bénát
                    </td>
                    <td class="col-lg-6 align-middle">
                        43. Jézus meggyógyítja a gutaütöttet
                    </td>
                </tr>
                <tr>
                    <td class="col-lg-6 align-middle">
                        45. Jézus tanítása a böjtről
                    </td>
                    <td class="col-lg-6 align-middle">
                        45. Jézus tanítása a bőjtről
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
                        63. A böjtölés
                    </td>
                    <td class="col-lg-6 align-middle">
                        63. A bőjtölés
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
                        76. A Hegyi Beszéd vége
                    </td>
                    <td class="col-lg-6 align-middle">
                        76. A hegyi beszéd vége
                    </td>
                </tr>
                <tr>
                    <td class="col-lg-6 align-middle">
                        79. „Jaj nektek!”
                    </td>
                    <td class="col-lg-6 align-middle">
                        79. „Jaj néktek!”
                    </td>
                </tr>
                <tr>
                    <td class="col-lg-6 align-middle">
                        84. Jézus meggyógyít egy leprást
                    </td>
                    <td class="col-lg-6 align-middle">
                        84. Jézus meggyógyít egy bélpoklost
                    </td>
                </tr>
                <tr>
                    <td class="col-lg-6 align-middle">
                        87. Jézus meggyógyítja Péter anyósát
                    </td>
                    <td class="col-lg-6 align-middle">
                        87. Jézus meggyógyítja Péter napát
                    </td>
                </tr>
                <tr>
                    <td class="col-lg-6 align-middle">
                        91. Jézus meggyógyít két gadarai megszállottat
                    </td>
                    <td class="col-lg-6 align-middle">
                        91. Jézus meggyógyít két gadarai ördöngőst
                    </td>
                </tr>                
                <tr>
                    <td class="col-lg-6 align-middle">
                        92. Jézus meggyógyítja a bénát
                    </td>
                    <td class="col-lg-6 align-middle">
                        92. Jézus meggyógyítja a gutaütöttet
                    </td>
                </tr>
                <tr>
                    <td class="col-lg-6 align-middle">
                        94. Jézus tanítása a böjtről
                    </td>
                    <td class="col-lg-6 align-middle">
                        94. Jézus tanítása a bőjtről
                    </td>
                </tr>
                <tr>
                    <td class="col-lg-6 align-middle">
                        97. Jézus meggyógyítja a megszállott némát
                    </td>
                    <td class="col-lg-6 align-middle">
                        97. Jézus meggyógyítja az ördöngős némát
                    </td>
                </tr>
                <tr>
                    <td class="col-lg-6 align-middle">
                        98. Az aratnivaló sok, a munkás kevés
                    </td>
                    <td class="col-lg-6 align-middle">
                        98. Az aratni való sok, a munkás kevés
                    </td>
                </tr>
                <tr>
                    <td class="col-lg-6 align-middle">
                        112. Jézus meggyógyítja a sorvadt kezűt szombaton
                    </td>
                    <td class="col-lg-6 align-middle">
                        112. Jézus meggyógyítja az elszáradt kezűt szombaton
                    </td>
                </tr>
                <tr>
                    <td class="col-lg-6 align-middle">
                        117. Jézust Belzebub szövetségesének mondják
                    </td>
                    <td class="col-lg-6 align-middle">
                        117. Jézust Belzebúb szövetségesének mondják
                    </td>
                </tr>
                <tr>
                    <td class="col-lg-6 align-middle">
                        122. Példabeszéd a magvetőről
                    </td>
                    <td class="col-lg-6 align-middle">
                        122. Példázat a magvetőről
                    </td>
                </tr>
                <tr>
                    <td class="col-lg-6 align-middle">
                        123. Miért mondasz példabeszédeket?
                    </td>
                    <td class="col-lg-6 align-middle">
                        123. Miért mondasz példázatokat?
                    </td>
                </tr>                                
                <tr>
                    <td class="col-lg-6 align-middle">
                        125. „Ha valakinek van füle a hallásra, hallja!”
                    </td>
                    <td class="col-lg-6 align-middle">
                        125. „Ha valakinek van füle a hallásra, hallja.”
                    </td>
                </tr>
                <tr>
                    <td class="col-lg-6 align-middle">
                        133. A hálóról
                    </td>
                    <td class="col-lg-6 align-middle">
                        133. A gyalomról
                    </td>
                </tr>
                <tr>
                    <td class="col-lg-6 align-middle">
                        141. Jézus beteget gyógyít szombaton a Betesda tavánál
                    </td>
                    <td class="col-lg-6 align-middle">
                        141. Jézus beteget gyógyít szombaton a Bethesda tavánál
                    </td>
                </tr>
                <tr>
                    <td class="col-lg-6 align-middle">
                        151. A kánaáni asszony
                    </td>
                    <td class="col-lg-6 align-middle">
                        151. A kananeus asszony
                    </td>
                </tr>
                <tr>
                    <td class="col-lg-6 align-middle">
                        156. A bétsaidai vak meggyógyítása
                    </td>
                    <td class="col-lg-6 align-middle">
                        156. A bethsaidai vak meggyógyítása
                    </td>
                </tr>
                <tr>
                    <td class="col-lg-6 align-middle">
                        171. Ahol ketten vagy hárman összegyűlnek…
                    </td>
                    <td class="col-lg-6 align-middle">
                        171. Ahol ketten vagy hárman egybegyűlnek…
                    </td>
                </tr>
                <tr>
                    <td class="col-lg-6 align-middle">
                        177. Jézus kiküldi hetvenkét tanítványát
                    </td>
                    <td class="col-lg-6 align-middle">
                        177. Jézus kiküldi hetven tanítványát
                    </td>
                </tr>
                <tr>
                    <td class="col-lg-6 align-middle">
                        179. „Aki titeket hallgat, engem hallgat”
                    </td>
                    <td class="col-lg-6 align-middle">
                        179. „A ki titeket hallgat, engem hallgat”
                    </td>
                </tr>
                <tr>
                    <td class="col-lg-6 align-middle">
                        180. A hetvenkét tanítvány visszatérése
                    </td>
                    <td class="col-lg-6 align-middle">
                        180. A hetven tanítvány visszatérése
                    </td>
                </tr>
                <tr>
                    <td class="col-lg-6 align-middle">
                        184. Mária és Márta
                    </td>
                    <td class="col-lg-6 align-middle">
                        184. Mária és Mártha
                    </td>
                </tr>
                <tr>
                    <td class="col-lg-6 align-middle">
                        188. Jézust Belzebub szövetségesének mondják
                    </td>
                    <td class="col-lg-6 align-middle">
                        188. Jézust Belzebúb szövetségesének mondják
                    </td>
                </tr>
                <tr>
                    <td class="col-lg-6 align-middle">
                        192. Példázat a lámpásról
                    </td>
                    <td class="col-lg-6 align-middle">
                        192. Példázat a gyertyáról
                    </td>
                </tr>
                <tr>
                    <td class="col-lg-6 align-middle">
                        195. „Óvakodjatok a farizeusok kovászától!”
                    </td>
                    <td class="col-lg-6 align-middle">
                        195. „Oltalmazzátok meg magatokat a farizeusok kovászától”
                    </td>
                </tr>
                <tr>
                    <td class="col-lg-6 align-middle">
                        197. A Szentlélek elleni bűn
                    </td>
                    <td class="col-lg-6 align-middle">
                        197. A Szent Lélek elleni bűn
                    </td>
                </tr>
                <tr>
                    <td class="col-lg-6 align-middle">
                        198. A Szentlélek segítsége
                    </td>
                    <td class="col-lg-6 align-middle">
                        198. A Szent Lélek segítsége
                    </td>
                </tr>
                <tr>
                    <td class="col-lg-6 align-middle">
                        204. Meghasonlás az evangélium miatt
                    </td>
                    <td class="col-lg-6 align-middle">
                        204. Meghasonlás az evangyéliom miatt
                    </td>
                </tr>                
                <tr>
                    <td class="col-lg-6 align-middle">
                        212. Jézus üzen Herodesnek
                    </td>
                    <td class="col-lg-6 align-middle">
                        212. Jézus üzen Heródesnek
                    </td>
                </tr>
                <tr>
                    <td class="col-lg-6 align-middle">
                        220. Az elveszett drahma
                    </td>
                    <td class="col-lg-6 align-middle">
                        220. Az elveszett drakhma
                    </td>
                </tr>
                <tr>
                    <td class="col-lg-6 align-middle">
                        223. Hűség a kevesen
                    </td>
                    <td class="col-lg-6 align-middle">
                        223. Hűség a kevésen
                    </td>
                </tr>
                <tr>
                    <td class="col-lg-6 align-middle">
                        227. A válás tilalma
                    </td>
                    <td class="col-lg-6 align-middle">
                        227. Az elbocsátás tilalma
                    </td>
                </tr>
                <tr>
                    <td class="col-lg-6 align-middle">
                        233. Tíz leprás meggyógyítása
                    </td>
                    <td class="col-lg-6 align-middle">
                        233. Tíz bélpoklos meggyógyítása
                    </td>
                </tr>
                <tr>
                    <td class="col-lg-6 align-middle">
                        235. Az Emberfia eljövetele
                    </td>
                    <td class="col-lg-6 align-middle">
                        235. Az ember Fia eljövetele
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
                        252. Kérdés a házassági elválásról
                    </td>
                    <td class="col-lg-6 align-middle">
                        252. Kérdés a házassági elbocsátásról
                    </td>
                </tr>
                <tr>
                    <td class="col-lg-6 align-middle">
                        260. A nagytanács elhatározza Jézus megölését
                    </td>
                    <td class="col-lg-6 align-middle">
                        260. A főtanács elhatározza Jézus megölését
                    </td>
                </tr>
                <tr>
                    <td class="col-lg-6 align-middle">
                        266. A minák
                    </td>
                    <td class="col-lg-6 align-middle">
                        266. A gírák
                    </td>
                </tr>
                <tr>
                    <td class="col-lg-6 align-middle">
                        268. A nagytanács elhatározza Lázár megölését
                    </td>
                    <td class="col-lg-6 align-middle">
                        268. A főtanács elhatározza Lázár megölését
                    </td>
                </tr>
                <tr>
                    <td class="col-lg-6 align-middle">
                        267. Jézus megkenetése Betániában
                    </td>
                    <td class="col-lg-6 align-middle">
                        267. Jézus megkenetése Bethániában
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
                        292. Az Emberfia eljövetele
                    </td>
                    <td class="col-lg-6 align-middle">
                        292. Az ember Fia eljövetele
                    </td>
                </tr>
                <tr>
                    <td class="col-lg-6 align-middle">
                        296. Példázat a vízözönről és intés éberségre
                    </td>
                    <td class="col-lg-6 align-middle">
                        296. Példázat az özönvízről és intés éberségre
                    </td>
                </tr>
                <tr>
                    <td class="col-lg-6 align-middle">
                        297. Az okos és a gonosz szolga
                    </td>
                    <td class="col-lg-6 align-middle">
                        297. A bölcs és a gonosz szolga
                    </td>
                </tr>
                <tr>
                    <td class="col-lg-6 align-middle">
                        299. A talentumok
                    </td>
                    <td class="col-lg-6 align-middle">
                        299. A tálentumok
                    </td>
                </tr>
                <tr>
                    <td class="col-lg-6 align-middle">
                        302. A földbe esett búzaszem
                    </td>
                    <td class="col-lg-6 align-middle">
                        302. A földbe esett gabonamag
                    </td>
                </tr>
                <tr>
                    <td class="col-lg-6 align-middle">
                        306. Jézus megkenetése Betániában"
                    </td>
                    <td class="col-lg-6 align-middle">
                        306. Jézus megkenetése Bethániában
                    </td>
                </tr>
                <tr>
                    <td class="col-lg-6 align-middle">
                        315. Úton az Olajfák hegyére, Jézus megjövendöli Péter tagadását
                    </td>
                    <td class="col-lg-6 align-middle">
                        315. Úton az olajfák hegyére, Jézus megjövendöli Péter tagadását
                    </td>
                </tr>
               <tr>
                    <td class="col-lg-6 align-middle">
                        316. A két kard
                    </td>
                    <td class="col-lg-6 align-middle">
                        316. A két szablya
                    </td>
                </tr>
                <tr>
                    <td class="col-lg-6 align-middle">
                        318. A másik Pártfogó igérete
                    </td>
                    <td class="col-lg-6 align-middle">
                        318. A másik vígasztaló igérete
                    </td>
                </tr>
                <tr>
                    <td class="col-lg-6 align-middle">
                        319. „Békességet hagyok nektek”
                    </td>
                    <td class="col-lg-6 align-middle">
                        319. „Békességet hagyok néktek”
                    </td>
                </tr>
                <tr>
                    <td class="col-lg-6 align-middle">
                        323. A Pártfogó bizonyságtétele
                    </td>
                    <td class="col-lg-6 align-middle">
                        323. A Vígasztaló bizonyságtétele
                    </td>
                </tr>
                <tr>
                    <td class="col-lg-6 align-middle">
                        325. A Szentlélek elvezet a teljes igazságra
                    </td>
                    <td class="col-lg-6 align-middle">
                        325. A Szent Lélek elvezet a teljes igazságra
                    </td>
                </tr>
                <tr>
                    <td class="col-lg-6 align-middle">
                        328. Jézus megjövendöli a tanítványok elszéledését
                    </td>
                    <td class="col-lg-6 align-middle">
                        328. Jézus megjövendöli a tanítványok szétoszlását
                    </td>
                </tr>
                <tr>
                    <td class="col-lg-6 align-middle">
                        332. Jézus a nagytanács előtt (Péter tagadása)
                    </td>
                    <td class="col-lg-6 align-middle">
                        332. Jézus a főtanács előtt (Péter tagadása)
                    </td>
                </tr>
                <tr>
                    <td class="col-lg-6 align-middle">
                        337. Jézus Heródes előtt
                    </td>
                    <td class="col-lg-6 align-middle">
                        337. Jézus Héródes előtt
                    </td>
                </tr>
                <tr>
                    <td class="col-lg-6 align-middle">
                        343. Jézus útja a Golgotára
                    </td>
                    <td class="col-lg-6 align-middle">
                        343. Jézus útja a Golgothára
                    </td>
                </tr>
                <tr>
                    <td class="col-lg-6 align-middle">
                        XVIII. Az evangéliumok befejezései
                    </td>
                    <td class="col-lg-6 align-middle">
                        XVIII. Az evangyéliomok befejezései
                    </td>
                </tr>                
                <tr>
                    <td class="col-lg-6 align-middle">
                        366. Az első, János szerinti befejezés: az evangélium célja
                    </td>
                    <td class="col-lg-6 align-middle">
                        366. Az első, János szerinti befejezés: az evangyéliom célja
                    </td>
                </tr>                
                <tr>
                    <td class="col-lg-6 align-middle">
                        367. A második, János szerinti befejezés: Jézus megjelenik a Tiberias tengernél.
                    </td>
                    <td class="col-lg-6 align-middle">
                        367. A második, János szerinti befejezés: Jézus megjelenik a Tibériás tengernél.
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>