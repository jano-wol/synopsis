import { ref, onMounted, nextTick } from 'vue';
import { defineStore } from 'pinia'
import type { CitationScheme, PartScheme, SectionScheme, SynopsisScheme } from '@/interfaces/synopsisInterface'
import type { DictionaryScheme } from '@/interfaces/dictionaryInterface'
import router from '../router';
import type { RouteLocationRaw } from 'vue-router';

import { fetchGospel, isValidDate} from '@/utils/calendarGospel';


import synopsisSZIT from '@/assets/translations/szit.json'
import synopsisKG from '@/assets/translations/kg.json'
import synopsisKNB from '@/assets/translations/knb.json'
import synopsisRUF from '@/assets/translations/ruf.json'
import synopsisESV from '@/assets/translations/esv.json'
import synopsisEU from '@/assets/translations/eu.json'
import synopsisBT from '@/assets/translations/bt.json'
import synopsisBJW from '@/assets/translations/bjw.json'
import synopsisRSP from '@/assets/translations/rsp.json'
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
                synopsisSZIT as SynopsisScheme,
                synopsisKG as SynopsisScheme,
                synopsisKNB as SynopsisScheme,
                synopsisRUF as SynopsisScheme,
                synopsisESV as SynopsisScheme,
                synopsisEU as SynopsisScheme,
                synopsisBT as SynopsisScheme,
                synopsisBJW as SynopsisScheme,
                synopsisRSP as SynopsisScheme,
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
            useSynopsisStore().error = null



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

                const  dailyGospel = await fetchGospel(new Date(date));
                this.isLoading = false
                const gospel = dailyGospel.gospel
                for (let i = 0; i<gospel.intervals.length; i++)
                {
                    gospel.intervals[i].start.verse = this.formatVerse(gospel.evangelist, gospel.intervals[i].start.chapter, gospel.intervals[i].start.verse)
                    gospel.intervals[i].end.verse = this.formatVerse(gospel.evangelist, gospel.intervals[i].end.chapter, gospel.intervals[i].end.verse)
                }
                if (isDaily)
                {
                    this.dailyGospel = gospel
                }
                else {
                    this.dateGospel = gospel
                }
                    // TODO: duplicated functions in isInQuote
                    const parseChapterVerse = (chapter: string, verse: string) => {
                    const chapterNumber = parseInt(chapter, 10);
                    const match = verse.match(/^(\d+)([a-z]?)$/);

                    if (isNaN(chapterNumber) || !match) {
                        return { chapter: Infinity, verse: Infinity, letter: "" }; // Invalid input fallback
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
                    if (cv1.chapter !== cv2.chapter) return cv1.chapter - cv2.chapter;  // Compare chapters
                    if (cv1.verse !== cv2.verse) return cv1.verse - cv2.verse;          // Compare verses
                    return cv1.letter.localeCompare(cv2.letter);                        // Compare optional letters
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
                                            !gospelSections.includes(section.id) 
                                        ){
                                            gospelSections.push(section.id)
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
        isQuoteInGospel(evangelist: string, chapter: string, verse: string, isDaily : boolean = true){
            let gospel = this.dailyGospel
            if (!isDaily) {
                gospel = this.dateGospel
            }
            if (gospel && gospel.evangelist === evangelist)
            {       
                const parseChapterVerse = (chapter: string, verse: string) => {
                    const chapterNumber = parseInt(chapter, 10);
                    const match = verse.match(/^(\d+)([a-z]?)$/);

                    if (isNaN(chapterNumber) || !match) {
                        return { chapter: Infinity, verse: Infinity, letter: "" }; // Invalid input fallback
                    }

                    return {
                        chapter: chapterNumber,            // Parsed chapter number
                        verse: parseInt(match[1], 10),     // Parsed verse number
                        letter: match[2] || ""             // Parsed optional letter
                    };
                 };
            
                const compareChapterVerses = (
                    cv1: { chapter: number; verse: number; letter: string },
                    cv2: { chapter: number; verse: number; letter: string }
                ) => {
                    if (cv1.chapter !== cv2.chapter) return cv1.chapter - cv2.chapter;  // Compare chapters
                    if (cv1.verse !== cv2.verse) return cv1.verse - cv2.verse;          // Compare verses
                    return cv1.letter.localeCompare(cv2.letter);                        // Compare optional letters
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
        }
    }
})