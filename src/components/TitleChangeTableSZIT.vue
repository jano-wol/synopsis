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
                        16. Keresztelő János bizonyságtétele a Messiásról
                    </td>
                    <td class="col-lg-6 align-middle">
                        16. Keresztelő János tanúságtétele a Messiásról
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
                        29. Keresztelő János bizonyságtétele
                    </td>
                    <td class="col-lg-6 align-middle">
                        29. Keresztelő János tanúságtétele
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
                        37. Jézus meggyógyítja Péter anyósát
                    </td>
                    <td class="col-lg-6 align-middle">
                        37. Jézus meggyógyítja Simon anyósát
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
                        90. Jézus lecsendesíti a vihart
                    </td>
                </tr>
                <tr>
                    <td class="col-lg-6 align-middle">
                        107. Jézus bizonyságtétele Keresztelő Jánosról
                    </td>
                    <td class="col-lg-6 align-middle">
                        107. Jézus tanúságtétele Keresztelő Jánosról
                    </td>
                </tr> 
                <tr>
                    <td class="col-lg-6 align-middle">
                        112. Jézus meggyógyítja a sorvadt kezűt szombaton
                    </td>
                    <td class="col-lg-6 align-middle">
                        112. Jézus meggyógyítja a béna kezűt szombaton
                    </td>
                </tr> 
                <tr>
                    <td class="col-lg-6 align-middle">
                        113. Jézus sok beteget gyógyít a tenger mellett
                    </td>
                    <td class="col-lg-6 align-middle">
                        113. Jézus sok beteget gyógyít a tó mellett
                    </td>
                </tr>
                <tr>
                    <td class="col-lg-6 align-middle">
                        117. Jézust Belzebub szövetségesének mondják
                    </td>
                    <td class="col-lg-6 align-middle">
                        117. Jézust Beelzebul szövetségesének mondják
                    </td>
                </tr> 
                <tr>
                    <td class="col-lg-6 align-middle">
                        124. A magvetőről szóló példázat magyarázata
                    </td>
                    <td class="col-lg-6 align-middle">
                        124. A magvetőről szóló példabeszéd magyarázata
                    </td>
                </tr>                                                                  
                <tr>
                    <td class="col-lg-6 align-middle">
                        125. „Ha valakinek van füle a hallásra, hallja!”
                    </td>
                    <td class="col-lg-6 align-middle">
                        125. „Akinek van füle a hallásra, hallja meg!”
                    </td>
                </tr>  
                <tr>
                    <td class="col-lg-6 align-middle">
                        130. Jézus példázatairól 
                    </td>
                    <td class="col-lg-6 align-middle">
                        130. Jézus példabeszédeiről
                    </td>
                </tr> 
                <tr>
                    <td class="col-lg-6 align-middle">
                        131. A búza és a konkoly példázatának értelme
                    </td>
                    <td class="col-lg-6 align-middle">
                        131. A búza és a konkoly példabeszédének értelme
                    </td>
                </tr>    
                <tr>
                    <td class="col-lg-6 align-middle">
                        134. A gazda
                    </td>
                    <td class="col-lg-6 align-middle">
                        134. A házigazda
                    </td>
                </tr>                                                   
                <tr>
                    <td class="col-lg-6 align-middle">
                        136. Jézus lecsendesíti a tengert
                    </td>
                    <td class="col-lg-6 align-middle">
                        136. Jézus lecsendesíti a vihart
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
                        147. Jézus a tengeren jár
                    </td>
                    <td class="col-lg-6 align-middle">
                        147. Jézus a vízen jár
                    </td>
                </tr>                
                <tr>
                    <td class="col-lg-6 align-middle">
                        155. „Őrizkedjetek a farizeusok kovászától!”
                    </td>
                    <td class="col-lg-6 align-middle">
                        155. „Óvakodjatok a farizeusok kovászától!”
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
                        170. Testvériség a gyülekezetben
                    </td>
                    <td class="col-lg-6 align-middle">
                        170. Testvériség az egyházban
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
                        182. A nagy parancsolat
                    </td>
                    <td class="col-lg-6 align-middle">
                        182. A főparancs
                    </td>
                </tr>                 
                <tr>
                    <td class="col-lg-6 align-middle">
                        183. Az irgalmas samaritánus
                    </td>
                    <td class="col-lg-6 align-middle">
                        183. Az irgalmas szamariai
                    </td>
                </tr>   
                <tr>
                    <td class="col-lg-6 align-middle">
                        186. Példázat a sürgős kérésről
                    </td>
                    <td class="col-lg-6 align-middle">
                        186. Példabeszéd a sürgős kérésről
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
                        192. Példázat a lámpásról
                    </td>
                    <td class="col-lg-6 align-middle">
                        192. Példabeszéd a világról
                    </td>
                </tr>   
                <tr>
                    <td class="col-lg-6 align-middle">
                        193. A test lámpása a szem
                    </td>
                    <td class="col-lg-6 align-middle">
                        193. A test világa a szem
                    </td>
                </tr>   
                <tr>
                    <td class="col-lg-6 align-middle">
                        200. A bolond gazdag
                    </td>
                    <td class="col-lg-6 align-middle">
                        200. Az esztelen gazdag
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
                        222. A hamis sáfár
                    </td>
                    <td class="col-lg-6 align-middle">
                        222. A hamis intéző
                    </td>
                </tr>   
                <tr>
                    <td class="col-lg-6 align-middle">
                        223. Hűség a kevésen
                    </td>
                    <td class="col-lg-6 align-middle">
                        223. Hűség a kicsiben
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
                        237. A farizeus és a vámszedő
                    </td>
                    <td class="col-lg-6 align-middle">
                        237. A farizeus és a vámos
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
                        265. Zákeus
                    </td>
                    <td class="col-lg-6 align-middle">
                        265. Zakeus
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
                        272. A fügefa elszáradása
                    </td>
                    <td class="col-lg-6 align-middle">
                        272. A fügefa kiszáradása
                    </td>
                </tr>
                <tr>
                    <td class="col-lg-6 align-middle">
                        275. A fügefa elszáradása
                    </td>
                    <td class="col-lg-6 align-middle">
                        275. A fügefa kiszáradása
                    </td>
                </tr>
                <tr>
                    <td class="col-lg-6 align-middle">
                        277. A két testvér példázata
                    </td>
                    <td class="col-lg-6 align-middle">
                        277. A két testvér példabeszéde
                    </td>
                </tr>                
                <tr>
                    <td class="col-lg-6 align-middle">
                        282. A nagy parancsolat
                    </td>
                    <td class="col-lg-6 align-middle">
                        282. A főparancs
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
                        291. Jézus figyelmeztet a hamis prófétákra
                    </td>
                    <td class="col-lg-6 align-middle">
                        291. Jézus figyelmeztet az álprófétákra
                    </td>
                </tr>  
                <tr>
                    <td class="col-lg-6 align-middle">
                        293. Jézus visszajövetelének időpontja, példázat a fügefáról
                    </td>
                    <td class="col-lg-6 align-middle">
                        293. Jézus visszajövetelének időpontja, példabeszéd a fügefáról
                    </td>
                </tr>                   
                <tr>
                    <td class="col-lg-6 align-middle">
                        296. Példázat vízözönről és intés éberségre
                    </td>
                    <td class="col-lg-6 align-middle">
                        296. Példabeszéd vízözönről és intés éberségre
                    </td>
                </tr>                 
                <tr>
                    <td class="col-lg-6 align-middle">
                        297. Az okos és a gonosz szolga
                    </td>
                    <td class="col-lg-6 align-middle">
                        297. Az okos és a hitvány szolga
                    </td>
                </tr>    
                <tr>
                    <td class="col-lg-6 align-middle">
                        311. Az úrvacsora
                    </td>
                    <td class="col-lg-6 align-middle">
                        311. Az utolsó vacsora
                    </td>
                </tr>
                <tr>
                    <td class="col-lg-6 align-middle">
                        314. Az új parancsolat
                    </td>
                    <td class="col-lg-6 align-middle">
                        314. Az új parancs
                    </td>
                </tr>                              
                <tr>
                    <td class="col-lg-6 align-middle">
                        318. A másik Pártfogó igérete
                    </td>
                    <td class="col-lg-6 align-middle">
                        318. A másik vigasztaló igérete
                    </td>
                </tr>
                <tr>
                    <td class="col-lg-6 align-middle">
                        319. „Békességet hagyok nektek”
                    </td>
                    <td class="col-lg-6 align-middle">
                        319. „Békességet hagyok rátok”
                    </td>
                </tr>  
                <tr>
                    <td class="col-lg-6 align-middle">
                        323. A Pártfogó bizonyságtétele
                    </td>
                    <td class="col-lg-6 align-middle">
                        323. A Vigasztaló tanúságtétele
                    </td>
                </tr>    
                <tr>
                    <td class="col-lg-6 align-middle">
                        328. Jézus megjövendöli a tanítványok elszéledését
                    </td>
                    <td class="col-lg-6 align-middle">
                        328. Jézus megjövendöli a tanítványok szétszéledését
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
                        332. Jézus a nagytanács előtt (Péter tagadása)
                    </td>
                    <td class="col-lg-6 align-middle">
                        332. Jézus a főtanács előtt (Péter tagadása)
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
                        344. Jézus megfeszítése
                    </td>
                    <td class="col-lg-6 align-middle">
                        344. Jézus keresztre feszítése
                    </td>
                </tr>    
                <tr>
                    <td class="col-lg-6 align-middle">
                        345. A megfeszített gyalázása
                    </td>
                    <td class="col-lg-6 align-middle">
                        345. A keresztre feszített gyalázása
                    </td>
                </tr>                             
                <tr>
                    <td class="col-lg-6 align-middle">
                        346. A két lator
                    </td>
                    <td class="col-lg-6 align-middle">
                        346. A két gonosztevő
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
                        360. Jézus megjelenik a tanítványoknak Tibériás tavánál
                    </td>
                </tr>
                <tr>
                    <td class="col-lg-6 align-middle">
                        367. A második, János szerinti befejezés: Jézus megjelenik a Tiberias tengernél
                    </td>
                    <td class="col-lg-6 align-middle">
                        367. A második, János szerinti befejezés: Jézus megjelenik Tibériás tavánál
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>