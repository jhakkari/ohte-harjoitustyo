### Käyttöohje

Lataa projektin viimeisin [Loppupalautus release](https://github.com/jhakkari/ohte-harjoitustyo/releases/tag/loppupalautus)

## Ohjelman käynnistäminen

1. Ennen käynnistämistä, asenna riippuvuudet komennolla:

```bash
poetry install
```

2. Ohjelman tietokanta tulee myös alustaa komennolla:

```bash
poetry run invoke db
```

3. Käynnistä sovellus komennolla:

```bash
poetry run invoke start
```