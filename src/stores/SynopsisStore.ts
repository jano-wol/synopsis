import { defineStore } from 'pinia'
import synopsis_szit from '@/assets/synopsis_szit.json'
import synopsis_esv from '@/assets/synopsis_esv.json'
import translation_en from '@/assets/translation/en.json'
import translation_hu from '@/assets/translation/hu.json'
import type { SynopsisScheme } from '@/interfaces/synopsisInterface'
import router from '../router';
const synopsis: SynopsisScheme = synopsis_szit
const synopsisEsv: SynopsisScheme = synopsis_esv
//TODO: proper typing
const translationEn: any = translation_en
const translationHu: any = translation_hu

export const useSynopsisStore = defineStore('synopsis', {
    state: () => {
        return {
            translation: translationHu,
            language: "hu",
            publisher: "SZIT",
            synopsis: synopsis,
        }
    },
    actions: {
        changeLanguage() {
            if (this.language === "hu") {
                this.translation = translationEn
                this.synopsis = synopsisEsv
                this.language = "en"
                this.publisher = "ESV"
            }
            else {
                this.translation = translationHu
                this.synopsis = synopsis
                this.language = "hu"
                this.publisher = "SZIT"
            }


            const currentRouteName = router.currentRoute.value.name
            let param = ""
            if (currentRouteName === "synopsis" ||
                currentRouteName === "index" ||
                currentRouteName === "subsection") {
                    param = this.publisher
            }
            else {
                param = this.language
            }
            router.push({ name: router.currentRoute.value.name as string, params: { lang: param } });
        },
        //TODO: proper typing
        get(location: any) {

            let result: any = this.synopsis.chapters[location.chapterIndex]
            if (location.sectionIndex !== null) {
                result = result.sections[location.sectionIndex]
                if (location.subsectionIndex !== null) {
                    result = result.subsections[location.subsectionIndex]
                }
            }
            return result
        },
        setupLanguage(language: any) {
            if (language !== "en" && language !== "ESV") {
                this.translation = translationHu
                this.language = "hu"
                this.publisher = "SZIT"
                this.synopsis = synopsis
            }
            else {
                this.translation = translationEn
                this.language = "en"
                this.publisher = "ESV"
                this.synopsis = synopsisEsv
            }
        }
    }
})