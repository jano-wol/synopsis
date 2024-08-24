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

        Synopsis contains the Gospels of Matthew, Mark, Luke and John in parallel.<br>
        On the main page, text boxes next to each other contain parallel verses of the four Gospels.<br>
    </p>

    <p>
        Two types of text boxes are distinguished:
    </p>
    <ul>
        <li>Boxes with black frame and shadow contain the body text. The body text contains the whole Gospel, without
            repetitions, in the original
            order of the verses. Each section contains maximum one body text, for one evangelist.
            In the <router-link
                :to="{ name: 'index', params: { language: synopsisStore.currentLanguage, translation: synopsisStore.currentTranslation } }">Table
                of contents</router-link> ther citation appears with bold.
        </li>
        <li>Boxes with grey frame and no shadow contain parallel text.</li>
    </ul>

    <p>
        Next to sections the following buttons can be found:
    </p>
    <ul>
        <li><i class="bi bi-arrow-up-right-square"></i> or <i class="bi bi-arrow-down-left-square"></i> : <br> Open link
            at its separate page ( <i class="bi bi-arrow-up-right-square"></i> )<br>
            Open link at original place ( <i class="bi bi-arrow-down-left-square"></i> ): returns the reader to the
            section’s original place on the main page.
        </li>
        <li><i class="bi bi-link-45deg"></i> : copies section’s link to clipboard.</li>
    </ul>

    <p>
        At the main page in the headers of text boxes the following buttons can be found:
    </p>
    <ul>
        <li><i class="bi bi-compass"></i> : Only in parallel text. Redirects the reader to where the chosen parallel
            text is found in the body text.
        </li>
        <li><i class="bi bi-arrow-up"></i> és <i class="bi bi-arrow-down"></i> : Only in main text. Redirects the reader
            to the next ( <i class="bi bi-arrow-down"></i> ) or previous ( <i class="bi bi-arrow-up"></i> ) body text in
            the same Gospel.
        </li>

    </ul>

    <p>
        More details under <router-link :to="{ name: 'sources', params: { language: synopsisStore.currentLanguage } }">Sources</router-link>.
    </p>
</template>