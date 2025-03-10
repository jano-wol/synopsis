import { ref, onMounted, nextTick } from 'vue';
import { defineStore } from 'pinia'
import type { CitationScheme, PartScheme, SectionScheme, SynopsisScheme } from '@/interfaces/synopsisInterface'
import type { DictionaryScheme } from '@/interfaces/dictionaryInterface'
import router from '../router';
import type { RouteLocationRaw } from 'vue-router';

import { fetchGospel, isValidDate} from '@/utils/calendarGospel';


import synopsisSZIT from '@/assets/translations/szit.json'
import synopsisESV from '@/assets/translations/esv.json'
import dictionaryEn from '@/assets/languages/en.json'
import dictionaryHu from '@/assets/languages/hu.json'
import type { QuoteScheme } from '@/interfaces/dailyGospelInterface';
import { ErrorCode } from '@/enums/ErrorCode';
import { options } from '@/utils/options';

export const useSynopsisStore = defineStore('synopsis', {
    state: () => {
        return {
            currentDictionary: dictionaryHu,
            currentLanguage: "hu",
            currentTranslation: "",
            currentSynopsis: synopsisSZIT,
            dictionary: {
               hu: dictionaryHu as DictionaryScheme,
               en: dictionaryEn as DictionaryScheme
            },
            synopses: [
                synopsisSZIT as SynopsisScheme,
                synopsisESV as SynopsisScheme,
            ],
            isLoading: false,
            date: new Date().toISOString().split('T')[0],
            color: null as null | string,
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
                const part : PartScheme = this.currentSynopsis.parts[i]
                for (let j = 0; j < part.sections.length; j++) {
                    const section = part.sections[j][evangelist as keyof SectionScheme] as CitationScheme[]
                    for (let k = 0; k < section.length; k++)
                    {
                        if (section[k]?.leading)
                        {
                            const content = section[k].content;
                            for (let l = 0; l < content.length; l++)
                            {
                                 // TODO: simple Lk 9,43 not working (in interval it's working properly)
                                if (
                                    content[l].chapter == chapter  
                                    && (content[l].verse == verse
                                    || content[l].verse == verse + 'a'
                                    || content[l].verse == verse + 'b')
                                ) {
                                    return content[l].verse
                                }
                            }
                        }
                    }
                }
            }
            const match = verse.match(/^\d+/); 
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
        async getGospel(date: string) : Promise<void> {
            if (!isValidDate(date))
            {
                this.error = ErrorCode.DATE
                return
            }
            useSynopsisStore().error = null



            

            // TODO: reduce try block length            
            try{
                if ((router.currentRoute.value.name === "today") || router.currentRoute.value.name === "calendar")
                {
                    this.isLoading = true
                }

                const  gospelInfo = await fetchGospel(new Date(date));
                const  gospel = gospelInfo.gospel
                this.color = gospelInfo.color
                this.date = date
                this.dateGospelSections = []
                
                this.isLoading = false
                for (let i = 0; i<gospel.intervals.length; i++)
                {
                    gospel.intervals[i].start.verse = this.formatVerse(gospel.evangelist, gospel.intervals[i].start.chapter, gospel.intervals[i].start.verse)
                    gospel.intervals[i].end.verse = this.formatVerse(gospel.evangelist, gospel.intervals[i].end.chapter, gospel.intervals[i].end.verse)
                }
                    this.dateGospel = gospel
                    // TODO: duplicated functions in isInQuote
                    const parseChapterVerse = (chapter: string, verse: string) => {
                    const chapterNumber = parseInt(chapter, 10);
                    const match = verse.match(/^(\d+)([a-z]?)$/);

                    if (isNaN(chapterNumber) || !match) {
                        return { chapter: Infinity, verse: Infinity, letter: "" };
                    }

                    return {
                        chapter: chapterNumber,
                        verse: parseInt(match[1], 10),
                        letter: match[2] || ""
                    };
                 };

                //TODO: similar function used in isQuoteInGospel
                const compareChapterVerses = (
                    cv1: { chapter: number; verse: number; letter: string },
                    cv2: { chapter: number; verse: number; letter: string }
                ) => {
                    if (cv1.chapter !== cv2.chapter) return cv1.chapter - cv2.chapter;
                    if (cv1.verse !== cv2.verse) return cv1.verse - cv2.verse;
                    return cv1.letter.localeCompare(cv2.letter);
                };
            
                for ( let n = 0 ; n < gospel.intervals.length; n ++)
                {
                    for (let i = 0; i < this.currentSynopsis.parts.length; i++) {
                        const part: PartScheme = this.currentSynopsis.parts[i]
                        for (let j = 0; j < part.sections.length; j++) {
                            const section: SectionScheme = part.sections[j]
                            for (let l = 0; l < section[gospel.evangelist as keyof SectionScheme].length; l++) {
                                const citation = section[gospel.evangelist as keyof SectionScheme][l] as CitationScheme
                                if (citation?.leading) {
                                    for (let m = 0; m < citation.content.length; m++) {
                                        const content = citation.content[m]
                                        
                                        const contentQuote = parseChapterVerse(content.chapter, content.verse);
                                        const gospelStartQuote = parseChapterVerse(gospel.intervals[n].start.chapter, gospel.intervals[n].start.verse);
                                        const gospelEndQuote = parseChapterVerse(gospel.intervals[n].end.chapter, gospel.intervals[n].end.verse);

                                        if (
                                            compareChapterVerses(gospelStartQuote, contentQuote) <= 0 
                                            && 
                                            compareChapterVerses(contentQuote, gospelEndQuote) <= 0  
                                            &&
                                            !this.dateGospelSections.includes(section.id) 
                                        ){
                                            this.dateGospelSections.push(section.id)
                                        }
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
        isQuoteInGospel(evangelist: string, chapter: string, verse: string){
            let gospel = this.dateGospel
            if (gospel && gospel.evangelist === evangelist)
            {       
                const parseChapterVerse = (chapter: string, verse: string) => {
                    const chapterNumber = parseInt(chapter, 10);
                    const match = verse.match(/^(\d+)([a-z]?)$/);

                    if (isNaN(chapterNumber) || !match) {
                        return { chapter: Infinity, verse: Infinity, letter: "" };
                    }

                    return {
                        chapter: chapterNumber,
                        verse: parseInt(match[1], 10),
                        letter: match[2] || ""
                    };
                 };
            
                const compareChapterVerses = (
                    cv1: { chapter: number; verse: number; letter: string },
                    cv2: { chapter: number; verse: number; letter: string }
                ) => {
                    if (cv1.chapter !== cv2.chapter) return cv1.chapter - cv2.chapter;
                    if (cv1.verse !== cv2.verse) return cv1.verse - cv2.verse;
                    return cv1.letter.localeCompare(cv2.letter);
                };

                
                const parsedQuote = parseChapterVerse(chapter, verse);
                for (let i = 0; i < gospel.intervals.length; i++)
                    {
                    const parsedStart = parseChapterVerse(gospel.intervals[i].start.chapter, gospel.intervals[i].start.verse);
                    const parsedEnd = parseChapterVerse(gospel.intervals[i].end.chapter, gospel.intervals[i].end.verse);

                    if (compareChapterVerses(parsedQuote, parsedEnd) <= 0 && compareChapterVerses(parsedQuote, parsedStart) >= 0) {
                        return true;
                    }
                }

                return false;
            }
        },
        getTranslationsList(){
            const translationsToLoad : string[]  = Object.values(options)
            .flat()
            .map((value) => value);
            return translationsToLoad
        },
        sortTranslaions(){
            const translations = this.getTranslationsList()
            this.synopses.sort((a, b) => {
                const indexA = translations.indexOf(a.translation);
                const indexB = translations.indexOf(b.translation);
                return (indexA === -1 ? Number.MAX_VALUE : indexA) - (indexB === -1 ? Number.MAX_VALUE : indexB);
              });
        },
        async loadSynopsis(translation : string)
        {
            const synopsis = (await import(`@/assets/translations/${translation}.json`)).default;
            this.synopses.push(synopsis)
            this.sortTranslaions()
        },
        async loadSynopses() {
            const translationsToLoad = this.getTranslationsList()
            if (this.synopses.length < translationsToLoad.length)
            {
                for (const path of translationsToLoad) {
                    try {
                    const translation = (await import(`@/assets/translations/${path.toLowerCase()}.json`)).default;
                    if (!this.synopses.includes(translation)) {
                        this.synopses.push(translation);
                        this.sortTranslaions()
                    }
                    } catch (error) {
                    console.error(`Error loading translation from ${path.toLowerCase()}:`, error);
                    }
                }
            }
        },
    }
})