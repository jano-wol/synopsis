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
    <p>
        The synopsis contains the Gospels of Matthew, Mark, Luke and John in parallel. The text boxes placed next to each other present the parallel passages of the Gospels. These parallels were determined by the German theologian Kurt Aland in his work <i>Synopsis Quattuor Evangeliorum</i>.<br>
        On this site, we use this structure and fill it with various Gospel translations.
    </p>
    <h2 class="fs-3">
        Structure
    </h2>
    <ul>
        <li>
            The synopsis consists of 18 <b>parts</b>, which outline the events of the Gospels. The parts are marked with Roman numerals.
        </li>
        <li>
            Each part is divided into <b>sections</b>, a total of 362, which are marked with Arabic numerals.
        </li> 
    </ul>

    <h2 class="fs-3">
        Text Types
    </h2>
    <ul>
        <li>
            <b>Body texts:</b>
            These appear in text boxes that have bold frames and grey headers. The body texts listed beneath one another include all the verses of a given Gospel in order, without repetitions. (In the <router-link    :to="{ name: 'index' }">Index</router-link>, verses corresponding to body texts are highlighted in bold.)
        </li>
        <li>
            <b>Parallel texts:</b>
            These appear in text boxes that have thin frames and white headers. They are texts aligned in parallel with the body texts. (In the <router-link    :to="{ name: 'index' }">Index</router-link>, verses corresponding to parallel texts are not highlighted in bold.)
        </li>
    </ul>

    <h2 class="fs-3">
        Explanation of symbols
    </h2>
    <ul>
        <li>
            <i class="bi bi-arrow-up-right-square"></i> :
            <b>Opening on a separate page.</b>
            Opening the given section on a separate, standalone subpage.
        </li>
        <li>
            <i class="bi bi-arrow-down-left-square"></i> :
            <b>Opening in context.</b>
            Opening the given section within the entire text of the synopsis.
        </li>
        <li>
            <i class="bi bi-link-45deg"></i> :
            <b>Copy link.</b>
            Copying the link of the given section to the clipboard.
        </li>
        <br>
        <li>
            <i class="bi bi-compass"></i> :
            <b>Redirect to body text.</b>
            Navigating to the body text corresponding to the given parallel text.
        </li>
        <li>
            <i class="bi bi-arrow-up"></i> :
            <b>Redirect to previous body text.</b>
            Navigating to the body text preceding the given one.
        </li>
        <li>
            <i class="bi bi-arrow-down"></i> :
            <b>Redirect to next body text.</b>
            Navigating to the body text following the given one.
        </li>
    </ul>

    <p>
        
    </p>
</template>