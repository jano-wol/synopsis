<script lang="ts">
import SourcesUsed from "@/components/SourcesUsed.vue"
import AvailableSources from "@/components/AvailableSources.vue"

export default {
    components: {
        SourcesUsed,
        AvailableSources
    }
}

</script>

<template>
    <h2 class="fs-3">Felhasznált források</h2>
    <SourcesUsed />    
    <h2 class="fs-3">Eltérések a forrásoktól</h2>
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
            A 139. szekcióban a Mk6,6a idézet a SZIT szerkesztésében a Mk6,6 idézetnek felel meg.<br>
            A 142. szekcióban a Mk6,6b idézet a SZIT szerkesztésében a Mk6,7 idézet elejének felel meg.<br>
            Indoklás: Nem követi kivételes számozás a Szinopszis törzsszövegét a többi fordításhoz képest.<br>
            Megjegyzés: Feltehetően hiba a Szent István Társulat szövegének szerkesztésében.
        </li>
        <li>
            Az BT fordításában:<br>
            A 229. szekcióban a Lk17,3a idézet az BT szerkesztésében a Lk17,2 idézet végének felel meg.<br>
            A 230. szekcióban a Lk17,3b idézet az BT szerkesztésében a Lk17,3 idézetnek felel meg.<br>
            Indoklás: Nem követi kivételes számozás a Szinopszis törzsszövegét a többi fordításhoz képest.<br>
            Megjegyzés: Feltehetően hiba a Biblia Tysiąclecia szövegének szerkesztésében.
        </li>
        <br>
        <li>
            A Szinopszis szerkezeti elnevezései néhány fordításban módosítva lettek.<br>
            Indoklás: Egységesítés a Biblia szöveggel, olvashatóság javítása, stb.<br>
            <!-- Megjegyzés: Az egységesítés szempontjait lásd a contributorok számára készített dokumentációban.  -->
        </li>
    </ul>
    <h2 class="fs-3">Felhasználható források</h2>
    <AvailableSources />
</template>