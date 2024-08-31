# Synopsis
Website for the parallel Gospels of Matthew, Mark, Luke and John.

Running on [synopticus.org](https://www.synopticus.org/).

## Contribution
The two main field of upcoming develeopment are 
- Adding new Gospel translations
- Adding daily reading option
    - Highlight citations which contains part of daily reading
    - `/:date` URLs for each subsection contains part of daily reading of the given date
    - `/today` URLs for each subsection contains part of daily reading

All help is welcome!

## Dependencies

npm

<!-- 
## To-dos
- Check proper ts typing everywhere
- Substitute database `.json` keys with better names -->

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
