<template>
    <div class="container">
        <h1 class="text-center">Leírás</h1>
        <p>

            A Szinopszis Máté, Márk, Lukács és János evangéliumának párhuzamos szövege.<br>
            Az egymás mellett elhelyezkedő szövegdobozok az evangélium párhuzamos részeit tartalmazzák.<br>
        </p>

        <p>
            Kétfajta szövegdobozt különböztetünk meg:
        </p>
        <ul>
            <li>A törzsszöveg fekete kerettel és árnyékkal jelenik meg. A <router-link
                    :to="{ name: 'index' }">tartalomjegyzékben</router-link> vastag kiemeléssel szerepelnek
                a hozzá tartozó idézetek. A törzsszöveg a teljes evangéliumot tartalmazza, ismétlődések nélkül, a versek
                eredeti sorrendjében.</li>
            <li>A párhuzamos szöveg szürke kerettel és árnyék nélkül jelenik meg.</li>
        </ul>

        <p>
            Minden alszekció mellett három gomb található.
        </p>
        <ul>
            <li><i class="bi bi-arrow-up-right-square"></i> vagy <i class="bi bi-arrow-down-left-square"></i> : <br> A
                megnyitás külön oldalon ( <i class="bi bi-arrow-up-right-square"></i> ) gomb megnyomásával az adott
                alszekció megnyitható egy különálló, saját aloldalon. <br> A megnyitás az eredeti helyen ( <i
                    class="bi bi-arrow-down-left-square"></i> ) gomb megnyomásával az adott alszekció megnyitható a
                Szinopszis egész szövegében elhelyezve.
            </li>
            <li><i class="bi bi-clipboard"></i> : A másolás gomb megnyomásával vágólapra kerül a link, ami az adott
                alszekcióra mutat az Szinopszis egész szövegében elhelyezve.</li>
            <li><i class="bi bi-share"></i> : A megosztás gomb megnyomásával vágólapra kerül a link, ami az adott
                alszekcióra mutat különállóan, egy saját aloldalon.</li>
        </ul>
        
        <p>
            További részletekért lásd a <router-link :to="{ name: 'details' }">Részletek</router-link> menüpontot.
        </p>
    </div>
</template>