import { defineStore } from 'pinia'
import synopsis_szit from '@/assets/synopsis_szit.json'
import synopsis_esv from '@/assets/synopsis_esv.json'
import dictionary_en from '@/assets/translation/en.json'
import dictionary_hu from '@/assets/translation/hu.json'
import type { SectionScheme, SynopsisScheme } from '@/interfaces/synopsisInterface'
import type { DictionaryScheme } from '@/interfaces/dictionaryInterface'
import router from '../router';
const synopsisSZIT: SynopsisScheme = synopsis_szit
const synopsisESV: SynopsisScheme = synopsis_esv
const dictionaryEn: DictionaryScheme = dictionary_en
const dictionaryHu: DictionaryScheme = dictionary_hu
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
        locateSection(id: string): SectionScheme {
            for (let i = 0; i < this.currentSynopsis.parts.length; i++) {
                const part = this.currentSynopsis.parts[i]
                for (let j = 0; j < part.subparts.length; j++) {
                    const subpart = part.subparts[j]
                    for (let k = 0; k < subpart.sections.length; k++) {
                        const section = subpart.sections[k]
                        if (section.id === id) {
                            return section
                        }
                    }
                }
            }
            return this.currentSynopsis.parts[0].subparts[0].sections[0]
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
        },
        getCitation(firstChapter: string, firstVerse: string, lastChapter: string, lastVerse: string) {
            let citation = firstChapter + "," + firstVerse
            if (lastChapter !== firstChapter) {
                return citation + "-" + lastChapter + "," + lastVerse
            }
            if (lastChapter === firstChapter && lastVerse !== firstVerse) {
                return citation + "-" + lastVerse
            }
            return citation
        }
    }
})