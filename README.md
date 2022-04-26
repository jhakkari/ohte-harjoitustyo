# Ohjelmistotekniikka, harjoitustyö

Sovelluksen avulla on mahdollista pitää kirjaa suorittamistaan kursseista ja niistä kerryttämistä opintopisteistä.

## Dokumentaatio
- [Viikko 5 release](https://github.com/jhakkari/ohte-harjoitustyo/releases/tag/viikko5)
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

Testikattavuusraportti: poetry run invoke coverage-report

Pylint: poetry run invoke lint
