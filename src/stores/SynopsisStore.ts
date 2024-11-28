import { ref, onMounted, nextTick } from 'vue';
import { defineStore } from 'pinia'
import type { CitationScheme, PartScheme, SectionScheme, SynopsisScheme } from '@/interfaces/synopsisInterface'
import type { DictionaryScheme } from '@/interfaces/dictionaryInterface'
import router from '../router';
import type { RouteLocationRaw } from 'vue-router';

import { fetchGospel, isValidDate, parseCitation } from '@/utils/dailyGospel';


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
import { ErrorCode } from '@/enums/ErrorCode';


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
            dateGospel: null as null | QuoteScheme,
            dateGospelSections: [] as Array<string>,
            error: null as null | ErrorCode,
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
        formatVerse(evangelist: string, chapter: string, verse: string): string {
            for (let i = 0; i < this.currentSynopsis.parts.length; i++) {
                const part = this.currentSynopsis.parts[i]
                for (let j = 0; j < part.sections.length; j++) {
                    const section = part.sections[j][evangelist as keyof SectionScheme]
                    for (let k = 0; k < section.length; k++)
                    {
                        // console.log(section[k])
                        if (section[k]?.leading)
                        {
                            const content = section[k].content;
                            // console.log(content)
                            for (let l = 0; l < content.length; l++)
                            {
                                
                                 console.log(verse)
                                 // TODO: simple Lk 9,43 not working (in interval it's working properly)
                                if (
                                    content[l].chapter == chapter  
                                    && (content[l].verse == verse
                                    || content[l].verse == verse + 'a'
                                    || content[l].verse == verse + 'b')
                                ) {
                                    console.log("YY")
                                    console.log("AAAA: " + content[l].verse)
                                    return content[l].verse
                                }
                            }
                        }
                    }
                }
            }
            console.log("ZZ")
            const match = verse.match(/^\d+/); 
            console.log("BBBB: " + ( match ? match[0] : verse))
            return match ? match[0] : verse
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
        async getGospel(date: string, isDaily: boolean = true) : Promise<void> {
            if (this.dailyGospel && isDaily)
            {
                return
            }
            if (!isValidDate(date))
            {
                this.error = ErrorCode.DATE
                return
            }



            let gospelSections = this.dailyGospelSections
            if (!isDaily)
            {
                gospelSections = this.dateGospelSections
            }

            // TODO: reduce try block length            
            try{
                if ((router.currentRoute.value.name === "today") || router.currentRoute.value.name === "calendar")
                {
                    this.isLoading = true
                }
                //TODO: rename to fetchGospel
                let  dailyGospel = await fetchGospel(new Date(date));
                this.isLoading = false
                let gospel =  parseCitation(dailyGospel.passage)
                console.log(gospel)
                gospel.start.verse = this.formatVerse(gospel.evangelist, gospel.start.chapter, gospel.start.verse)
                gospel.end.verse = this.formatVerse(gospel.evangelist, gospel.end.chapter, gospel.end.verse)
                console.log(gospel)
                if (isDaily)
                {
                    this.dailyGospel = gospel
                }
                else {
                    this.dateGospel = gospel
                }
                // console.log(this.dailyGospel)
                // console.log(this.dateGospel)
                
                for (let i = 0; i < this.currentSynopsis.parts.length; i++) {
                    const part: PartScheme = this.currentSynopsis.parts[i]
                    for (let j = 0; j < part.sections.length; j++) {
                        const section: SectionScheme = part.sections[j]
                        for (let l = 0; l < section[gospel.evangelist as keyof SectionScheme].length; l++) {
                            const citation = section[gospel.evangelist as keyof SectionScheme][l] as CitationScheme
                            if (citation?.leading) {
                                for (let m = 0; m < citation.content.length; m++) {
                                    const content = citation.content[m]
                                    if (content.chapter === gospel.start.chapter && content.verse === gospel.start.verse) {
                                        gospelSections.push(section.id)
                                    }
                                    else if (gospelSections.length > 0 && !gospelSections.includes(section.id) ) {
                                        gospelSections.push(section.id)
                                    }
                                    if (content.chapter === gospel.end.chapter && content.verse === gospel.end.verse) {
                                        return
                                    }
                                }
                            }
                        }
                    }
                }
            }
            catch (error) {
                this.isLoading = false
                this.error = ErrorCode.SERVER
            }
        },
        //TODO: quote? what is citation, what is quote, what is verse?
        isQuoteInGospel(evangelist: string, chapter: string, verse: string, isDaily : boolean = true){
            // console.log("ASD")   
            let gospel = this.dailyGospel
            if (!isDaily) {
                gospel = this.dateGospel
            }
            // console.log("HELLO")
            // console.log(gospel)
            if (gospel && gospel.evangelist === evangelist)
            {       
                const parseVerse = (verse: string) => {
                    const match = verse.match(/^(\d+)([a-z]?)$/);
                    if (!match) return { number: Infinity, letter: "" }; // Invalid verse fallback
                    return { number: parseInt(match[1], 10), letter: match[2] || "" };
                };
            
                const compareVerses = (verse1: { number: number; letter: string }, verse2: { number: number; letter: string }) => {
                    if (verse1.number !== verse2.number) return verse1.number - verse2.number;
                    return verse1.letter.localeCompare(verse2.letter);
                };
            
                const quoteChapter = parseInt(chapter, 10);
                const quoteVerse = parseVerse(verse);
                const startChapter = parseInt(gospel.start.chapter, 10);
                const startVerse = parseVerse(gospel.start.verse);
                const endChapter = parseInt(gospel.end.chapter, 10);
                const endVerse = parseVerse(gospel.end.verse);

                
                if (quoteChapter < startChapter || quoteChapter > endChapter) {
                    return false;
                }
                
                
                // console.log(quoteChapter, quoteVerse, startChapter, startVerse)  
            
                if (quoteChapter === startChapter && compareVerses(quoteVerse, startVerse) < 0) {
                    return false;
                }
            
                if (quoteChapter === endChapter && compareVerses(quoteVerse, endVerse) > 0) {
                    return false;
                }
            
                return true;
            }
        }
    }
})