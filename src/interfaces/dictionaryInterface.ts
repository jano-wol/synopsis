export interface DictionaryScheme {
    menu: MenuScheme,
    tooltips: TooltipsScheme,
    index: IndexScheme,
    notFound: NotFoundScheme
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

interface IndexScheme {
    title: string 
}

interface NotFoundScheme {
    notFound: string 
}


