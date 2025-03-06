export interface GospelScheme {
    color: string;
    gospel: QuoteScheme;
}

interface VerseScheme {
    chapter: string;
    verse: string;
}

interface QuoteIntervalScheme {
    start: VerseScheme
    end: VerseScheme
}

export interface QuoteScheme {
    evangelist: string,
    intervals: QuoteIntervalScheme[]
    start: VerseScheme
    end: VerseScheme
}

