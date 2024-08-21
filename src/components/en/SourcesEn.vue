<script lang="ts">
import TitleChangeTableSZIT from '@/components/TitleChangeTableSZIT.vue'


export default {
    components: {
        TitleChangeTableSZIT
    }
}

</script>

<template>
    <ul>
        <li>
            Biblia,
            <a href="https://szentistvantarsulat.hu/">Szent István Társulat</a>,
            <a href="https://szentiras.hu/api">szentiras.hu API</a>
        </li>
        <li>
            Bible,
            <a href="https://www.esv.org/">ESV</a>,
            <a href="https://api.esv.org/">esv.org API</a>
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
    <h2>Differences compared to sources</h2>
    <ul>
        <li>
            Secondary parallels are not included.<br>
            Reason: Simplification.<br>
        </li>
        <br>
        <li>
            Subsection 361 is not not included.<br>
            Reason: It refers to 1Cor15,3-8, which is not part of the four gospels.<br>
            Note: The numbering of other chapters remains the same.
        </li>
        <li>
            Subsection 362 is not not included.<br>
            Reason: It follows the non-canonical ending of Mark.<br>
            Note: The numbering of other chapters remains the same.
        </li>
        <br>
        <!-- TODO: Esetleg Jn6,6 és Jn6,67-71 szétvágás is lehetséges-->
        <li>
            In subsection 158, the quotation Jn6,66.67-71 has been changed to Jn6,67-71.<br>
            Reason: Simplification.
        </li>
        <li>
            In subsection 365, the quotation Mk16,15.19 has been separated to Mk16,15 and Mk16,19 .<br>
            Reason: Simplification.
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
            In SZIT translation:<br>
            In subsection 139, the quotation Mk6.6a is equivalent with quotation Mk6.6 in SZIT edition.<br>
            In subsection 142, the quotation Mk6.6b is equivalent with quotation Mk6.7 in SZIT edition.<br>
            Reason: No exceptional numbering follows the main text of the Synopsis compared to other translations.<br>
            Note: Probably an error in the editing of the text of the SZIT publisher.
        </li>
        <br>
        <li>
            In hungarian the title of subsection 367 is shorter.<br>
            Reason: Simplification.<br>
            Note: The original title is "<i>A második, János szerinti befejezés: Jézus megjelenik a Tiberias tengernél.
                A nagy halfogás. Jézus kérdése Péterhez, Péter megbizatása. Jézus szava Péter és a szeretett tanítvány
                sorsáról</i>"
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