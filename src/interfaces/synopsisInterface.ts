export interface SynopsisScheme {
    chapters: ChapterScheme[]
}

export interface ChapterScheme {
    chapter_name: string
    sections: SectionScheme[]
}

export interface SectionScheme {
    section_name: string | null
    subsections: SubsectionScheme[]
}

export interface SubsectionScheme {
    number: string
    subsection_name: string
    Mt: (CitationScheme | null)[]
    Mk: (CitationScheme | null)[]
    Lk: (CitationScheme | null)[]
    Jn: (CitationScheme | null)[]
}

export interface CitationScheme {
    citation: string
    primary: boolean
    leading: boolean
    content: ContentScheme[]

}

export interface ContentScheme {
    text: string | null
    chapter: string
    verse: string
}