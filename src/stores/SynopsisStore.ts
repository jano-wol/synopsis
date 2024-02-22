import { defineStore } from 'pinia'
import synopsis_szit from '@/assets/synopsis_szit.json'
import type { SynopsisScheme } from '@/interfaces/synopsisInterface'
const synopsis: SynopsisScheme = synopsis_szit

export const useSynopsisStore = defineStore('synopsis', {
    state: () => {
        return {
            synopsis: synopsis
        }
    },
})