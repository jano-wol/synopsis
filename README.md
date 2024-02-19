# Synopsis

## Requirements
- [x] Primary parallels in `.json` format (SZIT translation)
- [ ] Main page
    - [x] Main title
    - [ ] Description
    - [x] Four gospel columns
    - [x] Evangelist name and citation always seen
    - [x] Chapters, sections, subsections, citations
    - [x] See gospels with primary parallels
- [x] Index page (table of contents)
- [ ] Details page
    - [ ] Sources
    - [ ] Differences compared to the sources, with explanation
    - [ ] Development informations 


## Additionals

- [ ] Favicon
- [ ] Responsive view
- [x] Consistent header on every page
- [x] Consistent footer on every page
- [ ] Non-primary parallels
- [ ] Links to subsections.
    - [ ] Local links in main page (anchor)
    - [ ] `/:id` URLs for subsection
    - [ ] Copy link buttons
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
- [ ] Current subsection location visualization on a map



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
