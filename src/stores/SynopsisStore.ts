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
            currentDictionary: dictionaryHu,
            currentLanguage: "hu",
            currentTranslation: "SZIT",
            currentSynopsis: synopsisSZIT,
            synopses: [synopsisSZIT, synopsisESV]
        }
    },
    actions: {
        changeLanguage(language: string) {
            for (let synopsisIndex = 0; synopsisIndex < this.synopses.length; synopsisIndex++) {
                if (this.currentLanguage !== language && this.synopses[synopsisIndex].language === language) {
                    this.currentLanguage = language
                    this.currentDictionary = dictionary[this.currentLanguage]

                    this.currentSynopsis = this.synopses[synopsisIndex]
                    this.currentTranslation = this.currentSynopsis.translation
                    router.push({ name: router.currentRoute.value.name as string, params: { language: this.currentLanguage, translation: this.currentTranslation } });
                    break
                }
            }
        },
        changeTranslation(translation: string) {
            for (let synopsisIndex = 0; synopsisIndex < this.synopses.length; synopsisIndex++) {
                if (this.synopses[synopsisIndex].translation == translation) {
                    this.currentSynopsis = this.synopses[synopsisIndex]
                    this.currentTranslation = translation
                    router.push({ name: router.currentRoute.value.name as string, params: { language: this.currentLanguage, translation: this.currentTranslation } });
                    break
                }
            }
        },
        //TODO: proper typing
        get(location: any) {

            let result: any = this.currentSynopsis.chapters[location.chapterIndex]
            if (location.subchapterIndex !== null) {
                result = result.subchapters[location.subchapterIndex]
                if (location.sectionIndex !== null) {
                    result = result.sections[location.sectionIndex]
                }
            }
            return result
        },
        setupLanguage(language: any) {
            for (let synopsisIndex = 0; synopsisIndex < this.synopses.length; synopsisIndex++) {
                if (language === this.synopses[synopsisIndex].language) {
                    this.currentDictionary = dictionary[language]
                    this.currentLanguage = language
                }
            }
        },
        setupTranslation(translation: any) {
            for (let synopsisIndex = 0; synopsisIndex < this.synopses.length; synopsisIndex++) {
                if (translation === this.synopses[synopsisIndex].translation) {
                    this.currentTranslation = translation
                    this.currentSynopsis = this.synopses[synopsisIndex]
                }
            }
        }
    }
})