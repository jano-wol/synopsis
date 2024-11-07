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
        A Szinopszis Máté, Márk, Lukács és János evangéliumának párhuzamos szövege.
    </p>
    <p>
        Az egymás mellett elhelyezkedő szövegdobozok az evangélium párhuzamos részeit tartalmazzák.
    </p>
    <h2 class="fs-3">
        Felépítés
    </h2>
    <ul>
        <li>
            A Szinopszis 18 <b>részből</b> áll, amelyek az evangélium átfogó eseményeit tagolják. A részeket római számokkal jelöljük.
        </li>
        <li>
            A Szinopszis 362* <b>szekcióból</b> áll, amelyek a <b>részeket</b> taglalják. A szekciókat arab számokkal jelöljük.
        </li> 
    </ul>

    <h2 class="fs-3">
        Szövegtípusok
    </h2>
    <ul>
        <li>
            <b>Törzsszöveg:</b>
            Minden <b>szekcióban</b> egy evangélistához, pontosan egy* törzsszöveg található. A törzsszövegek összeolvasva a teljes evangéliumot tartalmazzák, ismétlődések nélkül, a versek eredeti sorrendjében.<br>
            A törzsszöveg vastag keretes, szürke fejléces szövegdobozban jelenik meg. Az
            <router-link    :to="{ name: 'index' }">Indexben</router-link>
            vastag kiemeléssel szerepelnek
            a hozzá tartozó versek.
        </li>
        <li>
            <b>Párhuzamos szöveg:</b>
            A <b>törzsszöveggel</b> párhuzamba állított szöveg.<br>
            Vékony keretes, fehér fejléces szövegdobozban jelenik meg.
        </li>
    </ul>

    <h2 class="fs-3">
        Jelmagyarázat
    </h2>
    <ul>
        <li>
            <i class="bi bi-arrow-up-right-square"></i> :
            <b>Megnyitás külön oldalon.</b>
            Az adott szekció megnyitása egy különálló, saját aloldalon.
        </li>
        <li>
            <i class="bi bi-arrow-down-left-square"></i> :
            <b>Megnyitás kontextusban.</b>
            Az adott szekció megnyitása a Szinopszis egész szövegében elhelyezve.
        </li>
        <li>
            <i class="bi bi-link-45deg"></i> :
            <b>Link másolása.</b>
            Az adott szekció linkjének vágólapra másolása.
        </li>
        <br>
        <li>
            <i class="bi bi-compass"></i> :
            <b>Átirányítás törzsszövegre.</b>
            Az adott párhuzamos szöveg törzsszövegéhez való navigálás.
        </li>
        <li>
            <i class="bi bi-arrow-up"></i> :
            <b>Átirányítás az előző törzsszövegre.</b>
            Az adott törzsszöveg előzményéhez való navigálás.
        </li>
        <li>
            <i class="bi bi-arrow-down"></i> :
            <b>Átirányítás a következő törzsszövegre.</b>
            Az adott törzsszöveg folytatásához való navigálás.
        </li>
    </ul>

    <p>
        
    </p>

    <p class="small">* Eltérés a forrástól. További részletek a <router-link :to="{ name: 'sources' }">Források</router-link> menüpont alatt találhatók.</p>
</template>