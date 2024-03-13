import { defineStore } from 'pinia'
import synopsis_szit from '@/assets/synopsis_szit.json'
import synopsis_random from '@/assets/synopsis_random.json'
import synopsis_esv from '@/assets/synopsis_esv.json'
import type { SynopsisScheme } from '@/interfaces/synopsisInterface'
const synopsis: SynopsisScheme = synopsis_szit
const synopsis_r: SynopsisScheme = synopsis_random
const synopsisEsv: SynopsisScheme = synopsis_esv

export const useSynopsisStore = defineStore('synopsis', {
    state: () => {
        return {
            synopsis: synopsis,
            language: "hu"
        }
    },
    actions: {
        changeLanguage() {
            if (this.language == "hu")
            {
                this.synopsis = synopsisEsv
                this.language = "ra"
            }
            else {
                this.synopsis = synopsis
                this.language = "hu"
            }
        },
        //TODO: proper typing
        get(location: any) {

            let result:any = this.synopsis.chapters[location.chapterIndex]
            if (location.sectionIndex !== null)
            {
                result = result.sections[location.sectionIndex]
                if (location.subsectionIndex !== null)
                {
                    result = result.subsections[location.subsectionIndex]
                }
            }
            return result
        }
    }
})