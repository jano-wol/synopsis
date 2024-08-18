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
                            class="nav-link" aria-current="page">{{ synopsisStore.translation.menu.synopsis }}
                        </router-link>
                    </li>
                    <li class="nav-item">
                        <router-link :to="{ name: 'index' }" :class="$route.name == 'index' ? 'active' : ''"
                            class="nav-link" aria-current="page">{{ synopsisStore.translation.menu.index }}
                        </router-link>
                    </li>
                    <li class="nav-item">
                        <router-link :to="{ name: 'about' }" :class="$route.name == 'about' ? 'active' : ''"
                            class="nav-link" aria-current="page">{{ synopsisStore.translation.menu.about }}
                        </router-link>
                    </li>
                    <li class="nav-item">
                        <router-link :to="{ name: 'sources' }" :class="$route.name == 'sources' ? 'active' : ''"
                            class="nav-link" aria-current="page">{{ synopsisStore.translation.menu.sources }}
                        </router-link>
                    </li>
                    <li class="nav-item">
                        <router-link :to="{ name: 'development' }" :class="$route.name == 'development' ? 'active' : ''"
                            class="nav-link" aria-current="page">{{ synopsisStore.translation.menu.development }}
                        </router-link>
                    </li>
                </ul>
                <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
                    <li class="nav-item">
                        <button v-if="synopsisStore.language === 'en'" type="button" class="nav-link btn d-inline"
                            @click="synopsisStore.changeLanguage()">HU</button>
                        <button v-if="synopsisStore.language === 'hu'" type="button" class="nav-link btn d-inline"
                            @click="synopsisStore.changeLanguage()">EN </button>
                        <i class="bi bi-translate fs-5"></i>
                    </li>

                </ul>
            </div>
        </div>
    </nav>
</template>