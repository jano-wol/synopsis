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
            </tbody>
        </table>
    </div>
</template>