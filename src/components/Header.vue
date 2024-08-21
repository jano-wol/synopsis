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
<template>
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
        <div class="container-fluid">
            <router-link :to="{ name: 'synopsis', params: { lang: synopsisStore.publisher } }"
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
                        <router-link :to="{ name: 'synopsis', params: { lang: synopsisStore.publisher } }"
                            :class="$route.name == 'synopsis' ? 'active' : ''" class="nav-link" aria-current="page">{{
                synopsisStore.translation.menu.synopsis }}
                        </router-link>
                    </li>
                    <li class="nav-item">
                        <router-link :to="{ name: 'index', params: { lang: synopsisStore.publisher } }"
                            :class="$route.name == 'index' ? 'active' : ''" class="nav-link" aria-current="page">{{
                synopsisStore.translation.menu.index }}
                        </router-link>
                    </li>
                    <li class="nav-item">
                        <router-link :to="{ name: 'about', params: { lang: synopsisStore.language } }"
                            :class="$route.name == 'about' ? 'active' : ''" class="nav-link" aria-current="page">{{
                synopsisStore.translation.menu.about }}
                        </router-link>
                    </li>
                    <li class="nav-item">
                        <router-link :to="{ name: 'sources', params: { lang: synopsisStore.language } }"
                            :class="$route.name == 'sources' ? 'active' : ''" class="nav-link" aria-current="page">{{
                synopsisStore.translation.menu.sources }}
                        </router-link>
                    </li>
                    <li class="nav-item">
                        <router-link :to="{ name: 'development', params: { lang: synopsisStore.language } }"
                            :class="$route.name == 'development' ? 'active' : ''" class="nav-link"
                            aria-current="page">{{ synopsisStore.translation.menu.development }}
                        </router-link>
                    </li>
                </ul>
                <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
                    <li class="nav-item">
                        <div class="btn-group me-2">
                            <a @click="synopsisStore.language === 'hu' ? synopsisStore.changeLanguage() : null"
                                class="btn btn-light border border-light-subtle"
                                :class="synopsisStore.language !== 'hu' ? 'active' : ''">
                                EN</a>
                            <a @click="synopsisStore.language !== 'hu' ? synopsisStore.changeLanguage() : null"
                                class="btn btn-light border border-light-subtle"
                                :class="synopsisStore.language === 'hu' ? 'active' : ''">
                                HU</a>
                        </div>

                        <i class="bi bi-globe2 fs-5 align-middle"></i>
                    </li>

                </ul>
            </div>
        </div>
    </nav>
</template>