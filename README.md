# ajanvaraus-laakarille

LOPPUPALAUTUS
- rajoitetun ajan ja muiden tenttien takia aika jäi rajalliseksi loppupalautuksen suhteen
- yritin parhaani huomioida viimeisen välipalautuksen arvioinnin seikkoja CSRF haavoittuvuuden ja schema.sql tiedoston suhteen mutta ohjelma ei täysin toimi
- ennen muutoksia sain omalla koneella toimimaan päivämäärän valintaan asti, johon jäin viimeiseen välipalautukseen (tämä siis oli kun pyöritin ohjelmaa omalla koneella olevalta tietokannalta)
- nyt ohjelma selviää kaupunginvalintaan, mutta mitään kaupunkeja ei tule valittavaksi eli ongelma on nimenomaan tietokannasta hakemisessa yms?
- alunperin schema.sql oli tehty sql dump metodilla mutta tämän toimintaa en tajunnut kokeilla kun pyöritin ohjelmaa oman koneen tietokannasta
- koodissa näkyy yritykseni toteuttaa CSRF haavoittuvuuden korjaus ja muutettu schema.sql tiedosto
- yritin myös lisäillä virheviestejä flaskin flash viesteillä mutta sen toteutus takkuili

- jos projekti ei riitä kurssin läpäisemiseen niin pyydän hieman lisäaikaa ongelmien korjailuun

Sovelluksen avulla asiakas voi varata ajan eri lääkärille ja jättää esitietoja tapaamiseen liittyen kommentin muodossa. 

- käyttäjä voi kirjautua sisään ja ulos sekä luoda tunnuksen
- käyttäjä valitsee alueen palvelupaikoista ja lääkärin toimialan, joista avautuu lääkärit ja heidän vapaat ajat
    - onko väliä jos toimialaa ei voi valita vaan palvelupaikan lääkärit avautuisi kerralla kaikki ja tieto toimialasta olisi lääkärin nimen yhteydessä?
- varauksen yhteydessä käyttäjä voi antaa esitietoja (viestin) liittyen lääkärissä asiointiin
- varauksen tehtäessä tietokanta päivittyy ja ottaa varatun ajan pois vapaista ajoista
    - yksi lääkäri voi olla esim. yleislääkäri + erikoistunut johonkin tiettyyn toimialaan jolloin ajanvaraus muuttaa kyseisen lääkärin vapaita aikoja kaikilla toimialoillaan
- käyttäjä voi muokata varausta tiettyyn aikaväliin asti esim. 24h ennen varatun ajan alkua
    - muokata = perua/vaihtaa toiseen aikaan
 

# käynnistys

1. mkdir app
2. cd app
3. git init
4. git clone https://github.com/juhok00/ajanvaraus-laakarille
5. cd ajanvaraus-laakarille
6. python3 -m venv venv
7. source venv/bin/activate
8. pip install -r ./requirements.txt
9. psql < schema.sql
10. flask run



# välipalautus 2

- sovellukselle on luotu sql-taulukot ja ne on täytetty tarvittavilla tiedoilla
- kaksi ensimmäistä templatea on saanut vähän alustavaa muotoa, eli welcome.html (kirjautuminen/rekisteröinti) ja location.html (toimipisteen valinta)
- muutama moduuli on saanut muotoa nyt alkuun kirjautumista/rekisteröintiä silmällä pitäen

- vähän on vielä python tiedostojen yhdistelyssä ymmärtämistä, aloin aluksi tekemään yksittäistä app.py tiedostoa mihin laittaisin kaikki kunnes tajusin, että vaatimuksina oli moduulit


- nyt rekisteröityminen/kirjautuminen on saatu toimimaan ja salasana tallennetaan users taulukkoon hajautusarvona



# välipalautus 3

- sovellus on saamassa lopullista muotoaan mutta toiminta takkuilee siirryttäessä päivämäärän valinnasta ajankohdan valintaan (työn alla)
- myös schema.sql tiedosto aiheuttaa itsellä ongelmia
