<script lang="ts">
import TitleChangeTableSZIT from '@/components/TitleChangeTableSZIT.vue'
import TitleChangeTableShorter from '@/components/TitleChangeTableShorter.vue'

export default {
    components: {
        TitleChangeTableSZIT,
        TitleChangeTableShorter,
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
    <h2>Eltérések a forrásoktól</h2>
    <ul>
        <li>
            A másodlagos párhuzamok nem szerepelnek.<br>
            Indoklás: Egyszerűsítés.<br>
        </li>
        <br>
        <li>
            A törzsszöveget tartalmazó idézetek kivételével az alversek helyett mindig az egész vers szerepel.<br>
            Indoklás: Egyszerűsítés.<br>
            Megjegyzés: A törzsszöveg folytonossága így fennmarad.
        </li>
        <br>
        <li>
            A 361. szekció nem szerepel.<br>
            Indoklás: 1Kor15,3-8 fejezetre hivatkozik, amely nem része a négy evangéliumnak.<br>
            Megjegyzés: A további fejezetek számozása nem változik.
        </li>
        <li>
            A 362. szekció nem szerepel.<br>
            Indoklás: Márk nem kanonikus befejezését követi.<br>
            Megjegyzés: A további fejezetek számozása nem változik.
        </li>
        <br>
        <!-- TODO: Esetleg Jn6,6 és Jn6,67-71 szétvágás is lehetséges-->
        <li>
            A 365. szekcióban a Mk16,15.19 idézet Mk16,15 és Mk16,19 idézetekre lett szétvágva.<br>
            Indoklás: Egyszerűsítés.
        </li>
        <br>
        <li>
            A SZIT fordításában:<br>
            A 139. szekcióban a Mk6.6a idézet a SZIT szerkesztésében a Mk6.6 idézetnek felel meg.<br>
            A 142. szekcióban a Mk6.6b idézet a SZIT szerkesztésében a Mk6.7 idézet elejének felel meg.<br>
            Indoklás: Nem követi kivételes számozás a Szinopszis törzsszövegét a többi fordításhoz képest.<br>
            Megjegyzés: Feltehetően hiba a Szent István Társulat szövegének szerkesztésében.
        </li>
        <br>
        <li>
            A 367. szekció címe rövidítve lett.<br>
            Indoklás: Egyszerűsítés.<br>
            Megjegyzés: Az címek változását az alábbi táblázat foglalja össze.
            <TitleChangeTableShorter />
        </li>
        <br>
        <li>
            A Szinopszis szerkezeti elnevezései egységesítve lettek a SZIT fordítás szerinti szóhasználattal.<br>
            Indoklás: Egységesítés.<br>
            Megjegyzés: Az elnevezések változását az alábbi táblázat foglalja össze.
            <TitleChangeTableSZIT />
        </li>
        <li>
            A Szinopszis szerkezeti elnevezései egységesítve lettek a KG fordítás szerinti szóhasználattal.<br>
            Indoklás: Egységesítés.<br>
            Megjegyzés: Az elnevezések változását az alábbi táblázat foglalja össze.
            <TitleChangeTableKG />
        </li>        
    </ul>
</template>