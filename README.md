# **Budjettisovellus**
Budjettisovelluksen tarkoituksena on päästä kirjaamaan omia menoja ja laskemaan yhteiskulutuksen määrä. Käyttäjä voi asettaa itselleen budjetin ja sovellus näyttää, kuinka suuren osan siitä on jo käyttänyt
ja kuinka paljon sitä on vielä jäljellä

### **Dokumentaatiotiedoston linkkejä**

[vaatimusmäärittely](https://github.com/lottatan/ot_harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[työaikakirjanpito](https://github.com/lottatan/ot_harjoitustyo/blob/master/dokumentaatio/ty%C3%B6aikakirjanpito.md)

[changelog](https://github.com/lottatan/ot_harjoitustyo/blob/master/dokumentaatio/changelog.md)

[arkkitehtuuri](https://github.com/lottatan/ot_harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

[releaset](https://github.com/lottatan/ot_harjoitustyo/releases/tag/viikko5)

[käyttöohje](https://github.com/lottatan/ot_harjoitustyo/blob/master/dokumentaatio/k%C3%A4ytt%C3%B6ohje.md)

### **Asennusohjeet**

1. Aloita asentamalla riippuvuudet koneella, ajamalla seuraava komento koneen terminaalissa:

```bash
poetry install
```

2. Sovelluksen voit käynnistää ajamalla seuraava komento koneen terminaalissa:

```bash
poetry run invoke start
```

### **Testaaminen**

Aloita testaaminen ajamalla seuraava komento koneen terminaalissa:

```bash
poetry run invoke test
```

### **Testikattavuus**

Tutki testikattavuutta ajamalla seuraava komento koneen terminaalissa:

```bash
poetry run invoke coverage-report
```
Tämän jälkeen htmlcov-kansiosta löytyy testikattavuusraportti index.html-tiedostosta.

### **Pylint**

```bash
poetry run invoke lint
```
