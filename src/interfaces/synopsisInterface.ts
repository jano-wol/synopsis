export interface SynopsisScheme {
    heading: string,
    subheading: string,
    name: string,
    language: string,
    translation: string,
    parts: PartScheme[],
    evangelists: EvangelistsScheme
}

export interface EvangelistsScheme {
    mt: string, 
    mk: string, 
    lk: string, 
    jn: string 
}

export interface PartScheme {
    part_title: string
    sections: SectionScheme[]
}


export interface SectionScheme {
    id: string
    section_title: string
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