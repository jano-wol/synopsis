<script setup lang="ts">
import { useSynopsisStore } from '@/stores/SynopsisStore'


</script>
<template>
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
        <div class="container-fluid">
            <router-link :to="{ name: 'synopsis' }" :class="$route.name == 'synopsis' ? 'active' : ''"
                class="navbar-brand" aria-current="page">
                <img src="/favicon.svg" alt="Szinopszis" width="33" height="33">
            </router-link>

            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav"
                aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav">
                    <li class="nav-item">
                        <router-link :to="{ name: 'synopsis' }" :class="$route.name == 'synopsis' ? 'active' : ''"
                            class="nav-link" aria-current="page">Szinopszis
                        </router-link>
                    </li>
                    <li class="nav-item">
                        <router-link :to="{ name: 'index' }" :class="$route.name == 'index' ? 'active' : ''"
                            class="nav-link" aria-current="page">Tartalomjegyzék
                        </router-link>
                    </li>
                    <li class="nav-item">
                        <router-link :to="{ name: 'description' }" :class="$route.name == 'description' ? 'active' : ''"
                            class="nav-link" aria-current="page">Leírás
                        </router-link>
                    </li>
                    <li class="nav-item">
                        <router-link :to="{ name: 'details' }" :class="$route.name == 'details' ? 'active' : ''"
                            class="nav-link" aria-current="page">Részletek
                        </router-link>
                    </li>
                    <li class="nav-item">
                        <router-link :to="{ name: 'developers' }" :class="$route.name == 'developers' ? 'active' : ''"
                            class="nav-link" aria-current="page">Fejlesztőknek
                        </router-link>
                    </li>
                    <li>
                        <button class="btn" @click="useSynopsisStore().changeLanguage()">Change l</button>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
    {{ useSynopsisStore().synopsis.chapters[0].chapter_name }}
</template>