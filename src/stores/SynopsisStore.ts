import { defineStore } from 'pinia'
import synopsis from '@/assets/synopsis.json'

export const useSynopsisStore = defineStore('synopsis', {
    state: () => {
        return {
            synopsis: synopsis
        }
    },
})