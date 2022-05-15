# Ohjelmistotekniikka, harjoitustyö

Sovelluksen avulla on mahdollista pitää kirjaa suorittamistaan kursseista, niihin kuluneesta ajasta ja kurssien kerryttämistä opintopisteistä.

## Dokumentaatio
- [Käyttöohje](https://github.com/jhakkari/ohte-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)
- [Loppupalautus release](https://github.com/jhakkari/ohte-harjoitustyo/releases/tag/loppupalautus)
- [Vaatimusmäärittely](https://github.com/jhakkari/ohte-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](https://github.com/jhakkari/ohte-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)
- [Changelog](https://github.com/jhakkari/ohte-harjoitustyo/blob/master/dokumentaatio/changelog.md)

## Asennus

1. Asenna riippuvuudet komennolla:

```bash
poetry install
```

2. Alusta tietokanta komennolla:

```bash
poetry run invoke db
```

3. Käynnistä sovellus komennolla:

```bash
poetry run invoke start
```

## Muut komennot

1. Testikattavuusraportti:
```bash
poetry run invoke coverage-report
```

2. Pylint:
```bash
poetry run invoke lint
```
