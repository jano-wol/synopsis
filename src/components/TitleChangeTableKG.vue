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
            </tbody>
        </table>
    </div>
</template>