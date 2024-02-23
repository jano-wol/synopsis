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
    id: string
    subsection_name: string
    mt: (CitationScheme | null)[]
    mk: (CitationScheme | null)[]
    lk: (CitationScheme | null)[]
    jn: (CitationScheme | null)[]
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