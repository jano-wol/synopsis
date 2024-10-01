<script lang="ts">
import { useSynopsisStore } from '@/stores/SynopsisStore'

export default {
    data() {
        return {
            synopsisStore: useSynopsisStore(),
            isHeaderVisible: false,
            navbarHeight: 0
        }
    },
    mounted() {
        this.navbarHeight = this.$refs.customNavbar.offsetHeight;

        window.addEventListener('mousemove', this.handleMouseMove);
        window.addEventListener('scroll', this.checkScrollPosition);
        window.addEventListener('resize', this.updateNavbarHeight);
        this.checkScrollPosition(); // Initial check for scroll position
    },
    beforeDestroy() {
        window.removeEventListener('mousemove', this.handleMouseMove);
        window.removeEventListener('scroll', this.checkScrollPosition);
        window.removeEventListener('resize', this.updateNavbarHeight);
    },
    methods: {
        handleMouseMove(event: MouseEvent) {
            // Check if the dropdown menu is open
            const isDropdownOpen = this.$el.querySelector('.dropdown-menu.show') !== null;

            // Logic to show the header
            if (isDropdownOpen) {
                this.isHeaderVisible = true; // Always show if dropdown is open
            } else {
                // Show if at the top or mouse is within navbar height
                this.isHeaderVisible = window.scrollY === 0 || event.clientY <= this.navbarHeight;
            }
        },
        checkScrollPosition() {
            // Always show the header if at the top
            this.isHeaderVisible = window.scrollY === 0;
        },
        updateNavbarHeight() {
            // Update the navbar height if the window is resized
            this.navbarHeight = this.$refs.customNavbar.offsetHeight;
        },
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

.xyz {
    opacity: 0; /* Start hidden */
    transform: translateY(-20px); /* Start slightly above */
    transition: opacity 0.3s ease, transform 0.3s ease; /* Transition for smooth effect */
}

.xyz.visible {
    opacity: 1; /* Make visible */
    transform: translateY(0); /* Move to original position */
}

</style>

<template>
    <nav ref="customNavbar" :class="['xyz', { visible: isHeaderVisible }]" class="navbar navbar-expand-lg bg-body-tertiary sticky-top shadow-sm">
        <div class="container-fluid">
            <router-link
                :to="{ name: 'synopsis', params: { language: synopsisStore.currentLanguage, translation: synopsisStore.currentTranslation } }"
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
                            :to="{ name: 'synopsis', params: { language: synopsisStore.currentLanguage, translation: synopsisStore.currentTranslation } }"
                            :class="$route.name == 'synopsis' ? 'active' : ''" class="nav-link" aria-current="page">{{
                    synopsisStore.currentDictionary.menu.synopsis }}
                        </router-link>
                    </li>
                    <li class="nav-item">
                        <router-link
                            :to="{ name: 'index', params: { language: synopsisStore.currentLanguage, translation: synopsisStore.currentTranslation } }"
                            :class="$route.name == 'index' ? 'active' : ''" class="nav-link" aria-current="page">{{
                    synopsisStore.currentDictionary.menu.index }}
                        </router-link>
                    </li>
                    <li class="nav-item">
                        <router-link :to="{ name: 'about', params: { language: synopsisStore.currentLanguage } }"
                            :class="$route.name == 'about' ? 'active' : ''" class="nav-link" aria-current="page">{{
                    synopsisStore.currentDictionary.menu.about }}
                        </router-link>
                    </li>
                    <li class="nav-item">
                        <router-link :to="{ name: 'sources', params: { language: synopsisStore.currentLanguage } }"
                            :class="$route.name == 'sources' ? 'active' : ''" class="nav-link" aria-current="page">{{
                    synopsisStore.currentDictionary.menu.sources }}
                        </router-link>
                    </li>
                    <li class="nav-item">
                        <router-link :to="{ name: 'contact', params: { language: synopsisStore.currentLanguage } }"
                            :class="$route.name == 'contact' ? 'active' : ''" class="nav-link" aria-current="page">{{
                    synopsisStore.currentDictionary.menu.contact }}
                        </router-link>
                    </li>
                </ul>
                <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
                    <li class="nav-item dropdown">
                        <button class="btn btn-sm btn-light border border-light-subtle dropdown-toggle"
                            data-bs-toggle="dropdown" aria-expanded="false">
                            <span class="align-middle me-2">{{ synopsisStore.currentLanguage.toUpperCase() }}</span>
                            <i class="bi bi-globe2 fs-5 align-middle"></i>
                        </button>
                        <ul class="dropdown-menu dropdown-menu-end">
                            <template v-for="key in Object.keys(synopsisStore.dictionary)" :key="key">
                                <li> <a @click="key !== synopsisStore.currentLanguage ? synopsisStore.changeLanguage(key) : null"
                                        class="dropdown-item hoverable text-black"
                                        :class="key === synopsisStore.currentLanguage ? 'bg-dark-subtle' : ''">
                                        {{ key.toUpperCase() }}</a></li>
                            </template>
                        </ul>
                    </li>
                    <li class="nav-item dropdown">
                        <button class="btn btn-sm btn-light border border-light-subtle dropdown-toggle"
                            data-bs-toggle="dropdown" aria-expanded="false">
                            <i class="bi bi-book fs-5 align-middle"></i>
                        </button>
                        <ul class="dropdown-menu dropdown-menu-end">
                            <li>
                                <h6 class="dropdown-header">{{ synopsisStore.currentDictionary.menu.translations }}</h6>
                            </li>
                            <template v-for="synopsis in synopsisStore.synopses" :key="synopsis.translation">
                                <li>
                                    <a @click="synopsis.translation !== synopsisStore.currentTranslation ? synopsisStore.changeTranslation(synopsis.translation) : null"
                                        class="dropdown-item hoverable text-black d-flex justify-content-between"
                                        :class="synopsis.translation === synopsisStore.currentTranslation ? 'bg-dark-subtle' : ''">
                                        <span class="me-3">{{ synopsis.name }}</span>
                                        <span>({{ synopsis.language }})</span>
                                    </a>
                                </li>
                            </template>
                        </ul>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
</template>