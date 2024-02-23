# Synopsis

## Requirements
- [x] Primary parallels in `.json` format (SZIT translation)
- [x] Main page (Synopsis)
    - [x] Main title
    - [x] Four gospel columns
    - [x] Evangelist name and citation always seen
    - [x] Chapters, sections, subsections, citations
    - [x] See gospels with primary parallels
- [x] Description page
- [x] Index page (table of contents)
- [x] Details page
    - [x] Sources
    - [x] Differences compared to the sources, with explanation
- [ ] Page for contributors
    - [x] Github page
    - [x] `.json` source
    - [ ] `.json` scheme
    - [ ] To notice 


## Additionals

- [x] Favicon
- [ ] Responsive view
- [x] Consistent header on every page
- [x] Consistent footer on every page
- [ ] Non-primary parallels
- [x] Links to subsections.
    - [x] `/#:id` anchor links in main page
    - [x] Anchor links in table of content
    - [x] `/:id` URLs for subsection
    - [x] Copy link buttons
- [ ] Daily readings
    - [ ] Highlight citations which contains part of daily reading
    - [ ] `/:date` URLs for each subsection contains part of daily reading of the given date
    - [ ] `/today` URL for each subsection contains part of daily reading
- [ ] Translations
    - [ ] Update geographical and personal names to match with SZIT translation
    - [ ] Adding Károli translation
    - [ ] Adding Polish translation
    - [ ] Creating interface for adding any translation by contributors
    - [ ] Interface for language switching
- [ ] Text box functions
    - [ ] Button for leading boxes: jump to following leading box.
    - [ ] Button for other boxes: jump to source leading leading text.
- [ ] Current subsection location visualization on a map

## To-dos
- Check proper ts typing everywhere
- Correct copy to clipboard on `/:id` subsection pages
- Substitute databas `.json` keys with better names

## Project Setup

```sh
npm install
```

### Compile and Hot-Reload for Development

```sh
npm run dev
```

### Type-Check, Compile and Minify for Production

```sh
npm run build
```

### Lint with [ESLint](https://eslint.org/)

```sh
npm run lint
```
