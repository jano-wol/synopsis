<script lang="ts">
import TitleChangeTableSZIT from '@/components/TitleChangeTableSZIT.vue'
import TitleChangeTableShorter from '@/components/TitleChangeTableShorter.vue'


export default {
    components: {
        TitleChangeTableSZIT,
        TitleChangeTableShorter
    }
}

</script>

<template>
    <h2>Differences compared to sources</h2>
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
            In section 139, the quotation Mk6.6a is equivalent with quotation Mk6.6 in SZIT edition.<br>
            In section 142, the quotation Mk6.6b is equivalent with quotation Mk6.7 in SZIT edition.<br>
            Reason: No exceptional numbering follows the main text of the Synopsis compared to other translations.<br>
            Note: Probably an error in the editing of the text of the SZIT publisher.
        </li>
        <br>
        <li>
            The title of section 367 is shorter.<br>
            Reason: Simplification.<br>
            Note: Changes are summarised in the table below.
            <TitleChangeTableShorter />
        </li>
        <br>
        <li>
            The structural names of Synopsis have been unified with the SZIT translation.<br>
            Reason: Unification.<br>
            Note: Changes are summarised in the table below.
            <TitleChangeTableSZIT />
        </li>
    </ul>
</template>