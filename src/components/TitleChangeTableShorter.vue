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
                    <th class="text-nowrap" scope="col">{{ synopsisStore.currentDictionary.sources.originalTitle }}
                    </th>
                    <th class="text-nowrap" scope="col">{{ synopsisStore.currentDictionary.sources.shorterTitle }}</th>
                </tr>
            </thead>
            <tbody class="table-group-divider">
                <tr>
                    <td class="col-lg-6 align-middle">
                        A második, János szerinti befejezés: Jézus megjelenik a Tiberias tengernél.
                        A nagy halfogás. Jézus kérdése Péterhez, Péter megbizatása. Jézus szava Péter és a szeretett
                        tanítvány
                        sorsáról.</td>
                    <td>A második, János szerinti befejezés: Jézus megjelenik a Tiberias tengernél</td>
                </tr>
                <tr>
                    <td class="col-lg-6 align-middle">
                        The Appendix to John: Jesus at the Sea of Tiberias. Peter and the Beloved Disciple. Final Authentication</td>
                    <td>The Appendix to John: Jesus at the Sea of Tiberias</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>