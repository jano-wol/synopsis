<script lang="ts">
import { RouterView } from 'vue-router'
import Footer from './components/Footer.vue'
import Header from './components/Header.vue'

export default {
  components: {
    Footer, Header
  }
}
</script>

<template>
  <div class="d-flex flex-column min-vh-100">
    <Header />
    <RouterView class="mt-4 wrapper flex-grow-1" />
    <Footer />
  </div>
</template>

