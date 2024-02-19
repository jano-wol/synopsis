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
  <Header />
  <RouterView />
  <Footer />
</template>

