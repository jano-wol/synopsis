<template>
    <p>

        Synopsis contains the Gospels of Matthew, Mark, Luke and John in parallel.<br>
        On the main page, text boxes next to each other contain parallel verses of the four Gospels.<br>
    </p>

    <p>
        Two types of text boxes are distinguished:
    </p>
    <ul>
        <li>Boxes with black frame and shadow contain the body text. A <router-link
                :to="{ name: 'index' }">tartalomjegyzékben</router-link> vastag kiemeléssel szerepelnek
            a hozzá tartozó idézetek. A törzsszöveg a teljes evangéliumot tartalmazza, ismétlődések nélkül, a versek
            eredeti sorrendjében. Minden alszekcióban egy evangélistához, legfeljebb egy törzsszöveg található.
        </li>
        <li>Boxes with grey frame and no shadow contain parallel text.</li>
    </ul>

    <p>
        Next to subsections the following buttons can be found:
    </p>
    <ul>
        <li><i class="bi bi-arrow-up-right-square"></i> or <i class="bi bi-arrow-down-left-square"></i> : <br> Open link
            at its separate page ( <i class="bi bi-arrow-up-right-square"></i> )<br>
            Open link at original place ( <i class="bi bi-arrow-down-left-square"></i> ): returns the reader to the
            subsection’s original place on the main page.
        </li>
        <li><i class="bi bi-link-45deg"></i> : copies subsection’s link on the main page to clipboard.</li>
        <li><i class="bi bi-share-fill"></i> : copies subsection’s link at its separate page to clipboard.</li>
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
        More details under <router-link :to="{ name: 'sources' }">Sources</router-link>.
    </p>
</template>