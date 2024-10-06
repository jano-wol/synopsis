<script lang="ts">
import { useSynopsisStore } from "@/stores/SynopsisStore"

export default {
  data() {
    return {
      synopsisStore: useSynopsisStore(),
    }
  },
}
</script>

<style scoped>
.spinner-background {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: white;
    z-index: 9999;
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: rgba(255, 255, 255, 0.5)
}

.fade-enter-active, .fade-leave-active {
  transition: opacity 0.5s ease-in-out;
}

.fade-enter, .fade-leave-to {
  opacity: 0;
}

.fade-enter-from {
  opacity: 0;
}

.fade-enter-to {
  opacity: 1;
}
</style>

<template>
    <transition name="fade">
      <div v-if="synopsisStore.isLoading" class="spinner-background">
        <div class="spinner-border spinner-border-lg" role="status">
          <span class="visually-hidden">Loading...</span>
        </div>
      </div>
    </transition>
  </template>
