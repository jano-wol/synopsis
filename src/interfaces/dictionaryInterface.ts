export interface DictionaryScheme {
    menu: MenuScheme,
    tooltips: TooltipsScheme,
    evangelists: EvangelistsScheme,
    index: IndexScheme,
    notFound: NotFoundScheme,
    synopsis: SynopsisScheme
}

interface MenuScheme {
    synopsis: string,
    index: string,
    about: string, 
    sources: string, 
    contact: string,
    translations: string
}

interface TooltipsScheme {
    share: string,
    location: string,
    openInSynopsis: string,
    openSeparately: string,
    nextMainText: string,
    previousMainText: string,
    jumpToMainText: string
}

export interface EvangelistsScheme {
    mt: string, 
    mk: string, 
    lk: string, 
    jn: string 
}

interface IndexScheme {
    title: string 
}

interface NotFoundScheme {
    notFound: string 
}

interface SynopsisScheme {
    subheading: string 
}


