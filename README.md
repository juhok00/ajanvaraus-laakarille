# ajanvaraus-laakarille

Sovelluksen avulla asiakas voi varata ajan eri lääkärille ja jättää esitietoja tapaamiseen liittyen kommentin muodossa. 

- käyttäjä voi kirjautua sisään ja ulos sekä luoda tunnuksen
- käyttäjä valitsee alueen palvelupaikoista ja lääkärin toimialan, joista avautuu lääkärit ja heidän vapaat ajat
    - onko väliä jos toimialaa ei voi valita vaan palvelupaikan lääkärit avautuisi kerralla kaikki ja tieto toimialasta olisi lääkärin nimen yhteydessä?
- varauksen yhteydessä käyttäjä voi antaa esitietoja (viestin) liittyen lääkärissä asiointiin
- varauksen tehtäessä tietokanta päivittyy ja ottaa varatun ajan pois vapaista ajoista
    - yksi lääkäri voi olla esim. yleislääkäri + erikoistunut johonkin tiettyyn toimialaan jolloin ajanvaraus muuttaa kyseisen lääkärin vapaita aikoja kaikilla toimialoillaan
- käyttäjä voi muokata varausta tiettyyn aikaväliin asti esim. 24h ennen varatun ajan alkua
    - muokata = perua/vaihtaa toiseen aikaan



# välipalautus 2

- sovellukselle on luotu sql-taulukot ja ne on täytetty tarvittavilla tiedoilla
- kaksi ensimmäistä templatea on saanut vähän alustavaa muotoa, eli welcome.html (kirjautuminen/rekisteröinti) ja location.html (toimipisteen valinta)
- muutama moduuli on saanut muotoa nyt alkuun kirjautumista/rekisteröintiä silmällä pitäen

- vähän on vielä python tiedostojen yhdistelyssä ymmärtämistä, aloin aluksi tekemään yksittäistä app.py tiedostoa mihin laittaisin kaikki kunnes tajusin, että vaatimuksina oli moduulit


- nyt rekisteröityminen/kirjautuminen on saatu toimimaan ja salasana tallennetaan users taulukkoon hajautusarvona



# välipalautus 3

- sovellus on saamassa lopullista muotoaan mutta toiminta takkuilee siirryttäessä päivämäärän valinnasta ajankohdan valintaan (työn alla)
- myös schema.sql tiedosto aiheuttaa itsellä ongelmia (ilmeisesti sen takia, että koneellani on jo taulut muodostettuna)
