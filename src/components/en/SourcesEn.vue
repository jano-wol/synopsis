<script lang="ts">
import SourcesUsed from "@/components/SourcesUsed.vue"
import AvailableSources from "@/components/AvailableSources.vue"

export default {
    components: {
        SourcesUsed,
        AvailableSources
    }
}

</script>

<template>
    <h2 class="fs-3">Sources used</h2>
    <SourcesUsed />    
    <h2 class="fs-3">Differences compared to sources</h2>
    <ul>
        <li>
            Secondary parallels are not included.<br>
            Reason: Simplification.<br>
        </li>
        <br>
        <li>
            With the exception of quotations containing the main text, the whole verse is given instead of the
            sub-verses.<br>
            Reason: Simplification.<br>
            Note: The continuity of the main text is preserved.
        </li>
        <br>
        <li>
            Section 358, 359 and 360. is not included.<br>
            Reason: These sections does not contain leading text.<br>
            Note: The numbering of other parts remains the same.
        </li>
        <li>
            Section 361 is not not included.<br>
            Reason: It refers to 1Cor15,3-8, which is not part of the four gospels.<br>
            Note: The numbering of other parts remains the same.
        </li>
        <li>
            Section 362 is not not included.<br>
            Reason: It follows the non-canonical ending of Mark.<br>
            Note: The numbering of other parts remains the same.
        </li>
        <br>
        <!-- TODO: Esetleg Jn6,6 és Jn6,67-71 szétvágás is lehetséges-->
        <li>
            In section 365, the quotation Mk16,15.19 has been separated to Mk16,15 and Mk16,19 .<br>
            Reason: Simplification.
        </li>
        <br>
        <li>
            In SZIT translation:<br>
            In section 139, the quotation Mk6,6a is equivalent with quotation Mk6,6 in SZIT edition.<br>
            In section 142, the quotation Mk6,6b is equivalent with beginning of quotation Mk6,7 in SZIT edition.<br>
            Reason: No exceptional numbering follows the main text of the Synopsis compared to other translations.<br>
            Note: Probably an error in the editing of the text of the SZIT publisher.
        </li>
        <li>
            In BT translation:<br>
            In section 229, the quotation Lk17,3a is equivalent with ending of quotation Lk17,2 in BT edition.<br>
            In section 230, the quotation Lk17,3b is equivalent with quotation Lk17,3 in BT edition.<br>
            Reason: No exceptional numbering follows the main text of the Synopsis compared to other translations.<br>
            Note: Probably an error in the editing of the text of the BT publisher.
        </li>
        <br>
        <li>
            The structural names of Synopsis have been modified in some translations.<br>
            Reason: Unification, better readability, etc.<br>
            <!-- Note: For details of the unification, see the documentation for contributors. -->
        </li>
    </ul>
    <h2 class="fs-3">Available sources</h2>
    <AvailableSources />
</template>