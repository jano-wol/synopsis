import { defineStore } from 'pinia'
import type { SectionScheme, SynopsisScheme } from '@/interfaces/synopsisInterface'
import type { DictionaryScheme } from '@/interfaces/dictionaryInterface'
import router from '../router';

import synopsisKG from '@/assets/translations/kg.json'
import synopsisSZIT from '@/assets/translations/szit.json'
import synopsisKNB from '@/assets/translations/knb.json'
import synopsisUF from '@/assets/translations/uf.json'
import synopsisESV from '@/assets/translations/esv.json'
import synopsisBT from '@/assets/translations/bt.json'
import dictionaryEn from '@/assets/languages/en.json'
import dictionaryHu from '@/assets/languages/hu.json'


export const useSynopsisStore = defineStore('synopsis', {
    state: () => {
        return {
            currentDictionary: dictionaryHu,
            currentLanguage: "hu",
            currentTranslation: "KG",
            currentSynopsis: synopsisKG,
            dictionary: {
               hu: dictionaryHu as DictionaryScheme,
               en: dictionaryEn as DictionaryScheme
            },
            synopses: [
                synopsisKG as SynopsisScheme,
                synopsisSZIT as SynopsisScheme,
                synopsisKNB as SynopsisScheme,
                synopsisUF as SynopsisScheme,
                synopsisESV as SynopsisScheme,
                synopsisBT as SynopsisScheme
            ]
        }
    },
    actions: {
        changeLanguage(language: string) {
            for (let synopsisIndex = 0; synopsisIndex < this.synopses.length; synopsisIndex++) {
                if (this.currentLanguage !== language && this.synopses[synopsisIndex].language === language) {
                    this.currentLanguage = language
                    this.currentDictionary = this.dictionary[this.currentLanguage as keyof typeof this.dictionary]

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
                for (let j = 0; j < part.sections.length; j++) {
                    const section = part.sections[j]
                    if (section.id === id) {
                        return section
                    }
                }
            }
            return this.currentSynopsis.parts[0].sections[0]
        },
        setupLanguage(language: string | string[]) {
            for (let synopsisIndex = 0; synopsisIndex < this.synopses.length; synopsisIndex++) {
                if (language === this.synopses[synopsisIndex].language) {
                    this.currentDictionary = this.dictionary[language as keyof typeof this.dictionary]
                    this.currentLanguage = language
                }
            }
        },
        setupTranslation(translation: string | string[]) {
            for (let synopsisIndex = 0; synopsisIndex < this.synopses.length; synopsisIndex++) {
                if (translation === this.synopses[synopsisIndex].translation) {
                    this.currentTranslation = translation
                    this.currentSynopsis = this.synopses[synopsisIndex]
                }
            }
        },
        getCitation(firstChapter: string, firstVerse: string, lastChapter: string, lastVerse: string) {
            const citation = firstChapter + "," + firstVerse
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