export interface DailyGospelScheme {
    passage: string;
}

interface VerseScheme {
    chapter: string;
    verse: string;
}

export interface QuoteScheme {
    evangelist: string,
    start: VerseScheme
    end: VerseScheme
}
