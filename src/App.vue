<script lang="ts">
import Footer from './components/Footer.vue'
import Header from './components/Header.vue'
import Loader from './components/Loader.vue'

export default {
  components: {
    Footer, Header, Loader
  },
}
</script>

<template>
  <Loader />
  <div class="d-flex flex-column min-vh-100">
    <Header />
    <div class="mt-4 wrapper flex-grow-1">
      <RouterView />
    </div>
    <Footer />
  </div>
</template>

