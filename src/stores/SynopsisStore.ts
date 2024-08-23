import { defineStore } from 'pinia'
import synopsis_szit from '@/assets/synopsis_szit.json'
import synopsis_esv from '@/assets/synopsis_esv.json'
import dictionary_en from '@/assets/translation/en.json'
import dictionary_hu from '@/assets/translation/hu.json'
import type { SynopsisScheme } from '@/interfaces/synopsisInterface'
import router from '../router';
const synopsisSZIT: SynopsisScheme = synopsis_szit
const synopsisESV: SynopsisScheme = synopsis_esv
//TODO: proper typing
const dictionaryEn: any = dictionary_en
const dictionaryHu: any = dictionary_hu

export const useSynopsisStore = defineStore('synopsis', {
    state: () => {
        return {
            dictionary: dictionaryHu,
            language: "hu",
            translation: "SZIT",
            synopsis: synopsisSZIT,
        }
    },
    actions: {
        changeLanguage() {
            if (this.language === "hu") {
                this.dictionary = dictionaryEn
                this.language = "en"
                this.synopsis = synopsisESV
                this.translation = "ESV"
            }
            else {
                this.dictionary = dictionaryHu
                this.language = "hu"
                this.synopsis = synopsisSZIT
                this.translation = "SZIT"
            }
            router.push({ name: router.currentRoute.value.name as string, params: { lang: this.language, translation: this.translation } });
        },
        changeTranslation() {
            console.log("HELLO")
            if (this.translation === "SZIT") {
                this.synopsis = synopsisESV
                this.translation = "ESV"
            }
            else {
                this.synopsis = synopsisSZIT
                this.translation = "SZIT"
            }
            router.push({ name: router.currentRoute.value.name as string, params: { lang: this.language, translation: this.translation } });
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
            if (language !== "en") {
                this.dictionary = dictionaryHu
                this.language = "hu"
            }
            else {
                this.dictionary = dictionaryEn
                this.language = "en"
            }
        },
        setupTranslation(translation: any) {
            if (translation === "SZIT") {
                this.translation = "SZIT"
                this.synopsis = synopsisSZIT
            }
            if (translation === "ESV") {
                this.translation = "ESV"
                this.synopsis = synopsisESV
            }
        }
    }
})