export interface SynopsisScheme {
    language: string,
    translation: string,
    chapters: ChapterScheme[]
}

export interface ChapterScheme {
    chapter_name: string
    subchapters: SubchapterScheme[]
}

export interface SubchapterScheme {
    subchapter_name: string | null
    sections: SectionScheme[]
}

export interface SectionScheme {
    id: string
    section_name: string
    mt: (CitationScheme | null)[]
    mk: (CitationScheme | null)[]
    lk: (CitationScheme | null)[]
    jn: (CitationScheme | null)[]
}

export interface CitationScheme {
    citation: string
    leading: boolean
    content: ContentScheme[]

}

export interface ContentScheme {
    text: string | null
    chapter: string
    verse: string
}