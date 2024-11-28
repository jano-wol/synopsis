export interface DictionaryScheme {
    menu: MenuScheme,
    tooltips: TooltipsScheme,
    notFound: NotFoundScheme,
    error: ErrorScheme
}

interface MenuScheme {
    synopsis: string,
    index: string,
    about: string, 
    sources: string, 
    contact: string,
    dailyGospel: string,
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

interface NotFoundScheme {
    notFound: string 
}

interface ErrorScheme {
    server: string,
    date: string
}


