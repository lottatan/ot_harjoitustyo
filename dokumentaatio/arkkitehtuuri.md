# Arkkitehtuuri

User interface vastaa käyttöliittymästä. Se sisältää tiedostot, joissa on sisäänkirjautumissivun,
käyttäjänluontisivun, sekä budjetti- ja ostosnäkymät. Services puolestaan vastaa sovelluslogiikasta 
ja repositories nimensä mukaan repositorioista. Siellä on tallennettuna käyttäjätiedot, sekä heidän 
budjettiinsa liittyvät tiedot. Entities sisältää käyttäjätiedoston, jota repositoriot muun muassa hyödyntävät.

![Screenshot from 2022-04-12 14-33-38](https://user-images.githubusercontent.com/96332972/162951455-54bb2406-830a-4327-8935-193eec9b02b2.png)


## Käyttöliittymä

Käyttöliittymässä on 4 erillistä näkymää: 1) Sisäänkirjautuminen, 2) Uuden käyttäjän luonti, 3) Budjettinäkymä, 4) Ostosten muokkaamisikkuna


## Sovelluslogiikka

Sovelluksessa on kaksi tietokantaa, jossa toinen pitää kirjaa käyttäjistä ja toinen käyttäjiin liittyvistä ostoksista. Ostoksen ominaisuuksia 
joita otetaan talteen ovat kategoria, hinta, ostoksen nimi / tyyppi ja käyttäjänimi.

![Screenshot from 2022-05-02 11-11-10](https://user-images.githubusercontent.com/96332972/166204313-8d3f59a5-8dae-472d-aa7b-89d2f2543f4d.png)


BudgetServices tiedoston metodit hyödyntävät näitä repositorioita.

Käyttäjiin liittyvät metodit ovat nimeltään login, create_user, get_current_user, set_new_budget ja delete_user.

Ostoksiin liittyvät metodit ovat nimeltään add_purchase, show_all_purchases ja delete_all_purchases.

Ostoksiin liittyvissä metodeissa annetaan aina parametriksi käyttäjänimi.

![Screenshot from 2022-05-02 13-45-56](https://user-images.githubusercontent.com/96332972/166222558-cd0e6848-d5c2-4ff6-af1b-e1b0c9e48086.png)



## Tietojen tallennus tietokantoihin

Sovellus tallentaa tiedot sekä ostoksista että käyttäjistä SQLite-tietokantaan. Ostokset tallennetaan tauluun Purchases ja käyttäjät tauluun Users.
Molemmat tietokannat ovat konfiguroitu samaan verkkoyhteyteen.


## Päätoiminnallisuudet

### Käyttäjän luominen

![Screenshot from 2022-05-03 14-25-58](https://user-images.githubusercontent.com/96332972/166447095-f9cc13b7-daa8-477c-9959-846bba0e8183.png)

### Sisäänkirjautuminen

![Screenshot from 2022-05-03 14-32-25](https://user-images.githubusercontent.com/96332972/166447136-89dcd7fe-2193-4708-b2dd-b72b101c1ce8.png)


### Budjetin päivittäminen

![Screenshot from 2022-05-03 14-40-43](https://user-images.githubusercontent.com/96332972/166447172-215cca55-eacc-4be4-ae31-dd0b5ba7fcde.png)
