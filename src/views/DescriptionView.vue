<template>
    <div class="container">
        <h1 class="text-center">Leírás</h1>
        A Szinopszis Máté, Márk, Lukács és János evangéliumának párhuzamos szövege.<br>
        Az egymás mellett elhelyezkedő szövegdobozok az evangélium párhuzamos részeit tartalmazzák.<br>
        Kétfajta szövegdobozt különböztetünk meg:
        <ul>
            <li>A törzsszöveg fekete kerettel és árnyékkal jelenik meg. A <router-link
                    :to="{ name: 'index' }">tartalomjegyzékben</router-link> vastag kiemeléssel szerepelnek
                a hozzá tartozó idézetek. A törzsszöveg a teljes evangéliumot tartalmazza, ismétlődések nélkül, a versek
                eredeti sorrendjében.</li>
            <li>A párhuzamos szöveg szürke kerettel és árnyék nélkül jelenik meg.</li>
        </ul>
        A további részletekért lásd a <router-link :to="{ name: 'details' }">Részletek</router-link> menüpontot.
    </div>
</template>