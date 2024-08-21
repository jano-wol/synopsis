<template>
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
            eredeti sorrendjében. Minden alszekcióban egy evangélistához, legfeljebb egy törzsszöveg található.
        </li>
        <li>A párhuzamos szöveg szürke kerettel és árnyék nélkül jelenik meg.</li>
    </ul>

    <p>
        Az alszekciók címe mellett a következő gombok találhatók.
    </p>
    <ul>
        <li><i class="bi bi-arrow-up-right-square"></i> vagy <i class="bi bi-arrow-down-left-square"></i> : <br> A
            megnyitás külön oldalon ( <i class="bi bi-arrow-up-right-square"></i> ) gomb megnyomásával az adott
            alszekció megnyitható egy különálló, saját aloldalon. <br> A megnyitás az eredeti helyen ( <i
                class="bi bi-arrow-down-left-square"></i> ) gomb megnyomásával az adott alszekció elérhető a
            Szinopszis egész szövegében elhelyezve.
        </li>
        <li><i class="bi bi-link-45deg"></i> : A másolás gomb megnyomásával vágólapra kerül a link, ami az adott
            alszekcióra mutat.</li>
    </ul>

    <p>
        A Szinopszis egész szövegében, a szövegdobozok fejlécében a következő gombok találhatók.
    </p>
    <ul>
        <li><i class="bi bi-compass"></i> : Az átirányítás gombra kattintva az adott párhuzamos szöveg
            törzsszevegének
            az alszekciója érhető el a Szinopszis egész szövegében elhelyezve.
        </li>
        <li><i class="bi bi-arrow-up"></i> és <i class="bi bi-arrow-down"></i> : A navigációs gombokra kattintva az
            adott törzsszöveget megelőző ( <i class="bi bi-arrow-up"></i> ), illetve követő ( <i
                class="bi bi-arrow-down"></i> ) törzsszöveg alszekciója érhető el a Szinopszis egész
            szövegében elhelyezve.
        </li>

    </ul>

    <p>
        További részletekért lásd a <router-link :to="{ name: 'sources' }">Források</router-link> menüpontot.
    </p>
</template>