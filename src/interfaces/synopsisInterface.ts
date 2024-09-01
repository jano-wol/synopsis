export interface SynopsisScheme {
    language: string,
    translation: string,
    parts: PartScheme[]
}

export interface PartScheme {
    part_title: string
    subparts: SubpartScheme[]
}

export interface SubpartScheme {
    subpart_title: string | null
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
    leading: boolean
    content: ContentScheme[]

}

export interface ContentScheme {
    text: string | null
    chapter: string
    verse: string
}