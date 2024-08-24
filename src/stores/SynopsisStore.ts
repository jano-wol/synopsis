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
const dictionary: any = {
    en: dictionaryEn,
    hu: dictionaryHu
}


export const useSynopsisStore = defineStore('synopsis', {
    state: () => {
        return {
            dictionary: dictionaryHu,
            language: "hu",
            translation: "SZIT",
            synopsis: synopsisSZIT,
            synopses: [synopsisSZIT, synopsisESV]
        }
    },
    actions: {
        changeLanguage(language: string) {
            for (let synopsisIndex = 0; synopsisIndex < this.synopses.length; synopsisIndex++) {
                if (this.language !== language && this.synopses[synopsisIndex].language === language) {
                    this.language = language
                    this.dictionary = dictionary[this.language]

                    this.synopsis = this.synopses[synopsisIndex]
                    this.translation = this.synopsis.translation
                    router.push({ name: router.currentRoute.value.name as string, params: { language: this.language, translation: this.translation } });
                    break
                }
            }
        },
        changeTranslation(translation: string) {
            for (let synopsisIndex = 0; synopsisIndex < this.synopses.length; synopsisIndex++) {
                if (this.synopses[synopsisIndex].translation == translation) {
                    this.synopsis = this.synopses[synopsisIndex]
                    this.translation = translation
                    router.push({ name: router.currentRoute.value.name as string, params: { language: this.language, translation: this.translation } });
                    break
                }
            }
        },
        //TODO: proper typing
        get(location: any) {

            let result: any = this.synopsis.chapters[location.chapterIndex]
            if (location.subchapterIndex !== null) {
                result = result.subchapters[location.subchapterIndex]
                if (location.sectionIndex !== null) {
                    result = result.sections[location.sectionIndex]
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