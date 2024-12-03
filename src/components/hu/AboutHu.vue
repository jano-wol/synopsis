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
        A szinopszis Máté, Márk, Lukács és János evangéliumának párhuzamos szövegeit tartalmazza. Az egymás mellett elhelyezkedő szövegdobozok az evangéliumok párhuzamos részeit mutatják be. A párhuzamokat Kurt Aland német teológus határozta meg <i>Synopsis Quattuor Evangeliorum</i> című művében.<br>
        Ezen a honlapon ezt a struktúrát töltjük fel különböző evangéliumfordításokkal.
    </p>
    <h2 class="fs-3">
        Felépítés
    </h2>
    <ul>
        <li>
            A szinopszis 18 <b>részből</b> áll, amelyek az evangélium átfogó eseményeit tagolják. A részeket római számokkal jelöljük.
        </li>
        <li>
            Az egyes részek <b>szekciókra</b> tagolódnak, összesen 362 darabra, és ezeket arab számokkal jelöljük.
        </li> 
    </ul>

    <h2 class="fs-3">
        Szövegtípusok
    </h2>
    <ul>
        <li>
            <b>Törzsszövegek:</b>
            vastag keretes, szürke fejléces szövegdobozban jelennek meg.
            Az egymás alatt elhelyezkedő törzsszövegek egy-egy evangélium összes versét ismétlődések nélkül, sorrendben tartalmazzák.
            (Az
            <router-link    :to="{ name: 'index' }">Indexben</router-link>
            a törzsszövegekhez tartozó versek vastag kiemeléssel szerepelnek.)
        </li>
        <li>
            <b>Párhuzamos szövegek:</b>
            vékony keretes, fehér fejléces szövegdobozban jelennek meg. A törzsszövegekkel párhuzamba állított szövegek.
             (Az
            <router-link    :to="{ name: 'index' }">Indexben</router-link>
            a párhuzamos szövegekhez tartozó versek kiemelés nélkül szerepelnek.)
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
            Az adott szekció megnyitása a szinopszis egész szövegében elhelyezve.
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
</template>