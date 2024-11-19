import { ref, onMounted, nextTick } from 'vue';
import { defineStore } from 'pinia'
import type { CitationScheme, PartScheme, SectionScheme, SynopsisScheme } from '@/interfaces/synopsisInterface'
import type { DictionaryScheme } from '@/interfaces/dictionaryInterface'
import router from '../router';
import type { RouteLocationRaw } from 'vue-router';

import { fetchDailyGospel, parseCitation } from '@/utils/dailyGospel';


import synopsisKG from '@/assets/translations/kg.json'
import synopsisSZIT from '@/assets/translations/szit.json'
import synopsisKNB from '@/assets/translations/knb.json'
import synopsisRUF from '@/assets/translations/ruf.json'
import synopsisESV from '@/assets/translations/esv.json'
import synopsisBT from '@/assets/translations/bt.json'
import synopsisBJW from '@/assets/translations/bjw.json'
import synopsisSBLGNT from '@/assets/translations/sblgnt.json'
import synopsisNV from '@/assets/translations/nv.json'
import dictionaryEn from '@/assets/languages/en.json'
import dictionaryHu from '@/assets/languages/hu.json'
import type { QuoteScheme } from '@/interfaces/dailyGospelInterface';


export const useSynopsisStore = defineStore('synopsis', {
    state: () => {
        return {
            currentDictionary: dictionaryHu,
            currentLanguage: "hu",
            currentTranslation: "",
            currentSynopsis: synopsisKG,
            dictionary: {
               hu: dictionaryHu as DictionaryScheme,
               en: dictionaryEn as DictionaryScheme
            },
            synopses: [
                synopsisKG as SynopsisScheme,
                synopsisSZIT as SynopsisScheme,
                synopsisKNB as SynopsisScheme,
                synopsisRUF as SynopsisScheme,
                synopsisESV as SynopsisScheme,
                synopsisBT as SynopsisScheme,
                synopsisBJW as SynopsisScheme,
                synopsisSBLGNT as SynopsisScheme,
                synopsisNV as SynopsisScheme
            ],
            isLoading: false,
            dailyGospel: null as null | QuoteScheme,
            dailyGospelSections: [] as Array<string>,
        }
    },
    actions: {
        loading(task: () => void) {
                this.isLoading = true;
                setTimeout(() => {
                    task();
                    this.isLoading = false;
                }, 0);
        },
        changeLanguage(language: string) {
            this.loading(() => 
            {
                for (let synopsisIndex = 0; synopsisIndex < this.synopses.length; synopsisIndex++) {
                    if (this.currentLanguage !== language && this.synopses[synopsisIndex].language === language) {
                        this.currentLanguage = language
                        this.currentDictionary = this.dictionary[this.currentLanguage as keyof typeof this.dictionary]
    
                        this.currentSynopsis = this.synopses[synopsisIndex]
                        this.currentTranslation = this.currentSynopsis.translation
                        router.push({ name: router.currentRoute.value.name as string });
                        return
                    }
                }
            })
        },
        changeTranslation(translation: string) {
        this.loading(() => 
            {
                for (let synopsisIndex = 0; synopsisIndex < this.synopses.length; synopsisIndex++) {
                    if (this.synopses[synopsisIndex].translation == translation) {
                        this.currentSynopsis = this.synopses[synopsisIndex]
                        this.currentTranslation = translation
                        router.push({ name: router.currentRoute.value.name as string });
                        return
                    }
                }
            })
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
                    return
                }
            }
        },
        setupTranslation(translation: string | string[], options : { [key: string]: string[] }) {
            if (!translation && !this.currentTranslation)
            {
                this.currentTranslation = options[this.currentLanguage][0]
                return
            }
            for (let synopsisIndex = 0; synopsisIndex < this.synopses.length; synopsisIndex++) {
                if (translation === this.synopses[synopsisIndex].translation) {
                    this.currentTranslation = translation
                    this.currentSynopsis = this.synopses[synopsisIndex]
                    return
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
        },
        pushToHistoryAndRedirect(pushToHistoryRoute: RouteLocationRaw, redirectRoute: RouteLocationRaw): void {
            router.push(pushToHistoryRoute)
            .then(
              () => {
                router.push(redirectRoute)
              }
            )
        },
        delayedRender(index: number, preRender: () => void) {
            preRender()
            if (index < this.currentSynopsis.parts.length) {
              setTimeout(() => {
                this.delayedRender(index + 1, preRender);
              }, 0);
            }
        },
        async getDailyGospel(date: Date) : Promise<void> {
            if (this.dailyGospel === null)
            {
                const dailyGospel = await fetchDailyGospel(date);
                const dailyGospelCitation : QuoteScheme = parseCitation(dailyGospel.passage)
                this.dailyGospel = dailyGospelCitation;
                console.log(dailyGospelCitation)
                
                for (let i = 0; i < this.currentSynopsis.parts.length; i++) {
                    const part: PartScheme = this.currentSynopsis.parts[i]
                    for (let j = 0; j < part.sections.length; j++) {
                        const section: SectionScheme = part.sections[j]
                        for (let l = 0; l < section[dailyGospelCitation.evangelist as keyof SectionScheme].length; l++) {
                            const citation = section[dailyGospelCitation.evangelist as keyof SectionScheme][l] as CitationScheme
                            if (citation?.leading) {
                                for (let m = 0; m < citation.content.length; m++) {
                                    const content = citation.content[m]
                                    const formattedVerse = content.verse.slice(-1) === "a" || content.verse.slice(-1) === "b" ? content.verse.slice(0, -1) : content.verse
                                    if (content.chapter === dailyGospelCitation.start.chapter && formattedVerse === dailyGospelCitation.start.verse) {
                                        this.dailyGospelSections.push(section.id)
                                        this.dailyGospel.evangelist = dailyGospelCitation.evangelist
                                    }
                                    else if (this.dailyGospelSections.length > 0 && !this.dailyGospelSections.includes(section.id) ) {
                                        this.dailyGospelSections.push(section.id)
                                    }
                                    if (content.chapter === dailyGospelCitation.end.chapter && formattedVerse === dailyGospelCitation.end.verse) {
                                        return
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },
        //TODO: quote? what is citation, what is quote, what is verse?
        isQuoteInDailyGospel(evangelist: string, chapter: string, verse: string){
            if (this.dailyGospel && this.dailyGospel.evangelist === evangelist)
            {                
                const quoteChapter = parseInt(chapter, 10);
                const quoteVerse = parseInt(verse.replace(/[^\d]/g, ""), 10);
                const startChapter = parseInt(this.dailyGospel.start.chapter, 10);
                const startVerse = parseInt(this.dailyGospel.start.verse, 10);
                const endChapter = parseInt(this.dailyGospel.end.chapter, 10);
                const endVerse = parseInt(this.dailyGospel.end.verse, 10);
            
                if (quoteChapter < startChapter || quoteChapter > endChapter) {
                    return false;
                }
            
                if (quoteChapter === startChapter && quoteVerse < startVerse) {
                    return false;
                }
            
                if (quoteChapter === endChapter && quoteVerse > endVerse) {
                    return false;
                }

                return true
            }
        }
    }
})