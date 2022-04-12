# Ohjelmistotekniikka, harjoitustyö

Sovelluksen avulla on mahdollista pitää kirjaa suorittamistaan kursseista ja niistä kerryttämistä opintopisteistä.

## Dokumentaatio

- [Vaatimusmäärittely](https://github.com/jhakkari/ohte-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](https://github.com/jhakkari/ohte-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)
- [Changelog](https://github.com/jhakkari/ohte-harjoitustyo/blob/master/dokumentaatio/changelog.md)

## Asennus

Asenna riippuvuudet komennolla: poetry install

Käynnistä sovellus komennolla: poetry run invoke start

## Muut komennot

Testikattavuusraportti: poetry run invoke coverage-report

Pylint: poetry run invoke lint
