<script lang="ts">
import { useSynopsisStore } from '@/stores/SynopsisStore'

export default {
    data() {
        return {
            synopsisStore: useSynopsisStore(),
        }
    },
}

</script>

<style>
.hoverable:hover {
    cursor: pointer;
}

.hoverable:active {
    background: #adb5bd;
}
</style>

<template>
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
        <div class="container-fluid">
            <router-link
                :to="{ name: 'synopsis', params: { language: synopsisStore.language, translation: synopsisStore.translation } }"
                :class="$route.name == 'synopsis' ? 'active' : ''" class="navbar-brand" aria-current="page">
                <img src="/favicon.svg" alt="Szinopszis" width="33" height="33">
            </router-link>

            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav"
                aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav">
                    <li class="nav-item">
                        <router-link
                            :to="{ name: 'synopsis', params: { language: synopsisStore.language, translation: synopsisStore.translation } }"
                            :class="$route.name == 'synopsis' ? 'active' : ''" class="nav-link" aria-current="page">{{
                    synopsisStore.dictionary.menu.synopsis }}
                        </router-link>
                    </li>
                    <li class="nav-item">
                        <router-link
                            :to="{ name: 'index', params: { language: synopsisStore.language, translation: synopsisStore.translation } }"
                            :class="$route.name == 'index' ? 'active' : ''" class="nav-link" aria-current="page">{{
                    synopsisStore.dictionary.menu.index }}
                        </router-link>
                    </li>
                    <li class="nav-item">
                        <router-link :to="{ name: 'about', params: { language: synopsisStore.language } }"
                            :class="$route.name == 'about' ? 'active' : ''" class="nav-link" aria-current="page">{{
                    synopsisStore.dictionary.menu.about }}
                        </router-link>
                    </li>
                    <li class="nav-item">
                        <router-link :to="{ name: 'sources', params: { language: synopsisStore.language } }"
                            :class="$route.name == 'sources' ? 'active' : ''" class="nav-link" aria-current="page">{{
                    synopsisStore.dictionary.menu.sources }}
                        </router-link>
                    </li>
                    <li class="nav-item">
                        <router-link :to="{ name: 'contact', params: { language: synopsisStore.language } }"
                            :class="$route.name == 'contact' ? 'active' : ''" class="nav-link" aria-current="page">{{
                    synopsisStore.dictionary.menu.contact }}
                        </router-link>
                    </li>
                </ul>
                <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
                    <li class="nav-item dropdown">
                        <button class="btn btn-sm btn-light border border-light-subtle dropdown-toggle"
                            data-bs-toggle="dropdown" aria-expanded="false">
                            {{ synopsisStore.language.toUpperCase() }}
                            <i class="bi bi-globe2 fs-5 align-middle"></i>
                        </button>
                        <ul class="dropdown-menu dropdown-menu-end">
                            <template v-for="synopsis in synopsisStore.synopses">
                                <li> <a @click="synopsis.language !== synopsisStore.language ? synopsisStore.changeLanguage(synopsis.language) : null"
                                        class="dropdown-item hoverable text-black"
                                        :class="synopsis.language === synopsisStore.language ? 'bg-dark-subtle' : ''">
                                        {{ synopsis.language.toUpperCase() }}</a></li>
                            </template>
                        </ul>
                    </li>
                    <li class="nav-item dropdown">
                        <button class="btn btn-sm btn-light border border-light-subtle dropdown-toggle"
                            data-bs-toggle="dropdown" aria-expanded="false">
                            <i class="bi bi-book fs-5 align-middle"></i>
                        </button>
                        <ul class="dropdown-menu dropdown-menu-end">
                            <template v-for="synopsis in synopsisStore.synopses">
                                <li> <a @click="synopsis.translation !== synopsisStore.translation ? synopsisStore.changeTranslation(synopsis.translation) : null"
                                        class="dropdown-item hoverable text-black"
                                        :class="synopsis.translation === synopsisStore.translation ? 'bg-dark-subtle' : ''">
                                        {{ synopsis.translation}}</a></li>
                            </template>
                        </ul>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
</template>