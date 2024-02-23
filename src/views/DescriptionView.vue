<template>
    <div class="container">
        <h1 class="text-center">Leírás</h1>
        <p>

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
        </p>
        <p>
            Minden alszekció mellett található egy másolás ( <i class="bi bi-clipboard"></i> )  és egy megosztás ( <i class="bi bi-share"></i> ) gomb. <br>
            A másolás gomb megnyomásával vágólapra kerül a link, ami az adott alszekcióra mutat az egész szinopszis szövegében elhelyezve. <br>
            A megosztás gomb megnyomásával vágólapra kerül a link, ami az adott alszekcióra mutat különállóan, egy saját aloldalon.
        </p>
        <p>
            További részletekért lásd a <router-link :to="{ name: 'details' }">Részletek</router-link> menüpontot.
        </p>
    </div>
</template>